#!/usr/bin/env python3
"""
Sweep finding 1 + 2: adjacency is flow-indexed, and the disformal seam does not fork it.

A0 §6 names adjacency "imported from GR's metric and named as peer of flow."
Exhibit test on  space = ordering + adjacency :  what does adjacency's magnitude need?

[F1] The spatial metric is h = g + u (x) u. It is defined only given a unit timelike
     field u -- a flow congruence. Flow's magnitude needs only a worldline
     (dtau^2 = -g(dx,dx)); adjacency's needs a congruence. Not peers: adjacency
     is parametrized by flow.

[F2] Under the corpus's own seam g~ = A(g + B n (x) n), check whether adjacency forks.
     If the n-orthogonal subspace and the metric restricted to it agree for g and g~
     (up to the conformal/volume gauge A, which scales space and time alike), then
     the fabric/content split is a FLOW split with shared adjacency, and c1's Cost 0
     names the wrong role.

Checks are covariant: a boosted n in Minkowski, plus a generic metric.
"""
import sympy as sp

ok = []
def check(name, cond):
    ok.append(bool(cond)); print(("  PASS  " if cond else "  FAIL  ")+name)

chi, B, A = sp.symbols('chi B A', real=True)
eta = sp.diag(-1,1,1,1)
n_up = sp.Matrix([sp.cosh(chi), sp.sinh(chi), 0, 0])   # boosted unit timelike
n_dn = eta*n_up
check("n unit timelike for every boost", sp.simplify((n_up.T*eta*n_up)[0]) == -1)

print("\n[F1] the spatial projector needs u")
h = eta + n_dn*n_dn.T
check("h = g + n n annihilates n  (h(n,.) = 0)", sp.simplify(h*n_up) == sp.zeros(4,1))
check("h has rank 3 -- a spatial metric on the slice orthogonal to n", h.rank() == 3)
# a different congruence gives a different spatial metric: adjacency depends on the flow chosen
chi2 = sp.symbols('chi2', real=True)
m_dn = eta*sp.Matrix([sp.cosh(chi2), sp.sinh(chi2), 0, 0])
h2 = eta + m_dn*m_dn.T
diff = sp.simplify(h - h2)
check("different flow congruence -> different spatial metric (h depends on u)",
      diff != sp.zeros(4,4))
print("        => separation is three-place: (A, B, congruence). Flow's magnitude")
print("           needs one worldline; adjacency's needs a family. Not peers.")

print("\n[F2] does the disformal seam fork adjacency?")
gt = A*(eta + B*n_dn*n_dn.T)
# n-orthogonal subspace under g and under g~
v = sp.Matrix(sp.symbols('v0:4', real=True))
g_orth  = sp.simplify((n_up.T*eta*v)[0])
gt_orth = sp.simplify((n_up.T*gt*v)[0])
check("g~-orthogonal complement of n == g-orthogonal complement  (same slice)",
      sp.simplify(gt_orth - A*(1-B)*g_orth) == 0)
# restrict both metrics to vectors orthogonal to n
w = sp.Matrix(sp.symbols('w0:4', real=True))
g_vw  = (v.T*eta*w)[0]
gt_vw = (v.T*gt*w)[0]
# on the slice, g(n,v)=g(n,w)=0, so the B term drops out:
on_slice = {v[0]: sp.solve(g_orth, v[0])[0],
            w[0]: sp.solve((n_up.T*eta*w)[0], w[0])[0]}
check("on the shared slice  g~(v,w) = A * g(v,w)  -- spatial metrics agree up to gauge A",
      sp.simplify((gt_vw - A*g_vw).subs(on_slice)) == 0)
# the flow leg is where they differ
check("along n:  g~(n,n) = A(1-B) * g(n,n)  -- the time leg carries the extra (1-B)",
      sp.simplify((n_up.T*gt*n_up)[0] - A*(1-B)*(n_up.T*eta*n_up)[0]) == 0)
print("        => modulo the conformal/volume gauge A (scales space and time alike),")
print("           the two metrics differ ONLY along n. Adjacency is shared; flow forks:")
print("           dtau~/dtau = sqrt(1-B). The cone ratio sqrt(1-B) is entirely a flow ratio.")

print("\n[F2'] generic background, not just Minkowski")
g = sp.Matrix(4,4, lambda i,j: sp.Symbol(f'g{min(i,j)}{max(i,j)}', real=True))
u = sp.Matrix(sp.symbols('u0:4', real=True))
u_dn = g*u
gt_gen = g + B*u_dn*u_dn.T
check("generic g: g~(u,v) = (1 + B g(u,u)) g(u,v)  -- same orthogonal complement",
      sp.simplify((u.T*gt_gen*v)[0] - (1 + B*(u.T*g*u)[0])*(u.T*g*v)[0]) == 0)
# for v,w with g(u,v)=g(u,w)=0 the B term vanishes identically
expr = (v.T*gt_gen*w)[0] - (v.T*g*w)[0] - B*(u.T*g*v)[0]*(u.T*g*w)[0]
check("generic g: g~(v,w) - g(v,w) = B g(u,v) g(u,w)  -- zero on the slice", sp.simplify(expr) == 0)

print(f"\n{sum(ok)}/{len(ok)} checks passed")
print("""
CONSEQUENCE FOR c1 COST 0.
  c1 books its unpaid premise as "the fabric/content split of ADJACENCY ... chosen,
  coined in this note, unaudited upstream." Within the rank-1 timelike class (the
  corpus's own seam class, c9's recognition lemma), adjacency does not fork. All
  three of A0's senses are shared: extension and separation (the restricted metric,
  equal up to gauge) and nextness (same point set P).

  What forks is FLOW -- two clock rates along n -- and c5 already derives that from
  the order pair ("flow forks with the pair ... g~00 = g00(1-B)"). So Cost 0 decomposes:
    kinematic split   -> flow only, inherited from the order-pair hypothesis
    dynamical asymmetry ("gravity IS, matter RIDES") -> which metric Einstein-Hilbert
                         governs; imported from c1's toy action, not a role carve
  Neither is a carve of adjacency. The parked root role is untouched.
""")
