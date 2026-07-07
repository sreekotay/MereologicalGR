# C4 — Cone-Delta Curves

*Exploratory — not canon. Grade: theory-class probe, conditional. Theory-space lane for
[C1](c1-gw170817-propagation.md): grant the
propagation reading and develop what can shape a cone delta, the curve each shaper draws, and where
each theory class touches data outside GW170817. [C3](c3-quantifying-the-cone-delta.md) prices the
estimator; this note prices the theory classes. Source physics gets no vote here — it is the
axiom-to-fit closure under re-read ([C2](c2-path-before-propagation.md), carrier 1).*

## The master relation

Everything propagation-level lives in one relation. For a cross-leg pair at redshift z, with b the
non-negative source intercept:

    Δt(z) = b + ∫₀^z ε(z′) dz′ / H(z′) ,

and every propagation hypothesis is a choice of what ε may depend on. Along a cosmological path
there are exactly five things available: nothing, the expansion, the background densities, the
structure crossed, and noise. That is the whole menu.

## The forced family

The grammar sorts the menu before any data does. B2 fixes H as *adjacency-scale change per cosmic
flow* — the rate the shared congruence renders. What is forced: if the delta is a property of the
riding relation itself, ε may depend only on expansion *kinematics* — H and its flow-derivatives
(Ḣ, the deceleration parameter) — with no content import. What is chosen: pricing the family's two
leading members and parking the rest (an ε ∝ q(z) member exists and draws its own distinguishable
curve):

- **T1 — ε constant.** A bare property of the riding relation. Exactly degenerate, forever, with
  dark-energy sourcing at w = −1.
- **T2 — ε ∝ H.** Riding lag proportional to how fast adjacency is re-laid. One scale, no shape
  freedom (see below).

Everything else imports content into the relation — Horn-B-class sourcing (C1, Cost 1) by another
name:

- **T3 — ε ∝ (1+z)³** (matter density); **T3′ — ε ∝ (1+z)⁴** (radiation bath);
- **T4 — ε ∝ Φ** along the line of sight (H_p2; the ∂Φ/∂t variant is low-z, ISW-weighted);
- **T5 — one-sided noise.** C1's sign-lock holds pointwise — content influence outside ordering is
  ungrammatical — so ε(x) ≥ 0 everywhere and a fluctuating seam fluctuates one-sided: a nonzero
  mean (the floor survives) plus variance σ(Δt) ∝ √D with no source-side counterfeit (source
  scatter is distance-independent). Zero-mean diffusion is dead by grammar, not by data.

## Curves

All calibrated through GW170817 (z ≈ 0.01, 1.74 s all-propagation → ε₀ ≈ 3.9×10⁻¹⁶). One datum
fixes the family's amplitude, never the member. Flat ΛCDM, H₀ = 67.4:

| z | T1 (concave) | T2 (linear) | T3 (convex) | T3′ |
|---|---|---|---|---|
| 0.1 | 17.4 s | 17.8 s | 19.8 s | 20.8 s |
| 0.3 | 49.5 s | 53.3 s | 74.6 s | 86.5 s |
| 0.5 | 78.1 s | 88.8 s | 152 s | 195 s |
| 1.0 | 136 s | 178 s | 458 s | 735 s |
| 2.0 | 213 s | 355 s | 1620 s | 3690 s |

T2 is *exactly* linear in z — the H's cancel in the master relation; no cosmology dependence, no
knobs. T1 tracks comoving distance (concave in z); the sourced classes are convex and high-z
weighted. T4 draws covariance with density/potential maps rather than a z-curve; T5 draws a
variance law. Sky decomposition: every class allows residual power only at ℓ = 0 (ε itself) and
ℓ = 1 (our CMB motion); any ℓ ≥ 2 power is fabric anisotropy — a different and larger claim.

Discrimination against a ~2 s per-event nuisance floor:

- **T3 splits from T1 at z ≈ 0.09** — inside late-O5 BNS reach. The sourced density class is
  testable first.
- **T1 vs T2 needs z ≈ 0.22** (2 s separation), z ≈ 0.34 (5 s), z ≈ 0.48 (10 s) — ET/CE era, then
  decisive per event: 11 s at z = 0.5, 42 s at z = 1.
- The curves' protection against source-evolution mimicry (C3): their shapes are cosmology-locked —
  χ(z), z, ∫(1+z)³dz/E — and a drifting b(z) has no reason to match any of them.

## The wall, twice

C1 found the boundedness wall spatially: raw curvature-sourcing, tuned to the weak field, gives
ε ≫ 1 at a black-hole horizon. The same wall stands in the time direction. Every kernel that grows
into the past hits ε = 1 at a computable epoch, where the matter cone closes and the theory
self-destructs:

