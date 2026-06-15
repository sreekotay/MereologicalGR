# B9 — Positive Frequency and the iε Prescription

*Working draft, June 2026.*

Status: B-note / hard-gate audit.  
Primary target: B8 scalar kernel boundary, B7 scalar response, B6 Unruh temperature, A0 ordering/flow/influence grammar.  
Grade: locating result + conditional derivation. Not a derivation of QFT.

Core question:

```text
Can MGR derive the positive-frequency / iε prescription
from ordering + influence + flow,
rather than importing it from QFT?
```

Run result:

```text
MGR can earn:
  causal orientation;
  retarded-vs-advanced asymmetry;
  the need for an ordering prescription at the light-cone singularity;
  positive-frequency as the energy/flow orientation slot,
  conditional on a stability / positive-energy postulate.

MGR cannot yet earn:
  the vacuum state;
  Hilbert-space spectral positivity;
  Wightman rather than retarded/Feynman choice;
  the full iε prescription as a quantum-state boundary condition.
```

So the boundary after B8 sharpens again:

```text
GR / LC earns:
  scalar interval skeleton

MGR role grammar earns:
  causal orientation and retarded ordering

QFT / quantum-state import remains:
  positive-frequency vacuum sampling / Wightman iε / KMS response
```

---

## 1. What B8 left open

B8 narrowed the scalar kernel import.

```text
GR-earned:
  R_skel(x,x′) ∝ 1/σ(x,x′)

not yet earned:
  iε;
  positive-frequency split;
  which side of the singularity is approached;
  which vacuum / state is sampled.
```

The tempting next move is to say:

```text
ordering supplies the sign of iε.
```

That is only partly right.

Ordering can supply a future/past distinction. It cannot by itself supply the quantum vacuum or positive-frequency split.

---

## 2. Three different prescriptions that must not be fused

The notation `iε` hides different jobs.

```text
retarded / advanced prescription:
  causal support choice;
  does influence propagate only to the future or only to the past?

Feynman prescription:
  time-ordered propagation;
  positive energy forward, negative energy backward in the time-ordering formalism.

Wightman / positive-frequency prescription:
  vacuum correlation / state sampling;
  chooses positive-frequency modes relative to a time-flow.
```

MGR can pressure the first most strongly, locate the second, and only conditionally reach the third.

For Unruh, the detector response uses the Wightman object, not merely the retarded causal Green function. That matters. A causal response kernel tells what can affect what; a Wightman kernel tells what vacuum relatedness a detector samples.

---

## 3. Run 3A — retarded ordering from cause

MGR composition:

```text
cause = ordering + influence
```

If influence is to be causal influence, then the influence-expression must respect ordering:

```text
future-directed ordering:
  event x can influence event y only if y lies in x's future cone
```

So MGR earns a retarded/advanced fork:

```text
retarded:
  influence follows ordering

advanced:
  influence runs against ordering
```

Given the framework's photon seed and cause composition, the retarded choice is the native causal one:

```text
cause = ordering + influence
⇒ influence-expression is future-ordered
⇒ retarded support is role-natural
```

This is a genuine result:

```text
MGR can derive the need for a causal boundary prescription
at the null singularity,
and it can privilege the retarded prescription for causal response.
```

But this is not yet the Wightman `iε`.

---

## 4. Run 3B — positive frequency from flow-conjugacy

A0 already reads energy as the flow-conjugate face of energy-momentum.

```text
flow:
  proper-time accrual along a timelike worldline

energy:
  conjugate to flow
```

A frequency decomposition relative to a timelike flow is therefore natural:

```text
mode ∼ e^{-iωτ}

ω:
  flow-frequency

ℏω:
  energy
```

Positive frequency then means:

```text
positive energy relative to future-directed flow
```

So MGR can locate the positive-frequency slot:

```text
positive-frequency = future-flow-compatible energy orientation
```

But the step from this slot to a selected vacuum correlation needs a further premise:

```text
stability / spectral condition:
  the physically relevant state has no excitations of negative energy
  relative to the chosen future-directed flow.
```

That condition is not pure GR. It is a quantum/state postulate or a stability import.

Therefore:

```text
MGR can identify what positive frequency means.
MGR cannot yet derive that the Wightman function must select it.
```

---

## 5. Run 3C — can iε be role-derived?

Start with the GR/LC scalar skeleton:

```text
R_skel(x,x′) ∝ 1/σ(x,x′)
```

The singularity lies at:

```text
σ = 0
```

To make this into a usable distribution, one must specify how the singularity is approached.

MGR role pressure:

