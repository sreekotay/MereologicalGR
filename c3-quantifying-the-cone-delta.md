# C3 — Quantifying the Cone Delta

*Exploratory — not canon. Grade: diagnostic / estimator lane. Conditional on
[C1](c1-gw170817-propagation.md): grant that the gap
is propagation — not source, not readout — and ask what a cone delta looks like and how it is
computed. [C2](c2-path-before-propagation.md) prices the carriers that must fail first; this note
prices the estimator that runs once they have.*

## The observable surface is one wedge

Grant C1's reading: matter's cone is universally interior to gravity's, and the gap accumulates
in transit. Then for constant ε the model's entire observable content is cross-messenger arrival
timing. Nothing else moves:

- gravity is pristine — no in-band GW dispersion, no friction, no birefringence, standard
  luminosity distance;
- matter physics is internally LI-exact — every matter-only record identical to GR;
- cosmological backreaction at ε ~ 10⁻¹⁶ is nil.

So there is exactly one plot. Each event i with a gravity-leg and a matter-leg arrival gives a
point (T_i, Δt_i): T_i the comoving distance over c from the host redshift — the constant-kernel
covariate; at GW170817's z it coincides with the light-travel time — Δt_i the measured gap, and

    Δt_i = b_i + ε T_i ,   b_i ≥ 0 ,

with b_i the *observed* emission offset — the source-frame offset dilated by (1+z_i); the matter
signal cannot precede the merger, so b_i ≥ 0 survives dilation. A real cone delta looks
like a **forbidden wedge**: no event below the line Δt = εT, source scatter riding above it, the
floor rising linearly with baseline. A source-only world is a horizontal band — floor at zero, no
T-trend. The wedge *is* the signature; everything below quantifies it.

## One-sided structure: bound, kill, detect

Because b ≥ 0 is the only assumption, every event is a prior-free upper bound:

    ε ≤ Δt_i / T_i   for every i.

- **Bound (now).** GW170817 gives ε ≤ 3.9×10⁻¹⁶. That is the whole current posture — one edge,
  no lower bound, ε = 0 fully allowed.
- **Kill (one event).** The floor rises with distance while jet-breakout gaps do not:

      floor(D) = 1.74 s × (D / 44 Mpc) :   100 Mpc → 4.0 s,  200 → 7.9 s,  300 → 11.9 s.

  A single BNS–GRB coincidence at 300 Mpc with a ~2 s gap forces ε ≤ 7×10⁻¹⁷ and constant-ε at
  the GW170817 value is dead. No population, no regression — the very next distant coincidence is
  near-decisive against the constant kernel. One protocol line guards the kill's false-fire mode:
  the onset must be the main pulse, precursor emission excluded — BNS mergers emit EM precursors
  seconds before merger, and a precursor-contaminated onset fakes a floor violation. (The bound
  direction is safe: contamination only inflates Δt.) This is the cheapest kill C2's carrier
  program feeds.
- **Detect (population).** A lower bound ε > 0 needs the floor's *rise*: a T-trend that source
  scatter cannot supply, priced against selection (C2, carrier 2). Note the naive selection tilt
  runs anti-mimicking — at large D only loud, near-axis events survive, and near-axis favors
  *shorter* breakout delays, tilting the band down where the cone tilts it up. Imported and
  model-dependent; priced, not banked.

## The anchor's error budget

The one measured event, decomposed by assumption. Each row conditions ε on a prior for the
emission offset b; timing error (±0.05 s) and distance error (~7.5%) ride along. 40 Mpc
convention — 44 Mpc rows sit ~9% lower; the wedge edge above (3.9×10⁻¹⁶) is the central 44 Mpc
value, the 4.8 here the conservative 2σ-timing, −1σ-distance edge:

