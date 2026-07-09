import numpy as np

# constants (SI)
hbar = 1.054571817e-34
G = 6.67430e-11
c = 2.99792458e8
eV = 1.602176634e-19
Mpc = 3.0856775814913673e22
kpc = Mpc/1e3
Msun = 1.98892e30
h = 0.674
H0 = h*100*1e3/Mpc  # s^-1
rho_crit = 3*H0**2/(8*np.pi*G)
Om = 0.315
rho_m0 = Om*rho_crit

def m_kg(m_eV):
    return m_eV*eV/c**2

print("=== de Broglie wavelength: lambda = 2*pi*hbar/(m v) ===")
for m22, v in [(1,10e3),(1,100e3),(1,200e3),(10,10e3),(100,10e3),(0.1,10e3)]:
    m = m_kg(m22*1e-22)
    lam = 2*np.pi*hbar/(m*v)
    print(f"m={m22}e-22 eV, v={v/1e3:.0f} km/s: lambda_dB = {lam/kpc:.3g} kpc")

print()
print("=== Quantum Jeans wavenumber (linear theory): k_J = (16 pi G rho_bar a m^2 / hbar^2)^(1/4) ===")
# comoving Jeans scale today (a=1) using mean matter density; standard formula
for m22 in [0.1,1,10,100]:
    m = m_kg(m22*1e-22)
    kJ = (16*np.pi*G*rho_m0*m**2/hbar**2)**0.25  # physical, a=1 -> comoving equal
    print(f"m={m22}e-22 eV: k_J(a=1) = {kJ*Mpc/h:.3g} h/Mpc, lambda_J = {2*np.pi/kJ/Mpc:.3g} Mpc")

print()
print("=== Half-mode scale (Hu, Barkana, Gruzinov 2000 fit): k_1/2 ~ 4.5 (m/1e-22)^(4/9) /Mpc ===")
for m22 in [0.1,1,20,40,200,3000]:
    k12 = 4.5*m22**(4/9)
    M12 = (4*np.pi/3)*rho_m0*(np.pi/k12*Mpc)**3/Msun  # mass within half-mode radius
    print(f"m={m22:g}e-22 eV: k_1/2 = {k12:.3g} /Mpc = {k12/h:.3g} h/Mpc; M_1/2 ~ {M12:.3g} Msun")

print()
print("=== invert: what m gives k_1/2 at Lya scales? ===")
for k in [1.0, 5.0, 10.0, 20.0]:  # h/Mpc
    m22 = (k*h/4.5)**(9/4)
    print(f"k_1/2 = {k} h/Mpc  ->  m = {m22:.3g} x 1e-22 eV")

print()
print("=== Soliton core (Schive+2014): r_c ~ 1.6 kpc (m/1e-22)^-1 (M_h/1e9 Msun)^(-1/3) at a=1 ===")
for m22, Mh in [(1,1e9),(1,1e12),(10,1e9),(30,1e8)]:
    rc = 1.6*(1/m22)*(Mh/1e9)**(-1/3)
    print(f"m={m22}e-22, M_h={Mh:.0e}: r_c ~ {rc:.3g} kpc")

print()
print("=== gravitational-heating / relaxation time check (Dalal-Kravtsov physics) ===")
# density-granule quasiparticle mass: m_eff ~ rho * (lambda_dB/2)^3 scale
for m22, v, rho_msun_pc3 in [(1,5e3,0.1),(100,5e3,0.1),(3000,5e3,0.1)]:
    m = m_kg(m22*1e-22)
    lam = 2*np.pi*hbar/(m*v)
    meff = rho_msun_pc3*Msun/( (kpc/1e3)**3 ) * (lam/2)**3 / Msun
    print(f"m={m22}e-22, v=5 km/s, rho=0.1 Msun/pc^3: lambda={lam/kpc:.3g} kpc, granule mass ~ {meff:.3g} Msun")

print()
print("=== when does ULA start behaving as matter? m vs H: oscillation starts when m ~ H(a) ===")
# H(a)^2 = H0^2 (Or/a^4 + Om/a^3 + OL); find a_osc where m c^2/hbar = H
Or = 9.2e-5
OL = 1-Om-Or

def H(a): return H0*np.sqrt(Or/a**4+Om/a**3+OL)
for m_eV in [1e-33, 1e-27, 1e-24, 1e-22]:
    w = m_eV*eV/hbar  # rad/s
    # bisect
    lo, hi = 1e-10, 1.0
    if w < H(1.0):
        print(f"m={m_eV:.0e} eV: m < H0 -> never oscillates, behaves as dark energy today")
        continue
    for _ in range(200):
        mid = np.sqrt(lo*hi)
        if H(mid) > w: lo = mid
        else: hi = mid
    a_osc = np.sqrt(lo*hi); z_osc = 1/a_osc-1
    print(f"m={m_eV:.0e} eV: starts oscillating at z ~ {z_osc:.3g} (a={a_osc:.3g})")
