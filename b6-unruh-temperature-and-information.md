# B6 — Unruh Temperature and Information

*Working draft, June 2026.*

Status: full B-note / refinement document.  
Primary target: A1 §11.4 Unruh / Rindler, with contact to A2 EB-1/EB-2 and A3 redshift / consequential uptake.  
Grade: machinery-routing and role-reduction. Not a new temperature derivation, not a new QFT calculation, not a new numerical prediction.

Core result:

```text
Unruh temperature is the temperature obtained when vacuum phase-bearing relatedness
is pulled back onto an accelerated flow-worldline and satisfies the KMS thermal test.
```

Companion result:

```text
temperature is not information itself;
it is a flow-indexed rendering parameter of accessible mixedness / response.
It becomes informational only when an ordered consequence is taken up
into a flow-bearing record.
```

The exact Unruh coefficient remains QFT-owned:

```text
T_U = ℏ a / (2π c k_B)
```

The framework-owned question is narrower but real: how much of the **machinery that computes temperature** follows from the roles once influence is read as consequence-capable phase-bearing relatedness?

---

## 1. Trigger

The parent Unruh section held five claims:

```text
1. invariant layer = field state / influence-structure
2. particle content / information = frame-relative rendering
3. worldline / flow-structure is the discriminator of uptake
4. influence invariant, rendering frame-dependent
5. could-fail: breaks if the field state itself differs between frames
```

That remains correct.

The refinement under consideration is the influence-floor carve:

```text
influence = consequence-capable phase-bearing relatedness
```

Here `phase-bearing` is role-language, not a claim that all influence is a U(1) phase angle. It means coherent, order-sensitive relatedness: abelian scalar phase at the simple face; holonomy, path-ordering, mixing, representation-dependent transport, and non-commuting structure in richer interiors.

This refinement does not change the Unruh grade. It sharpens what the invariant layer is:

```text
old:
  field state / influence-structure

new:
  phase-bearing relatedness of the field,
  made consequence-capable when coupled to the detector
```

The accelerated detector does not discover a pre-existing invariant particle bath. It samples the same vacuum phase-bearing relatedness through a different flow-path and access structure, and that pullback has a thermal response.

---

## 2. Failure condition

This refinement fails if any of the following occur:

```text
F1. The Unruh temperature requires observer-subjective choice rather than worldline structure.
F2. The thermal response cannot be stated as a pullback of field correlations to a flow-worldline.
F3. The same invariant field state is not shared between inertial and accelerated descriptions.
F4. Temperature must be assigned to particles as one-place in-flight objects, rather than to response/distribution relative to a worldline or congruence.
F5. The machinery requires a constituted record before the thermal response can be defined.
```

Current status: none fire. Standard QFT gives a worldline-only detector response from the field two-point function. The state can be the same Minkowski vacuum while particle content / response is frame-relative. Constitution enters only when a detector write or application record is completed.

---

## 3. Standard Unruh temperature machinery, externally owned

For a uniformly accelerated detector in the Minkowski vacuum, the standard computation has this schematic form:

```text
field state
→ two-point function / Wightman function G⁺(x,x′)
→ pull back to the detector worldline x(τ)
→ G⁺(τ,τ′)
→ detector response integral
→ KMS / imaginary-proper-time periodicity
→ inverse temperature
→ T_U = ℏ a / (2π c k_B)
```

The uniformly accelerated trajectory supplies a proper-time scale set by acceleration. The pulled-back correlation function has the characteristic imaginary proper-time periodicity:

```text
β_τ = 2π c / a
```

This is an inverse-temperature period in **time units**. Converting to ordinary thermodynamic inverse temperature:

```text
β_E = 1/(k_B T) = β_τ / ℏ = 2π c / (ℏ a)
```

therefore:

```text
T_U = ℏ a / (2π c k_B)
```

The framework does not derive the Wightman function, the detector response integral, the KMS theorem, or the coefficient. Those are QFT-owned.

But the machinery has role-slots.

---

## 4. Role-routing of the Unruh machine

The role-route is:

```text
phase-bearing relatedness
→ detector coupling / consequence-capacity
→ flow-sampling
→ thermal test
→ temperature parameter
→ possible uptake / write
```

Mapped:

```text
what is sampled:
  phase-bearing relatedness of the field
  formal representative: field correlations / two-point function

what makes it influence in this setup:
  detector coupling gives the relatedness consequence-capacity

where it is sampled:
  a flow-bearing worldline x(τ)
  parameter: proper time τ

what changes between inertial and accelerated cases:
  the flow-worldline / access structure,
  not the invariant global state

what makes it thermal:
  KMS / imaginary-proper-time periodicity of the pulled-back relatedness

what sets the scale:
  acceleration as worldline curvature,
  giving β_τ = 2π c/a

what converts to temperature:
  ℏ converts proper-time frequency to energy;
  k_B converts energy scale to temperature

where information enters:
  only at uptake/write — detector response, click, threshold, record-chain
```

So the framework can say:

```text
The computation of Unruh temperature is a computation on vacuum phase-bearing
relatedness as sampled by a flow-worldline and made consequence-capable through
detector coupling.
```

It may not say:

```text
The framework derives the Unruh temperature value.
```

The correct grade is:

```text
value:
  externally derived by QFT

machinery route:
  framework-licensed, if influence = consequence-capable phase-bearing relatedness
```

---

## 5. What Unruh becomes under phasic influence

Before:

```text
same field state;
different worldline rendering.
```

After:

```text
same vacuum phase-bearing relatedness;
different flow-path sampling;
different rendered particle / temperature content.
```

The accelerated detector's thermal response is not created by an observer's belief. It is also not an invariant bath of particles in the global state. It is the response of a detector coupled along a non-inertial flow-worldline to vacuum correlations whose pullback has KMS form.

In role form:

```text
Minkowski vacuum:
  invariant phase-bearing relatedness

inertial worldline:
  samples it as vacuum / no thermal bath

accelerated worldline:
  samples it with Rindler access restriction and imaginary-time periodicity

thermal response:
  temperature rendering of the same relatedness under that flow

detector click:
  possible constitution event, if application threshold is crossed
```

This keeps the parent grade exactly:

```text
PB-4a sharpened:
  rendering is worldline/flow-set, observer-free

PB-4-full not confirmed:
  Unruh still shows rendering, not constitution-completion
```

---

## 6. Relation to CMB / redshift work

The CMB/redshift work already made the sibling move.

There, the pseudo-problem was:

```text
where did the redshifted photon's energy go?
```

The resolution was that photon energy is not a one-place in-flight property. It is a two-place rendering:

```text
E(γ, worldline) = −p·u
```

Different comoving worldlines render different energies. Nothing drains from an in-flight photon-register because there is no flow-bearing in-flight register for constituted energy to reside in.

The CMB temperature is likewise not a one-place property of each photon-in-itself. It is a distribution parameter rendered relative to a congruence. In an expanding universe, the rendered photon energy scales with the congruence, and a thermal radiation distribution preserves its thermal form with:

```text
T(z) = T₀(1+z)
```

The machinery there is:

```text
null radiation distribution
→ rendered against a comoving congruence u
→ per-photon energy E = −p·u
→ distribution remains thermal under expansion
→ temperature parameter scales with the rendered energy scale
```

EB-1 / EB-2 supply the aggregate side:

```text
single photon:
  no rest frame

photon aggregate / box:
  rest frame possible at the aggregate
  net spatial momentum cancels
  de-oriented adjacency-spread remains

entropy reading:
  valid only given mixedness;
  a pure photon pair may have de-oriented spread but S_vN = 0
```

Thus CMB and Unruh share a role skeleton but not a substrate:

```text
CMB:
  real photon aggregate
  content-selected rest frame / comoving congruence
  mixed radiation distribution
  temperature rendered by congruence

Unruh:
  no invariant real particle bath
  accelerated worldline / Rindler access
  vacuum correlations appear thermally in detector response
  temperature rendered by flow-worldline
```

Shared machine:

```text
field/radiation relatedness
+ flow-worldline or congruence
+ rendered energy scale
+ mixedness, restriction, or KMS response
→ temperature parameter
```

---

## 7. Temperature and information — first reduction

Question:

```text
what kind of information is temperature?
```

Answer:

```text
temperature is not information itself.
```

Temperature is a parameter of rendering, distribution, or response. It can become informational only when an ordered consequence is taken up into a flow-bearing record.

Three distinctions matter.

### 7.1 Temperature is not entropy

Entropy measures accessible mixedness / multiplicity / uncertainty relative to a coarse-graining or state description.

