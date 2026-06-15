# B5 — Jockel-Menger Figure 4 Vector Extraction Readout

*Working draft, June 2026.*

Status: vector extraction from uploaded `Figure4.pdf`.  
Purpose: move from paper-text headline to approximate numeric gate rows.  
Grade: medium-confidence figure extraction, not author-provided source data.

---

## 1. Method

Input:

```text
Figure4.pdf
```

The PDF is vector enough to extract the plotted curve paths. I converted PDF drawing coordinates into plot coordinates using the Figure 4 axis rectangle:

```text
radius axis: 10.0 to 14.0 km
mass axis:   0.0 to 2.5 M_sun
```

For target masses:

```text
M = 1.40 M_sun
M = 2.08 M_sun
```

the extraction selects the rightmost radius crossing as the stable-radius proxy.

Outputs:

```text
data/b5-jm-figure4-target-extraction.csv
data/b5-jm-figure4-target-gate.csv
```

---

## 2. Key extracted rows

### DD2 high-mass target: M = 2.08 M_sun

| curve | radius | ΔR vs pure | max mass on curve | gate |
|---|---:|---:|---:|---|
| Pure DD2 | 13.113 km | 0.000 km | 2.424 | high-mass baseline pass |
| DD2 f=100 Hz | 13.052 km | -0.060 km | 2.419 | mild negative pass |
| DD2 f=300 Hz | 12.634 km | -0.478 km | 2.381 | high-mass negative-lane pass |
| DD2 Ω=0.1 Ω_Kep | 12.927 km | -0.186 km | 2.401 | mild negative pass |
| DD2 Ω=0.2 Ω_Kep | no crossing | - | 1.577 | no target reach |
| DD2 Ω=0.3 Ω_Kep | no crossing | - | 0.590 | no target reach |

Readout:

```text
DD2 f=300 Hz is the first numerically useful B5 lane:
  M≈2.08 survives;
  R≈12.63 km lands inside the J0740 radius window;
  ΔR≈-0.48 km is close to the promoted -0.5 km lane.
```

### DD2 lower-mass / BNS proxy: M = 1.40 M_sun

| curve | radius | ΔR vs pure | max mass on curve | gate |
|---|---:|---:|---:|---|
| Pure DD2 | 13.230 km | 0.000 km | 2.424 | BNS baseline pass |
| DD2 f=100 Hz | 13.152 km | -0.079 km | 2.419 | mild BNS negative pass |
| DD2 f=300 Hz | 12.635 km | -0.595 km | 2.381 | BNS negative window pass |
| DD2 Ω=0.1 Ω_Kep | 13.070 km | -0.160 km | 2.401 | mild BNS negative pass |
| DD2 Ω=0.2 Ω_Kep | 12.615 km | -0.616 km | 1.577 | BNS negative window pass, but high-mass fail |
| DD2 Ω=0.3 Ω_Kep | no crossing | - | 0.590 | no target reach |

Readout:

```text
DD2 f=300 Hz passes both cheap gates:
  high-mass J0740 proxy pass;
  lower-mass BNS proxy pass;
  negative compactification in both rows.
```

This is the first real candidate row-set.

---

## 3. APR rows

APR reaches M≈2.08 in the vector extraction, but radii are around `10.7-10.85 km`, below the working J0740 radius window:

| curve | radius at 2.08 | ΔR vs pure | gate |
|---|---:|---:|---|
| Pure APR | 10.846 km | 0.000 km | high-mass radius fail |
| APR f=100 Hz | 10.819 km | -0.027 km | high-mass radius fail |
| APR f=200 Hz | 10.743 km | -0.103 km | high-mass radius fail |
| APR Ω=0.1 Ω_Kep | 10.701 km | -0.144 km | high-mass radius fail |

At M=1.4, APR is near or below the lower BNS proxy edge:

```text
Pure APR: 11.573 km
APR f=100 Hz: 11.521 km
APR f=200 Hz: 11.378 km
APR Ω=0.1 Ω_Kep: 11.415 km
```

Readout:

```text
APR is not the J0740 application lane.
It may be useful as a compact-EOS control / lower-radius boundary case.
```

---

## 4. What changed

Before vector extraction, the B5 lane was:

```text
maybe Jockel-Menger gives the right sign/magnitude
```

After vector extraction, it becomes:

```text
DD2 f=300 Hz gives a concrete approximate row-set:
  M=2.08: R ≈ 12.634 km, ΔR ≈ -0.478 km
  M=1.40: R ≈ 12.635 km, ΔR ≈ -0.595 km
```

This is not full author data, but it is enough to promote one lane:

```text
DD2 + f=300 Hz + rotation-induced torsion
```

from headline support to approximate candidate pipeline.

---

## 5. Updated B5 conclusion

The honest conclusion now is stronger:

```text
Jockel-Menger does not merely support the B5 lane qualitatively.
A vector extraction of Fig. 4 identifies a concrete candidate:
  DD2, f=300 Hz,
  negative compactification around -0.5 to -0.6 km,
  with M≈2.08 and M≈1.4 both surviving the working radius gates.
```

But still not final:

```text
Need author/source rows or reproducible code output.
Need Lambda/I recomputation.
Need high-mass and BNS constraints with real posteriors, not rough windows.
Need check whether f=300 Hz is the right physical comparison for J0740/J0952/BNS populations.
```

---

## 6. Next step

Promote the first model row:

```text
EOS: DD2
rotation: f = 300 Hz
model: rotation-induced torsion
```

Run a dedicated candidate-gate note:

```text
DD2 f=300 Hz J0740/BNS candidate
```

Questions:

```text
1. Is f=300 Hz close enough to J0740 spin (~346 Hz) for first approximation?
2. Does the curve's max mass remain above J0740's mass? yes, approx 2.381 M_sun in extraction.
3. Does the lower-mass row remain BNS-compatible? yes, approx 12.635 km.
4. Does the model give Lambda/I? not yet.
```

Current status:

```text
candidate observational pipeline, pending source-data verification and Lambda/I work
```
