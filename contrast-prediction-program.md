# Contrast-Class Prediction Program

*Working draft, June 2026.*

Status: outward-facing application program.  
Purpose: turn the framework into contrast experiments and residual-routing tests at subatomic, laboratory, astrophysical, and cosmological scales.  
Grade: prediction-program scaffold. Mostly constraint predictions; one currently live generative/nonzero lane: spin/current → torsion burden.

Core thesis:

```text
The framework becomes predictive by constraining contrasts.
It does not only ask where meaning belongs;
it says which contrasts should survive measurement.
```

A prediction can have several forms:

```text
X should change under knob A but not knob B.
Y should vanish after accounting C.
Z, if nonzero, should scale with D rather than E.
An apparent extra term should collapse into an already-priced term.
```

So the outward program is not a search for slogans. It is a search for controlled contrasts:

```text
same baseline
+ one role-knob varied
→ predicted residual shape
```

---

## 1. Prediction grammar

Each application should be written in this form:

```text
baseline:
  what standard physics already prices

role-knob:
  what the framework says is the live distinction

forbidden knob:
  what should not matter once standard physics is accounted

observable:
  the measured number, residual, scaling, or formal term

prediction:
  zero residual, scaling route, or forbidden-term collapse

failure:
  what would actually make the framework wrong or weaker
```

The three prediction types:

```text
zero-residual prediction:
  ε = 0

scaling-route prediction:
  residual, if nonzero, scales with X rather than Y

forbidden-term prediction:
  no independent term of type Z is allowed;
  apparent Z must route to an already-priced structure
```

---

## 2. Master contrast table

| ID | Scale | Arena | Baseline held fixed | Role-knob varied | Forbidden / non-live knob | Predicted contrast | Result type |
|---|---|---|---|---|---|---|---|
| C1 | subatomic/lab | accelerated detector / Unruh-like response | field state and detector model class | worldline, acceleration profile, coupling, switching, detector gap | invariant in-flight particle bath | response changes with pullback/coupling; no detector-independent bath residual | zero-residual + response-routing |
| C2 | subatomic/lab | Quantum Darwinism / SBS | global state and redundancy diagnostics | uptake operation, POVM, fragment access, threshold, coarse-graining | record redundancy alone as constituted information | objectivity metrics improve with redundancy; constituted info changes with uptake/application | contrast/uptake residue |
| C3 | subatomic/lab | virtual exchange / near-field / evanescent systems | interaction kernel / field theory | endpoint uptake and observable commutators | carrier-like in-flight information in virtual exchange | influence-kernel may extend; constituted info remains endpoint/observable-constrained | forbidden-term |
| C4 | subatomic/lab analogue | spin-current / torsion-like materials | energy density / material platform | spin polarization, spin current, defect/strain/torsion analogue | scalar energy density alone | effective translational-closure residual tracks spin/current structure | analogue scaling-route |
| C5 | astrophysical | neutron stars / compact objects | mass/EOS family as much as possible | spin/current, angular momentum, retained spin source | mass-energy density alone | residual, if live, scales with spin/current and routes through torsion/contortion | nonzero scaling-route |
| C6 | cosmological | CMB temperature-redshift | standard photon/cosmology/thermalization model | congruence/redshift | semantic/information content | `T(z)` follows standard redshift; no information-specific term | zero-residual |
| C7 | formal/cosmological | QES / holographic QEC / magic | generalized entropy accounting | code resource, area operator, backreaction, edge structure | constituted info living on QES/null surface | extra terms route to geometry/reconstruction/backreaction, not QES-constitution | forbidden-term |
| C8 | horizon/analogue/cosmology | Hawking / horizon thermality | field theory near horizon | surface gravity / access structure / detector congruence | null-generator storage of constituted info | thermality/access can change; no null in-flight constitution term | forbidden-term + response-routing |
| C9 | lab/space/engineering | information-specific redshift | carrier frequency, potential difference, clocks, channel | code semantics, compression, redundancy, recoverability | information content as gravitational frequency source | no semantic/code-dependent redshift residual | zero-residual |

---

## 3. Subatomic and laboratory contrasts

### 3.1 Accelerated detector / Unruh-like response

Baseline:

```text
QFT detector response from field correlations pulled back to a detector worldline.
```

Role-knobs:

```text
acceleration profile
trajectory / congruence
coupling strength
coupling window
switching function
detector gap
boundary/cavity condition
multi-detector timing and separation
```

Forbidden knob:

```text
invariant in-flight particle bath
```

Prediction:

