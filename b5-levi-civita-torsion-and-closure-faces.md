# B5 — Levi-Civita, Torsion, and the Missing Closure Face

Status: consolidated B-note / internal audit / structural-bet and number-pipeline note.  
Grade: missing-cell audit against the gravity composition; upward correction to any parent curvature-form derivation that used torsion-free / first Bianchi; PB-1-grade structural-bet candidate for spin → torsion; quantitative-output procedure and neutron-star target table integrated; Levi-Civita remains correct in GR-owned contexts but torsion-free is not yet framework-forced; magnitude remains Einstein-Cartan / Poincaré-gauge / QG-priced and framework-disowned.

This note pulls the Levi-Civita / torsion question out of the parent framework. The target is narrow: the framework often treats non-integrability / loop-failure-to-close as the primitive geometric signal and then reads the GR import as curvature. But affine loop-failure-to-close has two structurally distinct faces: rotational holonomy and translational closure failure. Curvature is the rotational face. Torsion is the translational face. If the framework claims to compose the full non-integrable gravity mode, it must either force the torsion cell empty by role-reason or book torsion as a structural bet. Inheriting GR's torsion-free Levi-Civita connection as if it were forced is not allowed by the method.

Sharper correction: torsion-free is not merely the exclusion of an extra companion cell. If a parent derivation of curvature's algebraic form used torsion-free to obtain the first Bianchi identity, then demoting torsion-free also demotes that curvature-form derivation. The Riemann / Bianchi / rank-4 curvature package is forced only inside the Levi-Civita sector unless torsion-free is separately earned.

Quantitative correction: the torsion bet is not merely a prohibition. If independent spin current is retained, the framework routes the calculation to a torsion-sector equation and expects a number: a torsion tensor, torsion scale, effective correction term, or bound, externally priced by Einstein-Cartan / Poincaré-gauge dynamics. The framework does not derive the coupling; it specifies which number must be computed from which input.

## 1. Claim under audit

The parent framework imports the GR geometry through the Levi-Civita connection in ordinary GR contexts.

Levi-Civita means:

```text
metric-compatible
+
torsion-free
```

The framework has a plausible role-reason for the first condition:

```text
metric-compatibility:
  adjacency / separation comparison remains path-independent under parallel transport
```

But the second condition is not yet forced:

```text
torsion-free:
  translational closure-failure cell is empty
```

The audit question:

```text
Does the framework have a role-reason for torsion-free,
or has it silently inherited GR's choice as a proscription?
```

## 2. Two closure-failure faces

A loop can fail to close in two different affine senses.

```text
curvature:
  rotational holonomy
  transport a vector around a loop;
  it returns rotated

torsion:
  translational closure failure
  form an infinitesimal parallelogram;
  the two edge-orders miss by a gap
```

So the cleaner parent category is:

```text
affine non-integrability / loop-failure-to-close
```

with two faces:

```text
rotational closure failure:
  curvature

translational closure failure:
  torsion
```

The framework's existing curvature reading captures only the first face.

## 3. Why the old exclusion does not bite

A possible exclusion argument says:

```text
non-integrability is proportional to enclosed area;
it is second-order in loop size;
therefore no first-order torsion failure is allowed.
```

That does not separate curvature from torsion.

Torsion's infinitesimal parallelogram gap is also areal in loop size:

```text
closure gap ~ ε^2 T(A,B)
```

Curvature's rotation is also areal in loop size:

```text
rotation ~ ε^2 R(A,B)
```

The difference is not loop-size order. The difference is what fails:

```text
curvature:
  vector orientation fails to return

torsion:
  infinitesimal translation fails to close
```

The common phrase "second-order" can mislead. Torsion is algebraic in the connection coefficients while curvature involves derivatives and commutators of the connection, but both appear as area-order effects around an infinitesimal loop. Therefore an enclosed-area argument can fix the loop-size form, but it cannot exclude torsion.

## 4. Upward consequence: first Bianchi and curvature form

