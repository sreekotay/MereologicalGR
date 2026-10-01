# Seam vacuum: does content vacuum energy leak through the seam?

Owed by `workbench/gravity-corner` §3. Referees: `seam_vacuum.py` (8/8) and `which_cone.py`
(8/8).

**Answer: it depends on the realisation, and running the check turned up a larger problem.**
The realisation c9 actually computed does not carry C1's observable.

---

## The leak, realisation by realisation

The flow-free gravity composition makes vacuum energy invisible at the corner only when vacuum
energy is proportional to the metric gravity is built from (gravity-corner §2). That protection
survives the seam **if and only if `√(−g̃)/√(−g)` is constant on-shell.**

| realisation | ratio constant? | leak | check |
|---|---|---|---|
| **R1** c1 toy with `n` tracking the congruence (unit-norm aether), constant B | yes, `A²√(1−B)` | none. The `n⊗n` piece is absorbed by the aether's Lagrange multiplier, `λ → λ − ρA²B/(2√(1−B))`, and the rest is an ordinary CC | R1a–d |
| **R2** c9's singly-coupled Hassan–Rosen, matter on `g` | trivially (matter shares `g`) | none. `ρ_vac` enters only as `ρ_vac + m²β₀`, and the branch function `G(y)` has no β₀ | R2a–c |
| **R3** single metric, B state-sourced (Horn C's tracking drag) | no | **yes**: a force `−ρA²B′/(2√(1−B))` on the state. With B ~ 10⁻¹⁶: ~10⁴⁴ ρ_crit at a TeV⁴ vacuum | R3 |
| **R4** doubly-coupled bigravity (matter on `g_eff = α²g + 2αβ gX + β²f`) | no | **yes**. `√(−g_eff) = √(−g) Σ α^{4−n}β^n e_n(X)`, so ρ_vac shifts β₁…β₄, all of which enter `G(y)` | identity already in `two-metric-seam/portal_protection_check1.py` |

**Correction to gravity-corner §3.** I wrote that in c9's realisation "β₄ enters the background
ratio, so CC tuning becomes cone-ratio tuning." That is wrong for c9. Matter is on `g`, so its
vacuum renormalises β₀, and β₀ is absent from the branch function. The cone-ratio statement
holds only in R4.

**What the leak costs where it is real (R3, R4).** It is not a new fine-tuning count. Matter
loops generate the content-frame volume operator (`√(−g̃)` or `√(−g_eff)`), and a counterterm
of that same operator cancels the whole leak. So the CC tuning is relocated, not multiplied:
**it must sit in the content frame.** What is lost is the free protection. In R1 and R2 a
trace-free/unimodular structure keeps vacuum energy off the corner whatever its size. In R3 and
R4 it reaches the corner at O(B) unless tuned. **Horn C, the state-tracking drag, gives up the
unimodular protection.** That is a price, not a kill.

## The larger finding: c9's realisation does not carry C1's observable

C1's whole content is that photons and gravitational waves ride different cones. GW170817's
1.74 s is read as propagation at `ε ≈ 3.8×10⁻¹⁶`. In singly-coupled bigravity (R2), matter
sources only its own metric's tensor mode and is detected only through it. At LIGO frequencies,
`k/m_FP ~ 10¹²`, so the propagation eigenbasis is the cone basis and mass mixing is negligible:

```text
matter-sourced GW at 100 Hz, m_FP = 1.4e-25 eV, alpha = M_f/M_g in {1e-3 ... 1e3}:
  f-content of the mode          1e-26 ... 1e-10
  (v - c_matter)/c                ~1e-31 ... 6e-26
  fabric-cone offset needed       5e-17 (B = 1e-16)          -> rides the matter cone   (which_cone.py)
```

**In R2, GWs and photons share a cone, and C1's delay is zero at any α.** The literature agrees:
singly-coupled bigravity is not constrained by GW170817 for exactly this reason. The
doubly-coupled class is, and GW170817 forces it to proportional backgrounds or back to single
coupling (Akrami–Brax–Davis–Vardanyan 2018).

There is also a labelling tension. c9 calls the wider f-cone the fabric, and matter couples to
`g`, which also carries the dominant Einstein–Hilbert term at α → 0. In c9's realisation,
gravity in the observed sense rides the content metric. That inverts c1's *"gravity IS fabric,
matter RIDES content."* The fabric is a hidden massive spin-2 sector at Planck mass αM_g.

## Assembled

| realisation | carries C1's observable | B state-sourced (Horn C) | vacuum protection |
|---|---|---|---|
| R1 aether, constant B | yes | no | kept |
| R3 single metric, B(state) | yes | yes | lost at O(B) |
| R2 singly-coupled HR (c9's) | **no** | yes | kept |
| R4 doubly-coupled HR | yes, GW170817-squeezed | yes | lost at O(B) |

No row has all three. c9's existence result ("seam exists-modified on the bimetric finite
branch") and C1's observable live in different realisation classes. **c9 shows that the seam
exists in R2. C1 needs R1, R3 or R4.** The two would meet only in a doubly-coupled or
single-metric realisation, and there the state-tracking drag costs the unimodular protection.

## Status and limits

- The leak table is exact algebra (R1–R3) plus a published identity (R4).
- `which_cone.py` is an order-of-magnitude two-mode model. It uses a flat dispersion, a
  proportional-background mass matrix, and no Hubble friction. The structural point does not
  depend on those details: at `k ≫ m_FP` matter emits and detects on its own metric.
- Not checked: whether c9 means matter to couple to `f`, which would contradict
  `bianchi_seam_branch.py`'s *"matter couples to g only"*. If it does, that script's constraint
  derivation needs re-running with the matter term moved.
- **Corpus items flagged, not edited:** c9's existence-gap paragraph (which realisation carries
  the timing observable); c1/c9 fabric labelling; gravity-corner §3, corrected by this note.
