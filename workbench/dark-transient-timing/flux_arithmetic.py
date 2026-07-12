#!/usr/bin/env python3
"""
Dark-transient timing channel: flux arithmetic.

Question: if DM rides the outer (fabric) cone with splitting eps <= 3.9e-16
(GW170817 anchor, c1/c3), a dark transient with an EM counterpart arrives
early by eps*D/c. Does any conceivable source-detector pair close?

Three gates, each computed here:
  GATE 1 (dispersion): a massive dark messenger at Lorentz factor gamma lags
          its own cone by D/(2 gamma^2 c); the eps-lead survives only if
          gamma > 1/sqrt(2 eps) ~ 3.6e7. Velocity spread smears the burst
          by ~D/c * Delta(1/v).
  GATE 2 (flux): burst energy density at Earth vs the ambient halo density
          rho_local = 0.45 GeV/cm^3 that haloscopes are designed against,
          plus the frequency mismatch (cavity band = m_a (1+O(1e-6));
          relativistic burst = gamma*m_a with O(1) spread).
  GATE 3 (clock): the matter-cone timestamp (neutrino onset / EM transient)
          must resolve eps*D/c at a distance where GATES 1-2 pass.

Sources for inputs are cited inline. Run: python3 flux_arithmetic.py
"""

import math

# ---------------------------------------------------------------- constants
c        = 2.998e10          # cm/s
pc       = 3.086e18          # cm
kpc, Mpc = 1e3 * pc, 1e6 * pc
Msun_erg = 1.788e54          # solar rest energy, erg
GeV_erg  = 1.602e-3
eV_GeV   = 1e-9
yr       = 3.156e7           # s

eps      = 3.8e-16           # GW170817 anchor (c1: eps = 1.74 s / tau at ~44 Mpc)
rho_loc  = 0.45 * GeV_erg    # local DM energy density, erg/cm^3
v_vir    = 238e5             # cm/s local virial speed -> ambient DM "flux"

def tld(D):   # timing lead eps*D/c, seconds
    return eps * D / c

print("=" * 72)
print("GATE 0 - the signal being chased: eps*D/c at eps = 3.8e-16")
print("=" * 72)
for name, D in [("0.1 pc (PBH burst horizon)", 0.1 * pc),
                ("1 pc", pc), ("10 kpc (Galactic SN)", 10 * kpc),
                ("770 kpc (M31)", 770 * kpc), ("1 Mpc", Mpc),
                ("40 Mpc (GW170817-class)", 40 * Mpc)]:
    print(f"  {name:32s}  D/c = {D/c:9.3e} s   lead = {tld(D):9.3e} s")
# z=1: light-travel time ~ 7.9 Gyr
T_z1 = 7.9e9 * yr
print(f"  {'z = 1 (T ~ 7.9 Gyr)':32s}  T   = {T_z1:9.3e} s   lead = {eps*T_z1:9.3e} s"
      f"  (~{eps*T_z1/60:.1f} min)")

print()
print("=" * 72)
print("GATE 1 - dispersion: which messengers keep the eps-lead at all")
print("=" * 72)
gamma_min = 1 / math.sqrt(2 * eps)
print(f"  massive messenger lags its cone by D/(2 gamma^2 c);")
print(f"  lead survives only if gamma > 1/sqrt(2*eps) = {gamma_min:.2e}")
print(f"  -> bosenova axions (Levkov-Panin-Tkachev 1609.03611: momenta k ~ m_a,")
print(f"     gamma ~ 1.2-3):  lag/lead = (1/2g^2)/eps ~ {1/(2*2**2)/eps:.1e}  DEAD")
print(f"  -> SN-core ALPs (E ~ 50 MeV, m_a <~ 1e-9 eV): gamma ~ "
      f"{50e6/1e-9:.0e}  PASSES")
print(f"  -> massless dark radiation (mirror photons/neutrinos): PASSES")
# burst smearing for the bosenova case
for name, D in [("1 pc", pc), ("10 kpc", 10 * kpc), ("40 Mpc", 40 * Mpc)]:
    # v/c in 0.4-0.9 -> Delta(1/v) ~ 1.4
    smear = D / c * (1/0.4 - 1/0.9)
    print(f"  bosenova burst arrival smear at {name:7s}: "
          f"{smear:9.3e} s  (= {smear/yr:9.3e} yr)")

print()
print("=" * 72)
print("GATE 2 - flux: bosenova axion burst vs haloscope (the best 'dark leg')")
print("=" * 72)
# dilute axion-star critical mass, QCD axion m_a = 1e-5 eV, f_a ~ 6e11 GeV:
# M_max ~ 10.15 * M_pl * f_a / m_a  (Chavanis; Levkov et al. lineage)
M_pl, f_a, m_a = 1.22e19, 6e11, 1e-5 * eV_GeV     # GeV
M_star = 10.15 * M_pl * f_a / m_a * GeV_erg        # erg (rest energy)
E_burst = 0.1 * M_star   # ~O(10%) of mass in relativistic axions over the
                         # collapse series (1609.03611)
print(f"  axion-star critical mass  : {M_star/Msun_erg:.2e} Msun "
      f"({M_star:.2e} erg)")
print(f"  relativistic burst energy : {E_burst:.2e} erg (10% of M*)")
print(f"  ambient benchmark: rho_loc = {rho_loc:.2e} erg/cm^3; "
      f"ambient 'flux' rho*v = {rho_loc*v_vir:.2e} erg/cm^2/s")
