#!/usr/bin/env python3
"""
Referee script: the recognition lemma for rank-1 timelike cone deformations
(c9's two-metric seam; the algebraic half of C5's two-order uniqueness conjecture).

Conventions (match c9 / workbench/two-metric-seam/): signature -+++,
u unit timelike with g(u,u) = -1, seam form

    gt_{mn} = A ( g_{mn} + B u_m u_n ),   u_m = g_{mn} u^n,   A > 0,

c9 normalization A = 1 - B/3 (bianchi_seam_branch.py finite-branch realization
gt = (1 - B/3)(g + B u@u)); the un-dressed c9 seam is A = 1, det gt = (1-B) det g.

LEMMA (proved symbolically in [S1]-[S3], verified numerically in [N1]-[N5]).
Let C^m_n = g^{ma} gt_{an} (a (1,1) tensor; eigenvalues frame-invariant).

(a) Uniqueness/recognition. If gt = A(g + B u@u), A > 0, B != 0, B < 1,
    g(u,u) = -1, then
      C = A( I + B u u_flat ),
      eigenvalues: A      (triple; eigenspace = u-perp, g-spacelike)
                   A(1-B) (simple; eigenvector u, g-timelike),
    so from the pair (g, gt) the data (A, B, u) is uniquely determined:
      A = triple eigenvalue, B = 1 - simple/triple, u = the timelike
      eigenvector normalized to g(u,u) = -1 -- unique up to u -> -u.
    Under conformal rescaling g -> e^{2p} g, gt -> e^{2q} gt: C -> e^{2(q-p)} C,
    so B and the direction of u depend only on the two CONFORMAL CLASSES
    (eigenvalue ratio + eigenvectors are scale-free); A carries the one
    remaining scalar, fixed by one volume normalization (or by A = 1 - B/3).

(b) Recognition criterion (converse). A pair of -+++ metrics at a point is
    in the class IFF C is diagonalizable with a triple eigenvalue L on a
    g-spacelike 3-space and a simple eigenvalue M != L with g-timelike
    eigenvector (L, M > 0 then automatic from the signatures). Converse
    mechanics: C is g-self-adjoint (g C = gt is symmetric), so eigenspaces at
    distinct eigenvalues are g-orthogonal (L g(v,u) = g(Cv,u) = g(v,Cu)
    = M g(v,u)); hence the triple eigenspace is exactly u-perp and
    gt = gC = L( g + (1 - M/L) u_flat@u_flat ): the seam form with
    A = L, B = 1 - M/L. A generic pair of nested cones has 4 distinct
    eigenvalues: the class is measure-zero AND algorithmically recognizable.

(c) Determinant identity. det gt = A^4 (1 - B) det g. With A = 1 - B/3:
      det gt / det g = (1 - B/3)^4 (1 - B) =: F(B),
      F'(B) = (1 - B/3)^3 (5B - 7)/3 < 0 for all B < 1,
    so F is strictly decreasing on the admissible range: one metered volume
    ratio recovers B (hence A) by itself, collapsing the conformal ambiguity.

(d) Boundaries. B = 0: C = A I, u undetermined -- hypothesis B != 0 is
    necessary. Signature: g + B u@u is congruent to diag(B-1, 1, 1, 1), so it
    stays Lorentzian -+++ IFF B < 1 (unbounded below); B = 1 degenerate,
    B > 1 Riemannian. Admissible: B in (-inf, 1) \\ {0}. For B in (0,1) the
    gt-cone is strictly inside the g-cone; for B < 0 strictly outside.
    Kerr-Schild (u -> null k, gt = g + B k@k): C - I = B k k_flat with
    (C - I)^2 = B^2 (k.k) k k_flat = 0 and C != I, so C is NON-diagonalizable
    (minimal polynomial (x-1)^2; Jordan blocks [2,1,1] at eigenvalue 1) and
    det gt = det g. The null class is distinguished from the timelike class
    by Jordan structure, not by eigenvalues (which all equal 1, as at B = 0).

(e) Imported (Malament chain; citation details verified via web search
    snippets -- primary PDFs egress-blocked, see README). Malament 1977
    (J. Math. Phys. 18, 1399-1404), sharpening Hawking-King-McCarthy 1976
    (J. Math. Phys. 17, 174-181): a chronological bijection between two
    past-AND-future-distinguishing spacetimes (d > 2) is a smooth conformal
    isometry; the distinguishing hypothesis is sharp. Chain: two causal
    orders -> two conformal classes (Malament, once per cone) -> membership
    decidable and (B, u) recovered from the classes alone (this lemma) ->
    A = 1 - B/3 pins the conformal-factor RATIO -> one volume normalization
    fixes the last overall scale -> (g, gt, u, B) determined outright.

Run: python3 recognition_lemma.py   (every check must print PASS)
"""

