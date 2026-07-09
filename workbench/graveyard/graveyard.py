#!/usr/bin/env python3
"""
Anomaly-graveyard statistic: does the record of portal-shaped DM anomalies
discriminate H_drift (coupling just below past sensitivity) from H_zero
(coupling exactly zero; anomalies are flukes/systematics/astro)?

Two levels of analysis:

(A) EPISODE-LEVEL (upper bound on evidence; assumes episode independence)
    Each decisively-resolved episode is a Bernoulli trial "confirm/die".
      H_zero : P(confirm) = eps            (false confirmation: shared
               systematic or repeated fluke)
      H_drift: P(confirm) = f*q + (1-f)*eps
               f = P(anomaly is a genuine threshold crossing | raised, drift)
               q = P(confirmation | genuine, follow-up ~1-2 decades deeper)
    LR(H_zero : H_drift) for k=0 confirms in n trials
      = [(1-eps)/(1 - f q - (1-f) eps)]^n

(B) REGISTER-LEVEL (defensible floor; one coupling per register, episodes
    within a register share it and are NOT independent)
    For register r, sensitivity advanced Delta_r decades (in signal-RATE
    units) beyond the frontier at the time its flagship anomaly was raised.
    Drift prior: log10(true rate) uniform over W decades below that frontier.
      P(frontier crossed true coupling) = min(1, Delta_r / W)
      P(register confirms | drift)      = c_r = q * min(1, Delta_r / W)
      P(register confirms | zero)       = eps
    LR(H_zero : H_drift) for 0 register confirmations
      = prod_r (1-eps)/(1-c_r)
    E[confirmations | drift] = sum_r c_r
"""

import numpy as np
from itertools import product

# ----------------------------------------------------------------------
# Episode table (decisive deaths only enter the count; open/contested don't)
# status: DEAD = decisively closed as a portal signal; OPEN/CONTESTED excluded
episodes_dead = [
    # (name, register, year_raised, year_dead, kill_mode)
    ("DAMA/LIBRA modulation",       "recoil",  1998, 2025, "replication (ANAIS-112 + COSINE-100)"),
    ("CoGeNT excess+modulation",    "recoil",  2010, 2014, "systematics (surface events)"),
    ("CRESST-II excess",            "recoil",  2011, 2014, "systematics (clamp alphas; upgraded detectors)"),
    ("CDMS-II Si 3 events",         "recoil",  2013, 2016, "replication (LUX/SuperCDMS/XENON exclusion)"),
    ("XENON1T ER excess",           "recoil",  2020, 2022, "replication (XENONnT; tritium)"),
    ("3.5 keV line",                "line",    2014, 2025, "replication (Hitomi, blank-sky, XRISM stack)"),
    ("Fermi 130 GeV line",          "line",    2012, 2015, "systematics + faded with data (Pass 8)"),
    ("Positron excess (portal DM interp.)", "flux", 2008, 2017, "astrophysics (pulsar halos) + CMB annihilation bounds"),
    ("AMS antiproton excess",       "flux",    2016, 2020, "systematics (correlated AMS errors -> <1 sigma)"),
    ("DAMPE 1.4 TeV peak",          "flux",    2017, 2023, "replication (CALET incompatible at 4.8 sigma)"),
    ("Stellar cooling hints (WD/HB/RGB)", "cooling", 2012, 2025, "better data (47 Tuc WDs, improved RGB/R-parameter bounds)"),
    ("EDGES 21-cm absorption",      "thermal", 2018, 2022, "replication (SARAS-3 rejects at 95.3%)"),
    ("Muon g-2 (dark-photon portal interp.)", "precision", 2001, 2025, "theory (lattice SM) + replication (BaBar/NA64 killed dark photon earlier)"),
]
episodes_open = [
    ("GC GeV excess",        "flux",  2009, "contested: MSP population vs DM annihilation"),
    ("511 keV bulge line",   "line",  2003, "contested: astrophysical positron sources plausible, morphology debated"),
    ("ATOMKI X17",           "precision", 2016, "contested: MEG II disfavors (94% CL), PADME 2.5 sigma bump"),
    ("Isotropic cosmic birefringence", "thermal", 2020, "open: beta=0.30+-0.05 deg (~3.6 sigma), calibration-limited"),
]
n = len(episodes_dead)   # decisive deaths
k = 0                    # confirmations

