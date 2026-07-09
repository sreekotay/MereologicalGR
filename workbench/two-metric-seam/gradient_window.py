"""
GRADIENT-WINDOW CALCULATION at the seam point.
Hassan-Rosen bimetric, GR-limit finite branch, y* = 1 model class
(beta1-beta4 model: beta2=beta3=0, beta4=-beta1, beta0 free -> Lambda),
m_FP = 1e8 H0, mixing alpha = M_f/M_g free and small.

Part A (sympy): background constraint, delta-y law, B(alpha, H/m) reconciliation,
               m_FP relation, y'(N) law, f-cone speed.
Part B (numpy): y(z), instability window z-range, conformal-time window,
               growth e-folds N(k) on CMB / Lya modes, alpha bounds.

Literature anchors (see report):
 - finite-branch scalar gradient instability exists for H > ~m_FP and ends
   when H drops to ~m_FP  [Konnig 1503.07436; Hogas-Mortsell 2101.08791/94,
   Hogas thesis; Akrami et al 1503.07521]
 - growth is exponential at rate |c_s| k in conformal time [Konnig 1503.07436]
 - the unstable mode is the massive/hidden-sector scalar; matter couples to it
   with weight sin(theta) ~ alpha  [1503.07521; Luben et al 2003.03382]
"""

import sympy as sp
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

print("=" * 72)
print("PART A: background algebra (sympy)")
print("=" * 72)

y, H, m, al, b0, b1, b2, b3, b4, rho = sp.symbols(
    'y H m alpha beta0 beta1 beta2 beta3 beta4 rho', positive=True)

# --- dynamical-branch constraint from the two Friedmann eqs + Bianchi ---
# g-Friedmann : 3H^2 = rho + m^2 (b0 + 3 b1 y + 3 b2 y^2 + b3 y^3)   [M_g=1]
# f-Friedmann : 3 H_f^2 = (m^2/al^2) (b1/y^3 + 3 b2/y^2 + 3 b3/y + b4)
# Bianchi (dynamical branch): bdot = X adot  =>  H_f = H/y
# =>  m^2 G(y) = 3 al^2 H^2,   G(y) = b1/y + 3 b2 + 3 b3 y + b4 y^2
G = b1/y + 3*b2 + 3*b3*y + b4*y**2

# vacuum check against literature proportional-background condition:
# al^2 (c b0 + 3c^2 b1 + 3c^3 b2 + c^4 b3) = b1 + 3c b2 + 3c^2 b3 + c^3 b4
lhs = al**2 * y * (b0 + 3*b1*y + 3*b2*y**2 + b3*y**3)   # al^2 * y * (3H^2/m^2)|vac
print("vacuum constraint == literature quartic:",
      sp.simplify(sp.expand(y*G - lhs)
                  - sp.expand((b1 + 3*b2*y + 3*b3*y**2 + b4*y**3)
                              - al**2*y*(b0 + 3*b1*y + 3*b2*y**2 + b3*y**3))) == 0)

# --- y* = 1 model class: G(1) = 0  <=>  b1 + 3 b2 + 3 b3 + b4 = 0 ---
print("G(1) =", sp.simplify(G.subs(y, 1)), " -> y*=1 iff b1+3b2+3b3+b4=0")

# --- beta1-beta4 model (b2=b3=0, b4=-b1) ---
Gb = G.subs({b2: 0, b3: 0, b4: -b1})          # G = b1 (1/y - y^2)
Gp = sp.diff(Gb, y)
print("beta1-beta4 :  G(y) =", sp.factor(Gb), ",  G'(1) =", Gp.subs(y, 1))

# linearized splitting near y*=1:  m^2 G'(1) dy = 3 al^2 H^2
dy = sp.solve(sp.Eq(m**2*Gp.subs(y, 1)*sp.Symbol('dy'), 3*al**2*H**2),
              sp.Symbol('dy'))[0]
print("delta-y = 3 al^2 H^2 / (m^2 G'(1)) =", sp.simplify(dy),
      "   (negative: y -> 1 from below)")

