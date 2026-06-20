# B5 — Toy EOS Gate Readout

*Working draft, June 2026.*

Status: readout of the toy EOS curve gate.  
Purpose: decide which sign/magnitude/source-dependence lane is worth real EOS/Love-number/torsion modeling.  
Grade: triage conclusion only. Uses toy radius curves and working radius windows.

---

## 1. Setup

Toy baseline curves:

| curve | `R_GR(1.4 M_sun)` | `R_GR(2.1 M_sun)` | read |
|---|---:|---:|---|
| compact-soft | 11.8 km | 11.7 km | compact / lower-radius baseline |
| middle | 12.4 km | 12.3 km | middle baseline |
| bns-upper | 13.0 km | 13.4 km | near BNS upper edge; high-ish at J0740 |
| stiff-high-support | 13.4 km | 13.8 km | stiff/high-radius baseline |
| very-stiff-risk | 13.8 km | 14.2 km | likely tidal-risk unless corrected/source-dependent |

Working gates:

```text
J0740 radius window:
  11.79 km ≤ R_J0740 ≤ 15.01 km

BNS / population radius window:
  11.50 km ≤ R_BNS ≤ 13.50 km
```

Trial high-source torsion corrections:

```text
ΔR_high_source ∈ {-0.9, -0.5, 0, +0.5, +0.9} km
```

BNS source factor:

```text
0.00 = no torsion correction in BNS population proxy
0.25 = weak population source
0.50 = moderate population source
1.00 = same correction as high-source object
```

This source factor is only a stand-in for the real spin/current source function.

---

## 2. Main result

The toy gate selects a specific lane:

```text
stiff/high-radius baseline
+
negative torsion correction
+
weak-to-moderate BNS source factor
→ advance
```

The cleanest selected cases are:

| baseline curve | `R_GR(2.1)` | `ΔR_high_source` | `BNS factor` | `R_J0740_after` | `R_BNS_after` | gate |
|---|---:|---:|---:|---:|---:|---|
| stiff-high-support | 13.8 | -0.9 | 0.00 | 12.9 | 13.4 | best-negative-lane |
| stiff-high-support | 13.8 | -0.9 | 0.25 | 12.9 | 13.18 | best-negative-lane |
| stiff-high-support | 13.8 | -0.9 | 0.50 | 12.9 | 12.95 | best-negative-lane |
| stiff-high-support | 13.8 | -0.5 | 0.00 | 13.3 | 13.4 | best-negative-lane |
| stiff-high-support | 13.8 | -0.5 | 0.25 | 13.3 | 13.28 | best-negative-lane |
| stiff-high-support | 13.8 | -0.5 | 0.50 | 13.3 | 13.15 | best-negative-lane |

Interpretation:

```text
A high-radius/high-support baseline is not automatically dead
if the torsion correction is negative and source-dependent.
```

This is the B5-looking lane:

```text
spin/current-rich high-mass object receives the stronger correction;
BNS population receives weaker or moderate correction;
J0740 lands in range;
BNS proxy lands in range.
```

---

## 3. Very-stiff rescue cases

The very-stiff baseline is mostly BNS-risk. But a few cases survive if the negative correction reaches the population enough to lower the BNS proxy.

Selected very-stiff cases:

| baseline curve | `R_GR(1.4)` | `R_GR(2.1)` | `ΔR_high_source` | `BNS factor` | `R_J0740_after` | `R_BNS_after` | gate |
|---|---:|---:|---:|---:|---:|---:|---|
| very-stiff-risk | 13.8 | 14.2 | -0.9 | 0.50 | 13.3 | 13.35 | best-negative-lane |
| very-stiff-risk | 13.8 | 14.2 | -0.5 | 1.00 | 13.7 | 13.3 | best-negative-lane |

Interpretation:

```text
Very-stiff curves are not first choice.
They require either stronger population correction or enough source dependence to avoid BNS failure.
```

This is useful because it tells us what the real model must not do:

```text
It cannot simply hide a too-stiff EOS behind a correction that only affects J0740.
If the baseline is very stiff, the correction must also repair BNS/tidal radii.
```

---

## 4. What fails

### 4.1 Compact-soft + negative correction

Compact-soft curves fail J0740 when the correction is negative:

```text
R_GR(2.1) = 11.7 km
ΔR = -0.9 km → R_J0740_after = 10.8 km
```

Interpretation:

```text
Negative torsion is not generically good.
It only helps high-radius/high-support baselines.
```

### 4.2 Positive correction on high-radius baselines

High-radius baselines plus positive correction hit BNS risk quickly:

```text
stiff-high-support:
  R14 = 13.4 km
  ΔR = +0.5 km with BNS factor ≥ 0.25 → BNS fail or tidal risk

very-stiff-risk:
  already BNS-risk at baseline
  positive correction fails broadly
```

Interpretation:

```text
Positive population-wide correction is the wrong first lane.
```

### 4.3 Baseline-only very-stiff curves

Very-stiff baseline with no correction:

```text
R14 = 13.8 km
```

fails the working BNS window.

Interpretation:

```text
If very-stiff baselines survive at all, they need a negative correction that also reaches the population or relevant BNS source channel.
```

---

## 5. Source-dependence lesson

The source factor is the key.

If the correction is purely J0740-only:

```text
BNS factor = 0
```

then stiff-high-support works well:

```text
J0740 corrected down;
BNS baseline stays near upper allowed window.
```

But very-stiff-risk does not:

```text
BNS remains too large.
```

If the correction is moderately shared:

```text
BNS factor = 0.5
```

then very-stiff can sometimes be rescued.

So the real source law matters:

```text
ΔR_torsion = F(spin/current, EOS, M, rotation, coupling convention)
```

The ledger-positive model cannot use arbitrary object-specific offsets. It must explain why the high-mass/high-source object receives one correction and the BNS/population proxy receives another.

---

## 6. The first real modeling target

The toy gate says the first serious external model to look for or build is:

```text
A torsion model with negative radius / compactness correction
that is stronger in high spin/current or high-source compact stars
and weaker, but not necessarily zero, in lower-source BNS inspiral objects.
```

Required outputs:

```text
R(M, source)
Λ(M, source)
I(M, source)
Mmax(source)
ρc(M, source)
```

First model class to prioritize:

```text
stiff/high-radius GR baseline
R_GR(1.4 M_sun) ≈ 13.0–13.4 km
R_GR(2.1 M_sun) ≈ 13.4–13.8 km
with negative torsion correction ≈ 0.5–0.9 km at high source
and weaker/moderate correction in BNS proxy
```

Not first priority:

```text
compact baseline + negative correction
positive correction on high-radius baselines
very-stiff baseline unless correction also repairs BNS radius
```

---

## 7. Residual claim after the toy gate

The residual claim is now sharper:

```text
If B5 torsion is observationally live,
the first viable lane is not arbitrary torsion in neutron stars.

It is a negative, source-scaled compactification correction
that allows a high-support baseline EOS to satisfy both:
  J0740 high-mass radius
  and BNS/tidal compactness.
```

So the next question is not:

```text
Does torsion change neutron stars?
```

It is:

```text
Does any serious EC / Poincaré-gauge / torsion-phenomenology model
produce this sign/source profile without free fitting?
```

---

## 8. End of cheap gates

The cheap gates have done their job.

They show:

```text
1. The effect size is not absurdly small.
2. The sign matters.
3. Negative correction is the first viable lane.
4. Source dependence matters more than a global offset.
5. Stiff/high-support EOS curves are the right first target.
6. Positive population-wide corrections are lower priority / tidal-risk.
```

Next step must leave toy arithmetic and go to external model/literature work:

```text
Find or build a torsion neutron-star model with:
  negative radius correction,
  source scaling,
  EOS compatibility,
  and recomputed Λ/I/Mmax.
```

That is the end of the first in-repo triage pass.
