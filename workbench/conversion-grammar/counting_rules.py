# counting_rules.py -- the pre-registered exponent relation for the conversion bet
#
# Workbench, non-canonical. Successor to xcompare.py / power.py, which killed the
# SHAPE program (beta-family fits random smooth curves at R^2 > 0.99; c8 re-set the
# bar to a pre-registered exponent relation, no per-register abscissa freedom).
#
# THE LAW UNDER TEST (stated before any data below is consulted):
#
#   rate ~ C_R * eps_R ^ N_R
#
#   eps_R = per-part conversion cost, measured at the level where the register's
#           parts compose INDEPENDENTLY:
#             coherent register (one matrix element) -> per-part amplitude weight,
#               entering the rate squared:  eps_R = |a_part|^2
#             stochastic register (classical iid events) -> per-part probability,
#               entering the rate unsquared: eps_R = p_part
#   N_R   = minimal number of eps-carrying parts whose joint state-change is
#           required for one conversion event, computed data-blind (from quantum
#           numbers / decoder guarantee / energy conservation -- never from slope).
#   f(N) = N identically, all registers.  Coefficients C_R register-owned
#           (c8's clause: metering form register-invariant, coefficients owned).
#
# KILL CONDITIONS (pre-registered):
#  (i)   any register needing f != identity after the stated eps-level rule
#        (e.g. calibrated-iid surface-code slope != ceil(d/2));
#  (ii)  any register whose N cannot be stated data-blind ("effective" counts
#        chosen after seeing the slope) -- same death as the shape program;
#  (iii) named datasets that can kill now: Google Willow logical-error-vs-d
#        (Nature 638, 920 (2024), Lambda = 2.14 +/- 0.02 for d=5->7); JLab-12GeV
#        exclusive scaling (gamma p -> pi+ n, gamma d -> pn at 90 deg); any modern
#        sub-saturation intensity scan of MPI with Keldysh gamma >> 1.
#
# Literature exponents below: verified via web search 2026-07 where marked [v];
# memory-sourced and flagged where marked [m].

import numpy as np

rng = np.random.default_rng(7)
LINE = "=" * 78


# ===========================================================================
# S1. BRODSKY-FARRAR / MMT DIMENSIONAL COUNTING (coherent register)
# ===========================================================================
print(LINE)
print("S1. BRODSKY-FARRAR: each elementary line crossing the hard interface")
print("    costs Lambda/sqrt(s) in the AMPLITUDE")
print(LINE)
print("""
Derivation (explicit bookkeeping, not hand-waved):
 1. Wide-angle exclusive 2->2: the only scale in the hard kernel is sqrt(s)
    (dimensionless coupling; masses negligible; t/s fixed).
 2. dsigma/dt = |M|^2 / (16 pi s^2)  with  [dsigma/dt] = mass^-4  =>  M is
    DIMENSIONLESS.
 3. Replace each composite hadron h by its n_h valence lines; the h -> n_h
    Fock coupling carries dimension Lambda^(n_h - 1) (f_pi for n=2, f_N for
    n=3).  An elementary external (photon, lepton) contributes n_h = 1,
    dimension Lambda^0.
 4. M = [prod_h Lambda^(n_h-1)] * T_hat(sqrt(s)); dimensionlessness forces
        T_hat ~ s^((4 - n_tot)/2),   n_tot = sum_h n_h .
    =>  M ~ s^((4-n_tot)/2),  dsigma/dt ~ s^(2 - n_tot).
 5. Per-part reading: every elementary line ENTERING OR LEAVING the hard
    interface costs Lambda/sqrt(s) in M, i.e. eps = Lambda^2/s per line in
    |M|^2.  s^2 * dsigma/dt = |M|^2 ~ eps^(n_tot): pure part-count; the s^-2
    flux/phase-space factor is 2->2 kinematics, register-independent.
 6. Diagram-level cross-check (form-factor kernel, per ADDED constituent):
       one extra hard gluon propagator   : Q^-2
       one extra internal quark line     : Q^-1   (qslash/q^2)
       numerator / spinor algebra        : Q^+1
       net                               : Q^-2  per constituent
    = 2 crossings x (Q^-1 per crossing): the crossing count REPLACES the
    participant/spectator convention -- a form-factor constituent crosses the
    interface twice (in and out), so it pays (1/sqrt(s))^2 = 1/Q^2 even
    though only n-1 gluons appear ("spectators need turning, the struck
    quark rides the photon" is the same ledger, re-partitioned).
 7. Form factor from the SAME rule: e h -> e h has n_tot = 2 + 2 n_h, so
    M ~ s^(1-n_h) = M_pointlike * F(t), fixed angle t ~ s:
        F(Q^2) ~ (Q^2)^(1 - n_h).
 8. Drell-Yan-West corollary (level assignment made checkable): near x -> 1
    the struck quark takes all momentum; holding n_s = n_h - 1 spectators at
    vanishing light-cone fraction costs (1-x)^(n_s) in AMPLITUDE, squared to
    (1-x)^(2 n_s) in probability, one power restored by the phase-space
    measure:  q(x) ~ (1-x)^(2 n_s - 1).
    The '2' is the coherence square; the '-1' is measure, not part-count.
    (This is the counting-rule source of the (1-z)^b falloff in c8's
    fragmentation register: b = 2 n_spectator - 1 before DGLAP evolution.)
""")