# --- Fierz-Pauli mass at the proportional point c = y* = 1 ---
# literature: m_FP^2 = m^2 (1+al^2 c^2)/(al^2 c^2) * c (b1 + 2 b2 c + b3 c^2)
mFP2 = m**2 * (1 + al**2)/al**2 * b1          # c = 1, b2=b3=0
print("m_FP^2 = m^2 b1 (1+al^2)/al^2  ->  m^2 b1 = al^2 m_FP^2/(1+al^2)")

# --- reconciliation: |delta-y| in terms of m_FP ---
dy_mFP = sp.simplify(sp.Abs(dy).subs(b1, sp.Symbol('mFP2')*al**2/((1+al**2)*m**2))
                     .rewrite(sp.Piecewise))
dy_mFP = sp.simplify(al**2*H**2/(m**2*b1)
                     .subs(b1, 1) * 0 + (al**2*H**2)/(al**2*mFP2/(1+al**2)))
print("|delta-y| = al^2 H^2/(m^2 b1) = (1+al^2) (H/m_FP)^2   [alpha cancels]")
print("   sympy:", sp.simplify((al**2*H**2)/(m**2*b1)
                               - (1+al**2)*H**2/mFP2), "== 0")

# --- exact finite-branch background, GR limit (H = H_LCDM):
#   (1 - y^3)/y = 3 H^2 (1+al^2) / m_FP^2  == u(z)      [alpha-independent]
# --- y' = dy/dlna along the branch ---
w = sp.Symbol('w')  # effective eq of state: dH^2/dlna = -3(1+w) H^2
u = sp.Symbol('u', positive=True)
yN = sp.symbols('yprime')
expr = sp.Eq((1 - y**3)/y, u)
yp = sp.solve(sp.Eq(sp.diff((1 - y**3)/y, y)*yN, -3*(1+w)*u), yN)[0]
yp = sp.simplify(yp.subs(u, (1 - y**3)/y))
print("y'/y = dlny/dlna =", sp.simplify(yp/y), "  [-> 3(1+w) as y->0; -> 0 as y->1]")
# f-metric cone speed in comoving coords (relative to g-frame):
print("c_f = X/y = 1 + dlny/dlna  ->  1+3(1+w) deep in the unstable era")
print("      radiation era: c_f -> 5 ;  matter era: c_f -> 4")

print()
print("=" * 72)
print("PART B: numbers at the seam point (numpy)")
print("=" * 72)

h = 0.674
H0_Mpc = h/2997.92458            # H0 in Mpc^-1 (c=1)
Om, Orad = 0.315, 9.15e-5        # incl. neutrinos as radiation (early times)
OL = 1 - Om - Orad
H0_eV = 1.437e-33*(h/0.674)      # H0 in eV


def E(z):                        # H/H0, GR-limit background
    return np.sqrt(Orad*(1+z)**4 + Om*(1+z)**3 + OL)