| class | ε = 1 at | epoch |
|---|---|---|
| T2 (∝H) | z ≈ 5×10⁸, T ≈ 0.1 MeV | mid-BBN (ε ≈ 67 at 1 MeV unsaturated) |
| T3 (∝(1+z)³) | z ≈ 1.4×10⁵ | radiation era, pre-recombination |
| T3′ (∝(1+z)⁴) | z ≈ 7×10³ | just before recombination |
| T1, T4 | never | (Φ never exceeds ~10⁻⁵; a constant is a constant) |

One requirement, seen in two orthogonal limits: **the riding delta must stay bounded wherever the
fabric gets extreme** — strong fields spatially, the early universe temporally. T1 evades both for
free. T2 survives only by saturating at some ε_max < 1, buying a new epoch ("when re-binding
saturated"). The sourced classes must saturate pre-recombination or die.

## The floor — standard-theory members

The sourced classes are not hypothetical: QED computes members of them wherever an environment
breaks the vacuum's symmetry. Scharnhorst (boundary-sourced: photons between Casimir plates run
*faster* — less virtual dressing to drag through); thermal QED (content-sourced:
δv/c ~ −α²T⁴/m_e⁴ in a blackbody bath); Drummond–Hathrell (curvature-sourced: the photon's
virtual dressing couples to curvature at one loop, δc/c ~ α λ_C² R, polarization-dependent). The
Latorre–Pascual–Tarrach form unifies the family: δv ∝ −α² ρ/m⁴ — drag proportional to the energy
density the dressing couples to, interior sign — the binding-cost mechanism, computed at one loop
in imported theory. Two consistency notes: the strong-field wall killed *anchor-scale* curvature
sourcing only — D-H exists ~25 orders below it, untuned and bounded; and D-H's birefringence
keeps it excluded as a cosmological carrier by the 10⁻³² form-certification, so these members are
local and tiny by construction.

The consequence is a floor. The actual universe is an environment — bath, curvature, congruence —
so the standard-theory cone shift is nonzero and computable: the thermal term alone gives
ε_QED ~ α²(T_CMB/m_e)⁴ ≈ 2×10⁻⁴² today. Exact cone-coincidence has no protective symmetry in an
environed universe; nominal is generic, and exactness would be the tuning. The seam parameter is
therefore bracketed from both ends:

    ε ∈ [ ~10⁻⁴² (computed, imported QED) , 4×10⁻¹⁶ (measured once, C1) ]

— twenty-six decades, floor from theory, ceiling from one event. The open question is not whether
the seam exists but whether any term sits above the environmental floor. Guard, stated so the
bracket cannot be over-read: none of these members evidences an anchor-scale term — the known
floor changes the question's *form* (every register narrows a bracket, not a point hypothesis),
not the answer's likelihood. Magnitudes all imported; this section owns the placement of the QED
members within the family, the bracket, and the burden statement.

## T2 as a one-scale theory

Write T2 as ε(z) = H(z)/H*. Then GW170817's number is not an unexplained small constant — it is
the measurement of the scale:

    H* = H₀/ε₀ ≈ 5.6×10⁻³ s⁻¹ ,   t* ≈ 90 s ,   T* ≈ 0.1 MeV .

The smallness of ε today is the statement that the present universe expands 10¹⁶ times slower than
at saturation. This converts T1's permanent naturalness debt (why 10⁻¹⁶?) into a locatable physics
question (what owns a rate scale of order minutes?). Flag, unpriced: T* sits near the deuterium
bottleneck (~78 keV). Either a hint about what owns the scale or famous-epoch numerology; neither
reading is used anywhere in this note.

## The second channel — backreaction, computed

In any T2 realization, gravity computes expansion from the Friedmann equation on `g` while matter
physics (weak rates, thermodynamics, clocks) runs on g̃. During the saturated era the mismatch
between *the expansion that gravitates* and *the expansion matter feels* is ΔH/H = κ·ε_max. κ is
now computed per realization of `n` in the toy: foliation (covector fixed) +3/2; external vector
fixed −1/2; g-normalized +5/2; **composite** — n built from the matter congruence, normalized in
matter's own metric — **+1/2**, in closed form (the implicit construction collapses to
g̃₀₀ = g₀₀/(1+B)). The composite is the only globally well-defined member (n exists wherever
matter flows: the global-n cost of Cost 0 dissolves there), and it is the realization b7's FT-2
licenses as *flow* — the others are background fields wearing flow vocabulary. So the
grammar-consistent sign is **positive**: a saturated T2 residue *adds* to the BBN-side expansion,
and an observed deficit is a bound on ε_max, not a claimable channel, unless one buys a Horn-A
background vector (the κ = −1/2 member) with its ontology bill. Given κ, the chain is exact:

- BBN reads the expansion rate at n/p freeze-out. In N_eff currency (g* = 10.75, one ν species =
  0.163 of the radiation density): **ΔN_eff = 12.3 × ΔH/H = 12.3 κ ε_max**.
