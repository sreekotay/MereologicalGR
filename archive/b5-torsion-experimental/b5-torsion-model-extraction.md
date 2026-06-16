# B5 — Torsion Model Extraction

*Working draft, June 2026.*

Status: literature/model extraction after the cheap gates.  
Purpose: identify whether existing torsion neutron-star work already has the sign/source profile selected by the B5 triage pass.  
Grade: outward model-screening note. This is not a derivation and not a final observational claim.

---

## 1. Result of the in-repo triage

The cheap gates selected this lane:

```text
stiff/high-support baseline EOS
+
negative radius / compactification correction
+
spin/current source scaling
+
BNS/tidal compatibility
```

More compactly:

```text
negative, source-scaled compactification
```

The model we now need is not generic torsion. It must satisfy:

```text
1. sign:
   radius / compactness correction should be negative in the first viable lane

2. source:
   correction should be tied to spin/current or angular momentum source,
   not arbitrary object-by-object fitting

3. compatibility:
   must survive J0740 high-mass radius and BNS tidal/radius constraints

4. outputs:
   should recompute R, Λ, I, Mmax, central density, or enough of them
   to compare with compact-object data
```

---

## 2. Existing model candidates

### 2.1 Jockel & Menger 2024 — Einstein-Cartan rotation-induced torsion

Reference:

```text
Cédric Jockel and Leon Menger,
"Effect of Torsion on Neutron Star Structure in Einstein-Cartan Gravity",
arXiv:2406.05851.
```

Extracted model read:

```text
framework match:
  strong sign match for the first lane

source lane:
  two lanes separated:
    microphysical spin
    macroscopic rotation / angular momentum

reported sign:
  torsion generally leads to smaller radii and masses, higher central densities

visible effect:
  realistic microphysical spin has no relevant influence
  rotation-induced torsion can decrease radius by up to about 900 m

extra qualitative effect:
  torsion-induced spin-up or spin-down depending on competition with centrifugal effects
```

B5 status:

```text
This is the best current sign match.
It lands almost exactly on the toy gate's promoted negative lane:
  ΔR ≈ -0.9 km
```

Caution:

```text
The clean intrinsic-spin EC lane appears hidden/negligible in their realistic treatment.
The visible lane is rotation-induced and therefore less cleanly tied to the minimal spin-current story.
```

Use:

```text
Promote as the first concrete model to extract numerically.
```

Needed extraction:

```text
- Which rotation rates produce ΔR ≈ -0.5 km and -0.9 km?
- What masses/EOS/polytropes were used?
- How does ΔR scale with angular velocity or angular momentum?
- Are Λ or I computed, or must we estimate from R/I relations?
- Does the model preserve high-mass support?
```

---

### 2.2 Vashistha, Gannouji & Ganguly 2026 — Poincaré gauge quadratic torsion

Reference:

```text
Chaitanya Vashistha, Radouane Gannouji, Apratim Ganguly,
"Neutron stars in Poincaré gauge gravity with quadratic torsion",
arXiv:2606.09786.
```

Extracted model read:

```text
framework match:
  strong algebraic source-routing match

source lane:
  spin current / Weyssenhoff fluid

machinery:
  torsion non-propagating;
  contorsion equation algebraic;
  solve contorsion in terms of spin current;
  reduce to effective Riemannian Einstein equations with spin-squared effective-fluid corrections

reported branch:
  positive effective spin-spin coupling branch

reported effects:
  more compact stellar configurations
  lower maximum mass
  reduced binding energy relative to GR sequence
  spin-correlation anisotropy negligible for their smooth weak-polarization profiles
```

B5 status:

```text
This is the best source-routing match.
It directly prices the missing B5 cell as algebraic contorsion sourced by spin current.
```

Caution:

```text
The branch they report reduces maximum mass.
That may be a problem for the J0740/J0952 high-mass support gate unless the EOS/couplings/source profile compensate.
```

Use:

```text
Promote as the first formal/source-clean model to study,
but require high-mass-support check before treating it as observationally viable.
```

Needed extraction:

```text
- What ΔR is produced for DD2 EOS at M ≈ 2.1 M_sun?
- How much does Mmax drop?
- Does any coupling branch preserve Mmax ≥ 2.08 M_sun, preferably ≥ 2.2 M_sun?
- Can the compactification be negative-radius helpful without killing high-mass support?
- Are Λ and I available or derivable from their sequence?
```

---

## 3. Comparison against B5 gate

| Model | Sign match | Source match | Magnitude match | High-mass risk | BNS/tidal readiness | B5 status |
|---|---|---|---|---|---|---|
| Jockel & Menger 2024 | strong: smaller radii | medium: rotation-induced visible; microphysical hidden | strong: up to ~900 m | unknown / must extract | unknown; no full Λ gate yet | first numerical extraction target |
| Vashistha et al. 2026 | strong: more compact | strong: spin-current algebraic contorsion | unknown from abstract | high: lowers Mmax in reported branch | unknown; Λ/I extraction needed | first source-clean formal target |

