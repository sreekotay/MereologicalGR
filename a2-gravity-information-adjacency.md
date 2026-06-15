# A2 — Gravity, Information, and Adjacency

*Sree Kotay — working draft, June 2026.*

Status: application document / gravity-side role decomposition.  
Foundation: A0 grammar and A1 photon-run commitments are assumed.  
Forward-reference rule: this document states its own debts internally; later notes may refine them, but A2 does not rely on later documents for its claims.

Core result:

```text
gravity = ordering + influence + energy-momentum
information = ordering + influence + flow

massive-sector reading:
  energy-momentum = flow-face + adjacency-face

therefore:
  gravity and information share ordering + influence;
  their difference, in the massive torsion-free sector, is the adjacency / energy-momentum sector.
```

Short form:

```text
gravity = information + adjacency
```

Scope:

```text
massive sector;
torsion-free / symmetric-stress-energy / GR-owned sector;
role-decomposition only;
no new field equation;
no coupling derivation;
no claim that torsion/spin remainder is closed.
```

---

## 1. Imported SR/GR substrate

Checkable physics, not framework claims:

```text
proper time:
  dτ² = -g_μν dx^μ dx^ν / c²  (signature -+++)

four-velocity:
  u^μ = dx^μ/dτ;
  u·u = -c²

four-momentum:
  p^μ = m u^μ

energy:
  p⁰ = E/c;
  E = γmc²;
  rest E = mc²

momentum:
  p^i = γm v^i

mass shell:
  E² = (pc)² + (mc²)²

photon:
  m = 0;
  E = |p|c

stress-energy:
  T_μν sources curvature in standard GR;
  T⁰⁰ energy density;
  T⁰i momentum density;
  T^ij stress
```

The framework may label this substrate. It does not derive the substrate here.

---

## 2. Framework definitions used

```text
cause = ordering + influence

information = ordering + influence + flow

gravity = ordering + influence + energy-momentum
```

Information is not influence-structure in transit. It is ordered influence taken up in flow at application scale.

Gravity is not declared a substance. It is the GR-owned structural mode by which energy-momentum constrains causal structure.

Shared core:

```text
ordering + influence
```

Difference:

```text
information adds flow;
gravity adds energy-momentum.
```

---

## 3. Imported labels / projection layer

Energy-momentum is imported as a dimensionful primitive. It has two projection faces:

```text
energy:
  flow-conjugate face

momentum:
  adjacency-conjugate face

mass:
  invariant rest / flow-projection face
```

For massive systems:

```text
energy-momentum = time-momentum + space-momentum
                = flow-face + adjacency-face
```

At the null limit:

```text
flow → 0
energy is adjacency-borne
E = |p|c
```

So the null case is not a counterexample. It is the opposite extreme from rest-massive content:

```text
rest-massive:
  flow-face maximal, net momentum zero

null:
  flow-face zero, adjacency-borne momentum/energy
```

---

## 4. GB-1 — gravity and information differ by adjacency

Claim:

```text
In the massive-sector role-decomposition,
gravity and information differ by the adjacency / energy-momentum sector.
```

Grade:

```text
definition + consistency-check;
not a bet;
no confirmatory weight.
```

Reason:

```text
P1. ordering is the same role in both compositions;
P2. influence is the same role in both compositions;
P3. energy-momentum decomposes into flow-face + adjacency-face in the massive sector;
therefore gravity's extra term over information is the adjacency / energy-momentum sector.
```

Scope guard:

```text
not unconditional;
not null-sector;
not torsion-complete;
not a derivation of G_N or the Einstein equation.
```

Torsion / spin debt:

```text
The standard GR connection is torsion-free.
Metric-compatibility may be role-licensed by adjacency / separation discipline.
Torsion-free is not currently framework-forced.
Therefore any claim here that relies on standard GR curvature is torsion-free-sector only.
```

Open cell:

```text
translational closure failure / torsion
```

must either be:

```text
forced empty by role-reason
```

or:

```text
booked as a structural bet, e.g. spin / rotational current → torsion-sector equation.
```

Do not treat GR's torsion-free choice as a prohibition.

---

## 5. GB-2 — stranding at an edge and ordering-collapse

Claim:

```text
information-stranding-at-an-edge ⟺ ordering-collapse
```

Grade:

```text
bet;
loss-edge partially pressure-tested;
unaccountability-edge open.
```

Projection path:

```text
ordering is shared by gravity and information;
cone structure has oriented continuation conditions;
edge-types create stranding pathologies;
therefore ordering-collapse and information-stranding should coincide at invariant edges.
```

Loss-edge reading:

```text
black-hole / singularity side:
  geodesic termination;
  invariant continuation failure;
  stranding threat.
```

Unaccountability-edge reading:

```text
past-boundary / low-entropy boundary side:
  antecedent not internally accounted for;
  status contested as an information problem.
```

Failure condition:

```text
a stranding-pathology occurs with no ordering-collapse;
or an ordering-collapse occurs with neither loss nor unaccountability pathology.
```

Observer-relative horizons do not automatically count:

```text
Rindler horizon / de Sitter access horizon:
  horizon-rich;
  not necessarily invariant ordering-collapse;
  no stranding implied without invariant edge.
```

---

## 6. GB-3 — no null structure constitutes information

Claim:

```text
No null structure constitutes information by itself.
```

Projection path:

```text
information = ordering + influence + flow

null structure:
  ordering + influence + adjacency;
  flow → 0

therefore:
  null structure carries influence-structure / transit structure,
  not constituted information.
```

Failure condition:

```text
a horizon null generator, gravitational-wave null ray, or photon-in-flight
constitutes a consequential result with no flow-bearing uptake anywhere in the loop.
```

Clarification:

```text
A null signal can perturb a flow-bearing receiver.
Constitution occurs at the receiver / uptake chain, not in the null transit itself.
```

---

## 7. Weyl two-face structure at the ordering-collapse corner

The Weyl tensor has two projected faces relative to a timelike `u`:

```text
electric Weyl:
  tidal / time-space face;
  projected along timelike u

magnetic Weyl:
  areal / space-space face;
  transverse / rotational structure
```

Role reading:

```text
electric face:
  ordering-collapse / directed collapse alignment candidate

magnetic / areal face:
  adjacency / transverse wall structure candidate
```

Regime split:

```text
monotonic approach:
  collapse direction supplies a single timelike u;
  ordering-collapse and electric-Weyl alignment can be forced in the generic case.

generic oscillatory approach:
  collapse direction rotates / Kasner axes permute;
  alignment is dynamic, not fixed.

termination:
  cone continuation and the u needed for Weyl projection terminate together.
```

Scope guard:

```text
Weyl decomposition is curvature-sector only.
It sharpens the rotational closure-failure face near ordering-collapse.
It does not exhaust affine non-integrability or settle torsion.
```

---

## 8. Scope and perimeter

A2 does not derive:

```text
p^μ = m u^μ;
T_μν;
Einstein field equation;
G_N;
metric signature/count;
full torsion-free condition;
non-abelian influence;
entropy measures;
QG completion.
```

A2 may use calibrated or imported scalars if the role route is explicit:

```text
Calibration is not failure.
Fitting is failure.

A scalar may be observed.
A structure must be earned.
```

Therefore:

```text
role-decomposition:
  framework-owned if cleanly composed

mass-shell / metric norm:
  consequence of licensed SR/GR imports

couplings / coefficients:
  imported or calibrated

unearned new structure:
  disallowed
```

---

## 9. Open items

```text
1. Does the singularity destroy ordering or transform it into influence?

2. Is there an ordering/influence conversion scale analogous in role-form to c?
   Not in evidence.

3. Can torsion-free be forced by role-reason?
   If not, spin / torsion remains a structural-bet candidate.

4. Does the Weyl-electric generic signature provide a useful falsifier for GB-2?
   Scoped to generic, not conformally flat, collapse.

5. Can the entropy reading of de-oriented adjacency-spread be stated only under mixedness,
   without confusing de-oriented with disordered?
```

---

## 10. EB-1 — photon at rest / box at rest

Forced chain:

```text
1. A single photon is massless and has no rest frame.
2. Asking for a photon at rest fails at the part.
3. The question becomes answerable only at an aggregate: a photon box.
4. In the box rest frame, individual spatial momenta cancel in the net.
5. Net p = 0, total E nonzero.
6. By the imported mass-shell, the box has rest mass.
```

Role reading:

```text
single photon:
  no flow-face / no rest frame

photon aggregate:
  net adjacency orientation cancels;
  total energy lands on the flow/rest face;
  rest frame exists at aggregate level
```

Grade:

```text
round-trip to GR;
illustration / consistency;
no confirmatory weight.
```

---

## 11. EB-2 — de-oriented interior and entropy

Given the photon box:

```text
photon parts:
  nonzero individual momenta;
  zero rest mass

resting box:
  total spatial momentum zero

therefore:
  individual momenta survive but cancel in the net

remainder:
  nonzero, net-directionless adjacency-spread
```

The forced core is:

```text
de-oriented adjacency-spread
```

The entropy identification is scoped:

```text
entropy measures mixedness / multiplicity of that spread when the state is mixed.
```

A pure photon pair may have de-oriented spread while `S_vN = 0`. Therefore:

```text
de-oriented ≠ disordered
```

and:

```text
remainder forced;
entropic measure mixedness-mediated and imported.
```

---

## 12. Compact result

```text
Shared core:
  ordering + influence

Information:
  ordering + influence + flow

Gravity:
  ordering + influence + energy-momentum

Massive-sector decomposition:
  energy-momentum = flow-face + adjacency-face

Therefore:
  gravity differs from information by the adjacency / energy-momentum sector
  in the massive torsion-free GR-owned sector.

Null limit:
  flow → 0;
  energy adjacency-borne;
  transit not constitution.

Torsion debt:
  translational closure-failure cell remains open unless forced empty.

Calibration rule:
  scalars may be observed or externally supplied;
  fitted structure is not derivation.
```