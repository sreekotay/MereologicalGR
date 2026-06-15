# B10 — Positive Energy and the Vacuum Condition

*Working draft, June 2026.*

Status: B-note / hard-gate audit.  
Primary target: B9 positive-frequency boundary, B8 scalar kernel, B7 scalar response, A0 energy-momentum / flow grammar.  
Grade: locating result + conditional derivation. Not a derivation of the quantum vacuum.

Core question:

```text
Can the positive-energy vacuum condition be derived from
flow + energy-momentum + no-extra/no-missing,
or must it remain imported?
```

Run result:

```text
MGR / GR can earn:
  local positive-energy orientation relative to future-directed flow;
  positive frequency as energy aligned with future flow;
  the need for a stability floor if detector response is to be well-defined;
  the fact that negative-frequency-as-independent-content would be extra/double-counted.

MGR / GR cannot yet earn:
  a unique vacuum state;
  Hilbert-space spectral positivity;
  global ground-state selection;
  Fock-space particle/no-particle split;
  Wightman two-point sampling as a state rule.
```

So the boundary after B9 sharpens to:

```text
GR / MGR-owned:
  future-flow energy orientation

conditional import:
  stable lower-bound / ground-state condition

QFT-owned:
  vacuum state and Wightman sampling rule
```

---

## 1. What B9 left open

B9 reached:

```text
positive-frequency = future-flow-compatible energy orientation
```

but stopped at the vacuum/state prescription:

```text
not yet derived:
  stable positive-energy vacuum;
  spectral positivity;
  Wightman iε as state boundary condition;
  detector two-point sampling rule.
```

B10 asks whether the stability/vacuum piece can be forced from the already imported energy-momentum primitive and flow.

---

## 2. Local positive energy is GR/SR-owned

For a flow-bearing observer/worldline with four-velocity `u`, the locally rendered energy of a momentum `p` is:

```text
E(u,p) = -p · u
```

where the sign convention assumes metric signature `(-,+,+,+)` and future-directed `u`.

If `p` is future-directed causal and `u` is future-directed timelike, then:

```text
E(u,p) > 0
```

for nonzero physical `p`.

MGR reading:

```text
flow:
  future-directed proper-time accrual

energy-momentum:
  imported dimensionful primitive

energy:
  flow-conjugate rendering of energy-momentum

positive energy:
  energy-momentum aligned with future-directed flow
```

This is a real local result. It does not use QFT.

---

## 3. Frequency orientation follows locally

A scalar mode sampled along the flow-worldline has the form:

```text
mode ∼ e^{-iωτ}
```

with:

```text
E = ℏω
```

So, if `ℏ > 0` is imported as the frequency-to-energy conversion scalar:

```text
ω > 0 ⇔ E > 0
```

Thus B9's positive-frequency slot is sharpened:

```text
positive frequency = energy-momentum rendered positive by future-directed flow.
```

This is MGR/GR-owned **conditional on** importing `ℏ` as the conversion between flow-frequency and energy.

---

## 4. No-extra / no-missing audit

### 4.1 Missing if no energy orientation

Without a positive-energy orientation, frequency decomposition relative to flow is ambiguous:

```text
ω and -ω both appear as independent candidates.
```

But energy is already the flow-conjugate face of energy-momentum. Once future-directed flow is fixed, allowing both signs as independent physical orientations would leave the detector response without a stable reference direction.

So the orientation is not optional:

```text
future-directed flow requires a compatible energy orientation.
```

### 4.2 Extra if negative frequency is made independent content

The negative-frequency component need not be a second physical energy direction. In a real scalar field, negative-frequency modes are paired with complex conjugates; in quantum theory they become creation/annihilation bookkeeping. Either way, treating negative frequency as an independent physical bearer of negative energy would double-count the same scalar degree or introduce an unbounded instability.

MGR reading:

```text
positive-frequency mode:
  future-flow energy orientation

negative-frequency partner:
  conjugate/bookkeeping face or reverse orientation,
  not an independent extra physical energy-flow content
```

This is a no-extra result, not a full quantum derivation.

### 4.3 Stability floor

A detector response requires a stable reference state. If arbitrary negative-energy excitations are physical, the response has no lower floor; excitation/de-excitation cannot be measured against a stable ground.

So B10 can derive the need for a stability floor:

```text
flow-indexed response requires a lower energy reference
relative to the sampling flow.
```

But it cannot yet derive which state fills that role.

---

## 5. Where the derivation stops

The following are different claims:

```text
C1. future-directed flow gives positive local energy orientation;
C2. positive frequency means positive energy relative to that flow;
C3. stable response requires a lower energy floor;
C4. there exists a unique vacuum state realizing that floor;
C5. the detector samples that vacuum through a Wightman two-point function.
```

B10 earns C1–C3.

B10 does not earn C4–C5.

Why not?

Because a vacuum is not merely a sign choice. It is a state selection. In QFT it depends on spectral structure, boundary conditions, global symmetries, and often observer/congruence structure. In generic curved spacetime there may be no unique global positive-frequency split and no unique vacuum.

That fact is not a problem for MGR. It is exactly where the boundary should land:

```text
local energy orientation:
  GR / MGR-owned

global vacuum/state selection:
  quantum-state import
```

---

## 6. Conditional derivation theorem

B10 can state a sharper conditional theorem:

```text
If:
  a scalar interval-relatedness skeleton exists;
  a future-directed flow is chosen;
  energy is the flow-conjugate rendering of energy-momentum;
  the scalar sector admits a stable lower-energy state relative to that flow;
  detector uptake samples that state's two-point relatedness;

then:
  positive frequency is fixed as future-flow positive energy,
  and the Wightman iε sign is fixed by that orientation.
```

This moves the import again:

```text
old import:
  Wightman iε as a finished QFT object

B9 import:
  stable positive-energy vacuum + two-point sampling rule

B10 narrowed import:
  existence/selection of the stable state + two-point sampling rule
```

MGR now owns the sign/orientation logic once the stable state is admitted.

---

## 7. Relation to Unruh

For Unruh, the crucial subtlety remains:

```text
Minkowski vacuum:
  stable positive-energy state relative to inertial time

accelerated detector:
  samples that same state along accelerated flow
```

B7/B8/B9/B10 together now say:

```text
GR / LC earns:
  scalar interval skeleton;
  accelerated pullback;
  2π imaginary proper-time period.

MGR earns:
  retarded causal orientation;
  positive frequency as future-flow energy orientation;
  need for stability floor.

QFT imports:
  the Minkowski vacuum as the state;
  Wightman two-point sampling;
  KMS/detailed-balance detector response.
```

This is the cleanest current split.

---

## 8. Failure / demotion conditions

This run demotes if:

```text
F1. Local energy positivity relative to future-directed flow fails for physical causal energy-momentum.
F2. Positive frequency cannot be tied to positive flow-energy orientation.
F3. Negative-frequency partners must be treated as independent physical negative-energy content rather than conjugate/bookkeeping or reverse-orientation content.
F4. Stable detector response does not require any lower energy reference.
F5. Vacuum/state selection can be derived locally without quantum-state structure, contrary to the boundary stated here.
```

Current status:

```text
F1:
  not fired locally for future-directed causal momenta.

F2:
  not fired once ℏ is admitted as frequency-energy conversion.

F3:
  not fired as stated; negative-frequency-as-independent-content would create extra/double-counting or instability.

F4:
  not fired; response needs a stable reference.

F5:
  live in reverse — if someone derives vacuum selection from pure GR/MGR, B10 promotes; until then it remains imported.
```

---

## 9. Relation to influence floor

Influence floor:

```text
influence = consequence-capable phase-bearing relatedness
```

After B8–B10:

```text
relatedness:
  GR / LC earns the interval scalar skeleton.

phase-bearing:
  analytic/frequency orientation is tied to future-flow energy orientation;
  full quantum phase/vacuum structure still imported.

consequence-capable:
  causal/retarded response is role-natural;
  actual detector uptake and threshold remain application-supplied.
```

So the influence floor is narrowed again.

The current face is:

```text
scalar phase-bearing relatedness
= interval-governed two-place relatedness
  with future-flow energy orientation,
  sampled from a stable state when such a state is supplied.
```

This is not the whole influence floor. It is the scalar face.

---

## 10. Standing result

B10 standing result:

```text
MGR can derive positive-energy orientation,
but not the vacuum state.
```

The updated boundary:

```text
GR/LC:
  scalar interval skeleton

MGR roles:
  retarded causal support;
  positive frequency as future-flow energy orientation;
  need for a stability floor

QFT/imported quantum state:
  existence/selection of the vacuum;
  Wightman two-point sampling;
  KMS/detailed balance;
  detector transition probabilities
```

The next possible run is not "derive vacuum" in general. In generic curved spacetime, there may be no unique vacuum. The disciplined next run is narrower:

```text
Can MGR derive a local Hadamard/stability condition
as the minimal admissible scalar state condition,
without choosing a global vacuum?
```

That is the next wall.