import numpy as np
import sympy as sp

RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append((name, bool(ok)))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{('  [' + detail + ']') if detail else ''}")
    return bool(ok)


# ===========================================================================
print("[S1] sympy, fully general (no frame chosen): g arbitrary symmetric 4x4,")
print("     u arbitrary 4-vector, N := g(u,u) left symbolic; A, B, x symbolic")

x, A, B = sp.symbols('x A B')
gsym = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'g{min(i, j)}{max(i, j)}'))
u = sp.Matrix([sp.Symbol(f'u{i}') for i in range(4)])
w = gsym * u                      # u_flat
N = (u.T * gsym * u)[0]           # g(u,u), left symbolic
I4 = sp.eye(4)

Cfac = A * (I4 + B * u * w.T)     # candidate C = A(I + B u u_flat)

check("g.C = gt = A(g + B u_flat u_flat) exactly (C^m_n = g^{ma} gt_{an})",
      sp.expand(gsym * Cfac - A * (gsym + B * w * w.T)) == sp.zeros(4, 4))

charpoly = (x * I4 - Cfac).det()
target = (x - A) ** 3 * (x - A * (1 + B * N))
check("charpoly(C) = (x - A)^3 (x - A(1+BN))  [fully general g, u]",
      sp.expand(charpoly - sp.expand(target)) == 0,
      "N = -1: eigenvalues A (triple), A(1-B) (simple)")

check("C u = A(1+BN) u  (u the simple eigenvector; eigenvalue A(1-B) at N = -1)",
      sp.expand(Cfac * u - A * (1 + B * N) * u) == sp.zeros(4, 1))

check("C - A.I = A.B u u_flat (rank 1): C acts as A on the 3-space u-perp = ker(u_flat)",
      sp.expand(Cfac - A * I4 - A * B * u * w.T) == sp.zeros(4, 4))

check("det(I + B u u_flat) = 1 + BN  =>  det gt = A^4 (1+BN) det g",
      sp.expand((I4 + B * u * w.T).det() - (1 + B * N)) == 0,
      "N = -1: det gt = A^4 (1-B) det g; c9 A = 1 seam: det gt = (1-B) det g")

M1 = B * u * w.T
check("(B u u_flat)^2 = B^2 N u u_flat: nilpotent IFF u null (N = 0)",
      sp.expand(M1 * M1 - B ** 2 * N * u * w.T) == sp.zeros(4, 4),
      "null: (C-I)^2 = 0, C != I -> minimal poly (x-1)^2 -> non-diagonalizable")

# ===========================================================================
print("[S2] sympy, orthonormal frame + boost: g = eta, u = (cosh X, sinh X, 0, 0)")

chi = sp.symbols('chi', real=True)
eta = sp.diag(-1, 1, 1, 1)
ub = sp.Matrix([sp.cosh(chi), sp.sinh(chi), 0, 0])
wb = eta * ub
check("u unit timelike for every boost: g(u,u) = -1",
      sp.simplify((ub.T * eta * ub)[0] + 1) == 0)

