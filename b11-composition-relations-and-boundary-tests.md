# B11 — Composition Relations and Boundary Tests

Status: B-note / derivation and boundary refinement of B1–B10.  
Foundation: A0 role-real composition test, A1 photon unfusion, and the A-series operational distinctions.  
Grade: conditional derivations, explicit counterexamples, and scoped literature contacts.

The photon supplies ordered causal effect without proper-time flow of its own. The surrounding
operation must still supply whatever completes its claimed result. Holding those jobs apart
exposes relationships: a phase need not distinguish histories, a correlation need not complete
a write, and a completed record does not by itself determine the cost of resetting it.

The tests below retain GR as ground. Field, quantum and statistical machinery enters where
specified. Necessary relationships do not identify their roles or decide their substrate.

---

## 1. B1 — covariant composition fixes the ordering residue

For bosonic scalar fields at spacelike-separated points x,y, two inertial frames can reverse
the coordinate-time order. Their time-ordering prescriptions select products differing by

```text
φ(x)φ(y) − φ(y)φ(x) = [φ(x),φ(y)].
```

Treating the composed quantity as the same physical quantity in both frames requires this
frame-ordering residue to vanish in its relevant matrix elements. For the usual field-theoretic
spectrum and reconstruction conditions, covariance of time-ordered functions implies operator
local commutativity (Greenberg, hep-th/0405211). A vanishing expectation in one state is weaker;
covariance of unordered Wightman functions alone is also insufficient.

```text
no invariant spacelike precedence
+ covariance of composed products
+ declared field-theoretic spectrum / reconstruction conditions
→ spacelike local commutativity.
```

The consequence follows from compatibility of composition, not from antisymmetry alone.
For S=½⟨{φ(x),φ(y)}⟩ and A=½⟨[φ(x),φ(y)]⟩, with overall propagator conventions suppressed,

```text
W = S + A
G_T = S + sgn(x⁰−y⁰)A.
```

Once local commutativity is established, A vanishes at spacelike separation and G_T=W=S there.
Spacelike correlation remains allowed. Symmetry alone neither requires a nonzero correlation
everywhere nor fixes its decay scale.

For a compactly smeared source J(f), U_f=exp(−iλJ(f)), and a receiver observable B,

```text
δ_f⟨B⟩ = iλ⟨[J(f),B]⟩ + O(λ²).
```

If the source commutes with the receiver algebra, this intervention cannot change its statistics.
A physical measurement model must also specify the local coupling and causal factorization of
its instruments; arbitrary nonlocal measurement prescriptions do not inherit that conclusion
from the field commutator alone (Fewster–Verch, arXiv:1810.06512).

**Boundary.** The causal test is source-dependent receiver statistics outside the source's causal
future, not an isolated early click or a peak advanced relative to a reference pulse. Neither a
universal 1/ω advance cap nor cone support from antisymmetry alone follows. A source-controlled
violation under the declared conditions rebuffs this composition claim; pulse reshaping tests a
different attribution.

The on-shell distribution in

```text
1/(q²+i0) = PV(1/q²) − iπδ(q²)
```

is likewise not an uptake operation. An internal line can meet q²=0; real-carrier status still
requires the external-state conditions. The analytic two-piece split does not itself count
physical registers.

---

## 2. B6/B7 — content, transport and thermal compatibility

For a small nonspinning body with p^μ=m u^μ and u·u=−c², differentiation gives

```text
F^μ = Dp^μ/dτ = ṁu^μ + ma^μ
u·a = 0
−u·F = c²ṁ
h^μ_ν F^ν = ma^μ,       h^μ_ν = δ^μ_ν + u^μu_ν/c².
```

The parallel projection changes rest energy; the perpendicular projection changes the bulk
flow direction. This is the same four-momentum balance, not independent dynamics. For a
composite detector, the internal energy also enters inertia through M̂=m₀+Ĥ_int/c². Expanding
at fixed momentum to first order in internal energy,

```text
H_body = E₀(P) + [m₀c²/E₀(P)]H_int + O(H_int²)
E₀(P) = √(m₀²c⁴+c²P²).
```

In the semiclassical trajectory limit the coefficient is dτ/dt. The same internal-energy term
participates in inertia and proper-time evolution without being identical to flow (Wood–Zych,
arXiv:2205.02394).