| assumption on b | ε (×10⁻¹⁶) | character |
|---|---|---|
| prior-free (b ≥ 0; Cherenkov closes the far side) | −0.002 ≤ ε ≤ +4.8 | the only assumption-free statement |
| b = 0 (maximally exposed; C6's branch) | +4.2 ± 0.4 | conditional measurement |
| b = 0.5 ± 0.3 s (fast breakout) | +3.0 ± 0.7 | model-conditional |
| b = 1.0 ± 0.5 s | +1.8 ± 1.2 | model-conditional |
| b = 1.7 ± 0.5 s (standard jet model) | +0.1 ± 1.2 | the orthodox posterior |
| b flat on [0, 10] s (the LVC assumption) | −20 … +4.2 | the published band, reproduced |

What the table shows:

- **The error budget is ~90% model, ~10% data.** In units of 10⁻¹⁶: timing contributes ±0.12,
  distance ±0.34, the b-prior ±1.2. The dominant uncertainty on the anchor was never
  instrumental; it is the width of a jet-breakout model never independently measured for this
  event.
- **The orthodox reading moves the center, not the width.** Under the standard jet prior,
  ε = +0.1 ± 1.2 — consistent with zero, with an error bar three times the b = 0 branch's.
  "c_grav = c confirmed" is, stated honestly, ε = 0 ± 1.2×10⁻¹⁶ conditional on a source model
  whose own ±0.5 s width is an estimate.
- **Only the wedge is prior-robust.** Every row respects ε ≲ 5×10⁻¹⁶ on the positive side; no
  row's center survives a prior change. The event's unconditional content is the one-sided bound
  and one degenerate scalar; everything this lane banks unconditionally rides on those alone.
- Shape note, recorded and not leaned on: the interval closes three orders tighter on the
  negative side — but by a cosmic-ray accident (Cherenkov), not by the carve; the open room
  merely happens to sit where one-sidedness says physics could be.

Role discipline, stated for the lane as a whole: the projections downstream — the b = 0
forecast, the distance-scaling templates, the per-face ledgers — are role realism's method:
assume the propagation reading, label the bets, price the kills. None of that converts a row of
this table into a conclusion. The concluding read of GW170817 is the disjunction the table
carries: **the gap may be all source (the prior-favored row), all propagation (the exposed row),
or any split between — and this event cannot say which.** The wedge, the floor, and the
population program below exist because only new events move a row's status; no reanalysis of
this one can.

The b-prior width dies only by population — b scatters event-to-event while propagation trends
with baseline, so the model term shrinks as σ_b/(σ_T√N) (the regression below). Better host
distances shrink the b = 0 bar; a Galactic intercept event bypasses b entirely. Nothing removes
the single event's prior-dependence.

## Estimators

Two, one prior-free and one hierarchical:

1. **Floor statistic.** ε̂ = min_i (Δt_i / T_i). Consistent from above; bias = b_min/T at the
   deepest event (b_min ~ 0.1 s at 300 Mpc → ~3×10⁻¹⁸, below the target). Distant events do all
   the work — the statistic improves with reach, not with count.
2. **Hierarchical regression.** Δt_i = ε T_i + (1+z_i)·b(z_i; θ) with a population prior on b from
   jet modeling (non-negative, scale ~ seconds, event-to-event scatter σ_b); the (1+z) dilation is
   the source term's only distance growth — a factor ~2 by z = 1, slow against any path-accumulated
   term. Fisher scaling:

       σ_ε ≈ σ_b / (σ_T √N) ,

   with σ_b ~ 1 s and events spread over 40–300 Mpc (σ_T ~ 10¹⁶ s): σ_ε ~ 10⁻¹⁶/√N. Ten events
   resolve the GW170817 value at ~10σ if it is real, or bury it. At BNS–GRB coincidence rates of
   ~0.1–1/yr (imported), that is a decade-class program, with the one-event kill live throughout.

The confound the regression must carry explicitly: **source evolution**. A b that drifts with
redshift — progenitor metallicity, mass distribution, environment — is the one source-side carrier
that mimics the full signature (achromatic, sign-stable, distance-trending). The discriminant is
covariate structure: propagation rides comoving distance exactly; evolution rides host
astrophysics at fixed z. A population spanning host properties at fixed T splits them.

## Kernel recipes

C1's sourcing options, as compute rules. Each kernel names the covariate K_i that replaces T_i in
both estimators (the floor statistic generalizes: ε ≤ Δt_i/K_i):

| kernel | covariate per event | data source |
|---|---|---|
| constant ε | comoving distance / c | host z + background cosmology |
| ε ∝ Φ (H_p2) | ∫Φ dl along the line of sight | density-field reconstruction; residual–template cross-correlation |
| ε ∝ ρ | host column / local density | loads the intercept — collapses the split (C1, Cost 3) |
| dark-energy drag | ρ_DE-weighted z-shape | concave, low-z template |
| free ε(z) | none | nonparametric reconstruction over residuals; needs N ≫ 10 |

Achromaticity is itself a number to fit, not a slogan: dΔt/d ln f across EM bands consistent with
zero, with spectral-lag systematics priced. Inside the GW band the cone delta produces zero
dephasing — waveform dispersion tests are blind by construction, so their nulls are not evidence
against. ε < 0 (gravity slower) is not this note's subject; gravitational Cherenkov already kills
it (C1, bounds).

## Channel census

The per-event figure of merit is σ_b/T — emission-model uncertainty over baseline. What varies
across channels is not the physics but whose b you must believe:

| channel | T (s) | σ_b | σ_ε per event | note |
|---|---|---|---|---|
| BNS–GRB, 44 Mpc | 4.5×10¹⁵ | ~1 s | 2×10⁻¹⁶ | the anchor (GW170817) |
| BNS–GRB, 300 Mpc | 3.1×10¹⁶ | ~1 s | 3×10⁻¹⁷ | best per event; kill-lane |
| Galactic CCSN, ν vs GW, 10 kpc | 1×10¹² | 1–10 ms | 10⁻¹⁵–10⁻¹⁴ | cross-leg; b is modeled bounce dynamics, not fitted jet astrophysics |
| LMC CCSN, 50 kpc | 5×10¹² | 1–10 ms | 2×10⁻¹⁶–2×10⁻¹⁵ | one event reaches the anchor at the optimistic edge |
| LISA MBHB + EM, z ~ 2 | 5×10¹⁷ | hours–days | ~10⁻¹³ | εT ~ 200 s, but the baseline is wasted on b |
| lensed GW+EM image pairs | — | — | null | differential closes to ~ns for constant ε (C2) |
| CMB-frame dipole | — | — | parked | signal εβT ~ 2–16 ms against σ_b ~ s → N ~ 10³–10⁵ events |

The census's content: BNS–GRB timing is the instrument, and the only channel with genuinely
independent systematics within striking distance is a nearby-galaxy core-collapse supernova seen
in both neutrinos and gravitational waves — its emission offset is bounce physics locked at
milliseconds, not jet physics fitted at seconds. Two per century (imported), but free when it
happens, and it is a clean cross-leg pair: ν rides the matter cone, the GW rides gravity's.

## Status

The cone delta, granted, is maximally thin: one number, one wedge, one plot — which is what makes
it cleanly killable. The floor statistic needs no source model; the kill needs one distant event;
the detection needs ten and a priced b population. If the wedge never rises, C1 demotes exactly as
C2 specifies, and the floor's final position is the export: the tightest matter-vs-gravity cone
bound the population supports.

Owned: the wedge as the complete observable surface; the anchor's error budget with its
prior-indexed decomposition and the disjunction it forces; the prior-free floor statistic and its
one-event kill; the σ_b/T channel rule; the kernel-to-covariate assignments; naming source
evolution as the sole full-signature source-side mimic. Imported: all rates, jet and bounce
emission models, σ_b values, selection functions, density-field reconstructions, cosmology,
detection pipelines, and every number in the census table.