Readout:

```text
The two best candidates split the job:

Jockel/Menger gives the right observable sign and magnitude.
Vashistha/Gannouji/Ganguly gives the cleaner source-routing structure.
```

So the next real B5 step is not to choose one prematurely. It is to extract both into the same gate:

```text
J0740 pass?
BNS pass?
Mmax pass?
source-scaling pass?
free-knob fail?
```

---

## 4. Anchoring observational gates

### 4.1 J0740

Working anchor:

```text
M = 2.08 ± 0.07 M_sun
R_eq = 12.92^{+2.09}_{-1.13} km
```

Use:

```text
first high-mass radius calibration gate
```

Pass condition:

```text
model sequence can place a ≈2.1 M_sun object inside the radius posterior
without arbitrary per-object fitting.
```

### 4.2 J0030

Working anchor:

```text
original 2019 NICER analyses: M ~ 1.3–1.4 M_sun, R ~ 13 km
updated analysis: multimodal / model-dependent; possible solutions around
  [1.4 M_sun, 11.5 km]
  and [1.7 M_sun, 14.5 km]
```

Use:

```text
control only until the source row is cleaned.
```

Pass condition:

```text
same torsion source law does not overfit J0740 while breaking lower-mass controls.
```

### 4.3 J0952

Working anchor:

```text
M_NS ≈ 2.35 ± 0.17 M_sun
spin frequency ≈ 707 Hz
```

Use:

```text
high-spin/high-mass stress gate;
not radius-ready.
```

Pass condition:

```text
model does not reduce Mmax below observed high-mass pulsars;
if high-spin radius/I data arrive, correction scales in right direction.
```

### 4.4 GW170817 / BNS tidal data

Working anchor:

```text
tidal deformability and radius constraints constrain the EOS/radius window.
Representative published analyses place R_1.4 in roughly the 12–13.5 km range
for many hadronic-EOS assumptions, while phase-transition/twin-star assumptions
can broaden allowed radii.
```

Use:

```text
population/tidal compatibility gate
```

Pass condition:

```text
torsion-shifted sequence survives Λ and radius constraints after k2/Love-number recomputation.
```

---

## 5. What to extract next, concretely

### 5.1 From Jockel & Menger 2024

Create a row table:

```text
rotation rate
mass
baseline radius
radius with torsion
ΔR
central density shift
mass shift
spin-up/down sign
EOS/polytrope parameters
```

Then ask:

```text
Does ΔR scale monotonically with angular momentum / spin source?
Does ΔR ≈ -0.5 to -0.9 km appear near observed millisecond spin rates?
Does the correction preserve M ≳ 2.08 M_sun?
Can the same source law be weak/moderate in BNS inspiral objects?
```

### 5.2 From Vashistha et al. 2026

Create a row table:

```text
quadratic-torsion couplings
spin-current profile
EOS used
Mmax_GR
Mmax_torsion
R_GR(M)
R_torsion(M)
ΔR(M)
central density
binding energy
anisotropy choice
```

Then ask:

```text
Is there a branch with compactification but acceptable high-mass support?
Does the spin-current profile create source scaling rather than a global shift?
Can Λ/I be computed from their sequences?
```

---

## 6. Decision after extraction

### Promote to real modeling if:

```text
negative ΔR exists at relevant masses;
source scaling is explicit;
Mmax remains compatible with J0740/J0952-style mass constraints;
BNS/tidal compatibility is not obviously broken;
Λ/I can be recomputed or estimated.
```

### Keep as formal support only if:

```text
source-routing is clean but high-mass support fails;
compactification exists but only in unrealistic profiles;
Λ/I cannot be connected to observable gates.
```

### Reject as B5-positive evidence if:

```text
effect is arbitrary coupling fit;
correction is not source-routed;
sign can be freely chosen to fit target;
EOS variation absorbs all improvement;
high-mass or BNS constraints fail broadly.
```

---

## 7. Current conclusion

The cheap gates did not dead-end. They landed on a real external target.

Current best statement:

```text
The B5 torsion bet has a live observational lane if — and only if —
existing torsion neutron-star models can produce negative, source-scaled compactification
while preserving high-mass support and BNS tidal compatibility.
```

Best candidates:

```text
Jockel & Menger 2024:
  sign/magnitude target

Vashistha, Gannouji & Ganguly 2026:
  source-routing target
```

Next step:

```text
Extract numeric tables from those papers.
Then run the same gates with real model rows instead of toy ΔR rows.
```
