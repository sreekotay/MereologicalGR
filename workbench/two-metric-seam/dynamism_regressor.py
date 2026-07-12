"""
THE DYNAMISM REGRESSOR — parametric estimates and regression power.

Premise under test: if the seam scalar B is flux-sourced (Horn C flux-
constitution; bimetric survey form B = 6(H/m_FP)^2 with B ∝ Hdot, f(0)=0,
B -> 0 on stationary regions), a merging source carries a local dynamism
zone with B_loc >> B_cosmo, contributing a near-source cross-messenger lag

    dt_dyn = (1/c) ∫_zone [ 1/sqrt(1-B_loc(r)) - 1 ] dr  ≈  (1/2c) ∫ B_loc dr

on top of the cosmological path term  eps0 * D / c.  Question: size, kernel
branches, regression detectability, and the emission-delay confound.

Anchors:
  - eps0 = 3.8e-16, B0 = 2*eps0                    [C1, GW170817]
  - m_FP = 1.4e-25 eV, B = 6 (H/m_FP)^2            [C9 bimetric survey,
                                                     bianchi_seam_branch.py]
  - GW170817 total gap 1.74 s at ~40 Mpc            [1710.05834]
  - SGRB emission-delay scatter sigma_em ~ 1.5 s    [jet-formation modeling]
"""

import numpy as np

# ---------------------------------------------------------------- constants
c      = 2.998e10          # cm/s
G      = 6.674e-8          # cgs
Msun   = 1.989e33          # g
Mpc    = 3.086e24          # cm
pc     = 3.086e18          # cm
yr     = 3.156e7           # s
eV2rad = 1.519e15          # eV -> rad/s

eps0   = 3.8e-16
H0     = 2.2e-18                       # s^-1
m_FP   = 1.4e-25 * eV2rad              # rad/s
sig_em = 1.5                           # s, SGRB jet-delay scatter

t_g  = lambda M: G*M*Msun/c**3         # s
r_s  = lambda M: 2*G*M*Msun/c**2       # cm

print("="*74)
print("PART 1 — SEAM RESPONSE SCALES")
print("="*74)
B0_pred = 6*(H0/m_FP)**2
print(f"m_FP                       = {m_FP:.3e} rad/s")
print(f"corner period 2pi/m_FP     = {2*np.pi/m_FP/yr:.0f} yr")
print(f"B0 = 6(H0/m_FP)^2          = {B0_pred:.2e}   (anchor B0 = {2*eps0:.2e})")
print(f"path-term slope eps0*Mpc/c = {eps0*Mpc/c*1e3:.1f} ms/Mpc")

# ------------------------------------------------------- source classes
# (name, M_tot [Msun], f_peak [Hz], Mc [Msun], D_typ [Mpc], sigma_em [s])
classes = [
    ("BNS       ", 2.7,  2000., 1.19,   100.,  1.5),
    ("NSBH      ", 8.0,   550., 2.50,   300.,  1.5),
    ("BBH(150914)",65.0,  250., 28.0,   410.,  np.nan),   # no EM counterpart
    ("SMBHB(LISA)",1e7, 1.6e-3, 4.3e6, 1.5e4,  1e6),      # disk-response scatter
]

print()
print("="*74)
print("PART 2 — NEAR-SOURCE KERNEL BRANCHES, dt_dyn per class")
print("="*74)
print("""
Branch 0 (licensed):   bimetric B responds to the coarse-grained cosmological
                       congruence only -> B_loc = B0, dt_dyn ~ eps0 * r_zone/c ~ 0.
Branch S (ceiling):    merger dynamism theta ~ 2*pi*f >> m_FP is 13 decades
                       above the corner; a driven massive mode responds as
                       S/theta^2 (bounded, oscillatory), nonlinearly saturated:
                       |B| <= B_max ~ 1 over the causal zone L = k * r_s only.
                       dt_dyn^max = B_max/2 * L/c = k * B_max * t_g.
Branch W (illicit):    quasi-static form B = 6(theta/m_FP)^2 extrapolated into
                       the wave zone with theta(r) = 2*pi*f * (D h)/r --
                       wrong oscillator physics (1/m^2 response applied above
                       resonance) AND empirically killable: see below.
""")

k_zone, B_max = 100., 1.0     # generous: zone = 100 r_s, saturated seam
print(f"{'class':12s} {'t_g [s]':>10s} {'ceil dt_dyn':>12s} {'D_x (path=ceil)':>16s} "
      f"{'sig_em':>8s} {'ceil/sig_em':>12s} {'ceil/(t_g)':>10s}")
