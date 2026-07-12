"""
Translation of the thermality-onset engagement map to BEC analog horizons
(Steinhauer-class). Anchors (from de Nova et al Nature 569, 688 (2019) and
Kolobov et al Nat. Phys. 17, 362 (2021); values flagged where from memory /
search snippets rather than verified full text):
  T_H ~ 0.35 nK  (predicted from measured flow, ratio measured 0.97 +/- 0.09)
  kappa = 2 pi k_B T_H / hbar
  sound speed (outside) c_out ~ 0.57 mm/s ; healing length ~ 2 um [flagged]
  step sweep speed ~ 0.21 mm/s [flagged]; condensate ~ 100-200 um, lifetime ~ 0.1-0.5 s
Engagement-map thresholds derived in onset_curve.py (a -> kappa, tau -> lab time
for the emitted phonons; c -> c_s):
  smooth window:   Q_DB(band .5-2) = 17.9/(k Dt)^2 ; fitted-T bias = +13.2/(k Dt)^2
                   Planck-shape residual = 113/(k Dt)^2
  C^1 (cos^2) ramps: Q_DB(band .25-1) += 8.0/(k^2 tau_r Dt)
  drift: dT/T in band <~ 0.15 (kappadot/k^2)^2 + 0.18 (kappaddot/k^3)
"""
import numpy as np
hbar, kB = 1.054571817e-34, 1.380649e-23

TH = 0.35e-9
kappa = 2*np.pi*kB*TH/hbar
print(f"kappa = 2 pi kB T_H / hbar = {kappa:.3g} s^-1   (T_H = 0.35 nK)")
print(f"correlation time 1/kappa = {1e3/kappa:.2f} ms ; thermal period 2pi/kappa = {2e3*np.pi/kappa:.1f} ms")

print("\nOnset thresholds (smooth engagement), hold time Dt after formation:")
for Q, name in [(0.10, "10%"), (0.01, "1%")]:
    kDt_DB   = np.sqrt(17.9/Q)
    kDt_bias = np.sqrt(13.2/Q)
    kDt_shape= np.sqrt(113.0/Q)
    print(f"  {name:>4} detailed balance: kappa*Dt = {kDt_DB:5.1f}  -> Dt = {1e3*kDt_DB/kappa:6.1f} ms")
    print(f"  {name:>4} fitted-T bias   : kappa*Dt = {kDt_bias:5.1f}  -> Dt = {1e3*kDt_bias/kappa:6.1f} ms")
    print(f"  {name:>4} Planck shape    : kappa*Dt = {kDt_shape:5.1f}  -> Dt = {1e3*kDt_shape/kappa:6.1f} ms")

print("\nFormation-ramp (edge) axis, cos^2-like ramps of duration tau_r:")
for tr_ms in [2, 5, 10, 20, 40]:
    tr = tr_ms*1e-3
    ktr = kappa*tr
    for Dt_ms in [50, 150]:
        Dt = Dt_ms*1e-3
        Q_edge = 8.0/(ktr*kappa*Dt)
        print(f"  tau_r = {tr_ms:3d} ms (k tau_r = {ktr:5.1f}), Dt = {Dt_ms:3d} ms: edge Q ~ {Q_edge:.3f}")

print("\nDrift axis (kappadot/kappa^2 scan):")
for xi in [0.01, 0.05, 0.1, 0.3, 0.5]:
    print(f"  xi = kappadot/k^2 = {xi:5.2f}: in-band dT/T ~ {0.15*xi**2:.2e} ;"
          f" Planck window closes at omega/kappa ~ {0.39/xi:6.1f} (100%) / {0.12/xi:5.1f} (10%)")

print("\nSpectral resolution needed: dOmega ~ 0.1 kappa =", f"{0.1*kappa:.0f} s^-1")
cs = 0.57e-3  # m/s, outside sound speed [flagged]
print(f"  correlation-window length L >~ 2 pi c_s/(0.1 kappa) = {2*np.pi*cs/(0.1*kappa)*1e6:.0f} um  (c_s = 0.57 mm/s)")
print(f"  c_s/kappa (horizon 'Planck-band' wavelength scale) = {cs/kappa*1e6:.1f} um")

print("\nExisting bracket: Kolobov 2021 ramp-up of Hawking signal over ~ one")
print("oscillation period; our curve: signal within ~20% of thermal at k*Dt ~ 10")
print(f"  -> Dt ~ {1e4/kappa:.0f} ms; within 10% (DB) at {1e3*13.4/kappa:.0f} ms; 1% at {1e3*42.3/kappa:.0f} ms")
