# B5 — J0740/BNS Negative-Torsion Lane

*Working draft, June 2026.*

Status: first sign-specific modeling lane for the neutron-star torsion program.  
Purpose: take the compatibility-gate result seriously and turn it into a model-selection question.  
Grade: triage / modeling target. No new stellar-structure calculation yet. Magnitudes and EOS behavior remain externally priced.

Core result from the first gates:

```text
The sign matters.

A negative torsion radius correction can let a high-baseline-radius EOS pass through
J0740 while landing closer to the BNS/tidal radius window.

A positive population-wide radius correction of comparable size risks over-expanding
BNS radii and should face tidal constraints first.
```

The first modeling lane is therefore:

```text
high-baseline-radius EOS
+
negative torsion radius correction
→ observed J0740 radius
and
BNS/tidal compatibility
```

---

## 1. What the gate computed

For J0740, using:

```text
R_obs = 12.92 km
```

and a proposed torsion correction:

```text
ΔR_torsion = -0.9 km
```

then the required GR/EOS baseline is:

```text
R_GR_required = R_obs - ΔR_torsion
              = 12.92 - (-0.9)
              = 13.82 km
```

So the negative correction says:

```text
A baseline EOS that would otherwise place J0740 near ~13.8 km
could be shifted down toward the observed ~12.9 km.
```

For a generic BNS/population radius placeholder:

```text
R_ref = 13.0 km
ΔR_torsion = -0.9 km
R_shifted = 12.1 km
```

So the same sign can move a high-ish baseline toward a more compact tidal-compatible range.

This is not a detection. It is a model lane.

---

## 2. Sign-lane interpretation

### 2.1 Negative correction lane

```text
baseline EOS radius:
  high / stiff-ish

torsion correction:
  negative ΔR

observed output:
  smaller radius

potential upside:
  may relieve tension between high-mass support and tidal/radius compactness
```

This lane is interesting because a high-mass object like J0740 demands EOS support, while BNS tidal data generally punish radii that are too large. A negative spin/current torsion correction could, in principle, let the baseline microphysics remain supportive while compactifying the observable star.

Framework read:

```text
spin/current-rich high-mass star
→ torsion/contortion correction
→ smaller observed R or altered I/Λ
```

### 2.2 Positive correction lane

```text
baseline EOS radius:
  ordinary / compact

torsion correction:
  positive ΔR

observed output:
  larger radius

risk:
  BNS/tidal population may over-expand
```

This lane is not forbidden, but it is less attractive as first target. A positive `+0.9 km` population-wide correction pushed the generic radius placeholder to `13.9 km`, which the current triage labels as high-radius/tidal risk.

---

## 3. First hypothesis

Candidate H1:

```text
If the B5 torsion cell is live in compact stars,
then the first viable observable lane is a negative radius correction in high-spin/current regimes.
```

More explicit:

```text
H1:
  A spin/current-sourced torsion correction can reduce observable radius and/or tidal deformability
  relative to a GR/EOS baseline, with the correction scaling with spin/current structure.
```

Predicted sign pattern:

```text
high spin/current:
  negative ΔR or reduced effective Λ relative to baseline

low spin/current control:
  smaller or absent correction
```

This is aligned with the already-noted rotation-induced torsion channel where some models report radius decreases up to order `0.9 km`.

Guardrail:

```text
Do not claim minimal intrinsic-spin EC necessarily produces this visible effect.
The visible lane may be rotation-induced / phenomenological torsion and therefore more model-dependent.
```

---

## 4. First model-selection question

The next modeling question is:

```text
Can one EOS family fit J0740 mass/radius while allowing a negative torsion ΔR
without violating BNS tidal constraints?
```

Expanded:

```text
Given an EOS family that supports M ≳ 2 M_sun,
compute GR baseline R(M) and Λ(M).

Apply a torsion correction ΔR_torsion(M, spin/current, source lane).

Ask:
  1. Does J0740 land inside its mass/radius posterior?
  2. Does the same EOS/correction stay inside BNS tidal constraints?
  3. Does the correction scale with spin/current rather than mass alone?
  4. Does it improve fit relative to pure GR+EOS, or merely add a free knob?
```

Minimum model equation for triage:

```text
R_obs(M, s) = R_GR(EOS, M) + ΔR_torsion(M, s)
```

where:

```text
s = spin/current source variable
```

The first sign lane uses:

```text
ΔR_torsion < 0
```

---

## 5. First contrast set

The minimal contrast set:

```text
J0740:
  high-mass calibration target

GW170817-like BNS:
  tidal/population compatibility gate

J0030:
  lower-mass control once data row is cleaned

J0952:
  high-spin/high-mass stress case without current radius anchor
```

Desired pattern:

```text
J0740:
  correction helps or remains compatible

BNS:
  correction does not violate tidal/radius constraints

J0030:
  correction is smaller / consistent with lower-mass or lower-source control

J0952:
  correction would be large if radius/I data become available
```

Bad pattern:

```text
same correction improves J0740 but breaks BNS tidal constraints;
correction scales only with mass/compactness;
EOS variation absorbs all improvement;
magnetic/crust/thermal/ordinary-rotation terms explain the same residual more cheaply;
source lane requires arbitrary free parameters.
```

---

## 6. Triage table

| Lane | ΔR sign | J0740 baseline required | BNS population shift from R≈13 km | First gate | Interpretation |
|---|---:|---:|---:|---|---|
| Negative large | `-0.9 km` | `13.82 km` | `12.1 km` | J0740 pass with tidal caution; BNS window pass | Most interesting first lane. Can compactify stiff/high-radius baseline. |
| Negative moderate | `-0.5 km` | `13.42 km` | `12.5 km` | J0740 pass; BNS window pass | Safer, less dramatic; useful bound lane. |
| Positive moderate | `+0.5 km` | `12.42 km` | `13.5 km` | J0740 pass; BNS upper edge | Possible but watch tidal/radius ceiling. |
| Positive large | `+0.9 km` | `12.02 km` | `13.9 km` | J0740 pass; BNS high-radius risk | Lower priority; likely constrained first by tidal population. |

---

## 7. What has to be computed next

The first real calculation requires an EOS baseline. The cheap version can use parameterized mass-radius curves. The real version needs TOV/rotating-star/EOS data and Love-number recomputation.

### 7.1 Cheap curve version

For each EOS candidate or toy curve:

```text
R_GR(M)
Λ_GR(M)
I_GR(M)
```

apply:

```text
R_torsion(M,s) = R_GR(M) + ΔR_torsion(s)
```

with sign/magnitude trial:

```text
ΔR_torsion ∈ {-0.9, -0.5, +0.5, +0.9} km
```

Then score:

```text
J0740 radius pass/fail
BNS radius/tidal pass/fail
J0030 control pass/fail
J0952 stress readiness
```

### 7.2 Real version

For each external torsion model:

```text
1. Choose EOS.
2. Solve GR/TOV baseline.
3. Apply EC/Poincaré-gauge/phenomenological torsion correction.
4. Recompute R, I, Λ, Mmax, central density.
5. Compare to J0740, BNS, J0030, J0952 stress handles.
```

The real decision variable is not just `ΔR`. It is:

```text
sign + source scaling + EOS compatibility + tidal survival
```

---

## 8. Source-scaling demand

The framework does not accept a free `ΔR` knob as positive witness. The correction must be source-routed.

Required form:

```text
ΔR_torsion = F(spin/current source, EOS, M, coupling convention)
```

Not enough:

```text
ΔR_torsion = arbitrary fitted radius offset
```

Minimum source tests:

```text
1. Does ΔR increase with spin/current source strength?
2. Does it weaken in lower-source controls?
3. Does the sign follow the torsion model rather than the fit target?
4. Does the same source lane also imply ΔI, ΔΛ, or Δρ_c with consistent signs?
```

---

## 9. First decision tree

```text
Start with negative ΔR lane.

If negative ΔR lets high-radius/high-mass EOS pass J0740 and BNS:
  advance lane to real EOS/Love-number modeling.

If negative ΔR fits J0740 but breaks BNS:
  reject or tighten magnitude/source dependence.

If negative ΔR is fully absorbed by EOS variation:
  no positive torsion witness; use as bound only.

If correction does not scale with spin/current:
  not B5-positive.

If same source lane predicts ΔI or frame-dragging shift:
  advance moment-of-inertia/precession as next discriminator.
```

---

## 10. Compact result

The first viable B5 application lane is now specific:

```text
Look for negative, spin/current-sourced radius or tidal corrections
in high-mass/high-spin compact stars,
with J0740 as calibration and BNS tidal data as compatibility gate.
```

The leading model question is:

```text
Can a stiff/high-baseline-radius EOS survive J0740 and BNS constraints
if a spin/current torsion correction shifts high-source stars downward in radius?
```

The residual claim is not simply:

```text
neutron stars are smaller
```

It is:

```text
if torsion is live,
then the correction should have a sign and magnitude dictated by spin/current source structure,
and the same source lane should survive the J0740/BNS/J0030/J0952 contrast set.
```

Immediate next artifact:

```text
Build a toy EOS-curve gate:
  assume several baseline R_GR values at 1.4 and 2.1 M_sun;
  apply ΔR signs;
  score J0740 + BNS compatibility;
  identify which baseline curve shapes are worth real modeling.
```
