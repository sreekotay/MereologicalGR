# C1 — GW170817 as a propagation delay (H_p1)

*Exploratory application: this exports new physics rather than relabeling inside GR.*

## Core claim

GR governs four roles with one geometric object, g_μν:

- **propagation** — the cone signals ride;
- **measurement** — the metric rulers and clocks realize;
- **gravitational dynamics** — what curves and sources;
- **operational chronology** — causal precedence and the operational "now."

H_p1 does not modify that object; it decomposes it, declining to assume the four are the same object.
The GW170817 gap is evidence that at least one role separates from the others at ε ≈ 3.8×10⁻¹⁶.

Minimal surviving statement: **the matter light-cone is universally and slightly interior to the
gravitational-wave cone** — one cone for all matter (*universal*), strictly nested inside gravity's
(*interior*), by ε (*slight*).

The construction below re-bundles propagation, measurement, and chronology onto one matter cone and
dynamics onto gravity's. One event does not force that bundling — only *a* dissociation, not which.
It is the minimal re-fusion, adopted for calculation.

## The measurement

GW170817: the gravitational-wave merger peak and the GRB 170817A gamma-ray onset arrived 1.74 s apart,
over ~40 Mpc (~144 Mly; light-travel time τ ≈ 4.5×10¹⁵ s). The 1.74 s is a single arrival-time
difference — GW peak by matched filter, gamma onset by a count-rate threshold. One event cannot split
it into emission offset and propagation offset; both enter the same scalar. The conventional reading
assigns the whole gap to source timing — the merger-to-breakout delay — but that is a model fitted to
keep c_grav = c, not an independent measurement. At a full 1.74 s the propagation alternative is not
dismissible a priori, so it earns a run-down even if it ends up false: a high-risk defusion, priced
and killable, useful in clean failure.

## The cone ratio

Gravity's causal cone is slightly wider than light's. The frame-independent content is the ratio:

    c_grav / c_light = 1 + ε ,   ε ≈ 3.8×10⁻¹⁶ = 1.74 s / τ .

An isotropic offset of light alone is coordinate-absorbable; only the ratio to gravity is physical,
because there are two cones to compare.

## Where the degeneracy lives

Lorentz invariance is kept as a symmetry of *constituted* information: every completed measurement,
every recorded quantity, is LI-exact. The two-cone structure is a degeneracy of *in-transit*
influence — unfused while propagating, resolved only at constitution (readout). So this is not Lorentz
violation of measured physics; each record is LI. It is an unfused in-transit structure that
constituted-vs-constituted comparisons never see.

`n` aligns with the constituting matter's rest frame (the CMB frame the pulsar preferred-frame
analyses already use). That alignment is a kinematic fact, not prior geometry — but it is not "merely"
a sampling condition either: for the gap to be propagation, matter's cone is physically modified, so
this *is* new physics in matter propagation. Whether `n` is a fixed background field (Horn A) or the
cone delta is sourced by the gravitational field with `n` only setting its direction (Horn B) is open
— see Costs.

The gap survives constitution only when two records rode *different* in-transit legs — gravity's
IS-adjacency (fabric) vs matter's RIDES-adjacency (content). Same-leg pairs (ν and γ, both matter)
cancel; the cross-leg pair (GW and γ) reads out the relative accumulation. The accumulation is
in-transit, so it scales with path — propagation, not a source or readout offset. Constitution
*reveals* the gap, it does not generate it: ε is fixed to a number only at the readout cut, so for an
influence-only interaction (no register) it is undefined, not zero — the degenerate structure is
present, but there is nothing constituted for ε to be the value of.

(Whether that degenerate in-transit structure *is* the s-bound is left un-pointed: the same shape —
degenerate until a cut — is not licence to identify them, and the claim does not need s to stand.)

## Construction — the minimal re-fusion

One dynamical metric `g`, pure Einstein–Hilbert gravity: gravitational waves and the causal structure
follow `g`'s null cones. Matter and light couple to a slightly narrower effective metric via a constant
disformal deformation to a fixed unit timelike `n` (the CMB rest frame):

    g̃_μν = g_μν + B n_μ n_ν ,   B ≈ 2ε ≈ 7.6×10⁻¹⁶ .

Toy action (c=ℏ=1, signature −+++):

    S = (1/16πG) ∫√(−g) R[g]
      − ¼ ∫√(−g̃) g̃^{μα} g̃^{νβ} F_{μν}F_{αβ}
      + ∫√(−g̃) [ −½ g̃^{μν}∂_μφ ∂_νφ − V(φ) ] + …

