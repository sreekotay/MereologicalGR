# C9 — The Cone Drag as Transport Structure

*Exploratory — not canon. Grade: formal development + bounds ledger, conditional on
[C1](c1-gw170817-propagation.md) through the pair ([C5](c5-the-order-pair.md)). Move-type (A0
§11): formalization and quantification of the existing split — no new peer role. The object here
is the seam's transport face: the difference of the two metrics' connections, what it derives,
what data bounds each of its parts, and the fork it reopens in C1's Costs. Referee computations:
`workbench/two-metric-seam/` (sympy; every Layer-2 formula below verified symbolically there).*

## Layers

```text
Layer 1 — owned (C1/C5/C8 lineage; b5's closure grammar):
  the drag as connection-difference: descriptions gauge, the differential physical
  the face map — the C4/C6 curve family as the congruence decomposition of one tensor
  the holonomy reading: Δt as translational holonomy; n as the defect-density profile
  the tilt/dilation role split and its discriminators
  the three-branch scoreboard; the third fork (compatibility-determined drag) and its audit
  the per-face bound ledger assembly

Layer 2 — projected (computed; sympy-verified in workbench/two-metric-seam/):
  the exact C formula, det g̃ = (1−B) det g, the Sherman–Morrison inverse
  the C = 0 rigidity theorem; exact path-identity; the δα/α = ε lensing residual
  the FLRW reduction and the comoving timing integral (the chain realization
    carries the extra (1+z))
  the multipole content ℓ ≤ 2 of the general nesting drag; dipole = gauge
  the count-compatibility rigidity (universal density ⟹ B constant)
  the QED floor with exact coefficient (5.1×10⁻⁴³ today)

Layer 3 — imported:
  disformal machinery (Bekenstein gr-qc/9211017; Zumalacárregui–García-Bellido 1308.4685;
    Bettoni–Liberati 1306.6724); the EFT-of-DE α-basis and the 2017 quartet (1710.05877,
    1710.05901, 1710.06394, 1710.05893)
  the Einstein-aether kinematic basis (Jacobson 0801.1547) and its post-GW170817 bounds
  the de Rham–Melville cutoff (1806.09417); multiband forecasts (2207.10096, 2203.00566)
  every bound: Cassini, CMB c_T, PTA, Cherenkov, GWTC-3, pulsar preferred-frame
  CPS naturalness and its evasions (gr-qc/0403053; 1601.06700; gr-qc/0512139)
  Euler–Heisenberg / LPT vacuum-velocity formulas
```

## The tensor

Two metrics, g and g̃ = g + h with h = B n⊗n, give two Levi-Civita connections, and the seam's
transport content is their difference — a genuine tensor built from a non-tensor pair:

    C^λ_μν = Γ̃^λ_μν − Γ^λ_μν = ½ g̃^{λρ} ( ∇_μ h_ρν + ∇_ν h_ρμ − ∇_ρ h_μν ) ,

exact, not merely O(h), with det g̃ = (1−B) det g and g̃^{μν} = g^{μν} − [B/(1−B)] n^μn^ν. Each
cone's offset alone is coordinate-absorbable (C1); the differential is physical — the same move
by which the contortion tensor is physical while each connection is gauge (b5: Γ = {} + K). The
frame-transfer parallel is structural, not decorative: gravity-the-force dissolved into
connection description; the drag is the candidate for the same dissolution one level up, and n is
its Christoffel-like face (seam-flavored, evaporating in the fused limit) while ε is its
curvature-like face (a pair-invariant, not zeroable).

The standard-literature identification: h = B n⊗n is Bekenstein's disformal transformation at
A = 1 with n a normalized gradient — which requires the congruence hypersurface-orthogonal; a
twisting matter flow needs the vector generalization, and the vorticity face below is reachable
only there. In the EFT-of-dark-energy basis the drag is the tensor-speed excess: ε = +α_T/2 in
the matter frame, and only the *relative* tilt of the two cones is observable — the disformal
frame-equivalence theorems say precisely that the connection-difference is the invariant content.

## The C = 0 theorem

