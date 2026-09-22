# A4 — QEC Failure Layer Autopsy

*Working draft, June 2026.*

Status: application document / quantum-error-correction failure diagnostic.
Primary target: A3 record-vs-constitution, A0 §3 influence ladder, A0 §5 compose/missing/extra, PB-3/PB-4.
Ledger: same record/constitution split as D4 (QD diagnostics); lab QEC is the operational mirror, not yet a separate ledger row. Published experiment map: diagnostic-ledger §14.
Grade: post-mortem template / engine-eligible diagnostic / predictive closure map. Not a verdict on QEC success or failure.

A surface-code run extracts syndromes each cycle, a decoder recommends a Pauli correction or frame update, and the declared logical operation uses it in time — or misses its dependency deadline. "QEC failed" bundles five separable legs of that cycle: record, route, decode, commit, threshold. Practice already operationalizes them; milestone language compresses them. A4 names the compression and routes failure to a layer.

```text
Bundled headline:  "QEC failed."
A4 question:       which layer broke?
Predictive add:    which cell is open → closure or projection → forward signature
```

Failed or partial runs are often more instructive than break-even wins: failure strips a role and opens the bundle, the A0 degenerate-corner method in lab form. Success autopsies use the same checklist.

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
| **Real-time / mid-circuit** | bad qubits | record OK; **commit delayed** beyond the dependent operation's deadline, or backlog unbounded |
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

`τ_deadline` is the time available before the declared operation needs the decoded information,
not automatically one syndrome cycle. Frame tracking can defer physical correction. Diagnostic
latency, syndrome cadence, and decoder throughput must be recorded separately; finite latency
and an unstable backlog are different failures (Chamberland–Iyer–Poulin, arXiv:1704.06662).

---

## 4. Engine-eligible tests

Hold one layer fixed; move another — vary the operation on the record, not only the state diagnostic (A3 record ≠ constitution; A0 §5 compose/missing/extra):

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
If logical LER tracks commit/threshold moves with record fixed → record was not the bottleneck.
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
| **commit** open / delayed | **missing** timely dependency | close frame/apply/handoff path; schedule buffers or abort rules | τ_dec / τ_deadline; decoder throughput / syndrome arrival rate | deadline failure or backlog growth under the specified convention; no universal cliff at τ_dec / τ_cyc = 1 |
| **threshold** compressed | **extra** unnamed scale | close accounting: rounds, depth, yield, extrapolation | yield, discard rate, declared ε | headline moves under threshold swap with commit fixed |
| **misread** | **extra** inference as constitution | require offline / online decode / online commit separately | tomography at prep vs memory through rounds | gap persists between offline bound and register constitution |

### 5.2 Degenerate corners (class predictions)

Strip one cell before the run; predict scaling **class**, not a fitted ε. This is the degenerate-corner method as a preregistered test:

```text
strip commit (offline decode only)     →  logical LER tracks decode, not memory claim
strip decode (syndrome-only headline)  →  no correction path; record-quality ceiling
strip leakage from record              →  distance plots misread; route blamed wrongly
strip threshold naming                 →  milestone debate only; no layer verdict possible
```

**Uniform success is a weak diagnostic:** if every decoder and latency achieves logical break-even, the layer split was never stressed.

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
record:     clicks / trajectories / homodyne trace / heralded outcomes; interrogation sequence specified
route:      noise model, prior, visibility, back-action, pass index
decode:     estimator / Bayesian update / adaptive policy
commit:     control actually applied before the dependent segment (θ, detuning, kick), where the protocol requires feedback
threshold:  resource law (passes vs photons vs bandwidth), ε, SQL/HL class
misread:    Fisher / CR bound on ρ sold as closed-loop precision
```

### 6.1 Metrology predictive table

| Layer stress | Missing / extra | Closure | Projection | Predicted signature |
|---|---|---|---|---|
| **record** | **missing** pass tag / herald | expand record (coincidence, pass index) | detected vs intended pass count | scatter width drops; HL slope unchanged if decode+commit OK |
| **record / acquisition** | insufficient interrogation sequence | vary repetition M at each pass depth with resource accounting fixed | M, pass schedule, estimator | Higgins protocol: M = 1, 2 has SQL variance scaling; reported HL class for M ≥ 4; not a decoder-only intervention |
| **route** | **extra** unmodeled noise | pass-indexed noise in update | visibility V(p), drift vs pass count | residual at max N tracks 1/V(p); not HL slope |
| **decode** | **missing** estimator / policy | change inference at fixed complete record | estimator identity, sufficient statistic | estimate may change; no universal SQL → HL threshold follows from decoder depth alone |
| **commit** | **missing** required in-loop apply | compare functioning, delayed, and disabled feedback during acquisition | τ_apply / τ_deadline; record distribution; actuator outcome | protocol-specific loss at a dependency deadline; unchanged record + estimator gives unchanged estimate, not automatic SQL collapse |
| **threshold** | **extra** unpriced resource law | declare N_pass vs N_photon vs bandwidth | two abscissae on same data | rescaling depends on resource relation; not generally a parallel shift |
| **misread** | **extra** bound as achievement | three-way report: bound / estimate / commit | Fisher vs Holevo vs committed θ error | gap persists under loop-closure tests |

### 6.2 Worked predictions — Higgins et al. 2007

Reference: entanglement-free Heisenberg-limited phase estimation (*Nature* **450**, 393; arXiv:0709.2996). Autopsy: A4 §6.2 (this section).

```text
Retrodiction (degenerate corner; role-route fixed before the read):
  M = 1 Kitaev sequence → SQL standard-deviation scaling on the same apparatus
  → the quantum Fourier measurement is optimal; broad tails come from the interrogation sequence
  → increasing M changes acquisition as well as adaptive processing; M is not decoder depth
  → HL class reported for M ≥ 4 in this protocol, not a universal policy threshold