Cb = A * (I4 + B * ub * wb.T)
check("frame form: charpoly = (x - A)^3 (x - A(1-B)) for every boost chi",
      sp.simplify(sp.expand((x * I4 - Cb).det())
                  - sp.expand((x - A) ** 3 * (x - A * (1 - B)))) == 0,
      "frame-covariant: S1 proved the same with no frame at all")

gtb = A * (eta + B * wb * wb.T)
check("frame form: det gt = A^4 (1-B) det eta = -A^4 (1-B)",
      sp.simplify(gtb.det() + A ** 4 * (1 - B)) == 0)

e0 = sp.Matrix([1, 0, 0, 0])
gt0 = eta + B * (eta * e0) * (eta * e0).T
check("g + B u@u congruent to diag(B-1, 1, 1, 1): Lorentzian -+++ IFF B < 1 (and A > 0)",
      gt0 == sp.diag(B - 1, 1, 1, 1),
      "admissible B in (-inf, 1) \\ {0}; B = 1 degenerate; B > 1 Riemannian")

aang = sp.Symbol('alpha', real=True)
v_null = sp.Matrix([1, sp.cos(aang), sp.sin(aang), 0])     # g-null for every alpha
check("on g-null v: gt(v,v) = A B (u_flat.v)^2 -- B>0 nests the gt-cone strictly inside",
      sp.simplify((v_null.T * gtb * v_null)[0]
                  - A * B * ((wb.T * v_null)[0]) ** 2) == 0,
      "B < 0: gt-cone strictly outside; sign of B = nesting orientation")

k = sp.Matrix([1, 1, 0, 0])
kf = eta * k
Cks = I4 + B * k * kf.T
check("Kerr-Schild: (C - I)^2 = 0 and C - I != 0 for B != 0",
      sp.expand((Cks - I4) ** 2) == sp.zeros(4, 4)
      and sp.expand(Cks - I4) != sp.zeros(4, 4))
_, Jj = Cks.subs(B, 2).jordan_form()
blocks = sorted([int(b.rows) for b in Jj.get_diag_blocks()], reverse=True)
check("Kerr-Schild Jordan form (B = 2): blocks [2,1,1], all eigenvalues 1",
      blocks == [2, 1, 1] and all(Jj[i, i] == 1 for i in range(4)),
      "eigenvalues alone cannot separate the null class from B = 0; Jordan structure can")
check("Kerr-Schild determinant: det gt = det g exactly",
      sp.simplify((eta + B * kf * kf.T).det() - eta.det()) == 0)

# ===========================================================================
print("[S3] sympy: the c9 normalization A = 1 - B/3 collapses the volume gauge")

F = (1 - B / sp.Integer(3)) ** 4 * (1 - B)
dF = sp.diff(F, B)
check("F(B) = det gt/det g = (1 - B/3)^4 (1-B);  F'(B) = (1 - B/3)^3 (5B - 7)/3",
      sp.simplify(dF - (1 - B / sp.Integer(3)) ** 3 * (5 * B - 7) / 3) == 0)
t = sp.symbols('t', positive=True)              # B = 1 - t covers all B < 1
dF_sub = sp.factor(dF.subs(B, 1 - t))           # = -(t+2)^3 (5t+2) / 81
check("F' < 0 on the whole admissible range B < 1  (B = 1 - t, t > 0)",
      sp.expand(dF_sub + (t + 2) ** 3 * (5 * t + 2) / 81) == 0
      and sp.ask(sp.Q.negative(dF_sub)),
      "F strictly decreasing: a metered volume ratio alone recovers B, hence A")

# ===========================================================================
print("[N1] numpy: positive trials -- recover (A, B, u) to machine precision")

rng = np.random.default_rng(20260712)
ETA = np.diag([-1.0, 1.0, 1.0, 1.0])


def random_frame(max_cond=50.0):
    while True:
        S = rng.normal(size=(4, 4))
        if np.linalg.cond(S) < max_cond:
            return S


def random_unit_timelike(g, S):
    r = rng.normal(size=3)
    r *= rng.uniform(0.0, 0.95) / max(np.linalg.norm(r), 1e-12)
    v = np.concatenate(([1.0], r))               # eta-timelike
    uu = np.linalg.solve(S, v)                   # g-timelike
    return uu / np.sqrt(-(uu @ g @ uu))


