# Khmelnitsky-Rubakov PTA signal - referee script
# Coherent scalar DM of mass m: pressure oscillates at 2m with full amplitude rho;
# ii-Einstein equation gives 2*Psidd = 8*pi*G*p  =>  Psi_osc amplitude Psi_c = pi*G*rho/m^2.
# Timing residual per term: R = Psi_c / (2*pi*f), f = 2*m*c^2/h.
# Verifies: numbers at m = 1e-24..1e-22 eV, rho = 0.4 GeV/cm^3; the m^-3 scaling;
# the reach scaling m_reach ~ (sqrt(Np*Nepoch)/sigma)^(1/3).

import numpy as np

G = 6.674e-11        # SI
c = 2.998e8
hbar = 1.0546e-34
h = 2*np.pi*hbar
eV = 1.602e-19

rho = 0.4e9 * eV / (1e-2)**3 / c**2   # 0.4 GeV/cm^3 -> kg/m^3
print(f"rho_local = 0.4 GeV/cm^3 = {rho:.3e} kg/m^3")

def signal(m_eV, rho_kgm3=rho):
    m = m_eV * eV / c**2                       # kg
    omega_c = m * c**2 / hbar                  # Compton angular frequency (rad/s)
    f = 2 * m * c**2 / h                       # signal frequency, Hz
    # Psi_c = pi G rho / m^2 in natural units; SI: pi G rho / (m c^2/hbar)^2 * c^2 ... do it dimensionlessly:
    Psi_c = np.pi * G * rho_kgm3 / (omega_c**2)   # [G rho]/omega^2 = dimensionless (G rho ~ 1/s^2)
    R = Psi_c / (2*np.pi*f)                    # seconds
    return f, Psi_c, R

print(f"{'m (eV)':>8} | {'f (Hz)':>9} | {'period':>8} | {'Psi_c':>9} | {'R (s)':>9}")
for m_eV in [1e-24, 1e-23, 1e-22]:
    f, Psi, R = signal(m_eV)
    print(f"{m_eV:8.0e} | {f:9.2e} | {1/f/3.156e7:6.2f}yr | {Psi:9.2e} | {R:9.2e}")

# scaling check: R ratio for m -> 2m should be 1/8
_, _, R1 = signal(1e-23); _, _, R2 = signal(2e-23)
print(f"\nR(2m)/R(m) = {R2/R1:.4f}  (expect 0.1250 for m^-3)")

# expected anchors: at 1e-23 eV, f = 4.84e-9 Hz, Psi_c = 6.5e-16, R = 21.3 ns
f, Psi, R = signal(1e-23)
assert abs(f/4.84e-9 - 1) < 0.01, f
assert abs(Psi/6.5e-16 - 1) < 0.03, Psi
assert abs(R/21.3e-9 - 1) < 0.03, R
print("anchors OK: f = 4.84 nHz, Psi_c = 6.5e-16, R = 21.3 ns at 1e-23 eV, rho = 0.4 GeV/cm^3")

# reach scaling: matched filter for a line in white noise
#   R_min = sigma_TOA * sqrt(2 SNR^2 / (Np * Nepoch));  m_reach = (21.3 ns / R_min)^(1/3) * 1e-23 eV
def m_reach(Np, Nepoch, sigma_ns, SNR=3.0, degrade=8.0):
    # degrade: empirical factor for red noise + GWB foreground + timing-model fitting,
    # calibrated so today's config reproduces the published EPTA-DR2 reach ~5e-24 eV
    Rmin = degrade * sigma_ns*1e-9 * np.sqrt(2*SNR**2 / (Np*Nepoch))
    return 1e-23 * (21.3e-9 / Rmin)**(1/3)

print(f"\n{'era':>22} | {'m decided at rho_local':>22}")
for era, Np, Nep, sig in [("today (EPTA-DR2-like)", 25, 600, 1000),
                          ("IPTA DR3 ~2029", 120, 500, 500),
                          ("early SKA ~2034", 200, 780, 200),
                          ("mature SKA ~2040", 500, 780, 100),
                          ("SKA+ ~2045", 3000, 1040, 50)]:
    print(f"{era:>22} | {m_reach(Np, Nep, sig):22.2e} eV")

# the wall: signal at 1e-22 eV is ~21 ps; even 3000 psr x 50 ns leaves R_min ~ 0.1 ns >> 0.021 ns
_, _, R22 = signal(1e-22)
print(f"\nthe wall: R(1e-22 eV) = {R22*1e12:.1f} ps -- no plausible array reaches this (cube-root scaling)")
