#!/usr/bin/env python3
"""
Clock-interferometry / collapse-model crossover:
Do MAGIS-100-class atom interferometers touch the surviving parameter space of
gravitationally motivated collapse models?

Bounds used (2026 status):
 - DP (Markovian, stochastic):  R0 > 2.8e-9 m   [XENONnT PRL 2026, arXiv:2506.05507]
       earlier: R0 > 0.54e-10 m [Donadi et al., Nat. Phys. 17, 74 (2021)]
                R0 ~> 4.9e-10 m [Majorana Demonstrator, PRL 129, 080401 (2022)]
 - CSL (white noise, mass-prop): lambda/r_c^2 < 3.0e-3 /s/m^2  [XENONnT 2026]
       => at r_c = 1e-7 m: lambda < 3.0e-17 /s  (GRW value 1e-16 EXCLUDED, white noise)
   colored/dissipative CSL: X-ray bound evaporates; best remaining ~mechanical:
       lambda <~ 1e-11..1e-9 at r_c ~ 1e-7 m (ultracold cantilever PRL 125,100404;
       LISA-PF translational/rotational, PRA 111, L020203 (2025))
 - KTM: already ruled out by single-atom interferometry
       [Altamirano, Corona-Ugalde, Mann, Zych, CQG 35, 145005 (2018)]

Instrument (MAGIS-100, Abe et al., Quantum Sci. Technol. 6, 044003 (2021)):
  Sr-87, wavepacket separation up to ~ meters (LMT n=100 -> ~10 m ultimate),
  interferometer time up to 9 s (full 100 m launch), phase noise 1e-3 rad/rtHz
  (=> ~1e6 atoms/shot at shot noise), upgrades: 1e8 atoms/s + squeezing.
"""
import numpy as np

hbar = 1.0546e-34
G    = 6.674e-11
amu  = 1.6605e-27

# ----- instrument -----
A_Sr   = 87                    # nucleons in Sr-87
m_atom = A_Sr * amu
dx     = 1.0                   # m, wavepacket separation (design: meter-scale)
t_int  = 9.0                   # s, max interferometer time (100 m launch)
N_atoms_shot = 1e6             # per shot (shot-noise 1e-3 rad)
shots_campaign = 1e7           # ~1 yr at ~0.3 Hz

dC_shot  = 1/np.sqrt(N_atoms_shot)                       # per-shot contrast stat. error
dC_camp  = 1/np.sqrt(N_atoms_shot*shots_campaign)        # campaign statistical floor
dC_real  = 1e-3                                          # realistic systematics floor (0.1%)

print("=== detectability floors (anomalous contrast loss) ===")
print(f" per-shot statistical floor      : {dC_shot:.1e}")
print(f" campaign statistical floor      : {dC_camp:.1e}  (1e6 at/shot x 1e7 shots)")
print(f" realistic systematics floor     : {dC_real:.1e}")

# ----- CSL: single-atom decoherence rate -----
# mass-proportional CSL, point particle (atom radius << r_c):
# Gamma = lambda * (m/m0)^2 * [1 - exp(-dx^2/(4 r_c^2))] ; m0 = 1 amu (nucleon)
def gamma_csl(lam, r_c, dx=dx, N=A_Sr):
    return lam * N**2 * (1 - np.exp(-dx**2/(4*r_c**2)))

print("\n=== CSL: single Sr-87 atom, dx = 1 m, t = 9 s ===")
cases = [
    ("GRW value (1e-16, 1e-7 m)  [DEAD, white noise, XENONnT]", 1e-16, 1e-7),
    ("XENONnT ceiling at r_c=1e-7 (3e-17)",                     3e-17, 1e-7),
    ("colored-CSL mech. ceiling r_c=1e-7 (~1e-11)",             1e-11, 1e-7),
    ("Adler value (1e-8, 1e-7 m) [DEAD, cantilever+LISA-PF]",   1e-8,  1e-7),
    ("large r_c = 1e-4 m, X-ray ceiling lam=3e-3*r_c^2",        3e-3*(1e-4)**2, 1e-4),
    ("large r_c = 1e-2 m, X-ray ceiling",                       3e-3*(1e-2)**2, 1e-2),
]
for name, lam, rc in cases:
    g = gamma_csl(lam, rc)
    print(f" {name:57s}: Gamma={g:.2e}/s  loss(9s)={g*t_int:.2e}")