The torsion audit reaches upward into any parent derivation that used torsion-free to force curvature's algebraic form.

In a torsion-free Levi-Civita connection, the first Bianchi identity has the familiar form:

```text
R^a{}_[bcd] = 0
```

But with torsion live, the cyclic curvature identity acquires torsion terms schematically of the form:

```text
cyclic R = ∇T + T·T
```

So a derivation that says:

```text
(a) loop-pair antisymmetry
+
(b) rotation-pair antisymmetry from metric-compatibility
+
(c) first Bianchi from torsion-free
→ Riemann rank-4 / pair-exchange package
```

is not globally framework-forced. It is forced only inside the Levi-Civita / torsion-free sector.

Corrected status:

```text
curvature algebraic form:
  forced in the Levi-Civita sector
  conditional on torsion-free
  not forced for general metric-compatible affine geometry with torsion
```

Therefore B5 does two things:

```text
opens the torsion cell
and
downgrades curvature-form derivations that depended on torsion-free.
```

This does not invalidate GR-owned calculations. It prevents the framework from claiming it forced the full Levi-Civita curvature package before it has earned torsion-free by role-reason.

## 5. Metric-compatibility is not enough

Metric-compatibility does not imply torsion-free.

The general metric-compatible connection may be written schematically as:

```text
Γ = { } + K
```

where:

```text
{ }:
  Levi-Civita connection

K:
  contortion
```

and contortion carries torsion while preserving metric-compatibility when its index symmetries are appropriate.

So the framework may be able to force:

```text
∇g = 0
```

from adjacency / separation discipline, but it has not thereby forced:

```text
T^a{}_{bc} = 0
```

The torsion-free condition is an additional empty-cell claim.

## 6. Compose / missing / extra audit

If the parent object is full affine non-integrability, then the role inventory is:

```text
affine non-integrability:
  rotational closure failure
  translational closure failure
```

Mapped:

```text
rotational closure failure:
  curvature

translational closure failure:
  torsion
```

Current gravity composition mostly uses:

```text
gravity = ordering + influence + energy-momentum
```

and, geometrically, reads the non-integrable mode through curvature alone.

Audit:

```text
compose:
  curvature / rotational holonomy present

missing:
  torsion / translational closure-failure face not booked

extra:
  none yet, unless torsion is smuggled through GR omission as a prohibition
```

Therefore the current claim cannot be:

```text
curvature exhausts loop-failure-to-close
```

unless the torsion cell is explicitly graded forced-empty.

## 7. Attempted forced-empty route: adjacency is undirected

Option A needs a real attempt, not a placeholder. The obvious candidate is:

```text
adjacency = undirected separation / nextness
```

whereas torsion's defect is:

```text
directed translational closure gap
```

So one might argue:

```text
no directed-displacement role exists in the framework;
therefore the torsion cell is forced-empty.
```

This does not currently work.

Reason: adjacency itself is undirected as separation-magnitude, but the framework already gives adjacency a directed/conjugate face:

```text
momentum = adjacency-conjugate
space-momentum = directed spatial-translation face
```

A torsion gap is not a new scalar separation-magnitude. It is a failure of infinitesimal displacement composition: a directed translational residue. That has at least a candidate role-home in the adjacency/momentum sector.

So the internal fork is:

```text
forced-empty route:
  show directed translational residue cannot be represented by adjacency/momentum

missing-role route:
  directed translational residue is a missing aspect of the adjacency/momentum sector
```

Current verdict:

```text
Option A not established.
```

Undirected adjacency alone does not force torsion empty, because the conjugate momentum side already carries directed spatial translation. This makes the torsion cell live, but not forced true.

## 8. Forced-empty versus bet

The framework has two clean options.

### Option A — forced-empty

State a role-reason why the torsion cell is empty:

```text
spin / rotational current cannot enter the framework's gravity composition;
translational closure failure is forbidden by a role constraint;
adjacency/momentum cannot host directed translational residue;
therefore torsion-free is forced.
```

But this cannot merely be:

