# B5 Neutron-Star Torsion Ledger

*Working draft, June 2026.*

Status: first numerical/outward ledger for the B5 torsion bet.  
Purpose: convert the structural bet `spin/current in → torsion burden out` into an object table, contrast design, and first-pass sensitivity targets.  
Grade: prediction-program scaffold with externally priced magnitudes. This does not derive Einstein-Cartan or Poincaré-gauge coupling constants. It specifies the residual shape and the data handles to test.

Core contrast:

```text
Hold mass/EOS/baseline GR modeling fixed as far as possible.
Vary spin/current structure.
If torsion is live, the residual should track spin/current,
not mass-energy density alone.
```

Primary prediction form:

```text
Observable_data
  = Observable_GR+EOS+ordinary-rotation+ordinary-matter
    + Observable_torsion(spin/current)
    + noise/systematics
```

If live:

```text
Observable_torsion ∝ independent spin/current source structure
```

If hidden:

```text
Observable_torsion is bounded below current sensitivity
```

If absent by role:

```text
a forced-empty proof is required;
empirical nulls alone only tighten bounds
```

---

## 1. What counts as positive

Not positive:

```text
any mass-radius anomaly
any EOS tension
any high-mass neutron star
any fast pulsar
```

Positive candidate:

```text
a residual that survives GR+EOS+ordinary-rotation+magnetic+thermal+crustal modeling
and correlates with spin/current structure better than with mass-energy density alone
```

Best positive pattern:

```text
same EOS family fits slow / low-spin objects;
fast / high-spin objects show residuals;
residual sign and scale match torsion-sector pricing;
ordinary matter effects do not absorb it.
```

---

## 2. Source-model split

The B5 torsion bet has two source lanes. Keep them separate.

```text
A. Intrinsic-spin / minimal Einstein-Cartan lane
   source: fermion spin density / independent spin current
   framework status: cleanest B5 lineage
   expected current status: likely hidden or tiny in realistic neutron-star models

B. Rotation-induced / phenomenological torsion lane
   source: macroscopic angular momentum, rotation, or model-specific current
   framework status: less clean but observationally more visible
   expected current status: potentially sub-km to km-scale radius effects in some models
```

The first lane is cleaner for the framework. The second lane is probably better for near-term data.

---

## 3. First observable list

```text
ΔR:
  radius shift

ΔI:
  moment-of-inertia shift

ΔΛ:
  tidal-deformability shift

ΔM_max:
  maximum-mass shift

Δρ_c:
  central-density shift

ΔE_bind:
  binding-energy shift

Δω_LT / frame-dragging:
  precession or dragging correction traceable to contortion

post-merger frequency shift:
  dense rotating remnant stress test
```

Priority ranking:

```text
1. ΔR and ΔΛ:
   available now through NICER / GW constraints, but EOS-degenerate

2. ΔI:
   cleaner future discriminator if moment-of-inertia measurements arrive

3. ΔM_max and Δρ_c:
   model-level constraints; useful for EOS compatibility

4. frame-dragging/precession:
   high value but harder to isolate

5. post-merger frequencies:
   future high-density/high-spin stress test
```

---

## 4. First target table

| Object / channel | Current handle | Why it matters | First torsion question | First observable | Status |
|---|---:|---|---|---|---|
| PSR J0740+6620 | `M = 2.08 ± 0.07 M_sun`; `R_eq = 12.92^{+2.09}_{-1.13} km`; `P ≈ 2.886 ms` | high mass, NICER/XMM radius, known millisecond spin | can a torsion-priced rotation/current correction fit without spoiling high-mass support? | `ΔR`, `ΔI`, `ΔΛ` | first calibration target |
| PSR J0030+0451 | original NICER analyses near `M ~ 1.3–1.4 M_sun`, `R ~ 13 km`; later reanalyses emphasize model-dependence, with possible compactness-led solutions near `R ~ 12.4 km` | lower-mass control; model-dependent radius inference | does the same EOS/torsion lane behave differently at lower mass/spin? | `ΔR(M,f)`, compactness residual | control / caution object |
| PSR J0952−0607 | `M_NS ≈ 2.35 ± 0.17 M_sun`; `f ≈ 707 Hz` | high-spin / high-mass stress case | does a spin/current correction appear in the most extreme fast/heavy cases? | `ΔM_max`, `ΔR`, spin residual | stress target; radius not clean |
| GW170817-like BNS constraints | tidal deformability / EOS constraints | radius-sensitive population constraint | do torsion-induced `ΔR` and `ΔΛ` remain allowed by tidal data? | `ΔΛ`, `R_1.4` shift | population constraint |
| Future double-pulsar moment of inertia | possible precision timing observable | `I` may distinguish EOS-only from spin/current correction | does `ΔI` scale with spin/current in a torsion-priced way? | `ΔI` | high-value future discriminator |
| Post-merger GW spectra | dense, hot, rapidly rotating remnant | high spin/current and high density | do remnant frequencies or damping show spin/current residuals beyond EOS? | `f_peak`, damping, compactness residual | future stress case |

