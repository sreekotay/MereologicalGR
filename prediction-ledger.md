# Prediction Ledger — Outward Tests and Residuals

*Working draft, June 2026.*

Status: outward-facing prediction ledger.  
Purpose: convert the framework into search targets, measurable residuals, and failure conditions.  
Grade: mixed. Some rows are zero-residual predictions; some are structural routing predictions; only torsion/spin-current currently offers a plausible positive nonzero numerical lane. Magnitudes remain externally priced unless explicitly marked as framework-owned.

Core discipline:

```text
Do not ask: where can the language be confirmed?
Ask: where is an active field already measuring a residual that the role split says should be
  zero,
  spin/current-scaled,
  worldline-indexed,
  reconstruction-priced,
  or uptake-dependent?
```

---

## 1. Ledger format

Each prediction should be tracked by:

```text
target:
  experimental / theoretical arena

observable:
  number, residual, scaling law, or formal term

standard baseline:
  what orthodox physics already predicts

framework residual:
  the extra term or routing variable the framework permits or forbids

expected sign / value:
  zero, nonzero, sign, monotonic relation, or scaling variable

current bound / status:
  known constraint or qualitative state

best dataset / literature lane:
  where to look now

failure condition:
  what would actually break or weaken the framework claim
```

---

## 2. Ranked outward targets

```text
1. Torsion / spin-current neutron-star observables
   Best positive nonzero chance.

2. Unruh / accelerated detector response and channeling stress cases
   Best lab-adjacent response-routing test.

3. Holographic QEC / QES / magic / area operators
   Best formal-theory discriminator.

4. Quantum Darwinism / spectrum broadcast structure / objectivity protocols
   Best record-vs-constitution discriminator.

5. CMB temperature-redshift and spectral-distortion constraints
   Cleanest cosmological zero-residual lane.

6. Information-specific gravitational redshift in communication channels
   Clean engineering null test.
```

---

## 3. Master ledger

