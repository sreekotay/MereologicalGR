# B8 — Zych Clock Interferometry and Flow-Register

Status: working external-form / engine-contact note.  
Grade: engine-eligible contact; probe for render vs flow-register separability; magnitude GR/QM-owned, MGR-disowned.

Zych et al. (*Nat Commun* 2, 505, 2011; arXiv:1105.4531) supply the physics. Contact: A0 §9 flow-rate sub-cell — compose / missing / extra, clock-ON vs clock-OFF factorial.

B8 role-locates what the standard calculation bundles. It does not re-derive the GR or QM formulas.

---

## 1. Starting Role Carve

The contact starts from grammar fixed before reading Zych:

```text
time        = ordering + flow
clock       = magnitude projection of flow (tick rate, τ-register)
rendering   = content through frame / worldline (phase, E = −p·u)
information = ordering + influence + flow at application threshold

A0 §9 sub-cell (fixed before contact):
  superposition of flow-rates
  (massive basis; internal proper-time accrual can differ per branch)
```

**Not in scope for this run:** constitution, PB-4 observer write-chain, influence-floor beyond carrier tier.

**Lineage:** the route is fixed before the Zych contact is used: photon corner first (flow stripped, ordering + influence remain), then the A0 §9 flow-rate sub-cell. Chronology is not evidence; the clean role-route is the criterion.

---

## 2. Standard setup (imported)

**Apparatus:** Mach–Zehnder; massive particle with internal Hamiltonian H (two-level model in Zych).

**Geometry:** arms at height difference Δh in stationary gravitational field; laboratory time in superposition ∆T; potential difference ∆V = g∆h.

**Imported outputs:**

| Symbol | Standard meaning | Zych eq. |
|---|---|---|
| φ, ∆Φ | Interferometer phase (includes Newtonian m∆V and GR corrections) | (12) |
| V | Fringe visibility (contrast) | (5), (13), **(16)** |
| D | Path distinguishability from clock readout | D = 1 − V²/2 (pure states) |
| ∆τ | Proper-time difference between arms | ∆τ ≈ ∆V ∆T / c² (small height diff.) |
| t⊥ | Orthogonalization time of internal state under H | t⊥ = πℏ/∆E (two-level) |

**Zych visibility (general form):**

```text
V = cos( π ∆τ / (2 t⊥) )     … eq. (16)  [two-level; generalizations in paper]
```

**Path–internal state (schematic):**

```text
|Ψ⟩_MZ ∝ |path_1⟩|τ_1⟩ + |path_2⟩|τ_2⟩
V = |⟨τ_1|τ_2⟩|
```

**Complementarity:** V² + D² = 1 (pure states).

MGR imports all of the above. It does not re-derive (7)–(16).

---

## 3. What Zych bundles (headline compression)

Standard presentation often collapses:

```text
"GR in QM interferometry"  →  one headline: gravitational phase + decoherence
```

Zych’s explicit split (their Discussion):

```text
Phase shift ∆Φ:
  occurs even when the particle is NOT operationally a clock
  explainable as AB-type: flat spacetime + effective potential (their claim: incomplete for proper time)

Visibility drop V:
  requires operational clock (internal evolution, accessible which-path from H)
  NOT explained by phase alone — prices proper time / time dilation operationally
```

That is already a **layer split** in the source paper. MGR names the legs:

```text
∆Φ channel  →  rendering / trajectory / potential comparison
V channel   →  flow-register (proper-time accrual + internal H evolution)
```

---

## 4. Role registers

```text
path superposition + arm geometry     →  ordering + adjacency (imported lab scaffold)
∆Φ (mass, ∆V, ∆T, ⟨H⟩ corrections)  →  rendering / phase map
∆τ per arm                            →  flow (proper-time accrual differs)
H_int evolution |τ_i⟩                 →  flow-register (clock projection active)
|τ_1⟩, |τ_2⟩ overlap                  →  recorded / which-path readiness (pre-uptake)
V                                     →  diagnostic: accessible path info from register
D                                     →  same information, which-path metric
```

**Forced / adjacency (lab, not witness):** particle often **supported** in gravitational potential (not free fall). Proper acceleration / support structure is **adjacency + forced-face** lab scaffolding — distinct from the ∆τ witness channel. Do not bundle as one undifferentiated “gravity effect.”

**Guardrail:**

```text
V drop  ≠  constitution
V drop  ≠  information write
V drop  ≠  influence tier earned beyond pre-uptake record
```

Which-path readiness is **recorded** tier at most; no PB-3/PB-4 uptake chain is completed in the interferometer alone.

---

## 5. Compose / missing / extra

### 5.1 Collapse: V into ∆Φ only (AB-only story)

**Substitution:** treat visibility as fixed; read only phase.

**Missing:** the V(∆τ, t⊥) structure; complementarity with internal readout.

**Extra:** none from MGR — this is the **under-read** Zych warns against.

**Verdict:** fails compose; remainder = visibility channel.

### 5.2 Collapse: V drop → “information in flight”

