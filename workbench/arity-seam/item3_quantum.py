"""Item 3 (+4 diagnostics): quantum violation of the causal bound with W_OCB.

Party operators are transposed Chois M = C^T (convention fixed in common.py);
for the real rank-one projector strategies here C^T = C.

p_succ = 1/2 [ P(x=b|b'=0) + P(y=a|b'=1) ]
       = (1/8) sum_{a,b} { Tr[W (M_A^{x=b|a} (x) N_B^{b,0})]
                         + Tr[W (N_A^{a}     (x) M_B^{y=a|b,1})] }
with N = sum over outcomes (CPTP element).

Part A: fixed OCB-style strategy (search tiny discrete family of encodings).
Part B: see-saw SDP optimization over ALL qubit instruments (gradient-free:
        alternating exact linear-SDP maximization), many random restarts.
Part C: item-4 diagnostics (correlator caps, anticommutation structure).
"""
import numpy as np
import cvxpy as cp
from common import I2, sx, sz, op_on, random_instrument_chois

rng = np.random.default_rng(1)
dims = [2, 2, 2, 2]
T1 = op_on({1: sz, 2: sz}, dims)
T2 = op_on({0: sz, 2: sx, 3: sz}, dims)
W = 0.25 * (np.eye(16) + (T1 + T2) / np.sqrt(2))

ket = [np.array([1, 0], dtype=complex), np.array([0, 1], dtype=complex)]
plus = [(ket[0] + ket[1]) / np.sqrt(2), (ket[0] - ket[1]) / np.sqrt(2)]  # sx eigenstates +,-


def proj(v):
    return np.outer(v, v.conj())


def contract_B(Wm, Y):
    """G on A with Tr[W (X (x) Y)] = Tr[G X]."""
    W4 = Wm.reshape(4, 4, 4, 4)          # (iA,iB),(jA,jB)
    return np.einsum('abcd,db->ac', W4, Y)


def contract_A(Wm, X):
    W4 = Wm.reshape(4, 4, 4, 4)
    return np.einsum('abcd,ca->bd', W4, X)


def psucc(MA, MB):
    """MA[a][x]: 4x4 on A_I(x)A_O.  MB[(b,bp)][y]: 4x4 on B_I(x)B_O."""
    p = 0.0
    for a in range(2):
        NA = MA[a][0] + MA[a][1]
        for b in range(2):
            NB0 = MB[(b, 0)][0] + MB[(b, 0)][1]
            p += np.trace(W @ np.kron(MA[a][b], NB0)).real       # x = b scored
            p += np.trace(W @ np.kron(NA, MB[(b, 1)][a])).real   # y = a scored
    return p / 8.0


def correlators(MA, MB):
    E1 = E2 = 0.0
    for a in range(2):
        NA = MA[a][0] + MA[a][1]
        for b in range(2):
            NB0 = MB[(b, 0)][0] + MB[(b, 0)][1]
            for x in range(2):
                E1 += (-1) ** (x + b) * np.trace(W @ np.kron(MA[a][x], NB0)).real
            for y in range(2):
                E2 += (-1) ** (y + a) * np.trace(W @ np.kron(NA, MB[(b, 1)][y])).real
    return E1 / 4.0, E2 / 4.0


# ---------- Part A: fixed OCB strategy ----------
def alice_ocb():
    """Measure sz (outcome x), re-prepare |a> encoding her bit."""
    return {a: {x: np.kron(proj(ket[x]), proj(ket[a])) for x in range(2)} for a in range(2)}


def bob_ocb(enc, meas0):
    """b'=1: measure sz (outcome y), re-prepare I/2.
       b'=0: measure meas0 basis (outcome beta), re-prepare |m(b,beta)> in z."""
    MB = {}
    basis0 = plus if meas0 == 'x' else ket
    for b in range(2):
        MB[(b, 1)] = {y: np.kron(proj(ket[y]), I2 / 2) for y in range(2)}
        MB[(b, 0)] = {be: np.kron(proj(basis0[be]), proj(ket[enc(b, be)])) for be in range(2)}
    return MB


MA0 = alice_ocb()
best = None
for meas0 in ['x', 'z']:
    for name, enc in [('m=b', lambda b, be: b), ('m=1-b', lambda b, be: 1 - b),
                      ('m=b^beta', lambda b, be: b ^ be), ('m=1-(b^beta)', lambda b, be: 1 - (b ^ be))]:
        p = psucc(MA0, bob_ocb(enc, meas0))
        if best is None or p > best[0]:
            best = (p, meas0, name)
        print(f"  fixed strategy: Bob b'=0 measures s{meas0}, encoding {name:14s}: p = {p:.6f}")
