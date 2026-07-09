# D2 — The Abundance Arithmetic

*Exploratory — not canon. Grade: occupancy note / priced calculation. Rides
[D1](d1-the-residence-reading.md)'s residence claim and inherits its double conditionality (the
note strands with the seam). The question D1 left named-not-run: under what production mechanism
does Ω_dark/Ω_baryon ≈ 5.4 come out at order unity without tuning, given an interface set that is
empty today? Referee computation: `workbench/abundance-arithmetic/abund.py` (all Layer-2 numbers
verified there). Independent derivation by agent, July 2026; formulas anchored to the named
literature, coefficients flagged where not re-derived.*

## Layers

```text
Layer 1 — owned (D1 lineage):
  the target-number framing: m_χY_χ against η·m_p — abundance-times-mass versus
    asymmetry-times-mass; any unlinked mechanism hits 4.4×10⁻¹⁰ GeV by accident
  the branch taxonomy and its verdicts; the interface-history corollary
  the hot-relic ceiling on branching (the T_NR theorem's reading)

Layer 2 — projected (computed; workbench/abundance-arithmetic/):
  the A1 exclusion trilemma; T_NR = 1.16 eV/Br; the required-branching table
  the ΔN_eff arithmetic: 6.14x⁴ (BBN) / 7.40x⁴ (CMB); x < 0.45 from Planck
  the A2/A3 parameter pairings for Ω h² = 0.12

Layer 3 — imported:
  Ω_c h² = 0.1200, Ω_b h² = 0.02237, η = 6.1×10⁻¹⁰; Planck ΔN_eff < 0.30
  PIDM freeze-in (Garny–Sandora–Sloth); expansion production (Ford; Chung–Kolb–Riotto);
    gravitational-reheating stiff-epoch results
  mirror-sector baryogenesis (Berezhiani-class); asymmetric dark matter
    (Kaplan–Luty–Zurek); asymmetric-reheating constructions
  Lyman-α free-streaming exclusion of hot relics; CMB-S4 σ(N_eff) ≈ 0.03
```

## The target number

Ω_c/Ω_b = 5.36 fixes m_χY_χ = 4.36×10⁻¹⁰ GeV (Y = n/s). The baryon side is m_p·Y_b with
Y_b = η/7.04: an **asymmetry**-times-mass product. The two sides run on different machinery
unless the mechanism links them — so "natural 5.4" means, precisely: the mechanism's output
references η, or runs the same machinery twice. Anything else lands within an order of magnitude
of 4.4×10⁻¹⁰ GeV by accident, on knobs that are log-flat over many decades.

## Branch A — democratic gravitational production (seam-count one at all epochs)

**A1, O(1) energy branching at reheating: excluded, not merely unnatural.** Three exhaustive
sub-cases. Stable matter carrying an O(1) energy fraction grows against radiation as a/a_reh;
matter–radiation equality at 0.80 eV allows an energy fraction at reheating of only
T_eq/T_reh ≈ 7×10⁻²⁰ (T_reh = 10¹⁰ GeV) — overclosure by nineteen orders. Kept relativistic
instead, an equal split gives T′/T = 0.84 and ΔN_eff ≈ 3.1 against Planck's 0.30 — and
gravity-only forbids dumping the dark entropy back. The tuned middle is an 11–400 eV relic: hot
dark matter, dead on free-streaming. The lesson is structural: gravitational *rates* are
M_P-suppressed, so genuinely democratic branching is tiny — which is A2.

