# C1 — GW170817 as a propagation delay (H_p1)

**Exploratory — not canon.** A captured hypothesis. Unlike the `a*`/`b*` notes (relabel inside GR, no
new dynamics), this one *exports new physics* and imports machinery the corpus does not own (disformal
/ bimetric couplings, Einstein-aether, the SME photon sector, Lorentz-violation naturalness). It is a
single un-ascertained reading of a degenerate number, held for the record and for its kill conditions
— not a graded claim.

Method: un-fuse the roles GR bundles inside the single metric — the causal-ordering cone and the
carrier-speed of light — and ask what a *pure-propagation* reading of the GW170817 gap requires.

---

## The measurement

GW170817: the gravitational-wave merger peak and the GRB 170817A gamma-ray onset arrived **1.74 s**
apart, over ~40 Mpc (~144 Mly; light-travel time τ ≈ 4.5×10¹⁵ s). The 1.74 s is a single
arrival-time difference — GW peak by matched filter, gamma onset by a count-rate threshold. One event
cannot split it into emission offset vs propagation offset; the two enter the same scalar.

## The claim

Read the whole 1.74 s as propagation, not emission. Gravity's causal cone is very slightly wider than
light's. The frame-independent content is the **ratio** of cone-speeds:

    c_grav / c_light = 1 + ε ,   ε ≈ 3.8×10⁻¹⁶ = 1.74 s / τ .

Light is not the edge of cause-and-effect; it runs just inside the true edge, which gravity marks.
An isotropic offset of light alone is coordinate-absorbable — only the ratio to gravity is physical,
because there are two cones to compare.

## Construction (one dynamical metric, no ghost)

One dynamical metric `g`, pure Einstein–Hilbert gravity — gravitational waves and the real causal
structure follow `g`'s null cones. Matter and light couple minimally to a slightly narrower effective
metric via a constant disformal deformation to a fixed unit timelike direction `n` (a preferred frame,
taken as the CMB rest frame):

    g̃_μν = g_μν + B n_μ n_ν ,   B ≈ 2ε ≈ 7.6×10⁻¹⁶ .

Toy action (units c=ℏ=1, signature −+++):

    S = (1/16πG) ∫√(−g) R[g]                                  (gravity, untouched GR)
      − ¼ ∫√(−g̃) g̃^{μα} g̃^{νβ} F_{μν}F_{αβ}                    (EM on g̃)
      + ∫√(−g̃) [ −½ g̃^{μν}∂_μφ ∂_νφ − V(φ) ] + …             (matter on g̃)

In the rest frame of `n`, g̃ = diag(−(1−B), 1, 1, 1), so the eikonal/null condition g̃^{μν}k_μk_ν = 0
gives ω = |k|√(1−B), i.e. c_light = √(1−B) ≈ 1 − B/2, while GW's follow `g` at c_grav = 1. Hence
ε = B/2. `n` is fixed and non-dynamical, `B` is constant → no new propagating degree of freedom →
no Boulware–Deser ghost. The price is that `n` is put in by hand.

## What is measured vs assumed

Measured: one number, ε, **averaged along one line of sight** through mostly-empty space —
ε_eff = (1/D)∫ε dl. Treating ε as a universal constant `B` is an *assumption*, not a result (and the
one that makes the effect maximally hidden). Under the constant reading:

- **Achromatic** — no frequency dependence (dimension-4, geometric). Forced, not tuned.
- **Non-birefringent** — both polarizations ride the single effective metric g̃. Exact in every
  frame, because a single metric has a single cone. Maps to the non-birefringent (c-type) SME sector.
- **Isotropic in the CMB frame**; a boosted observer sees a dipole scaling with their velocity.
- Over comoving distances the delay simply adds up.

## Predictions (constant ε)

- Delay linear in **comoving** distance: Δt(z) = ε ∫₀^z dz′/H(z′). Plotted against *luminosity*
  distance it looks slightly curved — that curvature is ordinary cosmology, not a failure of the model.
- Directional term ~2 ms from our motion through the CMB frame.
- Lab photon-speed anisotropy at O(B·β_boost) ≈ 10⁻¹⁸ (β_boost ≈ 1.23×10⁻³), near current
  optical-resonator reach.