---

## 5. First numerical sensitivity: radius to tidal deformability

Tidal deformability is strongly radius-sensitive. Schematically:

```text
Λ ~ k₂ / C⁵
C = GM/(Rc²)
```

Holding mass and Love-number response aside for a first-pass estimate:

```text
ΔΛ / Λ ≈ 5 ΔR / R
```

For a typical radius:

```text
R ≈ 13 km
```

and a torsion-model radius shift:

```text
ΔR ≈ 0.9 km
```

then:

```text
ΔR/R ≈ 0.9/13 ≈ 0.069
ΔΛ/Λ ≈ 5 × 0.069 ≈ 0.35
```

Interpretation:

```text
A sub-km to km-scale torsion radius shift can be order-30% in tidal-deformability sensitivity.
This is not a prediction until the EOS/Love-number response is recomputed.
It is a reason to include ΔΛ early in the ledger.
```

---

## 6. Object-specific first passes

### 6.1 PSR J0740+6620

Known handle:

```text
M = 2.08 ± 0.07 M_sun
R_eq = 12.92^{+2.09}_{-1.13} km
P ≈ 2.886 ms
```

First comparison:

```text
current 68% radius lower uncertainty ≈ 1.13 km
rotation-induced torsion-model target ≈ up to 0.9 km
```

Readout:

```text
not a detection;
not obviously excluded;
near enough to current radius precision to justify model-level comparison.
```

First task:

```text
For EOS families fitting J0740 and GW170817,
compute whether a spin/current torsion correction can shift R or I
without violating high-mass support.
```

### 6.2 PSR J0030+0451

Known handle:

```text
original NICER analyses: M ~ 1.3–1.4 M_sun, R ~ 13 km
updated analyses: mass/radius inference more model-dependent;
compactness-led estimates can give R ~ 12.4 km in some models
```

Readout:

```text
use as a lower-mass control, not as a clean radius anchor.
```

First task:

```text
Ask whether the torsion correction has the expected mass/spin dependence
relative to J0740-like objects.
```

### 6.3 PSR J0952−0607

Known handle:

```text
M_NS ≈ 2.35 ± 0.17 M_sun
f ≈ 707 Hz
```

Readout:

```text
extreme spin/high-mass stress case;
excellent for source-knob intuition;
not first calibration because the mass/radius inference is less clean.
```

First task:

```text
Use as a high-spin/high-mass constraint on ΔM_max and spin-current scaling,
not as the primary radius target.
```

### 6.4 GW170817-like BNS constraints

Known handle:

```text
tidal deformability constraints restrict EOS and radius range.
```

Readout:

```text
any torsion radius shift must be checked against tidal deformability.
```

First task:

```text
Translate ΔR from each torsion source model into approximate ΔΛ,
then run or cite full EOS/Love-number recomputation where available.
```

---

## 7. Model comparison design

The minimum useful comparison is not one object. It is a contrast set:

```text
slow / low-spin control
fast / high-spin stress object
high-mass radius anchor
population tidal constraint
```

First contrast set:

```text
J0030:
  lower-mass / control / model-dependent radius

J0740:
  high-mass / NICER radius / known ms spin

J0952:
  high-spin + high-mass stress case

GW170817-like population:
  tidal/EOS constraint
```

Desired pattern:

```text
same EOS family works across low-spin / ordinary-spin objects;
fast/high-spin objects carry an additional residual;
residual tracks spin/current and matches torsion pricing;
tidal constraints remain acceptable.
```

Bad pattern:

```text
residual tracks mass alone;
residual disappears under EOS change;
residual tracks magnetic/crust/thermal/ordinary-rotation priors;
torsion correction spoils high-mass or tidal constraints.
```

---

## 8. Minimal spreadsheet schema

```text
object
M_mean
M_minus
M_plus
R_mean
R_minus
R_plus
spin_frequency_Hz
spin_period_ms
has_radius_anchor
has_tidal_anchor
has_moment_of_inertia_anchor
source_lane_intrinsic_spin
source_lane_rotation_induced
torsion_model_reference
Delta_R_target_km
Delta_Lambda_over_Lambda_estimate
ordinary_explanations_to_control
framework_status
notes
```

First seeded rows:

