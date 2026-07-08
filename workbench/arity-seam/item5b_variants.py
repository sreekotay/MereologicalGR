"""Item 5c variants: critical visibility of the switch under different
choices of which systems are kept in the global future / past.

(i)   bipartite + F = F_t(x)F_c (d_F=4), past fixed |+>,|psi>   [main script]
(ii)  bipartite + F = F_c only (target traced out, d_F=2)
(iii) 4-partite: open past P_O (d=4, control+target), F = F_t(x)F_c (d=4)
(iv)  bipartite + F = F_t only (control traced -> should be SEPARABLE, lam*=1)

Causal separability: W = X_{ord1} + X_{ord2}, each PSD + ordered-comb subspace.
Noise: white noise 1/N with N fixed by unit probability (Tr W0 = Tr W).
"""
import numpy as np
import cvxpy as cp

# ---------- generic helpers ----------

def perm_matrix(perm, dims):
    n = len(dims)
    Dtot = int(np.prod(dims))
    P = np.zeros((Dtot, Dtot))
    for idx in range(Dtot):
        digs, r = [], idx
        for d in reversed(dims):
            digs.append(r % d)
            r //= d
        digs = digs[::-1]
        std = [digs[list(perm).index(k)] for k in range(n)]
        j = 0
        for d, dig in zip(dims, std):
            j = j * d + dig
        P[j, idx] = 1.0
    return P


def tr_repl_expr(X, pos, dims):
    """cvxpy: trace out factors pos, reinsert 1/d in place."""
    pos = sorted(pos)
    keep = [k for k in range(len(dims)) if k not in pos]
    perm = keep + pos
    P = perm_matrix(perm, dims)          # maps frame(perm ordering) -> standard
    Xp = P.T @ X @ P                     # X in permuted ordering (kept first)
    dims_p = [dims[k] for k in perm]
    Y = Xp
    cur = list(dims_p)
    for _ in pos:
        Y = cp.partial_trace(Y, cur, axis=len(cur) - 1)
        cur = cur[:-1]
    dt = int(np.prod([dims[k] for k in pos]))
    Rep = cp.kron(Y, np.eye(dt)) / dt
    return P @ Rep @ P.T


def comb_cone(X, layers, dims):
    """layers: list of (in_factor_or_None, out_factor) from FIRST to LAST tooth,
    where 'out' means a space the comb outputs to a party (or F) and 'in' a
    space it receives. Conditions built from last tooth backwards."""
    cons = [X >> 0]
    traced = []
    for (fin, fout) in reversed(layers):
        lhs = tr_repl_expr(X, traced + [fout], dims) if traced or True else None
        # condition: _out(traced+) X == _{out,in}(...) X   [in absent for first tooth]
        t1 = tr_repl_expr(X, traced + [fout], dims)
        if fin is not None:
            t2 = tr_repl_expr(X, traced + [fout, fin], dims)
            cons.append(t1 == t2)
            traced = traced + [fout, fin]
        else:
            # first tooth: after tracing everything but nothing remains but scalar; no condition
            traced = traced + [fout]
    return cons


def solve_vis(W, cones, dims, N_noise, eps=1e-8):
    D = W.shape[0]
    W0 = np.eye(D) / N_noise
    lam = cp.Variable()
    Xs = [cp.Variable((D, D), hermitian=True) for _ in cones]
    cons = []
    for X, layers in zip(Xs, cones):
        cons += comb_cone(X, layers, dims)
    eq = sum(Xs) == lam * W + (1 - lam) * W0
    cons += [eq, lam >= 0, lam <= 1]
    prob = cp.Problem(cp.Maximize(lam), cons)
    prob.solve(solver=cp.SCS, eps=eps, max_iters=400000)
    return lam.value, eq, prob


def permute_factors_np(M, perm, dims):
    n = len(dims)
    dims_out = [dims[p] for p in perm]
    Mt = M.reshape(dims + dims)
    return np.transpose(Mt, list(perm) + [p + n for p in perm]).reshape(M.shape)


# ---------- switch construction ----------
psi = np.array([1, 0], dtype=complex)

# bipartite: (A_I A_O B_I B_O F_t F_c)
dims6 = [2] * 6
w6 = np.zeros(dims6, dtype=complex)
for i in range(2):
    for j in range(2):
        for k in range(2):
            w6[i, j, j, k, k, 0] += psi[i] / np.sqrt(2)
            w6[k, j, i, k, j, 1] += psi[i] / np.sqrt(2)
