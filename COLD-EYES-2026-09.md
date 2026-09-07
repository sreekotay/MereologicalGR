# Cold-Eyes Read — September 2026

*External audit pass. Not canon, not a note in any lane, not graded by A0 §11. Written by a
reader given the whole corpus and no prior stake in it. The corpus's own vocabulary is used only
where refusing it would cost precision.*

---

## What the thing is

A single-author foundations workbench (~600 KB of markdown, 14 workbench directories) arguing
that GR's success is compatible with GR's formalism having **bundled several distinct roles into
one geometric object**, and that naming those roles — ordering, influence, flow, adjacency,
rendering, uptake, constitution — buys constraints when the grammar is exported to seams where GR
is silent and another closure (QFT, thermodynamics, cosmology) takes over.

The seed is one clean observation: along a null geodesic `dτ = 0`, yet causal ordering and
effect-capacity survive. Therefore `cause ≠ flow`. Everything else is built out from that corner.

Three layers, explicitly separated by the repo itself:

- **A/B notes** — the grammar and its application to known phenomena. Relabels inside GR by design.
- **C notes (c1–c10)** — the "seam": the one place the corpus exports new physics. Marked not canon.
- **D notes (d1–d2)** — occupancy: dark matter as fabric-side residence. Doubly conditional.

---

## What is genuinely good

**The epistemic apparatus is better than the field it's competing in.** The corpus names its own
failure mode (*relabel*), grades every claim, disowns coefficients, separates calibration from
fitting, marks forced / chosen / imported / parked, and prints could-fail conditions next to each
bet. `diagnostic-ledger.md` §12 states plainly that most rows are one of four *low-weight* forms.
`USES.md` adds a sterility criterion — a definition that stops locating anything gets demoted.
Very little alternative-foundations writing does any of this.

**The workbench is real.** `recognition_lemma.py` runs and passes 26/26; the underlying algebra
(for `g̃ = A(g + B u⊗u)`, the mixed tensor `C = g⁻¹g̃` has eigenvalue `A` triple on `u^⊥` and
`A(1−B)` simple on `u`, so `(A, B, u)` is recoverable from the pair, with the Kerr–Schild null
class separated by Jordan structure rather than eigenvalues) is correct. `abund.py` reproduces
standard cosmology correctly, including the neat `T_NR = 2 m_χ T_reh/m_φ = 1.16 eV / Br` result.

**Citations survive spot-checks.** arXiv:2601.22238 is the LBT Y_p paper and is characterized
accurately; arXiv:2306.04373 is the deep LIGO/Virgo–GBM multimessenger search and is used for
what it actually says. No fabricated references found in the sample.

**Several individual observations are correct and cleanly put**: record ≠ constitution (a3 —
Quantum Darwinism diagnostics are state functionals and cannot locate a commit); kernel ≠ carrier
(b1 — virtual lines are not tiny particles); rendered ≠ constituted (b6 — an Unruh temperature is
a response scale, not a bath). None of these are new. All are stated better than usual.

---

## Where a cold reader pushes back

### 1. The load-bearing empirical move is the weakest link

`c1` re-reads GW170817's 1.74 s GW–GRB gap as **propagation** rather than emission delay, giving
`c_grav/c_light = 1 + ε`, `ε ≈ 3.8×10⁻¹⁶`. The note is careful — it says one event cannot split
the gap, and that the conventional reading is a closure, not a measurement.

That is true as stated and still too generous to itself. The jet-breakout delay is not merely "a
model fitted to keep c_grav = c" — it is an independent expectation from short-GRB physics that
predicted a delay of roughly this size for reasons having nothing to do with graviton speed. The
corpus treats the two closures as symmetric competitors; they are not. And the corpus's own
CD-1 row concedes the point: *"the only row expected to lose."*

Everything downstream — c3 through c9's entire formal apparatus, and the whole D-lane — hangs
off a number the authors expect to be taken away.

### 2. The new physics is a known model class

The seam, stripped of vocabulary, is a **constant disformal deformation to a fixed unit timelike
`n`** — Bekenstein 1993, with `ε = +α_T/2` in the EFT-of-dark-energy basis, in Einstein-aether
territory. The corpus cites all of this honestly (c9 Layer 3 is scrupulous). So the novelty claim
is not the model; it is the *route* — that a role decomposition forces this corner rather than
selecting it from a zoo. That is a real claim, but it is a claim about derivation lineage, and
lineage claims are exactly the ones an outside reader cannot check and will not credit.

### 3. The costs are priced honestly and are severe