def draw_B(lo=-2.0, hi=0.95, floor=0.05):
    while True:
        b = rng.uniform(lo, hi)
        if abs(b) >= floor:
            return b


def seam_pair(A_val, B_val):
    S = random_frame()
    g = S.T @ ETA @ S
    uu = random_unit_timelike(g, S)
    uf = g @ uu
    return g, A_val * (g + B_val * np.outer(uf, uf)), uu


def recognize(g, gt, rtol_group=1e-7, rtol_quad=5e-6, sep=1e-4):
    """Classify a metric pair at a point from C = g^{-1} gt.
    Returns (label, data), label in {'rank1-timelike', 'conformal',
    'null-rank1', 'generic'}."""
    C = np.linalg.solve(g, gt)
    ev, V = np.linalg.eig(C)
    scale = np.max(np.abs(ev))
    # -- quadruple cluster first (conformal, or Kerr-Schild: defective
    #    eigenvalues split only at ~sqrt(machine eps))
    mean_all = np.mean(ev)
    if np.max(np.abs(ev - mean_all)) < rtol_quad * scale and abs(mean_all.imag) < rtol_quad * scale:
        lam = mean_all.real
        D = C - lam * np.eye(4)
        sv = np.linalg.svd(D, compute_uv=False)
        if sv[0] < rtol_quad * scale:
            return 'conformal', {'A': lam}
        if sv[1] < 1e-8 * sv[0] and np.linalg.norm(D @ D) < 1e-10 * sv[0] ** 2 + 1e-13:
            return 'null-rank1', {'A': lam}
        return 'generic', {}
    # -- 3+1 split: a simple eigenvalue against a triple
    if np.max(np.abs(ev.imag)) > rtol_group * scale:
        return 'generic', {}
    evr = ev.real
    for i in range(4):
        triple = np.delete(evr, i)
        lam = triple.mean()
        if np.max(np.abs(triple - lam)) >= rtol_group * scale or abs(evr[i] - lam) <= sep * scale:
            continue
        mu = evr[i]
        D = C - lam * np.eye(4)
        _, sv, Vt = np.linalg.svd(D)
        # geometric multiplicity of lam must be 3: rank(C - lam I) = 1
        if not (sv[0] > sep * scale and sv[1] < 10 * rtol_group * scale):
            return 'generic', {}
        uu = V[:, i].real
        q = uu @ g @ uu
        if q >= 0:
            return 'generic', {}               # simple eigenvector not timelike
        uu = uu / np.sqrt(-q)
        W = Vt[1:, :].T                        # 3-dim null space of D: triple eigenspace
        if np.any(np.linalg.eigvalsh(W.T @ g @ W) <= 0):
            return 'generic', {}               # triple eigenspace not g-spacelike
        if lam <= 0 or mu <= 0:
            return 'generic', {}               # both metrics could not be -+++
        return 'rank1-timelike', {'A': lam, 'B': 1.0 - mu / lam, 'u': uu, 'W': W}
    return 'generic', {}


def positive_trial(c9=False):
    B_val = draw_B()
    A_val = (1.0 - B_val / 3.0) if c9 else rng.uniform(0.2, 3.0)
    g, gt, uu = seam_pair(A_val, B_val)
    label, d = recognize(g, gt)
    if label != 'rank1-timelike':
        return False, (1.0, 1.0, 1.0, 1.0, 1.0)
    eA = abs(d['A'] - A_val) / A_val
    eB = abs(d['B'] - B_val) / abs(B_val)
    eu = min(np.linalg.norm(d['u'] - uu), np.linalg.norm(d['u'] + uu))
    uf = g @ d['u']
    erec = (np.linalg.norm(d['A'] * (g + d['B'] * np.outer(uf, uf)) - gt)
            / np.linalg.norm(gt))
    orth = np.max(np.abs(d['W'].T @ g @ d['u']))    # u-perp = triple space
    ok = eA < 1e-7 and eB < 1e-7 and eu < 1e-6 and erec < 1e-8 and orth < 1e-6
    return ok, (eA, eB, eu, erec, orth)


