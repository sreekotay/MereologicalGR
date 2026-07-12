import numpy as np

# ---------- Framework signal ----------
B      = 1e-16
dOmega = B/6.0            # |Omega - 1| ~ B/6  (Omega^2-1 = -B/3)
# duality signal: d_L^GW/d_L^EM - 1 = ln-ish Omega(z_s)/Omega(0) - 1 <= |Omega-1| variation
sig_conformal = dOmega    # ~1.7e-17 (MAXIMAL, requires O(1) cosmological evolution of B)
sig_disformal = B/2       # endpoint O(B) pieces from u(x)u term (also requires B to evolve)
print(f"Framework signal (conformal, max): |R-1| <~ {sig_conformal:.2e}")
print(f"Framework signal (disformal endpoint, max): |R-1| <~ {sig_disformal:.2e}")
print(f"If B, Omega constant: signal = 0 exactly (constant conformal factor = unit choice)\n")

# ---------- GW170817 today ----------
dgw, dgw_p, dgw_m = 43.8, 2.9, 6.9      # Mpc, LVC PE with EM sky location
dem, dem_e        = 40.7, np.hypot(1.4, 1.9)  # Cantiello+18 SBF: 40.7 +/- 1.4stat +/- 1.9sys
z17 = 0.00968                            # cosmological (Hubble-flow corrected ~0.00980 vs helio .00968; use LVC)
sgw = 0.5*(dgw_p + dgw_m)               # symmetrized
R   = dgw/dem
sR  = R*np.hypot(sgw/dgw, dem_e/dem)
print(f"GW170817: d_GW = {dgw}+{dgw_p}-{dgw_m} Mpc ; d_EM(SBF) = {dem} +/- {dem_e:.1f} Mpc")
print(f"  R = d_GW/d_EM = {R:.3f} +/- {sR:.3f}   (R-1 = {R-1:.3f} +/- {sR:.3f})")
print(f"  1-sigma bound |R-1| <~ {sR:.2f} ; 2-sigma <~ {2*sR:.2f}")
# local friction: R-1 ~ -delta(0) * z  =>  delta(0) bound
print(f"  implied |delta(0)| ~ |R-1|/z = {sR/z17:.0f}  (lit: delta(0) = -7.8 +9.7/-18.4, Belgacem+18)")
# with VLBI jet-inclination prior the GW distance error ~7%
sR_vlbi = R*np.hypot(0.07, dem_e/dem)
print(f"  with VLBI jet constraint (7% GW dist): |R-1| <~ {sR_vlbi:.3f} (1-sigma)\n")

# ---------- 3G forecasts ----------
# bright sirens ET(+CE): per-event distance precision
per_event = {'typical bright siren (incl. degeneracy)': 0.10,
             'with EM jet/KN inclination info':          0.03,
             'golden events':                            0.01}
for k,v in per_event.items(): print(f"  per-event sigma_d/d: {k}: {v:.0%}")
for N, s in [(100,0.10),(1000,0.05),(10000,0.05)]:
    print(f"  N={N:>6}, per-event {s:.0%}: statistical floor {s/np.sqrt(N):.1e}")
# systematics floor
print("""  systematics: amplitude calibration ~0.5% now -> 0.1-0.5% (3G goal, correlated!)
               waveform systematics ~0.5-1% ; lensing (z~1) 1-5%/event, averages but biased tail
               EM absolute-distance anchor ~1-2% ; peculiar velocities (low z) ~1-2%""")
asymptotic = 1e-3
print(f"  realistic asymptotic bound on |R-1|: ~{asymptotic:.0e} (optimistic few x 1e-4)\n")

# ---------- The gap ----------
print(f"Current bound / signal  = {sR/sig_conformal:.1e}   ({np.log10(sR/sig_conformal):.1f} orders)")
print(f"Asymptotic bound / signal = {asymptotic/sig_conformal:.1e}   ({np.log10(asymptotic/sig_conformal):.1f} orders)")

# ---------- Xi0 translation ----------
# Xi(z) = Xi0 + (1-Xi0)/(1+z)^n ;  endpoint conformal model: Xi(z) = Omega(z)/Omega_0
# GWTC-4 dark sirens: Xi0 = 1.2 +0.8/-0.4 ; ET+CMB+BAO+SNe forecast: dXi0 ~ 0.8% ; LISA ~1-4%
for name, dXi in [("GWTC-4 dark sirens (now)", 0.6), ("ET bright sirens + ext. data", 0.008),
                  ("ET+CE spectral (BNS mass fn)", 0.06), ("LISA MBHB", 0.03)]:
    print(f"  {name:35s} sigma(Xi0) ~ {dXi:.3f}  ->  |dln Omega| < {dXi:.1e}  vs signal {dOmega:.1e}")