```text
ordering:
  supplies future/past distinction

flow:
  supplies proper-time orientation and frequency decomposition

influence:
  supplies consequence-capable relatedness across the singular support
```

This earns the claim:

```text
some ordering prescription is required;
it cannot be left as a naked singularity.
```

For causal response, this gives a retarded `i0`-type prescription.

For Wightman response, however, the prescription is stronger:

```text
ct - ct′ → ct - ct′ - iε
```

which selects positive-frequency vacuum correlations.

That selection requires:

```text
1. a time-flow relative to which frequency is defined;
2. a positive-energy / stability condition;
3. a state called vacuum;
4. a rule that the detector samples that state through a two-point function.
```

MGR gives (1) and locates (2). It does not derive (3) or (4).

So B9's answer is:

```text
retarded i0:
  role-derived / causal-response natural

Wightman iε:
  conditionally located, not derived
```

---

## 6. Consequence for B7/B8

B7 and B8 reached:

```text
R_skel(Δτ) ∝ 1 / sinh²[aΔτ/(2c)]
```

and its imaginary period:

```text
β_τ = 2πc/a
```

B9 says:

```text
periodicity as analytic geometry:
  earned by GR/LC + scalar skeleton

retarded causal orientation:
  earned by MGR cause = ordering + influence

Wightman/KMS thermal response:
  still imported from quantum state/spectral structure
```

This prevents a false promotion. The `2π` period is real and GR-owned at the skeleton level. But the fact that a detector samples it as a thermal Wightman response is not yet MGR-derived.

---

## 7. Conditional derivation theorem

B9 can state a conditional theorem:

```text
If:
  scalar interval relatedness exists;
  the scalar sector has a stable positive-energy vacuum relative to a future-directed flow;
  detector uptake samples the vacuum two-point relatedness;

then:
  the iε sign and positive-frequency Wightman choice are fixed by
  future-flow orientation + stability.
```

This is useful but conditional. It moves the import:

```text
old import:
  Wightman iε as a finished QFT object

new conditional import:
  stable positive-energy vacuum + two-point sampling rule
```

That is progress. It is not full derivation.

---

## 8. Failure / demotion conditions

This run demotes if:

```text
F1. Retarded causal support cannot be derived from ordering + influence.
F2. Positive frequency cannot be identified with future-flow-compatible energy orientation.
F3. The Wightman iε sign has no relation to future-flow orientation or energy positivity.
F4. The vacuum/spectral condition cannot be separated from the whole QFT apparatus.
F5. Detector response cannot be stated as two-point sampling without importing full field quantization.
```

Current status:

```text
F1:
  not fired — retarded causal support follows directly from cause = ordering + influence.

F2:
  not fired — energy is flow-conjugate, so positive frequency is naturally positive energy relative to flow.

F3:
  not fired conditionally — Wightman sign tracks positive-frequency choice once that choice is admitted.

F4:
  live — vacuum/spectral positivity may be inseparable from QFT.

F5:
  live — detector response remains QFT/imported beyond the skeleton.
```

---

## 9. Relation to influence floor

Influence floor:

```text
influence = consequence-capable phase-bearing relatedness
```

B8 earned the scalar relatedness skeleton.

B9 adds:

```text
phase-bearing, scalar quantum face:
  requires a positive-frequency orientation of relatedness relative to flow.
```

Thus the floor splits:

```text
relatedness:
  GR/LC interval skeleton

phase-bearing:
  analytic/frequency orientation;
  conditionally tied to future-directed flow and energy positivity;
  not fully derived

consequence-capable:
  retarded causal response is role-natural;
  detector uptake still imported/application-supplied
```

This is a useful narrowing. It shows where phase lives:

```text
not in the interval skeleton alone;
but in the orientation / spectral reading of that skeleton through flow.
```

---

## 10. Standing result

B9 standing result:

```text
MGR derives causal ordering of scalar influence,
and conditionally locates positive-frequency as future-flow energy orientation.
```

But:

```text
MGR does not yet derive the Wightman vacuum prescription.
```

Updated boundary:

```text
GR/LC:
  interval kernel skeleton

MGR roles:
  retarded causal support;
  positive-frequency slot as flow-energy orientation

QFT / imported quantum state:
  vacuum selection;
  spectral positivity;
  Wightman iε;
  KMS/detailed balance;
  detector transition probabilities
```

The next possible run is no longer about `iε` directly. It is about the stability/vacuum postulate:

```text
Can the positive-energy vacuum condition be derived from
flow + energy-momentum + no-extra/no-missing,
or must it remain imported?
```

That is the next wall.