# B5 — Jockel-Menger Tidal / Moment-of-Inertia Proxy Readout

*Working draft, June 2026.*

Status: first proxy recomputation from vector-extracted Figure 4 rows.  
Purpose: estimate how the DD2 f=300 Hz negative compactification changes tidal deformability and moment of inertia before full EOS/Love-number modeling.  
Grade: proxy only. Not a full TOV/Love-number recomputation.

---

## 1. Inputs

From vector extraction of Jockel-Menger Fig. 4:

```text
DD2 pure, M=1.40:
  R ≈ 13.230 km

DD2 f=300 Hz, M=1.40:
  R ≈ 12.635 km
  ΔR ≈ -0.595 km

DD2 pure, M=2.08:
  R ≈ 13.113 km

DD2 f=300 Hz, M=2.08:
  R ≈ 12.634 km
  ΔR ≈ -0.478 km
```

Source file:

```text
data/b5-jm-figure4-target-extraction.csv
```

Output file:

```text
data/b5-jm-lambda-i-proxy.csv
```

---

## 2. Proxy formulas

Compactness:

```text
C = GM / (Rc²)
```

Tidal deformability proxy:

```text
Λ = (2/3) k₂ C⁻⁵
```

For this first pass:

```text
k₂ = 0.09 held fixed
```

Moment-of-inertia proxy:

```text
I ≈ 0.237 M R² (1 + 4.2C + 90C⁴)
```

reported in:

```text
10^45 g cm²
```

Guardrail:

```text
Holding k₂ fixed is a radius/compactness proxy, not a full tidal calculation.
A real run must recompute k₂ from the perturbed stellar model.
```

---

## 3. Results

| Model | Mass | Radius | Compactness | Λ proxy | ΔΛ | I proxy | ΔI |
|---|---:|---:|---:|---:|---:|---:|---:|
| DD2 pure | 1.40 | 13.230 km | 0.1563 | 644.0 | baseline | 1.975 | baseline |
| DD2 f=300 | 1.40 | 12.635 km | 0.1636 | 511.6 | -20.6% | 1.845 | -6.6% |
| DD2 pure | 2.08 | 13.113 km | 0.2342 | 85.1 | baseline | 3.800 | baseline |
| DD2 f=300 | 2.08 | 12.634 km | 0.2431 | 70.7 | -17.0% | 3.654 | -3.8% |

---

## 4. Interpretation

The DD2 f=300 Hz lane does not just move radius. It moves the two next observables in the expected direction:

```text
negative ΔR
→ higher compactness
→ lower Λ
→ lower I
```

For the lower-mass/BNS proxy:

```text
ΔR ≈ -0.595 km
ΔΛ ≈ -20.6%
ΔI ≈ -6.6%
```

For the J0740-like high-mass point:

```text
ΔR ≈ -0.478 km
ΔΛ ≈ -17.0%
ΔI ≈ -3.8%
```

This is a regular pattern. It is not a random artifact of one radius read.

---

## 5. What the framework now says

The B5 lane has become:

```text
rotation-induced torsion
→ negative compactification
→ lower tidal deformability
→ lower moment of inertia
```

The live prediction is now sharper:

```text
If this torsion lane is real, its best observational footprint is not only a smaller radius.
It should also suppress Λ and I relative to the GR/DD2 baseline,
with the suppression source-scaled by rotation/current.
```

---

## 6. What still blocks final status

Still missing:

```text
1. author/source numerical data;
2. full k₂ recomputation;
3. full I recomputation from the stellar model, not universal-relation proxy;
4. real posterior comparison for J0740, GW170817/BNS, and J0952;
5. source-scaling check across rotation values, not just f=300 Hz.
```

So the status upgrades only to:

```text
candidate observational pipeline with proxy Λ/I support
```

not to:

```text
validated prediction
```

---

## 7. Next step

Run the same proxy for all extracted DD2 rotation rows:

```text
pure
f=100 Hz
f=300 Hz
Ω=0.1 Ω_Kep
Ω=0.2 Ω_Kep where mass target exists
```

Then check monotonic source scaling:

```text
rotation/source increases
→ |ΔR| increases
→ |ΔΛ| increases
→ |ΔI| increases
```

If that monotonicity holds, B5 gets a clean source-scaling lane.
