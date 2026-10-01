"""Referee for workbench/counting-leg: is counting the unfused leg under flow and adjacency,
and is acceleration (frame transport) a count deficit?

Continuum checks (sympy) then a discrete check (2D Poisson sprinkling): recover a writer's proper
acceleration from counts alone -- no metric, no frame, no coordinates handed to the estimator.
"""
import bisect
import numpy as np
import sympy as sp

checks = []
def check(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)

# ---- 1. ordering + number gives the maximal count (geodesic proper time) ----------------------
tau, a = sp.symbols('tau a', positive=True)
# Alexandrov interval volume: 2D tau^2/2, 4D (pi/24) tau^4.  tau is recoverable from the count.
t = sp.symbols('t', positive=True)
V4 = 2*sp.integrate(sp.Rational(4, 3)*sp.pi*(tau/2 - t)**3, (t, 0, tau/2))
check("1. 4D diamond volume = (pi/24) tau^4: the maximal count fixes tau", sp.simplify(V4 - sp.pi*tau**4/24) == 0)

# ---- 2. acceleration is a count deficit ---------------------------------------------------------
# uniform acceleration a, writer's own count tau between two of its events; the ordering-maximal
# count between the same two events is tau_geo (b7 section 5: interval = (4/a^2) sinh^2(a tau/2)).
X0 = lambda s: sp.Matrix([sp.sinh(a*s)/a, sp.cosh(a*s)/a])
d = X0(tau/2) - X0(-tau/2)
interval = sp.simplify(d[0]**2 - d[1]**2)
tau_geo = 2*sp.sinh(a*tau/2)/a
check("2a. maximal count between writer events: tau_geo = (2/a) sinh(a tau/2)  [b7's sinh^2]",
      sp.simplify(interval - tau_geo**2) == 0)
deficit = sp.series(tau_geo - tau, tau, 0, 5).removeO()
check("2b. deficit tau_geo - tau = a^2 tau^3/24 + O(tau^5)", sp.simplify(deficit - a**2*tau**3/24) == 0)
check("2c. tau_geo/tau = sinh(x)/x, x = a tau/2: a is fixed by the two counts alone (monotone)",
      sp.simplify(sp.diff(sp.sinh(sp.Symbol('x'))/sp.Symbol('x'), sp.Symbol('x')).subs(sp.Symbol('x'), 1)) > 0)
# 2d. imaginary period of the map tau -> tau_geo(tau)^2 is 2 pi i / a: b7's Unruh period, as a
# property of the count-deficit function
check("2d. tau_geo(tau + 2 pi i/a)^2 = tau_geo(tau)^2: the Unruh period lives in the deficit map",
      sp.simplify(sp.expand_complex((tau_geo.subs(tau, tau + 2*sp.pi*sp.I/a))**2 - tau_geo**2)) == 0)

# 2e. a non-uniform worldline (circular motion): small-tau deficit still a^2 tau^3 / 24
R_, w_ = sp.Rational(1), sp.Rational(1, 2)          # radius 1, angular speed 1/2 (v = 1/2)
gam = 1/sp.sqrt(1 - (R_*w_)**2)
acc = gam**2*(R_*w_)**2/R_
def pos(s):   # proper time s
    tt = gam*s
    return np.array([float(tt), float(R_*sp.cos(w_*tt)), float(R_*sp.sin(w_*tt))])
ok = True
for s in [0.05, 0.1]:
    p, q = pos(-s/2), pos(s/2)
    dd = q - p
    tg = np.sqrt(dd[0]**2 - dd[1]**2 - dd[2]**2)
    pred = float(acc)**2*s**3/24
    ok &= abs((tg - s)/pred - 1) < 0.02
check("2e. circular motion (non-uniform direction): deficit = a^2 tau^3/24 at small tau", ok)

# ---- 3. the corners are degeneracies of the counting measure --------------------------------------
eta = sp.diag(-1, 1, 1, 1)
k = sp.Matrix([1, 1, 0, 0]); e2 = sp.Matrix([0, 0, 1, 0]); e3 = sp.Matrix([0, 0, 0, 1])
for name, basis, surv in [("null curve (photon)", [k], 0), ("null 2-plane", [k, e2], 1),
                          ("null hypersurface (light-sheet)", [k, e2, e3], 2)]:
    E = sp.Matrix.hstack(*basis)
    q = E.T*eta*E
    check(f"3. {name}: induced measure degenerate in one direction, rank {surv} survives",
          q.det() == 0 and q.rank() == surv)

# ---- 3b. the thermal period is a period of the writer's diamond count -----------------------------
# Writer events tau apart; V(tau) = volume (count) of the causal diamond between them.
H = sp.symbols('H', positive=True)
x_ = sp.symbols('x', positive=True)
V_rindler = tau_geo**2/2                                          # 2D, accelerated writer
V_inertial = tau**2/2                                             # 2D, inertial writer
# 2D de Sitter, geodesic writer at x = 0 in conformal time eta < 0: ds^2 = (-d eta^2 + dx^2)/(H eta)^2
# events at eta1 = -1 and eta2 = -r, r = exp(-H tau); diamond is the conformal (Minkowski) diamond.
eta, rr = sp.symbols('eta r', positive=True)
e1, e2 = -1, -rr
em = (e1 + e2)/2
V_ds = (sp.integrate(2*(eta - e1)/eta**2, (eta, e1, em)) + sp.integrate(2*(e2 - eta)/eta**2, (eta, em, e2)))/H**2
V_ds = sp.simplify(V_ds)
V_ds_tau = V_ds.subs(rr, sp.exp(-H*tau))
per = lambda V, k: sp.simplify(sp.expand_complex(V.subs(tau, tau + 2*sp.pi*sp.I/k) - V)) == 0
check("3b. accelerated writer: V(tau) has imaginary period 2 pi i / a", per(V_rindler, a))
check("3c. de Sitter geodesic writer (no acceleration, no deficit): V(tau) has period 2 pi i / H",
      sp.simplify(V_ds_tau.subs(tau, tau + 2*sp.pi*sp.I/H) - V_ds_tau) == 0)