w6 = w6.reshape(64)
W6 = np.outer(w6, w6.conj())

# (i) recompute with tighter eps
cones_i = [
    [(None, 0), (1, 2), (3, 4)],   # A<B<F : out A_I(0); in A_O(1)->out B_I(2); in B_O(3)->out F(4)
    [(None, 2), (3, 0), (1, 4)],   # B<A<F
]
# F is factors 4,5 -> treat as single by merging: use dims [2,2,2,2,4]
W6m = W6  # same matrix, dims view [2,2,2,2,4]
dims5 = [2, 2, 2, 2, 4]
lam, eq_i, _ = solve_vis(W6m, cones_i, dims5, N_noise=16, eps=1e-9)
print(f"(i)  F = F_t(x)F_c, fixed past:  lam* = {lam:.7f},  r = {(1-lam)/lam:.5f}")
S_i = eq_i.dual_value

# (ii) F = F_c only: trace F_t (factor 4 of dims6)
W5 = np.einsum('abcdefABCDeF->abcdfABCDF',
               W6.reshape(dims6 + dims6)).reshape(32, 32)
dims5b = [2, 2, 2, 2, 2]
lam, _, _ = solve_vis(W5, cones_i, dims5b, N_noise=8, eps=1e-9)
print(f"(ii) F = F_c only:              lam* = {lam:.7f},  r = {(1-lam)/lam:.5f}")

# (iv) F = F_t only: trace F_c
W5t = np.einsum('abcdefABCDEf->abcdeABCDE',
                W6.reshape(dims6 + dims6)).reshape(32, 32)
lam, _, _ = solve_vis(W5t, cones_i, dims5b, N_noise=8, eps=1e-9)
print(f"(iv) F = F_t only (control traced): lam* = {lam:.7f}  (expect 1: separable)")

# (iii) open past: (P_O(4)=t(x)c, A_I, A_O, B_I, B_O, F(4)=t(x)c)
dims_iii = [2, 2, 2, 2, 2, 2, 2, 2]  # p_t p_c aI aO bI bO f_t f_c
w8 = np.zeros(dims_iii, dtype=complex)
for t in range(2):
    for j in range(2):
        for k in range(2):
            w8[t, 0, t, j, j, k, k, 0] += 1.0
            w8[t, 1, k, j, t, k, j, 1] += 1.0
w8 = w8.reshape(256)
W8 = np.outer(w8, w8.conj())
print("Tr W (open past) =", np.trace(W8).real, " (expect 16)")
# quick validity: random state on P_O, random CPTP A,B, trace F -> prob 1
import sys
sys.path.insert(0, '.')
from common import random_instrument_chois
rng = np.random.default_rng(5)
worst = 0.0
for _ in range(50):
    v = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    rho = v @ v.conj().T
    rho /= np.trace(rho)
    MA = sum(random_instrument_chois(2, nk=2, rng=rng)).T
    MB = sum(random_instrument_chois(2, nk=2, rng=rng)).T
    p = np.trace(W8 @ np.kron(np.kron(np.kron(rho.T, MA), MB), np.eye(4))).real
    worst = max(worst, abs(p - 1))
# note: P is a prepare-only party; its Choi (trivial input) is rho itself,
# transposed convention -> rho^T? test both:
worst2 = 0.0
for _ in range(50):
    v = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    rho = v @ v.conj().T
    rho /= np.trace(rho)
    MA = sum(random_instrument_chois(2, nk=2, rng=rng)).T
    MB = sum(random_instrument_chois(2, nk=2, rng=rng)).T
    p = np.trace(W8 @ np.kron(np.kron(np.kron(rho, MA), MB), np.eye(4))).real
    worst2 = max(worst2, abs(p - 1))
print(f"  open-past validity: max|P-1| with rho^T: {worst:.2e}, with rho: {worst2:.2e}")

dims_iii5 = [4, 2, 2, 2, 2, 4]   # P_O, A_I, A_O, B_I, B_O, F
cones_iii = [
    [(0, 1), (2, 3), (4, 5)],    # P<A<B<F: in P_O -> out A_I; in A_O -> out B_I; in B_O -> out F
    [(0, 3), (4, 1), (2, 5)],    # P<B<A<F
]
lam, eq3, _ = solve_vis(W8, cones_iii, dims_iii5, N_noise=16, eps=1e-8)
print(f"(iii) open past P (d=4), F (d=4): lam* = {lam:.7f},  r = {(1-lam)/lam:.5f}")
