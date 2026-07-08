"""Item 1: validity of W_OCB.
Ordering: A_I (x) A_O (x) B_I (x) B_O   (all qubits, dim 16).
W_OCB = 1/4 [ 1 + ( sz^{A_O} sz^{B_I} + sz^{A_I} sx^{B_I} sz^{B_O} ) / sqrt2 ]
Party operators: transposed Chois (convention fixed in common.py).
"""
import numpy as np
from common import I2, sx, sz, op_on, random_instrument_chois

dims = [2, 2, 2, 2]  # A_I, A_O, B_I, B_O

T1 = op_on({1: sz, 2: sz}, dims)          # sz^{A_O} sz^{B_I}
T2 = op_on({0: sz, 2: sx, 3: sz}, dims)   # sz^{A_I} sx^{B_I} sz^{B_O}
W_OCB = 0.25 * (np.eye(16) + (T1 + T2) / np.sqrt(2))


def permute_factors(W, perm):
    Wt = W.reshape([2] * 8)
    axes = perm + [p + 4 for p in perm]
    return np.transpose(Wt, axes).reshape(16, 16)


def tr_repl(W, pos):
    """_x W : trace out factors in pos, reinsert 1/d_x in place."""
    pos = sorted(pos)
    keep = [k for k in range(4) if k not in pos]
    perm = keep + pos
    P = permute_factors(W, perm)
    dk, dt = 2 ** len(keep), 2 ** len(pos)
    red = np.einsum('aibi->ab', P.reshape(dk, dt, dk, dt))
    rep = np.kron(red, np.eye(dt)) / dt
    return permute_factors(rep, list(np.argsort(perm)))


# --- algebraic structure ---
anti = T1 @ T2 + T2 @ T1
ev = np.linalg.eigvalsh(W_OCB)
print("Tr W           =", np.trace(W_OCB).real)
print("min eigenvalue =", f"{ev.min():.3e}")
print("eigenvalues (unique, rounded):", sorted(set(np.round(ev, 10))))
print("||{T1,T2}||    =", np.linalg.norm(anti), " (anticommutation of the two terms)")
print("||T1+T2||_op   =", np.linalg.norm(T1 + T2, 2), " vs sqrt2 =", np.sqrt(2))

# --- linear validity conditions (bipartite process subspace) ---
c1 = np.linalg.norm(tr_repl(W_OCB, [2, 3]) - tr_repl(W_OCB, [1, 2, 3]))  # no signaling B->A via A_O-marginal structure
c2 = np.linalg.norm(tr_repl(W_OCB, [0, 1]) - tr_repl(W_OCB, [0, 1, 3]))
c3 = np.linalg.norm(W_OCB - (tr_repl(W_OCB, [3]) + tr_repl(W_OCB, [1]) - tr_repl(W_OCB, [1, 3])))
print("linear validity conditions (should be ~0): %.2e %.2e %.2e" % (c1, c2, c3))

# --- probability normalization for random CPTP instrument pairs ---
rng = np.random.default_rng(42)
worst_dev, min_prob = 0.0, 1.0
for trial in range(300):
    ChA = random_instrument_chois(n_out=int(rng.integers(1, 4)), nk=int(rng.integers(1, 4)), rng=rng)
    ChB = random_instrument_chois(n_out=int(rng.integers(1, 4)), nk=int(rng.integers(1, 4)), rng=rng)
    ptot = 0.0
    for a in ChA:
        for b in ChB:
            p = np.trace(W_OCB @ np.kron(a.T, b.T)).real
            min_prob = min(min_prob, p)
            ptot += p
    worst_dev = max(worst_dev, abs(ptot - 1.0))
print("\n300 random CPTP instrument pairs (1-3 outcomes, random Kraus rank):")
print(f"  max |sum_of_probs - 1| = {worst_dev:.3e}")
print(f"  min single-outcome prob = {min_prob:.3e}  (must be >= 0)")