B7's uniformly accelerated trajectory yields

```text
(Δct)²−(Δx)² = (4c⁴/a²)sinh²[aΔτ/(2c)].
```

The corresponding massless scalar interval skeleton has imaginary period 2πc/a. A local
singularity and its analytic period do not alone select a global Wightman state: a smooth state
dependent term, boundary conditions and the KMS analytic strip remain part of the composition.
Retarded support additionally specifies a past-source initial-value problem; ordering alone does
not choose that problem over a future-boundary one.

### 2.1 Positivity precedes thermality

For a stationary, suitably smeared Hermitian observable X, choose

```text
W_X(ω) = ∫dt exp(iωt)⟨X(t)X(0)⟩
N_X(ω) = [W_X(ω)+W_X(−ω)]/2
D_X(ω) = [W_X(ω)−W_X(−ω)]/2.
```

State positivity gives a positive spectral measure. Where spectral densities exist,
N_X±D_X=W_X(±ω)≥0, hence

```text
N_X(ω) ≥ |D_X(ω)|.
```

If the same state and generator also satisfy thermal detailed balance,
W_X(−ω)=exp(−βℏω)W_X(ω), then

```text
N_X(ω)/D_X(ω) = coth(βℏω/2),       D_X(ω) ≠ 0.
```

Symmetric fluctuations and antisymmetric response remain distinct. Positivity constrains their
possible combinations; thermality adds a stronger relationship. A thermal ratio for one channel
does not establish that relationship for every observable carried by the body. Stargen–Sudhir's
finite-mass detector model exhibits thermal internal response without corresponding motional
thermality under its weak-coupling, prescribed-longitudinal-acceleration and nonrelativistic
transverse-motion assumptions (arXiv:2509.01983).

**Boundary.** Failure of KMS for another channel narrows the thermal assignment, not the geometric
period or the positivity condition. Proper temperature can be a scalar once the relevant state,
flow and equilibrium compatibility are fixed; it need not be a property of every probe response.

### 2.2 State admissibility remains a specific open implication

Two literature contacts identify what would have to be derived:

```text
stationary globally hyperbolic spacetime + the stated linear field conditions
+ passive ground/KMS mixtures
→ microlocal spectrum condition (Sahlmann–Verch, math-ph/0002021).

ultrastatic slab with compact Cauchy surface + the specified Klein-Gordon state class
+ finite fluctuations of all time-derivative Wick squares
→ Hadamard condition (Fewster–Verch, arXiv:1307.5242).
```

A single finite detector response does not supply these hypotheses. The open step is whether
the declared operation requires the stated passivity or all-observable finiteness condition.
A driven transition response is not automatically a passive equilibrium reference.

---

## 3. B8 — a control derived by matching mean energy

For prescribed semiclassical paths, a common time-independent H_int and Δτ=τ₂−τ₁,

```text
χ(Δτ) = Tr[ρ_int exp(−iH_int Δτ/ℏ)]
visibility V = |χ|; internal phase = arg χ.
```

Using the imported unitary dynamics, expansion near Δτ=0 gives, for finite energy moments,

```text
arg χ = −⟨H_int⟩Δτ/ℏ + O(Δτ³)
1−V = Var(H_int)Δτ²/(2ℏ²) + O(Δτ⁴).
```

The leading phase depends on the mean; the leading contrast loss depends on the variance.
One scalar phase cannot determine both. This derives a matched control rather than merely
naming phase and clock as different roles (Zych et al., arXiv:1105.4531).

With three energies E₀−Δ, E₀, E₀+Δ and E₀>Δ>0, prepare

```text
OFF = |E₀⟩
ON  = (|E₀−Δ⟩+|E₀+Δ⟩)/√2.
```

Their mean energies agree exactly, while

```text
χ_OFF = exp(−iE₀Δτ/ℏ)
χ_ON  = exp(−iE₀Δτ/ℏ) cos(ΔΔτ/ℏ).
```

Before the cosine changes sign the internal phases agree and the contrasts differ. State-dependent
recoil, trapping and mass-energy backreaction must be controlled when implementing the common-path
approximation. The two-level formula is V=|cos(πΔτ/(2t⊥))|, with t⊥=πℏ/ΔE.

