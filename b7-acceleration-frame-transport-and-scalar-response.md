# B7 — Frame-Transport and Scalar Response

*Working draft, June 2026.*

Status: B-note / scalar-response clarifier and role-location.
Primary target: A0 rendering/uptake seam, A1 PB-4, and B6 temperature/information discipline.  
Grade: retrodictive role-location + boundary audit of the standard scalar-response derivation. Magnitude and full QFT machinery remain imported.

B7 separates three frame-transport bets:

```text
FT-1:
  frame-transport is physically real;
  carried / comparison structure can change observables.

FT-2:
  proper acceleration is the local residue of non-geodesic self-transport of flow;
  this is the Levi-Civita face of the frame-transport bet.

FT-3:
  the Unruh scalar-response skeleton can be role-located through
  flow self-transport / rendering rather than only bare worldline pullback;
  live projection, stated / role-located here;
  not a separate test of full carried-frame-basis transport.
```

FT-1 is the broader axis. It is supported by ordinary GR and quantum handles: gyroscope precession, spin transport, holonomy, spin-rotation coupling, polarization transport, and related carried-vector / carried-frame effects. FT-2 and FT-3 are narrower. B7 reads proper acceleration first as a Levi-Civita self-transport fact: the flow direction is compared with itself along its own path, and the nonzero residue is `a^mu = u^nu nabla_nu u^mu`. That is stronger than a slogan and weaker than a full identity between acceleration and all frame-transport. It says acceleration exposes the flow-leg face of frame-transport.

The richer carried-frame-basis claim is separate. A tetrad, spin axis, polarization basis, or detector orientation can also be transported, and those richer cases are where FT-1 has broad external support. The scalar Unruh run suppresses the distinguishing carried-basis variable, so it cannot test full carried-frame-basis transport. Its question is narrower: whether the standard scalar lineage can be cleanly role-located as bare worldline pullback plus flow/self-transport status.

Frame-transport is broader than proper acceleration, but it is not arbitrary tetrad relabeling or coordinate bookkeeping. It names invariant or operationally fixed frame change / comparison as priced by the imported GR transport structure: along a flow, between nearby flows, around loops, or through any live torsion sector. B7 uses uniform proper acceleration because it gives the clean scalar-response computation and a place to audit FT-2 / FT-3 for missing/extra remainder.

Once acceleration is read this way, the standard scalar Unruh response has a GR interval skeleton with an MGR role-location. Metric/Levi-Civita structure gives the natural scalar propagation operator once a scalar sector is admitted. The flat massless scalar sector gives the local interval singularity. Uniform acceleration pulls that skeleton onto a hyperbolic worldline. The resulting `sinh²` form has imaginary proper-time period `2πc/a`.

B7 does not provide a competing Unruh calculation. It re-audits the standard lineage: GR interval geometry supplies the pullback period, QFT supplies the state and detector interpretation, and MGR supplies a clarifier-grade flow/rendering/uptake role audit. That audit returns no missing/extra remainder.

Calibration is not failure. Fitting is failure. A scalar may be observed; a structure must be earned.

---

## 1. Minimal toolkit and import boundary

The scalar-response seam takes a three-layer audit, not a competing Unruh calculation.

```text
Layer 1 — owned (GR / A0 lineage):
  frame = ordering + flow + adjacency; rendering is always through a flow-bearing frame
  frameless null content is rendered only second-hand at a flow-frame (A1 photon corner)
  frame-transport bets FT-1 / FT-2 / FT-3
  acceleration = local residue of non-geodesic self-transport of flow
  rendering ≠ constitution; uptake/write at threshold is the constitution site (A1 PB-4)
  retarded causal orientation from cause = ordering + influence

Layer 2 — projected (read from GR / Levi-Civita geometry):
  scalar operator □_g from metric / connection, given a scalar probe
  leading 1/σ interval skeleton in 4D; hyperbolic sinh² pullback under uniform acceleration
  imaginary proper-time period β_τ = 2πc/a (geometric, not fitted)
  proper acceleration a = sqrt(a^μ a_μ), spacelike (A2 §6)

Layer 3 — imported (QFT state machinery + calibration):
  vacuum / state selection; Wightman two-point sampling; iε / positive-frequency state rule
  KMS / detailed-balance thermal reading; detector transition probabilities
  ℏ, k_B, normalizations, couplings, detector gaps, thresholds
  all magnitude
```

