# A4 — QEC Failure Layer Autopsy

*Working draft, June 2026.*

Status: application document / quantum-error-correction failure diagnostic.  
Primary target: A3 record-vs-constitution, A0 §3 influence ladder / compose/missing/extra, PB-3/PB-4.  
Ledger: same record/constitution seam as D4 (QD diagnostics); lab QEC is the operational mirror — not yet a separate ledger row. Published experiment map: diagnostic-ledger §14.  
Grade: post-mortem template / engine-eligible diagnostic / predictive closure map. Not a proof of QEC success or failure.

```text
Why this note:
  QEC is the cleanest lab instance of the A3 seam.
  Practice already operationalizes record, decode, commit, threshold;
  milestone language compresses them.
  A4 names the compression and routes failure — it does not specify product or decoder theory.
```

```text
Bundled headline:  "QEC failed."
A4 question:       which layer broke?
Predictive add:    which cell is open → closure or projection → forward signature
Not asked:         did MGR predict this failure?  (MGR predicts class / route, not coefficients)
```

Failed or partial runs are often more instructive than break-even wins: failure strips a role and opens the bundle (A0 degenerate corners). Success autopsies use the same checklist.

---

## 1. Layer split

```text
record:
  syndrome / flag / leakage / erasure stream made available for correction
  syndrome bits may be constituted records in the classical controller;
  they are not by themselves constituted logical information of the protected register (PB-3 targets in-flight / wrong-register constitution, not classical logging)

route / model:
  noise assumptions, graph, priors, correlation / leakage model, decoder schema

decode:
  record → recovery inference; Pauli recommendation or frame update

constitution / commit:
  logical register maintained or handed off under declared convention
  (decode output counts only when convention ties it to frame/apply/handoff)

threshold:
  application consequence scale: memory time, gate fidelity, depth, yield, budget

misread:
  tomography, postselection, offline decode, or syndrome alone counted as constitution
```

**Influence-ladder placement (A0 §3):**

```text
record:           recorded influence (syndrome stream available)
decode:           operation on that record
commit:           protected logical register under declared convention
misread:          record or diagnostic sold as constitution (PB-4)
```

---

## 2. Common failure reads

| Pattern | Bundled | Layer break |
|---------|---------|-------------|
| **Logical worse than physical** | overhead hurt | record maybe OK; uptake did not outrun error; commit below baseline at declared ε |
| **No break-even** | no logical qubit | physical/record improved; constitution still below app threshold |
| **Leakage / erasure** | decoder failed | **missing record leg** — out-of-subspace unpriced; repair = expand record (A0 missing) |
| **Correlated / non-Markov** | QEC won't scale | record exists; **route/model** wrong; distance plot misread |
| **Real-time / mid-circuit** | bad qubits | record OK; **commit delayed** or round aborted before apply — record without timely constitution |
| **Postselection / yield** | high logical fidelity | conditional threshold; constitution **rate** needs yield and discard rules |
| **Prep tomography** | logical state 99% | **misread** — record at prep ≠ memory through rounds |
| **Decoder swap** | QEC broken | **same record, different decode** — commit-linked swap tests constitution (A3); offline-only → inference or misread |
| **Model / prior swap** | noise wrong | **same record, different route** — syndrome OK; graph/prior/correlation model mismatched |
| **Magic pipeline** | magic QEC failed | distillation commit ≠ injection commit — two constitution sites |
| **Milestone debate** | we have / don't have a logical qubit | **same data, different threshold** (rounds, depth, extrapolation) |

Erasure detection is record expansion (row 3), not a separate ontology: detected erasure routes influence; constitution still at decode commit.

---

## 3. Autopsy checklist

```text
record:     syndrome fidelity; leakage/erasure/correlation logged?
route:      noise class tested, not assumed?
decode:     decoder / frame rule; online vs offline; decoder swap outcome?
commit:     register maintained T under convention C (apply vs frame-tracked)?
threshold:  app budget named (memory, gate, depth, yield, extrapolation)?
misread:    tomography / postselection / offline decode sold as memory?
```

**Verdict block:**

```text
record:     adequate / inadequate to X
route:      matched / mismatched to noise class Y
decode:     +/− latency, overhead, or error vs baseline
commit:     maintained for T under convention C
threshold:  pass / fail application A at ε
verdict:    which layer broke → repair path
predictive: open cell (missing / extra) → closure OR projection → signature (§5)
```