**Boundary.** Not reading a clock does not turn it OFF. For a pure OFF control the conditional
internal states must coincide up to phase. A mixed state diagonal in H can remain identical on
both paths yet have |χ|<1 through energy-phase averaging; contrast alone then does not establish
an accessible internal which-path record. A clock-attributed residual after pure OFF, phase,
preparation and other decoherence controls would challenge the claimed single-channel account.
An arbitrary contrast loss with the clock OFF would not.

---

## 4. B9 — connecting depth and dynamical duration

Let H=Σ_e h_e be a nearest-neighbor Hamiltonian on a finite interaction graph. Then

```text
A(t) = Σ_(n≥0) (it/ℏ)^n/n! · ad_H^n(A),       ad_H(A)=[H,A].
```

Each commutator can extend the initial support by at most one graph edge. If A and B are r
edges apart,

```text
[ad_H^n(A),B] = 0       for n<r.
```

This determines the first possibly connecting order. The remaining sum also requires its weights:
interaction norms, path multiplicities and (t/ℏ)^n/n!. Bounding that tail requires the hypotheses
of the specified Lieb-Robinson theorem (Nachtergaele–Sims, arXiv:1004.2086).

```text
connecting count:  which orders can reach the receiver
physical rate:     how the generator weights those orders over duration
```

Rescale H→αH, α>0. The graph and minimum connecting depth remain fixed, but

```text
A_(αH)(t)=A_H(αt).
```

The physical timescale changes. Count and duration are non-substitutable contributions to this
calculation without being dynamically disconnected. A finite-depth circuit has an exact support
restriction; continuous evolution sums arbitrarily high orders and generally has small nonzero
tails. A circuit approximation must retain layer duration and its error.

**Boundary.** Spacetime metric absent does not mean graph metric absent. Width alone is impotent
only when local connectivity, strength, range and supplied resources are fixed. Changing width
can change those resources. A loose proof bound is not a unique physical ceiling; slack below it
can be proof slack rather than a new physical parameter.

Eisert–Gross (arXiv:0808.3581) provide an unbounded local-model counterexample to unrestricted
finite-speed claims. Yin–Lucas (arXiv:2106.09726) establish bounds for a specified finite-density
bosonic class. These do not establish that all bosonic bounds must be state-dependent or that all
generic interacting fronts lie strictly inside a relativistic ceiling. A universal cross-register
resource law remains separately testable under matched tasks.

---

## 5. B10 — the reset price requires the accessible relationship

A marker-only unitary preserves conditional overlap:

```text
⟨m₀|U†U|m₁⟩=⟨m₀|m₁⟩.
```

It cannot restore unconditional path interference by itself. Joint path–marker unmarking and
conjugate-basis measurement with coincidence selection are different operations. More generally,
for a local trace-preserving marker map Λ_M,

```text
Tr_M[(id_P⊗Λ_M)(ρ_PM)] = Tr_M ρ_PM.
```

Conditional fringes use an instrument outcome and its communicated selection record; they do
not alter this unconditioned marginal.

For memory M initially independent of a Gibbs bath B, with fixed bath Hamiltonian and joint
unitary evolution, use dimensionless entropies and β=1/(k_B T). If Q_B is bath energy gained,

```text
ΔS_erase = S(ρ_M)−S(ρ′_M)
ΔS_B = ΔS_erase + I(M:B)_(ρ′)
D(ρ′_B||τ_B) = βQ_B−ΔS_B

βQ_B = ΔS_erase + I(M:B)_(ρ′) + D(ρ′_B||τ_B) ≥ ΔS_erase.
```

This is the equality-form Landauer balance (Reeb–Wolf, arXiv:1306.4352). The usual ln2 limit
requires an initially unbiased bit and complete erasure under the stated independence and bath
conditions; finite-time and finite-bath requirements can add cost.

Constitution status alone does not fix that price. A source S can retain a bit whose completed
copy is in R:

```text
ρ_SR = ½|00⟩⟨00| + ½|11⟩⟨11|

controlled reset using S:
|00⟩→|00⟩,   |11⟩→|10⟩.
```

R is blank, S retains the original bit, and joint entropy is unchanged. With degenerate logical
states and an ideal reversible implementation, resetting R alone has no universal positive
k_B T ln2 heat floor. Applying the uncorrelated-memory bound to R while omitting its usable
correlation with S is the missing accounting. Other copies, control resources and restoration
must be included for a full-cycle claim. Quantum side information gives a conditional-entropy
extension (del Rio et al., arXiv:1009.1630).

