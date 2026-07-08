"""Item 4: verify the identities behind the Tsirelson-type bound p <= (2+sqrt2)/4.

Write E1 = Tr[W S1], E2 = Tr[W S2] with signed strategy operators
  S1 = (1/4) sum_{a,b,x} (-1)^{x+b} M_A^{x|a} (x) N_B^{b,0}
  S2 = (1/4) sum_{a,b,y} (-1)^{y+a} N_A^{a}   (x) M_B^{y|b,1}
and W = (1/4)[1 + (T1+T2)/sqrt2].

Claimed identities (consequences of trace preservation alone, for ARBITRARY
instruments):   Tr S1 = Tr S2 = 0,   Tr[T1 S1] = 0,   Tr[T2 S2] = 0.
Hence E_i = (1/(4 sqrt2)) Tr[T_i S_i], and term-by-term
  |Tr[T_i S_i]| <= (1/4) sum_{a,b} ||T_i||_op * Tr[M (x) N] = (1/4)*16 = 4
so E_i <= 1/sqrt2 for EVERY strategy, and p = 1/2 + (E1+E2)/4 <= (2+sqrt2)/4.
The sqrt2 comes solely from W's coefficient, which is maximal because
||T1+T2|| = sqrt2 by {T1,T2}=0 (anticommuting Hermitian unitaries): the
Tsirelson anticommutator bound applied to the PROCESS, not to the strategies.
"""
import numpy as np
from common import sx, sz, op_on, random_instrument_chois

rng = np.random.default_rng(3)
dims = [2, 2, 2, 2]
T1 = op_on({1: sz, 2: sz}, dims)
T2 = op_on({0: sz, 2: sx, 3: sz}, dims)
W = 0.25 * (np.eye(16) + (T1 + T2) / np.sqrt(2))

worst = np.zeros(4)
worst_bound = 0.0
for trial in range(200):
    MA = {a: [C.T for C in random_instrument_chois(2, nk=int(rng.integers(1, 4)), rng=rng)] for a in range(2)}
    MB = {(b, bp): [C.T for C in random_instrument_chois(2, nk=int(rng.integers(1, 4)), rng=rng)]
          for b in range(2) for bp in range(2)}
    S1 = np.zeros((16, 16), dtype=complex)
    S2 = np.zeros((16, 16), dtype=complex)
    for a in range(2):
        NA = MA[a][0] + MA[a][1]
        for b in range(2):
            NB0 = MB[(b, 0)][0] + MB[(b, 0)][1]
            for x in range(2):
                S1 += (-1) ** (x + b) * np.kron(MA[a][x], NB0) / 4
            for y in range(2):
                S2 += (-1) ** (y + a) * np.kron(NA, MB[(b, 1)][y]) / 4
    ids = [np.trace(S1), np.trace(S2), np.trace(T1 @ S1), np.trace(T2 @ S2)]
    worst = np.maximum(worst, np.abs(ids))
    worst_bound = max(worst_bound, abs(np.trace(T2 @ S1).real), abs(np.trace(T1 @ S2).real))

print("max |Tr S1|, |Tr S2|, |Tr[T1 S1]|, |Tr[T2 S2]| over 200 random strategies:")
print(" ", np.round(worst, 12), "  (identities: all must vanish)")
print(f"max |Tr[T2 S1]|, |Tr[T1 S2]| observed = {worst_bound:.6f}  (analytic cap: 4)")
print(f"=> E_i <= 4/(4 sqrt2) = 1/sqrt2; p <= 1/2 + 2*(1/sqrt2)/4 = {(0.5 + 1/(2*np.sqrt(2))):.10f}")
print(f"   (2+sqrt2)/4 = {(2+np.sqrt(2))/4:.10f}")

# and the positivity/anticommutation origin of the 1/sqrt2 in W:
for c, note in [(1/np.sqrt(2), "c = 1/sqrt2"), (1/np.sqrt(2) + 0.01, "c slightly larger")]:
    Wc = 0.25 * (np.eye(16) + c * (T1 + T2))
    print(f"min eig of (1/4)[1 + c(T1+T2)] at {note}: {np.linalg.eigvalsh(Wc).min():+.6f}")