for (nm, M, f, Mc, D, sg) in classes:
    ceil  = k_zone * B_max * t_g(M)                       # s
    Dx    = ceil / (eps0/c) / Mpc                         # Mpc where path term = ceiling
    ratio = ceil/sg if np.isfinite(sg) else np.nan
    print(f"{nm:12s} {t_g(M):10.3e} {ceil:10.2e} s {Dx*1e3:12.1f} kpc "
          f"{sg:8.1e} {ratio:12.1e} {ceil/t_g(M):10.0f}")
print("""
-> the ceiling is 100 t_g at EVERY mass; emission scatter is ~1e5 t_g (BNS:
   1.5 s / 13.3 us; SMBHB: ~1e6 s / 49 s = 2e4 t_g). The ratio
   ceiling/scatter ~ 1e-3..1e-2 is scale-free: all source clocks run on t_g,
   so no mass range escapes. Path term overtakes the ceiling beyond ~30 kpc:
   every extragalactic event is path-dominated.""")

# Branch W self-kill: saturation radius and implied lag for a BNS
Dh   = 4*(G*1.19*Msun/c**2)**(5/3) * (np.pi*2000/c)**(2/3)   # cm (peak, PN est.)
th   = lambda r: 2*np.pi*2000 * Dh / r                        # wave-zone rate
rsat = np.sqrt(6)*2*np.pi*2000*Dh/m_FP                        # 6(th/m)^2 = 1
dtW  = (rsat + rsat/2)/(2*c)                                  # core + tail
print(f"Branch W (BNS): D*h_peak = {Dh:.2e} cm, r_sat = {rsat/pc:.1f} pc, "
      f"dt_dyn ~ {dtW/yr:.0f} yr")
print(f"   vs GW170817 total gap 1.74 s -> excluded by ~{dtW/1.74:.0e}x. "
      f"Branch W is anchor-dead.")

# Sub-corner environmental byproduct: compressive/turbulent flows BELOW corner
th_cl = 1/(1e6*yr)                    # 1/Myr free-fall / eddy rate
B_cl  = 6*(th_cl/m_FP)**2
dt_cl = B_cl/2 * (10*pc)/c
print(f"\nByproduct bound (sub-corner tail of the pointwise-theta kernel):")
print(f"   collapsing/turbulent cloud, theta ~ 1/Myr -> B = {B_cl:.1e} "
      f"(= {B_cl/(2*eps0):.0e} x B0)")
print(f"   10 pc crossing -> dt = {dt_cl:.0f} s  >> 1.74 s anchor.")
print("   Any GW-gamma sightline crossing star-forming gas kills the pointwise")
print("   kernel at this normalization -> belongs to the grad-B face (C9 ledger),")
print("   not to near-source dynamism; noted as a handoff.")

print()
print("="*74)
print("PART 3 — DIMENSIONLESS DYNAMISM MEASURE")
print("="*74)
print("D_hat := (D_L/c) * max|hdot|  (distance-free, from public strain data)")
print(f"{'class':12s} {'D*h_peak [cm]':>14s} {'D_hat':>9s}")
Dhat_vals = []
for (nm, M, f, Mc, D, sg) in classes:
    dh = 4*(G*Mc*Msun/c**2)**(5/3) * (np.pi*f/c)**(2/3)
    dhat = 2*np.pi*f*dh/c
    Dhat_vals.append(dhat)
    print(f"{nm:12s} {dh:14.3e} {dhat:9.3f}")
print("""
-> near mass-invariant (all compact mergers reach v ~ c): D_hat ~ eta*(v/c)^5
   spans only ~[0.005 (q~10), 0.1 (equal-mass)] -- one decade of lever arm.
   Secondary components (mass-ratio eta, disk/accretion flag) widen it but are
   exactly the variables jet-delay models depend on (the confound's variables).""")

print()
print("="*74)
print("PART 4 — REGRESSION POWER:  dt = alpha*K(z) + beta*(1+z)*D_hat + b_c + e")
print("="*74)
sdD = 0.03                       # spread of D_hat across a mixed BNS/NSBH sample
for R2 in (0.0, 0.5):
    print(f"\n collinearity R^2(D_hat leverage vs distance) = {R2}")
    print(f" {'signal spread s = beta*SD(D)':>30s} {'N for 3-sigma':>14s}")
    for s in (1.33e-3, 0.01, 0.1, 0.5):
        N = (3*sig_em/s)**2/(1-R2) if R2 < 1 else np.inf
        tag = " <- Branch-S ceiling (BNS)" if abs(s-1.33e-3) < 1e-6 else ""
        print(f" {s:27.3g} s  {N:14.3g}{tag}")
b_min = lambda N, sig, R2: 3*sig/(sdD*np.sqrt(N*(1-R2)))
print(f"\n reachable beta at N=100, sigma=1.5 s, R^2=0.3:  "
      f"beta_min = {b_min(100,1.5,0.3):.1f} s per unit D_hat "
      f"(signal spread {b_min(100,1.5,0.3)*sdD:.2f} s)")
