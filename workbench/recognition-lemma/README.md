# The Recognition Lemma

*Workbench — non-canonical. Referee computation for the c9/C5 two-metric seam: the algebraic
half of C5's two-order uniqueness conjecture, proved at a point. Conventions match
`workbench/two-metric-seam/` — signature −+++, u unit timelike (g(u,u) = −1), seam form
g̃ = A(g + B u⊗u), c9 normalization A = 1 − B/3 (the Bianchi finite-branch dressing). One
script, `recognition_lemma.py`; every check must print PASS (currently 26/26). Not promoted;
promotion requires A0 grading.*

## What is proved (symbolic, exact — sympy)

Let C^μ_ν = g^{μα} g̃_{αν}. For fully symbolic g (arbitrary symmetric 4×4), fully symbolic u,
with N = g(u,u) left symbolic — no frame chosen, so the statements are covariant by
construction — and again in an orthonormal frame at arbitrary boost:

- **Eigenstructure.** charpoly(C) = (x − A)³ (x − A(1 + BN)). At N = −1: eigenvalue **A**
  (triple; eigenspace = u-perp, g-spacelike) and **A(1 − B)** (simple; eigenvector u,
  g-timelike). So (A, B, u) are recovered from the metric pair — A the triple eigenvalue,
  B = 1 − simple/triple, u the timelike eigenvector normalized to g(u,u) = −1, unique up to
  sign. B ≠ 0 is necessary: at B = 0, C = A·I and u is undetermined.
- **Converse (recognition criterion).** C is g-self-adjoint (gC = g̃ symmetric), so eigenspaces
  at distinct eigenvalues are g-orthogonal; a diagonalizable 3+1 pattern (triple eigenvalue on a
  g-spacelike 3-space, simple eigenvalue with g-timelike eigenvector) therefore *rebuilds* the
  seam form g̃ = L(g + (1 − M/L) u⊗u). Membership is decidable from the eigenvalue pattern.
- **Determinant identity.** det g̃ = A⁴ (1 − B) det g (the c9 A = 1 seam is the (1−B) special
  case). With A = 1 − B/3: det g̃/det g = F(B) = (1 − B/3)⁴(1 − B), and
  F′(B) = (1 − B/3)³(5B − 7)/3 < 0 on all B < 1 — F injective, so one metered volume ratio
  recovers B (hence A) by itself.
- **Signature bound.** g + B u⊗u is congruent to diag(B − 1, 1, 1, 1): Lorentzian −+++ iff
  **B < 1** (unbounded below). Admissible range B ∈ (−∞, 1) \ {0}. B ∈ (0,1) nests the g̃-cone
  strictly inside the g-cone; B < 0 strictly outside.
- **Null (Kerr–Schild) boundary.** g̃ = g + B k⊗k with k null: C − I = B k k♭ is nilpotent of
  index 2, C ≠ I — non-diagonalizable, Jordan blocks [2,1,1] at eigenvalue 1, det g̃ = det g.
  All eigenvalues equal 1, as at B = 0: the null class is separated from the timelike class by
  Jordan structure, not by eigenvalues.

## What is verified numerically (numpy, seed 20260712)

- 1000 positive trials (random congruence g = SᵀηS, cond(S) < 50; random unit timelike u;
  B ∈ (−2, 0.95), |B| ≥ 0.05; A ∈ (0.2, 3)) + 500 with A = 1 − B/3: recovery of (A, B, u) and
  rebuild of g̃, max relative error ~10⁻¹¹ or better. 1000/1000 and 500/500.
- 1000 generic nested-cone controls (g̃ = g + P, P positive definite — nested by construction):
  4 distinct eigenvalues every time, 0 false recognitions. The class is measure-zero *and*
  recognizable.
- 1000 Kerr–Schild controls: rank-1 nilpotent C − I, det g̃ = det g, classified null, 0 false
  recognitions as timelike.
- 100 B = 0 controls (conformal); 200 conformal-rescale trials: B and the direction of u are
  invariants of the *pair of conformal classes*; A alone carries the volume gauge, scaling as
  the ratio of conformal factors.

## What is imported (the Malament chain)

- **Malament 1977** (J. Math. Phys. **18**, 1399–1404, "The class of continuous timelike curves
  determines the topology of spacetime"), sharpening **Hawking–King–McCarthy 1976** (J. Math.
  Phys. **17**, 174–181): a chronological bijection (f and f⁻¹ preserve ≪) between two
  past-**and**-future-distinguishing spacetimes of dimension > 2 is a smooth conformal isometry.
  The distinguishing hypothesis is sharp — future-distinguishing alone admits counterexamples.
  HKM needed strong causality and path-topology homeomorphisms; Malament weakened to ≪ and
  distinguishing.
- Chain, assembled: two causal orders → two conformal classes (Malament, applied once per
  cone) → membership in the rank-1 timelike class decidable, and (B, u) recovered, from the
  conformal classes alone (this lemma) → A = 1 − B/3 pins the conformal-factor ratio → one
  volume normalization (a single clock/rod gauge, or the metered det ratio via F(B)) fixes the
  last overall scale. Net: **two causal orders + one volume normalization determine
  (g, g̃, u, B) outright**, u up to sign. Hypotheses carried: both orders past-and-future
  distinguishing; B < 1, B ≠ 0; the pointwise algebra is a field-of-eigenvalues statement —
  smoothness of the recovered (A, B, u) fields follows from simple-eigenvalue perturbation
  theory wherever B ≠ 0, but no global/dynamical uniqueness is claimed here. C5's full
  conjecture (dynamics included) stays open.

## Flags

Primary texts (arXiv, AIP, Springer, Semantic Scholar, INSPIRE) were egress-blocked; the
Malament/HKM statements were verified against search-snippet quotations of the theorems
(HKMM form: chronological bijection ⟺ conformal isometry for d > 2 distinguishing spacetimes),
volume/page metadata against ADS, OSTI, and Caltech-authors listings. The dimension caveat
(d > 2) and the sharpness of the distinguishing hypothesis come from those secondary
statements, not from the primary PDFs.