Layer 1 is the minimal constituency for the rendering/uptake audit. Layer 2 maps it onto GR interval geometry, which forces the sinh² pullback and the 2π period with no QFT input. Layer 3 supplies the thermal reading of that period and all magnitude. The audit returns no missing/extra remainder. Sections below are consumers of this boundary.

---

## 2. Acceleration as frame-transport

A0 defines:

```text
frame = ordering + flow + adjacency
rendering = content-through-frame
```

Because `frame` carries the flow leg, rendering is always through a flow-bearing frame. Frameless null content (A1 photon corner: ordering + influence + adjacency, no flow) has no frame of its own, so it is rendered only second-hand — through a flow-bearing worldline that is not its own. The accelerated detector below is exactly such a flow-frame: it renders relatedness that cannot render itself.

B7 uses one operation:

```text
frame-transport =
  invariant or operationally fixed frame change / comparison through GR transport
```

Four-acceleration is the covariant rate at which the flow-leg fails to transport inertially:

```text
a^μ = u^ν ∇_ν u^μ
```

where `u` is the local flow direction and `∇ along u` is transport through flow.

The scalar proper acceleration is the magnitude of this vector:

```text
a = sqrt(a^μ a_μ)
```

Four-acceleration is spacelike (`a·u = 0`), so with signature `(−,+,+,+)` the magnitude `a = sqrt(a^μ a_μ)` is real (matching A2 §6). This scalar `a` sets the uniform-acceleration scale in the Unruh calculation.

On this Levi-Civita reading, velocity and acceleration do different work:

```text
velocity:
  relates inertial frame descriptions

proper acceleration:
  marks non-geodesic self-transport failure of the flow direction
```

An inertial worldline self-transports its flow direction. An accelerated worldline does not. A carried frame-basis adds the richer Fermi-Walker / tetrad question, but the local scalar acceleration already diagnoses failure of inertial self-transport of flow.

Guardrail:

```text
frame-transport:
  GR-imported transport/comparison operation;
  broader than proper acceleration;
  not pure frame-gauge choice

proper acceleration:
  measurable local face of non-geodesic self-transport of timelike flow
```

Acceleration is not gravity. On a timelike geodesic `u^ν ∇_ν u^μ = 0`, so `a = 0`, yet curvature `R` may be nonzero: tidal deviation, holonomy, and redshift stay live (A2 §5–6 geodesic stress test). Proper acceleration meters non-geodesic use of `∇` on this one line; it is not gravity and not frame-transport whole. The uniform Rindler `a` used below is a flat-spacetime laboratory for scalar pullback (`R = 0`), not a curved-source readout.

This matters for uptake if FT-3 is right, because acceleration changes the sampling/rendering conditions:

```text
content
→ rendering through frame
→ frame-transport along flow
→ possible uptake/write
→ information
```

Acceleration is not required for constitution. Inertial detectors can write records. The narrower claim is that acceleration changes what relatedness is sampled and how it is pulled back onto proper time. The live question is whether that change is exhausted by bare worldline pullback or whether the worldline is already a compressed GR object: flow plus connection-comparison plus self-transport status.

The reason FT-3 remains live even in a scalar case is rendered-influence structure. The scalar pullback does not show an orientation-sensitive frame basis, but it does show relatedness rendered along accelerated flow into a response-capable proper-time structure. Phase-bearing enters where the imported field route exposes path, period, or correlation structure. That is enough to keep the rendering/influence reading live. It does not prove the richer carried-frame-basis operation; it tests the flow self-transport face of the seam.

This is the useful "naked flow" result, in the role sense. The scalar setup suppresses the richer frame-basis roles:

```text
spin axis;
polarization basis;
detector orientation tensor;
spatial tetrad leg visible in the coupling.
```

What remains exposed is:

```text
proper-time indexing;
energy-gap orientation relative to flow;
self-transport status of flow;
phase-bearing relatedness rendered along that flow.
```

So scalar Unruh does not prove full carried-frame-basis transport. It isolates the flow/self-transport face of frame-transport.

