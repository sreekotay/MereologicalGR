# B5 — Levi-Civita, Torsion, and the Missing Closure Face

*Working draft, June 2026.*

Status: B-note / internal audit / number-pipeline note.
Primary target: A2 gravity composition and curvature-form derivations that silently use torsion-free Levi-Civita structure; A0 corner discipline and compose / missing / extra audit; diagnostic-ledger D9 (archived sensitivity lane).
Grade: missing-cell audit + structural-bet candidate. GR is held fixed; numerical workbench: `archive/b5-torsion-experimental/`.

B5's claim is simple:

```text
curvature is rotational closure failure;
torsion is translational closure failure.
```

If MGR treats loop-failure-to-close as a primitive geometric signal, it cannot silently keep only curvature and inherit torsion-free as if GR's silence were prohibition. It must either force the torsion cell empty by role-reason or book torsion as a live structural bet.

This is a corner in A0's sense: GR remains predictively complete while one closure cell is set empty. The instructive question is whether that cell was priced or merely inherited.

Positive output:

```text
independent spin current retained
→ torsion-sector equation live
→ torsion tensor
→ contortion
→ torsion-live connection
→ transport correction / observable bound
```

Calibration is not failure. Fitting is failure. A scalar may be observed; a structure must be earned.

---

## 1. Two ways a loop can fail to close

A loop can fail to close in two affine senses.

```text
curvature:
  rotational holonomy;
  transport a vector around a loop;
  it returns rotated.

torsion:
  translational closure failure;
  form an infinitesimal parallelogram;
  the two edge-orders miss by a displacement.
```

Parent category:

```text
affine non-integrability / loop-failure-to-close
```

Two faces:

```text
rotational closure failure:
  curvature

translational closure failure:
  torsion
```

So curvature is not automatically the whole non-integrable mode. It is one face of it.

---

## 2. Levi-Civita is two claims, not one

The standard GR connection is Levi-Civita:

```text
Levi-Civita = metric-compatible + torsion-free
```

MGR has a plausible role-reason for metric-compatibility:

```text
metric-compatibility:
  adjacency / separation comparison remains coherent under transport
```

But metric-compatibility does not imply torsion-free. A general metric-compatible connection may be written schematically:

```text
Γ = { } + K
```

where `{ }` is Levi-Civita and `K` is contortion. Contortion carries torsion while preserving metric-compatibility when its index symmetries are appropriate.

So the framework may license:

```text
∇g = 0
```

without yet licensing:

```text
T^a{}_{bc} = 0
```

Torsion-free is an extra empty-cell claim. It needs a role-reason.

---

## 3. The old exclusion does not work

A tempting exclusion says:

```text
non-integrability is proportional to enclosed area;
it is second-order in loop size;
therefore no first-order torsion failure is allowed.
```

That does not separate curvature from torsion.

Both effects appear at area order around an infinitesimal loop:

```text
curvature rotation ~ eps^2 R(A,B)
torsion gap       ~ eps^2 T(A,B)
```

The difference is not loop-size order. The difference is what fails:

```text
curvature:
  orientation fails to return

torsion:
  displacement composition fails to close
```

So an enclosed-area argument can fix the loop-size form, but it cannot exclude torsion.

---

## 4. Why torsion is not role-homeless

One possible forced-empty route says:

```text
adjacency is undirected separation;
torsion is directed translational residue;
therefore no role can host torsion.
```

This is not established.

Adjacency has a directed/conjugate face:

```text
momentum = adjacency-conjugate
space-momentum = directed spatial-translation face
```

A torsion gap is not a new scalar separation-magnitude. It is a failure of infinitesimal displacement composition: a directed translational residue. That has a candidate home in the adjacency/momentum sector.

Live fork:

```text
forced-empty route:
  show directed translational residue cannot be represented by adjacency/momentum

missing-cell route:
  treat directed translational residue as a missing face of adjacency/momentum transport
```

