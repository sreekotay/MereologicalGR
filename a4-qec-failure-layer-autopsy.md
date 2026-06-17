# A4 — QEC Failure Layer Autopsy

*Working draft, June 2026.*

Status: application document / quantum-error-correction failure diagnostic.  
Primary target: A3 record-vs-constitution, A0 compose/missing/extra, PB-3/PB-4, diagnostic-ledger D4 (lab instance of the same seam).  
Grade: post-mortem template / engine-eligible diagnostic. Not a decoder theory or a proof of QEC success or failure.

```text
Bundled headline:  "QEC failed."
A4 question:       which layer broke?
Not asked:         did MGR predict this failure?
```

Failed or partial runs are often more instructive than break-even wins: failure strips a role and opens the bundle (A0 degenerate corners).

---

## 1. Layer split

```text
record:
  syndrome / flag / leakage / erasure stream made available for correction
  classical syndrome bits are record, not constituted logical information (PB-3)

route / model:
  noise assumptions, graph, priors, correlation / leakage model, decoder schema

decode / uptake:
  record → recovery, Pauli-frame update, abort, or feed-forward

constitution / commit:
  logical register maintained or handed off under the declared convention
  (physical apply optional; deferred Pauli frame counts if convention says so)

threshold:
  application consequence scale: memory time, gate fidelity, depth, yield, budget

misread:
  tomography, postselection, offline decode, or syndrome alone counted as constitution
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
| **Decoder swap** | QEC broken | **same record, different uptake** — engine-eligible (§4) |
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
```

---

## 4. Engine-eligible tests

Hold one layer fixed; move another (A3: vary operation, not only state diagnostic):

```text
same syndrome stream     → swap decoder / priors / graph
same decoder               → vary apply latency, frame timing, mid-circuit abort rules
same physical run          → report offline decode, online decode, online commit separately
same rounds                → vary declared threshold (one gate vs memory vs depth vs yield)
same code/noise            → leakage/erasure syndromes on vs off
```

```text
If logical LER tracks uptake/threshold moves with record fixed → record was not the bottleneck.
If LER tracks only syndrome quality → record was the bottleneck.
```

---

## 5. Formal QEC boundary

Holographic / QES settings: same record/constitution grammar, different register (diagnostic-ledger D3/D7). Forbidden independent **constitution-on-surface** term unless write-site actually moves. Lab decoder engineering stays on D4.

---

## 6. A4 demotion conditions

```text
logical outcome fully determined by syndrome quality with no uptake/threshold variation;
convention-free state functional locates constitution without decode/commit/context;
postselected / tomographic / offline record equivalent to full register constitution for all uses.
```

Ordinary QEC practice carries the layers operationally; milestone language compresses them.

---

## 7. Compact result

```text
Layers:  record → route → decode/uptake → commit → threshold  (+ misread guard)

Sharpest corners:
  good syndromes, dead memory;
  leakage/correlation absent from record;
  offline OK, online commit fails;
  fidelity needs postselection;
  tomography sold as memory;
  threshold unnamed.

Payoff:  same headline → different missing/extra diagnosis → different repair path.
```
