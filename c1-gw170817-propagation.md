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
it into emission offset and propagation offset; both enter the same scalar.

## The cone ratio

Gravity's causal cone is slightly wider than light's. The frame-independent content is the ratio:

    c_grav / c_light = 1 + ε ,   ε ≈ 3.8×10⁻¹⁶ = 1.74 s / τ .

An isotropic offset of light alone is coordinate-absorbable; only the ratio to gravity is physical,
because there are two cones to compare.

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
With `n` fixed and `B` constant there is no new propagating degree of freedom and no Boulware–Deser
ghost. The cost is that `n` is put in by hand.

## Measured vs assumed

One number is measured: ε, averaged along a single line of sight through mostly-empty space,
ε_eff = (1/D)∫ε dl. Taking ε as a universal constant `B` is an assumption. Under it:

- achromatic — no frequency dependence (dimension-4, geometric);
- non-birefringent — both polarizations ride the single metric g̃, in every frame; this is the
  non-birefringent (c-type) SME sector;
- isotropic in the CMB frame; a boosted observer sees a dipole scaling with velocity;
- over comoving distances the delay adds up.

## Predictions

- Propagation delay accumulates along the path as ∫ε dl. For constant ε this is linear in comoving
  distance, Δt(z) = ε ∫₀^z dz′/H(z′) (curved in luminosity distance — that curvature is cosmology,
  not the model). Constant ε is a special case: the accumulation *kernel* is what the data recovers,
  and its shape — not a slope — is the discriminant (see Source vs propagation).
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

1. **Absolute structure.** Fixed `n` is a preferred frame. Explicit Lorentz violation gives
   ∇^μT_{μν} = O(B) ≠ 0, against the Bianchi identity's ∇^μT_{μν} = 0 (Kostelecký). This vanishes on
   the FLRW background, so the model works as an effective description there but is not complete.
   Promoting `n` to a dynamical field (spontaneous breaking; Einstein-aether / bumblebee) restores
   conservation, reintroduces a degree of freedom, and reopens the ghost and preferred-frame (α₁, α₂)
   audits.

2. **Naturalness.** ε ≈ 3.8×10⁻¹⁶ runs to O(1) under radiative corrections (Collins–Perez–Sudarsky).
   A custodial (SUSY-like) symmetry gives ε = (m/M_Pl)², placing the breaking scale near
   m ≈ 2×10¹¹ GeV. Stability under gravitational loops is open.

3. **Uniformity.** If ε varies with position: ε ∝ Φ gives an achromatic Shapiro-sector anomaly in
   Cassini / LLR / pulsar timing / clock redshift at ~10⁻¹⁷–10⁻¹⁸ (this is H_p2). ε ∝ ρ acquires part
   of the delay at the merger itself — the densest point on the path — collapsing the
   emission/propagation split. Density-independence is a requirement of the reading, not a detail.

## Existing bounds and status

Because all matter shares one cone g̃, a universal matter-sector shift is a coordinate rescaling:
every matter-only comparison — photon-vs-fermion resonators, atomic clocks, neutrino-vs-photon timing
— is common-mode and blind. Only matter-vs-gravity comparisons are physical, and among those only
cosmological baselines beat the ε suppression. Lab tests therefore do not constrain H_p1;
multimessenger timing is the sole access.

- **GW170817 speed:** (c_grav − c)/c ∈ [−3×10⁻¹⁵, +7×10⁻¹⁶] (Abbott et al. 2017). The +7×10⁻¹⁶ edge
  *is* the pure-propagation reading; the window's width is the assumed 0–10 s emission delay. H_p1
  sits at that positive edge — contained, not excluded, not independently confirmed.
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
explanation until a population of sirens spanning distance exists. The decomposition — propagation,
measurement, dynamics, and chronology no longer assumed to share one geometric object — is the durable
content; the two-cone constant-ε closure is one way to realize it, and "c_grav = c_light" is the
conditional closure it competes with, not an established fact.

The companion kill-lane [C2](c2-lensing-before-propagation.md) prices the non-cone carriers — source
timing, population, waveform, path/lensing — before any cone delta is licensed.
