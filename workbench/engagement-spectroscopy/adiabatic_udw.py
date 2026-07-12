"""
Adiabatic expansion of the Unruh-DeWitt response for slowly varying proper
acceleration a(tau).

Setup (3+1 Minkowski, massless scalar, monopole UdW detector, first order PT):
  Worldline in the t-x plane, rapidity theta(tau), theta'(tau) = a(tau).
  Invariant interval between tau+s/2 and tau-s/2 (midpoint prescription):
     I(s) = Dt^2 - Dx^2 = int_{-s/2}^{s/2} dsig1 int_{-s/2}^{s/2} dsig2
                          cosh( theta(sig1) - theta(sig2) )
  (exact identity, since Dt = int cosh theta, Dx = int sinh theta).

  Expand theta(sig) = a sig + (adot/2) sig^2 + (addot/6) sig^3 about midpoint.
  Wightman: W(s) = -1/(4 pi^2) 1/I(s - i eps)   [only s=0 pole matters on R]
  Response rate density: F(omega, tau) = int ds e^{-i omega s} W.

  Dimensionless adiabatic parameters:
     xi  = adot / a^2 ,   eta = addot / a^3 ,  x = a s.

Outputs: h_eta(x), h_xi2(x) with  I = I0 [ 1 + eta h_eta + xi^2 h_xi2 + O(3rd) ]
         (the O(xi) term is shown to vanish identically),
         then universal spectral correction functions
         F = F0(omega;a) [ 1 + eta G_eta(w) + xi^2 G_xi2(w) ],  w = omega/a,
         and the running detailed-balance temperature deviation.
"""
import sympy as sp
import numpy as np

# ---------------- symbolic part ----------------
s, a = sp.symbols('s a', positive=True)
s1, s2 = sp.symbols('s1 s2', real=True)
x = sp.symbols('x', positive=True)

u = a*(s1 - s2)

def dbl(f):
    return sp.integrate(sp.integrate(f, (s1, -s/2, s/2)), (s2, -s/2, s/2))

I00 = sp.simplify(dbl(sp.cosh(u)))
I10 = sp.simplify(dbl(sp.sinh(u)*(s1**2 - s2**2)/2))                # coeff of adot
I01 = sp.simplify(dbl(sp.sinh(u)*(s1**3 - s2**3)/6))                # coeff of addot
I20 = sp.simplify(dbl(sp.cosh(u)*((s1**2 - s2**2)/2)**2/2))         # coeff of adot^2

print("I00 =", sp.simplify(I00 - 4*sp.sinh(a*s/2)**2/a**2), "(should be 0 vs 4 sinh^2(as/2)/a^2)")
print("I10 =", I10, "   <-- first order in adot (expect 0)")

h_eta = sp.simplify((a**3 * I01 / I00).rewrite(sp.exp).simplify())
h_xi2 = sp.simplify((a**4 * I20 / I00).rewrite(sp.exp).simplify())
h_eta_x = sp.simplify(h_eta.subs(s, x/a))
h_xi2_x = sp.simplify(h_xi2.subs(s, x/a))
print("\nh_eta(x)  =", sp.simplify(sp.trigsimp(h_eta_x)))
print("h_xi2(x) =", sp.simplify(sp.trigsimp(h_xi2_x)))

# small-x behaviour (regularity of kernels at s=0)
print("\nsmall-x: h_eta ->", sp.series(h_eta_x, x, 0, 7))
print("small-x: h_xi2 ->", sp.series(h_xi2_x, x, 0, 7))

# kernels for the response correction:
#   dW/W0 = -(eta h_eta + xi^2 h_xi2)   since W ~ 1/I
#   dF(omega) = - int ds e^{-i w s} W0(s) [eta h_eta + xi^2 h_xi2]
#   W0(s) = -a^2/(16 pi^2 sinh^2(as/2));  F0 = (1/2pi) omega/(e^{2pi omega/a}-1)
# universal:  G_i(w) = dF_i/F0 = [a^2/(16 pi^2 F0)] * FT[ h_i / sinh^2(x/2) ]
K_eta = sp.simplify(h_eta_x / sp.sinh(x/2)**2)
K_xi2 = sp.simplify(h_xi2_x / sp.sinh(x/2)**2)
print("\nK_eta small-x:", sp.series(K_eta, x, 0, 5))
print("K_xi2 small-x:", sp.series(K_xi2, x, 0, 5))
print("\nParity checks (K(-x) - K(x), expect 0):")
print(" ", sp.simplify(K_eta.subs(x, -x) - K_eta))
print(" ", sp.simplify(K_xi2.subs(x, -x) - K_xi2))

# lambdify kernels for numerics (guard x=0 by series value)
Ke = sp.lambdify(x, K_eta, 'numpy')
Kx = sp.lambdify(x, K_xi2, 'numpy')

# ---------------- numeric universal curves ----------------
# G_i(w) = FT[K_i](w) / ( 8*pi*  w/(e^{2 pi w}-1) ) * (-1) ... derive signs:
# dF = -(1/(4 pi^2)) * d(1/I) ... careful:
#   W = -1/(4 pi^2 I);  I = I0(1+c) => W = W0 (1 - c + ...),  c = eta h_eta + xi^2 h_xi2
#   dW = -W0 c = + a^2/(16 pi^2) * K_i(x) * (eta or xi^2)   with K_i = h_i/sinh^2
#   dF_i(omega) = a^2/(16 pi^2) * int ds e^{-i omega s} K_i(a s)
#              = a/(16 pi^2) * FTK_i(w),   FTK(w) = int dx e^{-i w x} K(x)  (w=omega/a)
#   F0 = (a/2pi) * w/(e^{2 pi w} - 1)
#   G_i(w) = dF_i/F0 = FTK_i(w) * (e^{2 pi w}-1) / (8 pi w)
def FTK(K, w, xmax=60.0, n=400001):
    xs = np.linspace(1e-6, xmax, n)
    vals = K(xs)
    # even kernel: FT = 2 int_0^inf cos(w x) K dx
    return 2.0*np.trapezoid(np.cos(w*xs)*vals, xs)

def G(K, w):
    return FTK(K, w) * (np.expm1(2*np.pi*w)) / (8*np.pi*w)

ws = np.array([0.05,0.1,0.2,0.3,0.5,0.75,1.0,1.5,2.0,3.0,4.0,5.0])
print("\n  w=omega/a    G_eta(w)      G_xi2(w)      G_eta(-w)     G_xi2(-w)")
rows = []
for w in ws:
    ge, gx = G(Ke, w), G(Kx, w)
    gem, gxm = G(Ke, -w), G(Kx, -w)
    rows.append((w, ge, gx, gem, gxm))
    print(f"  {w:7.3f}  {ge:12.6f}  {gx:12.6f}  {gem:12.6f}  {gxm:12.6f}")

# running detailed-balance temperature:
#   F(-w)/F(w) = e^{2 pi w} [1 + eta (G_eta(-w)-G_eta(w)) + xi^2 (...)]
#   T_eff(w)/T_U = 1 + (1/(2 pi w)) [ eta DG_eta + xi^2 DG_xi2 ]  (sign: T = w a/ln ratio)
print("\n  w    dT/T coefficient of eta      of xi^2   [T_eff/T_U = 1 - coeff*param]")
for (w, ge, gx, gem, gxm) in rows:
    ce = (gem - ge)/(2*np.pi*w)
    cx = (gxm - gx)/(2*np.pi*w)
    print(f"  {w:5.2f}   {ce:12.6f}   {cx:12.6f}")
