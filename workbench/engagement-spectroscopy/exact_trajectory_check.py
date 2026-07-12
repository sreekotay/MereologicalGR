"""
Validation of the adiabatic expansion against EXACT (non-expanded) trajectories.

Trajectory A (constant xi):  a(tau) = a0/(1 - xi a0 tau)
   => adot/a^2 = xi (const), addot/a^3 = 2 xi^2  => eta = 2 xi^2 at tau=0.
   rapidity theta = -(1/xi) ln r,  r = 1 - xi a0 tau ; t(tau), x(tau) closed form.

Trajectory B (pure eta):     a(tau) = a0 (1 + (eta/2)(a0 tau)^2)
   => at tau=0: adot=0, addot = eta a0^3. theta = a0 tau + eta a0^3 tau^3/6.

For each: I(s) = Dt^2 - Dx^2 with midpoint at tau=0;
 dW(s) = -(1/4pi^2)(1/I - 1/I0) is regular & even; dF = 2 int_0^inf cos(w s) dW ds.
Compare dF/F0 with prediction  eta G_eta(w) + xi^2 G_xi2(w).
Units a0 = 1.
"""
import numpy as np
import sympy as sp

# analytic universal functions
w_ = sp.symbols('w', real=True)
P_ = w_/(sp.exp(2*sp.pi*w_) - 1)
dP = [P_] + [sp.diff(P_, w_, k) for k in (1, 2, 3)]
G_eta_f = sp.lambdify(w_, sp.simplify(-(w_*dP[1] - dP[0] + dP[2]/8 - w_*dP[3]/24)/dP[0]), 'numpy')
G_xi2_f = sp.lambdify(w_, sp.simplify(-(sp.Rational(8,3)*dP[0] - sp.Rational(8,3)*w_*dP[1]
              - (2*w_**2+5)/12*dP[2])/dP[0]), 'numpy')

def I0(s):  # constant a0=1
    return 4.0*np.sinh(s/2.0)**2

# ---- trajectory A: constant xi ----
def I_constxi(s, xi):
    tp, tm = s/2.0, -s/2.0
    def tx(tau):
        r = 1.0 - xi*tau
        p1, p2 = 1.0 - 1.0/xi, 1.0 + 1.0/xi
        A = (r**p1 - 1.0)/p1
        B = (r**p2 - 1.0)/p2
        t = -(A + B)/(2*xi)
        x = -(A - B)/(2*xi)
        return t, x
    t1, x1 = tx(tp); t2, x2 = tx(tm)
    return (t1-t2)**2 - (x1-x2)**2

# ---- trajectory B: pure eta ----
def I_pureeta(s, eta):
    # theta(tau) = tau + eta tau^3/6 ; integrate cosh/sinh theta on fine grid
    n = 20001
    tau = np.linspace(-s/2.0, s/2.0, n)
    th = tau + eta*tau**3/6.0
    ch, sh = np.cosh(th), np.sinh(th)
    Dt = np.trapezoid(ch, tau)
    Dx = np.trapezoid(sh, tau)
    return Dt**2 - Dx**2

def dF_over_F0(Ifun, par, wlist, smax):
    ns = 40000
    ss = np.linspace(1e-4, smax, ns)
    Ivals = np.array([Ifun(s, par) for s in ss])
    dW = -(1.0/(4*np.pi**2))*(1.0/Ivals - 1.0/I0(ss))
    out = []
    for w in wlist:
        dF = 2.0*np.trapezoid(np.cos(w*ss)*dW, ss)
        F0 = (1.0/(2*np.pi))*w/np.expm1(2*np.pi*w)
        out.append(dF/F0)
    return np.array(out)

wlist = [0.25, 0.5, 1.0, 2.0]

print("=== Trajectory A (constant xi; eta = 2 xi^2) ===")
print("  xi      w     dF/F0 (exact)   pred = (2 G_eta + G_xi2) xi^2      ratio")
for xi in [0.02, 0.04, 0.08]:
    smax = min(60.0, 1.8/xi*0.9)  # stay inside r>0 for both branch ends
    res = dF_over_F0(I_constxi, xi, wlist, smax)
    for w, r in zip(wlist, res):
        pred = (2*G_eta_f(w) + G_xi2_f(w))*xi**2
        print(f"  {xi:5.3f} {w:6.2f}  {r:14.6e}  {pred:14.6e}  {r/pred:10.4f}")

print("\n=== Trajectory B (pure eta at tau=0) ===")
print("  eta     w     dF/F0 (exact)      pred = G_eta * eta         ratio")
for eta in [0.005, 0.01, 0.02]:
    res = dF_over_F0(I_pureeta, eta, wlist, 50.0)
    for w, r in zip(wlist, res):
        pred = G_eta_f(w)*eta
        print(f"  {eta:5.3f} {w:6.2f}  {r:14.6e}  {pred:14.6e}  {r/pred:10.4f}")