---

## 4. Engine-eligible tests

Hold one layer fixed; move another (A3: vary operation, not only state diagnostic):

```text
same syndrome stream     → swap decoder / priors / graph / noise model
same decoder               → vary apply latency, frame timing, mid-circuit abort rules
same physical run          → report offline decode, online decode, online commit separately
same rounds                → vary declared threshold (one gate vs memory vs depth vs yield)
same code/noise            → leakage/erasure syndromes on vs off
```

Readouts:

```text
decoder swap with record fixed     → decode/inference layer live if decoded claim moves;
                                      constitution layer only if swap feeds declared commit C
model/prior swap with record fixed → route layer live if LER moves
latency / commit timing swap       → constitution layer live if LER moves
threshold swap with commit fixed   → application scale was compressed in headline
```

```text
If logical LER tracks uptake/threshold moves with record fixed → record was not the bottleneck.
If LER tracks only syndrome quality with decoder, commit convention, timing, and threshold held fixed → record was the bottleneck.
```

---

## 5. Predictive closure

Autopsy is retrospective. Predictive MGR adds: **layer stress → open cell → closure or projection → forward signature**.

```text
closure:     complete the composition — add a missing leg, close the feedback loop,
             stop forcing a cell empty

projection:  measure the right face of imported content and feed route / decode / commit
             (not a new primitive — a rendered input the engine lacked)

MGR-owned predictions:  scaling class, cliff, correlation with named projection, degenerate-corner behavior
Externally supplied:    coefficients, optimal constants, fit-after-the-fact numerology
```

**Closure vs projection:**

```text
closure:     a role or operation was absent from the composition
projection:  a face was present in the setup but not rendered into the live engine
```

### 5.1 QEC predictive table

| Layer stress | Missing / extra | Closure (new direction) | Projection (measure & feed) | Predicted signature |
|---|---|---|---|---|
| **record** inadequate | **missing** leg | expand channel (leakage / erasure / flag syndromes) | leakage rate, erasure rate vs code distance | LER improves only when missing leg was dominant; slope vs distance unchanged if decode+commit OK |
| **route** mismatched | **extra** noise or **missing** correlation model | close route cell: correlated / non-Markov model in decoder | correlation length, leakage graph, prior class | pseudo-threshold in distance plots; LER tracks model swap with record fixed |
| **decode** weak | **missing** policy / decoder depth | swap decoder or graph; mid-circuit decode policy | decoder identity, offline vs online decode bit | decoded claim moves with swap; logical LER moves only if swap feeds commit C |
| **commit** open / delayed | **missing** timely apply | close feedback loop; mid-circuit apply; abort rules | τ_dec / τ_cyc, τ_apply / τ_coherence | **cliff** when latency ratio → 1; good syndromes + dead memory |
| **threshold** compressed | **extra** unnamed scale | close accounting: rounds, depth, yield, extrapolation | yield, discard rate, declared ε | headline moves under threshold swap with commit fixed |
| **misread** | **extra** inference as constitution | require offline / online decode / online commit separately | tomography at prep vs memory through rounds | gap persists between offline bound and register constitution |

### 5.2 Degenerate corners (class predictions)

Strip one cell before the run; predict scaling **class**, not a fitted ε (A0 degenerate corners):

```text
strip commit (offline decode only)     →  logical LER tracks decode, not memory claim
strip decode (syndrome-only headline)  →  no correction path; record-quality ceiling
strip leakage from record              →  distance plots misread; route blamed wrongly
strip threshold naming                 →  milestone debate only; no layer verdict possible
```

**Uniform success is a failure signal** (A0 §7): if every decoder and latency achieves logical break-even, the layer split was never stressed.

### 5.3 Preregistered bundles

```text
Bundle A — degenerate corners:   strip one cell; predict class (e.g. offline-only → decode-limited)
Bundle B — projection witnesses:   name projection before run; predict residual correlation
Bundle C — composition closure:    close only the failed cell; predict other layers unchanged
```

---

## 6. Metrology mirror (closed-loop engine)

Same grammar on a **parameter register** instead of a logical qubit. QFT-adjacent closed-loop work (adaptive phase estimation, homodyne feedback, real-time control) is the reference family; diagnostic-ledger §14 maps published contact.

