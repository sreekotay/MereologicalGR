import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import pearsonr

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(0)

def r2(y, yhat):
    ss_res = np.sum((y - yhat)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    return 1 - ss_res/ss_tot

def aic(y, yhat, k):
    n = len(y); rss = np.sum((y-yhat)**2)
    return n*np.log(rss/n) + 2*k

def rmse(y, yhat): return np.sqrt(np.mean((y-yhat)**2))

# residual-structure test: runs of same-sign residuals (Wald-Wolfowitz-ish)
def sign_runs(resid):
    s = np.sign(resid); s = s[s!=0]
    runs = 1 + np.sum(s[1:]!=s[:-1])
    return runs, len(s)

print("="*70)
print("REGISTER A - QCD fragmentation D_h(z)  [DSS-class: N z^a (1-z)^b]")
print("="*70)
# DSS (de Florian-Sassot-Stratmann PRD75 114010) pi+ favored, representative
# exponents. Shape only (N absorbs normalization / sum-rule).
zA = np.linspace(0.05, 0.95, 40)
aA, bA = -0.60, 1.55          # soft-gluon rise, large-z falloff
DA = zA**aA * (1-zA)**bA
DA = DA/np.max(DA)            # normalize peak to 1 for shape comparison
print(f"  natural form: z^{aA} (1-z)^{bA}  (this IS the beta family)")

print("="*70)
print("REGISTER B - Entanglement distillation, hashing bound E_D(F)")
print("="*70)
# Bennett et al PRA54 3824: Werner/Bell-diagonal fidelity F, other 3 comps (1-F)/3
# E_D >= 1 - H2diag ; distillable for F>0.8107
def hashing(F):
    p = np.array([F, (1-F)/3, (1-F)/3, (1-F)/3])
    p = np.clip(p, 1e-12, 1)
    H = -np.sum(p*np.log2(p))
    return 1 - H
Fgrid = np.linspace(0.8108, 0.999, 40)
EB = np.array([hashing(f) for f in Fgrid])
EB = np.clip(EB, 0, None)
print(f"  natural form: 1 - H(Bell-diag(F));  E_D>0 for F>0.8107 -> 1 at F=1")

print("="*70)
print("REGISTER C - QEC logical suppression below threshold")
print("="*70)
# Threshold theorem / surface code (Fowler et al PRA86 032324):
#   p_L = A (p/p_th)^((d+1)/2)
d = 5; expo = (d+1)/2            # = 3
p_th = 1.0                        # work in units of p_th
Acoef = 0.5
pgrid = np.linspace(0.02, 0.98, 40)   # p/p_th in (0,1)
pL = Acoef*(pgrid/p_th)**expo
effC = 1 - pL                     # "commit efficiency" = logical fidelity proxy
print(f"  natural form: p_L = {Acoef} (p/p_th)^{expo:.0f};  eff = 1 - p_L")

# ---------------------------------------------------------------------------
print("\n" + "#"*70)
print("# COMMON INTERFACE-QUALITY COORDINATE x in [0,1]")
print("#"*70)
# A: x = z (momentum fraction already in [0,1]); observable = density D (single-humped)
xA, yA = zA, DA
# B: normalize fidelity above distillability onset. x=0 at onset, x=1 at pure.
xB, yB = (Fgrid-0.8107)/(1-0.8107), EB
# C: quality = distance below threshold. x=1 at p=0 (perfect), x=0 at threshold.
xC, yC = 1 - pgrid/p_th, effC
print("  A: x=z,           y=D(z)      (probability DENSITY, single-humped)")
print("  B: x=(F-F0)/(1-F0), y=E_D     (efficiency, monotone rising to 1)")
print("  C: x=1-p/p_th,    y=1-p_L     (efficiency, monotone rising to 1)")

# ---------------------------------------------------------------------------
# CANDIDATE SHARED FAMILIES
def beta_like(x, N, a, b):        # 3-param beta / Dirichlet kernel
    x = np.clip(x, 1e-9, 1-1e-9)
    return N * x**a * (1-x)**b
def onemin_pow(x, A, c):          # 2-param threshold/saturation: 1 - A(1-x)^c
    return 1 - A*np.clip(1-x,0,1)**c
def exp_sat(x, A, k):             # 2-param exponential saturation
    return A*(1-np.exp(-k*x))

datasets = {"A_frag":(xA,yA), "B_distill":(xB,yB), "C_qec":(xC,yC)}

def fit_report(name, x, y, f, p0, k, label, bounds=(-np.inf,np.inf)):
    try:
        popt,_ = curve_fit(f, x, y, p0=p0, maxfev=200000, bounds=bounds)
        yhat = f(x,*popt)
        resid = y-yhat
        runs, ns = sign_runs(resid)
        # expected runs under randomness ~ (ns+1)/2 ; few runs => structured misfit
        print(f"  [{label:11s} -> {name:9s}] params={np.round(popt,3)} "
              f"R2={r2(y,yhat):.4f} RMSE={rmse(y,yhat):.4f} "
              f"AIC={aic(y,yhat,k):7.1f} runs={runs}/{ns} (rand~{(ns+1)//2})")
        return r2(y,yhat), rmse(y,yhat)
    except Exception as e:
        print(f"  [{label:11s} -> {name:9s}] FIT FAILED: {e}")
        return np.nan, np.nan

print("\n" + "="*70)
print("FIT 1: beta-like N x^a (1-x)^b  to each register (3 params)")
print("="*70)
for nm,(x,y) in datasets.items():
    fit_report(nm, x, y, beta_like, [1,0.5,0.5], 3, "beta")

print("\n" + "="*70)
print("FIT 2: 1 - A(1-x)^c  (2 params)  -- 'threshold/saturation' family")
print("="*70)
for nm,(x,y) in datasets.items():
    fit_report(nm, x, y, onemin_pow, [0.5,2], 2, "1-A(1-x)^c",
               bounds=([0,0.1],[5,10]))

print("\n" + "="*70)
print("FIT 3: A(1-exp(-k x))  (2 params) -- exponential saturation")
print("="*70)
for nm,(x,y) in datasets.items():
    fit_report(nm, x, y, exp_sat, [1,3], 2, "exp-sat", bounds=([0,0],[5,50]))

# ---------------------------------------------------------------------------
print("\n" + "#"*70)
print("# NULL TEST: each family forced onto the OTHERS' native shape")
print("#"*70)
print("Key: does the beta family (native to A) actually REPRODUCE B & C, or")
print("just interpolate smoothly? Compare to the native power-law for C.\n")

# C is a pure power law in (1-x): the TRUTH is 1 - 0.5(1-x)^3, so 1-A(1-x)^c
# should recover it exactly (c->3). beta should merely approximate.
print("REGISTER C truth = 1 - 0.5(1-x)^3  (exact power law):")
fit_report("C_qec", xC, yC, onemin_pow, [0.5,2], 2, "native form",
           bounds=([0,0.1],[5,10]))
fit_report("C_qec", xC, yC, beta_like, [1,0.5,0.5], 3, "beta(alien)")

print("\nREGISTER B truth = 1 - H(F)  (entropy form, NOT algebraically beta):")
fit_report("B_distill", xB, yB, beta_like, [1,0.5,0.5], 3, "beta(alien)")
fit_report("B_distill", xB, yB, onemin_pow, [0.5,2], 2, "1-A(1-x)^c")

print("\nREGISTER A truth = z^a(1-z)^b DENSITY (single-humped, not monotone):")
fit_report("A_frag", xA, yA, beta_like, [1,0.5,0.5], 3, "native beta")
fit_report("A_frag", xA, yA, onemin_pow, [0.5,2], 2, "1-A(1-x)^c")
fit_report("A_frag", xA, yA, exp_sat, [1,3], 2, "exp-sat")

# ---------------------------------------------------------------------------
print("\n" + "#"*70)
print("# LOOK-ELSEWHERE / POWER CHECK: can beta fit RANDOM smooth monotone curves?")
print("#"*70)
# generate random smooth monotone [0,1] curves and fit beta -> if it always wins,
# a good fit carries ~zero evidential weight.
good = 0; N=300
for _ in range(N):
    ctrl = np.sort(rng.uniform(0,1,5)); ctrl[0]=0; ctrl[-1]=1
    xs = np.linspace(0,1,40)
    ys = np.interp(xs, np.linspace(0,1,5), np.cumsum(np.abs(np.diff(np.concatenate([[0],ctrl])))))
    ys = (ys-ys.min())/(ys.max()-ys.min()+1e-9)
    try:
        popt,_=curve_fit(beta_like, xs, ys, p0=[1,0.5,0.5], maxfev=20000)
        if r2(ys, beta_like(xs,*popt))>0.99: good+=1
    except Exception: pass
print(f"  beta family achieves R2>0.99 on {good}/{N} RANDOM smooth monotone curves")
print("  -> a high-R2 'shared-form' fit is expected by construction (underpowered).")
