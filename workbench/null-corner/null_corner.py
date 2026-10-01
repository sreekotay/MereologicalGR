"""Referee for workbench/null-corner: does adjacency survive a flow strip?

F1 (workbench/sweep) said no: "strip flow, keep adjacency -> adjacency's magnitude does not
survive". This script separates three objects F1 ran together and tests each.

  (a) h(u) = g + u(x)u      projection onto a congruence's rest space      -> u-indexed
  (b) induced metric on a surface / proper length of a spacelike curve     -> intrinsic, no u
  (c) radar distance from one worldline (ordering + that worldline's flow) -> worldline-indexed

and then the corner F1 missed:

  (d) a null hypersurface N: pullback of g is degenerate, rank 2, kernel = generator k.
      Proper time along k is zero (flow stripped). Transverse area survives, needs no u.
"""
import sympy as sp

checks = []
def check(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)

eta = sp.diag(-1, 1, 1, 1)
b = sp.symbols('beta', real=True)
gam = 1 / sp.sqrt(1 - b**2)

def boost_x(beta):
    G = 1 / sp.sqrt(1 - beta**2)
    L = sp.eye(4)
    L[0, 0] = G; L[0, 1] = -G*beta; L[1, 0] = -G*beta; L[1, 1] = G
    return L

def boost_y(beta):
    G = 1 / sp.sqrt(1 - beta**2)
    L = sp.eye(4)
    L[0, 0] = G; L[0, 2] = -G*beta; L[2, 0] = -G*beta; L[2, 2] = G
    return L

# ---- (a) projection is u-indexed ---------------------------------------------------------
u0 = sp.Matrix([1, 0, 0, 0])
ub = sp.Matrix([gam, gam*b, 0, 0])
h = lambda u: eta + (eta*u)*(eta*u).T
D = sp.Matrix([1, 2, 0, 0])                         # a timelike-or-spacelike displacement
d0 = sp.simplify((D.T*h(u0)*D)[0])
db = sp.simplify((D.T*h(ub)*D)[0])
check("(a) h(u)(D,D) changes with u", sp.simplify(d0 - db) != 0)

# ---- (b) intrinsic spacelike length needs no u ---------------------------------------------
S = sp.Matrix([sp.Rational(1, 2), 1, 0, 0])         # spacelike: -1/4 + 1 > 0
s2 = (S.T*eta*S)[0]
for L, nm in [(boost_x(b), "x"), (boost_y(b), "y")]:
    Sp = L*S
    check(f"(b) spacelike interval invariant under boost_{nm}", sp.simplify((Sp.T*eta*Sp)[0] - s2) == 0)
# induced metric of the t=0 slice equals h(u0) restricted, i.e. the slice supplies its own normal
E = sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])   # tangent basis of t=0
check("(b) induced metric on slice = pullback, defined without picking u", sp.simplify(E.T*eta*E - sp.eye(3)) == sp.zeros(3))

# ---- (c) radar distance is worldline-indexed -----------------------------------------------
# event P = (0, X, 0, 0); observer through origin with velocity v along x.
# radar: emit at proper time t1, receive at t2, distance = (t2 - t1)/2 (c = 1).
X, v = sp.symbols('X v', real=True)
def radar(Pt, Px, vel):
    Gv = 1 / sp.sqrt(1 - vel**2)
    tau = sp.symbols('tau', real=True)
    # observer at (Gv*tau, Gv*vel*tau); outgoing ray reaches P: Pt - Gv tau1 = Px - Gv vel tau1
    t1 = sp.solve(sp.Eq(Pt - Gv*tau, Px - Gv*vel*tau), tau)[0]
    t2 = sp.solve(sp.Eq(Gv*tau - Pt, Px - Gv*vel*tau), tau)[0]
    return sp.simplify((t2 - t1)/2)
r_rest = radar(0, X, 0)
r_move = radar(0, X, sp.Rational(3, 5))
check("(c) radar distance from rest observer = X", sp.simplify(r_rest - X) == 0)
check("(c) radar distance changes with the radar worldline", sp.simplify(r_move.subs(X, 1) - 1) != 0)
# radar distance uses only light signals (ordering) and one clock (flow): it equals proper
# length when the event is simultaneous in the observer's frame -> the chronometric bridge
check("(c) radar distance = proper length when P is simultaneous for the observer", sp.simplify(r_rest**2 - (sp.Matrix([0, X, 0, 0]).T*eta*sp.Matrix([0, X, 0, 0]))[0]) == 0)

# ---- (d) the null corner ------------------------------------------------------------------
# N = {t = x}. Coordinates on N: (lam, y, z) -> (lam, lam, y, z). Generator k = (1,1,0,0).
EN = sp.Matrix([[1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
qN = sp.simplify(EN.T*eta*EN)
check("(d) pullback to N is diag(0,1,1): degenerate, rank 2", qN == sp.diag(0, 1, 1))
k = sp.Matrix([1, 1, 0, 0])
check("(d) generator is null: proper time along it is zero (flow stripped)", (k.T*eta*k)[0] == 0)
check("(d) kernel of the pullback is the generator direction", qN*sp.Matrix([1, 0, 0]) == sp.zeros(3, 1))
# Lorentz maps that preserve N: boost along x rescales k, leaves y,z alone.
# Pull back via the transformed embedding and compare.
L = boost_x(b)
ENb = L*EN
# image of N under L is N itself (t-x -> scaled), so ENb spans N's tangent space; the pullback
# in the new parametrisation differs only by reparametrising lam -> transverse block unchanged
qNb = sp.simplify(ENb.T*eta*ENb)
check("(d) transverse 2-metric of N unchanged by the boost that preserves N", qNb[1:, 1:] == sp.eye(2) and qNb[0, 0] == 0)
# A boost along y moves N to a different null plane; the pullback of eta to *that* plane,
# built from L*EN, is identical. This is true by construction (L preserves eta) -- which is the
# point: the pullback is a property of (g, surface) and has no slot for u.
Ly = boost_y(b)
qNy = sp.simplify((Ly*EN).T*eta*(Ly*EN))
check("(d) pullback is frame-free: identical under any Lorentz map (no u enters)", sp.simplify(qNy - qN) == sp.zeros(3))
# Contrast: h(u) restricted to N's tangent space DOES depend on u (nondegenerate, u-indexed)
hN0 = sp.simplify(EN.T*h(u0)*EN)
hNb = sp.simplify(EN.T*h(boost_y(sp.Rational(1, 2)).inv()*u0)*EN)
check("(d) contrast: projecting N's tangents with h(u) instead gives u-dependent data", hN0 != hNb)

# ---- (e) area evolves along ordering, not flow: Raychaudhuri on a light cone ---------------
# future light cone of the origin, cut at affine lam along generators k = (1, n): area 4 pi lam^2.
lam = sp.symbols('lam', positive=True)
A = 4*sp.pi*lam**2
theta = sp.diff(A, lam)/A
check("(e) cone cross-section area grows along affine (ordering) parameter, theta = 2/lam",
      sp.simplify(theta - 2/lam) == 0)
# vacuum Raychaudhuri, shear-free: d theta/d lam = -theta^2/2
check("(e) vacuum null Raychaudhuri satisfied with zero proper time elapsed",
      sp.simplify(sp.diff(theta, lam) + theta**2/2) == 0)

print()
n_ok = sum(ok for _, ok in checks)
print(f"{n_ok}/{len(checks)} checks passed")