**Rebuff.** The universal claim constituted record → fixed positive reset cost fails. The
relationship among the target reset, accessible correlations, bath and restoration survives.
An actual irreversible path logger can also complete a record before the screen; neither
visibility loss nor the word marker identifies where a write occurred.

---

## 6. B4 — stationary equality does not identify charge, area and flux

Use c=ℏ=k_B=1. For a stationary bifurcate Killing horizon with generator ξ and surface gravity κ,

```text
S_Wald = (2π/κ)∫_B Q_ξ
Einstein gravity: ∫_B Q_ξ = κA/(8πG)
therefore S_Wald=A/(4G).
```

The normalized Noether charge and geometric area are necessarily related here. This is not
identity of roles, and the bare charge integral is not generally the Hamiltonian mass without
the required boundary terms (Wald, gr-qc/9307038).

A dynamical contact keeps GR fixed. For first-order perturbations of a stationary horizon, on
constant-affine-v cuts with v=0 at its background bifurcation surface, use the Hollands–Wald–Zhang
entropy definition (arXiv:2402.00818):

```text
S_dyn(v)=[A(v)−vA′(v)]/(4G),       to first perturbative order.
```

The affine parameter v is not proper time on the null generator. Linearizing Raychaudhuri about
θ=σ=0, with background area element dA₀, gives

```text
δA″(v)=−8πG∫δT_kk(v)dA₀
δS_dyn′(v)=−vδA″(v)/(4G)=2πv∫δT_kk(v)dA₀.
```

A teleological pre-flux area perturbation δA=Cv therefore has δS_dyn=0. The latter changes with
the actual matter flux, not the earlier area growth. Source-free first-order perturbations have
no entropy change; gravitational-wave energy enters at second order. One metric and one GR
dynamics suffice for this distinction. The entropy definition and approximation remain supplied;
identifying its role with PB-2's ordering resource is still an exposed further claim.

**Boundary.** Evaporation already gives dA/dt<0 when M decreases and A∝M². Page turnover concerns
fine-grained radiation entropy, not the onset of shrinking area. The island competition is
between generalized-entropy branches, not automatically an ordering quantity and bare area.
The GB-1 energy/flow cancellation cannot justify that identification.

A further scope condition applies to the singularity argument: a closed trapped surface, null
convergence and the standard Penrose global hypotheses entail null geodesic incompleteness.
A caustic alone is not incompleteness; an event horizon alone is not the trapped-surface theorem.

---

## 7. B5 — distinct closure faces with a required identity

For coframe e^a and metric-compatible spin connection ω^a_b, Cartan's definitions give

```text
T^a=de^a+ω^a_b∧e^b
R^a_b=dω^a_b+ω^a_c∧ω^c_b
DT^a=R^a_b∧e^b.
```

The last relation follows by applying D twice to e. In the torsion-free sector it reduces to
R^a_b∧e^b=0, the first Bianchi relation in this notation. Curvature and torsion are different
closure faces while their derivatives are constrained together.

Metric compatibility alone does not remove torsion. In a coordinate coframe e^a=dx^a with
Minkowski metric, choose only

```text
ω¹₂=−dx¹,   ω²₁=dx¹.
```

This connection is metric-compatible and has R=0, but T¹=−dx¹∧dx²≠0. It is a counterexample
to metric-compatible ⇒ torsion-free, not a counterexample to GR's specified Levi-Civita connection.
Both loop effects occur at area order; their different output is the relevant distinction.

**Boundary.** A retained spin current does not alone select a gravitational action. The usual
spin→torsion equation follows within the declared Einstein–Cartan/Poincaré-gauge variational
closure. Naming spin, torsion or their relationship does not require another physical substrate
(Blagojević–Hehl, arXiv:1210.3775).

---

## 8. B2/B3 — completeness depends on the actual inference or write map

### 8.1 Shared flow does not remove calibration

In the shared-FRW setting, H=(1/a)da/dτ. Reparametrize the reading by σ=λτ, λ>0:

```text
(1/a)da/dσ = H/λ.
```