```text
GR does not include torsion.
```

By the parent method, reading a GR omission as a prohibition is a proscription. A proscription discharges as a bet, not a fact.

### Option B — structural bet

Book the missing companion:

```text
spin / rotational current → torsion / translational closure failure
```

Grade:

```text
PB-1-grade structural bet candidate
magnitude externally priced
standard extensions price the coupling
```

Option B preserves the framework's uniformity premise, but uniformity is itself the wager. So this supports booking a bet; it does not force the bet or make it more than PB-grade.

## 9. Native role map

Torsion should not remain only an external Einstein-Cartan vocabulary item. The framework has a native cell for it.

Curvature, in native language:

```text
curvature:
  rotational non-closure of frame / orientation transport
  curvature-sector non-integrability
  orientation returns changed
```

Torsion, in native language:

```text
torsion:
  translational non-closure of adjacency / momentum transport
  adjacency-translation-sector non-integrability
  displacement endpoint returns displaced
```

So the native framework statement is:

```text
curvature:
  non-integrability of orientation / frame transport

torsion:
  non-integrability of adjacency-translation / momentum-conjugate transport
```

This is the internal reason torsion is not merely an outside imposition. If the framework takes loop-failure-to-close seriously, the translational failure of the adjacency/momentum sector is a live missing face unless forced empty.

## 10. Structural pairing

In Einstein-Cartan / Poincaré-gauge gravity, two related pairings are present and must not be fused.

### 10.1 Noether / gauge-origin pairing

One kinematic/gauge-theoretic pairing is:

```text
translations:
  vierbein / coframe / solder form
  field-strength face: torsion
  current: energy-momentum

Lorentz rotations:
  spin connection
  field-strength face: curvature
  current: spin / angular momentum
```

This is the origin/grouping relation: translations own the coframe/torsion/energy-momentum family; Lorentz rotations own the spin-connection/curvature/spin family.

### 10.2 Source / field-equation pairing

A different source/equation pairing, in Einstein-Cartan-type formulations, is:

```text
energy-momentum:
  source in the curvature / metric field equation

spin / angular-momentum current:
  source in the torsion equation
```

This is the pairing the framework's structural bet uses.

Guardrail:

```text
The table groups by gauge/Noether origin.
The bet uses source/equation coupling.
They look crossed because they are different relations, not because one is wrong.
```

Also do not infer:

```text
spin's geometric home is torsion simpliciter
```

Careful statement:

```text
Spin's immediate mathematical home is Lorentz representation / spin-connection structure.
In EC/Poincaré-gauge completions, an independent spin current sources or activates torsion.
```

Different conventions distribute the currents and field strengths differently, and GR often Belinfante-symmetrizes spin into a symmetric stress-energy tensor. The framework does not own those technical choices.

Framework projection:

```text
energy-momentum → curvature-sector equation
spin / rotational current → torsion-sector equation
```

with magnitude externally priced.

## 11. Quantitative output: torsion burden

The torsion bet should produce a number when the input data exist. It is not just a prohibition.

The framework-owned routing is:

```text
independent spin current retained
→ torsion-sector equation live
→ torsion tensor / torsion scale / effective correction is computed
```

The externally owned pricing is schematic:

```text
Torsion ~ κ × spin density
```

or, more carefully:

```text
T^a{}_{bc} + trace terms = κ × spin-current^a{}_{bc}
```

where the exact index placement, trace convention, and coefficient are owned by the chosen Einstein-Cartan / Poincaré-gauge formulation. The framework owns the route, not the coefficient.

Algorithm:

