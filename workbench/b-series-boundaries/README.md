# B-series boundary checks

Status: computational checks of the scoped derivations and counterexamples in
[B11](../../b11-composition-relations-and-boundary-tests.md). Not independent experimental
confirmation or a proof of the continuum field-theoretic results cited there.

## Run

Requires Python 3.10+, NumPy, SciPy and SymPy.

```sh
python workbench/b-series-boundaries/check_relations.py
```

A failed check raises an exception and exits nonzero. Numerical comparisons use tolerance
2e-11, except the small-delay finite-difference check (1e-6). The random unitary sample uses
seed 230922. Entropies are in nats; toy calculations set c=ℏ=1 where appropriate.

## Checked on 2026-09-22

`py_compile` succeeded. All 38 checks passed.

| Contact | Checks | Scope |
|---|---:|---|
| B1 | 4 | Matrix ordering residue; a single zero expectation does not imply a zero commutator |
| B2 | 1 | Clock reparametrization changes the rate normalization |
| B3 | 2 | Same input record; copying and idle operations yield different target correlations |
| B6 | 5 | Positive spectral weights and the KMS coth identity |
| B7 | 3 | Hyperbolic interval; orthogonality and rest-energy projection of four-force |
| B8 | 7 | Matched-mean pure-state control; variance dependence; mixed-state counterexample |
| B9 | 5 | Four-site chain connecting order and coupling/time rescaling |
| B10 | 4 | Marker-unitary invariance; correlated-copy reset; finite-bath Landauer equality |
| B4 | 4 | Normalized Wald charge; area shrinkage; first-order flux/area identities |
| B5 | 3 | Metric-compatible flat connection with nonzero torsion |

The count records execution coverage, not 38 independent pieces of evidence. Repeated parameter
values check the same identity. The B1 matrices do not establish continuum microcausality; the
B9 chain does not prove a general Lieb-Robinson theorem. The B4 polynomial checks the linearized
relation under B11's supplied entropy definition. A reversible logical reset does not establish
zero cost for an entire laboratory control cycle. No laboratory visibility or horizon measurement
was performed.
