# B5 — Levi-Civita, Torsion, and the Missing Closure Face

Status: working internal-audit / structural-bet note.  
Grade: missing-cell audit against the gravity composition; upward correction to any parent curvature-form derivation that used torsion-free / first Bianchi; PB-1-grade structural-bet candidate for spin → torsion; Levi-Civita remains correct in GR-owned contexts but torsion-free is not yet framework-forced; magnitude remains Einstein-Cartan / Poincaré-gauge / QG-priced and framework-disowned.

This note pulls the Levi-Civita / torsion question out of the parent framework. The target is narrow: the framework often treats non-integrability / loop-failure-to-close as the primitive geometric signal and then reads the GR import as curvature. But affine loop-failure-to-close has two structurally distinct faces: rotational holonomy and translational closure failure. Curvature is the rotational face. Torsion is the translational face. If the framework claims to compose the full non-integrable gravity mode, it must either force the torsion cell empty by role-reason or book torsion as a structural bet. Inheriting GR's torsion-free Levi-Civita connection as if it were forced is not allowed by the method.

Sharper correction: torsion-free is not merely the exclusion of an extra companion cell. If a parent derivation of curvature's algebraic form used torsion-free to obtain the first Bianchi identity, then demoting torsion-free also demotes that curvature-form derivation. The Riemann / Bianchi / rank-4 curvature package is forced only inside the Levi-Civita sector unless torsion-free is separately earned.

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
magnitude disowned
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

with magnitude disowned.

## 11. Rank-2 remainder and Belinfante warning

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

## 12. Wigner receipt

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

## 13. Photon / write-act containment

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

## 14. Prediction bundle

The framework should state the torsion prediction as a structural bet, not a magnitude claim.

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

7. Magnitude is externally priced and likely tiny in ordinary regimes;
   the framework does not derive the coupling strength.

8. If torsion is absent, the framework owes a forced-empty role-reason,
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

## 15. Could-have-failed

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

## 16. Grade

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
  magnitude disowned

Levi-Civita import:
  remains correct for GR-owned torsion-free calculations
  not globally promoted to forced unless torsion cell is emptied

Collision-room:
  role-reason forcing torsion empty would close the gap
  adjacency/momentum unable to host directed translational residue would weaken the bet
  independent spin-current gravitational coupling favors torsion live
  treating GR omission as prohibition violates the method
```

## 17. Compact result

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
```

The photon/write-act Levi-Civita use can remain intact. The correction belongs at the gravity-composition level and at any parent curvature-form derivation that used torsion-free: curvature is not automatically the whole of affine non-integrability, and the Levi-Civita curvature package is not globally forced before torsion-free is earned.

## References / external anchors

- Levi-Civita connection: metric-compatible and torsion-free connection of GR.
- Cartan / Einstein-Cartan theory: torsion coupled to spin density.
- Poincaré-gauge gravity: translation/Lorentz gauge structure, curvature and torsion field strengths.
- First Bianchi identity with torsion: cyclic curvature identity acquires ∇T and T·T terms.
- Belinfante-Rosenfeld symmetrization: relation between spin current and symmetric stress-energy in torsion-free descriptions.
- Wigner classification: mass and spin as representation labels.
- Standard differential geometry of affine connections, curvature, torsion, and contortion.