# --- fixed-angle processes: bookkeeping + dimensional closure check ---------
PROCESSES = {
    # name: (constituent counts of the 4 external states, measured, source)
    "p p -> p p":        ([3, 3, 3, 3], "s^-10 w/ oscillations (Landshoff)",
                          "[v] arXiv:hep-ph/0411267; data Akerlof/Allaby 90deg"),
    "pi- p -> pi- p":    ([2, 3, 2, 3], "~ s^-8  (90 deg)",
                          "[m] Sivers-Brodsky-Blankenbecler, Phys.Rept.23(1976)1"),
    "gamma p -> pi+ n":  ([1, 3, 2, 3], "s^-(7.1+/-0.2), E_gam > ~3 GeV",
                          "[v] Zhu et al PRL 91,022003(2003); Anderson 1976"),
    "gamma d -> p n":    ([1, 6, 3, 3], "consistent w/ s^-11 above ~1 GeV",
                          "[m] Bochna et al PRL 81,4576(1998); JLab follow-ups"),
}
print(f"{'process':18s} {'n_tot':>5s} {'pred dsig/dt':>13s}  measured / source")
for name, (nh, meas, src) in PROCESSES.items():
    n_tot = sum(nh)
    pred = 2 - n_tot
    # dimensional closure: Lambda-power + 2*s-power of M must vanish
    lam_pow = sum(h - 1 for h in nh)          # = n_tot - 4
    s_pow2 = 4 - n_tot                        # 2 * ((4-n_tot)/2)
    assert lam_pow + s_pow2 == 0, "dimensional closure failed"
    print(f"{name:18s} {n_tot:5d} {'s^%+d' % pred:>13s}  {meas}")
    print(f"{'':24s}{src}")

# --- form factors via the crossing rule -------------------------------------
print(f"\n{'form factor':18s} {'n_h':>4s} {'pred':>10s}  measured / source")
FFS = {
    "F_pi(Q^2)":  (2, "Q^2 F_pi slowly varying ~0.4 GeV^2",
                   "[m] JLab F_pi: Horn et al PRL 97,192001(2006)"),
    "F_1^p(Q^2)": (3, "Q^4 F_1 ~ const, Q^2 > ~8 GeV^2",
                   "[m] SLAC: Sill et al PRD 48,29(1993) class"),
}
for name, (n_h, meas, src) in FFS.items():
    pred = 1 - n_h
    n_tot = 2 + 2 * n_h                       # e h -> e h crossing count
    assert (4 - n_tot) // 2 == pred           # same rule, no new input
    print(f"{name:18s} {n_h:4d} {'(Q^2)^%+d' % pred:>10s}  {meas}")
    print(f"{'':24s}{src}")