In `n`'s rest frame, g̃ = diag(−(1−B), 1, 1, 1), so g̃^{μν}k_μk_ν = 0 gives ω = |k|√(1−B): light
travels at c_light = √(1−B) ≈ 1 − B/2 while gravitational waves follow `g` at c_grav = 1, so ε = B/2.

The toy's scope is local: it fixes the dispersion relation and the ε = B/2 dictionary on a patch,
and that is all it is used for. A genuinely fixed unit timelike `n` exists globally only on flat
spacetime; the CMB frame is the comoving congruence — position-dependent, defined by the matter
distribution. So the Horn-A realization forks under its own construction: hold `n` truly fixed and
the no-new-dof, no-ghost statement holds, but the field is honest flat-background Lorentz violation
with no global cosmological extension of its own; let `n` track the congruence and it is dynamical —
aether territory, new propagating degrees of freedom, its own constraint structure, the ghost
disclaimer unearned. Either way `n` functions as a physical background at constant `B` — the cost
that makes Horn B worth wanting (see Costs; no Horn-B realization is currently priced).

## Measured vs assumed

One number is measured: ε, averaged along a single line of sight through mostly-empty space,
ε_eff = (1/D)∫ε dl. Taking ε as a universal constant `B` is an assumption. Under it:

- achromatic — no frequency dependence (dimension-4, geometric);
- non-birefringent — both polarizations ride the single metric g̃, in every frame; this is the
  non-birefringent (c-type) SME sector;
- isotropic in the CMB frame; our motion through it makes the offset direction-dependent, but only
  against gravity (multimessenger) — never in a matter-only measurement;
- over comoving distances the delay adds up.

## Predictions

- Propagation delay accumulates along the path as ∫ε dl. For constant ε this is linear in comoving
  distance, Δt(z) = ε ∫₀^z dz′/H(z′) (curved in luminosity distance — that curvature is cosmology,
  not the model). This takes `B` constant in the comoving frame at each point along the path — the
  minimal global extension, assumed here, not supplied by the local toy (see Construction).
  Constant ε is a special case: the accumulation *kernel* is what the data recovers, and its
  shape — not a slope — is the discriminant (see Source vs propagation).
- A directional ~2 ms term from our motion through the CMB frame, appearing as a dipole in
  multimessenger arrival-time differences (a matter-vs-gravity comparison), not in any single-sector
  lab measurement (see Existing bounds and status).

## Source vs propagation

The observable in the only accessible channel — cosmological multimessenger timing — is a single gap,

    Δt = b + (path-accumulated propagation term) + (frequency terms),

with b the intrinsic emission offset (distance-independent, with event-to-event scatter). One event is
one (D, Δt) point: source and propagation are not separable from it. Source is what survives at zero
baseline (the D→0 intercept); propagation is what grows with path. That split is robust to the
accumulation shape — *except* when the kernel is source-peaked (ε ∝ ρ), which loads propagation onto
the intercept and collapses the split.

The propagation term is an accumulation kernel of unknown shape, not a slope. A population spanning
distance, line-of-sight potential, and redshift recovers it:

- constant cone → linear in comoving distance;
- ∝ ∫Φ dl → structure-lumpy, correlated with line-of-sight potential (H_p2);
- ∝ ∫ρ dl → source-peaked (collapses the source/propagation split);
- ∝ ρ_DE(z)/(1+w) → concave, low-z weighted (dark-energy drag);
- general ε(z) → the curve is ε(z) itself.

The shape is the discriminant, and it is open (PB-2: ε is an intensive, possibly configuration-
dependent rate, not a universal scalar). "c_grav = c_light" is the closure assigning the whole gap to
b under an assumed source model; H_p1 is the closure assigning it to propagation. GW170817 alone picks
neither — the accumulation shape across a population does. Host-astrophysics scatter with no coherent
trend points back to emission timing.

## Costs

