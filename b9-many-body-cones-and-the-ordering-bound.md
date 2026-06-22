# B9 — Many-Body Causal Cones and the Per-Ordering Bound

*Working draft, June 2026.*

Status: B-note / Lieb-Robinson many-body contact / candidate positive witness — retrodictive contact, not engine; witness-status pending a run could-fail (a4 §6).  
Primary target: PB-1 ordering-axis bound, PB-2 per-ordering interior, and the PB-2.1 / PB-2.2 signatures forced at the horizon corner (b4 §6a).  
Grade: clarifier and role-diagnostic. Not a derivation of the Lieb-Robinson bound or any velocity coefficient.

B9's claim is simple:

```text
a finite influence cone exists with the spacetime metric absent.
```

On a lattice of local interactions, correlations cannot outrun an emergent cone whose speed is set by interaction range and strength — not by `c`. This is the cleanest available reading of PB-1: a bound on the ordering/influence axis that is not the flow/adjacency bound `c`. It is also the wall where PB-2's interior is testable rather than merely opened — per-ordering, flow-free, and bound-vs-realized all surface here, where the horizon corner (b4 §6) could only declare the fork.

The photon seam opened PB-2's interior; the horizon corner showed it absent at an adjacency wall. This is the wall where it is present.

---

## 1. Minimal toolkit and import boundary

```text
Layer 1 — owned (A0 lineage):
  PB-1: the ordering/influence axis carries a bound (A0 §12)
  PB-2: its interior is influence per ordering-resource (A0 §12)
  ordering = causal-precedence chain; adjacency = side-by-side on a slice
    (space = ordering + adjacency, A0 §6)
  flow-stripping: ordering survives with flow removed (photon seam, A0 §2, a1)
  the PB-2.1 / PB-2.2 demand forced by the horizon corner (b4 §6a)

Layer 2 — projected (many-body / quantum-circuit formalism, GR absent):
  local Hamiltonian / bounded-range interaction graph
  commutator growth ‖[A(t), B]‖ as influence-reach
  emergent cone: reach ≲ v_LR · t + range
  circuit depth = sequential interaction layers; width = parallel sites

Layer 3 — imported (the coefficients, not the role):
  the exact Lieb-Robinson velocity v_LR for a given Hamiltonian
  proof constants; tail shape outside the cone
  specific lattice, dimension, interaction decay
```

Layer 1 is the same ordering/influence carve A0 extracted at the photon seam. Layer 2 maps it onto the many-body formalism, where no metric is present. Layer 3 is the quantitative content — the velocity, the constants — which B9 does not derive.

---

## 2. The cone with the metric absent

GR is not held fixed here because GR is not present. The lattice has no metric, no light cone, no `c`. Influence still cannot spread arbitrarily fast:

```text
‖[A_x(t), B_y]‖ ≤ C · exp( −(d(x,y) − v_LR · t) / ξ )
```

Outside the cone `d(x,y) > v_LR · t`, influence is exponentially suppressed. The cone is real and the velocity `v_LR` is finite.

Role read:

```text
this is a bound on the ordering/influence axis (PB-1) with the flow/adjacency
bound c absent. PB-1 bet that such an axis carries a bound "as the flow/adjacency
axis carries c"; here the bound appears with c removed from the problem, so it
cannot be c in disguise.
```

The non-relativistic lattice is what makes the witness clean: the bound is exhibited on the ordering/influence axis alone, with the metric axis not in play.

Read discipline (magnitude disownership):

```text
the commutator norm ‖[A(t), B]‖ is the many-body formalism's own measure of
operator spread. B9 borrows it as a witness of influence-reach; it does not
claim the norm is a tier on MGR's influence ladder (A0 §3). The role-claim is
the cone's existence and its depth-dependence — not the magnitude.
```

Reconciliation contact (open):

```text
the independence above rests on the non-relativistic regime, where v_LR is set
by couplings and c is absent. In a Lorentz-invariant continuum limit the cone
is expected to track c. Whether lattice v_LR and continuum c are two faces of
one bound or two distinct bounds is the live PB-1 could-fail — named here, not
resolved.
```

---

## 3. Depth, not width — PB-2.1

The cone advances with sequential interaction layers, not with parallel system size.

```text
add width (more sites in parallel):
  the cone does not advance faster; v_LR is fixed by local range/strength,
  not by how many sites sit side-by-side.

add depth (more sequential layers):
  the cone advances; reach grows with the number of layers.
```

Role read:

```text
the ordering-resource is depth — sequential causal steps — and it is not
substitutable by adjacency-width. PB-2.1 realized positively: a per-ordering
bound that parallelism cannot buy back.
```

This is the corner b4 §6a could not supply. At the horizon the only extensive was adjacency; here the binding resource is depth, and width is explicitly impotent.

Adversarial counterpart: a4 §6 — the Heisenberg yield may be reachable by depth **or** parallel probe count (substitutability could-fail on the **precision-yield** register). That does not contradict depth-governed **influence spread** here; see CLAIMS D12 triangulation.

Could-fail (PB-2.1):

```text
a protocol that advances the cone by width alone (parallel resources)
→ the resource was adjacency, and PB-2's ratio reads per-adjacency.
```

This wall is favorable by construction — depth wins here. That does not falsify the adversarial corner: PB-2.1 lands only if the a4 §6 metrology trial, where width could in principle substitute, also refuses substitution. Favorable here plus adversarial there, or it does not hold.

---

## 4. Count, not duration — PB-2.2

The structural content of the cone is combinatorial: reach is graph-distance on the interaction lattice, advanced per layer. Strip the wall-clock and the cone is still a count — sites crossed per sequential layer.

```text
v_LR carries units (distance / time);
but the bound that does the work is depth-counting: layer k reaches
graph-distance ≲ k (up to range), independent of how long each layer takes.
```

Role read:

```text
the ordering-resource is a count on the causal order, not a duration. PB-2.2:
flow-free. The same flow-stripping that opened the photon seam (A0 §2, a1)
is what lets the cone be stated as a layer-count.
```

Could-fail (PB-2.2):

```text
the only available bound carries irreducible duration / metric dependence with
no depth-count form → the resource was flow, not ordering.
```

---

## 5. Bound vs realized — the split the horizon could not reach

PB-2 requires that the bound and the realized value separate (A0 §12). The horizon corner (b4 §6) could not test this; the many-body cone can.

```text
bound (ceiling):
  the Lieb-Robinson velocity v_LR — the fastest the cone may advance.

realized (actual):
  the true correlation front in a given state, which can be slower —
  localized, many-body-localized, or sub-ballistic dynamics fall inside the
  cone and never saturate it.
```

The gap between the ceiling and the actual front is the bound-vs-realized decomposition: present, and in principle measurable. This is the one PB-2 clause the horizon left untouched.

Could-fail (PB-2):

```text
if ceiling and realized front cannot separate — every dynamics saturates the
cone with no slack — the decomposition fails and PB-2's interior collapses to
a single number.
```

---

## 6. What B9 adds

```text
1. a GR-free witness: the ordering/influence axis carries a bound (PB-1) with
   the spacetime metric absent — so the bound is not c in disguise.

2. PB-2.1 positive: the binding resource is depth; adjacency-width cannot
   substitute for it.

3. PB-2.2 positive: the bound is a layer-count on the causal order, not a
   duration.

4. the bound-vs-realized split the horizon corner (b4 §6) could not reach:
   the Lieb-Robinson ceiling vs the actual correlation front.
```

It does not derive:

```text
the Lieb-Robinson bound;
any velocity coefficient v_LR;
the proof constants or tail shape;
the dynamics of any specific Hamiltonian.
```

---

## 7. Ledger

MGR role claims:

```text
ordering/influence-axis bound exhibited with the metric absent (PB-1);
per-ordering, non-substitutable-by-width interior (PB-2.1);
flow-free layer-count form (PB-2.2);
bound-vs-realized separation (PB-2).
```

Externally supplied / calibrated:

```text
the Lieb-Robinson velocity and proof constants;
the specific interaction graph, dimension, and decay;
the actual correlation front of a given dynamics.
```

Demotion / failure conditions:

```text
the cone advances by parallel width alone → per-adjacency (PB-2.1 fails);
the only bound carries irreducible duration with no depth-count → flow not
  ordering (PB-2.2 fails);
ceiling and realized front cannot separate → PB-2 decomposition fails;
every many-body influence bound reduces to the ambient metric c once relativity
  is restored → the ordering-axis bound was not independent (PB-1).
```

Standing result:

```text
B9 is a clarifier / candidate positive witness — retrodictive contact, not
engine. It is the favorable wall for PB-2: per-ordering, flow-free, and
bound-vs-realized are all testable here, where the horizon corner (b4 §6)
could only open the fork. Witness-status is earned only when the adversarial
corner is run (a4 §6) and the PB-1 reconciliation contact (§2, lattice v_LR
vs continuum c) is settled. Favorable-by-construction does not falsify the
adversarial corner.
```