print("\nDYW large-x: valence quark in proton, n_s = 2 -> (1-x)^3;")
print("  global PDF fits: u_v ~ (1-x)^(3.0-3.7) at moderate Q^2 [m].")
print("  (Evolution drifts the exponent; the counting rule owns the input scale.)")


# ===========================================================================
# S2. QEC MINIMAL-FAILURE COMBINATORICS (stochastic register)
# ===========================================================================
print("\n" + LINE)
print("S2. QEC: exponent = minimal number of physical errors that must conspire")
print(LINE)
print("""
Derivation:
 1. Distance-d code: any error of weight t = floor((d-1)/2) is corrected
    (decoder guarantee -- weight-t errors are closer to the identity coset
    than to any logical coset).
 2. Minimal weight causing logical failure after optimal decoding:
        t + 1 = floor((d-1)/2) + 1 = floor((d+1)/2) = ceil(d/2).
 3. iid errors at rate p:  p_L = sum_{k >= ceil(d/2)} (failure fraction at
    weight k) C(n,k) p^k (1-p)^(n-k)  ->  leading order  ~ C p^(ceil(d/2)).
 4. ceil(d/2) vs (d+1)/2, resolved: for ODD d they coincide, (d+1)/2 exactly
    (the surface-code convention, Fowler et al PRA 86,032324: d odd, exponent
    (d+1)/2).  For EVEN d the correct exponent is d/2 -- weight-d/2 errors tie
    between cosets and a tie can decode wrong; the sometimes-quoted
    ceil((d+1)/2) = d/2 + 1 overstates even-d suppression.  General law:
        N = ceil(d/2).
 5. Each error is a classical stochastic event: parts compose in PROBABILITY,
    eps = p unsquared.  No amplitude level exists to square.
""")

def majority_fail_exact(d, p):
    """Exact logical failure of a distance-d repetition code, majority vote."""
    from math import comb
    kmin = (d + 1) // 2
    return sum(comb(d, k) * p**k * (1 - p)**(d - k) for k in range(kmin, d + 1))

def fit_slope(ps, pLs):
    return np.polyfit(np.log(ps), np.log(pLs), 1)[0]

print(f"{'d':>2s} {'N pred':>7s} {'MC slope':>9s} {'exact slope':>12s} "
      f"{'C(d,N) check':>13s}  {'trials/pt':>10s}")
WINDOWS = {3: np.geomspace(0.002, 0.02, 5),
           5: np.geomspace(0.008, 0.05, 5),
           7: np.geomspace(0.02, 0.10, 5)}
from math import comb
for d in (3, 5, 7):
    N_pred = (d + 1) // 2                      # = ceil(d/2), d odd
    ps = WINDOWS[d]
    ntrials = int(2e7)
    pL_mc, pL_ex = [], []
    for p in ps:
        flips = rng.binomial(d, p, size=ntrials)   # iid errors per trial
        fails = np.count_nonzero(flips >= N_pred)  # majority decode fails
        pL_mc.append(fails / ntrials)
        pL_ex.append(majority_fail_exact(d, p))
    slope_mc = fit_slope(ps, pL_mc)
    slope_ex = fit_slope(ps, pL_ex)
    # leading-coefficient check at the smallest p
    lead = pL_ex[0] / (comb(d, N_pred) * ps[0]**N_pred)
    print(f"{d:2d} {N_pred:7d} {slope_mc:9.3f} {slope_ex:12.3f} "
          f"{lead:13.3f}  {ntrials:>10.0e}")
print("(exact slope sits slightly below N over a finite window -- the (1-p)")
print(" factors and subleading binomials; both converge to N as p -> 0.)")

# --- correlated (pair) noise: the exponent follows the EVENT count ----------
print("""
Correlated-noise exhibit (adjacency probe): error EVENTS flip 2 bits each.
Predicted exponent = minimal number of independent EVENTS spanning the
failure = ceil(ceil(d/2)/2) -- the count re-atomizes to the independent
unit; 'physical error count' is no longer the part.  Adjacent pairing vs
RANDOM pairing tests whether the exponent sees spatial layout:""")