Route projection (N = 378):
  p = 32 visibility dip → outlier scatter
  → predict residual tracks V(32); close route by V(p)-weighted policy

Open (commit witness):
  disable / delay θ during acquisition at fixed pass schedule and declared output task
  → compare changed record distributions and control performance; scaling must be computed
  same complete record + same estimator → same estimate, even without subsequent actuation

Threshold:
  N_pass = M(2^(K+1) − 1), N_photon = M(K+1)
  → varying K makes the two abscissae nonlinearly related; not a parallel shift
```

Feedback is protocol-dependent: nonadaptive multipass HL estimation exists (Higgins et al.,
arXiv:0809.3308). That rebuffs mandatory adaptive commit for precision yield; it does not identify
inference with actuation or remove the specified acquisition/readout path.

**PB-2 / D12 contact.** `N_pass` counts phase interactions; `M` counts repetitions at each pass depth,
not decoder depth. Photon count is not automatically parallel width. The ordering-resource reading
must distinguish these counts and their scheduling. The sharp could-fail remains substitutability:
sequential multipass and parallel entangled-probe protocols can reach the same Heisenberg scaling
under matched resource assumptions. This is the **adversarial** PB-2.1 wall (precision yield).
Failure may restrict the claimed resource relationship without identifying the roles. The
**favorable** wall is many-body cone spread (b9 §3; b4 §6a export) — a different register;
triangulation in CLAIMS D12 / diagnostic-ledger D12.

### 6.3 QEC ↔ metrology crosswalk

```text
syndrome stream          ↔  click / trajectory record
decoder / noise model    ↔  estimator / Bayesian policy
apply / mid-circuit      ↔  θ / actuator commit
τ_dec / τ_deadline       ↔  τ_apply / τ_deadline
distance / rounds        ↔  pass depth, repetition M, resource law N
leakage syndrome         ↔  herald / pass-index expansion
offline decode sold as memory  ↔  Fisher bound sold as closed-loop precision
```

**Named transfer (grammar, not coefficient):** QEC — good syndromes with dead memory (record OK, target commit failed) ↔ metrology — good path phase with clock-OFF (render OK, flow-register inactive). Both test whether one supplied role licenses the target operation; neither shared failure class nor shared substrate follows from the crosswalk.

Mid-circuit QEC is one register instance of this mirror.

---

## 7. Formal QEC boundary

Holographic / QES settings: same record/constitution grammar, different register (diagnostic-ledger D3). Forbidden independent **constitution-on-surface** term unless write-site actually moves.

---

## 8. Demotion

```text
across varied decoders, commit conventions, timing, and thresholds,
logical success predicted by syndrome quality alone;
constitution locatable from the input state alone across unspecified write maps (A3);
postselected / tomographic / offline record equivalent to register constitution for all uses.
```

---

## 9. Compact result

```text
Layers:  record → route → decode → commit → threshold  (+ misread guard)

Autopsy:   headline → layer break → repair path
Predictive: open cell → closure OR projection → forward signature (class, cliff, correlation)

Sharpest corners:
  good syndromes, dead memory;
  leakage/correlation absent from record;
  same syndromes, different decoder or noise model;
  offline OK, required online handoff misses its deadline;
  fidelity needs postselection;
  tomography sold as memory;
  threshold unnamed.

Metrology mirror (§6):  same engine on parameter register; Higgins 2007 = HL success + M=1 SQL interrogation corner.

Payoff:  same headline → different missing/extra diagnosis → different repair path
         AND preregistered direction before the next run.
Template:  success headlines deserve the same layer split as failure headlines.
```