```text
Input:
  connection assumption
  matter-current inventory
  spin density / spin current, if retained
  metric / frame / coframe choice
  external EC / Poincaré-gauge coupling convention

Step 1 — split the import:
  Levi-Civita = metric-compatible + torsion-free.

Step 2 — keep the forced part:
  if adjacency requires separation-magnitude preservation,
  retain metric-compatibility as role-forced or role-licensed.

Step 3 — test the empty cell:
  if torsion-free is asserted,
  require a role-reason that empties translational closure failure.

Step 4 — inspect matter current:
  if spin current is absent or Belinfante-absorbed,
  output GR-sector torsion burden = 0 in that description.

Step 5 — retain spin independently:
  if spin current survives as an independent matter current,
  route it to the torsion-sector equation.

Step 6 — compute externally:
  apply the selected EC / Poincaré-gauge field equation to obtain
  T^a{}_{bc}, axial torsion, contortion K, an effective four-fermion term,
  or a torsion scale/bound.

Step 7 — grade the result:
  cell/source routing = framework-owned structural bet;
  numeric value = externally priced;
  empirical accessibility = regime-dependent.
```

Outputs:

```text
LC-sector / spin-absorbed:
  torsion burden = 0 in the chosen GR-sector description

spin retained independently:
  torsion burden = EC-priced number from spin density

torsion-free claimed globally:
  forced-empty proof owed

curvature-form using first Bianchi:
  Levi-Civita-sector only unless torsion-free is earned
```

Positive prediction:

```text
In regimes with independent spin density, the first non-GR affine closure-failure correction
should scale with spin density through the torsion-sector equation, not with mass-energy
alone.
```

This is a number-generating claim:

```text
spin density in
→ torsion burden out
```

The magnitude is expected to be tiny in ordinary regimes because the imported gravitational coupling is tiny, but tiny is not zero-by-role. In extreme spin-density regimes, the torsion burden is the first place this framework would look for a positive, non-prohibitive divergence.

## 12. Experimental target: neutron-star torsion burden

The neutron-star worksheet is now part of B5, not a separate B5a document. Its role is to turn the torsion bet into an astrophysical number pipeline:

```text
independent spin / angular-momentum current
→ torsion-sector equation
→ torsion tensor / contortion / effective correction
→ neutron-star observable shift or bound
```

The first neutron-star target is not direct torsion measurement. It is a model-to-observable comparison.

```text
Input:
  mass M
  radius R
  spin frequency f or period P
  EOS / central density profile
  microphysical spin density and/or macroscopic angular momentum source
  chosen EC / Poincaré-gauge torsion equation

Output:
  ΔR
  ΔM_max
  Δρ_c
  ΔI
  ΔΛ
  spin-up / spin-down sign
  torsion scale or bound
```

### 12.1 Source-model split

The experimental audit must not blur two different source classes.

```text
A. Intrinsic-spin / minimal EC channel
   source: fermion spin density / independent spin current
   framework status: cleanest spin → torsion route
   current neutron-star status: hidden / negligible in realistic models so far

B. Rotation-induced / phenomenological torsion channel
   source: macroscopic angular momentum, rotation, or model-specific current
   framework status: useful positive number target, but not identical to minimal EC spin-density torsion
   current neutron-star status: potentially observable in some models, e.g. ΔR up to ~0.9 km
```

Why the split matters:

```text
The clean B5 bet is strongest for retained independent spin current.
The most observationally visible neutron-star number currently appears in a rotation-induced torsion channel.
```

So the audit must keep two questions separate:

```text
Minimal EC question:
  Does realistic intrinsic spin density produce a non-negligible torsion burden?

Rotation-induced question:
  Can a macroscopic-current torsion model improve or predict neutron-star observables?
```

The first is the cleaner framework lineage. The second is the better near-term observational target. Both are allowed external price paths, but they are not the same claim.

### 12.2 Observational anchors

