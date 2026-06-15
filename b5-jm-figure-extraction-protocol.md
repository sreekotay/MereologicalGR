# B5 — Jockel-Menger Figure Extraction Protocol

*Working draft, June 2026.*

Status: bridge from text extraction to numeric curve extraction.  
Purpose: finish the Jockel-Menger application lane by specifying exactly what must be digitized from Fig. 4 and how it will be gated.  
Grade: extraction protocol. No claim of completed digitization.

---

## 1. Source figure

Target:

```text
Jockel & Menger 2024, Fig. 4
```

Figure caption states:

```text
Mass-radius relations of different neutron stars with rotation-induced torsion effects
computed using the upper-limit prescription from Eq. (51) and Eq. (52).
```

Relevant curve families:

```text
DD2 EOS:
  Pure DD2
  f = 100 Hz
  f = 300 Hz
  Ω = 0.1 Ω_Kep
  Ω = 0.2 Ω_Kep
  Ω = 0.3 Ω_Kep

APR EOS:
  Pure APR
  f = 100 Hz
  f = 200 Hz
  Ω = 0.1 Ω_Kep
  Ω = 0.2 Ω_Kep
  Ω = 0.3 Ω_Kep
```

Paper text immediately around Fig. 4 says:

```text
higher rotation rates → stronger torsion effects;
rotation-induced torsion decreases radius and gravitational mass;
modest rotation rates can change radius by several hundred meters;
current model probes up to a few hundred Hz or 20–30% of Keplerian rate;
some cutoff points are artifacts of the simplified upper-limit prescription;
results should be read as general trend with conservative error bars.
```

Conclusion section says:

```text
rotational torsion effects decrease gravitational mass and radius;
radius can be decreased by up to 900 m;
centrifugal effects would increase radius, so the physical result depends on balance.
```

---

## 2. What to digitize

Fill:

```text
data/b5-jm-figure4-digitization-template.csv
```

Required columns:

```text
source
panel_or_curve
EOS
rotation_spec
rotation_value
mass_Msun
R_GR_km
R_torsion_km
Delta_R_km
Delta_M_Msun
central_density_change
read_method
confidence
notes
```

Minimum useful digitization points:

```text
For each curve family, read at:
  M ≈ 1.4 M_sun
  M ≈ 2.08 M_sun if curve reaches it
  M near Mmax / cutoff if visible
```

For B5 gates, the key points are:

```text
DD2 f=100Hz at M≈2.08
DD2 f=300Hz at M≈2.08 if curve reaches it
DD2 0.1–0.3 Ω_Kep near M≈2.08
APR curves near M≈1.4 and high-mass reach, if any
```

---

## 3. How the gate will score it

Run:

```text
python scripts/b5_jm_digitized_curve_gate.py
```

The gate will compute:

```text
Delta_R_km_computed = R_torsion_km - R_GR_km
```

and score rows as:

```text
JM-D0-pending-digitization:
  missing numeric values

JM-D1-wrong-sign:
  no negative compactification

JM-D2-high-mass-pass:
  M ≥ 2.08 M_sun and R_torsion lies inside J0740 window

JM-D3-high-mass-radius-fail:
  high-mass point misses J0740 window

JM-D4-bns-proxy-pass:
  lower-mass point remains inside BNS radius proxy

JM-D5-bns-proxy-risk:
  lower-mass point outside BNS radius proxy
```

---

## 4. B5-positive condition

Jockel-Menger upgrades from sign/magnitude support to candidate observational pipeline only if digitized rows show:

```text
1. ΔR < 0 at relevant source strength.
2. ΔR roughly lives in the -0.5 to -0.9 km lane for high-source/high-mass cases.
3. A M≈2.08 M_sun point survives the J0740 radius gate.
4. Lower-mass/BNS proxy rows do not obviously violate the BNS radius/tidal gate.
5. The correction scales with rotation/current source rather than arbitrary fitting.
```

If not, Jockel-Menger remains:

```text
sign/magnitude anchor only
```

---

## 5. Current endpoint

The paper-text extraction is complete enough to identify the target.

The in-repo cheap gates are complete enough to identify the sign/source lane.

The remaining blocker is numeric figure extraction:

```text
Fig. 4 digitization or author/source data required.
```

Until then, the honest endpoint is:

```text
Jockel-Menger supports the B5 application lane qualitatively and by headline magnitude,
but cannot yet pass or fail the J0740/BNS gates numerically.
```
