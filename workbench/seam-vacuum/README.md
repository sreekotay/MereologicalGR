# Seam vacuum: does content vacuum energy leak through the seam?

Owed by `workbench/gravity-corner` §3. Referees: `seam_vacuum.py` (8/8), `which_cone.py` (8/8),
`band_scan.py` (5/5).

**Answer: it depends on the realisation.** In c9's own realisation, the GW face of the seam
moves out of the LIGO band and into the mHz and lower bands.

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

## Side finding: where c9's realisation shows its seam in gravitational waves

The bets are independent probes. Nothing requires C1 and c9 to share one model unless one of
them fails. So this section asks a narrower question: **what does c9's realisation itself
project for gravitational waves?** (`which_cone.py`, `band_scan.py`, 5/5)

In singly-coupled bigravity, matter sources only its own metric's tensor mode. The wave it emits
has fabric-cone (f) content of about `α m²/(k²B + m²)`. The crossover sits where `k²B ~ m²`:

```text
f* = m_FP / (2πħ √B)  ≈ 3×10⁻³ Hz     (m_FP = 1.4e-25 eV, B = 1e-16)

band      f          f-content (α = 1e-3)    f-content (α = 1e-2)
LIGO      100 Hz     1e-12                   1e-11
DECIGO    0.1 Hz     1e-6                    1e-5
LISA      1 mHz      9e-4                    9e-3
PTA       10 nHz     1e-3 (saturates at α)   1e-2
```

- **LIGO band.** The emitted wave rides the matter cone, offset ≲ 10⁻²⁵ (`which_cone.py`, for α
  from 10⁻³ to 10³). c9's realisation therefore does not carry the GW170817-band delay C1 reads.
  That is a scope fact about the realisation, not a failure of C1, which is its own bet. The
  literature agrees: singly-coupled bigravity escapes GW170817 for this reason, and
  doubly-coupled bigravity is squeezed by it (Akrami–Brax–Davis–Vardanyan 2018).
- **Below about f\*.** An O(α) admixture rides the wider fabric cone. Because matter both
  emits and detects through `g`, the strain modulation is about 2α²: α emitted times α detected. This is bigravity's GW-oscillation phenomenon, which is prior
  art for the mechanism. **What c9 adds is the location.** The crossover is set by the seam
  itself, `f* = m_FP/√B`, and with c9's numbers it lands in the LISA band.
  `band_scan.py` uses a flat B = 10⁻¹⁶. The c9-consistent version, with `B = 6(H/m_FP)²`, is
  `two-metric-seam/gw_oscillation.py`: f\* ≈ 1.35 mHz, carried into c9 and CLAIMS as CD-12. This is a projection
  of c9's realisation, with LISA and PTA as the bands where it could be wrong.
- **Scope note for c9's text.** *"every timing observable sees the pure seam"* is true of the
  cones. In this realisation, though, LIGO-band GWs carry no messenger on the fabric cone, so the
  seam is seen only below about f\* and at amplitude about α.

On labelling: in this realisation matter's metric also carries the dominant Einstein–Hilbert
term, and the "fabric" f is the weakly coupled massive sector. This is noted, not judged. The
mapping of c1's words onto c9's realisation is the author's call.

## Status and limits

- The leak table is exact algebra (R1–R3) plus a published identity (R4).
- `which_cone.py` is an order-of-magnitude two-mode model. It uses a flat dispersion, a
  proportional-background mass matrix, and no Hubble friction. The structural point does not
  depend on those details: at `k ≫ m_FP` matter emits and detects on its own metric.
- Not checked: whether c9 means matter to couple to `f`, which would contradict
  `bianchi_seam_branch.py`'s *"matter couples to g only"*. If it does, that script's constraint
  derivation needs re-running with the matter term moved.
- The admixture amplitude uses a proportional-background mass matrix. The real FRW mixing
  carries `y` and `X` factors of order one. The crossover's scaling `m_FP/√B` is the robust part.
- **Corpus items flagged, not edited:** the scope of c9's "every timing observable" sentence;
  the LISA-band projection, if wanted as a c9 row; c1/c9 fabric labelling; gravity-corner §3,
  corrected by this note.