print(f" timing precision: irrelevant below ~0.3 s -- sigma_eff^2 = sigma_em^2 +")
print(f" sigma_t^2 is emission-dominated for any sigma_t < 0.5 s. The floor is")
print(f" astrophysical, not instrumental.")
print(f"\n GW170817 alone: 1 datum, >=3 parameters (alpha, beta, b) -> ")
print(f" non-identifiable. One point is no regression. Confirmed: NO.")

# ------- identifiability: propagation-dynamism vs emission-dynamism columns
print()
print("="*74)
print("PART 5 — STRUCTURAL CONFOUND: rank of the design matrix")
print("="*74)
rng = np.random.default_rng(1)
N   = 5000
z   = rng.uniform(0.005, 2.0, N)
Dh_ = rng.lognormal(np.log(0.03), 0.5, N)
K   = z/H0/c * Mpc/Mpc                     # ~ comoving-kernel proxy (shape only)
X   = np.column_stack([K,                  # alpha  : path term
                       (1+z)*Dh_,          # beta_prop : near-source dynamism
                       (1+z)*Dh_,          # beta_em   : dynamism-correlated jet delay
                       (1+z)])             # b : mean source-frame offset
print(f" N = {N}, columns = [K(z), (1+z)D (prop), (1+z)D (em), (1+z)]")
print(f" rank(X) = {np.linalg.matrix_rank(X)} of {X.shape[1]} -> singular at every N.")
print(" beta_prop and beta_em multiply the SAME column: both distance-free,")
print(" both source-frame (identical (1+z) dilation), both functions of the")
print(" same source observables. Var(beta_prop - beta_em | GW-gamma data) = inf")
print(" for all N and all timing precision. No population separates them.")

# ------- the one structural breaker: same-leg vs cross-leg (GW-nu vs nu-gamma)
print()
print("="*74)
print("PART 6 — THE ONLY BREAKER: LEG PARITY (nu vs gamma), AND ITS PRICE")
print("="*74)
print(""" Propagation-dynamism is CROSS-LEG: identical for every matter messenger
 (nu and gamma both ride g-tilde) -> cancels exactly in nu-gamma timing.
 Emission-dynamism is per-messenger. Per event:
     dt_GWg = P + E_g ;  dt_GWnu = P + E_nu ;  dt_nug = E_g - E_nu
 2 independent observables, 3 unknowns -> still underdetermined UNLESS E_nu
 carries an external bound. Thermal-nu emission is locked to the merger clock
 (remnant cooling ~ 30 ms), an energetics-bounded prior 50x tighter than any
 jet model -> P per event to +/- 30 ms.""")
sig_nu   = 0.03
horizon  = 3.0                         # Mpc, thermal-nu detection (Hyper-K class)
rate_bns = 300e-9                      # Mpc^-3 yr^-1
r_local  = rate_bns * 4/3*np.pi*horizon**3
N_need   = (3*sig_nu/1.33e-3)**2      # to see the Branch-S ceiling spread
print(f" nu-horizon ~ {horizon:.0f} Mpc -> local BNS rate = {r_local:.1e} /yr")
print(f" N needed at sigma = {sig_nu*1e3:.0f} ms for ceiling signal: {N_need:.0f}")
print(f" -> waiting time ~ {N_need/r_local:.1e} yr. And a single Galactic event")
print(f" (D = 8 kpc): ceiling dt_dyn = {k_zone*t_g(2.7)*1e3:.1f} ms < 30 ms nu floor --")
print(f" even one perfect event cannot resolve the ceiling. Rate-priced out AND")
print(f" precision-floored. The breaker exists structurally, not observationally.")

print()
print("="*74)
print("VERDICT SUMMARY")
print("="*74)
print(""" 1. Amplitude: licensed branch ~0; ceiling branch <= 100 t_g (ms, stellar)
    -- under the emission floor by the scale-free factor ~1e-3 at ALL masses;
    the only large branch (W) is anchor-dead by ~2e8 and physics-dead (above-
    resonance 1/m^2 response).
 2. Regression: beta_tot != 0 is detectable at N ~ 1e2 (s ~ 0.5 s) -- but
    beta_tot != 0 is astrophysically guaranteed (jet delays DO correlate with
    dynamism). Detection confirms astrophysics, not the seam.
 3. Confound: beta_prop and beta_em are the same regression column -- exact
    rank deficiency; redshift scaling identical, lensing common-mode, within-
    signal levers absent. Only leg-parity (GW-nu) breaks it: rate ~ 3e-5/yr
    and still precision-floored above the ceiling.
 DEAD -- doubly: by amplitude in every licensed kernel, by confound in the
 agnostic reading. The death is scale-free (t_g cancels) and messenger-proof.""")
