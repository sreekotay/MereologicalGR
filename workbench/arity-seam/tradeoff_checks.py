"""
Spot checks for the CQ decoherence-diffusion trade-off derivation.

Conventions (mine, derived from block positivity of the short-time CP kernel):
  Master eq:  d rho/dt = -(i/hbar)[H,rho]
      - d_z ( D1^{00} rho )  + (1/2) d_z^2 ( D2 rho )
      + D0^{ab} ( L_a rho L_b+  - 1/2 {L_b+ L_a, rho} )
      - d_z ( D1^a L_a rho + conj(D1^b) rho L_b+ )
  Block positivity:  [[D0, D1],[D1+, D2]] >= 0  =>  D2 >= D1+ D0^{-1} D1.
  Noise:  <xi(t) xi(t')> = D2 delta(t-t')   (since Var(dz) = D2 dt with 1/2 d^2 convention)
  Back-reaction drift of z:  d<z>/dt = 2 Re D1 <L>  => sourcing with unit coeff => D1 = 1/2
  => scalar trade-off  D0 * D2 >= 1/4.
  Decoherence of L/R superposition (L = mass density rho_m(x), ultralocal D0):
      lambda = (D0/2) * Int (rho_L - rho_R)^2 d^3x
"""
import numpy as np

rng = np.random.default_rng(0)

# ---- 1. numeric sanity: block positivity <=> Schur complement --------------
def rand_psd(n):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return A @ A.conj().T

ok = True
for _ in range(200):
    n, m = 3, 2
    M = rand_psd(n + m)
    D0, D1, D2 = M[:n, :n], M[:n, n:], M[n:, n:]
    S = D2 - D1.conj().T @ np.linalg.inv(D0) @ D1  # Schur complement
    if np.min(np.linalg.eigvalsh(S)) < -1e-9:
        ok = False
print("Schur complement of PSD block matrix always PSD:", ok)

# and the converse direction: build M with D2 slightly BELOW D1+ D0^-1 D1 -> not PSD
D0 = rand_psd(3); D1 = rng.normal(size=(3, 2)) + 1j * rng.normal(size=(3, 2))
D2bad = 0.999 * D1.conj().T @ np.linalg.inv(D0) @ D1
M = np.block([[D0, D1], [D1.conj().T, D2bad]])
print("violating D2 < D1+ D0^-1 D1 breaks positivity:",
      np.min(np.linalg.eigvalsh(M)) < 0)

# ---- 2. sphere self-field integral  Int |g|^2 = (24 pi/5) M^2 / R ----------
# g(y) = (Newtonian field of uniform sphere)/G ; check by direct quadrature
M_, R_ = 1.0, 1.0
r = np.linspace(1e-4, 60, 4_000_000)
g = np.where(r < R_, M_ * r / R_**3, M_ / r**2)
I = np.trapezoid(g**2 * 4 * np.pi * r**2, r)
print("Int |g|^2 numeric / (24 pi/5 M^2/R):", I / (24 * np.pi / 5))

# ---- 3. the exclusion arithmetic -------------------------------------------
G   = 6.674e-11          # m^3 kg^-1 s^-2
mN  = 1.66e-27           # kg (nucleon)
# (a) interferometry: N_s nucleons coherent for tau  =>  lambda <= 1/tau
N_s, tau = 1e5, 1e-3
lam = 1 / tau
# (b) probe options
T   = 100.0              # s
sig_a_kg   = 1e-7        # m/s^2  (task's torsion-balance number, kg mass)
rho_metal  = 8.0e3
R_sph = (3 * 1.0 / (4 * np.pi * rho_metal))**(1/3)
sig_a_atom = 1e-9        # m/s^2  (atom-interferometer gravimeter, ~87 nucleons)
N_p = 87

for name, ell in [("atomic-scale smearing l=1e-10 m", 1e-10),
                  ("nucleon-scale smearing l=1e-15 m", 1e-15)]:
    drho2 = 2 * N_s * mN**2 / ell**3          # Int (rho_L-rho_R)^2
    D0max = 2 * lam / drho2                   # decoherence ceiling
    D2min = 1 / (4 * D0max)                   # = drho2/(8 lam), diffusion floor
    # ceiling from kg sphere: sigma_a^2 = (8 pi/5) G^2 D2 /(R T)
    D2max_sph  = sig_a_kg**2 * R_sph * T / ((8 * np.pi / 5) * G**2)
    # ceiling from atom probe: sigma_a^2 = (4 pi/3) G^2 D2 /(N_p l T)
    D2max_atom = sig_a_atom**2 * 3 * N_p * ell * T / (4 * np.pi * G**2)
    # predicted noise if D2 = floor
    sa_sph  = np.sqrt((8 * np.pi / 5) * G**2 * D2min / (R_sph * T))
    sa_atom = np.sqrt((4 * np.pi / 3) * G**2 * D2min / (N_p * ell * T))
    print(f"\n== {name} ==")
    print(f"  Int drho^2      = {drho2:.3e} kg^2/m^3")
    print(f"  D0 ceiling      = {D0max:.3e} m^3 kg^-2 s^-1")
    print(f"  D2 floor        = {D2min:.3e} kg^2 s m^-3")
    print(f"  D2 ceil (kg sphere, 1e-7 m/s^2, T=100s, R={R_sph:.3f} m) = {D2max_sph:.3e}")
    print(f"  D2 ceil (atom grav., 1e-9 m/s^2) = {D2max_atom:.3e}")
    print(f"  predicted sigma_a: kg sphere {sa_sph:.2e} | atom {sa_atom:.2e}  m/s^2")
    print(f"  EXCLUDED (sphere)? {D2min > D2max_sph} | (atom)? {D2min > D2max_atom}")

# critical smearing scale for exclusion with atom probe (l_d = l_p = l):
# sigma_min^2 = pi G^2 N_s mN^2 / (3 N_p l^4 lam T)  > sig_a_atom^2
l_crit = (np.pi * G**2 * N_s * mN**2 / (3 * N_p * lam * T * sig_a_atom**2))**0.25
print(f"\ncritical smearing scale (atom probe): l < {l_crit:.2e} m")
l_crit_s = (np.pi*8/5 * G**2 * 2*N_s * mN**2 / (8 * lam * R_sph * T * sig_a_kg**2))**(1/3)
print(f"critical smearing scale (kg sphere @1e-7): l < {l_crit_s:.2e} m")