**Refinement — the forced face and its mass-blind sibling.** [B7 stands on its own skeleton without this refinement. Grade: clarifier.] Proper acceleration is the **forced face** of frame-transport — ∇ along a normalizable timelike `u`, flow-bearing only; integrated, it is the boost / inertial-frame generator, and null content is locked out for want of a normalizable `u`. Its sibling is the **curvature face** (holonomy, geodesic deviation; A2 §5–6), mass-blind, acting on null tangents too (light bends). One operation — the single Levi-Civita ∇ — split by whether the transported thing carries flow: B7 works the forced (flow-only) face, A2 the mass-blind one. This keeps B7's contribution legible as a scalar-skeleton route rather than a relabeled `2π`.

---

## 3. Metric/Levi-Civita structure gives the scalar operator

Levi-Civita structure does more than transport vectors. Given a metric-compatible torsion-free GR sector and an admitted scalar probe, the metric/connection structure gives the natural scalar wave operator:

```text
□_g φ = ∇_μ ∇^μ φ
```

For a scalar, `∇_μ φ = ∂_μ φ`, but the second derivative and divergence require the metric/connection structure:

```text
□_g φ = |g|^{-1/2} ∂_μ( |g|^{1/2} g^{μν} ∂_ν φ )
```

MGR reading:

```text
metric:
  ordering + adjacency + clock/separation magnitudes + signature

Levi-Civita:
  comparison / transport preserving that metric structure

scalar □_g:
  minimal scalar relatedness propagation generated by that metric/transport structure
```

This still assumes a scalar probe. The minimal scalar assumptions are:

```text
scalar relatedness exists;
it is local, covariant, and index-free;
it is massless / scale-free for the flat Unruh run;
it uses second-order linear propagation.
```

Those assumptions are smaller than importing a finished Wightman function, but they are not zero. They license the scalar sector; GR/LC then fixes the natural operator up to curvature and scale terms:

```text
P = □_g + ξR + m²
```

For the flat massless run, `R = 0` and `m = 0`, so `P = □`. The curvature coupling `ξ` is invisible here and remains a curved-sector choice unless separately earned.

---

## 4. The scalar skeleton is interval-governed

In flat four-dimensional spacetime, the massless scalar operator is schematically:

```text
□ = η^{μν} ∂_μ ∂_ν
```

A scalar response object is constrained by the flat operator:

```text
□ R(x,x′) ∝ δ⁴(x-x′)
```

Away from coincidence, Lorentz invariance and absence of internal indices force the local interval skeleton to depend on invariant separation:

```text
R_skel(x,x′) = F(σ)
```

where `σ` is quadratic interval/world-function data.

In four spacetime dimensions, the leading local massless scalar singularity has dimension `length^-2`. With no additional scale in the flat massless run, the interval-governed local skeleton has the form:

```text
R_skel(x,x′) ∝ 1 / σ(x,x′)
```

This is not a full Green function, and not yet a Wightman function. Distributional prescription, normalization, state choice, and global boundary conditions are not earned here. B7 uses only the leading local interval singularity, singular at `σ = 0`, the null cone.

MGR reading:

```text
null cone:
  ordering boundary

1/σ singularity:
  scalar relatedness concentrated at that boundary
```

This matches the photon seed: massless relatedness is organized around the null boundary, where ordering remains and flow is stripped.

In curved spacetime the local Hadamard form is schematically:

```text
G(x,x′) ∼ U(x,x′)/σ + V(x,x′) log σ + W(x,x′)
```

The leading interval singularity and transport/focusing data are geometric. The state-dependent smooth part, global boundary conditions, and quantum meaning of the two-point object are not earned here.

---

## 5. Acceleration pulls the skeleton onto `sinh²`

Use flat spacetime and a uniformly accelerated timelike worldline. With `x⁰ = ct`:

```text
ct(τ) = (c²/a) sinh(aτ/c)
x(τ)  = (c²/a) cosh(aτ/c)
```

Equivalently:

```text
t(τ) = (c/a) sinh(aτ/c)
x(τ) = (c²/a) cosh(aτ/c)
```

Here `a` is scalar proper acceleration, the magnitude of the four-acceleration.

Let:

```text
α = a/c
Δτ = τ - τ′
```

Then:

```text
Δ(ct) = (c²/a)[sinh(ατ) - sinh(ατ′)]
Δx    = (c²/a)[cosh(ατ) - cosh(ατ′)]
```

Using the hyperbolic identities:

```text
sinh A - sinh B = 2 cosh((A+B)/2) sinh((A-B)/2)
cosh A - cosh B = 2 sinh((A+B)/2) sinh((A-B)/2)
```

the invariant separation becomes, up to sign convention:

```text
(Δct)² - (Δx)²
= (4c⁴/a²) sinh²[aΔτ/(2c)]
```

Pulling back the scalar skeleton gives:

```text
R_skel(τ,τ′) ∝ 1 / sinh²[a(τ-τ′)/(2c)]
```

This is the main positive computation. Uniform acceleration plus GR interval geometry forces the `sinh²` pullback denominator.

---

## 6. The `2π` period is geometric

The pulled-back skeleton has imaginary proper-time periodicity because:

```text
sinh(z+iπ) = -sinh(z)
```

and the square removes the sign. Therefore:

```text
β_τ = 2πc/a
```

This `2π` is geometric. It is not fitted, not calibrated, and not supplied by QFT state machinery. It follows from the hyperbolic pullback.

Converting a proper-time period into temperature requires the usual quantum/thermodynamic scalars:

```text
β_E = β_τ / ℏ
    = 2πc/(ℏ a)

T = 1/(k_B β_E)
  = ℏ a/(2π c k_B)
```

So the scalar Unruh temperature form follows conditionally:

```text
T = ℏ a/(2π c k_B)
```

given the geometric period and the temperature-reading imports.

In this run, the `2π` itself is structure-derived. What remains externally supplied is the thermal meaning of the period: state choice, Wightman/KMS sampling, detector response, and the quantum/thermodynamic constants.

---

## 7. The quantum state boundary

The skeleton is not the full response. The missing piece is the state prescription:

```text
iε;
positive-frequency split;
which side of the singularity is approached;
which vacuum/state is sampled.
```

Three prescriptions must not be fused:

```text
retarded / advanced:
  causal support

Feynman:
  time-ordering

Wightman:
  vacuum correlation / positive-frequency sampling
```

MGR can derive the retarded causal orientation from:

```text
cause = ordering + influence
```

If influence is causal influence, influence-expression must respect future ordering. Retarded support is therefore role-natural. That does not derive the Wightman prescription.

MGR also locates positive frequency. Energy is the flow-conjugate face of energy-momentum, so a mode sampled along proper time,

```text
mode ∼ e^{-iωτ}
```

has:

```text
E = ℏω
```

Positive frequency is positive energy relative to future-directed flow:

```text
positive-frequency = future-flow-compatible energy orientation
```

But turning that orientation into a Wightman two-point function requires a state and sampling rule.

For a worldline with future-directed four-velocity `u`, local energy is:

```text
E(u,p) = -p · u
```

with signature `(-,+,+,+)`. For future-directed causal `p`, `E(u,p) > 0`. Thus MGR/GR earns positive-energy orientation. It does not earn the vacuum state.

A detector response also requires a stable lower reference. Otherwise excitation and de-excitation are not measured against a floor. MGR can derive the need for such a stability floor from flow-indexed response, but not the state that realizes it.

The boundary is:

```text
retarded i0:
  role-derived / causal-response natural

positive frequency:
  future-flow energy orientation

stability floor:
  required by flow-indexed response;
  state realizing it not derived

Wightman iε:
  conditionally located, not derived

vacuum / KMS / detector response:
  quantum-state machinery
```

---

## 8. Consistency check for Unruh and PB-4

For Unruh:

```text
Minkowski vacuum:
  stable positive-energy state relative to inertial time

accelerated detector:
  samples that same state along accelerated flow
```

The geometry supplies the scalar skeleton and `2π` period. QFT supplies the vacuum/Wightman/KMS detector-response layer. B7's role-audit of this standard lineage returns no missing/extra remainder.

Consistency with PB-4a:

```text
rendering is worldline / frame-transport set,
not observer-set.
```

The clarifier read is not that an observer imagines particles. It is:

```text
same scalar relatedness;
different frame-transport;
different response rendering;
possible write if detector threshold is crossed.
```