Current verdict:

```text
torsion-free is not yet role-forced.
```

---

## 5. Upward consequence: Bianchi and curvature form

The torsion audit reaches upward into any curvature-form derivation that used torsion-free.

In a torsion-free Levi-Civita connection, the first Bianchi identity has the familiar form:

```text
R^a{}_[bcd] = 0
```

With torsion live, the cyclic identity acquires torsion terms schematically:

```text
cyclic R = covariant-derivative-of-T + T*T
```

Therefore a derivation that uses:

```text
loop-pair antisymmetry
+ rotation-pair antisymmetry from metric-compatibility
+ first Bianchi from torsion-free
→ Riemann rank-4 / pair-exchange package
```

is not globally framework-forced. It is forced only inside the Levi-Civita / torsion-free sector unless torsion-free is separately earned.

This does not invalidate GR-owned calculations. It prevents MGR from claiming it forced the full Levi-Civita curvature package before it has emptied the torsion cell.

---

## 6. Native role map

Curvature in native language:

```text
curvature:
  rotational non-closure of frame / orientation transport;
  non-integrability of orientation / frame transport.
```

Torsion in native language:

```text
torsion:
  translational non-closure of adjacency / momentum transport;
  non-integrability of adjacency-translation / momentum-conjugate transport.
```

Native framework map:

```text
curvature:
  orientation transport fails to return

torsion:
  displacement transport fails to close
```

If the framework takes loop-failure-to-close seriously, the translational failure of the adjacency/momentum sector is live unless forced empty.

---

## 7. Spin current and the torsion-sector equation

In Einstein-Cartan / Poincare-gauge-style completions, two relations must not be fused.

Gauge / origin grouping:

```text
translations:
  coframe / solder form;
  field-strength face: torsion;
  current: energy-momentum.

Lorentz rotations:
  spin connection;
  field-strength face: curvature;
  current: spin / angular momentum.
```

Source / field-equation pairing:

```text
energy-momentum:
  source in the curvature / metric equation

spin / angular-momentum current:
  source in the torsion equation
```

The tables look crossed because they are different relations.

Careful statement:

```text
Spin's immediate mathematical home is Lorentz representation / spin-connection structure.
In EC/Poincare-gauge completions, an independent spin current sources or activates torsion.
```

MGR does not derive the coupling. It fixes only the route:

```text
energy-momentum → curvature-sector equation
spin / rotational current → torsion-sector equation
```

with magnitude externally priced.

---

## 8. Number pipeline: torsion burden

The torsion bet is not just a prohibition. If independent spin current is retained, it produces a number.

Framework-owned routing:

```text
independent spin current retained
→ torsion-sector equation live
→ torsion tensor / contortion / effective correction / bound computed
```

Externally priced schematic form:

```text
Torsion ~ kappa * spin density
```

or, more carefully:

```text
T^a{}_{bc} + trace terms = kappa * spin-current^a{}_{bc}
```

The exact index placement, trace convention, and coefficient are supplied by the chosen EC / Poincare-gauge formulation. MGR fixes the source-route, not the coefficient.

Algorithm:

```text
1. Split the import:
   Levi-Civita = metric-compatible + torsion-free.

2. Retain what role-reason licenses:
   metric-compatibility may be licensed by adjacency / separation comparison.

3. Test the empty cell:
   if torsion-free is asserted, require a role-reason that empties translational closure failure.

4. Inspect matter currents:
   if spin current is absent or Belinfante-absorbed, output GR-sector torsion burden = 0 in that description.

5. Retain spin independently:
   if spin current survives as an independent matter current, route it to the torsion-sector equation.

6. Compute externally:
   apply the selected EC / Poincare-gauge field equation to obtain torsion, contortion,
   an effective correction, or a bound.

7. Grade the result:
   route = MGR-claimed;
   numeric value = externally priced / calibrated;
   empirical accessibility = regime-dependent.
```

