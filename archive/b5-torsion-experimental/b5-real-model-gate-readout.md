# B5 — Real Model Gate Readout

*Working draft, June 2026.*

Status: endpoint of the first B5 neutron-star application pass.  
Purpose: state what the model extraction shows and where the work must go next.  
Grade: model-screening conclusion, not observational conclusion.

---

## 1. What survived the whole pass

The B5 program started with a broad question:

```text
Could torsion show up in compact-object data?
```

The cheap gates narrowed that to:

```text
negative, source-scaled compactification
in high-mass / high-spin-current compact stars
with BNS/tidal compatibility
```

The real-model screen finds two external model anchors:

```text
Jockel & Menger 2024:
  observable sign/magnitude anchor

Vashistha, Gannouji & Ganguly 2026:
  source-routing anchor
```

They do not yet close the loop together.

---

## 2. Model gate table

| model | strongest match | strongest risk | gate | action |
|---|---|---|---|---|
| Jockel-Menger-2024 | negative radius correction up to about 0.9 km; same scale selected by toy gates | visible lane is rotation-induced; high-mass/tidal curves still need extraction | `G1-extract-curves` | extract mass-radius rows first |
| Vashistha-Gannouji-Ganguly-2026 | algebraic contorsion sourced by spin current; clean B5 source-routing | reported branch lowers maximum mass; may fail J0740/J0952 high-mass gate | `G2-source-clean-high-mass-risk` | extract Mmax/branch viability first |

---

## 3. What this means

The B5 torsion lane is live, but not yet confirmed even internally.

The reason it is live:

```text
There exists at least one current model with the right observable sign/magnitude:
  negative radius correction up to ~0.9 km.

There exists at least one current model with the right source-routing structure:
  non-propagating torsion / algebraic contorsion / spin-current source.
```

The reason it is not yet closed:

```text
The sign/magnitude model is less source-clean.
The source-clean model may hurt high-mass support.
Neither has yet been passed through the full J0740 + BNS + J0952 + Λ/I gate in our ledger.
```

---

## 4. End-state prediction

After this pass, the prediction is no longer vague.

Not:

```text
torsion changes neutron stars
```

Not:

```text
look for any mass-radius anomaly
```

But:

```text
If the B5 torsion cell is observationally live,
the first viable signature is a negative, source-scaled compactification correction
that is strong enough to affect high-source/high-mass stars,
but compatible with BNS tidal/radius constraints.
```

More operationally:

```text
R_obs(M, s) = R_GR(EOS, M) + ΔR_torsion(M, s)

where:
  ΔR_torsion < 0 in the promoted lane
  ΔR_torsion scales with spin/current source s
  high-mass support survives
  BNS tidal/radius constraints survive
```

---

## 5. Decision tree now

```text
1. Extract Jockel/Menger curves.

   If ΔR≈-0.5 to -0.9 km appears near relevant spin/source ranges
   and M≈2.08 survives:
     promote to real EOS/tidal gate.

   If effect exists only by arbitrary rotation-induced parameter choice:
     keep as sign/magnitude support, not B5-positive evidence.

2. Extract Vashistha/Gannouji/Ganguly curves.

   If compactification occurs while Mmax remains ≥ J0740/J0952 bounds:
     promote as source-clean candidate.

   If Mmax drops below observed high-mass pulsars:
     keep as formal source-routing support only.

3. If neither paper supplies both sign and source cleanliness:
     next target is a hybrid or new model:
       spin/current-routed negative compactification
       with high-mass and tidal survival.
```

---

## 6. What counts as the end of this phase

This phase ends here:

```text
The prediction lane has been reduced to a falsifiable model query.
```

The query:

```text
Does any serious torsion neutron-star model produce negative, source-scaled compactification
while preserving high-mass support and BNS tidal compatibility?
```

The current answer:

```text
Maybe.

One paper gives sign/magnitude.
One paper gives source-routing.
The combined requirement remains open.
```

That is a real endpoint. The next step is not more in-repo arithmetic. It is paper-table extraction or actual model computation.

---

## 7. Required next artifact if continuing

The next artifact should be one of these:

```text
A. Jockel-Menger numeric extraction table
   rotation rate, mass, R_GR, R_torsion, ΔR, central density, mass shift

B. Vashistha-Gannouji-Ganguly numeric extraction table
   coupling branch, Mmax_GR, Mmax_torsion, R(M), ΔR(M), binding energy, central density

C. A real TOV/Love-number notebook/script
   external EOS baseline + parameterized torsion correction + Λ/I recomputation
```

Without one of those, the cheap prediction engine has reached its limit.

---

## 8. Compact conclusion

```text
B5 is now a real model-search problem.

The best lane is:
  negative, source-scaled compactification.

The best sign/magnitude anchor is:
  Jockel & Menger 2024.

The best source-routing anchor is:
  Vashistha, Gannouji & Ganguly 2026.

The missing combined object is:
  a model that has both,
  and survives J0740 + BNS + J0952 gates.
```