**Substitution:** gravitationally induced decoherence = constituted information.

**Missing:** uptake, threshold, flow-bearing write chain (A3, PB-3).

**Extra:** information grade without operation.

**Verdict:** fails missing/extra; demote to **record / which-path readiness**.

### 5.3 Collapse: proper time → generic “time” label

**Substitution:** ∆τ identified with laboratory t alone.

**Missing:** GR proper-time definition; ṫ = √(−g_μν ẋ^μ ẋ^ν) structure.

**Extra:** none if GR imported — but **flow-register** leg is lost.

**Verdict:** clarifier failure if claimed as full audit.

### 5.4 Clean compose (MGR read)

```text
rendering leg:   ∆Φ(∆V, ∆T, m, ⟨H⟩_GR)  — can run with clock OFF
flow-register:   V(∆τ, t⊥)               — requires clock ON
```

Both present in standard calculation; **factor** under clock-OFF control.

---

## 6. Engine factorial — clock-ON vs clock-OFF

**Convention C (declare before contact):**

```text
Clock-OFF:
  (a) |τ_in⟩ eigenstate of H  →  t⊥ → ∞  (Zych Discussion, eq. 16)
  (b) H_int = 0 during arm transit  (operational: no distinguishable internal advance)
  (c) which-path information not physically accessible (Zych: no V drop)

Clock-ON:
  superposition of internal energy states (e.g. (|0⟩+|1⟩)/√2)
  t⊥ finite; ∆τ from time dilation between arms
```

**Held fixed (render knob):** Δh, g, ∆T, m, arm geometry → same ∆V, same ∆Φ **to leading order** (Zych: phase occurs with or without clock).

**Moved (flow-register knob):** t⊥, internal evolution, ∆τ/t⊥ ratio.

### 6.1 Predictions (role level)

```text
Clock-OFF:  V → 1 (maximal contrast); D → 0
            ∆Φ unchanged vs ON at matched geometry
            → visibility channel was flow-register, not render alone

Clock-ON:   V = cos(π ∆τ / (2 t⊥))  [two-level]
            V modulates with ∆τ/t⊥ at fixed ∆Φ scaffold
            → proper-time register is the which-path channel
```

Zych’s own **clock-OFF** paragraph (Discussion):

> if one prepares the initial state |τ_in⟩ as an eigenstate of the internal energy Hamiltonian H, only the phase of such a state would change … interferometric visibility would be maximal. This ‘clock’ would not ‘tick’ (t⊥ = ∞) so the concept of proper time would have no operational meaning **in this case**.

MGR: that is the **OFF** limit of the same engine — not a different experiment.

### 6.2 One concrete protocol pair

| Run | Internal prep | Arms | Readout |
|---|---|---|---|
| **A (ON)** | (|0⟩+|1⟩)/√2 | Δh, ∆T fixed | V < 1 scaling with ∆τ/t⊥; ∆Φ |
| **B (OFF)** | |0⟩ or |1⟩ eigenstate (or H_int off in arms) | **same** Δh, ∆T | V ≈ 1; **same** ∆Φ |

**Primary discriminator:** ΔV = V_ON − V_OFF at matched φ, not φ alone.

---

## 7. Could-fail conditions

### 7.1 MGR structure fails

```text
V still drops with Clock-OFF after ∆Φ matched
  → render and flow-register not separable in this regime
  → A0 §9 sub-cell demoted or narrowed

V with Clock-ON tracks only total phase, not ∆τ/t⊥
  → Zych proper-time witness collapses to AB story (their own could-fail)
```

### 7.2 Standard physics fails (Zych-owned)

```text
No ∆τ at fixed Δh / ∆T  →  GR proper-time difference absent (separate check)
V² + D² ≠ 1 with mixed internal states  →  complementarity bookkeeping (see §8)
```

### 7.3 MGR overread fails

```text
Claim V drop = information constitution  →  A3/PB-3 collision
Bundle support force with ∆τ witness     →  adjacency/forced conflation
```

---

## 8. Experimental data map

**Zych visibility witness (V vs ∆τ/t⊥): not measured.** Zych Table 1: outcome **“Not tested.”** No published report of fringe **contrast** dropping because internal clock states entangle with path at gravitational ∆τ.

**Clock-OFF factorial: no data.** No paired ON/OFF runs at matched φ.

```text
Render leg (φ, redshift):     data exist
Flow-register leg (V, ∆τ/t⊥):  no detection data
Clock-OFF control:             no data
```