for tag, mfp_over_H0 in [("m_FP = 1e8 H0 (prompt normalization, B==(H/m_FP)^2)", 1e8),
                         ("m_FP = sqrt(6)e8 H0 (if B==6(H/m_FP)^2 = 1e-16 today)",
                          np.sqrt(6)*1e8)]:
    print("-"*72)
    print(tag)
    mfp = mfp_over_H0
    print(f"  m_FP = {mfp*H0_eV:.3g} eV ; Compton wavelength = "
          f"{1/(mfp*H0_Mpc)*1e6:.3g} pc")

    # background y(z): (1-y^3)/y = 3 E^2/mfp^2  (alpha->0; (1+al^2)->1)
    # solve in d = 1-y (exact polynomial form, precision-safe for d ~ 1e-16):
    #   (1-y^3)/y = (3d - 3d^2 + d^3)/(1-d) = u
    def dbg(z):
        uu = 3*E(z)**2/mfp**2
        d = uu/3                       # Newton on (3d-3d^2+d^3) - uu(1-d) = 0
        for _ in range(60):
            f = (3*d - 3*d**2 + d**3) - uu*(1-d)
            fp = 3 - 6*d + 3*d**2 + uu
            d -= f/fp
        return d

    def ybg(z):
        return 1 - dbg(z)

    # instability window: H > m_FP  (anchored); y at the boundary:
    y_end = brentq(lambda yy: (1-yy**3)/yy - 3, 1e-6, 1)   # H = m_FP
    z_GI = brentq(lambda z: E(z) - mfp, 1e3, 1e9)
    z_half = brentq(lambda z: E(z) - mfp/np.sqrt(2), 1e3, 1e9)  # Higuchi-marginal band
    print(f"  window ends (H=m_FP):        z_GI  = {z_GI:.3e}   y(z_GI) = {y_end:.3f}")
    print(f"  marginal band (H=m_FP/rt2):  z     = {z_half:.3e}")
    print(f"  y today = 1 - {dbg(0):.2e}  (splitting (H0/m_FP)^2 = {1/mfp**2:.1e})")
    print(f"  splitting 1-y at recomb (z=1090) = {dbg(1090):.3e}")
    print(f"  splitting 1-y at zeq (3400)      = {dbg(3400):.3e}")
    print(f"  y at BBN (z=4e8)                 = {ybg(4e8):.3e}"
          f"  [{(mfp/E(4e8))**2/3:.3e} = (m_FP/H)^2/3]")

    # conformal time from a=0 to end of window (Mpc, comoving):
    # eta = int_0^a da'/(a'^2 E(a')) / H0
    a_GI = 1/(1+z_GI)
    Ea = lambda a: np.sqrt(Orad/a**4 + Om/a**3 + OL)
    eta_GI = quad(lambda a: 1/(a**2*Ea(a)), 0, a_GI, limit=400)[0]/H0_Mpc
    print(f"  conformal time eta(z_GI) = {eta_GI:.2f} Mpc comoving"
          f"   [1/(aH) at z_GI = {(1+z_GI)/(mfp*H0_Mpc):.2f} Mpc]")

    # growth e-folds N(k) = |c_s| * k * eta_GI  (WKB; growth only if N > ~1)
    ks = np.array([1e-4, 1e-3, 1e-2, 0.05, 0.1, 0.2, 1.0, 3.0, 5.0])
    print(f"  {'k [1/Mpc]':>10} | {'N/|c_s|':>9} | {'N(c=1/rt3)':>10} |"
          f" {'N(c=1)':>8} | {'N(c=5)':>8} | e^N(c=1)")
    for k in ks:
        Nk = k*eta_GI
        print(f"  {k:10.4g} | {Nk:9.3g} | {Nk/np.sqrt(3):10.3g} |"
              f" {Nk:8.3g} | {5*Nk:8.3g} | {np.exp(min(Nk,700)):.3g}")

    # alpha bounds: contamination of observable spectrum ~ alpha^2 e^N < eps
    print("  alpha bounds from alpha^2 e^N(k) < eps :")
    for k, eps, lab in [(0.2, 1e-2, "CMB damping tail k=0.2, eps=1e-2"),
                        (3.0, 0.3,  "Lya k=3/Mpc, eps=0.3")]:
        for cs in [1/np.sqrt(3), 1.0, 5.0]:
            Nk = cs*k*eta_GI
            amax = np.sqrt(eps*np.exp(-min(Nk, 1400)))
            print(f"    {lab:34s} |c_s|={cs:4.2f}: alpha < {amax:.3g}")

print("-"*72)
print("cutoff sanity: hidden-sector strong-coupling scale "
      "L3=(m_FP^2 M_f)^(1/3), M_f = alpha M_Pl:")
MPl_eV = 2.435e27
for a_ in [1e-2, 1e-4, 1e-8]:
    L3 = (( (1e8*H0_eV)**2 * a_*MPl_eV ))**(1/3.)
    print(f"  alpha={a_:.0e}: L3 = {L3:.3g} eV  (length {1.9732e-7/L3:.3g} m)")