| Anchor | Available data | Use in torsion worksheet |
|---|---:|---|
| PSR J0740+6620 mass | `M = 2.08 ± 0.07 M_sun` | High-mass support constraint; any torsion-modified EOS must still support about two solar masses. |
| PSR J0740+6620 radius | updated NICER/XMM result: `R_eq = 12.92^{+2.09}_{-1.13} km` at 68% credibility | First radius-shift target; compare predicted `ΔR` against current uncertainty. |
| PSR J0740+6620 spin | period about `2.89 ms` | Rotation input; not near breakup, but fast enough to test spin/rotation-correlated residuals. |
| PSR J0030+0451 radius/mass | NICER source near `M ~ 1.3–1.4 M_sun`, `R ~ 13 km` in 2019 analyses; later reanalyses emphasize model dependence | Lower-mass radius anchor; useful for mass-dependence versus spin-dependence separation. |
| GW170817 / BNS events | tidal deformability and EOS constraints; radius-sensitive through compactness | Tests whether torsion-induced `ΔR` implies allowed or excluded `ΔΛ`. |
| PSR J0952−0607 | mass estimate `M_NS = 2.35 ± 0.17 M_sun`; spin frequency about `707 Hz` | Extreme high-mass / high-spin candidate; mass modeling is less clean than Shapiro-delay systems, but important stress case. |

### 12.3 Direct torsion-model anchor

The currently most relevant direct paper is:

```text
Effect of Torsion on Neutron Star Structure in Einstein-Cartan Gravity
Jockel and Menger, 2024
arXiv:2406.05851
```

Its abstract-level results are directly usable as B5 targets:

```text
microphysical spin source:
  realistic spin models have no relevant influence on neutron-star structure

rotation-induced torsion source:
  can decrease radius by up to about 900 m
  can compete with centrifugal-radius increase
  can cause torsion-induced spin-up or spin-down depending on dominance
```

Framework read:

```text
microphysical spin row:
  current model says torsion burden hidden / negligible

rotation-induced row:
  possible positive observable, because ΔR ~ 0.9 km is near current/future radius precision
```

### 12.4 Working target table

| Object / event | Data now | Spin / current input | Torsion channel to price | Output number | First status |
|---|---:|---|---|---:|---|
| PSR J0740+6620 | `M = 2.08 ± 0.07 M_sun`; `R_eq = 12.92^{+2.09}_{-1.13} km`; `P ≈ 2.89 ms` | rotation; possible internal spin-density model | split: intrinsic-spin EC channel vs rotation-induced torsion channel | `ΔR`, `ΔI`, `ΔΛ`, sign of spin-up/down | Best first calibrated object; predicted `ΔR <= 0.9 km` is below but near current radius uncertainty. |
| PSR J0030+0451 | NICER mass/radius anchor around lower mass; radius inference model-dependent | rotation / spin state | same split as above | `ΔR(M,f)`, compare lower-mass response | Control object for mass-dependence; less clean due model dependence. |
| GW170817 | BNS tidal/EOS constraint | binary components' compactness, possible spin prior | torsion-modified mass-radius relation | `ΔΛ`, inferred `R_1.4` shift | Strong radius-sensitive population constraint; not direct torsion. |
| PSR J0952−0607 | `M_NS = 2.35 ± 0.17 M_sun`; `f ≈ 707 Hz` | high spin, high mass; model-dependent mass | high-spin stress test; likely rotation-induced channel first | `ΔR`, `ΔM_max`, possible spin-torsion residual | Interesting extreme case; not first calibration because radius is not NICER-clean. |
| Future moment-of-inertia measurement | expected from precision pulsar timing / double-pulsar programs | rotation + compactness | torsion-modified `I(M,R,f)` | `ΔI` | High value; moment of inertia may distinguish rotation/torsion corrections from EOS-only shifts. |

### 12.5 Calculation pipeline

For each selected neutron star or EOS family:

```text
1. Choose baseline GR / TOV model:
   EOS, M, R, ρ_c, I, Λ.

2. Choose torsion source model:
   intrinsic-spin / minimal EC channel
   or
   rotation-induced / phenomenological torsion channel.

3. Apply imported torsion pricing:
   EC / Poincaré-gauge torsion equation,
   or the Jockel-Menger effective correction model.

4. Compute corrections:
   ΔR
   ΔM_max
   Δρ_c
   ΔI
   ΔΛ
   spin-up/down sign.

5. Compare to data:
   NICER radius uncertainty,
   high-mass support constraints,
   GW tidal deformability,
   future moment-of-inertia constraints.

6. Grade:
   hidden: below current uncertainty
   testable: comparable to current/future uncertainty
   excluded: violates high-mass or radius/tidal constraints
   suggestive: residual scales with spin/current rather than mass-energy alone
```

