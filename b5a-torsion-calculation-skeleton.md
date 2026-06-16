# B5a — Torsion Calculation Skeleton

*Working draft, June 2026.*

Status: companion calculation note for B5.  
Primary target: B5 torsion audit and A2 computational-handle discipline.  
Grade: imported-computation skeleton / route clarification. Not a new torsion dynamics.

B5 established the structural point:

```text
curvature = rotational closure failure
torsion = translational closure failure
```

B5a asks the next question:

```text
If the torsion cell is live, what is the smallest honest computation?
```

Answer:

```text
spin/current source retained
→ imported torsion-sector equation
→ torsion tensor
→ contortion
→ torsion-live connection
→ transport correction / observable bound
```

The framework owns the route if the role decomposition is clean. The dynamics, coefficients, conventions, and observations remain imported or calibrated.

---

## 1. Kinematic split

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
K ~ 1/2 · (T + index-permuted T terms)
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

---

## 2. Loop split

For a small loop with area bivector `A^{bc}`:

```text
rotational closure failure:
  δV^a ~ R^a{}_{bcd} V^b A^{cd}

translational closure failure:
  δx^a ~ T^a{}_{bc} A^{bc}
```

This is the clean computational distinction.

```text
R prices orientation failure.
T prices endpoint failure.
```

If MGR names loop-failure-to-close as a primitive diagnostic, both prices must either be paid or one must be forced empty.

---

## 3. Source route

In Einstein-Cartan / Poincare-gauge-style completions, the torsion equation is algebraic or constraint-like in the simplest cases:

```text
T + trace terms = κ · spin-current
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

MGR owns:

```text
spin-current retained independently
→ torsion-sector equation live
```

It does not own:

```text
κ;
trace convention;
index convention;
choice of EC / Poincare-gauge action;
whether the physical source model is correct.
```

---

## 4. Minimal computation recipe

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
    T + trace terms = κ · s.

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

---

## 5. Zero and tiny-number discipline

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

This prevents both overclaim and underclaim.

---

## 6. Method ledger

Imported handles:

```text
Γ = { } + K
T^a{}_{bc} = 2 Γ^a{}_[bc]
R-loop holonomy
T-loop closure gap
EC / Poincare-gauge torsion-sector equation
compact-object model / EOS / observational inference
```

Framework-owned if earned:

```text
role-route:
  spin/current retained independently → torsion-sector equation live

missing-cell diagnosis:
  curvature does not automatically exhaust affine closure failure

output slot:
  torsion burden / contortion correction / transport correction / bound
```

Externally priced:

```text
coefficient;
trace convention;
index placement;
source model;
field equation;
observable number.
```

One-line form:

```text
B5a turns the torsion cell from a missing-role warning into an externally priced calculation route.
```