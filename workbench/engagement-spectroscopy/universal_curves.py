"""
Universal spectral-distortion functions for the adiabatic UdW detector.

From adiabatic_udw.py (symbolic):
  I(s) = I0(s) [1 + eta h_eta(x) + xi^2 h_xi2(x)],  x = a s,
     h_eta  = (x + x^3/24) coth(x/2) - x^2/4 - 2          [coeff of eta=addot/a^3]
     h_xi2  = x^2/4 + 5 - 2x coth(x/2) - (x^2/4)/sinh^2(x/2)   [coeff of xi^2=(adot/a^2)^2]
  and the O(adot) term vanishes identically (midpoint prescription).

Response:  F(omega,tau) = F0(omega; a(tau)) [1 + eta G_eta(w) + xi^2 G_xi2(w)],
  w = omega/a,  F0 = (a/2pi) P(w),  P(w) = w/(e^{2 pi w}-1).

Analytic reduction (FT table, a=1 units, s -> s - i eps):
  S = 1/sinh^2(x/2):        FT[S] = J(w) = -8 pi P(w)
  coth(x/2) S = -S':        FT = -i w J
  FT[S^2] = -(2/3)(w^2+1) J
  FT[x^n f] = (i d/dw)^n FT[f]
Result:
  G_eta(w)  = -[ w P' - P + P''/8 - (w/24) P''' ] / P
  G_xi2(w)  =  [ (8/3) P - (8/3) w P' - ((2 w^2+5)/12) P'' ] / P
This script verifies these against direct numerical FT of the kernels.
"""
import numpy as np
import sympy as sp

# ---------- analytic G's ----------
w_ = sp.symbols('w', real=True)
P_ = w_/(sp.exp(2*sp.pi*w_) - 1)
dP = [P_] + [sp.diff(P_, w_, k) for k in (1, 2, 3)]
G_eta_sym = -(w_*dP[1] - dP[0] + dP[2]/8 - w_*dP[3]/24)/dP[0]
# note: G = FT[K]/(8 pi P) and J = -8 pi P, so G = -FT[K]/J  (sign!)
G_xi2_sym = -(sp.Rational(8,3)*dP[0] - sp.Rational(8,3)*w_*dP[1]
              - (2*w_**2 + 5)/12*dP[2])/dP[0]
G_eta_f = sp.lambdify(w_, sp.simplify(G_eta_sym), 'numpy')
G_xi2_f = sp.lambdify(w_, sp.simplify(G_xi2_sym), 'numpy')

# limits
print("w->0 limits:", sp.limit(G_eta_sym, w_, 0), sp.limit(G_xi2_sym, w_, 0))
print("w->0+ series G_eta:", sp.series(sp.simplify(G_eta_sym), w_, 0, 2))
print("w->0+ series G_xi2:", sp.series(sp.simplify(G_xi2_sym), w_, 0, 2))

# ---------- numeric check via direct FT ----------
def coth(z): return 1.0/np.tanh(z)
def h_eta(x):  return (x + x**3/24)*coth(x/2) - x**2/4 - 2
def h_xi2(x):  return x**2/4 + 5 - 2*x*coth(x/2) - (x**2/4)/np.sinh(x/2)**2
def K_eta(x):  return h_eta(x)/np.sinh(x/2)**2
def K_xi2(x):  return h_xi2(x)/np.sinh(x/2)**2

xs = np.linspace(1e-6, 80.0, 800001)
Ke, Kx2 = K_eta(xs), K_xi2(xs)

def G_num(Kv, w):
    ft = 2.0*np.trapezoid(np.cos(w*xs)*Kv, xs)        # even kernel
    return ft*np.expm1(2*np.pi*w)/(8*np.pi*w)

print("\n   w        G_eta(anl)    G_eta(num)    G_xi2(anl)    G_xi2(num)")
for w in [0.1, 0.25, 0.5, 1.0, 2.0, 4.0, -0.5, -1.0, -2.0]:
    print(f" {w:6.2f}  {G_eta_f(w):12.6f} {G_num(Ke,w):12.6f}"
          f"  {G_xi2_f(w):12.6f} {G_num(Kx2,w):12.6f}")

# ---------- running detailed-balance temperature ----------
# F(-w)/F(w) = e^{2 pi w} [1 + eta dGe + xi^2 dGx],  dG = G(-w)-G(w)
# T_eff(w)/T_U = 2 pi w / ln ratio ~= 1 - [eta dGe + xi^2 dGx]/(2 pi w)
print("\n   w      tau_eta(w)      tau_xi2(w)    [T_eff/T_U = 1 + eta*tau_eta + xi^2*tau_xi2]")
tau_eta, tau_xi2 = [], []
wgrid = np.array([0.05,0.1,0.2,0.3,0.5,0.75,1.0,1.25,1.5,2.0,2.5,3.0,4.0,5.0])
for w in wgrid:
    te = -(G_eta_f(-w) - G_eta_f(w))/(2*np.pi*w)
    tx = -(G_xi2_f(-w) - G_xi2_f(w))/(2*np.pi*w)
    tau_eta.append(te); tau_xi2.append(tx)
    print(f" {w:5.2f}  {te:14.8f}  {tx:14.8f}")

# w->0 limit of tau's (temperature reading of a broadband/low-gap detector)
te0 = sp.limit(-( G_eta_sym.subs(w_,-w_) - G_eta_sym )/(2*sp.pi*w_), w_, 0)
tx0 = sp.limit(-( G_xi2_sym.subs(w_,-w_) - G_xi2_sym )/(2*sp.pi*w_), w_, 0)
print("\n w->0 limits of tau_eta, tau_xi2:", sp.nsimplify(sp.simplify(te0)), ",",
      sp.nsimplify(sp.simplify(tx0)), "=", float(te0), float(tx0))

# large-w behaviour
print("\n large-w: G_eta ~", sp.limit(G_eta_sym/w_, w_, sp.oo), "* w ;",
      "G_xi2 ~", sp.limit(G_xi2_sym/w_**2, w_, sp.oo), "* w^2")
te_inf = sp.limit(-( G_eta_sym.subs(w_,-w_) - G_eta_sym )/(2*sp.pi*w_), w_, sp.oo)
tx_inf = sp.limit(-( G_xi2_sym.subs(w_,-w_) - G_xi2_sym )/(2*sp.pi*w_), w_, sp.oo)
print(" tau_eta(inf) =", sp.simplify(te_inf), " tau_xi2(inf) =", sp.simplify(tx_inf))
