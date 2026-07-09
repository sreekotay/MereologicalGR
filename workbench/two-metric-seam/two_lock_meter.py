#!/usr/bin/env python3
"""Price the two-lock (two-cone) imprint on accelerated-charge radiation.

Sector split: matter/EM on cone c; fabric/GW on cone c(1+eps), eps <= few e-16.
KMS locks: T_matter = hbar a/(2 pi c k_B), T_fabric = T_matter/(1+eps).
"""
import numpy as np

# CODATA-ish constants (SI)
c      = 2.99792458e8
G      = 6.67430e-11
hbar   = 1.054571817e-34
kB     = 1.380649e-23
e      = 1.602176634e-19
eps0   = 8.8541878128e-12
me     = 9.1093837015e-31
mp     = 1.67262192369e-27
alpha  = e**2/(4*np.pi*eps0*hbar*c)
EPl_J  = np.sqrt(hbar*c**5/G)          # Planck energy
EPl_eV = EPl_J/e
Mpc    = 3.0856775814913673e22

eps_cone = 1e-16   # fiducial two-cone split

print("="*72)
print("0) KMS locks")
Tcoef = hbar/(2*np.pi*c*kB)
print(f"   T_U = {Tcoef:.3e} K per (m/s^2);  a for 1 K = {1/Tcoef:.2e} m/s^2")
for name,a in [("LEP-like synchrotron (gamma^2 c^2/rho, gamma=2e5, rho=3096 m)", (2e5)**2*c**2/3096),
               ("strong-laser electron (E~1e15 V/m)", e*1e15/me),
               ("magnetar/curvature e- (gamma=1e7, rho=1e4 m)", (1e7)**2*c**2/1e4)]:
    T = Tcoef*a
    print(f"   a = {a:.2e} m/s^2  ->  T_U = {T:.3e} K ; DeltaT(two-lock) = {eps_cone*T:.2e} K   [{name}]")

print("="*72)
print("1b) Gravitational vs EM bremsstrahlung of the SAME accelerated particle")
# 'gravitational fine structure' kappa = 4 pi eps0 G m^2 / q^2 = (m/M_Pl)^2/alpha for q=e
for name,m in [("electron",me),("proton",mp)]:
    kappa = 4*np.pi*eps0*G*m**2/e**2
    print(f"   {name}: kappa = Gm^2/(e^2/4pi eps0) = {kappa:.2e}"
          f"   [(m c^2/E_Pl)^2/alpha = {((m*c**2/EPl_J)**2/alpha):.2e}]")
    # circular motion: P_EM = e^2 a^2 gamma^4/(6 pi eps0 c^3) with a=lab accel; using proper accel a_p:
    # P_EM = e^2 a_p^2/(6 pi eps0 c^3);  P_GW(quadrupole, circular) = 32 G m^2 r^4 w^6/(5 c^5)
    #      = (32/5)(G m^2/c^5) a_p^2 (v/c)^2 / gamma^4 ... parametrically P_GW/P_EM = (48/5) kappa (v/c)^2
    for beta in [0.99, 1e-3]:
        R = (48/5)*kappa*beta**2
        print(f"      P_grav/P_EM (circular, v/c={beta}) = {R:.2e}")
    Rbest = (48/5)*kappa*0.99**2
    print(f"      eps-imprint via GW channel on total radiated observable ~ eps*R = {eps_cone*Rbest:.2e}")

print("="*72)
print("1c) interference / phase-space edge")
print("   photon(spin-1, matter cone) and graviton(spin-2, fabric cone) final states are")
print("   orthogonal -> no cross term in any inertial rate; edge shift is O(eps) ON TOP of")
print("   the GW channel -> same size as (1b): ~ eps * (48/5) kappa (v/c)^2")
# Gertsenshtein-type coherent mixing needs background B; conversion prob over L:
B, L = 10.0, 1e4  # 10 T over 10 km, wildly optimistic
Pgp = (np.sqrt(4*np.pi*G)/c**2 * B * L / np.sqrt(4*np.pi/ (4*np.pi*eps0*1e-7*c**2*4*np.pi)) if False else
       4*np.pi*G*B**2*L**2/(1e-7*4*np.pi*c**4*4*np.pi))  # ~ (kappa_g B L)^2/4, kappa_g=sqrt(16 pi G)^(1/2)/...