If ∇(B n⊗n) = 0 the two connections coincide. The hypothesis is rigid: contracting the condition
forces **B constant and ∇n = 0**, which only ultrastatic products admit. There, path identity is
exact to all orders in B — every geodesic of the shared connection has a speed-independent
spatial track, so the g̃-null photon and the g-null GW traverse the *same curve* and the entire
observable difference is arrival timing, at lag rate (1−B)^{−1/2} − 1 = ε + 3ε²/2 + … per unit
path. Timing-only observability is a theorem, not an observation.

Where the hypothesis fails — every real lens — the residual is computable: cone-selection through
a potential gives α_γ − α_GW = (2GM/b)·B/(1−B), a fractional GW/EM image offset δα/α = ε,
sourced specifically by the acceleration face and ∇B. At 4×10⁻¹⁶ fractional it is hopeless as a
detection channel; its role is negative — deflection, Shapiro geometry, and lensing tests are
structurally blind at leading order, and the one instrument that touches path structure is the
lensed-event *differential* (below).

## The decomposition: the curve family is one tensor

C is built from ∇B and ∇n, and ∇n decomposes along the seam congruence into acceleration a,
expansion θ, shear σ, vorticity ω. The face map, from the verified closed form: **θ and σ
retime** (clock effects along n, isotropic and direction-dependent respectively); **a and the
transverse gradient D⊥B refract** (the δα/α = ε class); **ω** couples the cones' frame-dragging —
a Sagnac-type circulation asymmetry with no counterpart in the other faces; **Ḃ retimes only**.
In FLRW with comoving n the tensor reduces exactly to

    C^λ_μν = [B/(1−B)] (θ/3) n^λ P_μν ,   θ = 3H ,

and the accumulated residual is the integral Δt = ε ∫₀^z dz′/H(z′) — (1+z)-weighted relative to
cosmic time, equivalently the unweighted comoving integral εD_C/c — C3's master relation,
confirmed exactly (a proper-path integral without the redshift weight undercounts by ~χ/η₀; the
chain realization carries one further power of (1+z), the depth-separable difference —
`workbench/cosmological-fan/`).

Three consequences the lane previously carried as choices:

- **The response family's argument is derived.** Expansion is the only seam invariant a
  homogeneous universe supplies; ε = f(H) is the generic transport face, and f(0) = 0 is the
  statement that the transport face has nothing to be made of in Minkowski — vacuum restoration,
  not an assumption.
- **The C4/C6 curve family is the congruence decomposition of one tensor**: the θ-face is the
  response family, the a-face is H_p2 (potential-correlated), the σ-face is the structure-
  covariance discriminant, ∇B is the source-peaked pathology. The menu was never a menu.
- **T1 is the lone support-mover**: the constant-kernel member is the only one whose transport
  face is off forever — response without stimulus, requiring vacuum Lorentz violation proper.
  The early discount of T1 is retroactively a derivation.

## The holonomy: a temporal Burgers vector

The two-messenger observable formalizes as holonomy around the closed loop (emit both at one
event, close the comparison on one detector worldline): to leading order

    Δτ = ∮ ϑ ,   ϑ = ε(k̂, l) dl / c ,

