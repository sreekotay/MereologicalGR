"""Compare, on one causal set, the writer's temperature read two ways:
  count side : a from the writer's interval counts V(tau)  (order + number only)
  field side : a from the SJ two-point function along the writer (order only -> state)
and diagnose what the SJ field tracks (local count, longest chain, or continuum interval)."""
import sys, bisect, numpy as np
from scipy.optimize import curve_fit
d = np.load(sys.argv[1])
W, U, V, C, th, a, N = d["W"], d["U"], d["V"], d["C"], d["th"], float(d["a"]), int(d["N"])
n = len(U); nw = len(th); rho = N/2.0
Cf = C.astype(np.float32)
cnt = Cf[:, :N] @ Cf[:N, :]
idx = np.arange(N, n)
dt, Vw, Ww, sw = [], [], [], []
for i in range(nw):
    for j in range(i):
        dt.append((th[i] - th[j])/a); Vw.append(cnt[idx[i], idx[j]]); Ww.append(W[idx[i], idx[j]].real)
        sw.append((4/a**2)*np.sinh((th[i]-th[j])/2)**2)
dt, Vw, Ww, sw = map(np.array, (dt, Vw, Ww, sw))
m = Vw >= 2
fc = lambda tau, aa, c: c + 2*np.log(np.sinh(aa*tau/2))
ff = lambda tau, aa, al, c: c + al*2*np.log(np.sinh(aa*tau/2))
pc, cc = curve_fit(fc, dt[m], np.log(Vw[m]), p0=[a/2, 3])
# Poisson maximum likelihood with the density known (number is the primitive): mu = rho*(2/a^2) sinh^2(a tau/2)
from scipy.optimize import minimize_scalar
def nll(aa, sel):
    mu = rho*(2/aa**2)*np.sinh(aa*dt[sel]/2)**2
    return np.sum(mu - Vw[sel]*np.log(mu))
mall = Vw >= 0
a_ml = minimize_scalar(lambda aa: nll(aa, mall), bounds=(0.1, 60), method='bounded').x
# bootstrap over writer ticks for an error bar
rngb = np.random.default_rng(9); boots = []
ti = np.array([(i, j) for i in range(nw) for j in range(i)])
for _ in range(200):
    keep = np.zeros(nw, bool); keep[rngb.choice(nw, nw, replace=True)] = True
    sel = keep[ti[:, 0]] & keep[ti[:, 1]]
    boots.append(minimize_scalar(lambda aa: nll(aa, sel), bounds=(0.1, 60), method='bounded').x)
a_ml_err = np.std(boots)
pf, cf = curve_fit(ff, dt[m], Ww[m], p0=[a/2, -0.08, 0.3])
pm, _ = curve_fit(ff, dt[m], -np.log(sw[m])/(4*np.pi), p0=[a/2, -0.08, 0.3])
res = Ww[m] - (-(1/(4*np.pi))*np.log(sw[m]))
k = np.polyfit(dt[m], res, 1)
print(f"{sys.argv[1].split('/')[-1]}: writer pairs {m.sum()}")
print(f"  a_count (Poisson ML, rho known) = {a_ml:.3f} +/- {a_ml_err:.3f};  [naive log-fit {pc[0]:.3f}: biased at small V, not used]")
print(f"  a_field(SJ) = {pf[0]:.3f} +/- {np.sqrt(cf[0,0]):.3f}"
      f" (alpha {pf[1]:+.4f})   a_minkowski = {pm[0]:.3f}   true {a}")
print(f"  SJ - Minkowski along writer: drift {k[0]:+.4f} per unit tau (mean {res.mean():+.4f})")
# bulk diagnostic in the writer's region
rng = np.random.default_rng(5)
reg = np.where((np.abs(U[:N]) < 0.35) & (np.abs(V[:N]) < 0.35))[0]
def lis(x, y):
    o = np.argsort(x); t = []
    for val in y[o]:
        i = bisect.bisect_left(t, val)
        if i == len(t): t.append(val)
        else: t[i] = val
    return len(t)
P = []
while len(P) < 4000:
    p, q = rng.choice(reg, 2)
    if C[p, q] and cnt[p, q] >= 3: P.append((p, q))
P = np.array(P); p, q = P[:, 0], P[:, 1]
Wb = W[p, q].real; lnV = np.log(cnt[p, q]); lnS = np.log(rho*(U[p]-U[q])*(V[p]-V[q])/2)
L = np.array([lis(U[np.where(C[pp, :N] & C[:N, qq])[0]], V[np.where(C[pp, :N] & C[:N, qq])[0]]) + 1 for pp, qq in zip(p, q)], float)
lnL = np.log(L**2/2)
def fit(cols):
    X = np.vstack(cols + [np.ones(len(Wb))]).T
    c = np.linalg.lstsq(X, Wb, rcond=None)[0]; return c, (Wb - X @ c).std()
for nm, col in [("ln V (local count)", lnV), ("ln L^2 (longest chain)", lnL), ("ln sigma (continuum)", lnS)]:
    c, r = fit([col]); print(f"  bulk Re W vs {nm:24s}: slope {c[0]:+.4f}  rms {r:.4f}")
c, r = fit([lnV, lnS]); print(f"  joint: ln V {c[0]:+.4f}, ln sigma {c[1]:+.4f}  (field tracks {'counts' if abs(c[0])>abs(c[1]) else 'the smoother interval'})")

import json, os
row = dict(file=os.path.basename(sys.argv[1]), a=a, a_count=a_ml, a_count_err=a_ml_err, a_field=pf[0],
           a_field_err=float(np.sqrt(cf[0, 0])), alpha=pf[1], joint_lnV=c[0], joint_lnsigma=c[1])
with open(sys.argv[2] if len(sys.argv) > 2 else os.devnull, "a") as fh:
    fh.write(json.dumps({k: (float(v) if not isinstance(v, str) else v) for k, v in row.items()}) + "\n")
