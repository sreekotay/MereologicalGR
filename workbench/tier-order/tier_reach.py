#!/usr/bin/env python3
"""
tier_reach.py -- the tier-reach map for a single-coupling Yukawa portal.

Question: does the interface decomposition I = (kernel, carrier, record)
predict an ORDER in which a genuine portal shows up across meters?

Portal: one scalar phi, mass m, coupling  L = g * phi * Nbar N  (per nucleon).
One coupling g, one mass m. For each tier we compute the minimum detectable
g as a function of m (decade-level; anchors from published exclusions).

Tier meters and their g-scaling (the structural core):

  KERNEL      fifth-force / EP tests.  Observable = static potential
              V = -(g^2/4pi) e^{-mr}/r between lab masses.
              signal ~ g^2 * N_source   (amplifier: macroscopic source,
              ALWAYS available; but range e^{-mr} dies for m >~ hbar*c/mm)

  CARRIER     production metering: stellar/SN energy loss, beam dumps,
              collider missing-energy.  signal ~ g^2 * (thermal/beam
              phase space)  (amplifier: on-shell production, available
              iff m < T_source or m < sqrt(s))

  RECORD-FLUX conversion-to-record of a NATURE-SOURCED FLUX that itself
              required g to be produced (helioscope-style absorption).
              signal ~ g^2(produce) * g^2(convert) = g^4
              (amplifiers: solar volume, detector N_T * exposure; no
              cosmological assumption)

  RECORD-RELIC conversion-to-record of a COSMOLOGICAL CONDENSATE
              (phi = the dark matter; oscillating classical field).
              delta m_N / m_N = g * sqrt(2 rho_DM)/(m * m_N) * cos(mt)
              signal ~ g^1 * sqrt(rho)/m   (amplifier: the relic density
              -- an ASSUMPTION, not an apparatus choice)

Note the degeneracy: for a scalar portal the "lab-sourced record" test
(source the field yourself, then convert it) IS the kernel test -- both
vertices in the lab. Record only becomes a distinct tier when nature
supplies at least one vertex (flux: one; relic: both-and-more).

Anchor sources (decade-level; arXiv/APS were 403 in this environment, all
numbers are from the published exclusions as compiled in reviews):
  kernel:  Murata & Tanaka CQG 32 (2015) 033001 [inverse-square compilation];
           Lee et al. PRL 124 (2020) 101101 [Eot-Wash, alpha=1 at 38.6 um];
           Wagner et al. CQG 29 (2012) 184002 [EP torsion, alpha~1e-11];
           MICROSCOPE final PRL 129 (2022) 121102 [eta = -1.5e-15 +- 2.3e-15]
  carrier: Hardy & Lasenby JHEP 1702 (2017) 033 [stellar g_N ~ 1e-12];
           Raffelt SN1987A-type g_N ~ 3e-9 to m~100 MeV; beam dumps ~1e-5
           (E137/NA62-class, MeV-GeV); LHC dijet/monojet ~0.3 (GeV-TeV)
  record-flux: XENON1T solar-ALP style absorption reach (PRD 102 (2020)
           072004): trails stellar-cooling carrier bound by ~1.5 decades
  record-relic: clock/cavity ultralight-scalar searches (Hees et al. PRL 117
           (2016) 061301; Kennedy et al. PRL 125 (2020) 201302; Arvanitaki,
           Huang, Van Tilburg PRD 91 (2015) 015015): fractional-frequency
           amplitude ~1e-16 today, ~1e-19 nuclear-clock class
"""

import numpy as np

# ---------------------------------------------------------------- constants
hbarc = 1.97327e-7        # eV * m
mN    = 9.389e8           # eV
MPl   = 1.22089e28        # eV (non-reduced)
rhoDM = 3.07e-6           # eV^4  (= 0.4 GeV/cm^3 local DM density)

# alpha (strength relative to gravity between nucleons) <-> g
G2A = MPl**2 / (4*np.pi*mN**2)          # alpha = G2A * g^2  (= 1.34e37)
def g_of_alpha(a): return np.sqrt(np.asarray(a) / G2A)