## Tests, and how it dies

One event is degenerate with a source-timing coincidence. A population of standard sirens breaks it:

- Δt tracks **distance** → this hypothesis (constant cone-gap).
- Δt tracks **integrated potential** ∫Φ dl per sight-line → the potential-dependent variant (= H_p2).
- Δt **scatters** with host astrophysics → ordinary emission timing.

Decisive tests: (1) the distance-scaling across sirens; (2) the ~10⁻¹⁸ lab anisotropy. Kill: any
robust deviation of Δt from proportionality to comoving distance across a siren population (beyond the
known FLRW distance mapping), or a lab anisotropy bound below ~10⁻¹⁸ with no dipole.

## Costs and open points

1. **Absolute structure.** The fixed `n` reintroduces a preferred frame. Its concrete technical price:
   explicit Lorentz violation gives ∇^μT_{μν} = O(B) ≠ 0, in tension with the Bianchi identity's
   demand ∇^μT_{μν} = 0 (Kostelecký no-go for explicit LV in gravity). Harmless on the exact FLRW
   background — the propagation calc stands — so the model is a good *effective* description, not a
   complete theory. The consistent completion promotes `n` to a dynamical field (spontaneous breaking,
   Einstein-aether / bumblebee), which restores conservation but **reintroduces the degree of freedom
   the fixed version avoided** and re-opens the ghost and preferred-frame (α₁, α₂) audits.

2. **Naturalness.** ε ≈ 3.8×10⁻¹⁶ is unnaturally small under radiative corrections (Collins–Perez–
   Sudarsky percolation). A custodial (SUSY-like) symmetry gives ε = (m/M_Pl)², placing the breaking
   scale at m ≈ 2×10¹¹ GeV. Lands at the right order; stability under gravitational loops is unproven.

3. **The uniformity fork.** If ε is not constant:
   - ε ∝ Φ (potential) → an achromatic Shapiro-sector anomaly in Cassini / LLR / pulsar timing / clock
     redshift, ~10⁻¹⁷–10⁻¹⁸ at the scaled slope — under current bounds, and *this is H_p2*.
   - ε ∝ ρ (density) → **not a weak test but a consistency fork**: the densest point on the path is the
     merger itself, so part of the delay is acquired *at the source*, breaking the emission-vs-
     propagation split the hypothesis rests on. "ε independent of local density" is therefore an
     assumption the hypothesis *needs*, not a detail.

## Consistency with existing bounds (constant ε)

Survives not by smallness alone but by structure: birefringence limits (~10⁻³²) target a sector this
operator is not in; GRB dispersion limits target dimension-5 (this is dimension-4); PPN α₁,α₂ ∝ ε are
~10⁻¹⁶ ≪ 10⁻⁷–10⁻⁹; binary-pulsar timing and Shapiro test the gravity sector, which is pristine GR
here. Gravitational-Cherenkov cosmic-ray bounds (~10⁻¹⁹) constrain only the *opposite* sign
(gravity slower); H_p1 has gravity faster, in that probe's blind spot.

## Status

A single, un-ascertained reading of one degenerate number. Internally consistent, sharp and
falsifiable at the population level, with an explicit cost (an absolute frame, whose technical
signature is a conservation-law tension). Fully interchangeable with a source-emission explanation
until more than one siren is in hand.

## Methodology note (why the quantum parallel is not counted as support)

The ordering ≠ adjacency split this hypothesis makes at the propagation level also appears, already at
O(1), in the correlation sector: Tsirelson (2√2) is the per-adjacency (space-like) witness; Leggett–
Garg is the per-ordering (time-like) witness, and it is *not* pinned at 2√2 (it runs to the algebraic
4). That is s(cut) refusing to be one number — PB-2's "not necessarily a constant" in the quantum
sector. But per the repo's retrodiction rule, H_p1 and LG ≠ Tsirelson **share the held variable**
"ordering ≠ adjacency," so they do not aggregate to convergence — they sharpen the bet, and weight
lands only where that variable is forced to dissociate. LG ≠ Tsirelson needs no ε (it is O(1),
preferred-frame-free), so it is a lineage-clean *prior instance* of the carve, not evidence for the
10⁻¹⁶. It is not counted as support.