**The hot-relic ceiling, derived** (the branch's one theorem-shaped result): a relic produced in
inflaton decay with branching Br and the *correct abundance* becomes non-relativistic at

    T_NR = 2 m_χ T_reh/m_φ = 1.16 eV / Br  —  independent of m_φ, m_χ, and T_reh.

At Br = 1 that is matter–radiation equality itself: an abundance-matched O(1)-branching relic is
*maximally hot by construction*, at any mass scale, in any reheating history. Coldness
(T_NR ≳ keV) imposes Br ≲ 10⁻³ absolutely.

**A2, graviton-mediated freeze-in (PIDM):** Y ≈ T_reh³/(480 M_P³); Ω h² = 0.12 pairs
(T_reh, m_χ) = (10¹⁵ GeV, 3 TeV) through (6.6×10¹⁵, 10 GeV). Fully calculable, perfectly
gravity-only, and 5.4 is a two-knob accident — Ω ∝ m_χT_reh³ never references η. Its data hook
is high-scale inflation: observable tensors, with BICEP/Keck already squeezing the heavy corner.

**A3, expansion production:** Ω h² ≈ (m/10¹¹ GeV)²(T_reh/10⁹ GeV) at m ≈ H_e, exponentially
suppressed above — viability requires dialing m/H_inf on an exponential, plus a CDM-isocurvature
exposure (β_iso < 0.04) for light non-conformal scalars. Maximally accidental.

## Branch B — the transient inflaton portal

Y_χ = Br·(3/4)(T_reh/m_φ) gives the requirement

    Br · m_χ · (T_reh/m_φ) = 5.8×10⁻¹⁰ GeV ≈ η·m_p.

The η-scale number reappears verbatim as the tuning target: generic masses need Br ~ 10⁻⁸±few,
and the "natural" Br = O(1) corner is closed by the hot-relic ceiling above — it forces the
relic non-relativistic exactly at equality. D1's fossil reading survives only in bookkeeping
form: a transient portal *can* set the abundance, but nothing about it makes 5.4 come out —
the coincidence is transplanted from a density ratio into a branching product, unexplained
either way, with no link to η unless added by hand.

## Branch C — the structured dark sector

    Ω_χ/Ω_b = (m_χ/m_p)(η_χ/η_b).

If the dark sector runs its own asymmetry with comparable magnitude, and its stable relic sits
within an order of m_p, the ratio compares asymmetry-machinery to asymmetry-machinery and 5.4 is
**structural — the only branch where it survives calculation as natural.** Mirror-sector
realizations (a colder twin favors η′ ≳ η; dark-QCD scales IR-attracted toward Λ_QCD) and
shared-asymmetry ADM both live here — and D1's self-sector freedom is exactly the license this
branch spends: their census must contain asymmetry machinery, which residence permits and never
required.

The invoice, priced: ΔN_eff = 6.14(T′/T)⁴ at BBN (7.40 at CMB), so Planck's 0.30 forces
**T′/T < 0.45** — and democratic reheating gives 0.84. The colder twin requires *asymmetric
reheating*: the inflaton coupling preferentially to our sector. With x = (Br′/Br)^{1/4}, even a
10⁻² reheating asymmetry leaves ΔN_eff ≈ 0.05 — at CMB-S4's σ(N_eff) ≈ 0.03 threshold. A mirror
sector generically leaves a *detectable* radiation residue unless the asymmetry exceeds ~10³.
Their asymmetry magnitude needs either a shared CP seed (a transient co-genesis portal) or
parallel machinery run cold; their atomic/dissipative phenomenology feeds the same self-census
rows (σ/m, dark disks) D1 already meters.

## The verdict

| branch | 5.4 natural? | ΔN_eff residue | status |
|---|---|---|---|
| A1 democratic | — | ≈3 if radiation | **excluded** (overclose / ΔN_eff / hot-relic trilemma) |
| A2 PIDM | no — two-knob accident | ~0 | viable; tensor-mode hook; the clean seam-count-one-always model |
| A3 expansion | no — exponential dial | ~0 | viable in a tuned band; isocurvature-exposed |
| B transient portal | no — η transplanted into Br·m_χT_reh/m_φ; Br ≲ 10⁻³ ceiling | ~0 | bookkeeping, not explanation |
| C own asymmetry | **yes, to a factor of a few** | ≥ ~0.05 generically | natural — paid for with early structure |

**Strict seam-count-one at all epochs cannot make 5.4 a prediction.** A2 and A3 accommodate the
dark density but leave its proximity to the baryon density an accident on log-flat knobs — under
that framing the coincidence stays a discount, permanently and visibly, as D1's could-fail
already prices. The coincidence becomes structural only when the dark sector carries its own
asymmetry, and that naturalness is purchased with early non-gravitational structure: asymmetric
reheating, a co-genesis seed, or both — an interface set nonempty early and empty now.

So the ratio is doing evidential work after all, and the compressed claim's epoch index was the
right instinct with the wrong default branch: **Ω_dark/Ω_b ≈ 5.4 is evidence about interface
history.** It leans toward I(t_early) ≠ ∅ closing to I(t₀) = ∅ — and against
seam-count-one-at-all-epochs — with a scheduled discriminator: the structured branch generically
leaves ΔN_eff ≳ 0.05, and CMB-S4 measures to 0.03. The fork's grading keeps existence and shape
distinct: a detection near that level shows early dark radiation *exists* — an existence
verdict, with branch selection still open; a hard null is a **shape** verdict — it kills the
generic structured corner, and the history claim survives only at reheating asymmetries above
~10³ or retreats to the accident branches, where the discount locks.

Owned: the target-number framing; the branch taxonomy with the A1 exclusion; the hot-relic
ceiling reading; the transplant diagnosis of Branch B; the interface-history corollary and its
CMB-S4 fork. Imported: every relic formula's anchor literature, the Planck numbers, the
mirror/ADM constructions, the Lyman-α exclusions; the A2 coefficient is parametric (anchored to
the published scalings, not re-derived exactly — flagged). Could-fail: ΔN_eff null at CMB-S4
with Branch C otherwise favored (the fossil reading loses its meter and the discount locks);
tensor-mode exclusion of high-scale inflation (kills A2's clean corner); any non-gravitational
detection (the lane's standing kill, inherited); the seam dying (strands this note with D1).
