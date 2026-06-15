# B5 — Jockel-Menger Source-Scaling Proxy Readout

*Working draft, June 2026.*

Status: source-scaling proxy from vector-extracted Figure 4 rows.  
Purpose: test whether the DD2 rotation-induced torsion lane has regular source scaling across radius, tidal deformability proxy, and moment-of-inertia proxy.  
Grade: proxy only. Not a full Love-number or moment-of-inertia computation.

---

## 1. What was tested

Previous pass promoted:

```text
DD2 f=300 Hz
```

This pass asks whether the pattern is regular across source strength.

Rows included:

```text
DD2 pure
DD2 f=100 Hz
DD2 f=300 Hz
DD2 Ω=0.1 Ω_Kep
DD2 Ω=0.2 Ω_Kep where mass target exists
```

Mass targets:

```text
M = 1.4 M_sun
M = 2.08 M_sun
```

Computed proxy outputs:

```text
compactness C = GM/(Rc²)
Λ proxy = (2/3) k₂ C^-5, with k₂ fixed at 0.09
I proxy = 0.237 M R² (1 + 4.2C + 90C⁴)
```

---

## 2. Source scaling at M = 1.4 M_sun

| DD2 row | R | ΔR | ΔΛ proxy | ΔI proxy | read |
|---|---:|---:|---:|---:|---|
| pure | 13.230 km | 0.000 | 0.0% | 0.0% | baseline |
| f=100 Hz | 13.152 km | -0.079 | -2.9% | -0.9% | mild |
| Ω=0.1 Ω_Kep | 13.070 km | -0.160 | -5.9% | -1.8% | mild/moderate |
| f=300 Hz | 12.635 km | -0.595 | -20.6% | -6.6% | strong |
| Ω=0.2 Ω_Kep | 12.615 km | -0.616 | -21.2% | -6.8% | strong, but high-mass cutoff |

Readout:

```text
At lower mass / BNS proxy,
stronger rotation-induced torsion produces larger negative ΔR,
larger Λ suppression,
and larger I suppression.
```

This is exactly the source-scaling shape B5 needs.

---

## 3. Source scaling at M = 2.08 M_sun

| DD2 row | R | ΔR | ΔΛ proxy | ΔI proxy | read |
|---|---:|---:|---:|---:|---|
| pure | 13.113 km | 0.000 | 0.0% | 0.0% | baseline |
| f=100 Hz | 13.052 km | -0.060 | -2.3% | -0.5% | mild |
| Ω=0.1 Ω_Kep | 12.927 km | -0.186 | -6.9% | -1.5% | mild/moderate |
| f=300 Hz | 12.634 km | -0.478 | -17.0% | -3.8% | strong, J0740 pass |

Readout:

```text
At the J0740-like mass,
the source-scaling pattern remains regular:
stronger torsion gives stronger compactification and stronger Λ/I suppression.
```

The strongest high-mass usable row is still:

```text
DD2 f=300 Hz:
  ΔR ≈ -0.478 km
  ΔΛ ≈ -17.0%
  ΔI ≈ -3.8%
```

---

## 4. What this shows

The data are regular in the way the framework needs:

```text
rotation/source increases
→ radius decreases
→ compactness increases
→ Λ proxy decreases
→ I proxy decreases
```

This turns the B5 candidate from a one-row coincidence into a structured lane.

Before:

```text
DD2 f=300 Hz might be a useful candidate.
```

Now:

```text
DD2 rotation-induced torsion shows a regular source-scaling pattern
across R, Λ proxy, and I proxy.
```

---

## 5. What the paper explains vs what B5 extracts

Paper explanation:

```text
rotation-induced torsion competes with centrifugal effects;
torsion decreases radius and gravitational mass;
centrifugal effects increase radius;
net behavior depends on which dominates.
```

Measurement / Figure 4:

```text
DD2 curves shift left/down with stronger torsion source;
f=300 Hz remains high-mass viable;
strong Ω-fraction curves may terminate early / cutoff.
```

B5 extraction:

```text
The viable observational lane is the part where torsion dominates enough to compactify,
but not so much that high-mass support or BNS compatibility fails.
```

---

## 6. Current status

The B5 lane now has:

```text
sign:
  negative compactification

source scaling:
  regular across f=100, Ω=0.1, f=300 / Ω=0.2 rows

high-mass candidate:
  DD2 f=300 Hz at M≈2.08 survives

BNS proxy candidate:
  DD2 f=300 Hz and Ω=0.2 at M≈1.4 remain inside proxy radius window

secondary observables:
  Λ proxy and I proxy both decrease in the expected direction
```

Status upgrade:

```text
candidate observational pipeline
→ candidate observational pipeline with regular proxy source scaling
```

Still not final:

```text
k₂ is fixed;
I uses a universal-relation proxy;
source data are vector-extracted, not author raw tables;
full posterior comparison still owed.
```

---

## 7. Next hard step

The next honest step is no longer another proxy.

It is one of:

```text
1. Get EC-Solver raw data / reproduce Figure 4 from source.
2. Recompute Love number k₂ and Λ along the torsion-modified sequence.
3. Recompute moment of inertia from the stellar model.
```

The proxy phase is complete.

If continuing in-repo without external solver work, the next artifact should be:

```text
b5-jm-observational-pipeline.md
```

with the candidate stated as:

```text
DD2 + rotation-induced torsion near f≈300 Hz
predicts lower R, lower Λ, and lower I
for high-source compact stars,
with source-scaled suppression visible already in Figure 4 proxy extraction.
```