1. **Frame and conservation (Horn A vs Horn B).** The cone difference is physical, so `n` (or the
   gravitational field) does real work in matter propagation — the only question is which, and
   consistency already narrows it. *Horn A*: `n` is a fixed background field (constant `B`) — explicit
   Lorentz violation, ∇^μT_{μν} = O(B) ≠ 0 against the Bianchi identity (Kostelecký), vanishing only
   on the FLRW background; numbers safe (ε ~ 10⁻¹⁶), ontology costly — and a globally fixed `n` does
   not exist off flat spacetime, so the field is either flat-patch honest or covertly dynamical (see
   Construction). *Horn B*: the delta is sourced by
   the gravitational field (ε → 0 in flat space, `n` only setting direction), so no flat-space
   background — but no priced realization is on the table. A raw curvature invariant is ruled
   out by strong-field consistency: tuned to the observed weak-field 1.74 s it gives ε ≫ 1 at a
   black-hole horizon (curvature spans ~10³⁸ between the two regimes), while demanding ε < 1 there
   makes the weak-field effect unmeasurable — inconsistent or invisible. Any surviving sourcing must
   stay bounded across those ~38 orders *and* leave the solar system quiet at Cost 3's
   Shapiro-sector level once tuned to the 1.74 s; no candidate written down so far passes both ends.
   Horn B is parked as a requirement, not banked as a form. What a form would buy: universality for
   free — geometric sourcing couples every matter species identically, where Horn A must posit exact
   universality as an unexplained coincidence (every "blind" entry under Existing bounds leans on it).
   The fork is Horn A, priced, vs Horn B, wanted but unrealized.

2. **Naturalness.** ε ≈ 3.8×10⁻¹⁶ runs to O(1) under radiative corrections (Collins–Perez–Sudarsky).
   A custodial (SUSY-like) symmetry gives ε = (m/M_Pl)², placing the breaking scale near
   m ≈ 2×10¹¹ GeV. Stability under gravitational loops is open.

3. **Uniformity.** If ε varies with position: ε ∝ Φ gives an achromatic Shapiro-sector anomaly in
   Cassini / LLR / pulsar timing / clock redshift at ~10⁻¹⁷–10⁻¹⁸ (this is H_p2). ε ∝ ρ acquires part
   of the delay at the merger itself — the densest point on the path — collapsing the
   emission/propagation split. Density-independence is a requirement of the reading, not a detail.

## Existing bounds and status

Constituted-vs-constituted comparisons are LI-exact, so any measurement within one in-transit leg is
blind — photon-vs-fermion resonators, atomic clocks, and neutrino-vs-photon timing all compare
records that rode the matter leg (equivalently: a universal matter-sector shift is a coordinate
rescaling). The gap reads out only across *different* legs (gravity vs matter), and among those only
cosmological baselines beat the ε suppression. Lab tests therefore do not constrain H_p1;
cross-leg multimessenger timing is the sole access.

- **GW170817 speed:** (c_grav − c)/c ∈ [−3×10⁻¹⁵, +7×10⁻¹⁶] (Abbott et al. 2017). The + edge is the
  all-propagation reading — H_p1's defining move; its value floats with the assumed distance (≈3.8×10⁻¹⁶
  at 40 Mpc, up to ~7×10⁻¹⁶ at the conservative ~26 Mpc used for the bound). H_p1 sits inside the
  window: contained, not excluded, not independently confirmed. The window's width is the assumed
  0–10 s emission delay.
- **Gravitational Cherenkov (cosmic rays):** c − c_grav < 2×10⁻¹⁹ extragalactic (Moore–Nelson 2001),
  but only for gravity slower. H_p1 has gravity faster — the sign in this probe's blind spot.
- **Preferred-frame PPN:** α̂₁ ~ 10⁻⁵, α̂₂ ≲ 10⁻⁴ (Shao–Wex 2012), already taking the CMB frame as
  preferred. H_p1's α ∝ ε ~ 10⁻¹⁶ is far below.
- **Photon-sector Lorentz violation:** anisotropy bounds reach ~9×10⁻¹⁹ (Nagel et al. 2015),
  isotropic κ̃_tr ~ 10⁻⁹ — both measure a photon-vs-matter difference, which universality sets to
  zero.
- **Neutrino–photon (SN1987A):** (v − c)/c ~ 2×10⁻⁹ — matter-vs-matter, predicted null.
- **GW luminosity distance / friction:** GWTC-3 is compatible with GR. H_p1 predicts an exact null
  (gravity is pristine), distinguishing it from running-Planck-mass models.
- **Birefringence (~10⁻³²) and GRB dispersion** target birefringent / dimension-5 operators; this one
  is neither.

**Status.** A single reading of one degenerate number, interchangeable with a source-emission
explanation until a population of sirens spanning distance exists. This note develops only the
propagation separation; measurement, dynamics, and chronology are named in the frame but not pursued
here. "c_grav = c_light" is the conditional closure H_p1 competes with, not an established fact — and
the two-cone constant-ε model is one realization of the propagation split, not the split itself. Read
down the influence ladder, Lorentz invariance stays exact at constitution while the degeneracy lives
in transit — but that is a claim about *where the new physics hides* (invisible to constituted-matter
comparisons), not that there is none: any in-transit cone difference is new physics in matter
propagation.
