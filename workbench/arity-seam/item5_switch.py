"""Item 5: the quantum switch process matrix.

Spaces (order): A_I(2), A_O(2), B_I(2), B_O(2), F_t(2), F_c(2)  -> dim 64.
Past fixed: control |+>, target |psi>. Pure process vector:
 |w> = (1/sqrt2)[ |psi>_{A_I} |I>>_{A_O B_I} |I>>_{B_O F_t} |0>_{F_c}
                + |psi>_{B_I} |I>>_{B_O A_I} |I>>_{A_O F_t} |1>_{F_c} ]
W = |w><w|.  Probability rule Tr[W (M_A (x) M_B (x) E_F)], party ops M = C^T
(transposed-Choi convention fixed in common.py); F is a measure-only party,
whose operator is the POVM element E itself (Choi of measure-and-discard is
E^T, transposed back to E).

(a) validity: W >= 0 (pure); Tr[W (M_A (x) M_B (x) 1_F)] = 1 for random CPTP
    pairs; sanity: F-statistics reproduce physical switch interferometry.
(b) dephasing F_c => exactly (1/2) W^{A<B} + (1/2) W^{B<A}, each a valid
    ordered comb (residuals checked) => causally separable by construction.
(c) SDP: max visibility lam s.t. lam W + (1-lam) 1/16 causally separable
    (= X_{A<B<F} + X_{B<A<F}, each PSD + comb subspace); random robustness
    r = (1-lam)/lam. Witness from SDP dual, spot-checked on random separable W'.
"""
import numpy as np
import cvxpy as cp
from common import I2, random_cptp_kraus, choi_from_kraus, random_instrument_chois

rng = np.random.default_rng(11)
NF = 6
DIMS = [2] * NF
D = 64


def build_branch(psi, order):
    w = np.zeros(DIMS, dtype=complex)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if order == 'AB':   # psi->A_I; A_O=B_I wire; B_O=F_t wire; F_c=|0>
                    w[i, j, j, k, k, 0] += psi[i]
                else:               # psi->B_I; B_O=A_I wire; A_O=F_t wire; F_c=|1>
                    w[k, j, i, k, j, 1] += psi[i]
    return w.reshape(D)


def permute_factors(M, perm, dims):
    n = len(dims)
    Mt = M.reshape(dims + dims)
    return np.transpose(Mt, list(perm) + [p + n for p in perm]).reshape(M.shape)


psi = np.array([1, 0], dtype=complex)
w0 = build_branch(psi, 'AB')
w1 = build_branch(psi, 'BA')
w = (w0 + w1) / np.sqrt(2)
W = np.outer(w, w.conj())
WAB, WBA = np.outer(w0, w0.conj()), np.outer(w1, w1.conj())

print("Tr W_switch =", np.trace(W).real, " (should be d_AO*d_BO = 4); W pure => W >= 0")

# ---- (a) normalization on random CPTP pairs, F traced ----
worst = 0.0
for t in range(200):
    MA = sum(random_instrument_chois(2, nk=int(rng.integers(1, 4)), rng=rng)).T
    MB = sum(random_instrument_chois(2, nk=int(rng.integers(1, 4)), rng=rng)).T
    p = np.trace(W @ np.kron(np.kron(MA, MB), np.eye(4))).real
    worst = max(worst, abs(p - 1))
print(f"(a) max |P-1| over 200 random CPTP pairs (F traced): {worst:.3e}")

U = np.linalg.qr(rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)))[0]
V = np.linalg.qr(rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)))[0]
MA, MB = choi_from_kraus([U]).T, choi_from_kraus([V]).T
out_expected = (np.kron(V @ U @ psi, [1, 0]) + np.kron(U @ V @ psi, [0, 1])) / np.sqrt(2)
rho_exp = np.outer(out_expected, out_expected.conj())
err = 0.0
for t in range(20):
    X = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    E = X @ X.conj().T
    E /= np.linalg.norm(E, 2) * 1.5
    p = np.trace(W @ np.kron(np.kron(MA, MB), E)).real
    err = max(err, abs(p - np.trace(E @ rho_exp).real))
