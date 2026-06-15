# B5a — Neutron-Star Torsion Worksheet

Status: working experimental-target worksheet.  
Parent: `b5-levi-civita-torsion-and-closure-faces.md`.  
Grade: number-pipeline scaffold for the B5 spin → torsion structural bet; magnitude externally priced; no torsion signal claimed.

This worksheet turns the B5 torsion bet into an astrophysical number pipeline:

```text
independent spin / angular-momentum current
→ torsion-sector equation
→ torsion tensor / contortion / effective correction
→ neutron-star observable shift or bound
```

The framework-owned claim is the routing:

```text
spin density / spin current in
→ torsion burden out
```

The externally owned physics is the numerical pricing: Einstein-Cartan / Poincaré-gauge model, equation of state, rotation model, magnetic-field model, and observational inference pipeline.

## 1. Quantitative target

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

The cleanest positive prediction is:

```text
if an independent spin current is retained,
the leading non-GR affine closure-failure correction should scale with spin / angular-momentum current,
not with mass-energy density alone.
```

## 2. Current observational anchors

| Anchor | Available data | Use in torsion worksheet |
|---|---:|---|
| PSR J0740+6620 mass | `M = 2.08 ± 0.07 M_sun` | High-mass support constraint; any torsion-modified EOS must still support about two solar masses. |
| PSR J0740+6620 radius | updated NICER/XMM result: `R_eq = 12.92^{+2.09}_{-1.13} km` at 68% credibility | First radius-shift target; compare predicted `ΔR` against current uncertainty. |
| PSR J0740+6620 spin | period about `2.89 ms` | Rotation input; not near breakup, but fast enough to test spin/rotation-correlated residuals. |
| PSR J0030+0451 radius/mass | NICER source near `M ~ 1.3–1.4 M_sun`, `R ~ 13 km` in 2019 analyses; later reanalyses emphasize model dependence | Lower-mass radius anchor; useful for mass-dependence versus spin-dependence separation. |
| GW170817 / BNS events | tidal deformability and EOS constraints; radius-sensitive through compactness | Tests whether torsion-induced `ΔR` implies allowed or excluded `ΔΛ`. |
| PSR J0952−0607 | mass estimate `M_NS = 2.35 ± 0.17 M_sun`; spin frequency about `707 Hz` | Extreme high-mass / high-spin candidate; mass modeling is less clean than Shapiro-delay systems, but important stress case. |

## 3. Direct torsion-model anchor

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

## 4. First working table

| Object / event | Data now | Spin / current input | Torsion channel to price | Output number | First status |
|---|---:|---|---|---:|---|
| PSR J0740+6620 | `M = 2.08 ± 0.07 M_sun`; `R_eq = 12.92^{+2.09}_{-1.13} km`; `P ≈ 2.89 ms` | rotation; possible internal spin-density model | rotation-induced torsion or EC spin-density torsion | `ΔR`, `ΔI`, `ΔΛ`, sign of spin-up/down | Best first calibrated object; predicted `ΔR <= 0.9 km` is below but near current radius uncertainty. |
| PSR J0030+0451 | NICER mass/radius anchor around lower mass; radius inference model-dependent | rotation / spin state | same torsion channel as above | `ΔR(M,f)`, compare lower-mass response | Control object for mass-dependence; less clean due model dependence. |
| GW170817 | BNS tidal/EOS constraint | binary components' compactness, possible spin prior | torsion-modified mass-radius relation | `ΔΛ`, inferred `R_1.4` shift | Strong radius-sensitive population constraint; not direct torsion. |
| PSR J0952−0607 | `M_NS = 2.35 ± 0.17 M_sun`; `f ≈ 707 Hz` | high spin, high mass; model-dependent mass | high-spin stress test | `ΔR`, `ΔM_max`, possible spin-torsion residual | Interesting extreme case; not first calibration because radius is not NICER-clean. |
| Future moment-of-inertia measurement | expected from precision pulsar timing / double-pulsar programs | rotation + compactness | torsion-modified `I(M,R,f)` | `ΔI` | High value; moment of inertia may distinguish rotation/torsion corrections from EOS-only shifts. |

## 5. Minimal calculation pipeline

For each selected neutron star or EOS family:

```text
1. Choose baseline GR / TOV model:
   EOS, M, R, ρ_c, I, Λ.

2. Choose torsion source model:
   microphysical spin density
   or
   rotation-induced angular-momentum source.

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

## 6. Useful approximate sensitivity

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

This is only a sensitivity estimate, not a prediction. The Love number and EOS response must be recomputed in a real model. But it shows why a sub-kilometer torsion radius shift is not automatically observationally irrelevant.

## 7. First target: PSR J0740+6620

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
Run the Jockel-Menger torsion correction or an EC-priced analogue across EOS families
that already fit J0740 and GW170817.

Ask whether adding a spin/rotation torsion channel improves, worsens, or is invisible
relative to the combined mass-radius-tidal data.
```

## 8. What would count as positive evidence?

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

## 9. External anchors

- Jockel and Menger, `Effect of Torsion on Neutron Star Structure in Einstein-Cartan Gravity`, arXiv:2406.05851.
- Dittmann et al., `A More Precise Measurement of the Radius of PSR J0740+6620 Using Updated NICER Data`, arXiv:2406.14467.
- Riley et al., `A NICER View of the Massive Pulsar PSR J0740+6620 Informed by Radio Timing and XMM-Newton Spectroscopy`, arXiv:2105.06980.
- Riley et al., `A NICER View of PSR J0030+0451: Millisecond Pulsar Parameter Estimation`, arXiv:1912.05702.
- Romani et al., `PSR J0952−0607: The Fastest and Heaviest Known Galactic Neutron Star`, arXiv:2207.05124.
- Standard GW170817 / binary-neutron-star tidal-deformability and EOS literature.
