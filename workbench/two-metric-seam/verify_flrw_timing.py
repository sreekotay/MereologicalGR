"""
FLRW seam: g = -dt^2 + a(t)^2 dx^2, n = comoving flow, constant B.
 1. kinematics: a=sigma=omega=0, theta=3H
 2. C^l_mn = (B/(1-B)) (theta/3) n^l P_mn exactly, all components
 3. timing: photon (gt-null) vs GW (g-null) from same event to comoving observer:
    conformal-time gap Dt_eta = chi (1/sqrt(1-B) - 1); observer proper-time gap
    Delta t = a_0 * chi * (1/sqrt(1-B)-1) ~= eps * D_C / c  (D_C comoving distance)
    versus naive int eps dl/c with proper dl = a d(chi): differs by (1+z) weight.
"""
import sympy as sp

t, x, y, z = sp.symbols('t x y z', real=True)
X = [t, x, y, z]
a = sp.Function('a', positive=True)(t)
B = sp.Symbol('B', positive=True)

g = sp.diag(-1, a**2, a**2, a**2)
ginv = g.inv()
nl = sp.Matrix([-1, 0, 0, 0]); nu = sp.Matrix([1, 0, 0, 0])
gt = g + B*nl*nl.T
gtinv = gt.inv()

def christoffel(gm, gmi):
    return [[[sp.simplify(sum(gmi[l, s]*(sp.diff(gm[s, m], X[n]) + sp.diff(gm[s, n], X[m]) - sp.diff(gm[m, n], X[s])) for s in range(4))/2)
              for n in range(4)] for m in range(4)] for l in range(4)]

Gam, Gamt = christoffel(g, ginv), christoffel(gt, gtinv)

H = sp.diff(a, t)/a
P = g + nl*nl.T
theta = 3*H
ok = True
nonzero = []
for l in range(4):
    for m in range(4):
        for n in range(4):
            C = sp.simplify(Gamt[l][m][n] - Gam[l][m][n])
            pred = (B/(1-B))*(theta/3)*nu[l]*P[m, n]
            if sp.simplify(C - pred) != 0:
                ok = False
            if C != 0:
                nonzero.append(((l, m, n), C))
print("FLRW: C == (B/(1-B)) (theta/3) n^l P_mn exactly:", ok)
print("nonzero components:", nonzero)

# acceleration, shear, vorticity of comoving n
Dn = sp.Matrix([[sp.diff(nl[n], X[m]) - sum(Gam[s][m][n]*nl[s] for s in range(4)) for n in range(4)] for m in range(4)])
acc = sp.simplify(sp.Matrix([sum(nu[m]*Dn[m, n] for m in range(4)) for n in range(4)]))
sig = sp.simplify((Dn + Dn.T)/2 - theta*P/3)   # (a=0 so full sym part is projected)
omg = sp.simplify((Dn - Dn.T)/2)
print("a = 0:", acc == sp.zeros(4, 1), "| sigma = 0:", sig == sp.zeros(4, 4), "| omega = 0:", omg == sp.zeros(4, 4),
      "| theta - 3H = 0:", sp.simplify(sum((ginv*Dn)[m, m] for m in range(4)) - 3*H) == 0)

# ---- timing residual ----
# radial null: photon  a dx/dt = sqrt(1-B)  =>  chi = sqrt(1-B) * (eta_g_arrive_gamma - eta_e)
# GW: chi = eta_arrive_gw - eta_e.  Conformal gap:
chi, eps = sp.symbols('chi epsilon', positive=True)
gap_eta = chi*(1/sp.sqrt(1-B) - 1)
print("conformal gap series:", sp.series(gap_eta, B, 0, 3))
print("with eps=B/2:", sp.simplify(sp.series(gap_eta, B, 0, 2).removeO().subs(B, 2*eps)), "+O(eps^2)")

# exact check in matter-dominated a = (eta/eta0)^2 (conformal time), a0 = 1:
eta, eta0, etae = sp.symbols('eta eta_0 eta_e', positive=True)
a_conf = (eta/eta0)**2
tt = sp.integrate(a_conf, (eta, 0, eta))          # cosmic time t(eta)
eta_gw = etae + chi
eta_ph = etae + chi/sp.sqrt(1-B)
Delta_t_exact = sp.simplify(tt.subs(eta, eta_ph) - tt.subs(eta, eta_gw))
lead = sp.simplify(sp.series(Delta_t_exact, B, 0, 2).removeO())
# compare to eps * a(eta_arr) * chi  = eps * a0-comoving distance when observed today (eta_gw -> eta0):
print("Delta t leading order (matter dom):", sp.factor(lead))
print("equals (B/2) * a(eta_arrival) * chi at chi->0 arrival:",
      sp.simplify(sp.limit(lead/( (B/2)*a_conf.subs(eta, eta_gw)*chi), chi, 0)) == 1)
# and against naive proper-path integral int eps dl = eps * int a d(chi'):
s = sp.Symbol('s', positive=True)
naive = (B/2)*sp.integrate(a_conf.subs(eta, etae + s), (s, 0, chi))
print("naive int eps dl (proper dl at passage):", sp.simplify(naive))
print("ratio correct/naive at etae=eta0-chi, small chi (should be 1 + O(chi)):",
      sp.series(sp.simplify(lead/naive).subs(etae, eta0 - chi), chi, 0, 2))
# correct formula: Delta t = eps * int (1+z(l)) dl = eps * a(eta_obs) * chi  (comoving distance x a_obs)
corr = (B/2)*sp.integrate(a_conf.subs(eta, eta_gw)/a_conf.subs(eta, etae + s)*a_conf.subs(eta, etae + s), (s, 0, chi))
print("(1+z)-weighted integral == leading Delta t:", sp.simplify(corr - lead) == 0)