| object | M_mean | M_minus | M_plus | R_mean | R_minus | R_plus | spin_frequency_Hz | spin_period_ms | ΔR_target_km | ΔΛ/Λ rough if R≈13km | status |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| PSR J0740+6620 | 2.08 | 0.07 | 0.07 | 12.92 | 1.13 | 2.09 | ~346 | 2.886 | up to ~0.9 | ~0.35 | first calibration target |
| PSR J0030+0451 | ~1.3–1.5 | TBD | TBD | ~12.4–13 | TBD | TBD | ~205 | ~4.87 | model-dependent | model-dependent | lower-mass control |
| PSR J0952−0607 | 2.35 | 0.17 | 0.17 | unknown | unknown | unknown | 707 | 1.414 | stress only | not radius-ready | high-spin/high-mass stress target |
| GW170817-like BNS | population | — | — | inferred | — | — | low/moderate | — | constrain | constrain | tidal/EOS check |

The J0030 spin row uses its known millisecond pulsar period/frequency as a working value and should be verified in the first literature pass before the table is promoted.

---

## 9. Failure / success flags

### Green flags

```text
spin/current-correlated residual survives EOS variation;
sign and scale match torsion-sector pricing;
fast/high-spin objects show correction absent in slow controls;
ΔI or frame-dragging correction agrees with same source lane;
tidal deformability remains compatible.
```

### Yellow flags

```text
radius shift comparable to uncertainty but EOS-degenerate;
rotation-induced lane visible but intrinsic-spin lane hidden;
source model is phenomenological rather than minimal EC;
residual could be magnetic/crust/thermal.
```

### Red flags

```text
residual tracks mass/compactness only;
EOS variation absorbs all improvement;
torsion correction violates high-mass support or tidal constraints;
source lane cannot be connected to independent spin/current;
model introduces free parameters that fit anything.
```

### Forced-empty is not a data flag

```text
No detection → tighter bound.
Persistent nulls → weaker bet.
Forced-empty → role-level closure proof required.
```

---

## 10. Immediate next calculation

First numeric calculation to perform:

```text
For each object with R available:
  choose ΔR = -0.9 km, -0.5 km, +0.5 km, +0.9 km
  compute ΔR/R
  compute rough ΔΛ/Λ ≈ 5ΔR/R
  compare to current radius/tidal uncertainty
```

For J0740:

```text
R = 12.92 km
ΔR = -0.9 km

ΔR/R = -0.0697
ΔΛ/Λ ≈ -0.348
```

For J0030 using `R = 12.4 km` as a working compactness-led estimate:

```text
ΔR/R = -0.9/12.4 = -0.0726
ΔΛ/Λ ≈ -0.363
```

Interpretation:

```text
sub-km torsion shifts would be large enough in tidal sensitivity to matter,
but current object-level radius inference and EOS/Love-number recomputation decide whether the effect is visible or absorbed.
```

---

## 11. References / anchors to verify in first literature pass

- Dittmann et al. 2024, updated NICER/XMM radius for PSR J0740+6620: `M = 2.08 ± 0.07 M_sun`, `R_eq = 12.92^{+2.09}_{-1.13} km`.
- Riley et al. 2019 and Miller et al. 2019, original NICER analyses of PSR J0030+0451 near `M ~ 1.3–1.4 M_sun`, `R ~ 13 km`.
- Vinciguerra et al. 2023/2024 updated J0030 analysis: model dependence; possible solutions around `[1.4 M_sun, 11.5 km]` and `[1.7 M_sun, 14.5 km]` depending on model.
- Luo et al. 2024 compactness-led J0030 inference near `M ≈ 1.48 M_sun`, `R ≈ 12.38 km` for selected compactness model.
- Romani et al. 2022, PSR J0952−0607: `M_NS ≈ 2.35 ± 0.17 M_sun`, `f ≈ 707 Hz`.
- Jockel and Menger 2024, Einstein-Cartan neutron-star torsion: realistic microphysical spin models negligible; rotation-induced torsion can shift radius by up to about 900 m.
- Poincaré-gauge neutron-star torsion literature, especially models where contorsion is algebraically solved in terms of spin current and affects compactness / maximum mass / binding energy.
- GW170817 and later BNS tidal-deformability EOS constraints.

---

## 12. Compact result

```text
B5's first real outward prediction is not "neutron stars deviate."
It is:

  if the torsion cell is live,
  residuals should scale with spin/current source structure,
  not mass-energy density alone.

The first numerical window is compact-object structure:
  ΔR, ΔI, ΔΛ, ΔM_max, Δρ_c.

The first sensitivity marker is:
  ΔR ~ 0.9 km at R ~ 13 km → rough ΔΛ/Λ ~ 0.35.

The first calibration object is J0740.
The first control is J0030.
The first high-spin stress case is J0952.
The first population constraint is GW170817-like BNS tidal data.
```

This file is deliberately a ledger, not a conclusion. The next step is a spreadsheet or script that computes the first ΔR/ΔΛ sensitivity rows and marks which effects are already excluded, hidden, or worth modeling.
