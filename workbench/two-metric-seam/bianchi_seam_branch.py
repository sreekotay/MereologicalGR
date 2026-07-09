import sympy as sp

t = sp.symbols('t')
a = sp.Function('a')(t)   # g scale factor, g lapse N=1 gauge (kept general below)
b = sp.Function('b')(t)   # f scale factor
X = sp.Function('X')(t)   # f-metric lapse (g lapse = 1)
b0,b1,b2,b3,b4 = sp.symbols('beta0 beta1 beta2 beta3 beta4')
m2 = sp.symbols('m2', positive=True)   # m^2 M_g^2 (units absorbed)
Mf2 = sp.symbols('Mf2', positive=True) # M_f^2 (times 1)

y = b/a
# elementary symmetric polynomials of S = diag(X, y, y, y):
U1 = b0 + 3*b1*y + 3*b2*y**2 + b3*y**3      # coefficient of N a^3 (N=1)
U2 = b1 + 3*b2*y + 3*b3*y**2 + b4*y**3      # coefficient of X a^3

da, db = sp.diff(a,t), sp.diff(b,t)

# minisuperspace Lagrangian, f-sector + interaction (matter & g-EH irrelevant
# for the f-sector Bianchi constraint since matter couples to g only)
L = -3*Mf2*b*db**2/X - m2*(a**3*U1 + X*a**3*U2)

# X is a lapse: primary constraint
E_X = sp.diff(L, X)
# b equation of motion
E_b = sp.diff(sp.diff(L, db), t) - sp.diff(L, b)

# consistency: d/dt E_X must vanish on-shell (using E_b=0 and E_X=0)
dE_X = sp.diff(E_X, t)

# eliminate bddot using E_b = 0
bdd = sp.solve(sp.Eq(E_b, 0), sp.diff(b, t, 2))[0]
D = dE_X.subs(sp.diff(b, t, 2), bdd)
# eliminate Mf2 using E_X = 0  ->  Mf2 = m2 a^3 U2 X^2 / (3 b db^2)
Mf2_sol = sp.solve(sp.Eq(E_X, 0), Mf2)[0]
D = sp.simplify(D.subs(Mf2, Mf2_sol))

D = sp.factor(sp.simplify(D))
print("Bianchi consistency condition (must vanish on-shell):")
print(D)

# check the claimed factorization: D ?= -3 m2 a^2 (b1 + 2 b2 y + b3 y^2)(db - X da) * (extra)

target = (b1*a**2 + 2*b2*a*b + b3*b**2)*(db - X*da)
q = sp.simplify(D / target)
print("\nD / [(beta1 a^2 + 2 beta2 a b + beta3 b^2)(bdot - X adot)] =")
print(sp.simplify(q))