Temperature is not that measure. Thermodynamically, temperature is the conjugate slope:

```text
1/T = ∂S/∂E
```

where applicable. In response language, temperature is the detailed-balance / KMS parameter controlling relative transition rates.

Role reading:

```text
entropy:
  measure of accessible mixedness / state multiplicity

temperature:
  flow-indexed energy scale of that accessibility / response
```

So temperature is about how the accessible state answers energy-exchange, not the full information content of that state.

### 7.2 Temperature is not microscopic content

A temperature does not specify the microstate. Many states can share the same temperature. Temperature is compression, not constitution.

Role reading:

```text
temperature:
  a scalar compression of accessible response

microstate / full record:
  much richer content
```

So temperature is information-bearing only in the weak sense that any measured scalar is information-bearing once recorded. It is not identical to the information constituted by the substrate.

### 7.3 Temperature is not in-flight particle property

For null radiation, energy is rendered against a worldline or congruence:

```text
E = −p·u
```

A thermal radiation temperature is therefore a property of a rendered distribution, not a one-place property of photons in transit.

For Unruh, the same lesson appears without a real photon gas:

```text
same vacuum phase-bearing relatedness
+ accelerated worldline sampling
→ thermal response temperature
```

Temperature belongs to the access/rendering machinery.

---

## 8. Proposed role definition

Candidate definition:

```text
temperature = a flow-indexed scale parameter of accessible phase-bearing / mixed response.
```

Expanded:

```text
flow-indexed:
  temperature requires a time parameter, worldline, congruence, or evolution parameter
  against which response / equilibrium / periodicity is defined

scale parameter:
  temperature is not the microstate; it is the energy scale of a distribution or response

accessible:
  temperature depends on what degrees of freedom are available to the renderer / subsystem / detector

phase-bearing / mixed response:
  in quantum-field settings, temperature can arise from KMS structure of correlations;
  in ordinary thermal settings, from mixed ensembles / statistical distributions
```

This definition intentionally does not claim all temperatures are Unruh-like. It says the role-home of temperature is the same kind of slot:

```text
accessible state or relatedness
sampled/rendered along flow
compressed into an energy-response scale
```

---

## 9. Information relation

Given the parent composition:

```text
information = ordering + influence + flow
```

and the influence refinement:

```text
influence = consequence-capable phase-bearing relatedness
```

then temperature sits below constituted information:

```text
relatedness:
  bare connection / substrate

phase-bearing relatedness:
  coherent / holonomic / order-sensitive connection

influence:
  consequence-capable phase-bearing relatedness

temperature:
  flow-indexed response scale of accessible relatedness / mixedness

information:
  ordered influence taken up in flow at application scale
```

Temperature can participate in information, but is not itself sufficient for information.

Example:

```text
Unruh detector response rate:
  thermal rendering exists at the response-function level

actual detector click:
  uptake event

recorded click above threshold:
  ordered consequence taken up in flow;
  constituted information for the application
```

So temperature is best read as an **information-conditioner** or **rendering parameter**, not as information itself.

Candidate phrasing:

```text
Temperature is the flow-indexed price of accessible mixedness;
information is the write that makes some ordered consequence of that mixedness count.
```

This is suggestive, not final. The safer version is:

```text
Temperature is the flow-indexed response scale of accessible mixedness / phase-bearing relatedness;
information requires ordered uptake into a consequential record.
```

---

## 10. Hawking contact

Hawking temperature should be treated as the horizon sibling, not as support by slogan.

The familiar role-form is:

```text
Unruh:
  acceleration a
  Rindler horizon / accelerated access
  T_U = ℏ a / (2π c k_B)

Hawking:
  surface gravity κ
  black-hole horizon / exterior access
  T_H = ℏ κ / (2π c k_B)
```

The shared structure is:

```text
restricted access + horizon/flow structure
→ KMS/thermal rendering of field relatedness
→ temperature set by acceleration/surface-gravity scale
```

But B4's discipline applies. Hawking/Page/QES should not be over-read as sealing GB-2 or PB-4-full. For B6, the legitimate contact is narrower:

```text
Hawking temperature belongs to the same temperature-machinery family:
field relatedness rendered thermally under horizon/access structure.
```

The exact coefficient and radiation spectrum remain QFT-in-curved-spacetime owned.

---

## 11. Edge cases and guardrails

### 11.1 Zero temperature