# ------------------------------------------------------------- KERNEL tier
# (lambda [m], alpha_limit) anchors, log-log interpolated.
_kernel_anchors = np.array([
    (1e-9,  1e26),   # sub-nm: neutron scattering / Casimir, very weak
    (1e-8,  1e20),
    (1e-7,  1e14),   # Casimir band
    (1e-6,  1e9),    # Stanford/IUPUI cantilever class
    (1e-5,  1e4),
    (3.9e-5, 1.0),   # Lee et al. 2020: gravity-strength ruled out above 38.6 um
    (1e-4,  1e-2),
    (1e-3,  3e-5),   # Eot-Wash ISL mm band
    (1e-2,  1e-6),   # Irvine class
    (1e0,   1e-9),
    (1e4,   1e-9),   # lake/tower geophysics plateau
    (1e7,   3e-13),  # MICROSCOPE / EP long-range
    (1e14,  3e-13),
])
def g_kernel(m_eV):
    lam = hbarc / m_eV
    la, aa = np.log10(_kernel_anchors[:,0]), np.log10(_kernel_anchors[:,1])
    lgl = np.log10(lam)
    if lgl < la[0]:            # range shorter than any probe: no kernel reach
        return np.inf
    alpha = 10**np.interp(lgl, la, aa)
    return float(g_of_alpha(alpha))

# ------------------------------------------------------------ CARRIER tier
def g_carrier(m_eV):
    lims = []
    # stellar interiors (HB/RGB), T ~ 8.6 keV; rate ~ g^2 exp(-m/T)
    T_hb = 8.6e3
    lims.append(1e-12 * np.exp(min(m_eV/(2*T_hb), 400.0)))
    # SN1987A, T ~ 30 MeV
    T_sn = 3e7
    lims.append(3e-9 * np.exp(min(m_eV/(2*T_sn), 400.0)))
    # proton beam dumps / rare meson decays, ~MeV..GeV
    if 1e6 <= m_eV <= 1e9:  lims.append(1e-5)
    # colliders, ~GeV..few TeV
    if 1e8 <= m_eV <= 3e12: lims.append(0.3)
    return min(lims)

# -------------------------------------------------------- RECORD-FLUX tier
def g_record_flux(m_eV):
    # solar-flux absorption: rate ~ g^4; reach trails the stellar carrier
    # bound by ~1.5 decades in g (XENON1T solar-ALP anchor), and needs
    # m below the solar core temperature ~ 1 keV
    if m_eV > 1e3: return np.inf
    return 10**1.5 * 1e-12

# ------------------------------------------------------- RECORD-RELIC tier
def delta_min_clock(m_eV, future=False):
    # fractional-frequency oscillation amplitude sensitivity
    base = 1e-19 if future else 1e-16
    m0 = 1e-15                       # eV; ~Hz. flat below, ~linear above
    if m_eV <= m0: return base
    if m_eV > 1e-6: return np.inf    # beyond clock/cavity/resonant band
    return base * (m_eV/m0)

def g_record_relic(m_eV, future=False):
    # requires: phi IS the local dark matter (assumption A_relic)
    if m_eV > 1.0: return np.inf     # no classical condensate above ~eV
    d = delta_min_clock(m_eV, future)
    if not np.isfinite(d): return np.inf
    return d * mN * m_eV / np.sqrt(2*rhoDM)