print(f"    interferometric sanity (random U,V; 20 random POVM effects on F_t(x)F_c): max err = {err:.3e}")

# ---- (b) dephasing the control ----
P0 = np.kron(np.eye(32), np.diag([1., 0.]))
P1 = np.kron(np.eye(32), np.diag([0., 1.]))
W_deph = P0 @ W @ P0 + P1 @ W @ P1
print(f"(b) ||W_deph - (1/2 WAB + 1/2 WBA)|| = {np.linalg.norm(W_deph - 0.5*(WAB+WBA)):.3e}")


def tr_repl(M, pos, dims=DIMS):
    pos = sorted(pos)
    keep = [k for k in range(len(dims)) if k not in pos]
    perm = keep + pos
    P = permute_factors(M, perm, dims)
    dk = int(np.prod([dims[k] for k in keep]))
    dt = int(np.prod([dims[k] for k in pos]))
    red = np.einsum('aibi->ab', P.reshape(dk, dt, dk, dt))
    return permute_factors(np.kron(red, np.eye(dt)) / dt, list(np.argsort(perm)), dims)


def comb_residuals(M, first):
    """Comb conditions for order first<second<F on standard factor order."""
    if first == 'A':
        o1, i2, o2 = 1, 2, 3
    else:
        o1, i2, o2 = 3, 0, 1
    F = [4, 5]
    r1 = np.linalg.norm(tr_repl(M, F) - tr_repl(M, F + [o2]))
    r2 = np.linalg.norm(tr_repl(M, F + [i2, o2]) - tr_repl(M, F + [i2, o2, o1]))
    return r1, r2

print("    comb residuals: WAB as A<B<F:", ["%.1e" % r for r in comb_residuals(WAB, 'A')],
      " WBA as B<A<F:", ["%.1e" % r for r in comb_residuals(WBA, 'B')])
print("    => W_deph = 1/2 W^{A<B<F} + 1/2 W^{B<A<F}: causally separable by explicit construction")

# ---- (c) SDP for critical visibility ----
W0 = np.eye(D) / 16.0


def pt_last(Xexpr, dims_list, n_last):
    """partial trace over the last n_last factors."""
    Y = Xexpr
    dims_cur = list(dims_list)
    for _ in range(n_last):
        Y = cp.partial_trace(Y, dims_cur, axis=len(dims_cur) - 1)
        dims_cur = dims_cur[:-1]
    return Y


def comb_cone_constraints(X):
    """X (64x64) is an unnormalized process ordered (f0 f1)<(f2 f3)<F in ITS OWN
    factor ordering (first party = factors 0,1; second = 2,3; F = 4,5)."""
    cons = [X >> 0]
    Y = pt_last(X, [2] * 6, 2)                       # trace F -> on [2,2,2,2]
    Yr = pt_last(Y, [2] * 4, 1)                      # trace second party's output
    cons.append(Y == cp.kron(Yr, np.eye(2)) / 2)     # Tr_F X = W2 (x) 1_{o2}
    Y2 = pt_last(Y, [2] * 4, 2)                      # on [2,2] = first party
    Y2r = pt_last(Y2, [2, 2], 1)
    cons.append(Y2 == cp.kron(Y2r, np.eye(2)) / 2)   # Tr_{i2 o2 F} X = W1 (x) 1_{o1}
    return cons


# permutation matrix mapping (B_I B_O A_I A_O F_t F_c) frame -> standard frame
Pperm = permute_factors(np.eye(D), [2, 3, 0, 1, 4, 5], DIMS)  # careful: build via action on basis
# verify: standard factor k should equal frame factor perm[k]
# We define P such that  X_std = P X_frame P^T. Build P by permuting identity's tensor legs:
def perm_matrix(perm, dims):
    n = len(dims)
    Dtot = int(np.prod(dims))
    P = np.zeros((Dtot, Dtot))
    # basis index in frame ordering -> index in standard ordering
    for idx in range(Dtot):
        # digits of idx in frame ordering
        digs, r = [], idx
        for d in reversed(dims):
            digs.append(r % d)
            r //= d
        digs = digs[::-1]           # frame digits
        std = [digs[perm.index(k)] for k in range(n)] if False else [digs[list(perm).index(k)] for k in range(n)]
        j = 0
        for d, dig in zip(dims, std):
            j = j * d + dig
        P[j, idx] = 1.0
    return P

