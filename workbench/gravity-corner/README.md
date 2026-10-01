# Gravity read at the null corner

Referee: `gravity_corner.py`, 15/15.

`gravity = ordering + influence + energy-momentum` is the one root-level composition that
carries **no flow**. The null corner (`workbench/null-corner`) is where flow is stripped while
transverse adjacency survives. So the corner is where gravity can be read with nothing it does
not need.

---

## 1. What gravity is at the corner

On a light-sheet, Raychaudhuri gives:

```text
dθ/dλ = −θ²/2 − σ² − R_kk          R_kk = 8πG T_kk
  θ    rate of change of transverse area    adjacency
  λ    affine parameter                     ordering, no unit
  σ    shear of the transverse area         adjacency deformation (Weyl / gravitational waves)
  T_kk energy-momentum along the generator  E-M
```

Read in MGR terms, **gravity at the corner is energy-momentum bending adjacency along
ordering**. No frame or flow enters. Requiring `R_kk = 8πG T_kk` for every null `k`, together
with Bianchi and conservation, returns the full Einstein equation (checks 1, 3). So the corner
carries all of GR except one piece (§2).

Two things follow for the corpus:

- **A0's operational chain** (E-M → curvature → **frame-transport** → rendering → uptake) is the
  timelike route. The corner is a second route that never passes through `frame`, which needs
  flow. The chain describes how a flow-bearing writer meets gravity. It is not what gravity
  needs.
- **The formula names the source side only.** At the corner, what gravity acts on is adjacency
  (area, shear, tidal strain). That patient is missing from `ordering + influence + E-M`. This is
  sweep F3's pattern again: a one-place formula for a relation that is actually indexed.

**Gravitational waves** are gravity's photon. A GW is pure transverse-adjacency deformation (the
shear `σ`, TT strain) carried along ordering, with no flow. "No information in flight" is
already **GB-3** in CLAIMS (null generator / GW ray / photon-in-flight). Detection is
chronometry: LIGO reads strain as a change in the round-trip time of light, timed by the laser's
phase, so it is ordering plus one writer's flow. That is the corrected F1 at work.

**Jacobson 1995.** δQ = T dS over local Rindler horizons. When the boost field is renormalised
`χ → aχ`, both δQ and `T` scale by `a`, so their ratio is invariant (check 4a). With
`η = 1/(4Għ)`, ħ cancels too (4b). Both the flow import (the accelerated observer) and the
quantum import cancel, and what remains is corner geometry, `R_kk = 8πG T_kk`. On MGR's
reading, the thermodynamic dressing is scaffolding. Jacobson notes that ħ drops out, and that
the thermodynamic route's most-cited payoff is the next point. This part is retrodiction.

## 2. What the corner cannot see: Λ

A symmetric tensor that vanishes on every null vector is a multiple of `g` (check 1). So the
corner is blind to exactly the part of gravity proportional to `g`:

```text
Λ g_kk = 0            vacuum energy  T_ab = −ρ g_ab  →  T_kk = 0          (check 2)
corner equation + Bianchi + conservation  →  G_ab + Λ g_ab = 8πG T_ab,  Λ an integration constant
                                                                           (check 3)
```

Taken literally, a flow-free gravity composition is **trace-free (unimodular) gravity**. Λ is a
constant of integration rather than a coupling, and vacuum energy does not source the corner.
Classically this is equivalent to GR. All of it is prior art: Anderson–Finkelstein,
Henneaux–Teitelboim, Weinberg 1989, Ellis et al. 2011, Jacobson's remark on Λ, and Padmanabhan's
null-vector argument that gravity should be invariant under `T_ab → T_ab + const·g_ab`.

**Λ acts only where there is flow.** In Schwarzschild–de Sitter (check 5):

| | Λ-dependence |
|---|---|
| null focusing `R_kk` | none (0) |
| tidal / shear part, `Weyl² = 48M²/r⁶` | none |
| timelike focusing `R_uu` | `−Λ`: defocuses flow-bearing congruences |

