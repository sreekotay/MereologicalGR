# B7 — Acceleration, Frame-Transport, and Scalar Response

*Working draft, June 2026.*

Status: B-note / positive-computation probe.  
Primary target: A0 rendering/uptake seam, A1 PB-4, B6 Unruh temperature, A3 write-act / record constitution.  
Grade: frame-transport refinement and scalar-response derivation program. Not a derivation of full QFT.

Core claim:

```text
velocity relates frames;
acceleration transports frames through flow.
```

MGR placement:

```text
frame = ordering + flow + adjacency

rendering = content-through-frame

frame-transport = change of frame-basis along flow

proper acceleration = nonzero frame-transport along flow
```

Acceleration is not a new role. It is an operation/derivative of the frame-process. It is the first clean place where the curvature of flow changes the rendering map itself.

Run-1 result:

```text
partial success:
  scalar Unruh response skeleton can be run from
  GR hyperbolic frame-transport + scalar two-place relatedness.

not derived:
  the scalar relatedness kernel itself,
  its positive-frequency / iε ordering prescription,
  full detector dynamics,
  full QFT.
```

The `2π` coefficient is not detector-specific machinery once the scalar kernel is admitted. It comes from the imaginary proper-time period of the hyperbolic pullback. The deep import is the scalar Wightman/Hadamard-style kernel and its `iε`/ordering structure.

---

## 1. Trigger

A0 already separates:

```text
content → rendering → uptake → information
```

B6 already states that Unruh temperature is not an invariant particle bath, but a flow-indexed rendering / response of vacuum relatedness pulled back onto an accelerated worldline.

The missing sharpening is:

```text
not all worldline dependence is equal.

velocity:
  selects a relative inertial rendering

proper acceleration:
  changes the instantaneous comoving frame through flow
```

An inertial observer with constant velocity is not actively moving through frames. It carries one local rest frame along its worldline. An accelerated observer continually changes instantaneous comoving inertial frame. That change is not a subjective observer-act; it is frame-transport along flow.

---

## 2. Layer placement

Do not promote acceleration to a peer role.

```text
roles:
  ordering
  influence
  flow
  adjacency

composite:
  frame = ordering + flow + adjacency

operation:
  rendering = content-through-frame

new operation under audit:
  frame-transport = transport / turning of frame-basis along flow

projection / scalar:
  proper acceleration = magnitude of non-inertial frame-transport
```

This preserves the anti-over-unfusing rule. Acceleration is a derivative/curvature of the frame-process, not a fifth component.

Operational shorthand:

```text
inertial flow:
  frame-basis is transported without turning

accelerated flow:
  frame-basis turns through flow
```

---

## 3. Why acceleration is stronger than velocity

Velocity is a relation between inertial frames. It changes a rendering comparison but does not itself curve the observer's worldline.

Proper acceleration changes the worldline's local frame basis from one moment of proper time to the next. It is the flow-derivative of the frame:

```text
proper acceleration ≈ d(frame-basis)/dτ
```

More precisely, in GR language, acceleration is the covariant derivative of the four-velocity along the worldline:

```text
a^μ = u^ν ∇_ν u^μ
```

This expression is imported GR mathematics. MGR's role-reading is:

```text
u^μ:
  flow-direction / local timelike frame leg

∇ along u:
  transport through flow

a^μ:
  failure of the flow-leg to transport inertially
```

So acceleration is not merely a state of motion. It is frame-transport made nontrivial.

---

## 4. Consequence for rendering and uptake

Current A0 stack:

```text
content → rendering → uptake → information
```

B7 inserts the transport condition:

```text
content
→ rendering through frame
→ frame-transport along flow
→ uptake/write
→ information
```

This does not mean acceleration is always required for constitution. Inertial detectors can write records. The claim is narrower:

```text
acceleration changes the sampling/rendering conditions under which uptake occurs.
```

Thresholds remain application-supplied. But acceleration can change:

```text
what field relatedness is sampled;
how it is pulled back onto proper time;
which modes are accessible;
what response spectrum a detector sees;
whether a thermal parameter is rendered.
```

Thus acceleration is a positive-computation handle on the rendering/uptake seam.

---

## 5. Scalar-only derivation probe

This is the suggestive part.

B6 currently says:

```text
framework-owned:
  compute on pulled-back phase-bearing relatedness;
  uniform acceleration supplies the flow-frequency scale a/c;
  therefore T = C · ℏ a/(c k_B)

QFT-owned:
  exact two-point kernel;
  KMS period;
  coefficient C = 1/(2π)
```

B7 asks whether that ownership split can be tightened for the scalar sector.