a **translation holonomy — perimeter-supported, like the Burgers vector of a screw dislocation —
not a curvature holonomy, which scales with enclosed area.** In b5's closure grammar: curvature
is rotational closure failure, torsion is translational closure failure, and GR's empty
translational cell is exactly the *shape* of the seam's observable — translational closure
failure in time. The distance-scaling exponent reads cleanly: Δt ∝ Dⁿ means the cone-gap line
density runs as ε(l) ∝ l^{n−1} (C8's identity, now as defect-density profile) — n = 0 an
endpoint/boundary defect, n = 1 a homogeneous dislocation (constant B predicts exactly this),
n = 2 the transition to genuinely area-supported (curvature-like) holonomy, n = 3 volume-like.
Multi-distance sirens measuring n are measuring the radial profile of the defect density.
Novelty flag, from an adversarial literature sweep: the timing residual as the integrated
holonomy of the connection-difference appears to be unoccupied in print — the ingredients
(tensoriality of C in the disformal literature; line-of-sight integrals in the GW-propagation
literature) exist separately and unsynthesized.

## The multipoles: what anisotropy can even be

The general nesting-preserving drag gives a direction-dependent gap ε(k̂) = ½[h₀₀ + 2h₀ᵢk̂ⁱ +
hᵢⱼk̂ⁱk̂ʲ] — **monopole, dipole, quadrupole, nothing higher** (nine invariant components; the
conformal mode drops exactly, cones being conformal-class objects). The dipole is removable by
re-choosing n: it reads the observer's boost against the seam frame — C1's ~2 ms dipole is this,
real as a velocity measurement and empty as seam anisotropy. **The invariant anisotropy is a
five-component quadrupole.** Intra-matter experiments are exactly blind (one cone serves both
arms); the readers are cross-sector: the siren sky map's invariant content is monopole +
quadrupole in Δt(k̂)/D, and CD-6 is re-cut accordingly in CLAIMS. The Einstein-aether precedent
is consonant: there the tensor speed couples to the shear coupling alone, and GW170817 bounds
exactly that combination (|c_σ| ≲ 10⁻¹⁵) while leaving the rest of the frame's coupling space to
weaker PPN and pulsar tests.

## Branches and prices

Support versus weight, stated once. Microcausality *saturates*: commutator support ends exactly
on the cone; what sits strictly interior is thresholded arrival — spread weight plus a finite
threshold gives interior, delayed, never-advanced arrival. In exact vacuum, Lorentz invariance of
one metric forces every field's support onto the same cone — which is the fusion under audit
stated as a symmetry, and every precision "LI test" is same-leg: per-sector LI, which the pair
keeps exact. The fused global boost group has one cross-sector datum. The scoreboard:

- **Fused + source-side**: no new physics, one astrophysical model (b ≈ 1.7 s). Forced, not
  merely preferred: within the fusion a propagation reading needs the weight branch to deliver
  the anchor, and the computed floor is the thermal Euler–Heisenberg drag against the CMB,
  δv/c = −(44π²/2025) α² (T/m_e)⁴ = 5.1×10⁻⁴³ today (2.4×10⁻⁴² without the prefactor; the
  curvature member is 10⁻⁸⁰ cosmologically). Gap to the anchor: **10²⁶·⁹**. The four levers in
  the formula — ρ (measured), m (excluded), coupling (walled), response power (the p-family) —
  leave only the last, so fused-propagation is dead by 27 orders unless the response to the
  background is nonlinear by that amount while staying achromatic.
- **Fused + propagation**: dead as above — which is the *derivation* of orthodoxy's source-side
  reading, and of why the official bound imports an emission model.
- **Unfused**: ε₀ = 4×10⁻¹⁶ is a measurement, not an amplification; the debts are the carve
  (C1 Cost 0), the realization (the fork below), and a stabilizer (naturalness runs toward
  "why so small," not "how so large").

The weight branch carries its own sign derivation: interiority scales with dressing, dressing
with coupling, and gravity (G) is the least-dressed carrier in physics — its realized front hugs
the kinematic cone closest, photons (α) run interior. At floor level the photon-leg sign is now
**forced** (two-leg referee, 2026-07; `workbench/two-metric-seam/two_leg_lock.py`): the
commutator leg's protection licenses Kramers–Kronig with front = c, KMS passivity makes the
thermal dressing pure added spectral weight (coth ≥ 1; vacuum-subtracted absorption nonnegative
below pair threshold), and the sum rule forces n(0) ≥ 1 — δv(ω→0) ≤ 0, the Euler–Heisenberg
minus sign as structure, not coefficient luck. Scope: forced for KMS dressings and as a
DC-versus-front statement only — Casimir (mode-removal) genuinely runs v(0) > c, and
Drummond–Hathrell proper stays dispersion-relation-dependent. The *differential* is now folded
(2026-07; `workbench/two-metric-seam/cross_sector_fold.py`, 19/19 checks): the fabric leg's
floor is its own sources' Ricci trace — n_gw − 1 = +R/12ω², phase interior, group exterior by
exactly the same amount, front pinned at c, photons conformally blind to the term. The photon's
KK chain provably cannot close there (gapless response — the zero-frequency-pole loophole plasma
uses); the sign is forced instead by the trace energy condition, p ≤ ρ/3: KMS signs the matter
leg, an energy condition signs the fabric leg, and where neither holds (kination) the front
still does. At arrival level the differential is **one-signed at every frequency** — the photon
runs more interior, both floors adding to Δt_γ−GW > 0 — with the two regimes changing hands at
f* ≈ 130–430 Hz, inside the LVK band, straddling the frequency wall at 260 Hz (both scales
H₀-powered). The GW group advance is sub-cycle-capped — under half a radian of accumulated phase
for any sub-horizon mode over cosmic history — so one-sidedness is untouched at every band: the
only exterior-signed object the fold produces lives on the fabric leg, below one cycle, at the
rendered tier. The
anchor-scale sign derivations (the grammar theorem; the halo asymmetry) are untouched by this.
Species order among matter messengers by coupling at the 10⁻⁴³ class: real, forced, and
operationally invisible — which is why the one-matter-cone statement survives.

The 2026-07 sweep sharpened the mechanism and drew its boundary. Realized fronts saturate their
ceilings exactly in **protected** sectors — free, integrable, or phase-space-starved (d = 2
chiral CFTs saturate at strong coupling, v_B = v_E = c: the honest counterexample, protected
because no transverse phase space exists for weight to spread into) — and sit strictly interior
at generic coupling (v_B = √(2/3)·c at *infinite* coupling in 3+1d holography; v_E ≈ 0.62;
log-cone at the MBL extreme). Where rigor is forced, the bound's form comes out intensive and
state-dependent (no state-independent LR bound exists for lattice bosons; the honest bound
scales with local density) — PB-2's declared form, landed independently. So what orders realized
fronts is proximity to protection, not coupling per se — and gravitons are the most
free-field-like carrier in nature: gravity riding closest to its cone is the pattern's own
prediction, not its exception. b9's reconciliation contact resolves on exactly this split (its
§2 carries the resolution).