print(f"best fixed OCB strategy: p = {best[0]:.10f}  (claim (2+sqrt2)/4 = {(2+np.sqrt(2))/4:.10f})")
MB0 = bob_ocb({'m=b': lambda b, be: b, 'm=1-b': lambda b, be: 1 - b,
               'm=b^beta': lambda b, be: b ^ be, 'm=1-(b^beta)': lambda b, be: 1 - (b ^ be)}[best[2]], best[1])
E1o, E2o = correlators(MA0, MB0)
print(f"  correlators at OCB point: E1 = {E1o:.6f}, E2 = {E2o:.6f}, 1/sqrt2 = {1/np.sqrt(2):.6f}")


# ---------- Part B: see-saw over all instruments ----------
def ptrace_out(M):
    """cvxpy partial trace over second factor of 2x2, expr 4x4 -> 2x2."""
    return cp.partial_trace(M, [2, 2], axis=1)


def solve_alice(MB, weights=(1.0, 1.0)):
    """Max w1*E1-part + w2*E2-part over Alice ops. Returns MA, val of objective."""
    V = {a: {x: cp.Variable((4, 4), hermitian=True) for x in range(2)} for a in range(2)}
    cons = []
    for a in range(2):
        cons += [V[a][x] >> 0 for x in range(2)]
        cons.append(ptrace_out(V[a][0] + V[a][1]) == np.eye(2))
    obj = 0
    w1, w2 = weights
    for a in range(2):
        for b in range(2):
            NB0 = MB[(b, 0)][0] + MB[(b, 0)][1]
            G1 = contract_B(W, NB0)
            obj += w1 * cp.real(cp.trace(G1 @ V[a][b])) / 8
            G2 = contract_B(W, MB[(b, 1)][a])
            obj += w2 * cp.real(cp.trace(G2 @ (V[a][0] + V[a][1]))) / 8
    prob = cp.Problem(cp.Maximize(obj), cons)
    prob.solve(solver=cp.SCS, eps=1e-9, max_iters=200000)
    MA = {a: {x: V[a][x].value for x in range(2)} for a in range(2)}
    return MA, prob.value


def solve_bob(MA, weights=(1.0, 1.0)):
    V = {(b, bp): {y: cp.Variable((4, 4), hermitian=True) for y in range(2)} for b in range(2) for bp in range(2)}
    cons = []
    for k in V:
        cons += [V[k][y] >> 0 for y in range(2)]
        cons.append(ptrace_out(V[k][0] + V[k][1]) == np.eye(2))
    obj = 0
    w1, w2 = weights
    for a in range(2):
        NA = MA[a][0] + MA[a][1]
        GA_N = contract_A(W, NA)
        for b in range(2):
            GA_x = contract_A(W, MA[a][b])
            obj += w1 * cp.real(cp.trace(GA_x @ (V[(b, 0)][0] + V[(b, 0)][1]))) / 8
            obj += w2 * cp.real(cp.trace(GA_N @ V[(b, 1)][a])) / 8
    prob = cp.Problem(cp.Maximize(obj), cons)
    prob.solve(solver=cp.SCS, eps=1e-9, max_iters=200000)
    MB = {k: {y: V[k][y].value for y in range(2)} for k in V}
    return MB, prob.value


def random_party_A():
    return {a: {x: C.T for x, C in enumerate(random_instrument_chois(2, nk=2, rng=rng))} for a in range(2)}


def random_party_B():
    return {(b, bp): {y: C.T for y, C in enumerate(random_instrument_chois(2, nk=2, rng=rng))}
            for b in range(2) for bp in range(2)}


def seesaw(MA, MB, iters=25, tol=1e-10):
    p_old = -1
    for it in range(iters):
        MA, _ = solve_alice(MB)
        MB, p = solve_bob(MA)
        if abs(p - p_old) < tol:
            break
        p_old = p
    return MA, MB, psucc(MA, MB)


print("\nsee-saw from OCB start:")
MAs, MBs, p_star = seesaw(MA0, MB0)
print(f"  p = {p_star:.10f}")

best_p, best_pt = p_star, (MAs, MBs)
print("see-saw from 20 random starts:")
vals = []
for r in range(20):
    _, _, p = seesaw(random_party_A(), random_party_B(), iters=30)
    vals.append(p)
best_r = max(vals)
print("  best over restarts:", f"{best_r:.10f}", " all:", np.round(sorted(vals)[-5:], 8))
print(f"GLOBAL best found: {max(best_p, best_r):.10f}   vs (2+sqrt2)/4 = {(2+np.sqrt(2))/4:.10f}")