**Malformed diagnosis: "does Λ bend light?"** At the corner the answer is no: focusing and
shear are both Λ-free. A bending angle is a composite that needs an observer, which means a
flow, and Λ enters only through that argument. The literature dispute matches in mechanism.
Rindler–Ishak (2007) got a Λ term with static observers. Butcher (2016) finds exact agreement with
the Λ = 0 lensing law to second order, once angles and distances are those of a comoving
cosmological observer. That observer follows the congruence that approaches local isotropy. The
disagreement was about which flow, which is where the corner reading puts it. Retrodiction, with
the mechanism shared.

**Where Λ's value could come from.** If gravity has no flow, Λ has to be fixed by something
that is not at the corner. Two candidates are on file: an imported global scalar (the cosmology
closure's H₀ import, per HOW-TO-READ), or **number**. In unimodular gravity Λ is canonically
conjugate to 4-volume. c5 imports "order + number = geometry" and assigns counting to flow
("counting supplies the conformal factor, hence proper time"). The null corner shows counting
also yields area (links across a horizon) with no flow involved. That points to a fusion in
c5: **number sits under both flow and adjacency.** If MGR unfused number, it would inherit
Sorkin's everpresent Λ (Λ ~ ±1/√V, of order H² at every epoch). That is a causal-set prediction,
not ours, and it currently fits the data as well as ΛCDM (Aspects of Everpresent Λ II, 2024).
This is a fork for the corpus, not a result.

## 3. The seam breaks the corner's blindness

Vacuum energy is invisible at the corner only when it is proportional to the metric the corner
is built from. In the C/D lane matter rides `g̃ = A(g + B n⊗n)`, and gravity is `g`:

```text
√(−g̃) = A² √(1−B) √(−g)                                             (6a)
content vacuum seen at the fabric's null corner:
   −ρ̃ g̃^ab k_a k_b = ρ̃ B / (A(1−B)) · (n·k)²   ≠ 0                 (6b, 6c)
```

The content sector's vacuum energy acquires a **rank-1 part along n, of order B·ρ̃_vac**, which
the fabric corner does see. If B is state-sourced, as c9 has it (Ḣ-sourced, `p = 2`), the
vacuum term `−ρ̃ A²√(1−B(state))` is a state-dependent energy, not a constant. The sign and the
exact coefficient depend on how `n` and `B` depend on `g`. That is model-level, and it is not
fixed here. The order of magnitude is the point.

Consequences, stated evenly:

- Trace-free protection, which the flow-free composition gives for free, is single-metric. The
  two-cone hypothesis gives it up at order B for the content sector.
- In c9's bimetric realisation this is the familiar statement that matter loops renormalise the
  content-metric cosmological term (β₄ in Hassan–Rosen). That term is radiatively stable as a CC
  term, which is just the CC problem. But β₄ enters the background ratio, and so enters the cone
  deficit. **The CC tuning becomes a tuning of the observed cone ratio.**
- c9 flags *"No CPS-style radiative analysis of a congruence-sourced disformal factor exists in
  the literature — an open niche."* This is the leading entry into that niche, at the level of
  vacuum energy before any loop-induced Lorentz violation. c9's dust-channel normalisation F
  and the Ḣ-sourcing of B were computed without the content-vacuum term. **The could-fail:** with
  ρ̃_vac at any QFT scale above ~meV, the term dominates the B-sector dynamics unless ρ̃_vac is
  tuned in the content frame. Owed: put the term into `workbench/two-metric-seam` and see
  whether c9's branch survives.

GW polarisations are unaffected by the seam: the transverse block is `g̃ = A g`, so TT stays
TT (check 7). The seam moves GWs only through ordering (arrival time), consistent with F2.

## Even accounting

| item | status |
|---|---|
| gravity at the corner = E-M bending adjacency along ordering | retrodiction; Raychaudhuri, Jacobson |
| A0's chain is the timelike route, not gravity's requirement | internal re-reading |
| formula omits its patient (adjacency) | internal, F3-class |
| flow-free composition ⇒ trace-free gravity | prior art; classically equivalent to GR |
| Λ acts only on flow; "does Λ lens" malformed | retrodiction, mechanism shared (Butcher) |
| number fused into flow in c5; everpresent Λ as the inherited fork | flagged fork; Sorkin's prediction |
| **seam leaks content vacuum energy at O(B)** | **new to the corpus; could-fail on c9; computation owed** |