# frame order for cone B: its factor f is standard factor permB[f]:
permB = [2, 3, 0, 1, 4, 5]
PB = perm_matrix(permB, DIMS)


def solve_visibility(Wtest, solver_eps=1e-8):
    lam = cp.Variable()
    XA = cp.Variable((D, D), hermitian=True)
    XBf = cp.Variable((D, D), hermitian=True)     # cone-B variable in its own frame
    cons = comb_cone_constraints(XA) + comb_cone_constraints(XBf)
    eq = XA + PB @ XBf @ PB.T == lam * Wtest + (1 - lam) * W0
    cons += [eq, lam >= 0, lam <= 1]
    prob = cp.Problem(cp.Maximize(lam), cons)
    prob.solve(solver=cp.SCS, eps=solver_eps, max_iters=200000)
    return lam.value, eq, prob


# sanity of perm matrix: WBA in standard frame should satisfy cone-B constraints,
# i.e. PB^T WBA PB should be a comb in its own frame
chk = PB.T @ WBA @ PB
print("    perm sanity (should be ~0):", ["%.1e" % r for r in comb_residuals(
    permute_factors(chk, [0, 1, 2, 3, 4, 5], DIMS), 'A')])

lam_star, eq, prob = solve_visibility(W)
r = (1 - lam_star) / lam_star
print(f"(c) critical visibility lam* = {lam_star:.6f}   (quoted ~0.388)")
print(f"    random robustness r = (1-lam*)/lam* = {r:.6f}   (quoted ~1.576)")

for name in ["|+>", "Haar"]:
    if name == "|+>":
        ps = np.array([1, 1]) / np.sqrt(2)
    else:
        v = rng.normal(size=2) + 1j * rng.normal(size=2)
        ps = v / np.linalg.norm(v)
    wA, wB = build_branch(ps, 'AB'), build_branch(ps, 'BA')
    Wp = np.outer(wA + wB, (wA + wB).conj()) / 2
    l2, _, _ = solve_visibility(Wp)
    print(f"    target {name}: lam* = {l2:.6f}, r = {(1-l2)/l2:.6f}")

# ---- witness from the dual ----
S = eq.dual_value
S = (S + S.conj().T) / 2
if np.trace(S @ W).real > 0:
    S = -S
print(f"    witness from dual: Tr[S W_switch] = {np.trace(S @ W).real:.6f}  (< 0)")
mins = []
for t in range(300):
    q = rng.uniform()
    Ws = np.zeros((D, D), dtype=complex)
    for order, wgt in [('A', q), ('B', 1 - q)]:
        v = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        rho1 = v @ v.conj().T
        rho1 /= np.trace(rho1)
        C1 = choi_from_kraus(random_cptp_kraus(2, 2, int(rng.integers(1, 5)), rng), 2, 2)
        C2 = choi_from_kraus(random_cptp_kraus(2, 4, int(rng.integers(1, 5)), rng), 2, 4)
        comb = np.einsum('ab,cdef,ghij->acdghbefij',
                         rho1, C1.reshape(2, 2, 2, 2), C2.reshape(2, 4, 2, 4)).reshape(D, D)
        Wc = comb if order == 'A' else PB @ comb @ PB.T
        Ws += wgt * Wc
    mins.append(np.trace(S @ Ws).real)
mins = np.array(mins)
print(f"    spot-check on 300 random causally separable W': min Tr[S W'] = {mins.min():.6e}  (>= 0?)")
print(f"    Tr[S W_deph] = {np.trace(S @ W_deph).real:.6e}   (dephased switch, must be >= 0)")