```text
response should price through worldline pullback + coupling + detector parameters;
no detector-independent bath residual should remain.
```

Numerical residual form:

```text
Response_data
  = Response_pullback+coupling+switching+gap+geometry
    · (1 + ε_invariant-bath)

Prediction:
  ε_invariant-bath = 0
```

Useful arenas:

```text
CERN NA63-style channeling radiation stress cases
high-intensity laser/electron acceleration regimes
circuit QED analogues
optical cavities
moving-mirror analogues
BEC analogue horizons
circular detector setups
```

Failure:

```text
a robust detector-independent thermal particle-bath term is required
after all pullback/coupling/switching/trajectory effects are accounted.
```

Framework read:

```text
Unruh is not a proof of constituted information in flight.
It is a worldline-indexed response rendering of phase-bearing relatedness.
```

---

### 3.2 Quantum Darwinism / SBS / objectivity

Baseline:

```text
environmental redundancy and objectivity diagnostics exist.
```

Role-knobs:

```text
fragment access
measurement operation
POVM choice
coarse-graining
threshold
application scale
observer/device uptake
```

Forbidden knob:

```text
redundant record structure alone as constituted information
```

Prediction:

```text
Increasing redundancy sharpens record diagnostics.
It should not eliminate uptake/application residue.
```

Numerical/formal residual form:

```text
Constituted_information
  ≠ f(global state redundancy alone)

Constituted_information
  = f(record structure, uptake operation, threshold, application scale)
```

Metrics to track:

```text
redundancy R_δ
mutual-information plateau width
SBS trace distance / objectivity error
basis dependence
fragment accessibility
threshold sensitivity
```

Failure:

```text
a basis-intrinsic, convention-free, purely state-functional criterion
identifies constituted information without operation, threshold, or uptake.
```

Framework read:

```text
record structure can be state-functional;
constitution is operation/application-indexed.
```

---

### 3.3 Virtual exchange / near-field / evanescent systems

Baseline:

```text
interaction kernels and near-field correlations can have non-carrier-like support;
observable endpoint algebras still obey causal constraints.
```

Role-knobs:

```text
interaction region
boundary condition
near-field geometry
endpoint detector placement
observable chosen
record threshold
```

Forbidden knob:

```text
virtual carrier as flow-bearing information propagator
```

Prediction:

```text
Influence-kernel structure may be spatially extended or spacelike-looking.
Constituted information should remain endpoint/observable/record constrained.
```

Residual form:

```text
endpoint_signal_claim
  = kernel/correlation contribution
    + ε_virtual-carrier-info

Prediction:
  ε_virtual-carrier-info = 0
```

Useful arenas:

```text
evanescent-wave tunneling
near-field heat transfer
Casimir / van der Waals force measurements
tunneling-time experiments
QFT microcausality analyses
```

Failure:

```text
virtual exchange requires carrier-like flow-bearing information propagation,
not merely kernel-level influence and endpoint uptake.
```

Framework read:

```text
influence without carrier-flow is allowed;
information without endpoint uptake is not.
```

---

### 3.4 Spin-current / torsion-like laboratory analogues

Baseline:

```text
ordinary condensed-matter transport, strain, spin-orbit, defect, and topological effects.
```

Role-knobs:

```text
spin polarization
spin current
defect density
strain / torsion analogue
chirality / Weyl-node structure
```

Forbidden knob:

```text
scalar energy density alone as the explanatory variable
```

Prediction:

```text
If a torsion-like translational-closure analogue is present,
its residual should track spin/current/defect structure,
not energy density alone.
```

Useful arenas:

```text
Weyl / Dirac semimetals with strain/torsion analogues
spin-current transport systems
chiral materials
spin-polarized dense matter analogues
acoustic/phononic torsion analogues
```

Guardrail:

```text
Laboratory analogues are role-tests, not direct gravitational torsion detections.
```

Failure:

```text
all residuals track ordinary transport/strain/topology variables
with no independent spin/current-to-translational-closure analogue.
```

---

## 4. Astrophysical and cosmological contrasts

### 4.1 Neutron stars / compact objects: the primary nonzero lane

Baseline:

```text
GR + EOS + rotation + magnetic/crust/thermal corrections.
```

Role-knob:

```text
independent spin/current or angular-momentum source retained
```

Forbidden knob:

```text
mass-energy density alone
```

Prediction:

```text
If the torsion cell is live,
observable residuals should correlate with spin/current structure and route through
torsion/contortion pricing.
```

Observable residuals:

```text
ΔR
ΔI
ΔΛ
ΔM_max
Δρ_c
ΔE_bind
frame-dragging / precession correction
post-merger frequency shift
```