Additional source-grade:

```text
intrinsic-spin result:
  cleaner B5 lineage
  likely hidden in current realistic neutron-star models

rotation-induced result:
  better near-term observable
  more model-dependent
```

### 12.6 Useful approximate sensitivity

Tidal deformability is highly radius-sensitive. Schematically:

```text
Λ ~ k_2 / C^5
C = GM/(Rc^2)
```

So, holding mass and Love-number changes aside for a first pass:

```text
ΔΛ / Λ ≈ 5 ΔR / R
```

For a neutron star with `R ~ 13 km`, a `ΔR ~ 0.9 km` shift is roughly:

```text
ΔR / R ~ 0.07
ΔΛ / Λ ~ 0.35
```

This is only a sensitivity estimate, not a prediction. The Love number, EOS response, and internal torsion-modified stellar structure must be recomputed in a real model. But it shows why a sub-kilometer torsion radius shift is not automatically observationally irrelevant.

### 12.7 First target: PSR J0740+6620

Use J0740 as the first worksheet object because it has:

```text
high mass from radio timing
NICER/XMM radius inference
known millisecond spin
strong EOS leverage
```

First comparison:

```text
observed radius uncertainty:
  +2.09 / -1.13 km at 68% credibility

model torsion shift from rotation-induced example:
  up to about -0.9 km
```

Interpretation:

```text
not currently a detection
not clearly excluded
near enough to radius precision to motivate a model-level comparison
```

First deliverable:

```text
Run both source paths across EOS families that already fit J0740 and GW170817:

  intrinsic-spin EC channel:
    expect hidden / negligible unless the spin-density model changes substantially

  rotation-induced torsion channel:
    test whether ΔR, ΔI, and ΔΛ remain allowed or improve fits

Ask whether adding a spin/rotation torsion channel improves, worsens, or is invisible
relative to the combined mass-radius-tidal data.
```

### 12.8 What would count as positive evidence?

Weak positive:

```text
a residual in mass-radius or moment-of-inertia fits correlates with spin / angular momentum
better than with mass-energy density alone.
```

Stronger positive:

```text
a torsion-sector correction predicts a sign and scale of ΔR or ΔI
that improves fit across fast and slow pulsars without spoiling GW tidal constraints.
```

Cleaner B5-positive signal:

```text
the same EOS family fits slow / low-spin objects normally,
but fast / high-spin objects require a correction,
and the correction's sign and scale match torsion-sector pricing.
```

Failure / weakening:

```text
all spin-current effects are fully absorbed into EOS / symmetric stress-energy modeling
with no independent torsion-sector burden;
```

or:

```text
observed spin-correlated residuals route through ordinary magnetic, thermal, crustal,
or EOS effects with no torsion/contortion improvement.
```

## 13. Rank-2 remainder and Belinfante warning

The parent four-momentum / stress-energy decomposition already contains a warning: the rank-2 remainder is not verified remainder-free.

This is adjacent to the torsion problem.

Careful statement:

```text
Spin current is not simply "the antisymmetric part of T_μν".
```

More precise:

```text
In torsion-free GR, spin can be absorbed into a symmetric stress-energy tensor
through Belinfante-Rosenfeld symmetrization.

In Einstein-Cartan-type formulations, spin density/current is kept as an independent
source associated with torsion.
```

So the framework's stress-energy remainder question and the torsion question are linked:

```text
remainder-free symmetric T_μν:
  torsion-free may remain a successful GR import

independent spin current retained:
  torsion cell is live and number-producing
```

The framework has not yet earned the first outcome by role-reason.

## 14. Wigner receipt

The parent framework cites Wigner's classification approvingly as role-individuation.

