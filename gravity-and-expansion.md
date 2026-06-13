# Gravity and Expansion

Status: working external-form note.  
Grade: lineage-witness candidate for the Hubble slot-count; clarifier for the field taxonomy; magnitude remains calibration-disowned.

This note states the framework's expansion result cleanly: what follows from the role carve, what is protected by GR identities, where Hubble tension can live, and what current theory classes are doing in the graph.

## 1. Starting role carve

The derivation starts from the existing role decomposition:

```text
space       = ordering + adjacency
time        = ordering + flow
gravity     = ordering + influence + energy-momentum
information = ordering + influence + flow
```

Gravity and information overlap in ordering + influence, but they are not fused. Gravity imports energy-momentum. Information requires flow-bearing constitution.

So an expanding universe is not information expanding, not photons losing information in flight, and not a semantic degradation of signals. It is a change in adjacency scale per flow:

```text
H = (1/a) da/dτ
```

Mereological reading:

```text
H = fractional adjacency-scale change per cosmic flow
```

This fixes the target role of `H0`: present adjacency-change per flow.

## 2. Immediate consequences

Expansion is first a statement about adjacency, not information.

Allowed:

```text
expansion changes adjacency relations over flow
carriers redshift under metric comparison
record arrival rates dilate by 1 + z
horizons change accessibility for a flow-bearing observer
```

Not allowed as first explanation:

```text
information expands
semantic content redshifts
photons lose information in flight
H contains a hidden information-loss term
```

The framework therefore predicts a null:

```text
ε_info-propagation = 0
```

Any information-like residual in cosmological propagation must first appear as an ordinary physical channel effect, detector threshold, opacity, scattering, lensing, selection, or record-constitution failure. It is not supplied by the role theory.

## 3. Protected identities

The expansion graph is gated by standard identities. These are not selected by the anomaly.

```text
H = (1/a) da/dτ
```

Target role: adjacency-change per flow.

```text
1 + z = a0 / a_emit
```

Cosmological redshift as scale/frame comparison.

```text
F = L / (4π D_L²)
```

Flux plus luminosity defines luminosity distance.

```text
μ = m - M = 5 log10(D_L / 10 pc)
```

Apparent magnitude plus absolute magnitude defines distance modulus.

```text
D_L = (1 + z)² D_A
```

Luminosity distance and angular diameter distance are reciprocally related under metric propagation and photon-number conservation.

```text
θ = r / D
```

Observed angle plus ruler size gives transverse distance.

These identities do not say the conditioners are safe. They say where the burden may not be placed unless the identity's assumptions independently fail.

Important distinction: Etherington distance duality is both a protected identity and an empirical test site. The identity protects the geometry conditional on metric propagation and photon-number conservation. Distance-duality tests probe whether the photon-conservation / opacity conditioner has failed. Those are different registers.

## 4. Exposed conditioners

Distance identities are protected. Distance conditioners are exposed.

The exposed non-identity edges include:

```text
Cepheid period-luminosity relation
TRGB tip luminosity
JAGB luminosity distribution
SN Ia standardization
anchor calibration
sample and host matching
local-flow correction
sound horizon / drag-scale constitution
ΛCDM bridge or dynamical expansion bridge
standard-siren inclination / host / detector conditioners
```

So the gap may trigger the audit, but the magnitude is not allowed to choose the edge. The edge is assigned by identity provenance and graph topology.

## 5. The Hubble slot-count

This is the framework-distinctive result.

The field already has a burden taxonomy for the Hubble tension: early-ruler changes, distance-ladder systematics, local-structure or void explanations, late-time expansion changes, and modified dynamics. The framework should not claim to invent that list.

Its contribution is the forced slot-count.

Under the FRW shared-congruence assumption, `H = (1/a) da/dτ` has one shared flow slot. A disagreement over `H0` can burden only:

```text
Slot 1: adjacency constitution
  local records become distances;
  early records become rulers.

Slot 2: ordering / transport bridge
  early structure is transported to present H0;
  local samples are indexed into a global scalar.
```

