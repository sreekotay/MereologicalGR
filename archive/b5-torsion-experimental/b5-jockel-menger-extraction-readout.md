# B5 — Jockel-Menger Extraction Readout

*Working draft, June 2026.*

Status: Jockel-Menger extraction pass from abstract / arXiv text.  
Purpose: decide whether this paper is enough to advance the B5 torsion application lane, or whether it only provides sign/magnitude support.
Grade: extraction-gate note. Numeric figure/table extraction still required.

---

## 1. Extracted facts

Paper:

```text
Cédric Jockel and Leon Menger,
"Effect of Torsion on Neutron Star Structure in Einstein-Cartan Gravity",
Phys. Rev. D 110, 104022; arXiv:2406.05851.
```

Relevant extracted claims:

```text
1. Torsion is sourced either by microphysical spin or macroscopic angular momentum.

2. The paper uses a simplified polytropic model for microphysical spin.

3. It derives expressions for rotation-induced torsion and estimates effects
   for rotating neutron stars at different rotation rates.

4. Torsion generally leads to smaller radii and masses, but higher central densities.

5. Realistic microphysical spin models have no relevant influence on neutron-star structure.

6. Rotation-induced torsion can decrease radius by up to about 900 m,
   comparable to the centrifugal radius increase.

7. Depending on whether torsion or centrifugal effects dominate,
   the star can undergo torsion-induced spin-up or spin-down.
```

---

## 2. B5 gate result

The paper splits into three rows:

| row | lane | B5 status | gate |
|---|---|---|---|
| microphysical spin | intrinsic spin / spin-fluid | framework-clean but observationally hidden | formal note only |
| macroscopic angular momentum | rotation-induced torsion | best sign/magnitude match | advance to figure/table extraction |
| general torsion trend | qualitative EC trend | sign support | qualitative support |

The key row is:

```text
macroscopic angular momentum / rotation-induced torsion
ΔR ≈ -0.9 km
```

That matches the toy gate's selected lane:

```text
negative, source-scaled compactification
```

---

## 3. What this paper shows for this archive pass

It is enough to say:

```text
The B5 selected lane is not invented by the framework.
There is an existing EC neutron-star model family with the right sign
and a relevant magnitude scale.
```

It also shows:

```text
The clean intrinsic-spin route is probably not the first observational route.
```

So B5 should not claim:

```text
fermion spin density in realistic neutron-star matter will visibly change radii
```

It should claim:

```text
the first visible torsion lane, if any, is likely macroscopic-rotation/current routed,
not bare microphysical spin density.
```

---

## 4. What it does not establish yet

It does not yet establish:

```text
J0740 compatibility
BNS tidal compatibility
Mmax survival
Λ recomputation
I recomputation
source-law cleanliness beyond rotation-induced phenomenology
```

So the gate remains:

```text
JM-G1-promote-extract-curves
```

Meaning:

```text
extract figures/tables next,
then run real rows through the existing J0740/BNS gates.
```

---

## 5. Needed numeric extraction

From the paper or figures, extract:

```text
rotation rate
mass
R_GR
R_torsion
ΔR
central density shift
mass shift
spin-up/spin-down sign
EOS or polytrope parameters
```

Then compute:

```text
J0740 gate:
  is M ≥ 2.08 M_sun possible after torsion?
  does R land inside radius posterior?

BNS gate:
  does the same source law keep R_1.4 or tidal proxy inside bounds?

source law gate:
  does ΔR scale with angular momentum / current,
  or is it adjustable by construction?
```

---

## 6. Decision

Current decision:

```text
Jockel-Menger is the application lane.
```

But the witness grade is:

```text
sign/magnitude anchor, not full B5-positive witness yet.
```

Full B5-positive witness status would require:

```text
negative ΔR at relevant source strength;
source scaling;
high-mass survival;
BNS tidal compatibility;
Λ/I or enough structure to recompute them.
```

---

## 7. End of this extraction pass

This pass has reached its limit from abstract/arXiv text.

Current endpoint:

```text
Proceed to figure/table extraction from Jockel-Menger.
```

If the extracted curves show:

```text
ΔR ≈ -0.5 to -0.9 km near relevant spin/source ranges
and M ≥ 2.08 M_sun survives,
```

then the B5 lane upgrades from:

```text
live model-search problem
```

to:

```text
candidate observational-pipeline input.
```

If not, it remains:

```text
sign/magnitude support only.
```