| Publication | Measured | Zych V? | MGR leg | Notes |
|---|---|---|---|---|
| Colella, Overhauser, Werner (1975) — COW | Gravitational **phase** | No | **render** | Zych ref. 7; bounds σ_τ only if ΔV assumed |
| Atom fountains / light-pulse AI (g, gradients) | **Phase** / acceleration | No | **render** | Contrast often logged for **technical** decoherence — not proper-time witness |
| Chou et al., *Nature* 2010 — 33 cm clocks | **Redshift** (static compare) | No | **render** | Ledger §14.3; no AI visibility |
| Overstreet et al., *Science* 2022 — grav. AB (Kasevich group) | Gravitational **phase** (proper-time / potential; 25 cm AI) | **No** | **render** | φ from ∆τ difference; **not** internal-clock V — Zych’s AB vs proper-time distinction |
| Zych et al., *Nat Commun* 2011 | **Theory** + feasibility (Table 2) | **Target** | **flow-register** | Required Δh·ΔT for full V loss ≫ achieved (2011) |
| Zych et al. 2012 — photonic timing | Theory | Partial | **render/timing** | Not massive internal register |
| Trapped-atom + Ramsey proposals (e.g. *Quantum* 2025) | **Proposal** | Target | both | Visibility modulations predicted; not reported |

**Bounds ≠ detection:** Zych reuses phase experiments to constrain proper-time width σ_τ (Table 1). Consistent with V = V_QM is **not** a measurement of the visibility drop.

**Feasibility (Zych Table 2, atoms / hyperfine):** full visibility loss needs Δh·ΔT ~ 10 ms (g ~ 10 m/s²); achieved ~ 10⁻⁵ ms (2011). Partial effect still needs ΔV ~ 10⁻⁶ visibility precision + decoherence control.

**On the horizon (not data):** Florence Sr/Cd AI + optical-clock program; trapped-atom minute-scale superposition + Ramsey extensions.

---

## 9. Caveats (engine honesty)

1. **Mixed states:** general V² + D² ≤ 1; clock-OFF must be **pure** internal control.

2. **Supported particle:** laboratory g, not necessarily geodesic motion — price forced/adjacency separately from flow-register.

3. **Implementation of OFF:** eigenstate prep vs decoupled H_int vs detuned trap — **Convention C** must be named in any lab claim.

4. **Extra phase from ⟨H⟩:** clock-ON can move **both** V and ∆Φ (eq. 12); factorial must separate **visibility** from **phase** readouts.

5. **Engine grade without witness:** preregistered factorial; lab contact open until ON/OFF at matched φ is run.

---

## 10. Photonic contrast (Zych et al. 2012)

**Clock = arrival time** at detector (Shapiro / time-of-flight).

```text
massive internal clock  →  flow-register on probe (timelike worldline)
photonic timing clock   →  rendering / record at null-line detection
```

Same complementarity logic; **different leg**. Useful negative control: photon path does not carry proper-time flow on its own worldline (A1 photon corner).

---

## 11. Cross-links

```text
A0 §9      superposition of flow-rates sub-cell
A1         clock as flow projection; photon has no internal clock
A2         E = −p·u rendering; gravity vs information adjacency split
A3         record ≠ constitution; V channel is pre-uptake
A4 §6      engine mirror: good φ + clock-OFF ↔ good syndromes + dead memory
diagnostic-ledger §14.3.1
CLAIMS     engine row (Zych + clock-OFF)
```

**Versus MPC–Wolf (clock vs atom redshift):** Zych holds **geometry**, toggles **internal register**; visibility **V** is the primary readout, not phase interpretation alone.

---

## 12. Grade

```text
Field taxonomy:
  convergent with GR + QM complementarity
  Zych supplies eq. (5)–(16)

Engine contact:
  render (φ) vs flow-register (V) factorial
  clock-OFF preregistered; lab witness pending

Role audit:
  compose clean when V and ∆Φ factored
  missing/extra fails if V → information or V → φ alone

Magnitude:
  GR/QM-owned; MGR-disowned

Collision-room:
  V drop without OFF control at matched φ would stress separability claim
  constituted-information reading of decoherence would break A3/PB-3
```

**Grade boundary:** this is forward engine contact, not retrodictive guardrail recovery.

---

## 13. Compact result

Zych separates **phase** (rendering) from **visibility** (flow-register). MGR reads that as the A0 §9 sub-cell with an explicit switch:

```text
Clock-ON:   ∆τ/t⊥ prices V  — proper time as operational which-path register
Clock-OFF:  V → 1, φ held    — register frozen; render leg alone

Engine move: hold trajectory / φ, vary internal flow-register activity.
Separability is the test, not coincidence with known GR phase shifts.
```

---

## References / external anchors

- Zych, M., Costa, F., Pikovski, I. & Brukner, Č. Quantum interferometric visibility as a witness of general relativistic proper time. *Nat. Commun.* **2**, 505 (2011).
- Zych, M., Costa, F., Pikovski, I. & Brukner, Č. General relativistic effects in quantum interference of photons. *Class. Quantum Grav.* **29**, 224010 (2012) — photonic timing variant.
- Englert, B.-G. Fringe visibility and which-way information. *Phys. Rev. Lett.* **77**, 2154 (1996) — V–D duality.
- Colella, Overhauser, Werner (1975) — gravitational phase; bounds cited in Zych Table 1.
- Overstreet et al., *Science* **375**, 226 (2022) — gravitational AB **phase**; not Zych visibility.
