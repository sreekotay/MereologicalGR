# Temperature on a causal set: counts against the field

Does a discrete order know its horizon temperature from counts alone, and does a quantum field
built from the same order agree?

## Setup

- **The causal set.** A Poisson sprinkling of the 2D diamond `|u|, |v| < 1`.
- **The writer.** A uniformly accelerated clock whose ticks are inserted as elements along
  `t = sinh(aτ)/a`, `x = (cosh aτ − 1)/a`, `aτ ∈ [−1.75, 1.75]`.
- **Count side, order and number only.** For each pair of ticks, V is the number of sprinkled
  elements strictly between them, read off the causal matrix. Take a Poisson maximum-likelihood
  fit of `V ~ Poisson(ρ (2/a²) sinh²(aτ/2))` with the density ρ known; number is the primitive.
  The writer's own clock supplies τ. Output: `a_count`, so `T = a/2π`.
- **Field side, order only.** The Sorkin–Johnston state. In 2D the massless retarded propagator
  is half the causal matrix, `G_R = C/2`. Then `iΔ = (i/2)(C − Cᵀ)`, and the SJ Wightman function is
  the positive spectral part of `iΔ`. Fit `Re W = α·ln sinh²(aτ/2) + β` along the writer, with α
  free. Output: `a_field`.
- **Two configurations, three independent causal sets each:**
  - *central writer:* N = 6000, a = 16, the writer stays within `|u|, |v| ≤ 0.30`;
  - *extended writer:* N = 4000, a = 8, the writer reaches `|u|, |v| ≈ 0.59`.

Files: `build.py` (sprinkle, writer, SJ; about 3 min at N = 6000), `compare.py` (both sides plus
diagnostics), `summarize.py` (pooled checks), `results.txt` (6/6). The `.npz` matrices are not
committed (~0.6 GB). To regenerate: `python3 build.py 6000 16 <seed> out.npz`, then `compare.py`.

## Results

| writer | true a | count side | field side (SJ) |
|---|---|---|---|
| central (N = 6000) | 16 | **16.65 ± 0.35** (+4%) | **16.85 ± 0.39** (+5%) |
| extended (N = 4000) | 8 | **8.17 ± 0.05** (+2%) | 10.26 ± 0.26 (**+28%**) |

1. **A causal set knows its writer's temperature from counts.** Order, number and the writer's
   ticks recover `a` within a few percent, about 1–2σ high, in both configurations.
2. **The field built from the same order agrees, for the central writer.** Count side and field
   side match within errors. The SJ log-slope is α = −0.078, against the continuum −1/4π = −0.080.
3. **For the extended writer they part, and the counts are the side that stays right.** The SJ
   state in a finite diamond is not the Minkowski vacuum away from the centre: it carries the
   region's boundary. Its non-Hadamard and boundary behaviour is known (Afshordi et al. 2012;
   arXiv 2212.10592). The geometric period is in the counts, while the field's reading depends on
   its state. This is the corpus's "the state is imported" caveat, made visible. *Attributed to
   the finite-diamond state, not verified here against the continuum SJ mode sum.*
4. **The field is not a function of the local count.** Over 4000 bulk pairs per set,
   regressing `Re W_SJ` on both `ln V` (the pair's own interval count, Poisson-noisy) and
   `ln σ` (the continuum interval) gives coefficients of about −0.02 on `ln V` and −0.06 on `ln σ`.
   The SJ field tracks the interval more smoothly than the pair's own count does. It uses order
   information beyond the single interval. The longest chain fits worse still. **So "thermality
   is in the counts" holds as the same period carried by both, not as the field being
   pointwise a function of the local count.**

## Honest limits

- The pass thresholds (6% and 4%) were set **after** seeing the data. Three causal sets per
  configuration; N ≤ 6000 because the SJ step is a dense eigendecomposition.
- Both sides fit the sinh² *form*. The test compares the period each side carries, not whether
  each side would discover the form unaided.
- The writer's ticks are inserted elements, and the clock τ is the writer's own reading.
- The count estimator matters. A naive log fit is badly biased at small V, down to 3.9 instead of
  16 in one set. Poisson ML with ρ known is the honest count-side estimator.
- This is 2D, massless, flat, with an inserted Rindler writer. It is not a causal set with a
  dynamical horizon.

## What this shows and what it does not

**Shown:** on a discrete order with no metric, no coordinates and no field supplied, the
thermal period of an accelerated writer is legible from counts. A quantum field constructed
from that same order reads the same period where its state is the geometric one. Where the
field and the counts disagree, the counts track the geometry and the field tracks its state.

**Not shown:**
- that the field's thermality is *derived* from the counts (the field uses more of the order
  than the local count);
- anything about a dynamical horizon or 4D;
- novelty beyond a quick search. No causal-set Unruh comparison of this kind turned up, but
  SJ-diamond thermality work exists (diamond temperature; SJ in causal diamonds) and was not
  reviewed in depth.