The proposed computation does **not** import QFT as a theory. It imports only a scalar two-place relatedness kernel and then lets GR geometry do the pullback.

Minimal import:

```text
scalar relatedness kernel:
  R(x,x′) = F(σ(x,x′), iε)

where:
  σ(x,x′) = invariant interval / world-function data
```

The scalar import may include:

```text
singular short-distance form;
choice of iε / ordering prescription;
ℏ as phase-to-energy conversion;
k_B as energy-to-temperature conversion.
```

Everything else should be forced from GR worldline geometry and frame-transport.

---

## 6. Run 1 — scalar Unruh response from GR pullback

### 6.1 Setup

Use flat spacetime and a uniformly accelerated timelike worldline.

Coordinate convention:

```text
x^0 = ct
```

Uniformly accelerated trajectory:

```text
ct(τ) = (c²/a) sinh(aτ/c)
x(τ)  = (c²/a) cosh(aτ/c)
```

Equivalently:

```text
t(τ) = (c/a) sinh(aτ/c)
x(τ) = (c²/a) cosh(aτ/c)
```

This is GR/SR-owned. It is the hyperbolic worldline generated by constant proper acceleration.

### 6.2 GR-owned invariant separation

Let:

```text
α = a/c
Δτ = τ - τ′
```

The coordinate differences are:

```text
Δ(ct) = (c²/a)[sinh(ατ) - sinh(ατ′)]
Δx    = (c²/a)[cosh(ατ) - cosh(ατ′)]
```

Use the hyperbolic identities:

```text
sinh A - sinh B = 2 cosh((A+B)/2) sinh((A-B)/2)
cosh A - cosh B = 2 sinh((A+B)/2) sinh((A-B)/2)
```

Then:

```text
(Δct)² - (Δx)²
= (4c⁴/a²) sinh²[aΔτ/(2c)]
```

up to the sign convention chosen for the interval.

This is the first real positive result:

```text
uniform acceleration + GR interval geometry
forces the sinh² pullback denominator.
```

No QFT operator algebra has entered.

### 6.3 Minimal scalar relatedness import

Now import a scalar two-place relatedness kernel with the massless short-distance form:

```text
R(x,x′) ∝ 1 / [ (ct-ct′-iε)² - |x-x′|² ]
```

This is the largest import in the run. It is not full QFT as a theory, but it is not nothing. It imports:

```text
scalar two-place relatedness;
null-cone singularity;
positive-frequency / ordering prescription via iε.
```

With that import, the accelerated pullback is forced:

```text
R(Δτ)
  ∝ 1 / sinh²[ a(Δτ-iε)/(2c) ]
```

This is the scalar-response object B7 needs.

### 6.4 Imaginary proper-time periodicity

Since:

```text
sinh(z + iπ) = -sinh(z)
```

and the kernel contains `sinh²`, the pulled-back relatedness satisfies the imaginary proper-time periodicity:

```text
Δτ → Δτ + i 2πc/a
```

Therefore:

```text
β_τ = 2πc/a
```

This is the second positive result:

```text
the 2π comes from hyperbolic frame-transport plus scalar analytic structure.
```

It is not supplied by detector mechanics. It is not fitted from the known Unruh value once the scalar kernel is accepted.

### 6.5 Temperature conversion

The period is a proper-time period. To read it thermally, import the scalar conversions:

```text
proper-time frequency → energy:
  ℏ

energy → temperature:
  k_B
```

Thus:

```text
β_E = β_τ / ℏ
    = 2πc/(ℏ a)
```

and:

```text
T = 1/(k_B β_E)
  = ℏ a/(2π c k_B)
```

So Run 1 reaches the exact scalar Unruh temperature form:

```text
T = ℏ a/(2π c k_B)
```

### 6.6 What was actually derived

Derived in Run 1:

```text
1. acceleration as frame-transport through flow;
2. hyperbolic worldline from constant proper acceleration;
3. invariant separation along that worldline;
4. sinh² pulled-back scalar form, given the scalar kernel;
5. imaginary proper-time period β_τ = 2πc/a;
6. Unruh temperature coefficient for scalar response, given ℏ and k_B.
```

Imported in Run 1:

```text
1. scalar two-place relatedness exists;
2. its massless short-distance/null-cone kernel form;
3. the iε / positive-frequency ordering prescription;
4. the legitimacy of reading imaginary proper-time periodicity thermally;
5. ℏ and k_B;
6. the minimal detector-response interpretation.
```

Not derived:

```text
QFT as a theory;
field quantization;
Hilbert space;
commutators;
particle operators;
renormalization;
spin/statistics;
interactions;
gauge fields;
non-abelian influence.
```

### 6.7 Verdict of Run 1

Run 1 succeeds at the narrower target:

```text
scalar Unruh response skeleton
from GR frame-transport + scalar relatedness import.
```

Run 1 does **not** derive QFT from GR.

The exact grade is:

```text
positive structural computation:
  yes, within scalar response

full QFT derivation:
  no

main remaining import:
  scalar Wightman/Hadamard-style relatedness with iε ordering
```

The live next question is whether the scalar kernel itself can be derived from MGR's influence floor plus Lorentz/GR interval structure, or whether it must remain an imported scalar.

---

## 7. What this would and would not derive

Derived / framework-owned if the probe succeeds:

```text
worldline pullback target;
acceleration as frame-transport scale;
hyperbolic-sine pulled-back form;
imaginary proper-time period 2πc/a;
Unruh scaling and coefficient for scalar response;
thermal response as rendering, not invariant particle bath.
```

Imported scalar ingredients:

```text
there is scalar phase-bearing relatedness at all;
its singular short-distance kernel form;
the iε / ordering prescription;
ℏ;
k_B.
```

Still not derived:

```text
Hilbert space;
canonical commutation relations;
field operator algebra;
particle creation/annihilation machinery;
spin/statistics;
interactions;
gauge fields;
renormalization;
full detector dynamics;
non-abelian influence floor.
```

So the maximal honest phrase is:

```text
scalar response skeleton from GR + scalar relatedness
```

not:

```text
full QFT derived from GR
```

unless later work shows that the scalar kernel itself is forced by the same machinery.

---

## 8. Failure conditions

This B-note fails or demotes if:

```text
F1. The scalar kernel import already smuggles in the whole QFT structure.
F2. The 2π coefficient depends on QFT machinery not contained in scalar interval-relatedness plus GR pullback.
F3. The iε prescription cannot be licensed as scalar ordering data without importing field quantization.
F4. Detector response / detailed balance cannot be stated without full QFT operator structure.
F5. Acceleration changes only rendering language, not any calculable response structure.
F6. The computation works only because the standard QFT result was silently chosen as the scalar kernel.
```

Run-1 status:

```text
F1:
  partially live — the scalar kernel is a serious import, but not full QFT by itself.

F2:
  not fired for the coefficient; 2π follows from hyperbolic pullback once scalar analytic structure is admitted.

F3:
  live — iε is the deepest unresolved import.

F4:
  live for detector rates; not live for the period/temperature skeleton.

F5:
  not fired — acceleration produces calculable imaginary proper-time periodicity.

F6:
  live hygiene risk — kernel must be justified independently, not reverse-engineered from Unruh.
```

F6 is the main hygiene risk. To avoid it, the scalar kernel must be stated before the accelerated pullback and justified independently as the minimal scalar relatedness object, not reverse-engineered from Unruh.

---

## 9. Relation to PB-4

PB-4 says information constitution is frame-process/write-chain, not observer.

B7 sharpens the frame-process side:

```text
frame-process is not merely a selected inertial frame;
it includes frame-transport through flow.
```

Unruh then becomes:

```text
same scalar relatedness;
different frame-transport;
different response rendering;
possible write if detector threshold is crossed.
```

This supports PB-4a more sharply:

```text
rendering is worldline / frame-transport set,
not observer-set.
```

It still does not confirm PB-4-full:

```text
thermal rendering is not yet information constitution;
constitution requires uptake/write at application scale.
```

---

## 10. Relation to horizons

Uniform acceleration is the clean flat-spacetime laboratory. Horizons are the curved / access-boundary continuation.

Working map:

```text
Unruh:
  acceleration horizon from frame-transport

black-hole exterior:
  static observer acceleration / access restriction near horizon

infalling observer:
  locally inertial flow, no same thermal rendering at crossing
```

This suggests the positive computation may extend:

```text
near-horizon Hawking response
≈ scalar relatedness pulled back through horizon-generating frame-transport
```

but this is a later run. Do not import the full Hawking derivation here.

---

## 11. Standing result

B7's standing claim:

```text
acceleration = frame-transport through flow
```

and its computation probe:

```text
Can scalar-response physics be derived from:
  GR frame-transport
  + scalar two-place relatedness
  + scalar conversion constants?
```

Run-1 answer:

```text
yes for the scalar Unruh response skeleton;
no for full QFT;
open for deriving the scalar kernel itself.
```

If the scalar kernel can later be earned, the framework gets a positive result stronger than a prohibition:

```text
GR geometry does not merely host QFT response;
for the scalar response skeleton, GR frame-transport computes it
once minimal scalar relatedness is imported.
```

That is the live edge. It is not a completed derivation of QFT; it is the first clean place where MGR derives a QFT-like thermal response without importing QFT as a whole.