**Layer map:**

```text
record:     clicks / trajectories / homodyne trace / heralded outcomes
route:      noise model, prior, visibility, back-action, pass index
decode:     estimator / Bayesian update / adaptive policy
commit:     control actually applied before next segment (θ, detuning, kick)
threshold:  resource law (passes vs photons vs bandwidth), ε, SQL/HL class
misread:    Fisher / CR bound on ρ sold as closed-loop precision
```

### 6.1 Metrology predictive table

| Layer stress | Missing / extra | Closure | Projection | Predicted signature |
|---|---|---|---|---|
| **record** | **missing** pass tag / herald | expand record (coincidence, pass index) | detected vs intended pass count | scatter width drops; HL slope unchanged if decode+commit OK |
| **route** | **extra** unmodeled noise | pass-indexed noise in update | visibility V(p), drift vs pass count | residual at max N tracks 1/V(p); not HL slope |
| **decode** | **missing** policy depth | raise M or richer sufficient statistic | policy label M, stat dimension | SQL → HL **class change** at predicted M* (Higgins: M* ≈ 4) |
| **commit** | **missing** in-loop apply | close θ / actuator loop | τ_apply / τ_window; log-only vs online θ | log-only replay → **SQL class**; stale θ → overhead factor worsens before slope breaks |
| **threshold** | **extra** unpriced resource law | declare N_pass vs N_photon vs bandwidth | two abscissae on same data | parallel shift of scaling line, not slope change |
| **misread** | **extra** bound as achievement | three-way report: bound / estimate / commit | Fisher vs Holevo vs committed θ error | gap persists under loop-closure tests |

### 6.2 Worked predictions — Higgins et al. 2007

Reference: entanglement-free Heisenberg-limited phase estimation (*Nature* **450**, 393; arXiv:0709.2996). Autopsy: diagnostic-ledger §14; chat worked example.

```text
Confirmed (degenerate corner):
  M = 1 Kitaev policy → SQL scaling class on same apparatus
  → decode-depth cell must close (M ≥ M*) for HL class

Route projection (N = 378):
  p = 32 visibility dip → outlier scatter
  → predict residual tracks V(32); close route by V(p)-weighted policy

Open (commit witness):
  same click stream, θ log-only → predict SQL class collapse
  stale / delayed θ apply → predict overhead factor blow-up before slope change

Threshold:
  N = passes through sample, not photon count
  → mis-threshold as photons → parallel shift of HL line
```

### 6.3 QEC ↔ metrology crosswalk

```text
syndrome stream          ↔  click / trajectory record
decoder / noise model    ↔  estimator / Bayesian policy
apply / mid-circuit      ↔  θ / actuator commit
τ_dec / τ_cyc            ↔  τ_apply / τ_coherence
distance / rounds        ↔  M, pass depth, resource law N
leakage syndrome         ↔  herald / pass-index expansion
offline decode sold as memory  ↔  Fisher bound sold as closed-loop precision
```

Mid-circuit QEC is one register instance of this mirror.

---

## 7. Formal QEC boundary

Holographic / QES settings: same record/constitution grammar, different register (diagnostic-ledger D3/D7). Forbidden independent **constitution-on-surface** term unless write-site actually moves.

---

## 8. Demotion

```text
across varied decoders, commit conventions, timing, and thresholds,
logical success predicted by syndrome quality alone;
constitution locatable as a convention-free state functional;
postselected / tomographic / offline record equivalent to register constitution for all uses.
```

---

## 9. Compact result

```text
Layers:  record → route → decode/uptake → commit → threshold  (+ misread guard)

Autopsy:   headline → layer break → repair path
Predictive: open cell → closure OR projection → forward signature (class, cliff, correlation)

Sharpest corners:
  good syndromes, dead memory;
  leakage/correlation absent from record;
  same syndromes, different decoder or noise model;
  offline OK, online commit fails;
  fidelity needs postselection;
  tomography sold as memory;
  threshold unnamed.

Metrology mirror (§6):  same engine on parameter register; Higgins 2007 = HL success + M=1 SQL degenerate corner.

Payoff:  same headline → different missing/extra diagnosis → different repair path
         AND preregistered direction before the next run.
Template:  success headlines deserve the same layer split as failure headlines.
```