Residual form:

```text
Observable_data
  = Observable_GR+EOS+ordinary-rotation+ordinary-matter
    + Observable_torsion(spin/current)
    + noise/systematics

Prediction if live:
  Observable_torsion ∝ spin/current source structure

Prediction if hidden:
  Observable_torsion bounded below current sensitivity
```

Best contrast design:

```text
same EOS family fits slow / low-spin objects;
fast / high-spin objects show residuals;
residual sign/scale matches torsion-sector pricing;
ordinary EOS/magnetic/crust/thermal explanations do not absorb it.
```

Objects / channels:

```text
PSR J0740+6620:
  high mass + NICER/XMM radius + known ms spin

PSR J0030+0451:
  lower-mass NICER control

PSR J0952−0607:
  high-spin / high-mass stress case

GW170817-like BNS events:
  tidal-deformability / EOS constraints

future double-pulsar moment-of-inertia measurement:
  high-value ΔI discriminator

post-merger GW spectra:
  dense, hot, rotating remnant stress case
```

First sensitivity:

```text
Λ ~ k₂ / C⁵
C = GM/(Rc²)

holding k₂ and mass-response aside:
  ΔΛ/Λ ≈ 5 ΔR/R

for R ≈ 13 km, ΔR ≈ 0.9 km:
  ΔR/R ≈ 0.07
  ΔΛ/Λ ≈ 0.35
```

Failure:

```text
spin/current-correlated residuals are fully absorbed by EOS, magnetic, crustal,
thermal, ordinary rotation, or inference-prior effects;
no torsion/contortion improvement remains.
```

Important:

```text
Null results bound and weaken the bet.
They force torsion empty only with a role-level closure argument.
```

---

### 4.2 CMB temperature-redshift

Baseline:

```text
T_CMB(z) = T0(1+z)
```

Role-knob:

```text
congruence/redshift/rendered photon energy scale
```

Forbidden knob:

```text
information content / semantic constitution
```

Prediction:

```text
T_CMB(z) = T0(1+z)(1 + ε_info)
ε_info = 0
```

Common parametrization target:

```text
T_CMB(z) = T0(1+z)^(1−β)
```

Framework-specific expectation:

```text
β_info = 0
```

Useful arenas:

```text
SZ cluster measurements
high-z molecular / atomic absorbers
CMB spectral distortions
future CMB spectral missions
foreground/calibration tests
```

Failure:

```text
a nonzero deviation tracks information/constitution specifically,
not photon-number violation, energy injection, scattering, foregrounds,
calibration, non-adiabaticity, or nonstandard cosmology.
```

Framework read:

```text
temperature/redshift is congruence rendering,
not in-flight information degradation.
```

---

### 4.3 QES / holographic QEC / magic / area operators

Baseline:

```text
S_gen = Area/4G + S_bulk + edge/reconstruction/backreaction terms
```

Role-knobs:

```text
code resource
nonlocal magic
area operator
state dependence
backreaction
edge/gauge structure
reconstruction map
```

Forbidden knob:

```text
constituted information living on QES/null surface
```

Prediction:

```text
extra formal resources should price geometry/reconstruction/backreaction,
not QES-constitution.
```

Forbidden residual:

```text
S_total
  = Area/4G
    + S_bulk
    + edge/reconstruction/backreaction terms
    + S_QES-constitution

Prediction:
  S_QES-constitution = 0
  S_null-constitution = 0
```

Useful arenas:

```text
holographic quantum error correction
area-operator codes
magic and non-stabilizer resources
edge-mode entropy
state-dependent reconstruction
island/QES formula refinements
```

Failure:

```text
a required entropy term is specifically constituted information on the QES/null surface
and cannot be reduced to area, bulk entropy, edge/gauge structure,
reconstruction, backreaction, or non-null microstructure.
```

Framework read:

```text
QES can be an accounting/reconstruction surface;
it should not be promoted to a constitution site without an extra term the framework forbids.
```

---

### 4.4 Horizon / Hawking / null thermality

Baseline:

```text
surface gravity / horizon access structure prices thermal response.
```

Role-knobs:

```text
surface gravity
horizon/access algebra
detector congruence
edge/gauge structure
reconstruction channel
```

Forbidden knob:

```text
null generator as storage site of constituted information
```

Prediction:

```text
horizon/access can price entropy and response;
constituted information should appear at uptake/reconstruction/non-null record structures,
not as in-flight null storage.
```

Residual form:

```text
S_horizon_accounting
  = area + edge/gauge + reconstruction + bulk terms
    + ε_null-storage

Prediction:
  ε_null-storage = 0
```

Useful arenas:

```text
analogue Hawking systems
algebraic QFT horizon thermality
soft hair / edge mode proposals
black-hole perturbation theory
island/QES formalism
```

Failure:

```text
constituted information must be located on the null generator itself,
not merely in area/edge/reconstruction/non-null uptake structures.
```

---

### 4.5 Information-specific gravitational redshift

Baseline:

```text
ν_B / ν_A = (p·u_B)/(p·u_A)
```

Role-knob:

```text
encoded semantic/information structure
```

Forbidden knob:

```text
semantic content as gravitational frequency source
```

Prediction:

```text
ν_B / ν_A
  = [(p·u_B)/(p·u_A)] · (1 + ε_info-redshift)

ε_info-redshift = 0
```

Test shape:

```text
hold fixed:
  carrier frequency
  potential difference
  channel noise
  detector model
  clock correction

vary:
  code semantics
  compression
  redundancy
  recoverability
  message content

prediction:
  no extra gravitational frequency/energy residual
```

Useful arenas:

```text
optical clock networks
satellite optical communication
QKD through gravitational potential differences
relativistic quantum information channels
deep-space optical links
```

Failure:

```text
semantic/coding structure produces reproducible gravitational frequency residual
after controlling for carrier, channel, detector, and clock physics.
```

Framework read:

```text
boring if correct;
valuable as a guardrail.
```

---

## 5. Which knobs matter where?

```text
Subatomic / lab:
  worldline
  coupling
  switching
  detector gap
  endpoint uptake
  POVM / threshold
  spin current / defect analogue

Astrophysical:
  spin/current
  mass/EOS
  angular momentum
  compactness
  tidal deformability
  moment of inertia

Cosmological/formal:
  congruence
  horizon/access algebra
  reconstruction map
  area operator
  code resource/magic
  edge/gauge structure

Forbidden as independent knobs:
  semantic information content in redshift
  invariant in-flight particle bath in Unruh
  redundant record alone as constituted information
  QES/null surface as constituted-information storage
  mass-energy alone for torsion if independent spin/current survives
```

---

## 6. Immediate action plan

### 6.1 B5 numerical table

Build the first actual number table:

```text
objects:
  J0740
  J0030
  J0952
  GW170817-like BNS channels
  future double-pulsar I measurement
  post-merger spectra

columns:
  M
  R
  spin frequency / period
  Λ or I if available
  EOS family
  torsion source model
  ΔR target
  ΔΛ sensitivity
  ΔI target
  source split: intrinsic-spin vs rotation-induced
  current status
```

### 6.2 NA63 / Unruh stress note

Question:

```text
Do channeling/Unruh interpretations actually support response-routing,
or do they smuggle intrinsic-bath language?
```

Output:

```text
model-comparison table:
  classical / quasi-classical / Unruh-like / bath-language
  variables controlled
  residual claimed
  framework status
```

### 6.3 QES/magic frontier note

Question:

```text
Are extra quantum resources in holographic codes reconstruction/area/backreaction-priced,
or constitution-priced?
```

Output:

```text
formal residual table:
  area operator
  state dependence
  nonlocal magic
  edge modes
  backreaction
  forbidden QES-constitution term
```

### 6.4 QD/SBS test-design note

Question:

```text
Can objectivity metrics eliminate uptake/application threshold,
or only sharpen record diagnostics?
```

Output:

```text
contrast table:
  redundancy held fixed / varied
  POVM varied
  threshold varied
  fragment access varied
  constitution criterion tested
```

---

## 7. Compact program

```text
The framework predicts contrast classes.

Spin/current contrast:
  Hold mass/EOS approximately fixed; vary spin/current.
  Prediction: torsion-candidate residual tracks spin/current.

Worldline/coupling contrast:
  Hold field state fixed; vary detector trajectory/coupling.
  Prediction: response changes there; invariant bath residual stays zero.

Redundancy/uptake contrast:
  Hold environmental redundancy high; vary uptake/threshold/coarse-graining.
  Prediction: constituted information changes with uptake, not redundancy alone.

Geometry/reconstruction contrast:
  Vary QEC code resources/backreaction/area operators.
  Prediction: extra terms route to geometry/reconstruction, not QES-constitution.

Congruence/semantic contrast:
  Hold photon/channel physics fixed; vary information content.
  Prediction: no information-specific redshift or CMB-temperature residual.
```

This is the application thesis:

```text
Constraining the contrast is the prediction engine.
```