| ID | Target | Observable | Standard baseline | Framework residual / routing | Expected value / sign | Best data / arena | Failure condition |
|---|---|---|---|---|---|---|---|
| P1 | Torsion / spin-gravity coupling | `ΔR`, `ΔI`, `ΔΛ`, `ΔM_max`, `Δρ_c`, binding-energy shift, frame-dragging/precession correction | GR + EOS + rotation + magnetic/crust/thermal modeling | independent spin/current retained → torsion-sector equation → contortion / observable shift | nonzero only if spin/current survives as independent source; scaling with spin/current, not mass-energy alone | NICER, pulsar timing, moment-of-inertia prospects, BNS tidal deformability, post-merger signals | residual fully absorbed by EOS/ordinary matter modeling; no independent spin-current torsion burden; or role-level forced-empty proof |
| P2 | Neutron-star torsion sensitivity | radius/tidal response to torsion-priced model | standard TOV/rotating-star model | `spin/current in → torsion burden out` | possible `ΔR` order sub-km to km in rotation-induced models; `ΔΛ/Λ ≈ 5ΔR/R` as first sensitivity estimate | J0740, J0030, J0952, GW170817-like BNS constraints | effect violates high-mass/radius/tidal constraints, or cannot be source-routed to torsion |
| P3 | Unruh / accelerated detector response | transition rate / spectrum / detailed balance / KMS parameter | QFT detector response from Wightman pullback to worldline | no invariant in-flight particle-bath residual; no pre-constituted record | `ε_invariant-bath = 0`; response prices through worldline pullback + coupling + switching + detector gap | circuit QED, cavities, moving mirrors, circular detectors, BEC analogues, NA63-style channeling stress cases | robust detector-independent particle bath term required; response independent of coupling/pullback/uptake in contradiction with role route |
| P4 | CMB temperature-redshift | `T_CMB(z)` deviation from adiabatic scaling | `T(z)=T0(1+z)` or parametrized `T(z)=T0(1+z)^(1−β)` | no information-specific thermal/redshift degradation | `ε_info = 0`; equivalently no framework-owned `β_info` | SZ clusters, high-z absorbers, spectral distortion measurements | deviation specifically tracks information/constitution rather than photon-number, thermalization, foregrounds, injection, calibration, or cosmology |
| P5 | Information-specific redshift | carrier redshift vs encoded semantic/compression content | GR/QFT redshift via `ν_B/ν_A=(p·u_B)/(p·u_A)` | no semantic/code/recoverability-dependent redshift term | `ε_info-redshift = 0` | optical clocks, satellite optical links, QKD, relativistic quantum information channels | same carrier/channel but different information content produces a reproducible gravitational frequency/energy residual |
| P6 | QES / holographic entropy | generalized entropy bookkeeping | `S=Area/4G+S_bulk+edge/reconstruction/backreaction terms` | forbidden independent constitution term on QES/null surface | `ε_QES-constitution = 0`; `ε_null-constitution = 0` | holographic QEC, area operators, edge modes, magic/state-dependence programs | a required entropy term exists only as constituted information on the QES/null generator, irreducible to allowed terms |
| P7 | Quantum Darwinism / SBS | redundancy `R_δ`, mutual-information plateau, SBS trace-distance/objectivity error | environment-as-witness redundant record diagnostics | record diagnostics do not equal constituted information without uptake/application threshold | uptake residue remains; no pure state-functional constitution criterion | photonic/NV/superconducting QD/SBS experiments; randomized measurement objectivity tests | basis-intrinsic, convention-free, purely state-functional criterion identifies constituted information without operation/uptake |
| P8 | Temperature / information separation | same-temperature states with different microstate/info; detector record thresholds | thermodynamic/statistical temperature as response/distribution parameter | temperature not identical to information; information requires ordered uptake into flow | `ε_temperature-is-information = 0` | thermodynamics, detector theory, nonequilibrium QFT, analogue Unruh/Hawking systems | temperature alone determines constituted information without record channel/coarse-graining/application threshold |
| P9 | Horizon / null constitution | entropy accounting at horizon/null generators | BH area entropy, edge modes, horizon algebra, Hawking/QES accounting | no constituted information living on null in-flight structure | `ε_horizon-null-constitution = 0` | black-hole information theory, algebraic QFT, soft hair/edge mode programs | nonzero information term lives specifically on null generator and cannot be accounted as area/edge/reconstruction/non-null microstructure |
| P10 | Virtual photon / microcausality | spacelike kernel support vs endpoint observable commutators | QED propagator support + microcausality of observables | influence-kernel without carrier-flow; no constituted information in virtual carrier | endpoint observables respect microcausality; no virtual-carrier information term | QFT foundations, scattering, near-field/evanescent analogues | virtual exchange requires carrier-like flow-bearing information propagation |

---

## 4. Priority row: torsion / spin-current neutron-star residuals

This is the best candidate for a positive nonzero numerical search.

Framework route:

```text
independent spin / angular-momentum current retained
→ torsion-sector equation live
→ torsion tensor / contortion / effective correction
→ neutron-star observable shift or bound
```

Numerical outputs to track:

```text
ΔR:
  radius shift

ΔI:
  moment-of-inertia shift

ΔΛ:
  tidal-deformability shift

ΔM_max:
  maximum-mass shift

Δρ_c:
  central-density shift

ΔE_bind:
  binding-energy shift

Δω_LT / frame-dragging:
  precession or dragging correction traceable to contortion
```

Core scaling prediction:

```text
observable residual should correlate with spin/current structure,
not mass-energy density alone.
```

Positive signal:

```text
same EOS family fits slow / low-spin objects normally,
but fast / high-spin objects require a correction,
and the correction's sign and scale match torsion-sector pricing.
```

Null / weakening:

```text
all spin/current-correlated residuals route through ordinary EOS,
magnetic, thermal, crustal, or rotation effects;
no torsion/contortion improvement remains.
```

Forced-empty requires more than null data:

```text
Persistent null results tighten bounds and weaken the live bet.
They force torsion empty only if paired with a role-level argument showing that
no independent spin-current torsion burden can survive the framework's allowed imports.
```

### 4.1 First numerical sensitivity

Tidal deformability is radius-sensitive:

```text
Λ ~ k₂ / C⁵
C = GM/(Rc²)
```

Holding mass and Love-number response aside for a first pass:

```text
ΔΛ / Λ ≈ 5 ΔR / R
```

For:

```text
R ≈ 13 km
ΔR ≈ 0.9 km
```

then:

```text
ΔR/R ≈ 0.07
ΔΛ/Λ ≈ 0.35
```

This is not a framework-owned prediction. It is a sensitivity target: sub-km to km-scale radius shifts are potentially large in tidal observables after real EOS/Love-number recomputation.

### 4.2 First object list

| Object / channel | Why it matters | First observable | Role in ledger |
|---|---|---|---|
| PSR J0740+6620 | high mass, NICER/XMM radius, known millisecond spin | `ΔR`, `ΔI`, high-mass support | first calibration target |
| PSR J0030+0451 | lower-mass NICER anchor | `ΔR(M,f)` | mass-dependence control |
| PSR J0952−0607 | high-spin/high-mass stress case | `ΔM_max`, `ΔR`, spin residual | extreme spin-current stress test |
| GW170817 / BNS events | tidal deformability / EOS constraint | `ΔΛ`, `R_1.4` | population/tidal constraint |
| Future double-pulsar `I` measurements | moment of inertia may distinguish EOS from spin-current corrections | `ΔI` | high-value discriminator |
| Post-merger GW spectra | dense, rotating, hot compact remnants | frequency shifts, damping, EOS/torsion residual | future high-density stress case |

---

## 5. Priority row: Unruh / accelerated response

The positive target is not the ordinary fact of acceleration/worldline dependence. Standard Unruh machinery already owns that.

The framework-positive edge is narrower:

```text
response, temperature, and record separate operationally;
intrinsic-bath / invariant in-flight-particle / pre-constituted-record readings fail
where pullback, coupling, and uptake models succeed.
```

Observable residual:

```text
response spectrum residual = data − pullback/coupling/recoil/trajectory model
```

Expected result:

```text
ε_invariant-bath = 0
ε_detector-independent-record = 0
```

Variables to perturb:

```text
acceleration profile
coupling window
switching function
detector gap
trajectory / congruence
multi-detector spacing and timing
cavity boundary conditions
```

Positive daylight:

```text
response varies with pullback/coupling/uptake model,
not with a detector-independent particle bath.
```

Candidate arenas:

```text
CERN NA63-style channeling stress cases
circuit QED
optical cavities
moving-mirror analogues
BEC analogue horizons
circular detector setups
```

Guardrail:

```text
Channeling or analogue evidence is not a PB-4-full proof.
It is useful only if it helps keep the layers separated:
  field/correlation/KMS structure before uptake;
  temperature as response rendering;
  constituted information at detector record uptake.
```

---

## 6. Priority row: QES / holographic QEC / magic

Framework target:

```text
S_total = Area/4G + S_bulk + allowed edge/reconstruction/backreaction terms
```

Forbidden residual:

```text
+ S_QES-constitution
+ S_null-constitution
```

Expected values:

```text
ε_QES-constitution = 0
ε_null-constitution = 0
```

Outward question:

```text
When holographic codes require extra resources beyond stabilizer entanglement,
do those resources price area operators, state dependence, reconstruction, edge modes,
and backreaction — or do they require constituted information living on QES/null surfaces?
```

Framework expectation:

```text
extra structure is geometry/reconstruction/backreaction-priced,
not constitution-priced.
```

Failure condition:

```text
A formal entropy term is required that cannot be reduced to area, bulk entropy,
edge/gauge structure, reconstruction, backreaction, or non-null microstructure,
and it is specifically constituted information on the QES/null surface.
```

---

## 7. Priority row: Quantum Darwinism / record vs constitution

Framework target:

```text
redundant environmental records ≠ constituted information
```

Observable / metric targets:

```text
redundancy R_δ
mutual-information plateau width
SBS trace-distance / objectivity error
fragment accessibility
basis dependence
observer/application threshold dependence
```

Expected pattern:

```text
more redundancy improves record diagnostics;
it does not eliminate uptake/application thresholds.
```

Failure condition:

```text
a basis-intrinsic, convention-free, purely state-functional criterion
identifies constituted information without operation, threshold, or uptake.
```

