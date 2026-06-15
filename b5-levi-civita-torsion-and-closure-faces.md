# B5 — Levi-Civita, Torsion, and the Missing Closure Face

Status: working internal-audit / structural-bet note.  
Grade: missing-cell audit against the gravity composition; PB-1-grade structural-bet candidate for spin → torsion; Levi-Civita remains correct in GR-owned contexts but torsion-free is not yet framework-forced; magnitude remains Einstein-Cartan / Poincaré-gauge / QG-priced and framework-disowned.

This note pulls the Levi-Civita / torsion question out of the parent framework. The target is narrow: the framework often treats non-integrability / loop-failure-to-close as the primitive geometric signal and then reads the GR import as curvature. But affine loop-failure-to-close has two structurally distinct faces: rotational holonomy and translational closure failure. Curvature is the rotational face. Torsion is the translational face. If the framework claims to compose the full non-integrable gravity mode, it must either force the torsion cell empty by role-reason or book torsion as a structural bet. Inheriting GR's torsion-free Levi-Civita connection as if it were forced is not allowed by the method.

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

## 4. Metric-compatibility is not enough

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

## 5. Compose / missing / extra audit

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

## 6. Forced-empty versus bet

The framework has two clean options.

### Option A — forced-empty

State a role-reason why the torsion cell is empty:

```text
spin / rotational current cannot enter the framework's gravity composition;
translational closure failure is forbidden by a role constraint;
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
magnitude disowned
standard extensions price the coupling
```

This option is more natural because it preserves the framework's uniformity move: the geometry cell already has companion closure-failure faces, and torsion is the obvious dual to curvature under affine closure failure.

## 7. Structural pairing

In Einstein-Cartan / Poincaré-gauge gravity, two related pairings are present and must not be fused.

### 7.1 Gauge-field-strength pairing

One kinematic/gauge-theoretic pairing is:

```text
translation gauge structure:
  coframe / solder form
  field-strength face: torsion

Lorentz rotation gauge structure:
  spin connection
  field-strength face: curvature
```

This is a gauge-geometry pairing. It says which field strengths correspond to which gauge structures.

### 7.2 Source / field-equation pairing

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
Do not infer "spin's geometric home is torsion" simpliciter.
Spin's immediate mathematical home is Lorentz representation / spin-connection structure.
In EC/Poincaré-gauge completions, an independent spin current sources or activates torsion.
```

Different conventions distribute the currents and field strengths differently, and GR often Belinfante-symmetrizes spin into a symmetric stress-energy tensor. The framework does not own those technical choices.

The structural lesson is narrower:

```text
energy-momentum is not the whole matter-current story once spin is kept independent.
spin is the missing rotational current.
torsion is the corresponding translational closure-failure face in EC/Poincaré-gauge completions.
```

Framework projection:

```text
energy-momentum → curvature-sector equation
spin / rotational current → torsion-sector equation
```

with magnitude disowned.

## 8. Rank-2 remainder and Belinfante warning

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
  torsion cell is live
```

The framework has not yet earned the first outcome by role-reason.

## 9. Wigner receipt

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

## 10. Photon / write-act containment

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

## 11. Prediction bundle

The framework should state the torsion prediction as a structural bet, not a magnitude claim.

```text
1. Affine non-integrability splits into two faces:
   curvature = rotational holonomy;
   torsion = translational closure failure.

2. Metric-compatibility may be forced by adjacency,
   but torsion-free is not forced by metric-compatibility.

3. If spin / rotational current is retained as an independent matter current,
   torsion is the natural companion cell.

4. The structural bet is:
   spin / rotational current → torsion-sector equation.

5. Magnitude is externally priced and likely tiny in ordinary regimes;
   the framework does not derive the coupling strength.

6. If torsion is absent, the framework owes a forced-empty role-reason,
   not merely GR inheritance.
```

Compact null/positive form:

```text
ε_torsion-forced-empty is not yet earned.
```

or, as a bet:

```text
spin → torsion
```

## 12. Could-have-failed

The torsion bet would fail or be forced-empty if:

```text
a role-reason shows translational closure failure cannot exist
under the framework's adjacency / ordering / influence / energy-momentum carve;
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

The critique would strengthen if:

```text
future framework work keeps using loop-failure-to-close as primitive
while treating only curvature as the full non-integrable mode.
```

## 13. Grade

```text
Field taxonomy:
  convergent with standard differential-geometry distinction
  torsion is known external structure, not framework discovery

Internal audit:
  strong
  current torsion-free inheritance is not framework-forced unless a role-reason is supplied

Structural bet candidate:
  spin / rotational current → torsion-sector equation
  PB-1-grade companion-cell projection
  magnitude disowned

Levi-Civita import:
  remains correct for GR-owned torsion-free calculations
  not globally promoted to forced unless torsion cell is emptied

Collision-room:
  role-reason forcing torsion empty would close the gap
  independent spin-current gravitational coupling favors torsion live
  treating GR omission as prohibition violates the method
```

## 14. Compact result

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

Therefore the honest framework status is:

```text
torsion-free:
  unforced unless a role-reason empties the cell

spin → torsion:
  structural bet candidate
  magnitude externally priced
```

The photon/write-act Levi-Civita use can remain intact. The correction belongs at the gravity-composition level: curvature is not automatically the whole of affine non-integrability.

## References / external anchors

- Levi-Civita connection: metric-compatible and torsion-free connection of GR.
- Cartan / Einstein-Cartan theory: torsion coupled to spin density.
- Poincaré-gauge gravity: translation/Lorentz gauge structure, curvature and torsion field strengths.
- Belinfante-Rosenfeld symmetrization: relation between spin current and symmetric stress-energy in torsion-free descriptions.
- Wigner classification: mass and spin as representation labels.
- Standard differential geometry of affine connections, curvature, torsion, and contortion.