NPOS, NC9 = 1000, 500
hits, maxes = 0, [0.0] * 5
for _ in range(NPOS):
    ok, errs = positive_trial()
    hits += ok
    maxes = [max(a, b) for a, b in zip(maxes, errs)]
check(f"positive trials, general A: {hits}/{NPOS} recognized and recovered",
      hits == NPOS,
      f"max rel err: A {maxes[0]:.1e}, B {maxes[1]:.1e}, |du| {maxes[2]:.1e}, "
      f"rebuild {maxes[3]:.1e}, u-perp orth {maxes[4]:.1e}")

hits9, maxes9 = 0, [0.0] * 5
for _ in range(NC9):
    ok, errs = positive_trial(c9=True)
    hits9 += ok
    maxes9 = [max(a, b) for a, b in zip(maxes9, errs)]
check(f"positive trials, c9-normalized A = 1 - B/3: {hits9}/{NC9} recovered",
      hits9 == NC9,
      f"max rel err: A {maxes9[0]:.1e}, B {maxes9[1]:.1e}, |du| {maxes9[2]:.1e}, "
      f"rebuild {maxes9[3]:.1e}")

ok_det, ndet = True, 200
for _ in range(ndet):
    B_val, A_val = draw_B(), rng.uniform(0.2, 3.0)
    g, gt, _ = seam_pair(A_val, B_val)
    lhs, rhs = np.linalg.det(gt), A_val ** 4 * (1 - B_val) * np.linalg.det(g)
    ok_det &= abs(lhs - rhs) < 1e-8 * abs(lhs)
check(f"det gt = A^4 (1-B) det g on {ndet} random pairs", ok_det)

# ===========================================================================
print("[N2] numpy: negative control -- generic nested cones (1000 trials)")


def generic_nested_frame():
    # eta-frame: gt0 = eta + P, P symmetric positive definite => every
    # eta-null v has gt0(v,v) = v.P.v > 0: strict nesting BY CONSTRUCTION
    while True:
        Q = np.linalg.qr(rng.normal(size=(4, 4)))[0]
        P = Q @ np.diag(rng.uniform(0.05, 0.6, size=4)) @ Q.T
        gt0 = ETA + P
        if (np.linalg.eigvalsh(gt0) < 0).sum() == 1:    # still Lorentzian
            return gt0


n_generic, false_pos, four_distinct = 1000, 0, 0
for _ in range(n_generic):
    gt0 = generic_nested_frame()
    S = random_frame()
    g, gt = S.T @ ETA @ S, S.T @ gt0 @ S
    label, _ = recognize(g, gt)
    false_pos += (label == 'rank1-timelike')
    ev = np.linalg.eigvals(np.linalg.solve(g, gt))
    evs = np.sort(ev.real)
    four_distinct += (np.max(np.abs(ev.imag)) < 1e-9
                      and np.min(np.diff(evs)) > 1e-6 * np.max(np.abs(evs)))
check(f"generic nested cones: 0/{n_generic} false recognitions", false_pos == 0)
check(f"generic nested cones: 4 distinct eigenvalues in every trial "
      f"({four_distinct}/{n_generic})", four_distinct == n_generic,
      "the rank-1 timelike class is measure-zero among nested-cone pairs")

ok_nest, n_nest = True, 100
for _ in range(n_nest):
    gt0 = generic_nested_frame()
    a = rng.normal(size=3)
    v = np.concatenate(([1.0], a / np.linalg.norm(a)))   # eta-null
    ok_nest &= (v @ gt0 @ v) > 0
check(f"control family really is nested: {n_nest}/{n_nest} sampled g-null "
      "vectors are gt-spacelike", ok_nest,
      "gt-cone strictly inside g-cone, the seam's B > 0 orientation")

