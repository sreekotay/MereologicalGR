"""
A. C=0 case. Dh=0 with B!=0 forces B const, Dn=0 => n_mu = -dt (locally), g ultrastatic:
   g = -dt^2 + gamma_ij(x) dx^i dx^j,  gt = -(1-B) dt^2 + gamma.
   Show: Gamma^i_{tt} = Gamma^i_{tj} = Gamma^t_{ij} = Gamma^t_{tt} = 0 for BOTH metrics,
   so spatial geodesic equation decouples from dt/dlambda: the spatial track of ANY
   geodesic (any speed, incl. gt-null and g-null) is a geodesic of gamma.
   => lensing identical EXACTLY (all orders in B); cone selection changes only dt/dl.

B. C!=0 case (realistic lens, static weak field, n static => a != 0):
   g = -(1+2*Phi) dt^2 + (1-2*Phi) delta, Phi = -GM/r.
   Deflection of a test track with coordinate speed beta:
     alpha(beta) = (2GM/b) (1 + 1/beta^2)   [derive by O(Phi) transverse impulse]
   Photon on gt: beta^2 = 1-B  =>  alpha_ph - alpha_gw = (2GM/b) * B/(1-B)
     = eps * alpha_gw * (1 + O(B)).

C. General drag h: cone speed c(khat) = 1 - eps(khat),
   eps(khat) = (1/2)[h_00 + 2 h_0i khat^i + h_ij khat^i khat^j] + O(h^2)  (rest frame of n)
   For h = B n x n : eps = B/2 for all khat (isotropic); adding lambda*g shifts eps by 0.
"""
import sympy as sp

# ---------- A ----------
t, x, y, z = sp.symbols('t x y z', real=True)
X = [t, x, y, z]
g11 = sp.Function('g11', positive=True)(x, y, z)
g22 = sp.Function('g22', positive=True)(x, y, z)
g33 = sp.Function('g33', positive=True)(x, y, z)
g12 = sp.Function('g12')(x, y, z)
B = sp.Symbol('B', positive=True)

gamma = sp.Matrix([[g11, g12, 0], [g12, g22, 0], [0, 0, g33]])

def christoffel(gm, XX):
    gi = gm.inv()
    d = len(XX)
    return [[[sp.simplify(sum(gi[l, s]*(sp.diff(gm[s, m], XX[n]) + sp.diff(gm[s, n], XX[m]) - sp.diff(gm[m, n], XX[s])) for s in range(d))/2)
              for n in range(d)] for m in range(d)] for l in range(d)]

for name, lapse2 in [("g (lapse 1)", sp.Integer(1)), ("gt (lapse 1-B)", 1-B)]:
    G4 = sp.zeros(4, 4)
    G4[0, 0] = -lapse2
    G4[1:, 1:] = gamma
    Gam = christoffel(G4, X)
    mixed_zero = all(sp.simplify(Gam[0][m][n]) == 0 for m in range(4) for n in range(4)) and \
                 all(sp.simplify(Gam[i][0][n]) == 0 for i in (1, 2, 3) for n in (0,)) and \
                 all(sp.simplify(Gam[i][0][j]) == 0 for i in (1, 2, 3) for j in range(4))
    spatial_match = all(sp.simplify(Gam[i][j][k] - christoffel(gamma, [x, y, z])[i-1][j-1][k-1]) == 0
                        for i in (1, 2, 3) for j in (1, 2, 3) for k in (1, 2, 3))
    print(f"{name}: all time-mixing Christoffels vanish: {mixed_zero}; spatial Christoffels == gamma's: {spatial_match}")
# consequence: d^2 x^i/dlam^2 + Gam^i_jk dx^j dx^k = 0 (pure gamma geodesic), d^2 t/dlam^2 = 0
# -> spatial track independent of speed and of which metric; only dt/dl differs.

# ---------- B ----------
GM, b, beta = sp.symbols('G_M b beta', positive=True)
Phi = -GM/sp.sqrt(x**2 + y**2)
gw = sp.diag(-(1+2*Phi), (1-2*Phi), (1-2*Phi), (1-2*Phi))
Gam = christoffel(gw, X)
# straight-line track: x = beta*t, y = b; 4-velocity u ~ (1, beta, 0, 0)
u = [1, beta, 0, 0]
ay = -sum(Gam[2][m][n]*u[m]*u[n] for m in range(4) for n in range(4))   # d^2 y/dt^2 at O(Phi)
ay = sp.expand(sp.series(ay.subs({y: b}), GM, 0, 2).removeO())
alpha = -sp.integrate(ay.subs(x, beta*t), (t, -sp.oo, sp.oo))/beta       # |Delta v_y| / v_x
alpha = sp.simplify(alpha)
print("alpha(beta) =", alpha)                                            # expect 2GM(1+beta^2)/(b beta^2)
print("check alpha(1) = 4GM/b:", sp.simplify(alpha.subs(beta, 1) - 4*GM/b) == 0)
dalpha = sp.simplify(alpha.subs(beta, sp.sqrt(1-B)) - alpha.subs(beta, 1))
print("alpha_photon - alpha_GW =", sp.factor(dalpha), " = eps*alpha_GW*(1+O(B)):",
      sp.simplify(sp.series(dalpha/( (B/2)*4*GM/b ), B, 0, 1).removeO()) == 1)

# ---------- C ----------
h00, e = sp.symbols('h00 e', real=True)
h0 = sp.Matrix(sp.symbols('h01 h02 h03', real=True))
hS = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'hs{min(i,j)}{max(i,j)}', real=True))
kx, ky, kz = sp.symbols('kx ky kz', real=True)   # unit spatial direction
khat = sp.Matrix([kx, ky, kz])
c = sp.Symbol('c', positive=True)
eta4 = sp.diag(-1, 1, 1, 1)
h4 = sp.zeros(4, 4)
h4[0, 0] = e*h00
for i in range(3):
    h4[0, i+1] = h4[i+1, 0] = e*h0[i]
    for j in range(3):
        h4[i+1, j+1] = e*hS[i, j]
c1 = sp.Symbol('c1', real=True)
k4 = sp.Matrix([1, (1+e*c1)*kx, (1+e*c1)*ky, (1+e*c1)*kz])
null = sp.expand((k4.T*(eta4+h4)*k4)[0]).subs(kz**2, 1-kx**2-ky**2)
o1 = sp.expand(null).coeff(e, 1)
c1sol = sp.solve(sp.Eq(o1, 0), c1)[0]
eps_k = sp.simplify(-c1sol)   # c = 1 - eps(khat)
pred = sp.Rational(1, 2)*(h00 + 2*(h0.T*khat)[0] + (khat.T*hS*khat)[0])
print("eps(khat) - (1/2)[h00+2h0.k+hS:kk] == 0 on |khat|=1:",
      sp.simplify((eps_k - pred).subs(kz**2, 1-kx**2-ky**2)) == 0)
# isotropic member: h = B n x n  (h00=B, h0=0, hS=0) -> eps = B/2 const; lambda*g adds (h00=-l, hS=l delta):
lam = sp.Symbol('lam')
print("conformal piece invisible:", sp.simplify(pred.subs({h00: -lam}).subs({hS[i, j]: lam*(1 if i == j else 0) for i in range(3) for j in range(3)}).subs(kz**2, 1-kx**2-ky**2)) == 0)
