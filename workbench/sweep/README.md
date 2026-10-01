# Sweep — the exhibit test on the corpus's own derivation

A0 §11's test, turned on A0 and its descendants. For each composition: does the formula as
written demand a value while suppressing an argument it needs (*missing*), or carry one it
doesn't (*extra*)? Referee: `adjacency_is_flow_indexed.py`, 9/9.

---

## Significant

### F1 — adjacency is flow-indexed, not flow's peer

A0 §6: adjacency is *"imported from GR's metric and named as peer of flow."*

The exhibit test on `space = ordering + adjacency` returns a suppressed argument. The spatial
metric is `h = g + u⊗u`: it exists only given a unit timelike field `u` — a flow congruence.
Change the congruence and `h` changes. So separation is three-place, `(A, B, congruence)`.

Flow's magnitude needs **one worldline** (`dτ² = −g(dx,dx)`); adjacency's needs **a family**.
The dependence runs one way, and the corner-strip test (A0 §11) shows it:

```text
strip adjacency, keep flow    a single isolated worldline: proper time accrues,
                              nothing is laid out beside it          -> flow survives
strip flow, keep adjacency    the null corner: no congruence, no h,
                              no frame-free separation               -> adjacency's
                                                                        magnitude does not
```

Separable in one direction only. **This is why adjacency has no strip corner** — not an
unfinished audit but a structural fact: there is no corner where adjacency's magnitude survives
without flow, because it is defined through flow.

**Scope, and a finding inside it.** A0 gives adjacency three senses — *extension, nextness,
separation*. Extension and separation are metric and flow-indexed (above). **Nextness is
topological** — which points neighbour which — and needs no `u` at all. So adjacency is itself
a fusion of a metric part (flow-indexed, now settled) and a topological part (flow-independent,
still open). The USES witness condition — *a surface code where only geometrically aligned
pair-noise chains across the logical cut* — is a layout question, i.e. about nextness. It is
aimed at exactly the part F1 does not settle.

### F2 — the seam does not fork adjacency; c1's Cost 0 names the wrong role

c1, Cost 0: H_p1 *"forks A0's `ordering` into fabric-ordering and content-ordering, **riding on
the fabric/content adjacency carve** (chosen, coined in this note)."*

Within the corpus's own seam class — rank-1 timelike, `g̃ = A(g + B n⊗n)`, c9's recognition
lemma — computed on Minkowski and on a generic background:

```text
n-orthogonal complement under g~  ==  under g          same slice
g~(v,w) = A g(v,w) for v,w on that slice                same spatial metric, up to gauge A
g~(n,n) = A(1-B) g(n,n)                                 the time leg alone carries (1-B)
```

`A` is the conformal/volume gauge — it scales space and time alike and is not an adjacency
split. Modulo it, the two metrics **differ only along n**. All three of A0's adjacency senses
are shared: extension and separation (restricted metric) and nextness (same point set). What
forks is flow — `dτ̃/dτ = √(1−B)` — and c5 already derives that from the order pair. The cone
ratio `√(1−B)` is entirely a flow ratio.

So c1 names the wrong role *and* runs the dependency backwards. The order fork is the primitive
hypothesis; flow forks from it; adjacency does not fork. Cost 0 decomposes:

| part | content | status |
|---|---|---|
| kinematic split | two clock rates along `n` | flow, derived in c5 from the order pair |
| dynamical asymmetry ("gravity IS, matter RIDES") | which metric Einstein–Hilbert governs | imported from c1's toy action |

Neither carves adjacency. **The C/D lane does not rest on a chosen carve of the parked root role.**
Its unpaid premise reduces to the probe hypothesis itself — two cones — which is exactly what a
probe is supposed to rest on.

Downstream consistency, both favourable:

- c3's covariate *"the comoving distance over c"* is well-defined *because* adjacency is shared.
  Had it forked, "the distance to the source" would be ambiguous between sectors.
- c9's tilt/dilation split already isolates the flow component: dilation **is** the flow fork.

Downstream re-reading, not an edit: d1's "fabric-side residence" reads more sharply as
*dark-sector clocks run on g-proper-time*, not *dark matter lives on fabric adjacency*.

**Limit.** F2 holds within the rank-1 timelike class. An anisotropic or higher-rank seam would
fork spatial structure. The corpus's seam is rank-1 by c9's membership criterion, so the result
applies to the corpus's own model; it is not a theorem about every conceivable two-metric seam.

---

## Medium

### F3 — the composition formulas are written one-place; the definitions are indexed

`information = ordering + influence + flow` appears three times in A0 with no threshold. A0 §3's
prose says constitution *"demands … an external threshold that fixes the application scale."* The
headline formula is one argument short of its own definition, and the argument it hides is the
corpus's central commitment — the pinned `T`.

The same pattern runs through the influence-bearing compositions: `cause`, `information` and
`gravity` all carry `influence`, whose live use must name a ladder tier (A0 §3), and none carries
the tier in the formula.

The prose covers both, so nothing is wrong in the definitions. But the formulas are what readers
quote, and in them the corpus writes one-place notation for many-place relations — the
compression signature it exists to catch, in its own notation.

---

## Minor

- **F4.** CLAIMS' "influence = shared hinge" row says gravity and information diverge only at
  energy-momentum vs flow. But energy is E-M's flow-conjugate face, so the two divergence points
  are conjugates rather than independents.
- **F5.** `T` is overloaded: c3 uses it for the light-travel covariate, PB-4 for the threshold.
  Small, but it is exactly what the literal-terms rule exists to prevent.

---

## Clean passes

| composition / claim | why it passes |
|---|---|
| `time = ordering + flow` | flow names its argument — the worldline |
| `cause = ordering + influence` | tier governed by A0 §3; quantum branch argument named in c10 |
| `frame = ordering + flow + adjacency` | consistent with F1 — the spatial triad lives in `h(u)` |
| `gravity = … + energy-momentum` | sourced by the tensor `T_μν`, which needs no `u` |
| mass | self-supplied flow, `u = p/m`; one-place, undefined for photons — matches A1 |
| energy | `E = −p·u`, argument named in A1 §6 |
| temperature | four-place and explicit, `T(state, flow, generator, access)` |
| PB-3 | robust across all `T` — no uptake in flight at any threshold |
| PB-4 | `T` explicit, with the anti-sliding guard |
| b1 support table | claims cone-*support* state-independence, not value — correct |
| c5 one-sidedness, c7 classification | well-formed in their stated domains |

---

## What the sweep did

Two of the corpus's largest open items move. Adjacency's missing strip corner turns out to be
structural for its metric part, and the remaining open part is the one the existing USES witness
already targets. And Cost 0 — the premise under the entire C/D lane — turns out not to be a carve
of the parked role at all.

Neither result is new physics. Both are the instrument doing what the AMPS calibration said it
does: finding the argument that was suppressed — here, in the corpus's own root.
