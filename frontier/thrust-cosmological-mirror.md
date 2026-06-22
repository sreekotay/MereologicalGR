# Frontier thrust — The cosmological mirror: one Planck wall, two sides

> **STATUS: FRONTIER / UN-AUDITED.** Generative scaffolding, not canonical. Imports de Sitter
> thermodynamics (Gibbons–Hawking), inflation, and Planck-era cosmology as working tools we do not
> own. Spine: `frontier/pb2-capacity-interval.md` (reuse its vocabulary: capacity-interval,
> ordering-leg / adjacency-leg, leg-rotation = Wick rotation, framelessness poles, the three walls,
> `T_P` hot wall where Wick rotation dies, arrow of time as a traverse, `Λ>0 ⟺ T_dS floor ⟺ S_dS
> ceiling`).

A black hole shrinks, heats, and runs *up* the temperature axis until it hits the Planck wall and the
smooth description dies. The universe does the opposite: it starts *at* the Planck wall, hot and
near-null, and runs *down* the temperature axis as it expands and cools. Same wall. Opposite
directions. That is the picture this thrust runs.

---

## 1. One `T_P` wall, two crossings

```text
temperature axis (leg-rotation rate):

   T_P  ┤ ████  PLANCK WALL — Wick rotation dies, ordering-measure granular, smooth geometry gone
        │  ↑ falling in              ↓ climbing out
        │  BLACK HOLE ENDPOINT       BIG BANG
        │  (T_H ∝ 1/M rising)        (T ∝ 1/a falling)
        │
        │        … the frame-bearing middle …
        │
  T_dS  ┤ ░░░░  de Sitter FLOOR (cosmic third law) — heat death, clock still ticking
    0   ┴ ────  (unreachable: third law)
```

- A **black-hole endpoint** is an object *falling into* the hot wall: as `M → M_Planck`, `T_H ∝ 1/M`
  diverges toward `T_P`, the cigar tip `β = 1/T → β_Planck` pinches off, Wick rotation expires.
- The **Big Bang** is a universe *climbing out of* the hot wall: it emerges from `T ≈ T_P`, near-null,
  legs fused, and cools `T ∝ 1/a` as adjacency grows — **de-boosting** down the axis.