Temperature zero is not absence of influence. It is a boundary in response/distribution structure:

```text
T → 0
β_E → ∞
```

Role reading:

```text
no finite thermal energy scale in the relevant response;
not no relatedness;
not no information;
not no possible consequence.
```

### 11.2 Negative temperature

Negative temperature, where defined, is not colder than zero. It is an inverted population in a bounded spectrum.

Role reading:

```text
sign of β marks response-orientation / population ordering,
not an absolute magnitude below zero.
```

This belongs to temperature's rendering/response side, not to the basic composition of information.

### 11.3 Local temperature vs global state

Unruh warns against treating temperature as a global one-place property. The same invariant state can yield different temperature renderings under different access/flow structures.

Role rule:

```text
Do not ask whether the state simply has temperature.
Ask: relative to which flow, access algebra, subsystem, detector, or congruence?
```

### 11.4 No temperature without a clock parameter

Temperature requires a flow/evolution parameter in the machinery: proper time, Killing time, comoving time, modular flow, detector time, or an application equivalent.

This does not mean temperature is subjective. It means temperature is indexed to the flow structure that defines response/equilibrium.

### 11.5 Phase-bearing is not only U(1) phase

The term `phase-bearing` is deliberately broader than abelian phase angle.

```text
simple face:
  U(1) phase / AB holonomy / scalar interference

richer interiors:
  non-abelian holonomy
  mode mixing
  representation transport
  path-ordering
  KMS analytic periodicity
```

The Unruh case uses phase-bearing relatedness through field correlations and their analytic / periodic structure under accelerated pullback. It does not reduce the entire phenomenon to a single U(1) phase.

---

## 12. What B6 updates in A1 §11.4

Replace the parent Unruh summary with this sharper form:

```text
Unruh / Rindler [machinery-routing; PB-4a sharpened]

The invariant layer is not particle content but field relatedness: phase-bearing
structure represented by vacuum correlations and made consequence-capable when
coupled to a detector. Pulling that relatedness back onto different flow-worldlines
yields different renderings. Along a uniformly accelerated worldline, the pulled-back
two-point function has KMS / imaginary-proper-time periodicity, so the detector
response is thermal with T_U = ℏ a/(2π c k_B), a value derived by QFT. The framework
does not derive the coefficient. It derives the role-route: phase-bearing relatedness
→ detector coupling / consequence-capacity → flow-sampling → thermal test →
temperature rendering → possible uptake/write.

This strengthens PB-4a: rendering is worldline-set, observer-free. It does not
confirm PB-4-full: Unruh still supplies rendering, not constitution-completion.
```

---

## 13. Findings

1. **Unruh remains PB-4a, not PB-4-full.**  
   It sharpens observer-free worldline rendering. It does not by itself prove constitution by frame-process.

2. **The exact temperature value is externally owned.**  
   QFT owns the Wightman function, detector response, KMS theorem, and coefficient.

3. **The temperature-computation machinery is role-routable.**  
   Once influence is read as consequence-capable phase-bearing relatedness, the Unruh computation has natural role-slots: relatedness, detector coupling, flow-pullback, thermal/KMS test, temperature parameter, possible uptake.

4. **CMB/redshift is the sibling, not the same case.**  
   CMB temperature is a real radiation aggregate rendered by a congruence. Unruh temperature is vacuum relatedness rendered thermally by accelerated access. Both reject one-place in-flight temperature.

5. **Temperature is below information.**  
   Temperature is a rendering/response scale. It becomes informational only when an ordered consequence is taken up in a flow-bearing record.

6. **Hawking is a controlled contact.**  
   Hawking temperature belongs to the same horizon/access temperature-family, but B4 still blocks over-reading Hawking/Page/QES as sealing the information-loss bet.

---

## 14. Compact result

```text
Relatedness:
  bare connection / substrate

Influence:
  consequence-capable phase-bearing relatedness

Unruh:
  vacuum phase-bearing relatedness coupled to a detector
  and pulled back onto accelerated flow
  → KMS periodicity
  → thermal response

Temperature:
  flow-indexed response scale of accessible relatedness / mixedness

Information:
  ordered influence taken up in flow at application scale
```

Or, in one line:

```text
Temperature is not information; it is the flow-indexed rendering scale by which
accessible relatedness can become informationally consequential.
```

Status: promoted as B6 working correction. Parent integration owed after cold read.