## Tilt and dilation: two phenomena, one degeneracy

A **tilt** is ordering-role structure: a signed, oriented cone ratio, coherent and universal,
accumulating by geometry. A **dilation** is expression-role structure: per-episode latency at
conversion or rendering. The kernel tier supplies the dilation's sign law: off-cone, "after" is
frame-dependent (C8's frame-entry), so the kernel halo carries no invariant orientation — it is
an *unsigned width*, ~ƛ — and the signed structure lives at interfaces, with asymmetric range:
**advance capped by the halo (~1/ω), delay unbounded.** Consequences:

- **Dilation generates one-sidedness automatically** — per-episode asymmetry drifts accumulated
  arrival to net delay. Third independent derivation of the sign (grammar theorem on the tilt
  branch; coupling hierarchy on the weight branch; halo asymmetry on the dilation branch). The
  cost of the abundance: an observed one-sided, distance-growing Δt does **not** uniquely
  indicate a tilted cone. At the mean level a large-N dilation chain is indistinguishable from a
  smooth tilt — C8's n = 1 conversion/path degeneracy, with its mechanism named.
- **Kernel carriage, correctly bounded**: a single interface crossing cannot carry the anchor
  (1/ω ~ 10⁻²¹ s against 1.74 s — unconditional, the halo's own width); accumulated kernel
  dilation (n ≥ 1 chains) is *not* excluded by the cap — it is the quantum-floor chain family,
  constrained only by mean-achromaticity (forcing ƛ-scaled steps or suppressed costs) and by the
  sector-owned-coefficient requirement (a sector-universal chain yields zero cross-leg
  differential and cannot carry the anchor).
- **The discriminator is species structure**: a tilt is a property of the one matter cone —
  universal, cancelling exactly in matter-vs-matter timing; a dilation is interface-owned —
  ν–γ differentials are possible with the cone still one. **A timing split is not a cone split.**
  CD-3 is refined accordingly in CLAIMS: a CCSN ν–γ residual kills the row-as-written only if the
  dilation channel is excluded; under dilation the one-cone claim survives the split.
- **Realization-space update (2026-07, computed against PTA noise budgets).** The ƛ-step chain
  predicts a per-epoch white-noise floor σ = √(D ε₀ ƛ)/c, scaling D^{1/2} ν^{−1/2} — 75 ns at
  J1909−3744 (1.15 kpc, 1.4 GHz) against a noise budget that closes at ~10 ns: **excluded ~7×,
  but only for latency decorrelation times in the observational window** (minutes–hours).
  Quenched realizations — the natural, state-tracking case, since the sightline crosses one
  ~500 AU step in ~25 yr — freeze into constants absorbed by pulsar phase; per-pulse
  realizations bury under ~9 μs of intrinsic single-pulse jitter (a 10⁻⁵ variance fraction).
  Retained handle: the chain predicts **distance-correlated jitter (∝ D^{1/2}) across the MSP
  population; intrinsic jitter predicts none** — decidable by re-analysis of published jitter
  tables. The measured jitter frequency-index (−0.42, near the chain's −1/2) is filed as
  coincidence unless the distance test says otherwise.
- **The rendered/constituted resolution**: the thirty-year Hartman-effect dispute — are
  tunneling/evanescent advances real? — is a tier collapse. The advance is real at the rendered
  tier (phase-sensitive, centroid observables) and forbidden at the constituted tier (threshold
  crossings are front-limited). Both camps correct, about different rungs; the ladder's
  rendered ≠ constituted line is the referee. Could-fail: a threshold detector ever firing early
  kills the resolution and much else.

## The third fork

C1's Costs fork the realization as Horn A (fixed background) versus Horn B (sourced). The
transport reading opens a third tine: **Horn C — the drag is compatibility-determined**, fixed
the way Levi-Civita is fixed, by coherence axioms between the descriptions, with zero independent
Cauchy data. What is established, what fights, and what is owed:

- **The obstruction result.** Joint metric-compatibility (∇g = 0 ∧ ∇g̃ = 0) forces B constant
  and ∇n = 0 — impossible in an expanding universe. The drag tensor is the obstruction tensor to
  the two metrics sharing a connection, the obstruction decomposes exactly into (∇B; θ, σ, ω, a),
  and no ∇B can cancel the kinematic pieces. An expanding universe does not permit the drag to
  respond to expansion; it forces it to. Under a max-compatibility reading, B = f(H) is derived
  in form, the shared-boundary axiom kills the integration-constant sector, and the amplitude
  stays calibrated — the house split, derive the slot, calibrate the scalar.
- **The axiom fight, priced.** Count-compatibility with universal density forces B *constant*
  (one sprinkling cannot host a varying gap without breaking number–volume universality in a
  sector); the obstruction result forces B = f(H). Inconsistent as stated. Resolution options:
  relax the count axiom to a shared-volume-form version, pricing the factor as a matter-unit
  rescaling Ω = (1−B)^{−1/8}; or accept constant B — which is T1, the discounted corner. The
  choice is now explicit; choosing silently would be the torsion-free move.
- **The minimal-seam audit.** Pure trace along n is role-licensed exactly where the congruence
  is isotropic; in shearing regions the same logic that forces B(H) makes a shear-coupled
  component τ ∝ σ expected, not merely permitted — anisotropic cone deficit correlated with
  local shear, far below the 10⁻³² quadratic-form certification cosmologically. Setting τ = 0
  globally is the unearned cell, named.
- **Naturalness, conditionally.** Collins–Perez–Sudarsky binds Lagrangian-parameter Lorentz
  violation; state-sourced frames (media, condensates — the emergent-spacetime results) evade it
  because loops renormalize the parent theory and the state-dependence rides along. The
  protection holds only if the drag demonstrably tracks the local matter state — which welds
  Horn C to its own kill shots: a drag tracking a fixed sidereal frame kills C (leaves A); a
  drag tracking the CMB frame *where it differs from the matter bulk* kills C's congruence form
  (C1's registered fork is the execution site); a drag in structureless voids kills C; any seam
  wave or retarded response (independent Cauchy data) pushes the structure to Horn B. No
  CPS-style radiative analysis of a congruence-sourced disformal factor exists in the
  literature — an open niche.
- **The thermodynamic selector (2026-07; resolution at C5's GSL wall).** A standing
  two-temperature horizon is a genuine second-law breach — Dubovsky–Sibiryakov's perpetuum
  mobile, with a classical shell-extraction version (Eling–Foster–Jacobson–Wall) that needs no
  quantum channels (import corrected with C5's wave-optics resolution: the classical tine has a
  published dynamical obstruction, Benkel et al. 1803.01624, so the weight sits on the quantum
  D-S channel — which the per-sector wave-optics derivation confirms) — and smallness of ε sets
  the rate, never the verdict. The unique escape is
  **flux-constitution**: n is the infalling matter congruence, so B vanishes on exactly
  stationary horizons, the horizons fuse, and the GSL holds; the two-temperature state exists
  only during accretion, where accretion's own entropy production dominates by ≥ 45 orders.
  That escape is Horn C's state-tracking form and nothing else's: **Horn A dies at this register
  outright**, and the axiom fight above loses its constant-B tine on stationary geometries
  (a universal-density count axiom forcing global constant B would include them — dead). Third
  independent selection of the composite member: global sanity, naturalness, now thermodynamic
  consistency. The orthodox alternative — a universal-horizon rescue — requires energy-dependent
  ε, a dispersive seam living on the frequency wall's axis: a structural fork with its own
  signature (frequency-dependent cross-leg residuals).
- **The objection, unsoftened.** Horn C has no uniqueness theorem. Levi-Civita earns its status
  by existence-and-uniqueness; the two-order analog (the pair plus one count determines both
  geometries plus n plus B up to scale) is C5's open conjecture, and until it is proven,
  "compatibility-determined" is an analogy with an existence gap — and possibly only a
  presentation of an algebraically-sourced Horn B. The non-verbal content is exactly: zero
  Cauchy data, frame-tracking, f(0) = 0, kinematic covariance. Filed as owed. Surveyed
  (2026-07; `workbench/two-metric-seam/bianchi_seam_branch.py`): in Hassan–Rosen bimetric
  gravity the exact lapse-only seam is obstructed on the healthy branch (the Bianchi constraint
  forces X = y + ẏ/H, so y ≡ 1 forces B ≡ 0) and survives only on the strongly-coupled algebraic
  branch — but the viable finite branch in its GR limit, with one parameter condition, realizes
  **g̃ = (1 − B/3)(g + B u⊗u)**: the seam plus a conformal dressing of derived shape, and null
  cones are conformally invariant, so every timing observable sees the pure seam. The nesting is
  **forced** — the expanding finite branch gives the fabric cone strictly wider, the opposite
  orientation living only on the ghost-dead infinite branch. B = 6(H/m_FP)² with B ∝ Ḣ —
  f(0) = 0 automatic, vanishing in de Sitter as well as Minkowski, sharpening the response
  family's argument from H to Ḣ and selecting **p = 2** in C6's exponent. B ~ 10⁻¹⁶ today needs
  m_FP ≈ 1.4×10⁻²⁵ eV — two orders under the graviton-mass bound, five inside the Λ₃ window,
  Higuchi-safe. The gap narrows to one named calculation: whether the finite branch's early-time
  gradient window (H ~ m_FP, z ~ 6×10⁴) clears CMB-observable modes at that parameter point.
  Existence: modified, favorable; uniqueness: still open.

## The per-face ledger

| face | best current bound | epoch / scale | source | status vs anchor |
|---|---|---|---|---|
| kinematic, gravity-fast | ε ≤ 7×10⁻¹⁶ | z = 0.01, one sightline, ~100 Hz | GW170817 (1710.05834) | the anchor |
| kinematic, gravity-slow | ε ≤ 2×10⁻¹⁹ (one-sided) | UHE cosmic rays | Cherenkov (hep-ph/0106220) | dead (nondispersive) |
| θ (epoch, ε = ε₀E(z)^p) | c_T² < 2.85 (95%) at z = 1100 → **p ≤ 3.5**; O(1) at z ≲ 2 | recombination; LSS | 1405.7974; α-basis fits | 15 orders open; every p ≤ 3 unconstrained |
| a (Φ-correlated, ε = κ_Φ Φ/c²) | κ_Φ ≲ 10⁻⁵ *only if photon-coupled* (Cassini); none GW-only | solar system | Bertotti+ 2003 | **alive**: anchor needs κ_Φ ≈ 4×10⁻¹¹ → 5.4+ orders unprobed (5.5 fs at Cassini) |
| σ (anisotropic) | ~10⁻¹⁵ per direction, one sightline; \|c_σ\| ≲ 10⁻¹⁵ (aether) | LVK band | SME/aether readings (1802.04303) | alive by a factor of a few, direction-starved |
| ∇B (source-peaked) | none (10⁻⁷ differential per lensed event, forecast) | lens scale | Collett–Bacon (1602.05882) | unconstrained; lensed events the unique probe |

Preferred-frame pulsar bounds, corrected import: α̂₂ < 1.6×10⁻⁹ (solitary MSPs — five orders
tighter than the binary-era figure C1 carried) — and still not mapping onto κ_Φ
model-independently; in generic frame theories the tensor speed and (α₁, α₂) are independent
coupling combinations.

**The frequency wall.** The anchor sits at the dark-energy EFT's own cutoff, Λ₃ = (M_Pl H₀²)^{1/3}
≈ 260 Hz (de Rham–Melville): operators generic at the cutoff drive c_T(f) → 1 there even when the
cosmological, low-frequency cone differs. The celebrated 10⁻¹⁵ is a one-frequency statement;
across ~19 decades (CMB → PTA → LISA → LVK) the constraint degrades to O(1), and the within-band
chromaticity kills of C8 (per-quantum λ²) do not police band-to-band structure. Multiband sources
(LVK+LISA) reach ~10⁻¹⁷ on exactly this axis. A wall and a lever, both previously uncounted.

**Future levers, ranked**: 3G BNS+GRB populations (ε ~ 5×10⁻¹⁸ per event at z = 2; maps p and the
quadrupole simultaneously); one lensed multimessenger event (the only ∇B/a separator — zero
emission systematic); a Galactic CCSN (floor 1.2×10⁻¹⁵ at 8 kpc/1 ms; under an anchor-carrying
a-face the Galactic prediction is 8.5×10⁻¹⁷, so a null discriminates readings rather than killing
the lane — and the ν–γ channel is the tilt/dilation discriminator); LISA counterparts (the only
buyer of z = 3–5 and the mHz band).

Owned: the connection-difference reading with the gauge/differential split; the face map deriving
the curve family; the holonomy reading with the defect-density profile of n; the multipole
theorem's re-cut of the anisotropy program; the scoreboard with the fused-propagation kill; the
tilt/dilation split with its three sign derivations and the CD-3 refinement; the third fork with
its axiom fight, kill shots, thermodynamic selector, and confessed existence gap; the
protected-sector boundary of the interiority mechanism; the pulsar slice-kill with its retained
population test; the ledger assembly. Imported: all disformal/EFT machinery, every bound and
coefficient, the cutoff argument, CPS and its evasions, the aether basis, the
Dubovsky–Sibiryakov/EFJW/Jacobson–Wall thermodynamic results, the v_B/v_E literature. Could-fail:
a credible negative-ε residual (dies with CD-2); a GW/EM path-geometry difference beyond
δα/α = ε (kills the transport reading wholesale); a threshold detector firing early (kills the
tier resolution); seam waves or retardation (kills Horn C into Horn B); a drag tracking a fixed
sidereal or wrong-congruence frame (kills Horn C's congruence form at C1's fork); a standing
two-temperature requirement on an exactly stationary horizon (breaks flux-constitution, with
C5); realized fronts saturating their ceilings at generic coupling outside the protected sectors
(kills the weight branch's mechanism); MSP jitter showing no distance correlation *and* the
chain surviving anyway by quenching (not a kill — the honest no-contest outcome); the two-order
uniqueness conjecture failing (Horn C demotes to vocabulary); a distant coincidence under C3's
floor (kills the constant member and banks the bound, as designed).