print()
print(f"  {'D':>8s} {'fluence':>12s} {'u_disp':>12s} {'u/rho_loc':>12s} "
      f"{'u_fantasy':>12s} {'uf/rho_loc':>12s}")
for name, D in [("1 pc", pc), ("10 kpc", 10 * kpc),
                ("1 Mpc", Mpc), ("40 Mpc", 40 * Mpc)]:
    F = E_burst / (4 * math.pi * D**2)             # erg/cm^2
    smear = D / c * (1/0.4 - 1/0.9)                # dispersion-set duration
    u_real = F / (c * smear)                       # erg/cm^3, dispersed
    # physically impossible best case: intrinsic ms burst, no dispersion
    u_fant = F / (c * 1e-3)
    print(f"  {name:>8s} {F:12.3e} {u_real:12.3e} {u_real/rho_loc:12.3e} "
          f"{u_fant:12.3e} {u_fant/rho_loc:12.3e}")
print()
print("  haloscope radiometer scaling: SNR ~ (u/rho_loc) * sqrt(tau/t_int)")
print("  ADMX reaches SNR ~ 3 on rho_loc with t_int ~ 100 s per tune AND the")
print("  signal inside the cavity band (Q_a ~ 1e6). The burst arrives at")
print("  gamma*m_a with O(1) spread: in-band fraction ~ 1e-6 even before SNR.")
D10, tau10 = 10 * kpc, (10*kpc/c) * (1/0.4 - 1/0.9)
u10 = E_burst / (4*math.pi*D10**2) / (c * tau10)
snr_deficit = (u10/rho_loc) * 1e-6      # density ratio x in-band fraction
print(f"  10 kpc, dispersed:  (u/rho)*band ~ {snr_deficit:.1e} "
      f"-> short by ~10^{-math.log10(snr_deficit):.0f}")
u10f = E_burst / (4*math.pi*D10**2) / (c * 1e-3)
print(f"  10 kpc, FANTASY (no dispersion, ms burst, in-band): "
      f"(u/rho)*sqrt(1e-3/100) ~ {u10f/rho_loc*math.sqrt(1e-5):.1e} "
      f"-> short by ~10^{-math.log10(u10f/rho_loc*math.sqrt(1e-5)):.0f}")

print()
print("=" * 72)
print("GATE 3 - the clock: SN ALP-conversion gamma burst vs neutrino onset")
print("        (the only candidate passing gates 1-2; ALP is ultrarelativistic")
print("         and Fermi-LAT is the 'dark detector' via B-field conversion)")
print("=" * 72)
# E_a ~ 1e50 erg in ~10 s allowed just under SN1987A / Fermi stacked bounds
# (g_ag ~ 2.6e-12 GeV^-1 exclusion, Meyer+ PRL 124.231101)
rows = [
    ("10 kpc (Galactic)", 10*kpc, "nu onset ~1 ms; a-vs-nu emission-model syst ~10-100 ms", 1e-2),
    ("770 kpc (M31)",     770*kpc, "Hyper-K ~O(10) events -> onset ~0.1-1 s", 3e-1),
    ("40 Mpc",            40*Mpc, "no nu detection (needs ~1e4 x Hyper-K)", float('inf')),
]
for name, D, note, floor in rows:
    lead = tld(D)
    # gamma-leg flux relative to Galactic benchmark
    rel = (10*kpc/D)**2
    verdict = ("signal/floor = %.1e" % (lead/floor)) if floor < 1e30 else "no timestamp"
    print(f"  {name:18s} lead = {lead:9.3e} s | clock floor: {note}")
    print(f"  {'':18s} gamma-leg flux vs 10 kpc: {rel:8.1e} | {verdict}")
print()
print("  Structure: the gamma leg is detectable where the lead is unresolvable")
print("  (Galactic, lead ~0.4 ms vs >=10 ms floor) and undetectable where the")
print("  lead is resolvable (40 Mpc: flux down 1.6e7, no neutrino clock).")
print("  Crossover does not exist at any D for any g_ag under current bounds.")
print("  NOTE: an SN-core ALP is produced at a baryonic interface -> under")
print("  residence it is matter-sector by construction; this channel tests a")
print("  different particle's cone, not the resident population's.")

print()
print("=" * 72)
print("GATE 3' - the GW alternative (cone-sibling test, not an eps test)")
print("=" * 72)
# GNOME/ELF: Dailey+ Nat.Ast. 5,150 (2021); GNOME PRX null (2407.13919)
# order-of-magnitude: ELF burst of energy E at 40 Mpc, mode frequency ~Hz-kHz,
# field amplitude at Earth for quadratic/linear couplings needs energies
# >> 1e50 erg AND couplings at/above current static bounds to register.
E_elf = 0.1 * Msun_erg   # generous: 0.1 Msun c^2 in exotic field @ BNS merger
F_elf = E_elf / (4 * math.pi * (40 * Mpc)**2)
print(f"  ELF burst 0.1 Msun c^2 at 40 Mpc -> fluence {F_elf:.2e} erg/cm^2")
print(f"  over ~10 s: energy density {F_elf/(c*10):.2e} erg/cm^3 "
      f"= {F_elf/(c*10)/rho_loc:.1e} x rho_loc")
print("  -> even a tenth of a solar mass radiated in exotic fields delivers")
print("     ~4e-9 of the ambient halo density; detection requires coupling")
print("     (portal) orders beyond static-limit values. GNOME's coincident")
print("     search (PRX 2024) set limits with 'no significant events'.")