Wigner's massive-particle labels include:

```text
mass
spin
```

The framework has already cashed mass through the energy-momentum / flow-projection line.

Spin remains underbooked.

Careful statement:

```text
Spin's immediate mathematical home is representation / Lorentz structure.
In gravitational gauge completions such as Einstein-Cartan, its independent coupling home is torsion.
```

So Wigner does not prove torsion. But it flags that a role-catalogue which keeps mass and drops spin has likely not finished the audit.

## 15. Photon / write-act containment

This torsion audit does not automatically damage the photon or write-act sections.

A free photon does not source torsion in the usual Einstein-Cartan accounting. Its helicity/spin information is carried in the radiation field and can be absorbed into the symmetric stress-energy description used by GR.

Therefore:

```text
Levi-Civita polarization transport for the photon remains correct
inside the GR-owned, torsion-free context.
```

The problem is not:

```text
the photon section is wrong.
```

The problem is:

```text
the gravity composition has not yet shown that curvature exhausts
all affine closure-failure faces.
```

## 16. Prediction bundle

The framework should state the torsion prediction as a structural, number-generating bet with externally priced magnitude.

```text
1. Affine non-integrability splits into two faces:
   curvature = rotational holonomy;
   torsion = translational closure failure.

2. Metric-compatibility may be forced by adjacency,
   but torsion-free is not forced by metric-compatibility.

3. Parent curvature-form derivations that use torsion-free / first Bianchi
   are Levi-Civita-sector only.

4. Directed translational residue is not role-homeless by default;
   the adjacency/momentum sector is the candidate native home.

5. If spin / rotational current is retained as an independent matter current,
   torsion is the natural companion cell.

6. The structural bet is:
   spin / rotational current → torsion-sector equation.

7. The quantitative output is:
   spin density / spin current → torsion tensor, contortion, effective correction,
   torsion scale, or bound, externally priced by EC/Poincaré-gauge dynamics.

8. The correction should scale with spin density, not mass-energy density alone.

9. In ordinary regimes the number should be tiny; in extreme spin-density regimes,
   the torsion burden is the positive divergence to compute.

10. If torsion is absent, the framework owes a forced-empty role-reason,
    not merely GR inheritance.
```

Compact status:

```text
ε_torsion-forced-empty is not yet earned.
```

Positive number-producing bet:

```text
spin density in → torsion burden out
```

## 17. Could-have-failed

The torsion bet would fail or be forced-empty if:

```text
a role-reason shows translational closure failure cannot exist
under the framework's adjacency / ordering / influence / energy-momentum carve;
```

or if:

```text
adjacency/momentum cannot host directed translational residue;
```

or if:

```text
spin is shown to have no independent gravitational current status
under the framework's allowed imports;
```

or if:

```text
a complete decomposition of T_μν and the connection remainder shows no missing cell
without reading GR's torsion-free choice as a prohibition.
```

The quantitative bet would weaken if:

```text
all observable spin effects remain fully and non-residually Belinfante-absorbed
with no independent torsion-sector burden in every admissible completion;
```

or if:

```text
spin-density regimes demand corrections that do not route through translational closure failure,
contortion, axial torsion, or an EC/Poincaré-gauge torsion-sector equation.
```

The neutron-star target would weaken if:

```text
all spin/rotation-correlated residuals in neutron-star structure route through ordinary EOS,
magnetic, crustal, thermal, or rotation effects with no torsion/contortion improvement;
```

or if:

```text
the potentially visible rotation-induced channel cannot be cleanly connected to an admissible
torsion-sector source model.
```

The critique would strengthen if:

```text
future framework work keeps using loop-failure-to-close as primitive
while treating only curvature as the full non-integrable mode.
```

The upward correction would be avoided only if:

```text
the parent curvature-form derivation does not actually rely on torsion-free,
or torsion-free is separately forced-empty.
```

## 18. Grade