# do it cleanly: P = (1/4) * (sqrt(16 pi G)/c^2)^2 * (B^2/mu0) * L^2  (Gertsenshtein, natural-ish SI)
mu0 = 4e-7*np.pi
Pgp = (16*np.pi*G/c**4) * (B**2/mu0) * L**2 / 4
print(f"   Gertsenshtein photon<->graviton mixing (B=10 T, L=10 km): P ~ {Pgp:.1e}; eps-part ~ {Pgp*eps_cone:.1e}")

print("="*72)
print("1d) loop: photon self-energy with internal graviton on the outer cone")
for name,a in [("laser a=1.8e26",e*1e15/me), ("magnetar a=9e26",(1e7)**2*c**2/1e4)]:
    T = Tcoef*a
    Egam_eV = kB*T/e  # typical KMS-scale photon energy
    delta = (Egam_eV/EPl_eV)**2
    print(f"   {name}: E_gamma ~ {Egam_eV:.2e} eV -> (E/E_Pl)^2 = {delta:.1e}; eps-sensitive part ~ {delta*eps_cone:.1e}")
# even at 1 TeV photons:
print(f"   even E_gamma = 1 TeV: eps*(E/E_Pl)^2 = {eps_cone*(1e12/EPl_eV)**2:.1e}")

print("="*72)
print("2) CLMV-class precision on the thermal factor")
# systematics floor: T_U proportional to proper acceleration a -> needs |da/a|, field calibration,
# absolute spectral radiometry. State-of-art absolute radiometry ~1e-3..1e-4; accelerator field
# knowledge ~1e-4..1e-6. Statistical floor for context:
rate, t = 1e20, 3.15e7   # absurdly generous: 1e20 tagged photons/s for a year
N = rate*t
print(f"   statistics-only floor with 1e20 photons/s for 1 yr: 1/sqrt(N) = {1/np.sqrt(N):.1e}")
print("   systematics floor (a-calibration + radiometry): ~1e-3 .. 1e-6 on the thermal factor")
print(f"   needed to split two locks: {eps_cone:.0e}  -> shortfall >= 10 orders even if the")
print("   fabric factor appeared in the EM spectrum at O(1) weight -- which it does not.")

print("="*72)
print("3) suppression chain, best charge channel (electron, v~c):")
kap_e = 4*np.pi*eps0*G*me**2/e**2
chain = eps_cone * (48/5)*kap_e
print(f"   eps({eps_cone:.0e}) x [P_GW/P_EM = (48/5)Gm_e^2 4pi eps0/e^2 = {(48/5)*kap_e:.1e}]")
print(f"   = {chain:.1e} fractional imprint on the total radiated observable")
print(f"   vs best conceivable spectral precision 1e-6:  deficit = {np.log10(1e-6/chain):.0f} orders of magnitude")

print("="*72)
print("4) systems radiating into BOTH cones (the real meter)")
D = 40*Mpc
dt = eps_cone*D/c
print(f"   BNS at 40 Mpc: arrival split Delta t = eps*D/c = {dt:.2f} s for eps=1e-16")
print(f"   GW170817/GRB170817A bound: -3e-15 < (v_gw-c)/c < +7e-16 ; fabric-faster sign -> eps <= 7e-16")
print(f"   eps sensitivity per second of timing at 40 Mpc: {1.0/(D/c):.1e}")
D2 = 400*Mpc
print(f"   future BNS at 400 Mpc with 0.1 s emission-model error: eps ~ {0.1/(D2/c):.1e}")
# pulsar spin-down partition
print("   Crab pulsar: LIGO O3 bound P_GW < ~1e-4 of spin-down; partition known to ~%, not 1e-16")