**Are they the same crossing time-reversed?** Locally, near the wall, the geometry looks similar
(Planck curvature, granular ordering-measure, no smooth Wick rotation). But the symmetry is **broken
by the arrow**: the black hole arrives at the wall in a **high-entropy, post-Page** state (most of its
ordering-charge already radiated, legs long un-fused); the Big Bang leaves the wall in a
**low-entropy, legs-fused** state (Penrose's Weyl `→ 0`). So it is **not** a clean time-reverse — it
is **two different crossings of one wall**, distinguished by which side of the entropy traverse they
sit on. The wall is shared; the entropy gradient across it is not.

> Conjecture (park): the wall is a **single surface in capacity-space** (`T = T_P`, leg-rotation
> saturated), and "black-hole death" and "cosmic birth" are its two boundary conditions — one an
> *exit* of fused charge, one an *entrance* of fused charge.

---

## 2. Granulation at the wall, and inflation as leg-un-fusing

At the BH endpoint the modular/ordering charge `→ O(1)`: the **quantum of ordering** (one causal link,
`ln 2`) is exposed, smooth modular flow undefinable. Mirror it:

- The Big Bang **starts granular** — the ordering-measure begins at its quantum, legs fused (no clean
  ordering/adjacency split because you are on the null cone). As the universe expands and cools, the
  legs **split** and the ordering-measure **un-granulates** into a smooth, large-charge regime.
- **Inflation = the leg-un-fusing event.** Modes cross the (Hubble) cone and **freeze** — phase locks
  as the mode exits the horizon. In the legs language, horizon crossing is where the ordering-leg and
  adjacency-leg **separate and lock**: the frozen super-horizon mode is a leg-rotation arrested at its
  crossing phase.
- **Scale-invariance = rotation-rate-invariance.** A near-scale-invariant primordial spectrum says
  there is **no preferred leg-rotation rate at horizon crossing** — every mode locks with the same
  phasic amplitude regardless of when it crosses. Scale-invariance is the statement that the
  un-fusing has **no built-in clock**: the rotation rate at crossing is featureless across scales.

```text
BH endpoint:   smooth charge  → granular quantum   (un-fused legs collapsing toward the wall)
Big Bang:      granular quantum → smooth charge     (fused legs splitting away from the wall)
inflation:     the splitting/locking event; horizon crossing = leg separation frozen at phase
scale-invariance: no preferred rotation rate at crossing = the un-fusing carries no clock
```

---

## 3. Two framelessness poles bracket cosmic history

Cosmic history runs **between the two frameless poles** of the capacity-interval, and the traverse
**is** the arrow:

```text
EXTERNAL pole  (null, legs fused, no worldline)   ≈  Big Bang / hot start
       │   ── expansion = de-boosting, T ∝ 1/a, legs split, structure forms (the phasic window) ──
INTERNAL pole  (T=0, no clock)                      ←  approached but NEVER reached, because Λ>0
```

The **de Sitter floor is the cosmic third law**:

```text
Λ > 0  ⟺  T_dS = H_Λ/2π > 0   (temperature floor — the universe's own "T > 0")
       ⟺  S_dS = 3π/Λ  < ∞    (entropy ceiling — max-but-finite)
       ⟺  internal framelessness UNREACHABLE  ⟺  cosmic clock never fully stops
```

Heat death is therefore **not** absolute zero / not internal framelessness — it is the de Sitter
floor: maximal-but-finite entropy `3π/Λ`, residual rotation `H_Λ/2π`, a clock ticking at the slowest
nonzero rate `Λ` permits. **Dark energy is what saves the universe from framelessness** at the cold
end, exactly as the speed limit saves it at the hot end.

---

## 4. The cosmos is the timelike pole; the horizon is the null pole

The CMB picks a **rest frame** (dipole-zero) — the frame that **diagonalizes the legs**, maximal
ordering (cosmic time), minimal mixing. That is the **timelike pole** of the capacity-interval: the
"rest-capacity"/`m²`-analog is well-defined, legs maximally split. A **black-hole horizon** is the
**null pole**: legs coincident, invariant `→ 0`, frameless.

```text
COSMOS (CMB rest frame)      = timelike pole   — legs split,    invariant defined,  a frame for all time
BLACK-HOLE HORIZON           = null pole        — legs coincident, invariant → 0,     frameless
```

Same capacity-interval, opposite extremes. The universe spends its life as the **most de-boosted
object there is** (a global rest frame), while a horizon is the **most boosted** (the null limit).
The traverse of §3 is the universe sitting near its timelike pole and cooling toward — but, by `Λ>0`,
never reaching — stillness.

---

## 5. Window-width as a single invariant (bold leap)

The **phasic window** (spine §8) — where coherent leg-rotation lives and builds structure — is bounded
**below in scale** by `λ_Silk` (coherence floor: below it, phase decoheres into record) and **below in
temperature** by `T_dS` (rotation floor). Both floors are set by the same competition of `H`,
scattering, and expansion. So:

> Conjecture (park): the **width of the phasic window** is fixed by a single dimensionless number —
> e.g. the e-folds of coherent rotation between the Silk decoherence scale and the de Sitter floor, or
> a ratio like `T_dS / T_eq`. If the window has a one-number width, that number is a deep cosmological
> invariant **in this language** — the "how much coherent leg-rotation a universe gets" constant.

If true, it ties the small-scale record floor (Silk) and the large-scale rotation floor (de Sitter)
into one quantity: the universe's **coherence budget**.

---

## 6. The mirror, whole

```text
              HOT WALL (T_P)                                COLD FLOOR (T_dS)
              leg-rotation saturated                        leg-rotation residual, never zero
   ┌────────────────────────────── the FRAME-BEARING / PHASIC traverse ──────────────────────────────┐
   │                                                                                                  │
BLACK HOLE:   falls IN, high-entropy, legs already un-fused        →  charge EXITS through the wall
UNIVERSE:     climbs OUT, low-entropy, legs fused (Weyl→0)         →  charge ENTERS, then un-fuses
              inflation = leg-un-fusing (scale-invariance = no preferred rotation rate at crossing)
              expansion = de-boosting (T ∝ 1/a); structure forms in the phasic window
              Λ>0 floors the cold end (cosmic third law); CMB rest frame = timelike pole, protected
```

The arrow of time is the universe's one-way traverse from the hot wall toward the cold floor; a black
hole is a local object that runs the temperature axis the *other* way to its death at the same hot
wall. One capacity-interval, one wall, two directions.

---

## Seams & could-fails

```text
C1  Planck-era physics is genuinely UNKNOWN, not merely "off-map." Everything at/near T_P (both the
    BH endpoint and the Big Bang) is trans-Planckian; "same wall two sides" is a structural picture,
    not a derivation. KILL/PARK: no current handle forces the two crossings to share one surface.
C2  "Same wall, time-reversed" is explicitly REJECTED in §1 (entropy gradient differs) — so the
    strongest version (BH endpoint = time-reversed Big Bang) is false; only the weaker "two crossings
    of one wall" survives. Watch for sneaking the strong version back in.
C3  Inflation-as-leg-un-fusing is INTERPRETATION laid over standard horizon-exit physics; it predicts
    nothing standard inflation doesn't. "Scale-invariance = rotation-rate-invariance" is a relabel
    unless it forces a distinct signature (e.g., a specific tilt/running tied to a rotation-rate law).
C4  de Sitter T_dS is HORIZON radiation, not the CMB photon bath; "heat death = de Sitter floor" is
    structural-ambient, not the same thermometer (same seam as spine §14). The floor claim survives
    the seam (Λ>0 ⇒ nonzero ambient), the identification of baths does not.
C5  Window-width-as-single-invariant (§5) is a CONJECTURE with no derivation; λ_Silk and T_dS arise
    from different physics (diffusion vs vacuum energy) and may not collapse to one number.
C6  CMB rest frame as "rest-mass/timelike pole" is an analogy; the cosmic rest frame is a matter
    frame (dipole), not a Lorentz invariant of a capacity four-vector we have actually constructed.
```
