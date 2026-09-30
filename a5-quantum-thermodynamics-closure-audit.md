# A5 — Quantum Thermodynamics Closure Audit

*Working draft, June 2026.*

Status: application document / quantum-thermodynamics closure audit.
Primary target: A3 record-vs-constitution, A4 engine layer split, A0 §5 compose/missing/extra, PB-3/PB-4, B6/D5 temperature leg.
Ledger: D13; extends D5 (temperature leg); record-vs-constitution parallel to D4 — thermo is the operational mirror for cycle/work/engine composites, not a new dynamics program.
Grade: route diagnostic + record-vs-constitution discriminator + engine-eligible where reset/memory/clock protocols are live.

A Maxwell demon reads a gas, an engine extracts work from a single bath, and an erasure step later pays the bill. Quantum thermodynamics prices that scene with entropy, mutual information, correlations, and resource states, and does so well. The audit is narrower: when a run reports *information*, *work*, or a *closed cycle*, which part of the composite is on the table — the state-functional record, or the register, uptake/write, threshold, and reset-paid closure that complete it?

The field already pays for batteries, baths, clocks, demons, feedback, memory, and erasure once a protocol goes operational. Those are the missing roles that finish the claimed composite, not optional add-ons.

```text
Bundled headline:  "information / work / cycle achieved."
A5 question:        which role-part of the composite is actually supplied?
```

---

## 1. Missing diagnosis

```text
entropy reduction / mutual information / correlation
≠
constituted information
```

```text
Missing (when sold as constitution):
  register
  uptake / write
  read / use path
  application threshold

Missing for repeated-cycle closure:
  erasure / reset accounting
```

Bad closure:

```text
correlation → information
```

MGR closure:

```text
correlation / entropy / MI  →  record-structure (state-functional)
+ register
+ uptake / write
+ threshold
+ possible readout / use
= constituted thermodynamic information
```

Record and constitution stay split as in A3. State functionals price record-structure; constitution requires the write-chain.

Temperature leg: already owned by B6 and D5 — temperature is response/rendering scale, not constituted information by itself.

---

## 2. Role splits at the seam

```text
temperature        ≠  information          (D5, B6)
free energy        ≠  constituted work
correlation / MI   ≠  register
measurement        ≠  constituted record
feedback           ≠  closed engine
protocol time      ≠  physical clock / control resource
state transition   ≠  autonomous operation
entropy accounting ≠  reset-paid cycle
```

These are export audits, not prohibitions. Standard thermodynamics and quantum information already distinguish many of them under operational pressure. MGR names the compose recipe each headline requires.

---

## 3. Compose recipes

```text
work      = energy-transfer + battery
operation = protocol + clock / control resource
information = record-structure + register + uptake/write + threshold
cycle     = feedback + reset (Landauer / erasure invoice paid)
engine    = all of the above + bath / accounting closure
```

Compose / missing / extra applies to each headline:

```text
compose:  all listed parts present and routed
missing:  a required leg absent (e.g. work claimed with no battery)
extra:    a part present but unaccounted (e.g. entropy drop sold as cycle closure without reset)
```

Battery and clock/control name work-storage and control roles, not necessarily separate devices.
Removing one implementation does not remove a role supplied elsewhere; co-occurrence does not
establish a shared substrate.

---

## 4. Sharpest missing-role claims

```text
No battery, no constituted work.

No clock / control resource, no autonomous operation.

No reset, no closed information-thermodynamic cycle.

No register / write-chain, no constituted information.
```

Each is a could-fail condition, not a slogan. **False** locates malformed bundling or a holding route. **True** forces new bets (which battery, which reset path, which pinned threshold). **Relabel** if the audit only recovers textbook resource vocabulary with no downstream export that could have failed — §8 carries the count/duration contact, the ratio question, and the separate cross-register cliff bet. A failed class transfer need not erase a surviving operational relationship.

---

## 5. Layer split (engine mirror)

A4 names record → route → decode → commit → threshold for QEC. A5 is the thermodynamic register instance:

```text
record:
  correlations, entropy, MI, fluctuation statistics in the state / ensemble

route / model:
  bath choice, coarse-graining, resource theory, fluctuation-theorem bookkeeping

decode / control:
  feedback policy, demon read, protocol update, adaptive control

commit / reset:
  memory erasure paid; cycle closure; battery handoff; Landauer invoice

threshold:
  work extraction budget, cycle time, error / fidelity floor, yield

misread:
  entropy accounting, MI plateau, or correlation alone sold as constituted information or closed cycle
```

**Crosswalk (grammar, not coefficient):**

```text
A4 syndrome stream     ↔  thermo correlation / fluctuation record
A4 route / model       ↔  bath choice / coarse-graining / resource theory
A4 decode              ↔  demon read / feedback policy
A4 commit              ↔  reset / erasure-paid memory / battery update
A4 threshold           ↔  work budget / cycle closure scale
A4 good syndromes, dead memory  ↔  good correlations, no reset-paid cycle
```

Reset is the thermo version of commit-cycle closure.

---

## 6. Engine-eligible tests

Hold one layer fixed; move another (same discipline as A4 §4):

