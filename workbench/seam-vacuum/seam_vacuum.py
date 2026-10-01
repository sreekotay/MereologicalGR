"""Does the content sector's vacuum energy leak through the seam? (gravity-corner §3, owed)

gravity-corner check 6 showed: at fixed covector n and fixed B, -rho g~^ab k_a k_b != 0 at the
fabric's null corner -- a rank-1 piece along n of order B*rho. Whether that piece is physical
depends on the realization. The corpus has two:

  R1  c1 toy, n tracking the congruence (aether: unit-norm n, Lagrange multiplier)
      matter on g~ = A(g + B n n), Einstein-Hilbert on g.
  R2  c9 Hassan-Rosen bimetric, finite branch: matter on g with its own EH (M_g),
      the seam metric f = g~ hidden (M_f = alpha M_g).

and the class the leak would need:

  R3  B a function of a field matter's vacuum can push (disformal scalar B(phi, X)).
"""
import sympy as sp

checks = []
def check(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)

# ---------------------------------------------------------------------------------------------
# R1. Aether. Write the vacuum term through g~ with n_mu a covector:
#     det(g + B n n) = det(g) (1 + B N),  N = g^{mu nu} n_mu n_nu.
#     So  -rho sqrt(-g~) = sqrt(-g) F(N),   F(N) = -rho A^2 sqrt(1 + B N).
# The aether carries  sqrt(-g) lam (N + 1)  (unit norm). Every equation of motion sees F only
# through dF/dN and F at N = -1. Show the g- and n-equations depend on (lam + F'(-1)) and F(-1)
# alone -- i.e. the vacuum term is a cosmological constant plus a shift of the multiplier.
# ---------------------------------------------------------------------------------------------
rho, A, B, lam = sp.symbols('rho A B lambda', real=True)
Nn = sp.symbols('N', real=True)
F = -rho*A**2*sp.sqrt(1 + B*Nn)
Fm1 = sp.simplify(F.subs(Nn, -1))
dFm1 = sp.simplify(sp.diff(F, Nn).subs(Nn, -1))
check("R1a. F(-1) = -rho A^2 sqrt(1-B): an ordinary cosmological term",
      sp.simplify(Fm1 + rho*A**2*sp.sqrt(1 - B)) == 0)

# Minkowski-tangent algebra with symbolic g^{mu nu} variations: for L = sqrt(-g) G(N),
#   T^{mu nu} = -2/sqrt(-g) dL/dg_{mu nu} = G g^{mu nu} - 2 G'(N)(-n^mu n^nu)... we just need the
# structure: dN/dg_{mu nu} = -n^mu n^nu,  d sqrt(-g)/dg_{mu nu} = (1/2) sqrt(-g) g^{mu nu}.
# Coefficients of g^{mu nu} and n^mu n^nu in dL/dg_{mu nu}, on N = -1:
def coeffs(G):
    Gm1 = G.subs(Nn, -1)
    dGm1 = sp.diff(G, Nn).subs(Nn, -1)
    return sp.Rational(1, 2)*Gm1, -dGm1        # (g^{mu nu} coeff, n^mu n^nu coeff)
c_vac = coeffs(F)
c_lam = coeffs(lam*(Nn + 1))
c_tot = [sp.simplify(c_vac[i] + c_lam[i]) for i in range(2)]
# n-equation: dL/dn_mu = 2 G'(N) n^mu  -> coefficient G'(-1)
n_tot = sp.simplify(sp.diff(F + lam*(Nn + 1), Nn).subs(Nn, -1))
lam_eff = sp.symbols('lambda_eff', real=True)
shift = {lam: lam_eff - dFm1}
check("R1b. g-equation: n n coefficient depends only on lam_eff = lam + F'(-1)",
      sp.simplify(c_tot[1].subs(shift) + lam_eff) == 0)
check("R1c. n-equation: force along n depends only on lam_eff",
      sp.simplify(n_tot.subs(shift) - lam_eff) == 0)
check("R1d. g-equation: g coefficient = F(-1)/2, a pure cosmological constant",
      sp.simplify(c_tot[0] - Fm1/2) == 0)
print("     multiplier shift F'(-1) =", sp.simplify(dFm1))

# ---------------------------------------------------------------------------------------------
# R2. Bimetric (c9). Matter on g. Its vacuum adds rho_vac to the g-Friedmann equation only.
#   g-Friedmann : 3H^2 = rho_m + rho_vac + m^2 (b0 + 3 b1 y + 3 b2 y^2 + b3 y^3)
#   branch      : m^2 G(y) = 3 alpha^2 H^2,  G = b1/y + 3 b2 + 3 b3 y + b4 y^2
# rho_vac enters only as rho_vac + m^2 b0; the branch function has no b0.
# ---------------------------------------------------------------------------------------------
y, H, m, al, rm, rv = sp.symbols('y H m alpha rho_m rho_vac', positive=True)
b0, b1, b2, b3, b4 = sp.symbols('beta0:5', real=True)
Gy = b1/y + 3*b2 + 3*b3*y + b4*y**2
check("R2a. branch function G(y) contains no beta0", b0 not in Gy.free_symbols)
fried = rm + rv + m**2*(b0 + 3*b1*y + 3*b2*y**2 + b3*y**3)
Lam = sp.symbols('Lambda_obs')
check("R2b. rho_vac and beta0 enter only as the sum Lambda_obs = rho_vac + m^2 beta0",
      sp.simplify(fried.subs(b0, (Lam - rv)/m**2) - (rm + Lam + m**2*(3*b1*y + 3*b2*y**2 + b3*y**3))) == 0)
# the seam B follows y(H) on the branch; with H observed, B is blind to the split
yb = sp.symbols('y_b', positive=True)
branch = sp.Eq(m**2*Gy.subs({b2: 0, b3: 0, b4: -b1}).subs(y, yb), 3*al**2*H**2)
check("R2c. branch y(H) (beta1-beta4 class) involves neither rho_vac nor beta0",
      not ({rv, b0} & branch.free_symbols))

# ---------------------------------------------------------------------------------------------
# R3. Where the leak is real: B = B(s) for a dynamical s that matter's vacuum can push.
#     V_eff(s) = rho A^2 sqrt(1 - B(s));  dV/ds = -rho A^2 B'(s) / (2 sqrt(1-B)).
# ---------------------------------------------------------------------------------------------
s = sp.symbols('s', real=True)
Bf = sp.Function('B')(s)
V = rho*A**2*sp.sqrt(1 - Bf)
dV = sp.simplify(sp.diff(V, s))
check("R3. state-dependent B: vacuum exerts force -rho A^2 B'/(2 sqrt(1-B)) on the state",
      sp.simplify(dV + rho*A**2*sp.diff(Bf, s)/(2*sp.sqrt(1 - Bf))) == 0)

# size of R3 if it applied with c9's numbers: B ~ 1e-16 today, B ~ (H/m_FP)^2 so dB/dlnH ~ 2B
rho_crit = 1.0
for label, scale in [("meV^4 (observed DE)", 1.0), ("TeV^4", 1e60), ("M_Pl^4", 1e120)]:
    print(f"     R3 scale {label:22s}: rho_vac*B ~ {scale*1e-16:.0e} rho_crit")

print()
print(f"{sum(o for _, o in checks)}/{len(checks)} checks passed")