# ===========================================================================
print("[N3] numpy: negative control -- Kerr-Schild null deformations (1000 trials)")

n_ks, ks_false, ks_jordan = 1000, 0, 0
for _ in range(n_ks):
    S = random_frame()
    g = S.T @ ETA @ S
    a = rng.normal(size=3)
    kv = np.linalg.solve(S, np.concatenate(([1.0], a / np.linalg.norm(a))))
    kv /= np.linalg.norm(kv)                             # g-null, normalized
    B_val = rng.uniform(0.3, 1.2) * rng.choice([-1.0, 1.0])
    kf = g @ kv
    gt = g + B_val * np.outer(kf, kf)
    label, _ = recognize(g, gt)
    ks_false += (label == 'rank1-timelike')
    C = np.linalg.solve(g, gt)
    D = C - np.eye(4)
    sv = np.linalg.svd(D, compute_uv=False)
    rank1 = sv[0] > 1e-4 and sv[1] < 1e-8 * sv[0]
    nilp = np.linalg.norm(D @ D) < 1e-10 * sv[0] ** 2 + 1e-13
    detok = abs(np.linalg.det(gt) - np.linalg.det(g)) < 1e-8 * abs(np.linalg.det(g))
    ks_jordan += (rank1 and nilp and detok and label == 'null-rank1')
check(f"Kerr-Schild: 0/{n_ks} false recognitions as the timelike class",
      ks_false == 0)
check(f"Kerr-Schild: {ks_jordan}/{n_ks} show rank-1 nilpotent C - I, "
      "det gt = det g, and classify null-rank1", ks_jordan == n_ks,
      "non-diagonalizable: geometric multiplicity 3 at eigenvalue 1, Jordan [2,1,1]")

# ===========================================================================
print("[N4] numpy: boundary B = 0 -- conformal pairs (100 trials)")

n_conf, conf_ok = 100, 0
for _ in range(n_conf):
    S = random_frame()
    g = S.T @ ETA @ S
    A_val = rng.uniform(0.2, 3.0)
    label, d = recognize(g, A_val * g)
    conf_ok += (label == 'conformal' and abs(d['A'] - A_val) < 1e-9 * A_val)
check(f"B = 0: {conf_ok}/{n_conf} classified conformal with u undetermined "
      "(hypothesis B != 0 is necessary)", conf_ok == n_conf)

# ===========================================================================
print("[N5] numpy: conformal-class invariance of (B, u-direction) (200 trials)")

n_inv, inv_ok = 200, 0
for _ in range(n_inv):
    B_val, A_val = draw_B(), rng.uniform(0.2, 3.0)
    g, gt, _ = seam_pair(A_val, B_val)
    p2, q2 = np.exp(rng.uniform(-1, 1)), np.exp(rng.uniform(-1, 1))  # e^{2p}, e^{2q}
    l1, d1 = recognize(g, gt)
    l2, d2 = recognize(p2 * g, q2 * gt)
    if l1 == l2 == 'rank1-timelike':
        same_B = abs(d1['B'] - d2['B']) < 1e-8 * max(1.0, abs(B_val))
        du = min(np.linalg.norm(d2['u'] * np.sqrt(p2) - d1['u']),
                 np.linalg.norm(d2['u'] * np.sqrt(p2) + d1['u']))
        same_A = abs(d2['A'] - (q2 / p2) * d1['A']) < 1e-8 * d1['A']
        inv_ok += (same_B and du < 1e-6 and same_A)
check(f"conformal rescale g -> p.g, gt -> q.gt: B and u-direction invariant, "
      f"A -> (q/p) A: {inv_ok}/{n_inv}", inv_ok == n_inv,
      "(B, u) live on the pair of conformal classes; A is the one volume-gauge scalar")

# ===========================================================================
n_ok = sum(1 for _, ok in RESULTS if ok)
print(f"\n{n_ok}/{len(RESULTS)} checks passed"
      + ("" if n_ok == len(RESULTS) else "  *** FAILURES ***"))