# ---------- Part C: item-4 diagnostics ----------
print("\n--- item 4 diagnostics ---")
E1s, E2s = correlators(*best_pt)
print(f"at joint optimum: E1 = {E1s:.8f}, E2 = {E2s:.8f} (both together!), 1/sqrt2 = {1/np.sqrt(2):.8f}")

# max E1 ALONE (weights kill E2) and max E2 alone
MA_, MB_ = MA0, MB0
for it in range(15):
    MA_, _ = solve_alice(MB_, weights=(2.0, 0.0))
    MB_, v1 = solve_bob(MA_, weights=(2.0, 0.0))   # objective = E1-part*2/... careful
E1_only = correlators(MA_, MB_)[0]
MA_, MB_ = MA0, MB0
for it in range(15):
    MA_, _ = solve_alice(MB_, weights=(0.0, 2.0))
    MB_, v2 = solve_bob(MA_, weights=(0.0, 2.0))
E2_only = correlators(MA_, MB_)[1]
# also from random starts
for r in range(6):
    MA_, MB_ = random_party_A(), random_party_B()
    for it in range(15):
        MA_, _ = solve_alice(MB_, weights=(2.0, 0.0))
        MB_, _ = solve_bob(MA_, weights=(2.0, 0.0))
    E1_only = max(E1_only, correlators(MA_, MB_)[0])
    MA_, MB_ = random_party_A(), random_party_B()
    for it in range(15):
        MA_, _ = solve_alice(MB_, weights=(0.0, 2.0))
        MB_, _ = solve_bob(MA_, weights=(0.0, 2.0))
    E2_only = max(E2_only, correlators(MA_, MB_)[1])
print(f"max E1 ALONE = {E1_only:.8f}, max E2 ALONE = {E2_only:.8f}")
print("  (CHSH analogue would allow each correlator alone -> 1; cap at 1/sqrt2 means")
print("   the sqrt2 lives in W, not in a strategy-level trade-off)")

# decomposition of correlators onto W's terms at the optimum
MAo, MBo = best_pt
S1 = np.zeros((16, 16), dtype=complex)
S2 = np.zeros((16, 16), dtype=complex)
for a in range(2):
    NA = MAo[a][0] + MAo[a][1]
    for b in range(2):
        NB0 = MBo[(b, 0)][0] + MBo[(b, 0)][1]
        for x in range(2):
            S1 += (-1) ** (x + b) * np.kron(MAo[a][x], NB0) / 4
        for y in range(2):
            S2 += (-1) ** (y + a) * np.kron(NA, MBo[(b, 1)][y]) / 4
for nm, S in [('S1 (x=b game)', S1), ('S2 (y=a game)', S2)]:
    print(f"  {nm}:  Tr S = {np.trace(S).real:+.5f},  Tr[T1 S]/4 = {np.trace(T1@S).real/4:+.5f},"
          f"  Tr[T2 S]/4 = {np.trace(T2@S).real/4:+.5f}")
print("  => E_i = (1/(4 sqrt2)) Tr[T_i S_i]; each |Tr[T_i S_i]| <= 4 trivially")

# Bob's effective B_I observables in the two roles at the optimum
def bob_obs(MBo, bp):
    O = []
    for b in range(2):
        o = sum((-1) ** y * np.einsum('abcb->ac', MBo[(b, bp)][y].reshape(2, 2, 2, 2)) for y in range(2))
        O.append(o)
    return O

Oz = bob_obs(MBo, 1)   # guessing role
# signalling role: relevant object is the B_I(x)B_O operator; take B_I 'direction' of
# the difference between b=0 and b=1 CPTP elements:
D = (MBo[(0, 0)][0] + MBo[(0, 0)][1]) - (MBo[(1, 0)][0] + MBo[(1, 0)][1])
print("\nBob's b'=1 observables (should be ~ +/- sz):")
for b in range(2):
    c = [np.trace(P @ Oz[b]).real / 2 for P in (I2, sx, 1j*(-1)*np.array([[0,-1],[1,0]]), sz)]
    print(f"   b={b}: bloch (1,sx,sy,sz) = {np.round(c,5)}")
cD = [[np.trace(np.kron(P, Q) @ D).real / 4 for Q in (I2, sx, sz)] for P in (I2, sx, sz)]
print("Bob's b'=0 signalling operator Delta = N(b=0)-N(b=1), coeffs on (1,sx,sz)x(1,sx,sz):")
print(np.round(np.array(cD), 5), " rows: B_I in {1,sx,sz}, cols: B_O in {1,sx,sz}")
print("  -> weight on sx^{B_I} sz^{B_O} shows the signalling role uses the sx observable,")
print("     anticommuting with the guessing role's sz. {sx,sz}=0:", np.linalg.norm(sx@sz+sz@sx))