There is no third information/clock slot:

```text
No semantic-redshift slot.
No photon-fatigue slot.
No independent clock-flow correction.
No information-loss-in-flight term.
```

Flow is common. The clock does not create a third burden register unless the shared-congruence assumption itself fails.

## 6. Collision-room

The two-slot count could have failed.

Its collision-room is the shared-congruence assumption. If early and late measurements cannot be rendered against one common cosmic flow, then the two-slot count breaks and a third slot reopens.

In doc-3 language, this is the support-index problem:

```text
W(z)
```

A measured `H0` is not a pure scalar read directly from the universe. It is sampled through a redshift window, sky window, environment window, and local-flow correction. A local-void or cosmic-variance explanation is a claim that the support window does not render the same role-output as the global FLRW scalar.

So the third slot is not information. It is failure of the comparison congruence: the measurements do not share one cosmic-flow remainder.

## 7. Numerical burden projection

The framework does not compute a new `H0`. It assigns burden slots. External cosmology prices them.

Representative external numbers:

```text
Planck base ΛCDM:      H0 = 67.4 ± 0.5
SH0ES SMC anchor:      H0 = 73.17 ± 0.86
CCHP JWST TRGB:        H0 = 69.85
CCHP JWST JAGB:        H0 = 67.96
CCHP JWST Cepheids:    H0 = 72.05
CCHP JWST combined:    H0 = 69.96
```

The Planck-SH0ES ratio is:

```text
73.17 / 67.4 = 1.0856
```

So the full burden is:

```text
8.56% in H0
≈ 0.178 mag in local distance-modulus currency
```

For local distance constitution, the relevant conversion is:

```text
H0 ∝ 1 / D
Δμ = 5 log10(H_high / H_low)
```

Local conditioner comparisons:

```text
CCHP Cepheid / TRGB = 72.05 / 69.85 = 1.0315
  ≈ 3.15%
  ≈ 0.067 mag

CCHP Cepheid / JAGB = 72.05 / 67.96 = 1.0602
  ≈ 6.02%
  ≈ 0.127 mag

SH0ES SMC / CCHP combined = 73.17 / 69.96 = 1.0459
  ≈ 4.59%
  ≈ 0.097 mag

SH0ES SMC / CCHP Cepheid = 73.17 / 72.05 = 1.0155
  ≈ 1.55%
  ≈ 0.033 mag
```

Result: the local luminosity-conditioner block has real variance in the right currency. It is live. But simple HST/JWST crowding-style differences at roughly the few-hundredths-of-a-magnitude scale are too small to carry the full Planck-SH0ES gap alone. If the late block pays, it is likely a broader constitution block: stellar conditioner + SN Ia standardization + anchor/sample/host/pipeline choices.

For the early ruler / bridge slot, carrying the full Planck-SH0ES gap requires shrinking the sound horizon or drag ruler by roughly the inverse ratio:

```text
r_d,new ≈ r_d,Planck × (67.4 / 73.17)
```

Using `r_drag ≈ 147.09 Mpc`:

```text
r_d,new ≈ 135.5 Mpc
```

So the early-ruler solution pays about an 8% ruler-shrink burden.

This is a burden map, not a fit.

## 8. Comparison to current theory classes

Current Hubble-tension theories can be read as edge-moves on the graph.

```text
Distance-ladder systematics
  → late adjacency constitution
  → record → luminosity conditioner → adjacency magnitude

Early dark energy / pre-recombination changes
  → early adjacency-ruler constitution
  → shrink r_s or r_d so early records infer higher H0

Dynamical dark energy / late-time expansion changes
  → ordering / transport bridge
  → alter the flow-history or adjacency-history bridge from ruler records to present H0

Modified gravity / interacting dark sector / exotic species
  → gravity/model side
  → change energy-momentum import, ruler physics, growth, or bridge dynamics

Local void / cosmic variance
  → support-index failure W(z)
  → local measurement window does not sample the same scalar role-output as the global FLRW remainder

Photon fatigue / opacity / information loss
  → photon-path slot
  → graph-disfavored unless distance-duality, time-dilation, or photon-conservation tests independently fail
```