c1's own Costs section says: Horn A is explicit Lorentz violation with `∇^μT_μν = O(B) ≠ 0`
against Bianchi, and a globally fixed `n` doesn't exist off flat space — so the field is either
flat-patch-honest or covertly dynamical (aether, new dof, unearned ghost disclaimer). Horn B has
**no priced realization at all**. Naturalness runs `ε` to O(1) absent a custodial symmetry at
~2×10¹¹ GeV. Cost 0 concedes that A0's `ordering` role itself has to fork into fabric-ordering
and content-ordering to make the note work, and that this fork is *chosen, coined in the note,
unaudited upstream*.

That is an unusually candid list. It is also, read coldly, a list of reasons the construction
does not currently stand.

### 4. PB-1/PB-2 — the corpus's own designated crux — has not moved

CLAIMS is explicit that `influence` is the one owned primitive with no anchor in the held-fixed
substrate, and that PB-1/2 therefore carry the heaviest could-fails. The designated *favorable*
witness was b9's many-body Lieb–Robinson cone. The July 2026 entry records what happened: the
ceiling **collapsed to c, as relativity demands**, and "the witness relocates to the bound/realized
split." That relocation is logged in the open, which is to the corpus's credit — and it is still
a moved goalpost. PB-2 remains ordinal, with no measure, no bound, and no number. The cascade
clause in Tier B says what follows if nothing downstream forces a distinct route: the architecture
reduces to relabel. Nothing has yet fired against that clause in either direction.

### 5. Falsification inventory is thinner than the ledger's volume suggests

Of the 11 CD rows and 4 DR rows:

| class | rows | comment |
|---|---|---|
| expected to lose | CD-1 | the lane's stated main export |
| standing forever-nulls | CD-2, CD-3, CD-4, DR-1, DR-3 | killable only by a positive; no null ever settles them |
| needs far-future data | CD-5, CD-6, CD-10, CD-11 | N ~ 10³–10⁵ sirens; lab measurements that don't exist |
| dormant / superseded | CD-7 | band closed by LBT; anomaly migrated to the rejected side |
| **decidable now from archives** | **CD-8, CD-9** | GBM × GWTC subthreshold re-ranking; sidereal Bell/QKD archives |
| **decidable on one experiment** | **DR-4** | CMB-S4 σ(N_eff) ≈ 0.03 vs a generic ΔN_eff ≳ 0.05 |

Five rows that no observation can ever confirm is a lot of ledger for a small amount of exposure.
The three bolded rows are the corpus's real near-term product, and two of them cost only
re-analysis of data already taken.

### 6. Provenance and verification

All 50 commits are authored `Claude`, dated 7–12 July 2026, opening with a bulk import of the
already-written A/B corpus. The C lane, the D lane, and thirteen of fourteen workbench
directories were produced in five days. Every referee script was written by the same process that
produced the claims it referees; every audit pass ("fresh-eyes", "cold-read", this one) is
internal. No domain physicist appears to have read c1 or c9.

This is not an accusation of error — I checked what I could and it held up. It is a statement
about what the corpus's confidence currently rests on, which is internal consistency at very high
volume. Internal consistency is exactly what a well-run private vocabulary produces whether or
not it is tracking anything.

### 7. The prose has crossed a threshold

The private vocabulary now runs to several hundred terms (fabric/content, seam, lock, invoice,
fold, tine, register, tier, cashed, strand, drag, arity, engagement, peeling). TONE.md forbids
defining a term by nearby terms from the same private vocabulary; large stretches of c8–c10 and
d1 do it anyway. CLAIMS.md's "Last aligned with corpus" footer is a single ~2,000-word run-on
sentence — unusable as a changelog by anyone, including its author.

The apparatus for grading results has grown larger than the results being graded. That is a
recognizable late-stage failure mode for solo research programs, and it is worth naming before it
consolidates.

---

## Bottom line

A disciplined, self-aware, genuinely well-organized program whose framing exceeds its yield.
The grammar mostly re-describes what causal-structure theory and quantum measurement theory
already say, in a vocabulary only this repository speaks. The one place it exports new physics is
a known disformal/aether model class, arrived at by an interesting route, hanging on a single
degenerate number its own ledger expects to lose, with the two realizations of it either
Lorentz-violating-and-non-conserving or entirely unwritten.

The corpus is unusually good at saying what would kill it. It has not yet run the cheap tests
that could.

### If I had to pick three things

1. **Run CD-8 and CD-9.** Both are re-rankings of existing archives. They are the only claims here
   that could produce a surprise this year, and they cost telescope time of zero.
2. **Get c1 and c9 in front of one outside relativist.** Specifically the Horn A conservation
   problem and the Cost 0 ordering fork. If those are fatal, everything downstream should stop
   accruing before more of it is written.
3. **Freeze the vocabulary and cut it by half.** Nothing in the last three commits' worth of new
   terms did work that plain language couldn't. The sterility criterion in USES.md already
   licenses this — apply it to the terms, not just the definitions.