# ----------------------------------------------------------------------
# (A) Episode-level LR range over judgment-call grid
print(f"Decisive deaths n = {n}, confirmations k = {k}, open/contested = {len(episodes_open)}\n")
print("(A) EPISODE-LEVEL (independence assumed -> UPPER BOUND on evidence)")
print(f"{'f':>5} {'q':>5} {'eps':>6} {'P(conf|drift)':>14} {'LR(zero:drift)':>15}")
for f, q, eps in product([0.2, 0.4, 0.6, 0.8], [0.5, 0.7, 0.9], [0.01, 0.05]):
    p = f*q + (1-f)*eps
    LR = ((1-eps)/(1-p))**n
    print(f"{f:5.1f} {q:5.1f} {eps:6.2f} {p:14.3f} {LR:15.3g}")

# ----------------------------------------------------------------------
# (B) Register-level floor
# Delta_r: decades of SIGNAL-RATE sensitivity gained between flagship-anomaly
# era and its decisive resolution (conservative estimates):
#   recoil : DAMA-era (~1998) frontier -> LZ/XENONnT 2024: SI sigma ~1e-42 ->
#            ~2e-48 cm^2  => ~5.5 decades in rate
#   line   : XMM stacked-cluster 2014 -> XRISM 2025 stack: ~1.2 decades in Gamma
#   flux   : PAMELA 2008 -> AMS-02 + CALET/DAMPE: ~2 decades in statistics/E-reach
#   cooling: 2012-era WD/HB hints -> 47 Tuc WD + Gaia-era RGB: ~0.7 decade in
#            emissivity (~0.35 in coupling^2 ... expressed in rate units)
#   thermal: EDGES 2018 -> SARAS-3: comparable instrument, ~0.3 decade (a
#            replication at similar depth, not a deeper probe)
registers = {  # name: Delta_r (rate decades traversed post-anomaly)
    "recoil": 5.5, "line": 1.2, "flux": 2.0, "cooling": 0.7, "thermal": 0.3,
}
# 'precision' register (g-2, X17) excluded from floor: kill was partly
# theory-side, keep the floor conservative.

print("\n(B) REGISTER-LEVEL FLOOR (one shared coupling per register)")
print("Drift prior width W = decades of log10(rate) below episode-era frontier")
print(f"{'W':>4} {'q':>5} {'eps':>6} {'E[k|drift]':>11} {'P(0|drift)':>11} {'LR(zero:drift)':>15}")
for W, q, eps in product([1.0, 2.0, 5.0, 10.0], [0.5, 0.7, 0.9], [0.02]):
    c = {r: q*min(1.0, d/W) for r, d in registers.items()}
    Ek = sum(c.values())
    P0_drift = np.prod([1-ci for ci in c.values()])
    P0_zero  = (1-eps)**len(registers)
    LR = P0_zero / P0_drift
    print(f"{W:4.0f} {q:5.1f} {eps:6.2f} {Ek:11.2f} {P0_drift:11.3g} {LR:15.3g}")

# ----------------------------------------------------------------------
# Forward form: LR increment per future decisive resolution, and the
# asymmetry: what one confirmation does.
print("\nFORWARD FORM")
eps = 0.02
for label, p in [("tight-drift episode (p_conf=0.5)", 0.5),
                 ("mid-drift episode  (p_conf=0.3)", 0.3),
                 ("loose-drift episode (p_conf=0.1)", 0.1)]:
    print(f"  future DEATH   multiplies LR(zero:drift) by {(1-eps)/(1-p):5.2f}  [{label}]")
    print(f"  future CONFIRM multiplies LR(zero:drift) by {eps/p:6.3f} "
          f"(i.e., x{p/eps:.0f} FOR drift) [{label}] -- and H_zero(g=0 exactly) is logically falsified")
