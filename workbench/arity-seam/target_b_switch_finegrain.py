"""Target B: fine-graining of a fixed-spacetime photonic quantum switch.

Model: control qubit c; target photon with internal (polarization) qubit;
photon position/rail p in {A-loc, B-loc}. Lab has background time with two
stages t1 < t2. Routing: if c=0 photon is at A-loc at t1 and B-loc at t2
(A then B); if c=1 the reverse.

FOUR spacetime-localized potential events:
  A-early = (device A fires at t1), A-late = (device A fires at t2),
  B-early = (device B fires at t1), B-late = (device B fires at t2).
Each device acts on whatever occupies its local mode: photon -> apply U on
polarization; vacuum -> identity. So each event is the unitary
  E_A = P_{p=Aloc} (x) U_A + P_{p=Bloc} (x) I     (on position (x) polarization)
  E_B = P_{p=Bloc} (x) U_B + P_{p=Aloc} (x) I
[E_A, E_B] = 0 (orthogonal position sectors).

Fine-grained circuit (FIXED, acyclic order on the four events):
  route(c->p)  ->  [A-early, B-early] at t1  ->  SWAP rails  ->
  [A-late, B-late] at t2  ->  unroute.
Order relations: A-early ≺ A-late, A-early ≺ B-late, B-early ≺ A-late,
B-early ≺ B-late; A-early/B-early unordered (spacelike/simultaneous). Definite
acyclic order. Each branch's photon traverses U_A exactly once and U_B exactly
once; the OTHER traversal of each device hits vacuum.

Coarse-graining: party 'A' = the single application of U_A to the input
subsystem  H_A_in = (mode at A-loc at t1 | c=0-branch) ⊕ (mode at A-loc at
t2 | c=1-branch)  — a TIME-DELOCALIZED subsystem. Written on parties (A, B)
the process is the quantum switch W_QS.
"""
import numpy as np
rng = np.random.default_rng(7)

def rand_u(n=2):
    z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    return q * (np.diag(r)/abs(np.diag(r)))

I2 = np.eye(2)
P0 = np.diag([1.0, 0.0]); P1 = np.diag([0.0, 1.0])

def kron(*ops):
    out = np.array([[1.0+0j]])
    for o in ops: out = np.kron(out, o)
    return out

U_A, U_B = rand_u(), rand_u()

# ---------- (1)+(2) fine-grained fixed-order circuit on c (x) p (x) pol ----------
CNOT_cp = kron(P0, I2, I2) + kron(P1, np.array([[0,1],[1,0]]), I2)  # route c->p
E_Ae = kron(I2, P0, U_A) + kron(I2, P1, I2)   # A-early (t1)
E_Be = kron(I2, P1, U_B) + kron(I2, P0, I2)   # B-early (t1)
SWAP_rails = kron(I2, np.array([[0,1],[1,0]]), I2)
E_Al = E_Ae.copy()                            # A-late (t2): same device, later time
E_Bl = E_Be.copy()                            # B-late (t2)
assert np.allclose(E_Ae @ E_Be, E_Be @ E_Ae)  # early events commute (unordered)

V_fine = CNOT_cp @ E_Al @ E_Bl @ SWAP_rails @ E_Ae @ E_Be @ CNOT_cp
# unroute at the end returns rail register to |0>; extract action on c (x) pol
# with p in |0> in and out:
idx = [0,1,4,5]  # basis states |c p pol> with p=0: 000,001,100,101
V_cpol = V_fine[np.ix_(idx, idx)]

W_switch = kron(P0, U_B @ U_A) + kron(P1, U_A @ U_B)
print("(2) fine-grained fixed-order circuit == switch unitary on c(x)pol:",
      np.allclose(V_cpol, W_switch))
# also check the rail register really returns to |0> (no leakage):
leak = np.linalg.norm(V_fine[np.ix_([2,3,6,7], idx)])
print("    rail-register leakage:", leak)

# ---------- (3) coarse-grained two-stage form: single use of U_A, U_B ----------
V1 = kron(P0, U_A) + kron(P1, U_B)   # stage t1 on c (x) pol
V2 = kron(P0, U_B) + kron(P1, U_A)   # stage t2
print("(3) V2 V1 == |0><0| (x) U_B U_A + |1><1| (x) U_A U_B :",
      np.allclose(V2 @ V1, W_switch))

# ---------- (4) process-matrix check: pure switch process vector ----------
# spaces: Pc Pt AI AO BI BO Ft Fc  (each dim 2)
# |w> = sum_ijk |0>|i>  |i>_AI |j>_AO |j>_BI |k>_BO  |k>|0>
#     + sum_ijk |1>|i>  |j>_AI |k>_AO |i>_BI |j>_BO  |k>|1>
w = np.zeros((2,)*8, dtype=complex)
for i in range(2):
    for j in range(2):
        for k in range(2):
            w[0, i, i, j, j, k, k, 0] += 1   # c=0: Pt->AI, AO->BI, BO->Ft
            w[1, i, j, k, i, j, k, 1] += 1   # c=1: Pt->BI, BO->AI, AO->Ft
W_proc = np.einsum('abcdefgh,ijklmnop->abcdefghijklmnop', w, w.conj())  # |w><w| (rank-1)

# insert operations: amplitude for AO=j given AI=i is (U_A)_{ji}
M = np.einsum('cpabdeft,ba,ed->ftcp', w, U_A, U_B)   # map (Pc,Pt) -> (Ft,Fc)
M = M.reshape(4, 4, order='C')                        # rows (f t)? build carefully
# rebuild with explicit ordering (Fc,Ft) x (Pc,Pt):
Mop = np.zeros((4, 4), dtype=complex)
for pc in range(2):
    for pt in range(2):
        for fc in range(2):
            for ft in range(2):
                Mop[2*fc+ft, 2*pc+pt] = np.einsum('abcd,ba,dc->',
                    w[pc, pt, :, :, :, :, ft, fc], U_A, U_B)
print("(4) contraction of pure process |w> with (U_A, U_B) == W_switch:",
      np.allclose(Mop, W_switch))

# causal non-separability of the coarse-grained process is standard (the switch
# violates causal inequalities' device-dependent witnesses); here we exhibit the
# signature: with U_A, U_B anticommuting Paulis the two orders differ by sign,
# and measuring control in |+/-> reads out the commutator:
X = np.array([[0,1],[1,0]], dtype=complex); Z = np.diag([1,-1]).astype(complex)
Vs = kron(P0, Z @ X) + kron(P1, X @ Z)
plus = np.array([1,1])/np.sqrt(2)
psi = np.kron(plus, np.array([1,0]))
out = Vs @ psi
# control measured in +/- basis:
pm = np.kron(np.array([1,-1])/np.sqrt(2), I2[:,0]*0+1)  # projector done manually below
ctrl_minus = np.kron(np.array([1,-1])/np.sqrt(2), np.eye(2))
p_minus = np.linalg.norm(ctrl_minus.reshape(2,4)[0] @ 0 + (ctrl_minus @ out))**2 / 2
amp = np.array([ (np.kron(np.array([1,-1])/np.sqrt(2), e) @ out) for e in np.eye(2)])
print("    commutator witness P(control=-) with A=X,B=Z:", float(np.sum(abs(amp)**2)))