# ------------------------------------------------------------------- map
def main():
    tiers = [("kernel",       g_kernel),
             ("carrier",      g_carrier),
             ("record-flux",  g_record_flux),
             ("record-relic", g_record_relic)]

    print("TIER-REACH MAP: scalar Yukawa portal g*phi*NbarN")
    print("g_min = minimum detectable coupling (decade-level)\n")
    hdr = f"{'m [eV]':>9} {'lambda':>9} | " + " ".join(f"{n:>12}" for n,_ in tiers) + \
          "  | leader        2nd/1st [dex]"
    print(hdr); print("-"*len(hdr))

    rows = []
    for lm in range(-22, 13):
        m = 10.0**lm
        gs = [f(m) for _, f in tiers]
        finite = [(g, tiers[i][0]) for i, g in enumerate(gs) if np.isfinite(g)]
        finite.sort()
        lead = finite[0][1] if finite else "none"
        gap = (np.log10(finite[1][0]/finite[0][0]) if len(finite) > 1 else np.inf)
        lam = hbarc/m
        lamstr = f"{lam:8.1e}m"
        cells = " ".join(f"{g:12.1e}" if np.isfinite(g) else f"{'--':>12}" for g in gs)
        print(f"{m:9.0e} {lamstr:>9} | {cells}  | {lead:13} {gap:5.1f}")
        rows.append((m, gs, lead, gap))

    # ---------------------------------------------------- coherence windows
    print("\nCOHERENCE WINDOWS (two tiers within 1.0 dex of each other -->")
    print("cross-tier tension observable BEFORE single-tier discovery):")
    for m, gs, lead, gap in rows:
        if np.isfinite(gap) and gap <= 1.0:
            finite = sorted((g, tiers[i][0]) for i, g in enumerate(gs)
                            if np.isfinite(g))
            print(f"  m = {m:8.0e} eV : {finite[0][1]} vs {finite[1][1]}"
                  f"  (gap {gap:4.2f} dex)")

    # ------------------------------------------------ headline crossovers
    print("\nCROSSOVERS (structural, from the scalings):")
    # kernel vs record-relic: g_kern(EP floor) = delta*mN*m/sqrt(2rho)
    for tag, d in (("today, delta=1e-16", 1e-16), ("nuclear-clock, delta=1e-19", 1e-19)):
        gk = g_of_alpha(3e-13)
        mstar = gk*np.sqrt(2*rhoDM)/(d*mN)
        print(f"  record-relic beats kernel below m* = {mstar:8.1e} eV  ({tag})")
    # kernel vs carrier: solve on grid
    mm = np.logspace(-3, 2, 501)
    diff = np.array([np.log10(g_kernel(x)) - np.log10(g_carrier(x)) for x in mm])
    idx = np.where(np.sign(diff[:-1]) != np.sign(diff[1:]))[0]
    for i in idx:
        print(f"  carrier overtakes kernel near m = {mm[i]:8.1e} eV"
              f"  (Yukawa range e^-mr kills the lab potential)")

    # --------------------------------------- forward-form worked example
    print("\nFORWARD FORM, worked point (kernel-carrier crossover, m = 1.3 eV):")
    m0 = 1.3  # eV -- where kernel and carrier reaches are equal
    gtrue = 0.85*min(g_kernel(m0), g_carrier(m0))
    print(f"  true portal: m = {m0} eV, g = {gtrue:.1e} (just below both reaches)")
    zs = []
    for n, f in tiers:
        gmin = f(m0)
        if not np.isfinite(gmin): print(f"    {n:13}: blind"); continue
        # signal in units of the tier's ~2-sigma reach; power law of tier
        p = {"kernel":2, "carrier":2, "record-flux":4, "record-relic":1}[n]
        z = 2.0 * (gtrue/gmin)**p
        zs.append(z)
        print(f"    {n:13}: g_min = {gmin:8.1e}, pull ~ {z:4.1f} sigma"
              f"  (signal ~ g^{p})")
    zs = np.array(zs)
    qcoh = zs.sum()**0 * (np.sum(zs**2) - np.max(zs**2))  # aligned pulls
    print(f"    Q_coh (aligned) = {np.sum(zs**2):.1f} - {np.max(zs**2):.1f}"
          f" = {qcoh:.1f}; doubles with each doubling of joint exposure."
          f"  Noise expectation: ~0.")
    print("""
  pre-registered statistic:  Q_coh = Z^2_joint - max_i Z^2_i, where Z_i is
  the per-tier pull at the SHARED best-fit (g,m). Genuine portal in a
  coherence window: pulls add, Q_coh -> sum of the sub-threshold tiers'
  Z^2 (here ~ several). Noise: pulls land at unrelated (g,m); profiling to
  a common point costs each tier its excess, Q_coh ~ 0. Threshold Q_coh > 9
  = 3-sigma cross-tier corroboration, immune to per-tier look-elsewhere
  because (g,m) is shared.""")

if __name__ == "__main__":
    main()