# lambda reach of MAGIS contrast measurement (dx >> r_c saturated regime)
lam_1pct = 0.01 / (A_Sr**2 * t_int)
lam_stat = dC_camp / (A_Sr**2 * t_int)
lam_real = dC_real / (A_Sr**2 * t_int)
print(f"\n lambda reach @1%/shot loss        : {lam_1pct:.2e} /s")
print(f" lambda reach @0.1% (realistic)    : {lam_real:.2e} /s")
print(f" lambda reach @stat floor (~3e-7)  : {lam_stat:.2e} /s")
print("   (valid for ALL r_c from ~1e-14 m up to ~dx; interferometric, noise-spectrum-independent)")

# where does MAGIS beat the world's best (X-ray) bound? lam_xray = 3e-3 * r_c^2
for lam_reach, tag in [(lam_1pct,"1%/shot"), (lam_real,"0.1% realistic"), (lam_stat,"stat floor")]:
    rc_cross = np.sqrt(lam_reach/3e-3)
    print(f" beats X-ray bound for r_c > {rc_cross:.1e} m   ({tag})")

# ----- DP: single-atom rate -----
# Gamma_DP = G m_nuc^2 / (hbar sqrt(pi) R0) * [1 - ...] , dx >> R0 saturated
def gamma_dp(R0, m=m_atom):
    return G * m**2 / (hbar * np.sqrt(np.pi) * R0)

print("\n=== DP: single Sr-87 atom, dx >> R0, t = 9 s ===")
for R0, tag in [(0.54e-10,"Donadi-2021 edge"), (4.9e-10,"Majorana-era edge"),
                (2.8e-9,"XENONnT-2026 edge (SURVIVING)")]:
    g = gamma_dp(R0)
    print(f" R0={R0:.2e} m ({tag:28s}): Gamma={g:.2e}/s  loss(9s)={g*t_int:.2e}")

g_dp = gamma_dp(2.8e-9)
print(f" shortfall vs stat floor : {dC_camp/(g_dp*t_int):.1e}x")
print(f" shortfall vs 1%/shot    : {0.01/(g_dp*t_int):.1e}x")

# ----- what mass DOES reach surviving DP? (solid particle, R0 > lattice const) -----
# Gamma ~ (G/(hbar sqrt(pi) R0)) * M * rho*(4pi/3)R0^3   (coherent nuclei within R0)
rho = 2200.0  # silica
R0  = 2.8e-9
def gamma_dp_solid(M, R0=R0, rho=rho):
    m_ball = rho * (4/3)*np.pi*R0**3
    return G * M * m_ball / (hbar*np.sqrt(np.pi)*R0)

print("\n=== DP reach of nanoparticle programs (silica, R0=2.8e-9 m surviving edge) ===")
for M_amu, t, tag in [(1e8,100,"MAQRO-class 1e8 amu, 100 s"),
                      (1e10,100,"MAQRO baseline 1e10 amu, 100 s"),
                      (1e13,100,"1e13 amu, 100 s")]:
    g = gamma_dp_solid(M_amu*amu)
    print(f" {tag:32s}: Gamma={g:.2e}/s  loss={g*t:.2e}")
M_needed = 0.01/(100*gamma_dp_solid(amu))  # amu for 1% at 100 s (Gamma linear in M)
print(f" mass for 1% loss in 100 s       : {M_needed:.1e} amu")

# ----- CSL reach of nanoparticle programs (r_c=1e-7) -----
print("\n=== CSL reach, MAQRO-class (dx ~ 100 nm ~ r_c, t=100 s) ===")
for M_amu, t in [(1e8,100),(1e10,100)]:
    lam_reach = 0.1/( (M_amu)**2 * t * (1-np.exp(-0.25)) )  # dx = r_c
    print(f" M={M_amu:.0e} amu: detects lambda > {lam_reach:.1e}/s (10% loss)"
          f"   [GRW floor 2.2e-17, XENONnT ceiling 3e-17]")

# ----- clock-state (internal) channel: collapse blindness -----
dE = 1.78 * 1.602e-19          # 698 nm Sr clock transition, J
dm_over_m = dE/(m_atom*(3e8)**2)
print("\n=== clock-state channel ===")
print(f" internal superposition mass difference dm/m = {dm_over_m:.1e}")
print(f" CSL rate ratio internal/spatial ~ (dm/m)^2 = {dm_over_m**2:.1e}  -> collapse-blind null channel")
