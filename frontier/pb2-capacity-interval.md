# Frontier — PB-2, the capacity-interval, and the ordering/adjacency legs

> **STATUS: FRONTIER / UN-AUDITED.** This is a captured exploratory thread, not a canonical note.
> It deliberately breaks corpus rules: it imports external machinery (Wald entropy, modular flow,
> the island/QES formula, causal-set horizon entropy) as *working scaffolding we do not own*, and it
> references forward and sideways freely. Nothing here is graded. Nothing here back-patches `A0` or
> `CLAIMS`. The point is to preserve a live train of thought before pruning. Survivors get audited
> and graduated into the canonical notes later; the rest stays here or is rejected.
>
> Seed question: *apply the "b1 lens" (owned / projected / imported) to PB-2 in the context of
> Hawking radiation.* What follows is where that ran.

---

## 0. The one-paragraph spine

PB-2 asks for a **measure on ordering** (it has been ordinal until that measure is earned). Running
the b1 lens on Hawking radiation, the measure turns out **not** to be a universal scalar (`c`-like)
but an **intensive, entropy/temperature-like** quantity — and more precisely the **Noether/modular
charge of the ordering (causal-time / boost) symmetry**. Ordering and adjacency behave like the two
**legs of one "capacity-interval"** (analogous to energy/momentum as legs of `p^μ`): frame-dependent
projections that **rotate into each other** under boost (relativity of simultaneity), carry a
**frame-independent invariant**, and **coincide in the null/frameless limit**. Temperature is the
**leg-rotation rate**; the rotation is literally **Wick rotation**. At a **stationary horizon**,
Wald's theorem **fuses** the ordering-charge to the adjacency-area (`S = A/4`); in **evaporation**
they **un-fuse**, and the **Page curve is the movie of that un-fusion**. Pre-Page the entropy is
**ordering-dominated** (PB-2's clean home, irreducible to adjacency); post-Page it is
**adjacency-dominated** (the per-adjacency could-fail regime). The whole picture self-predicts its
own breakdown at the **Planck temperature** (evaporation endgame), and mirrors onto cosmology
(arrow of time as a traverse between two framelessness poles, `Λ>0` as the floor that keeps the
clock ticking).

---

## 1. Selector vs measured (the first fork)

Two distinct ways ordering can be load-bearing — the original "ordering-resource" word blurred them:

- **Ordering-as-measured-resource.** Ordering supplies an *amount* in the denominator: "influence
  per N units of causal depth." This is what PB-2's "measure on ordering" gate always meant.
  Candidate contact: metrology decode-depth (a4 §6). Could-fail: **substitutability** (depth ↔
  count at the same Heisenberg bound).
- **Ordering-as-selector.** Ordering supplies no amount; it supplies a **constraint that picks which
  configuration is realized.** The measured thing stays a count (area, entropy), but *which* count
  is physical is fixed by a causal/ordering condition. Candidate: the island/QES `ext` over causal
  surfaces. Could-fail: collapses to a generic geometric extremum (then it is "every variational
  principle," not ordering content).

**Scope guard:** selector only counts as PB-2 content if the selecting constraint **references causal
access** (causal wedges, homology), not merely a geometric extremum. (Resolved later in §10–§11: the
selector is the *search for the modular fixed point* when there is no Killing one.)

---

## 2. The measure is entropy-like, not c-like

`c` is the **kinematic** exchange rate for `(space, time)` and is universal *because* it is kinematic.
Influence and ordering are **not** a kinematic pair — they are a **thermodynamic/informational** one.
Their exchange is **entropy-like**: dimensionful, bounded, directional, state-dependent. A conjugate
pair, not a light-cone slope.

```text
c : (space, time)        :: kinematic constant (universal)
[measure] : (influence, ordering) :: thermodynamic / bounded (NOT universal)
```

This dissolves "c-envy" from the right side: the reason there is no universal scalar is the same
reason there is no universal entropy value — entropy is a functional of state. The bet **narrows**
and becomes two-sided falsifiable:

- if the influence/ordering relation turns out to be a universal constant (`c`-like) → entropy-form wrong;
- if it stays purely ordinal forever (no units, no bound, no conversion law) → measure never existed.

Earn-condition for the measure: **units + a bound + a non-degenerate conversion rate**.

---

## 3. It is temperature/information-like — and the compositions already said so

PB-2 is a **"per" quantity** → an **intensive** variable. The intensive conjugate to entropy is
**temperature**. Dimensionally:

```text
influence per ordering-resource  =  energy per entropy  =  dE/dS  =  temperature
```

The existing role-compositions already encode the first law `dE = T dS`:

```text
gravity      = ordering + influence + energy-momentum     ← carries E (energy-momentum sector)
information  = ordering + influence + flow                ← carries S (ordering) and T (flow-indexed)
                                                            influence = the SHARED hinge term
```

`T` showing up as **flow-indexed** is exactly what b6/b4 already derived: `T = κ/2π` with `κ` the
frame-transport/access scale. So the two big carves are **the two sides of `dE = T dS`, joined at
influence**, and PB-2 sits on the `T = dE/dS` hinge. We assembled the conjugate structure piecewise
(energy = flow-conjugate in a2; temperature = κ in b6/b4; entropy = ordering here) without naming it.

---

## 4. Correction: temperature is a *generic* intensive (the Unruh brake)

Temperature is **not** the fingerprint of ordering. Unruh shows **adjacency and density** carry
temperature-like measures too (horizon/acceleration, vacuum mode-density). So "PB-2 looks
temperature-like" cannot tag ordering by itself.

**Reorder:** the ordering-specific content lives in the **extensive** (the entropy), not the
**intensive** (the temperature). Temperature is the cheap, shared, multiply-realized part; the
expensive, falsifiable part is showing an **extensive ordering-measure** not reducible to the
adjacency extensive (area) or a density extensive. This kills the bad could-fail "temperature pairs
with area → PB-2 is per-adjacency": adjacency *having* a temperature (Unruh) is expected and says
nothing against ordering having its own pair. (Also pushes toward influence = **shared coupling**,
not the `E` of any one axis.)

---

## 5. The energy-momentum "legs" metaphor

Energy and momentum are **legs of one object** `p^μ`: genuinely two, frame-dependent projections,
**rotating into each other** under boost, **coinciding in the null limit** (`E = |p|`), with a
frame-independent invariant `m² = E² − |p|²`.

Drop `(ordering-measure, adjacency-measure)` into the same mold:

```text
ONE capacity-object, two legs:
  ordering-leg   (timelike projection)
  adjacency-leg  (spacelike projection)
genuinely two, projections of one object; rotate into each other; coincide in the null limit;
carry a frame-independent invariant (interval-like "rest capacity")
```

Payoffs: explains why PB-2 is not `c`-like (a leg is a *projection*, frame-dependent by
construction); predicts an **invariant** that vanishes at horizons (null → legs coincide); and makes
**framelessness** = loss of leg-splitting (no frame → legs cannot be separated). Unifies the horizon
coincidence, the Sorkin links↔area coincidence, and PB-3/GB-3 framelessness as "you hit the null
cone." **Earn-condition for "legs": an actual transformation law mixing them + an actual invariant.**

---

## 6. The boost is real: relativity of simultaneity

The transformation that rotates ordering into adjacency is the **actual Lorentz boost**. For two
spacelike-separated events, one frame says A precedes B (**ordering**), another says simultaneous
(**adjacency**); a boost rotates one leg into the other. Ordering = timelike projection, adjacency =
spacelike projection, rapidity = the dial.

- **Invariant** is interval-like: `s² = −t² + x²`. Timelike → ordering-dominant; spacelike →
  adjacency-dominant; **null → legs coincide = horizon = frameless**; the `m²`-analog ("rest
  capacity") needs a frame and dies on the null cone.
- **Boost generator = acceleration = b7 frame-transport.** Accelerating is continuous re-boosting →
  continuous ordering↔adjacency rotation.
- **`T = κ/2π` is the leg-rotation rate.** Boost in imaginary time is a rotation that must close
  smoothly at `2π` (Euclidean conical smoothness / KMS). Temperature is the rate acceleration spins
  ordering into adjacency; the `2π` is the rotation closing.

```text
capacity-object, two legs:  ordering (timelike) | adjacency (spacelike)
boost generator:            acceleration = frame-transport (b7)
mechanism:                  relativity of simultaneity (order ↔ side-by-side)
invariant:                  interval-like "rest capacity" (needs a frame)
null cone:                  legs coincide = horizon = frameless (PB-3/GB-3, Sorkin links↔area)
rotation rate (closes 2π):  Unruh/Hawking T = κ/2π   ← PB-2's intensive
influence:                  the shared coupling this is all the bookkeeping of
```

---

## 7. The rotation is Wick rotation

```text
Lorentzian face:  legs (E,p) / (ordering,adjacency);  invariant m²=E²−p²;  boost = hyperbolic rotation (rapidity = imaginary angle)
Euclidean face:   legs (clock ω, rotation T);          invariant ω/T = PHASE; thermal = periodic rotation, closes 2π (KMS)
```

`t → iτ` carries one into the other. Rapidity is an imaginary angle; the thermal phase is the real
Euclidean angle; **the "leg-rotation" we kept invoking IS the Wick rotation.** The two
invariant-types (difference-of-squares vs ratio/phase) are the Lorentzian and Euclidean faces of one
capacity-object. Framelessness poles are where the rotation degenerates in each face (`v=c` kills the
hyperbolic one; `T=0` kills the periodic one).

---

## 8. CMB / phasic structure

The CMB is a **frozen phase photograph** carrying **two phase-closures on two cones**:

- **Thermal phase** — blackbody; imaginary-time `2π` closure; cone = light cone (`c`); intensive =
  temperature.
- **Acoustic phase** — the peaks; real-time closure on the **sound horizon**; cone = **sound cone**
  (`c_s ≈ c/√3`); intensive = sound speed.

The **sound cone** is a sub-luminal null-cone analog: a sound wave couples spatial compression
(adjacency) to time-delayed pressure (ordering) — a leg-rotation at `c_s`. So the CMB hands us a
**second cone** for free. Generalization: **phase is the primitive; temperature and sound speed are
phase-closure rates on different cones; each cone has its own horizon and intensive.**

- **Silk damping** is **not** a third cone — it is **parabolic** (diffusion, `length ∝ √t`), no sharp
  cone. It is where **phase is destroyed → record written**: the reversible leg-rotation **decoheres
  into the irreversible record** (the second law made visible as the high-ℓ damping scale). *Seam:*
  CMB Silk damping is classical photon diffusion, structurally — not literal quantum decoherence.
- **Cosmic rest frame** (dipole-zero) = the **timelike pole** (legs maximally split), opposite to the
  **null pole** of a black-hole horizon (legs coincident). `T ∝ 1/a` = the universe **de-boosting**
  (cooling = leg-rotation slowing). The hot Big Bang = near-null, legs mixed; the **horizon problem**
  is a **leg-coincidence artifact** of starting near the null cone.

---

## 9. Three temperatures, tested (accelerated two-level atom)

Unruh–DeWitt detector, gap `ω₀`, acceleration `a`:

- **Unruh** `T_U = a/2π` (from motion) and **thermodynamic** `T_thermo` (from level populations,
  `P_exc/P_gnd = e^{−ω₀/T_U}`) **coincide**.
- **Quantum-speed clock** `ΔE = ω₀` (Mandelstam–Tamm) is **independent of `a`** (set by the atom).

So three → **two**: a **rotation rate** `T` (from motion) and a **clock rate** `ω₀` (from internal
structure). The physics is in their **ratio** `ω₀/T = ω₀·β` — which **is a phase** (the
Matsubara/imaginary-time angle). **The invariant of the clock+rotation pair is a phase.** Resolution:
**two legs and an angle** — clock `ω`, rotation `T`, invariant `ω/T` = thermal phase. Confirms §7:
the thermal invariant is a phase; it is the Wick-rotation of the kinematic `m²`.

---

## 10. The extensive weld: fails naively, closes via Noether/Wald

**Test:** do `(ordering-count, area)` co-rotate like `(E, p)`? Near-horizon Euclidean geometry is the
**cigar** (`β = 2π/κ` from smoothness), and the natural coordinates are **polar**:

```text
near-horizon Euclidean plane = ℝ² (polar):
  radius  ξ   = radial distance to horizon  ← ADJACENCY (radial)
  angle   κτ  = imaginary ordering-time      ← ORDERING (the rotation)
  horizon = ORIGIN (ξ=0)
transverse (y,z) = AREA                       ← ADJACENCY (transverse), spectator
```

**First result — a clean no.** The extensive legs do **not** co-rotate: ordering is the *angle*,
radial-adjacency is the *radius*, and the **area is transverse (the fixed axis)**. Under boost the
area is invariant; the ordering-angle **degenerates to zero proper length at the origin** (the horizon
*is* the fixed point of the boost Killing field). This *derives* area-law entropy:

> Entropy is an area (adjacency) law because the horizon is the fixed point of the ordering-rotation,
> and a fixed point is a transverse surface. Ordering cannot form a horizon-extensive because the
> ordering-angle has zero extent at the fixed point.

This also explains the **Sorkin** coincidence: causal links counted *at the bifurcation surface* (the
origin, where ordering collapses onto the transverse area) reproduce area — not because ordering-count
*is* area, but because it **pierces** the area at the fixed point. Off-horizon, link-count tracks
volume/depth, not area. The coincidence is a fixed-point artifact.

**Second result — the back door closes it.** Ordering is a **symmetry** (causal-time / boost), so its
measure is a **Noether charge**. Wald's theorem:

> Black-hole entropy **is** the Noether charge of the horizon-generating (boost = ordering) Killing
> field, evaluated on the bifurcation surface; for GR it equals `A/4`.

```text
ordering-measure  = Noether charge of the ordering (boost / time-translation) symmetry
adjacency-measure = area

  BULK:    ordering-charge = energy / mass M   (≠ area)   → legs are TWO
  HORIZON: Wald forces charge|_bifurcation = A/4 = S      → legs are ONE
```

**Two legs, distinct in the bulk, identified at the horizon — fusion operator = Wald.** ("Genuinely
two, fused only at horizons," made exact.) The first law `dM = T dS` = bulk ordering-charge `M` and
horizon adjacency-extensive `S` bridged by the rotation rate `T`.

---

## 11. Modular flow unifies; selector vs measured resolved

- **Stationary:** entropy surface = fixed point of the **boost** symmetry (bifurcation surface) →
  Wald.
- **Dynamical:** entropy surface = fixed point of the **replica `Z_n`** symmetry (Lewkowycz–Maldacena)
  → the **QES / island boundary**.

Both are faces of **modular flow**: stationary modular flow *is* the geometric boost; in general it is
Tomita–Takesaki flow whose fixed point is the entangling/QES surface and whose **modular charge is the
entropy**.

> **PB-2's "ordering symmetry" = modular flow. Its modular charge = the ordering-measure. Its fixed
> point = where ordering-charge fuses to adjacency-area. Wald is the stationary face; the island is the
> dynamical face.**

This resolves §1: **selector = the search for the modular fixed point when there is no Killing one;
measured-resource = the modular charge evaluated there.** Both appear only in the dynamical case —
which is why selector never showed up in the static metrology corner.

---

## 12. The Page curve is the un-fusion movie

An evaporating horizon has no exact Killing field / clean bifurcation surface, so Wald fusion cannot
stay exact — the legs **un-fuse**:

```text
S_rad(t) = min( S_ordering , S_adjacency )

  rising  S_ordering  = ordering-charge accumulated in the radiation
                        (entanglement built in causal-emission sequence; radiated M streaming out,
                         UN-fused, carried on frameless null quanta)
  falling S_adjacency = area of the shrinking remnant (quasi-Wald-fused: charge ≈ area)

  PAGE TIME = the crossing  S_ordering = S_adjacency  = a fixed-point JUMP (no-island → island)
```

- **Pre-Page:** ordering-leg smaller → entropy is **ordering-dominated** → **PB-2's clean home,
  irreducible to adjacency**. The per-adjacency could-fail **does not fire here**.
- **Post-Page:** adjacency-leg smaller → area/island controls → the per-adjacency could-fail regime.
- **Page turnover** = the dominant replica saddle jumps → the modular fixed point **discontinuously
  relocates** to the island (the kink in the curve).

A black hole = a **temporary fusion** of ordering-charge and adjacency-area: forms (fuses), radiates
(un-fuses), and the charge — never destroyed, only fused then freed — goes back out.

---

## 13. Framelessness has two faces (and the third law is the mirror of the speed limit)

A frame needs a **worldline** (timelike direction you move along) and a **clock** (internal change
that ticks). Kill either → frameless.

```text
EXTERNAL framelessness:  null / massless, v=c, τ=0           — no worldline (too fast)
INTERNAL framelessness:  T=0 / ΔE=0, stationary ground state — no clock (too still)

external frame-protection:  v < c  always   ← special relativity
internal frame-protection:  T > 0  always   ← third law
                MASS = has both, walled off from both poles
```

Rigor hook: **quantum speed limit** (Mandelstam–Tamm), clock period `~ ħ/ΔE`. `T=0` ground state →
energy eigenstate → `ΔE=0` → no tick → internally frameless. A massive worldline *defines* a proper
time → forces `ΔE>0` → `T>0`. **Mass keeps the clock running** (the third law in MGR terms). Photon:
`τ=0`, already clockless (external version of the same nothing).

---

## 14. Cosmology: the traverse between the poles

The universe is one object **between the poles**, but unlike a particle it **begins at one and
traverses toward the other** — and that traverse **is the arrow of time**.

```text
Big Bang        = EXTERNAL pole (near-null, hot, legs fused) — the cosmic "v=c" start
de Sitter future = INTERNAL floor — approached, never reached, because:

  Λ > 0  ⟺  T_dS = H_Λ/2π > 0 (temperature FLOOR)
         ⟺  S_dS = 3π/Λ < ∞   (entropy CEILING)
         ⟺  the universe can never reach internal framelessness
         ⟺  cosmic clock never fully stops  ⟺  CMB rest frame protected forever
```

So **heat death is not absolute zero** — it is the de Sitter floor (max-but-finite entropy `3π/Λ`,
residual temperature `H_Λ/2π`). **Dark energy is what saves the universe from framelessness** — it
keeps the worldline expanding and the clock ticking. Penrose's Weyl hypothesis fits: external pole
(null, legs fused, smooth, `Weyl→0`) = low gravitational entropy; de Sitter horizon = the maximum.
The arrow is gravitational entropy climbing from the fused-legs Big Bang to the de Sitter ceiling.

---

## 15. Evaporation endgame: the framework predicts its own death

`T_H = 1/(8πM)` **rises** as `M` falls — the endpoint sprints toward the **hot** pole, walled at the
**Planck temperature** `T_P` (a **third wall**: maximal leg-rotation, where `β → β_Planck`, the cigar
tip goes Planckian, and **Wick rotation itself dies**).

```text
THREE walls on the capacity-interval:
  EXTERNAL / hot pole:  v→c, T→∞   — quantum-walled at T_P (Planck)   ← cap on leg-rotation
  INTERNAL / cold pole: T→0, ΔE→0  — walled by the third law          ← cap on leg-stillness
  the FRAME lives strictly between them; the BH endpoint hits the HOT wall
```

- **Ordering-measure granulates:** as `A → A_Planck`, the modular charge → `O(1)`; smooth modular flow
  can't be defined on a few bits → the **quantum of ordering** (one causal link, `ln 2`) is exposed.
  PB-2's measure is **discrete at bottom**, and evaporation is the process that drives it to the grain.
- **Remnant vs complete evaporation:** a remnant requires the charge to stay **fused** to the area to
  the end; but the charge **un-fuses (Page)** and leaves, so the area can → 0 because it holds nothing.
  → **complete evaporation, no long-lived remnant, information returns in the radiation** (sides with
  unitarity; could-fail: a stable Planck remnant being required).
- **Honest seam:** the final `O(1)` bits (area ~ 1 bit, `T ~ T_P`) are where Wick rotation, quasi-Wald,
  and smooth modular flow all died — **the fate of the last bit is off-map.** The framework names
  exactly where it goes dark.

---

## 16. The PB-2 landing (inkable-core candidate)

> **PB-2's measure on ordering = the Noether/modular charge of the ordering (causal-time/boost)
> symmetry.**
> - **not `c`-like** — it is a charge / intensive-conjugate (config- and state-dependent);
> - **entropy/temperature-like** — at a stationary horizon it *is* the entropy (Wald); its conjugate
>   rate is the temperature;
> - **energy `M` in the bulk; `A/4` at a stationary horizon** (Wald fuses it to adjacency);
> - **un-fused and ordering-dominant in the pre-Page branch** — PB-2's clean non-adjacency home;
> - **intensive conjugate = temperature = leg-rotation rate = Wick-rotation angle (`ω/T` phase)**;
> - **selector vs measured = found vs given modular fixed point** (QES vs bifurcation surface).

Honesty note: in the bulk the ordering-charge **is energy** — so this is a **unification** (the
ordering-measure is the Noether charge of ordering, = energy in bulk, = area at horizon), **not a new
primitive**. That is the stronger result and the most likely thing to survive an audit.

---

## 17. Seams & could-fails ledger (for the eventual prune)

```text
S1  higher-curvature Wald corrections: charge ≠ A/4 → ordering & adjacency come apart even AT the
    horizon. A place to test whether the legs are truly two. (measurable-in-principle)
S2  pre-Page branch: ordering-dominated entropy irreducible to area → PB-2's clean home. KILL if it
    reduces to an area/count after all.
S3  remnant: if a stable Planck remnant is REQUIRED (charge stays fused), the un-fusion picture is wrong.
S4  modular-flow-as-owned: modular = boost only for special states/regions (Bisognano–Wichmann);
    treating modular charge as "the ordering measure" leans hard on imported entanglement-wedge results.
S5  ordering = emission-sequence: identifying the rising Page branch with ordering-charge is an
    interpretation, not a theorem (defensible: radiated M is the bulk ordering charge leaving).
S6  quasi-stationary/adiabatic approximation breaks at the Planckian endpoint (S15 last bit off-map).
S7  three-temperatures-as-one: thermodynamic T, Unruh T, quantum-speed ΔE were treated as faces of one
    clock; clean for a single mode, unaudited in general (§9 resolves to "two legs + a phase").
S8  selector-as-generic: if QES extremization is reproducible as pure geometric extremization with no
    irreducible causal-access content, the selector mode collapses to "every variational principle."
```

---

## 18. Open thrusts (in progress)

- **Formation side** — collapse as the *fusion* event; "Page curve in reverse"; horizon formation =
  first appearance of a modular fixed point. → `frontier/thrust-formation.md`
- **Cosmological mirror** — BH endgame and the Big Bang as the *same* `T_P` wall seen from two sides
  (one object falling in, one universe climbing out). → `frontier/thrust-cosmological-mirror.md`
- **Ink core** — identify the lineage-clean core that could survive an audit today and where it would
  land (without importing modular machinery as owned). Done; folded into the live map.
  → `frontier/README.md`
