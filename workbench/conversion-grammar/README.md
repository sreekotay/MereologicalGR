# The Conversion Grammar Workbench

*Workbench — non-canonical. Numeric experiments supporting c8's ratio program (the
one-conversion-law bet, stated and not pointed). Two phases: the shape program, run and killed
here (2026-07); the exponent program, pre-registered here (2026-07). Referee scripts in this
directory. Not promoted; promotion requires A0 grading.*

## Phase 1 — the shape program, dead

`xcompare.py`, `power.py`: cross-register comparison of conversion-weight *shapes*
(fragmentation D(z), distillation E_D(F), QEC suppression) is unrunnable. The beta-family
template hits R² > 0.99 on 100% of random single-humped curves — its own observable class —
and on 13–44% of random monotone curves it has no claim to (`power.py`, `xcompare.py`), the
registers are not one observable class (a density against cumulatives), and shared-form is
indistinguishable from generic smoothness. Banked in c8: the earning test must be a
**pre-registered exponent relation** with no per-register abscissa freedom.

## Phase 2 — the exponent relation (`counting_rules.py`)

```text
rate ~ C_R · ε_R^(N_R),   f(N) = N in every register

ε_R = per-part cost at the register's level of independent composition:
      coherent (one matrix element)  → |per-part amplitude weight|²
      stochastic (classical events)  → per-part probability, unsquared
N_R = minimal number of ε-carrying parts whose joint state-change one
      conversion event requires — counted data-blind (quantum numbers /
      decoder guarantee / energy conservation; never from the slope)
```

Three registers, counted before data:

- **Brodsky–Farrar / MMT** (hard exclusive QCD): each elementary line crossing the hard
  interface costs Λ/√s in amplitude → dσ/dt ~ s^(2−n_tot). The crossing count replaces the
  participant/spectator convention (a form-factor constituent crosses twice → 1/Q² per part;
  gluon −2 + quark −1 + numerator +1 = −2 is the same ledger). DYW corollary makes the level
  assignment checkable: (1−x)^(2n_s−1) — the 2 is the coherence square, the −1 is measure.
- **QEC** (stochastic): minimal conspiring errors = ⌊(d−1)/2⌋+1 = ⌈d/2⌉ (= (d+1)/2 odd d;
  d/2 even d — the quoted ⌈(d+1)/2⌉ overstates even-d suppression). ε = p, no square: no
  amplitude level exists.
- **Multiphoton ionization** (third register, pre-registered): rate ~ I^N,
  N = ⌈E_ion/ħω⌉ — spectroscopic, intensity-blind. Domain: Keldysh γ ≫ 1, below saturation.

Results (script, run clean): repetition-code MC slopes 1.98 / 3.00 / 3.93 against predicted
2 / 3 / 4 (d = 3, 5, 7; 2×10⁷ trials/point); BF table lands 12→s⁻¹⁰, 9→s⁻⁷ (measured
7.1±0.2), 13→s⁻¹¹; MPI Xe 11-photon I¹¹ verified in the literature.

## Kill conditions (registered before the data columns were filled)

1. Any register needing f ≠ identity after the stated ε-level rule — the law dies.
2. Any register whose N cannot be stated data-blind ("effective" counts chosen after the
   slope) — bet unplaceable; the shape program's death, again.
3. Named near-term killers: Google Willow logical-error-vs-d (Λ = 2.14±0.02, d 5→7, Nature
   638, 920); JLab 12-GeV exclusive 90° scaling; any sub-saturation MPI intensity scan.

**Negative control:** chemical reaction order vs molecularity. Order = molecularity only for
a single elementary step; multi-step mechanisms are sequences of conversion events and the
law's own hypothesis (all N parts in ONE event) refuses them. A law that also fit multi-step
kinetics would be the smoothness disease again.

## Adjacency verdict (the parked audit stays parked)

The exponent counts parts that must participate coherently in one conversion event — a
contact *cardinality*, not adjacency. Correlated-noise MC (script §2): pair-events re-atomize
the count to ⌈⌈d/2⌉/2⌉, and adjacent vs *random* pairing gives the same exponent — the count
is layout-blind. BF offers a real order/part divergence (the s-exponent counts lines, the α_s
power counts vertices; data follows lines), so the count is not bare perturbation-order — but
what it renders is independence structure (how many units), not spatial extension (where they
sit). Would-carve witness, named: a surface code where only geometrically aligned pair-noise
chains across the logical cut — exponent following layout at fixed unit count. Proposable,
not in hand. USES.md's parked entry gains that witness condition and nothing else.

## Grading (method layer)

- **Imported:** every derivation — dimensional counting in a scale-free theory, decoder
  combinatorics, LOPT — and every measured exponent. The law's common form is owned by
  probability theory + locality (independent per-part costs multiply); c8 pre-priced this
  outcome as the banked relabel.
- **Chosen:** the ε-level rule (coherent → square, stochastic → not) and the crossing-count
  bookkeeping. Data-blind and killable, but other conventions survive.
- **Forced:** nothing yet. One relation, one f, three registers is a placeable bet, not a
  forced structure.
- **Parked:** adjacency, still — with the witness condition sharpened above.

Honest assessment: one law-*form*, not two coincidences — but the form's ownership is
imported. What the grammar adds is the commensuration (which level, which parts), and that
is exactly what conditions (1)–(2) put at risk.

## Flags

Literature exponents marked [v] were verified by web search 2026-07 (γp→π⁺n 7.1±0.2; pp
s⁻¹⁰ with Landshoff oscillations; Willow Λ; Xe I¹¹ law); [m] are memory-sourced (πp, γd→pn,
F_π, F₁, DYW fit range, Cs slope) — primary texts not pulled. The pp 90° data oscillate
about s⁻¹⁰ (generalized counting rule literature); the MPI I^N law breaks at saturation and
at γ ≲ 1 by the law's own domain clause.

Key sources: Brodsky–Farrar PRL 31, 1153 (1973); Matveev–Muradyan–Tavkhelidze Lett. Nuovo
Cim. 7, 719 (1973); Lepage–Brodsky PRD 22, 2157 (1980); Zhu et al PRL 91, 022003 (2003);
Bochna et al PRL 81, 4576 (1998); Fowler et al PRA 86, 032324 (2012); Google Quantum AI,
Nature 638, 920 (2024); Kruit et al PRA 28, 248 (1983); Lompré et al JOSA B 2, 1906 (1985);
Mainfray–Manus Rep. Prog. Phys. 54, 1333 (1991); Keldysh JETP 20, 1307 (1965).