check("3d. inertial Minkowski writer: V(tau) = tau^2/2 has no imaginary period",
      sp.simplify(V_inertial.subs(tau, tau + 2*sp.pi*sp.I/a) - V_inertial) != 0)
# 3e. circular writer: accelerated (deficit, check 2e) but its diamond count has no imaginary period
Rc, wc = sp.Rational(1), sp.Rational(1, 2)
gc = 1/sp.sqrt(1 - (Rc*wc)**2)
ac = gc**2*(Rc*wc)**2/Rc
sig_c = gc**2*tau**2 - 4*Rc**2*sp.sin(gc*wc*tau/2)**2          # interval between writer events
no_period = True
for P in [2*sp.pi/ac, sp.pi/ac, 4*sp.pi/ac, 2*sp.pi/(gc*wc)]:
    diff = [complex(sp.N((sig_c.subs(tau, tt + sp.I*P) - sig_c.subs(tau, tt)))) for tt in (0.3, 1.7)]
    no_period &= max(abs(d_) for d_ in diff) > 1e-6
check("3e. circular writer: accelerated, yet V(tau) has no imaginary period (non-thermal, Bell-Leinaas)",
      no_period)
print("     de Sitter diamond count V(r) =", V_ds, "  (depends on tau only through exp(-H tau))")

# ---- 4. discrete: recover a from counts alone (2D sprinkling) -------------------------------------
# The writer is a sequence of its own events x_0 .. x_n on its worldline. The estimator sees only
# the causal order and counts: the longest chain between consecutive writer events (segments) and
# between the end events (the maximal count). Counts -> durations via the counting density rho
# (number is the primitive) and the known longest-chain law E[L] = 2 sqrt(N) - 1.7711 N^(1/6)
# (Vershik-Kerov / Baik-Deift-Johansson), N = rho * tau^2 / 2.
rng = np.random.default_rng(7)

def lis(u, v):
    """longest chain = longest increasing subsequence in both light-cone coordinates."""
    order = np.argsort(u)
    tails = []
    for val in v[order]:
        i = bisect.bisect_left(tails, val)
        if i == len(tails):
            tails.append(val)
        else:
            tails[i] = val
    return len(tails)

def tau_of_count(L, rho):
    lo, hi = 1.0, 1e9                    # invert E[L](N), then tau = sqrt(2N/rho)
    for _ in range(200):
        mid = 0.5*(lo + hi)
        if 2*np.sqrt(mid) - 1.7711*mid**(1/6) < L: lo = mid
        else: hi = mid
    return np.sqrt(2*lo/rho)

def chain_between(U, V, p, q):
    up, vp = p[0] - p[1], p[0] + p[1]
    uq, vq = q[0] - q[1], q[0] + q[1]
    m = (U > up) & (U < uq) & (V > vp) & (V < vq)
    return lis(U[m], V[m])

A_TRUE, TAU, RHO, NSEG, RUNS = 1.0, 2.0, 40000.0, 4, 24
writer = [(np.sinh(A_TRUE*s)/A_TRUE, np.cosh(A_TRUE*s)/A_TRUE)
          for s in np.linspace(-TAU/2, TAU/2, NSEG + 1)]
th = writer[-1][0]
est, segs, tots = [], [], []
for _ in range(RUNS):
    n = rng.poisson(RHO*(2*th + 0.2)*(2*th + 0.2))
    T = rng.uniform(-th - 0.1, th + 0.1, n)
    X = rng.uniform(writer[0][1] - th - 0.1, writer[0][1] + th + 0.1, n)
    U, V = T - X, T + X
    G = tau_of_count(chain_between(U, V, writer[0], writer[-1]), RHO)
    s_ = np.mean([tau_of_count(chain_between(U, V, writer[i], writer[i + 1]), RHO) for i in range(NSEG)])
    # unknowns (a, tau): s_ = (2/a) sinh(a tau/(2n)),  G = (2/a) sinh(a tau / 2)
    #   => G = (2/a) sinh(n asinh(a s_/2)); solve for a by bisection
    f = lambda aa: (2/aa)*np.sinh(NSEG*np.arcsinh(aa*s_/2)) - G
    lo, hi = 1e-4, 5.0
    for _ in range(100):
        mid = 0.5*(lo + hi)
        if f(mid) < 0: lo = mid
        else: hi = mid
    est.append(lo); segs.append(s_); tots.append(G)
est = np.array(est)
print(f"   maximal count -> {np.mean(tots):.3f} (true {2*np.sinh(A_TRUE*TAU/2)/A_TRUE:.3f});  "
      f"segment count -> {np.mean(segs):.3f} (true {2*np.sinh(A_TRUE*TAU/(2*NSEG))/A_TRUE:.3f})")
print(f"   a from counts = {est.mean():.3f} +/- {est.std(ddof=1)/np.sqrt(RUNS):.3f}   (a_true = {A_TRUE})")
check("4. discrete: the writer's proper acceleration is recovered from order + counts alone (10%)",
      abs(est.mean() - A_TRUE) < 0.1)

print()
print(f"{sum(o for _, o in checks)}/{len(checks)} checks passed")