```text
Field taxonomy:
  convergent with standard differential-geometry distinction
  torsion is known external structure, not framework discovery

Internal audit:
  strong
  current torsion-free inheritance is not framework-forced unless a role-reason is supplied

Upward consequence:
  strong
  parent first-Bianchi / Riemann-form derivations that use torsion-free are Levi-Civita-sector only

Native role-home:
  candidate
  torsion = translational non-closure of adjacency/momentum transport
  not yet forced, but not role-homeless

Structural bet candidate:
  spin / rotational current → torsion-sector equation
  PB-1-grade companion-cell projection

Quantitative output:
  number-generating with external pricing
  spin density / spin current → torsion tensor, contortion, effective correction, torsion scale, or bound
  exact coupling and index form EC/Poincaré-gauge-owned

Neutron-star target:
  integrated as experimental number-pipeline
  intrinsic-spin channel is cleaner but likely hidden in current realistic models
  rotation-induced channel is more visible but more model-dependent

Levi-Civita import:
  remains correct for GR-owned torsion-free calculations
  not globally promoted to forced unless torsion cell is emptied

Collision-room:
  role-reason forcing torsion empty would close the gap
  adjacency/momentum unable to host directed translational residue would weaken the bet
  independent spin-current gravitational coupling favors torsion live
  treating GR omission as prohibition violates the method
```

## 19. Compact result

Levi-Civita is not one import. It is two claims:

```text
metric-compatible
+
torsion-free
```

The framework may have a role-reason for metric-compatibility. It does not yet have one for torsion-free.

The closure-failure cell splits:

```text
curvature:
  rotational holonomy

torsion:
  translational closure failure
```

The native role map is:

```text
curvature:
  non-integrability of orientation / frame transport

torsion:
  non-integrability of adjacency-translation / momentum-conjugate transport
```

Therefore the honest framework status is:

```text
torsion-free:
  unforced unless a role-reason empties the cell

curvature-form derivations using first Bianchi:
  Levi-Civita-sector only until torsion-free is earned

spin → torsion:
  structural bet candidate
  magnitude externally priced

spin density → torsion burden:
  positive quantitative output
  exact number owned by EC/Poincaré-gauge dynamics

neutron-star worksheet:
  folded into B5 as the first experimental target table
```

The photon/write-act Levi-Civita use can remain intact. The correction belongs at the gravity-composition level and at any parent curvature-form derivation that used torsion-free: curvature is not automatically the whole of affine non-integrability, and the Levi-Civita curvature package is not globally forced before torsion-free is earned.

The non-prohibitive output is the algorithmic number:

```text
independent spin current retained
→ compute the torsion burden
```

## References / external anchors

- Levi-Civita connection: metric-compatible and torsion-free connection of GR.
- Cartan / Einstein-Cartan theory: torsion coupled to spin density.
- Poincaré-gauge gravity: translation/Lorentz gauge structure, curvature and torsion field strengths.
- First Bianchi identity with torsion: cyclic curvature identity acquires ∇T and T·T terms.
- Belinfante-Rosenfeld symmetrization: relation between spin current and symmetric stress-energy in torsion-free descriptions.
- Wigner classification: mass and spin as representation labels.
- Jockel and Menger, `Effect of Torsion on Neutron Star Structure in Einstein-Cartan Gravity`, arXiv:2406.05851.
- Dittmann et al., `A More Precise Measurement of the Radius of PSR J0740+6620 Using Updated NICER Data`, arXiv:2406.14467.
- Riley et al., `A NICER View of the Massive Pulsar PSR J0740+6620 Informed by Radio Timing and XMM-Newton Spectroscopy`, arXiv:2105.06980.
- Riley et al., `A NICER View of PSR J0030+0451: Millisecond Pulsar Parameter Estimation`, arXiv:1912.05702.
- Romani et al., `PSR J0952−0607: The Fastest and Heaviest Known Galactic Neutron Star`, arXiv:2207.05124.
- Standard GW170817 / binary-neutron-star tidal-deformability and EOS literature.
- Standard differential geometry of affine connections, curvature, torsion, and contortion.
