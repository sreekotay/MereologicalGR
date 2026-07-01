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

- Delay linear in comoving distance: Δt(z) = ε ∫₀^z dz′/H(z′). Against luminosity distance it curves;
  that curvature is cosmology, not the model.
- Directional term ~2 ms from our motion through the CMB frame.
- Lab photon-speed anisotropy at O(B·β_boost) ≈ 10⁻¹⁸ (β_boost ≈ 1.23×10⁻³).

## Tests

One event is degenerate with a source-timing coincidence. A population of standard sirens separates
the cases:

- Δt ∝ distance → constant cone-gap (this reading);
- Δt ∝ ∫Φ dl per sight-line → the potential-dependent variant (H_p2);
- Δt scattered with host astrophysics → emission timing.

Kill: Δt departing from proportionality to comoving distance across a siren population (beyond the
FLRW mapping), or a lab anisotropy bound below ~10⁻¹⁸ with no dipole.

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

## Existing bounds

Birefringence limits (~10⁻³²) apply to a sector this operator is not in; GRB dispersion limits apply
to dimension-5 (this is dimension-4); PPN α₁, α₂ ∝ ε ~ 10⁻¹⁶ sit below the 10⁻⁷–10⁻⁹ bounds;
binary-pulsar timing and Shapiro delay test the gravity sector, which is pristine GR here.
Gravitational-Cherenkov cosmic-ray bounds (~10⁻¹⁹) constrain the opposite sign (gravity slower); here
gravity is faster.

## Status

A single reading of one degenerate number, interchangeable with a source-emission explanation until
more than one siren is in hand. The decomposition — propagation, measurement, dynamics, and chronology
no longer assumed to share one geometric object — is the durable content; the two-cone closure is one
way to realize it.
