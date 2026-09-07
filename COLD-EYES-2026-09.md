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

**The A/B lane contains derivation-shaped results, and they are the corpus's strongest material.**
The program is stated plainly in the README — *a relabel inside GR by design, an exported
constraint system outside it; GR held fixed, other closures not* — so the right test is whether
the unfused grammar **derives features the non-GR closures impose as axioms**. Against that test:

- **Microcausality relocated from axiom to consistency condition** (b1 §5.1 + c8's frame-entry).
  Response theory needs an *after*: `R_AB(x,y) = iθ_u(x⁰−y⁰)⟨[A(x),B(y)]⟩`, and the θ imports a
  congruence — so θ_u is covariant *only where the commutator already vanishes*. Microcausality
  stops being a desideratum imposed to prevent signaling and becomes the condition under which
  response functions are frame-independent objects at all. Stronger than the textbook motivation.
  Paired with b1's two-leg decomposition it also explains what textbooks wave past: why
  microcausality coexists with non-vanishing spacelike Wightman/Feynman support. Halo is
  substrate (symmetric, pre-ordering, unorientable); cone is orientation. The support table across
  the two-point zoo is then predicted from leg content rather than tabulated.
- **The engagement onset map** (c8) — ~13 peeling e-folds for 10% thermality, ~42 for 1%, hot-side
  finite-time bias, Wien tail floored by switching smoothness. The literature handles adiabaticity
  case-by-case per field; this is a universal budget in generator-drift form. A number, not a reading.
- **The two-leg lock** (CD-11) — Unruh thermality as a forced coth ratio between the relatedness and
  influence legs, verified exactly in the scalar register (13/13; influence leg bit-for-bit
  invariant, symmetric leg moved by exactly a Planck spectrum).
- **Layer sorting** (a4/a5) — predicts *which* readout moves under a preregistered factorial.

Against those, a3 (record ≠ constitution) and b6 (temperature ≠ bath) are limitation results and
re-readings rather than derivations — correct, well-stated, in a known genre.

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

### 2. The C-lane seam is a known model class — and this verdict does NOT transfer to the A/B lane

The seam, stripped of vocabulary, is a **constant disformal deformation to a fixed unit timelike
`n`** — Bekenstein 1993, with `ε = +α_T/2` in the EFT-of-dark-energy basis, in Einstein-aether
territory. The corpus cites all of this honestly (c9 Layer 3 is scrupulous). The novelty claim
there is the *route*, not the model.

Scope matters: this is a verdict on c1/c9's cone model, not on the grammar's derivations above.
They are different claims with different standings, and the A/B lane is the better of the two by
a distance.

### 2b. The real limit on the derivations: lineage is unauditable from outside

Every item in the derivation list has one form: **GR's cone + a composition rule ⇒ a feature the
other closure imposes separately.** The composition rules — relatedness precedes ordering and so
cannot be oriented; influence composes with orientation — were written by someone who already
knew the targets. From outside, "the carve forced this" and "the carve was shaped to land here"
are not distinguishable. That is not an accusation of bad faith; it is a structural limit on what
any reader can verify, and the corpus names it itself (*chronology is not evidence; lineage is
the criterion*).

The corpus's own answer is the correct one — pre-register forward exposure, because the
retrodictive lane cannot settle itself. The consequence is a weighting: **the value of the A/B
derivations is hostage to the forward rows.** b1's could-fail (*a threshold detector ever firing
early kills the tier resolution, and the cone-support of the influence leg with it*) is the most
valuable sentence in the A/B lane precisely because it is the one place a retrodictive result put
a real neck out.

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

A disciplined, self-aware, genuinely well-organized program with a real result class and a
verification problem.

The result class is the A/B lane: holding GR fixed and unfusing roles does produce features that
QFT imposes as axioms — microcausality as a covariance condition on response rather than a
signaling taboo, the two-point support table as role composition, the thermality budget as a
counted quantity. That is the program working as advertised, and an earlier draft of this audit
graded it against a target the README explicitly disclaims (deriving relativity) and dismissed it
in a line. Correction stands on the record.

The verification problem is that those derivations run on composition rules whose independence
from their targets no outside reader can check, and the C/D lanes — where the falsifiable
exposure lives — hang off a single degenerate number the ledger itself expects to lose, in a
model class already in the literature, with realizations either Lorentz-violating-and-non-
conserving or entirely unwritten.

The corpus is unusually good at saying what would kill it. It has not yet run the cheap tests
that could.

### If I had to pick three things

1. **Run CD-8 and CD-9.** Both are re-rankings of existing archives, at zero telescope cost. They
   matter more under the corrected reading, not less: the retrodictive lane cannot settle its own
   lineage, so the forward rows carry the whole evidential load.
2. **Get c1 and c9 in front of one outside relativist.** Specifically the Horn A conservation
   problem and the Cost 0 ordering fork. If those are fatal, everything downstream should stop
   accruing before more of it is written.
3. **Freeze the vocabulary and cut it by half.** Nothing in the last three commits' worth of new
   terms did work that plain language couldn't. The sterility criterion in USES.md already
   licenses this — apply it to the terms, not just the definitions.