This is a consistency check with PB-3 / PB-4, not a B7-originated guardrail. It does not confirm PB-4-full, because thermal rendering is not information constitution. Constitution still requires uptake/write at application scale.

**D1 alignment:** the accelerated response routes through pullback + coupling + gap + uptake, QFT supplying the state/detector layer. It fails if a detector-independent invariant in-flight bath is required (`diagnostic-ledger.md` §5 / D1; B6 owns the temperature/information daylight).

---

## 9. Horizons and the next wall

Uniform acceleration is the flat-spacetime laboratory. Horizons are the curved/access-boundary continuation.

```text
Unruh:
  acceleration horizon from frame-transport

black-hole exterior:
  static observer acceleration / access restriction near horizon

infalling observer:
  locally inertial flow, no same thermal rendering at crossing
```

This suggests a later near-horizon run:

```text
near-horizon Hawking response
≈ scalar relatedness pulled back through horizon-generating frame-transport
```

But B7 does not import the full Hawking derivation.

The next disciplined question is not “derive the vacuum” in general. Generic curved spacetime may have no unique global vacuum. The narrower live edge is:

```text
Can MGR derive a local Hadamard/stability condition
as the minimal admissible scalar state condition,
without choosing a global vacuum?
```

---

## 10. Ledger

Role-located / clarified / inherited computation:

```text
FT-1:
  frame-transport as a real GR/QM-visible operation;
  supported broadly, not derived from the scalar Unruh run.

FT-2:
  acceleration as local residue of non-geodesic self-transport of flow;
  Levi-Civita face of the frame-transport bet.

FT-3:
  Unruh scalar response as phase-bearing relatedness rendered through
  accelerated flow self-transport rather than only bare worldline pullback;
  stated / role-located here.

standard computation, role-located here:
  scalar wave operator from metric/Levi-Civita structure, given scalar assumptions;
  interval/world-function dependence;
  leading 1/σ scalar skeleton in 4D;
  hyperbolic pullback under uniform acceleration;
  imaginary proper-time period β_τ = 2πc/a.

role-natural / boundary-located:
  retarded causal support;
  positive frequency as future-flow energy orientation;
  need for a stability floor.
```

Calibrated / allowed scalars:

```text
ℏ and k_B;
normalizations;
coupling strengths;
detector gaps;
threshold scales;
empirically measured coefficients, if the structural form was fixed first;
curvature coupling ξ in curved sectors, unless separately derived.
```

Imported / not derived machinery:

```text
existence of scalar relatedness/probe;
second-order linear local scalar dynamics;
massless/scale-free scalar sector;
stable state / vacuum selection;
Wightman two-point sampling;
KMS/detailed-balance thermal interpretation;
detector transition probabilities;
Hilbert space / operator algebra / particle machinery;
spin, gauge fields, interactions, renormalization;
non-abelian influence floor.
```

Demotion conditions:

```text
FT-1 fails if carried / comparison structure never changes any invariant or operational observable;
FT-2 fails if acceleration is only a worldline parameter, not self-transport failure of flow;
FT-3 fails if the Unruh scalar skeleton is exhausted by bare worldline pullback with no phasic rendering role;
the audit finds a missing/extra remainder in the standard Unruh lineage;
the scalar operator is not forced by the stated scalar assumptions;
the 1/σ skeleton can be replaced without adding a scale or violating the wave equation;
the 2π period depends on QFT iε rather than hyperbolic geometry;
retarded causal support does not follow from ordering + influence;
positive frequency cannot be tied to future-flow energy orientation;
stable detector response does not require a lower energy reference;
the analytic period has no role in the thermal response once QFT state machinery is supplied;
scalar assumptions smuggle in too much field theory;
coefficient or dependency was selected by fitting rather than derived before calibration.
```

Standing result:

```text
B7 does not provide a distinct Unruh lineage.
It role-locates the standard scalar-response lineage:
  GR interval geometry supplies the pullback skeleton and 2π imaginary proper-time period;
  QFT supplies the Wightman/KMS detector-response interpretation;
  MGR supplies a clarifier-grade flow/rendering/uptake audit.

Audit verdict:
  no missing/extra remainder in the standard lineage.

Grade: retrodictive role-location; magnitude QFT-supplied.
```

Calibration rule:

```text
Calibration is not failure.
Fitting is failure.
```