```text
same correlation / entropy record  →  swap register declaration or write-chain
same protocol                      →  vary clock / control resource present vs absent
same feedback policy               →  reset paid vs reset omitted
same state diagnostics             →  vary uptake threshold or erasure path
```

Readouts:

```text
work claim moves only when battery leg is supplied or removed
cycle claim moves only when reset / erasure is paid or omitted
information claim moves only when register + write + threshold are pinned
```

Success with a required role genuinely absent, at the same pinned task and threshold, refutes its
necessity. Success after removing only an implementation requires locating the role still supplied.

---

## 7. Common bundled reads

| Pattern | Bundled | Layer break |
|---------|---------|-------------|
| **MI / entropy as information** | QI thermo headline | record OK; **missing register + write + threshold** |
| **Free energy extracted** | work achieved | **missing battery** or unpriced energy account |
| **Protocol completes** | operation autonomous | **missing clock / control resource** |
| **Cycle closed in state** | reversible engine | **missing reset / erasure** — entropy accounting ≠ cycle closure |
| **Feedback improves efficiency** | engine works | feedback ≠ closed engine without reset + bath accounting |
| **Measurement stores info** | demon succeeds | measurement ≠ constituted record without write-chain |

---

## 8. Instances — the register's measured structure

The thermodynamic register contains measured count/duration and bound/realized distinctions.
Their relationship to the ordering-resource bet remains testable; one cross-register arm is open.

**8.1 Finite-time Landauer: count and duration remain distinct.** Complete erasure of an initially
unbiased, symmetric bit at bath temperature T has the ideal bound

```text
W_min = k_B T ln 2
```

In the optimized high-success Bérut protocol, the success-conditioned heat approaches this scale
approximately as `⟨Q⟩_success ≈ k_B T ln 2 + B/τ`; the coefficient and regime are protocol-specific.
Imperfect erasure changes the unconditional bound, and a selected-success mean is not the
full-ensemble mean (Bérut et al., *Nature* **483**, 187 (2012); analysis: arXiv:1503.06537).

The count/duration distinction survives. Bit count alone does not establish ordering-resource:
independent bits can be erased in parallel while the ideal total bound remains `n k_B T ln 2`.
The PB-2 reading must therefore test the relation between erased amount, sequential depth, and
available parallel resources rather than identify their counts. `k_B T ln 2` is energy per erased
bit, not a velocity or time rate. Could-fail: the ordering interpretation fails if parallel amount
substitutes for its proposed resource under matched task and error criteria; the count/duration
contact remains. Pin the logical encoding, success criterion, and erasure map before comparing.

**8.2 The record→constitution conversion rung, tabulated.** The experiments supply measured
(bound, realized) pairs; the solvable tape model supplies a theoretical comparison:

```text
Toyabe et al.  (Nat. Phys. 6, 988 (2010))   feedback work vs kT·I bound; realized ~28%;
                                            measured degradation as feedback delay grows
Koski et al.   (PRL 115, 260602 (2015))     autonomous on-chip demon; the demon's own register
                                            dissipation metered — clock/control and reset legs
                                            made physical
Bérut et al.   (Nature 483, 187 (2012))     the reset leg alone, priced toward its floor
Mandal–Jarzynski (PNAS 109, 11641 (2012))   solvable model, not an experiment: engine/eraser/dud
                                            regime set by the incoming tape's blank capacity
```

All retrodictive contacts — standard accounting (Sagawa–Ueda, resource theories) already prices each.
The additional question is whether these ratios share a constrained relation — converted weight,
unconverted remainder, sum-rule shape — with conversion weights at other interfaces. Similar
roles do not by themselves establish one law or one substrate.

**8.3 The open arm — the cross-register cliff.** Does QEC dependency latency have the same failure
class as feedback-engine latency relative to usable correlation time? Fix the task, error/yield
threshold, delay normalization, and criterion for matching the onset or asymptotic form before
comparing curves. Decoder backlog, a missed decision deadline, and correlation decay are distinct
candidate mechanisms, not one cliff by description. Toyabe's delay curve and QEC timing data are
contact handles; the matched comparison is open. Different classes rebuff the universal class
transfer; a narrower relation between latency and required uptake remains separately testable.

---

## 9. Demotion

```text
constituted work, information, or cycle achievable from the specified input-state diagnostics alone
without the corresponding work-storage, write, control, or reset role at the pinned target;
entropy / MI / correlation sufficient for target completion across varied uptake conditions;
reset omitted while the same closed-cycle task is achieved;
cliff classes differ under the §8.3 matching rule → common-class bet fails, not every layer relation.
```

---

## 10. Compact result

```text
Lane:     D13 — quantum thermodynamics operational closure audit
Extends:  A3 (record ≠ constitution), A4 (engine layers), D5 (temperature ≠ information)

Missing diagnosis:
  entropy / MI / correlation ≠ constituted information without register + write + threshold
  (reset closes the cycle, not every information headline)

Sharpest gates:
  no battery → no constituted work
  no clock/control → no autonomous operation
  no reset → no closed cycle
  no register/write-chain → no constituted information

Payoff:
  same thermo headline → different missing/extra diagnosis → different repair path
  and preregistered direction before the next protocol run.
```

Contact map and at-a-glance status: `diagnostic-ledger.md` D13, `CLAIMS.md`.