The framework agrees with the field's broad taxonomy but does not merely relabel it. The field lists possible solution realms. The framework derives why the live burden must fall into two slots under shared FRW flow, and why photon/information fixes are not legitimate first burdens.

## 9. Standard-siren fork

The forward discriminator is the standard-siren fork.

Standard sirens remove the late luminosity-constitution ladder. They do not remove all modeling inputs. Sirens still carry inclination-distance degeneracy, waveform modeling, detector calibration, lensing, host association, and low-redshift peculiar-velocity corrections.

But they are clean for the graph because they replace:

```text
photon record → luminosity conditioner → distance
```

with:

```text
GW waveform record → GR amplitude-distance identity → distance
```

The fork:

```text
Percent-level sirens high, ≳71:
  bill the early-ruler / ordering-bridge slot.

Percent-level sirens low, ≲69:
  bill the late luminosity-constitution slot.

Sirens varying by depth, direction, or environment:
  probe the slot-count itself.
```

The third branch is not merely another burden assignment. It is the observable form of the shared-congruence collision-room. If siren-inferred `H0` varies with depth, sky direction, or environment after known systematics are controlled, then the support-index `W(z)` is not rendering one common `H0` remainder. In that case the two-slot count is itself under pressure.

Clean firing of the third branch requires range, not merely precision. At low redshift, peculiar-velocity corrections sit on the same axis as `W(z)`, so depth-dependence and local velocity systematics do not separate cleanly. The discriminating sirens must reach deep enough that residual depth or sky structure reads the support window rather than the peculiar-velocity floor.

## 10. Grade

```text
Hubble edge taxonomy:
  convergent-with-field clarifier
  thin weight by itself

Hubble slot-count:
  lineage-witness candidate
  discounted-nonzero
  lineage clean because the role carve predates the Hubble contact

Collision-room:
  shared-congruence / W(z) support-index failure

Magnitude:
  type-1 kernel-barred
  calibration-disowned
  the framework assigns slots but cannot price the calibration kernel from inside

Forward edge:
  three-tine standard-siren fork
```

Chronology is not the criterion. The Hubble numbers being known in advance does not disqualify the result. The relevant criterion is lineage: the role carve used in the derivation existed before the Hubble contact. It did.

The ceiling is not retrodiction. The ceiling is that the magnitude is externally priced. The framework can say which graph-derived parts may bear the burden, and can state the structural collision-room. It cannot derive the numerical calibration kernel from inside.

## 11. Compact result

The Hubble tension does not show that distance, redshift, or information propagation is broken.

It shows a disagreement between identity-protected `H0` and non-identical constitution paths.

Under shared FRW flow, there are two burden slots and no third:

```text
adjacency constitution
ordering / transport bridge
```

The live forward test is the standard-siren fork. High sirens bill early ruler/bridge. Low sirens bill late luminosity constitution. Depth or direction dependence tests the shared-congruence assumption itself.

## References / external anchors

- Planck Collaboration, `Planck 2018 results. VI. Cosmological parameters`, arXiv:1807.06209.
- Freedman et al., `Status Report on the Chicago-Carnegie Hubble Program (CCHP): Three Independent Astrophysical Determinations of the Hubble Constant Using the James Webb Space Telescope`, arXiv:2408.06153.
- Riess et al., SH0ES SMC-anchor / JWST cross-check papers, including recent JWST Cepheid and JAGB comparisons.
- Dark Energy Survey Supernova Program, cosmological time-dilation measurement, arXiv:2406.05050.
- Di Valentino et al., `In the realm of the Hubble tension — a review of solutions`, Classical and Quantum Gravity, 2021.
- DESI DR2 / evolving-dark-energy analyses, 2025-2026.
- Standard-siren and TDCOSMO / GWTC-4 H0 analyses, 2026.