def pair_noise_fail(d, q, ntrials, adjacent):
    nslots = d - 1
    fire = rng.random((ntrials, nslots)) < q
    flips = np.zeros((ntrials, d), dtype=np.int64)
    if adjacent:
        for i in range(nslots):
            flips[:, i]     += fire[:, i]
            flips[:, i + 1] += fire[:, i]
    else:
        # each firing slot flips a uniformly random (unordered) pair
        for i in range(nslots):
            a = rng.integers(0, d, ntrials)
            off = rng.integers(1, d, ntrials)
            b = (a + off) % d
            f = fire[:, i]
            np.add.at(flips, (np.nonzero(f)[0], a[f]), 1)
            np.add.at(flips, (np.nonzero(f)[0], b[f]), 1)
    net = flips % 2                                # XOR accumulation
    return np.count_nonzero(net.sum(axis=1) >= (d + 1) // 2) / ntrials

print(f"{'d':>2s} {'N_evt pred':>10s} {'slope adj':>10s} {'slope rand':>11s}")
for d in (3, 5, 7):
    N_evt = -(-((d + 1) // 2) // 2)                # ceil(ceil(d/2)/2)
    qs = np.geomspace(0.01, 0.06, 4)
    sl = {}
    for adj in (True, False):
        pf = [pair_noise_fail(d, q, int(2e6), adj) for q in qs]
        sl[adj] = fit_slope(qs, pf)
    print(f"{d:2d} {N_evt:10d} {sl[True]:10.3f} {sl[False]:11.3f}")
print("Adjacent and random pairing give the SAME exponent: the repetition-code")
print("count is layout-blind -- it renders independence structure (how many")
print("units), not adjacency (where they sit).  Recorded as evidence AGAINST")
print("un-parking adjacency on this witness; the would-carve case is a surface")
print("code where only geometrically ALIGNED pairs chain across the logical cut")
print("(exponent would follow layout at fixed unit count) -- proposable, not in")
print("hand.  Google's observed scaling breaks under correlated events (leakage,")
print("cosmic rays) already show exponent -> effective distance [v Nature 638,920].")


# ===========================================================================
# S3. MULTIPHOTON IONIZATION (third register, pre-registered; coherent)
# ===========================================================================
print("\n" + LINE)
print("S3. MPI: N = ceil(E_ion / hbar omega) photons must be coherently absorbed")
print(LINE)
print("""
Lowest-order perturbation theory (Keldysh gamma >> 1, below saturation):
the N-photon matrix element carries one field amplitude E per absorbed
photon -> |M|^2 ~ E^(2N) ~ I^N.  Coherent register: per-part amplitude
weight sqrt(I), rate-level cost eps = I.  Rate/atom = sigma_N I^N with N
fixed by energy conservation BEFORE any intensity scan -- the data-blind
count is spectroscopic.""")

HBAR_EV_NM = 1239.842
CASES = {  # atom: (IP eV, lambda nm, measured, source)
    "Xe": (12.130, 1064.0, "I^11 law verified (electron yields)",
           "[v] Lompre/L'Huillier et al JOSA B 2,1906(1985); Kruit PRA 28,248(1983)"),
    "Cs": (3.894, 1064.0, "slope ~ 4 (classic 4-photon)",
           "[m] Morellec et al; Mainfray-Manus Rep.Prog.Phys.54,1333(1991)"),
    "He": (24.587, 1064.0, "N=22: LOPT regime barely reachable -- domain edge",
           "[m] review: Mainfray-Manus 1991"),
}
print(f"{'atom':>4s} {'IP(eV)':>7s} {'hw(eV)':>7s} {'IP/hw':>6s} {'N pred':>7s}  measured / source")
for atom, (ip, lam, meas, src) in CASES.items():
    hw = HBAR_EV_NM / lam
    N = int(np.ceil(ip / hw))
    print(f"{atom:>4s} {ip:7.3f} {hw:7.4f} {ip/hw:6.2f} {N:7d}  {meas}")
    print(f"{'':36s}{src}")

# domain edge: Keldysh gamma = sqrt(IP / 2 Up), Up[eV] = 9.33e-14 I[W/cm^2] lam[um]^2
ip, lam_um = 12.130, 1.064
I_gamma1 = ip / 2 / (9.33e-14 * lam_um**2)
print(f"\nDomain edge (Xe, 1064nm): Keldysh gamma = 1 at I ~ {I_gamma1:.1e} W/cm^2;")
print("above it (tunneling) the exponent DIES ENTIRELY -- the law's own scope")
print("condition (independent perturbative parts) fails, in every register the")
print("same way (QEC above threshold, BF below the hard scale).")
print("ATI note: above-threshold peak s scales I^(N+s) in LOPT -- order and")
print("part count still coincide; ATI is not the carve witness.")


# ===========================================================================
# S4. THE LAW, THE TABLE, THE CONTROL
# ===========================================================================
print("\n" + LINE)
print("S4. SUMMARY -- one f, two data-blind inputs per register")
print(LINE)
rows = [
    ("BF pp->pp 90deg",      "eps=Lam^2/s (=|amp|^2/line)", "12 lines cross",
     "s^2 dsig/dt ~ eps^12", "s^-10 (osc.) [v]"),
    ("BF gam p->pi+ n",      "eps=Lam^2/s",                 "9 lines cross",
     "dsig/dt ~ s^-7",       "s^-(7.1+/-0.2) [v]"),
    ("BF gam d->p n",        "eps=Lam^2/s",                 "13 lines cross",
     "dsig/dt ~ s^-11",      "~ s^-11 [m]"),
    ("BF F_pi / F_1^p",      "eps=Lam^2/Q^2 per 2-crossing","n_h = 2 / 3",
     "(Q^2)^-1 / (Q^2)^-2",  "flat Q^2 F_pi; Q^4 F_1 [m]"),
    ("DYW valence x->1",     "(1-x) per spectator (amp)",   "n_s = 2",
     "(1-x)^3  (2n_s-1)",    "(1-x)^(3.0-3.7) [m]"),
    ("QEC rep d=3/5/7",      "eps=p (probability)",         "ceil(d/2)=2/3/4",
     "p^2 / p^3 / p^4",      "MC slopes above"),
    ("QEC surface d=5->7",   "eps=p/p_th",                  "(d+1)/2=3->4",
     "Lambda = 1/eps",       "Lam=2.14+/-0.02 [v]"),
    ("MPI Xe 1064nm",        "eps=I (=|sqrtI|^2/photon)",   "ceil(IP/hw)=11",
     "rate ~ I^11",          "I^11 verified [v]"),
    ("MPI Cs 1064nm",        "eps=I",                       "ceil(IP/hw)=4",
     "rate ~ I^4",           "slope ~4 [m]"),
]
w = (22, 29, 17, 22, 24)
hdr = ("register", "small parameter (rate level)", "part count N",
       "predicted", "measured")
print(" | ".join(h.ljust(x) for h, x in zip(hdr, w)))
print("-+-".join("-" * x for x in w))
for r in rows:
    print(" | ".join(c.ljust(x) for c, x in zip(r, w)))

print("""
NEGATIVE CONTROL (where the law must NOT apply, and why that is principled):
chemical reaction ORDER vs MOLECULARITY.  Measured order equals molecularity
only for a single ELEMENTARY step (bimolecular collision: rate ~ [A][B]);
generic mechanisms (pre-equilibria, chains, catalysis, rate-determining
steps) are SEQUENCES of conversion events, and the observed order becomes a
composite -- fractional, negative, concentration-dependent.  The law's own
hypothesis (all N parts participate in ONE conversion event) fails exactly
there, and the failure is predicted by the counting procedure, not patched
after.  A 'law' that also fit multi-step kinetics would be the smoothness
disease again; refusing it is what makes the exponent bet placeable.
""")