- Planck+BBN consistency (ΔN_eff ≲ 0.3) caps the ceiling: **κ ε_max ≲ 2.4×10⁻²**. The temporal
  wall has a measured height, from data already in hand.
- CMB-S4 (σ(N_eff) ≈ 0.03) reaches κ ε_max ≈ 5×10⁻³. The live band is **5×10⁻³ – 2.4×10⁻²**.

The signature is a *split*. The saturated era ends at t ~ 10³–10⁵ s (for ε_max in the allowed
range): after BBN, eight orders in ε before recombination. Computed directly: ε is pinned at ε_max
throughout BBN but has decayed to 9×10⁻¹² by recombination (6×10⁻¹¹ at equality). So T2 shifts the
*BBN-inferred* N_eff (helium, deuterium yields) and leaves the *CMB-inferred* N_eff (Silk damping)
exactly standard:

    T2:  N_eff(BBN) − N_eff(CMB) = 12.3 κ ε_max ≠ 0 .
    T1:  exact equality, forever.

No neighbor produces this. Real dark radiation — the thing ΔN_eff is named for — shifts both
inferences equally, because the extra species is still present at recombination. A coherent
BBN-vs-CMB N_eff split currently has no label in the standard analysis; it would be filed as a
systematic in the primordial-abundance measurements.

What the computation closed: the sound horizon r_d is weighted toward the epochs just before
recombination, where T2's ε is 10⁻¹¹-class; the BBN-era shift touches a negligible sliver of the
integral. **A saturating T2 cannot pay the Hubble-tension ruler.** The b2 slot-2 overlap was
label-space only; under computation it resolves into a distinct observable (the split), not a
tension payment.

## Mislabel audit

Two places where an axiom-to-fit closure filed evidence under the wrong role:

- **SN1987A.** The equal Shapiro delays of the neutrinos and photons (Longo 1988; Krauss–Tremaine
  1988) are filed in the literature as a test of *gravity* — equivalence principle, GR's cone. The
  route shows the fabric *leg* was never in the measurement: the Galactic potential is the lens,
  but ν and γ are both content — same-leg — so it tested content-universality of gravitational
  response, not gravity's cone. The fabric leg was untouched until 2017, and has been touched
  exactly once.
- **BBN's N_eff.** The standard analysis fuses *the expansion that gravitates* with *the expansion
  matter feels* — the same propagation/dynamics fusion C1 unfuses, applied at the earliest measured
  epoch, unlabeled. The ΔN_eff slot would silently absorb a violation as "dark radiation," and a
  BBN-vs-CMB split — the actual cone-delta residue — has no slot at all.

(C1 carries the other two: the GW170817 "c_gw = c" headline as a joint constraint with the source
closure, and the Cassini γ sector as T4's leakage — Cost 3.)

## Status

The fork after computation: **T1** — wall-free, one observable channel (the wedge, concave curve),
permanent naturalness debt, and a forever-degeneracy with w = −1 dark energy. **T2** — one measured
scale in place of a bare constant, an exactly linear curve with no shape freedom, and two
independent kill channels: the wedge (ET/CE era, z ≳ 0.22) and the BBN-side N_eff split (ceiling
already capped at 2.4×10⁻², CMB-S4 probes to 5×10⁻³). T2 is strictly more exposed than T1 — by the
repo's currency, the better bet. The sourced classes carry the wall in both directions; the
noise class is one-sided (ε ≥ 0 by C1's sign-lock), floor-bearing, and distinguishable by its
second moment — σ ∝ √D against every deterministic member's measurement-error-only scatter.

The fork also carries foundation-bet weight. C1 already reads ε through PB-2 — an intensive,
possibly configuration-dependent rate, not a universal scalar — and PB-2's could-fail includes the
measure coming out universal (c-like). T1 *is* a universal scalar; T2 is the intensive-rate
reading. So the T1/T2 curve discrimination is a PB-2 contact, not lane-internal housekeeping —
conditional exactly as C1 leaves it (the s-bound identification stays un-pointed), but the
citation is C1's own.

Owned: the relation-level branch forced to expansion-kinematic functionals (from b2's rendered
rate), with T1/T2 priced as its leading members; the curve table
and discrimination redshifts; the temporal wall and its identification with C1's spatial wall as
one boundedness requirement; the one-scale reading of T2 and H* as what GW170817 measured; the
ΔN_eff = 12.3 κ ε_max chain and the BBN-vs-CMB split as T2's discriminant; the r_d no-payment
result; the SN1987A and N_eff mislabel assignments. Imported: ΛCDM and all cosmological parameters,
g* bookkeeping, N_eff bounds and CMB-S4 forecasts, primordial-abundance systematics, detector
horizons, and κ (open: requires a full realization).
