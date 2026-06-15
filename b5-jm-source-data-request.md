# B5 — Jockel-Menger Source Data Request

*Working draft, June 2026.*

Status: data-acquisition step for the B5 torsion application lane.  
Purpose: get actual mass-radius/source rows for Jockel & Menger Fig. 4 rather than hand-digitizing the plot.  
Grade: operational request note.

---

## 1. Why we need the source data

The B5 gate selected:

```text
negative, source-scaled compactification
```

Jockel & Menger 2024 is the best sign/magnitude anchor because it reports rotation-induced torsion decreasing neutron-star radii by up to about `900 m`.

But the current in-repo gate cannot finish until we have actual rows:

```text
mass
radius without torsion
radius with rotation-induced torsion
rotation rate / source parameter
EOS
central density
mass shift
```

The plot-level claim is enough to identify the lane. It is not enough to run the J0740/BNS gates numerically.

---

## 2. Best source-data targets

### 2.1 Highest value

```text
Raw data behind Fig. 4:
  Mass-radius curves for DD2 and APR
  pure GR baseline
  f = 100 Hz / 200 Hz / 300 Hz curves
  Ω = 0.1, 0.2, 0.3 Ω_Kep curves
```

Minimum rows needed:

```text
M ≈ 1.4 M_sun
M ≈ 2.08 M_sun
near maximum mass / cutoff
```

### 2.2 Useful if raw data unavailable

```text
Numerical script/notebook used to generate Fig. 4
EOS tables / polytrope parameters
rotation-induced torsion formula implementation
sample output CSVs
```

### 2.3 Fallback

```text
High-resolution PDF / vector figure extraction
manual digitization using WebPlotDigitizer or equivalent
```

---

## 3. Where to look first

1. arXiv source package.

The arXiv page exposes a TeX source link. The source package may include the figure PDFs/EPS files but may or may not include the underlying data. The arXiv page lists the paper and exposes both PDF and TeX Source links. The abstract reports the sign/magnitude result directly: smaller radii/masses, higher central densities, realistic microphysical spin negligible, and rotation-induced radius decrease up to about `900 m`.

2. Physical Review D article page / supplementary materials.

The paper was published as:

```text
Phys. Rev. D 110, 104022
```

Check whether PRD provides supplemental material or a data availability statement.

3. Author request.

If no data/code is attached, email the authors asking specifically for Fig. 4 numerical data or plotting scripts.

---

## 4. Draft author email

Subject:

```text
Request for numerical data behind Fig. 4 of Jockel & Menger 2024
```

Body:

```text
Dear Dr. Jockel and Dr. Menger,

I am studying the observational implications of torsion-induced corrections to neutron-star structure and am using your paper,
"Effect of Torsion on Neutron Star Structure in Einstein-Cartan Gravity" (Phys. Rev. D 110, 104022; arXiv:2406.05851), as a key reference.

Would you be willing to share the numerical data or plotting script behind Fig. 4, especially the mass-radius curves for the DD2 and APR EOS with rotation-induced torsion at the different rotation rates?

The columns most useful for my comparison would be:

- EOS
- rotation prescription / value
- gravitational mass
- radius without torsion
- radius with rotation-induced torsion
- central density, if available
- any mass shift or cutoff/stability marker used in the figure

I am particularly trying to compare the sign and magnitude of the radius shift against current neutron-star mass/radius and tidal-deformability constraints, so the raw curve data would be much more reliable than digitizing the figure.

Thank you for the paper and for any data or guidance you can share.

Best,
Sree Kotay
```

---

## 5. If we must digitize manually

Use the template:

```text
data/b5-jm-figure4-digitization-template.csv
```

Then run:

```text
python scripts/b5_jm_digitized_curve_gate.py
```

Target rows:

```text
DD2 pure / f=100 / f=300 / 0.1Kep / 0.2Kep / 0.3Kep
APR pure / f=100 / f=200 / 0.1Kep / 0.2Kep / 0.3Kep
```

Read points at:

```text
M ≈ 1.4 M_sun
M ≈ 2.08 M_sun, if the curve reaches it
near maximum mass / cutoff
```

---

## 6. Acceptance threshold

Jockel-Menger upgrades from sign/magnitude anchor to candidate B5 observational pipeline if raw data show:

```text
1. negative radius shift at relevant rotation/source values;
2. ΔR in the -0.5 to -0.9 km lane for high-source cases;
3. M ≈ 2.08 M_sun remains on a stable sequence;
4. corrected high-mass radii pass the J0740 window;
5. lower-mass/BNS proxy points do not obviously violate the tidal/radius window;
6. source scaling is monotonic or at least structured by rotation/current, not arbitrary fitting.
```

If these fail, the model remains:

```text
sign/magnitude support only
```

---

## 7. Immediate action

```text
Check arXiv source.
Check PRD supplementary material / data availability.
If no source rows exist, send the author email.
If no reply, digitize Fig. 4 manually.
```