The physical history is unchanged; the normalization of the inferred rate must still be
accounted for. B2's two burden groups concern distance/ruler construction and the expansion
history under a specified comparison map. They are not two scalar degrees of freedom. Clock,
redshift and detector calibrations remain measurement dependencies even when the cosmic flow
is shared. Standard-siren agreement changes the inference-path comparison; multiple correlated
biases can remain, so it does not uniquely identify a cause by itself.

### 8.2 An input-state diagnostic does not select an unspecified operation

Let S and F hold a correlated bit and prepare target R blank:

```text
ρ_SF=½|00⟩⟨00|+½|11⟩⟨11|,      R=|0⟩.
```

At the same input state, target and success criterion, compare copying F into R with doing
nothing. The first gives P(R=S)=1, the second P(R=S)=1/2. The input record diagnostic is unchanged;
the target operation is not. This is an insufficiency result for the specified input, not a ban
on describing a completed output register by its state.

Likewise the QES minimization gives an entropy/reconstruction assignment, not an implementation
of an arbitrary target write. The full generalized entropy, including its area term, computes
the radiation entropy in the applicable models. It cannot be divided into all actual information
in S_bulk versus a universally noninformational area merely by naming the terms.

**Boundary.** A QES need not itself be null. Uptake on non-null degrees near a cut would test a
cut-only attribution, not automatically GB-3. The no-null-constitution bet fails only on its
stated null/flowless operation condition. Absence of an uptake term in an entropy calculation
does not independently establish that universal prohibition. GB-2 remains the two directional
bets stated in A2, not a restored equivalence.

---

## 9. Contact outcomes

| Contact | Surviving result | Rebuff or open continuation |
|---|---|---|
| B1 | Covariant composition constrains spacelike order-sensitive response | Antisymmetry and an isolated early click are insufficient; physical instruments require their coupling conditions |
| B2 | Shared-flow inference has explicit calibration and history dependencies | Two burden labels do not count physical freedoms or uniquely diagnose a bias |
| B3 | Input record, reconstruction assignment and performed target write are distinct | No universal state-description ban; QES not automatically null |
| B4 | Stationary charge/area relationship; first-order area/flux-sensitive separation in GR | Page is not onset of area shrinkage; ordering-resource identification remains open |
| B5 | Different closure faces obey Cartan/Bianchi compatibility | Metric compatibility does not force torsion-free; spin source route remains action-conditional |
| B6/B7 | Geometric period, spectral positivity and thermal compatibility have distinct premises | No state or whole-body thermality from a local period or single response alone |
| B8 | Mean phase and variance-dependent contrast yield a matched-mean pure-state control | Mixed-state contrast and unrelated OFF decoherence do not certify clock distinguishability |
| B9 | Minimum connecting order and its dynamical weighting are separately necessary | No duration-free velocity, universal saturation rule or unqualified width claim |
| B10 | Complete reset accounting includes accessible correlations and restoration | Universal positive cost based on constitution status alone is rejected |

A failed independence claim can expose a required relationship. A failed relationship has its
own definite scope. Neither outcome identifies the roles with one another or decides whether
they are faces of one substrate.

## References

- Greenberg, hep-th/0405211 — covariance of time-ordered products and local commutativity.
- Fewster–Verch, arXiv:1810.06512 — local system–probe measurement theory.
- Wood–Zych, arXiv:2205.02394 — internal mass-energy and detector motion.
- Stargen–Sudhir, arXiv:2509.01983 — internal/motional thermality in a finite-mass Unruh model.
- Sahlmann–Verch, math-ph/0002021; Fewster–Verch, arXiv:1307.5242 — scoped state-admissibility results.
- Zych et al., arXiv:1105.4531 — proper-time-dependent internal-state overlap.
- Nachtergaele–Sims, arXiv:1004.2086; Eisert–Gross, arXiv:0808.3581; Yin–Lucas, arXiv:2106.09726 — local propagation bounds and their assumptions.
- Reeb–Wolf, arXiv:1306.4352; del Rio et al., arXiv:1009.1630 — erasure balances and side information.
- Wald, gr-qc/9307038; Hollands–Wald–Zhang, arXiv:2402.00818 — stationary and perturbative dynamical horizon entropy.
- Blagojević–Hehl, arXiv:1210.3775 — metric-compatible connections and action-dependent spin/torsion equations.