Positive number-producing bet:

```text
spin density in → torsion burden out
```

The correction should scale with spin/current, not mass-energy density alone. Tiny is not zero-by-role. In extreme spin-density regimes, the torsion burden is the first non-GR affine closure-failure correction this framework should price.

---

## 9. Computational handles

The closure-failure reading is useful only if it points to real differential-geometric handles. B5 therefore keeps the handles imported, and states only what role they expose.

```text
Levi-Civita split:
  imported handle: Γ^a{}_{bc} = {^a{}_{bc}} in the torsion-free GR sector
  role exposed: metric-compatible comparison / transport with torsion cell set empty;
  computes: standard GR parallel transport, geodesics, curvature, holonomy;
  not derived: torsion-free as a role-forced condition.

curvature / holonomy:
  imported handle: ΔV^μ ~ R^μ{}_{νρσ} V^ν A^{ρσ}
  role exposed: rotational closure failure / loop frame-transport;
  computes: orientation change after infinitesimal loop transport;
  not derived: translational closure failure is absent.

first Bianchi identity:
  imported handle: R^a{}_[bcd] = 0 in the torsion-free Levi-Civita sector
  role exposed: algebraic closure of the rotational curvature package;
  computes: familiar Riemann symmetry / curvature-form constraints;
  not derived: the same identity in a torsion-live affine geometry.

torsion / closure gap:
  imported handle: gap ~ T(A,B)
  role exposed: translational closure failure / adjacency-translation residue;
  computes: infinitesimal endpoint displacement from non-closing parallelogram;
  not derived: torsion is physically nonzero.

contortion split:
  imported handle: Γ = { } + K
  role exposed: metric-compatible transport can retain torsion through contortion;
  computes: how a torsion-live connection departs from Levi-Civita;
  not derived: which K is realized in nature.

spin-current torsion equation:
  imported handle: T^a{}_{bc} + trace terms = kappa * spin-current^a{}_{bc}
  role exposed: independent spin current routes to torsion-sector equation;
  computes: torsion tensor, axial torsion, contortion, effective correction, or bound;
  not derived: kappa, index convention, trace convention, or EC/Poincare-gauge dynamics.

neutron-star torsion burden:
  imported handle: selected EC / Poincare-gauge stellar model or effective torsion correction
  role exposed: spin/current-correlated torsion burden in a compact-object regime;
  computes: delta R, delta M_max, delta rho_c, delta I, delta Lambda, spin response sign, or bound;
  not derived: EOS, observational inference, or source-model correctness.
```

Method reading:

```text
The handle is imported.
The role-location is MGR-claimed if the decomposition is clean.
The scalar or tensor value is computed by the imported formalism.
A new MGR claim appears only where the role-route forces a missing/extra diagnosis.
```

The concrete payoff is a sharper map of which existing geometric formula prices which closure face:

```text
metric-compatible transport:
  Levi-Civita sector

loop frame-transport:
  curvature / holonomy

algebraic curvature closure:
  first Bianchi, torsion-free only

translational closure failure:
  torsion / closure gap

metric-compatible torsion-live transport:
  contortion K

spin-current pricing:
  EC / Poincare-gauge torsion-sector equation
```

---

## 10. Minimal torsion calculation skeleton

The handles above locate formulas. The next step is a calculation skeleton: the smallest sequence that turns the missing torsion cell into a priced correction or bound.

Nothing in this section is a new MGR dynamics. The dynamics are imported. The MGR-claimed part is the route and the missing/extra diagnosis.

### 10.1 Kinematic split

Start with the affine data:

```text
connection:
  Γ^a{}_{bc}

torsion:
  T^a{}_{bc} = 2 Γ^a{}_[bc]

Levi-Civita part:
  {^a{}_{bc}}

contortion:
  K^a{}_{bc}
```

Metric-compatible torsion-live transport can be written schematically:

```text
Γ^a{}_{bc} = {^a{}_{bc}} + K^a{}_{bc}
```

with `K` algebraically determined by torsion once the convention is fixed. A common convention has the form:

```text
K ~ 1/2 * (T + index-permuted T terms)
```

The exact signs and index positions are imported from the chosen formalism.

Role reading:

```text
{ }:
  metric-compatible torsion-free comparison / transport

K:
  torsion-live correction to the transport rule

T:
  translational closure-failure tensor
```

### 10.2 Loop split

For a small loop with area bivector `A^{bc}`:

```text
rotational closure failure:
  delta V^a ~ R^a{}_{bcd} V^b A^{cd}

translational closure failure:
  delta x^a ~ T^a{}_{bc} A^{bc}
```

This is the clean computational distinction.

```text
R prices orientation failure (rotational holonomy; A2 ΔV ~ R face).
T prices endpoint failure (translational holonomy; adjacency-transport gap).
```

If MGR names loop-failure-to-close as a primitive diagnostic, both prices must either be paid or one must be forced empty. A2's frame-transport handles price the rotational face; B5 prices the translational face the Levi-Civita sector sets to zero.

### 10.3 Source route

In EC/Poincare-gauge-style completions, the torsion equation is algebraic or constraint-like in the simplest cases:

```text
T + trace terms = kappa * spin-current
```

Schematic source route:

```text
spin current in
→ solve torsion-sector equation
→ T
→ K
→ corrected connection Γ = { } + K
→ modified transport / effective stress / observable shift
```

MGR fixes:

```text
spin-current retained independently
→ torsion-sector equation live
```

It does not own:

```text
kappa;
trace convention;
index convention;
choice of EC / Poincare-gauge action;
whether the physical source model is correct.
```

### 10.4 Computation recipe

A minimal torsion-burden computation has this form:

```text
Input:
  metric / tetrad or baseline GR solution;
  matter model;
  decision whether spin current is Belinfante-absorbed or retained independently;
  chosen torsion-sector equation.

Step 1:
  compute or model independent spin-current s.

Step 2:
  solve imported torsion equation:
    T + trace terms = kappa * s.

Step 3:
  compute contortion:
    K = K(T).

Step 4:
  form torsion-live connection:
    Γ = { } + K.

Step 5:
  compute transport consequences:
    geodesic/autoparallel shift;
    curvature correction;
    effective stress-energy correction;
    spin-correlated radius / mass / moment-of-inertia / tidal-response shift.

Step 6:
  compare to data or bound:
    hidden;
    testable;
    excluded;
    suggestive.
```

The framework-positive output is not:

```text
any deviation from GR
```

but:

```text
spin/current-routed torsion burden
not absorbed by ordinary GR + matter modeling.
```

### 10.5 Zero and tiny-number discipline

A zero or tiny torsion burden in a model is not automatically a refutation of the missing-cell audit.

```text
zero because spin current is absent / absorbed:
  GR-sector description successful for that source model

zero because role-reason forbids translational closure failure:
  torsion-free forced, cell closed

tiny because realistic spin density is small or cancels:
  live cell, hidden number

nonzero and spin/current-correlated:
  positive number-producing target
```

This keeps the audit from treating tiny as empty or residual as victory.

---

## 11. Application workbook (archived numerics)

Compact objects are the first sensitivity arena: high density, spin, EOS leverage, mass/radius/tidal constraints. **Canonical B5 stops at the route; numbers live in the workbench.**

Two source channels must not be fused:

```text
A. Intrinsic-spin / minimal EC:
   fermion spin density → independent spin current → torsion equation
   lineage: cleanest B5 route
   realistic NS status: usually hidden / negligible

B. Rotation-induced / phenomenological:
   macroscopic rotation or model-specific current → effective torsion
   lineage: externally priced; not identical to A
   near-term status: model-dependent shifts (e.g. sub-km radius in some EC models)
```