Good test design:

```text
hold global state diagnostics fixed as much as possible;
vary measurement operation / fragment access / threshold / coarse-graining;
ask whether constituted information changes.
```

Framework expectation:

```text
record structure can be state-functional;
constitution is operation/application-indexed.
```

---

## 8. Priority row: CMB temperature-redshift

Standard relation:

```text
T_CMB(z) = T0(1+z)
```

Deviation parametrization often used:

```text
T_CMB(z) = T0(1+z)^(1−β)
```

Framework read:

```text
temperature/redshift is congruence rendering,
not in-flight information degradation.
```

Framework residual:

```text
T_CMB(z) = T0(1+z)(1 + ε_info)
```

Prediction:

```text
ε_info = 0
```

Failure condition:

```text
A nonzero deviation tracks information/constitution specifically,
not photon-number violation, non-adiabatic cosmology, injection, foregrounds,
scattering, calibration, or thermalization physics.
```

Status:

```text
clean null lane;
not likely the first positive discovery channel.
```

---

## 9. Priority row: information-specific redshift

Standard relation:

```text
ν_B / ν_A = (p·u_B) / (p·u_A)
```

Framework residual:

```text
ν_B / ν_A = [(p·u_B)/(p·u_A)] · (1 + ε_info-redshift)
```

Prediction:

```text
ε_info-redshift = 0
```

Test shape:

```text
same carrier frequency / potential difference / noise / detector model
but different code semantics, compression, redundancy, or recoverability
→ no extra gravitational redshift term.
```

Candidate arenas:

```text
optical clock networks
satellite optical communication
QKD through gravitational potential differences
relativistic quantum information channels
deep-space optical links
```

Failure condition:

```text
semantic or coding structure produces a reproducible frequency/energy residual
after controlling for carrier, channel, detector, and clock physics.
```

Status:

```text
probably boring;
excellent guardrail.
```

---

## 10. What is actually framework-owned?

Framework-owned:

```text
which residual should be zero
which variable a live correction should scale with
which apparent positive signal is the wrong signal
which extra terms are forbidden by role discipline
which empirical silence only bounds versus forces-empty
```

Externally owned:

```text
Unruh coefficient
Einstein-Cartan / Poincaré-gauge torsion coupling
neutron-star EOS and Love-number response
QFT detector response integrals
holographic entropy formulae
CMB thermalization and spectral-distortion physics
GR redshift measurements
```

Most predictions are therefore of one of three types:

```text
zero-residual:
  ε = 0

scaling-route:
  residual ∝ spin/current rather than mass-energy alone

forbidden-term:
  no independent constitution term at null/QES/horizon/in-flight carrier
```

---

## 11. Immediate next work items

1. **Build the B5 neutron-star table numerically.**

```text
rows:
  J0740, J0030, J0952, GW170817, future I measurement, post-merger spectra

columns:
  M, R, f/P, Λ/I if available, EOS family, predicted torsion channel,
  ΔR target, ΔΛ sensitivity, source split, current status
```

2. **Make a mini-note for NA63 / Unruh channeling.**

```text
question:
  Is NA63 evidence actually response-routing evidence,
  or does it smuggle intrinsic-bath language?
```

3. **Make a QES/magic frontier note.**

```text
question:
  Are extra quantum resources in holographic codes reconstruction/area/backreaction-priced,
  or constitution-priced?
```

4. **Make a QD/SBS test-design note.**

```text
question:
  Can state-functional objectivity eliminate uptake/application threshold,
  or only sharpen record diagnostics?
```

---

## 12. Compact ledger result

```text
Best nonzero lane:
  spin/current-correlated torsion burden in neutron-star observables

Best lab stress lane:
  Unruh/channeling response routing, not intrinsic bath

Best formal-theory lane:
  QES/holographic QEC extra resources must be reconstruction/area/backreaction-priced,
  not constitution-priced

Best conceptual experiment lane:
  QD/SBS record diagnostics versus uptake threshold

Best clean null lane:
  ε_info-redshift = 0
  ε_CMB-info = 0
  ε_null/QES-constitution = 0
```

The project should now track predictions as residuals, not slogans.
