"""Target C: BMV Newtonian-phase entanglement arithmetic.

Two masses m, each split into branches L/R along the line joining them.
Joint branch (i,j) has separation d_ij and accumulates phase
   phi_ij = G m^2 t / (hbar d_ij)
(Newtonian interaction energy E_ij = -G m^2/d_ij; phase e^{-i E t/hbar}; sign
is a common convention, only differences matter).

State after time t:
  (1/2) sum_ij e^{i phi_ij} |i>|j>
Product-state iff phases factor as phi_ij = a_i + b_j, i.e. iff
  Dphi := phi_RL + phi_LR - phi_LL - phi_RR = 0 (mod 2pi).
Dphi is the entanglement phase; e.g. negativity/concurrence of the resulting
two-qubit state is |sin(Dphi/2)| (up to local dephasing), so entanglement is
generated iff Dphi != 0 mod 2pi and is maximal at Dphi = pi.

Canonical geometry (Bose et al. / Marletto-Vedral): centers such that the
CLOSEST approach (R of mass 1 vs L of mass 2) is d_min = 200 um, split
Dx = 250 um. Then
  d_RL = 200 um; d_LL = d_RR = 200+250 = 450 um; d_LR = 200+2*250 = 700 um.
"""
import numpy as np

G = 6.67430e-11
hbar = 1.054571817e-34
m = 1e-14
t = 2.5
dmin, split = 200e-6, 250e-6

d = {"RL": dmin, "LL": dmin+split, "RR": dmin+split, "LR": dmin+2*split}
phi = {k: G*m*m*t/(hbar*v) for k, v in d.items()}
for k in ("RL", "LL", "RR", "LR"):
    print("phi_%s (d=%4.0f um) = %8.4f rad" % (k, d[k]*1e6, phi[k]))

Dphi = phi["RL"] + phi["LR"] - phi["LL"] - phi["RR"]
print("entanglement phase Dphi = phi_RL+phi_LR-phi_LL-phi_RR = %.4f rad" % Dphi)
print("concurrence of resulting state |sin(Dphi/2)| = %.4f" % abs(np.sin(Dphi/2)))

# build state and compute negativity to confirm
ket = 0.5*np.array([np.exp(1j*phi["LL"]), np.exp(1j*phi["LR"]),
                    np.exp(1j*phi["RL"]), np.exp(1j*phi["RR"])])
rho = np.outer(ket, ket.conj()).reshape(2,2,2,2)
rho_pt = rho.transpose(0,3,2,1).reshape(4,4)   # partial transpose on qubit 2
neg = -sum(l for l in np.linalg.eigvalsh(rho_pt) if l < 0)
print("negativity = %.4f (max 0.5); concurrence = %.4f" % (neg, 2*neg))