Channel A is the structural bet. Channel B is a **sensitivity probe only** — useful for bounds, not for top-level project identity.

Workbench pipeline (detail, anchors, gates, Jockel–Menger readouts):

```text
archive/b5-torsion-experimental/
```

Applied routing when fitting residuals:

```text
spin/current-correlated residual → price through torsion-sector route first
not absorbed by EOS / symmetric T_mu_nu / magnetic / crust alone
```

**Positive evidence (B5-positive, not generic GR deviation):**

```text
same EOS fits slow/low-spin objects;
fast/high-spin objects need a correction;
correction sign/scale matches torsion-sector pricing, not mass-energy density alone.
```

**Failure / weakening:** all spin/current effects absorbed by ordinary GR+matter modeling; or residuals route through magnetic/thermal/crust/EOS with no torsion improvement. **Null tightens bounds; it does not force torsion empty** — forced-empty still needs a role-level closure proof.

Promotion from archive to top-level requires: stable source data, fixed role-route before fitting, and clear demotion/failure conditions (diagnostic-ledger D9 discipline).

---

## 12. Belinfante and Wigner guardrails

Spin current is not simply:

```text
the antisymmetric part of T_mu_nu
```

In torsion-free GR, spin can be absorbed into a symmetric stress-energy tensor through Belinfante-Rosenfeld symmetrization. In Einstein-Cartan-type formulations, spin density/current is kept as an independent source associated with torsion.

So the stress-energy remainder question and the torsion question are linked:

```text
remainder-free symmetric T_mu_nu:
  torsion-free may remain a successful GR import

independent spin current retained:
  torsion cell is live and number-producing
```

Wigner does not prove torsion. But Wigner's massive-particle labels include mass and spin. The framework has already cashed mass through the energy-momentum / flow-projection line. Spin remains underbooked. A role-catalogue that keeps mass and drops spin has likely not finished the audit.

---

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

---

## 14. Ledger

Derived / MGR-claimed:

```text
1. closure-failure splits into rotational and translational faces;
2. curvature is rotational closure failure;
3. torsion is translational closure failure;
4. metric-compatibility does not imply torsion-free;
5. curvature-form derivations using first Bianchi are Levi-Civita-sector only;
6. directed translational residue has a candidate home in the adjacency/momentum sector;
7. if spin current is retained independently, the torsion-sector equation is the native route;
8. computational handles map existing geometry to closure-face roles without deriving the dynamics;
9. minimal torsion calculation skeleton turns the live cell into an externally priced correction or bound.
```

Calibrated / externally priced:

```text
EC / Poincare-gauge coupling;
index and trace conventions;
torsion tensor / contortion magnitude;
effective correction terms;
neutron-star observable shifts;
bounds from mass-radius-tidal data.
```

Imported / not derived:

```text
Levi-Civita connection;
Riemann curvature and holonomy formulas;
Einstein-Cartan or Poincare-gauge field equations;
spin-current dynamics;
EOS and neutron-star microphysics;
observational mass/radius/tidal inference;
full QG completion.
```

Demotion / failure conditions:

```text
a role-reason shows translational closure failure cannot exist under the framework carve;
adjacency/momentum cannot host directed translational residue;
spin has no independent gravitational current status under allowed imports;
complete stress-energy / connection decomposition shows no missing cell without treating GR omission as prohibition;
all spin/current residuals route through ordinary GR+matter modeling with no torsion improvement.
```

Standing result:

```text
Levi-Civita is not one import. It is metric-compatibility plus torsion-free.
Metric-compatibility may be role-licensed. Torsion-free is not yet forced.
```

Positive output:

```text
independent spin current retained
→ compute the torsion burden
```

One-line form:

```text
Curvature is not automatically the whole of affine non-integrability;
torsion is the missing translational closure face unless MGR earns torsion-free.
```
