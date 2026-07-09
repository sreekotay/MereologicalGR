import sympy as sp, random

# ---------- (a) composite metric determinant identity ----------
# random symmetric g (invertible, signature irrelevant for the algebraic identity)
random.seed(3)
def randsym():
    A = sp.Matrix(4,4, lambda i,j: sp.Rational(random.randint(-4,4)))
    return (A+A.T)/2 + sp.diag(5,5,5,5)  # push away from singular
g = randsym()
# build f = g * X^2 with a random X that has real sqrt: choose X = S diag S^-1 style via g^-1 f construction
# simpler: pick X directly with positive eigenvalues via X = I + small random
R = sp.Matrix(4,4, lambda i,j: sp.Rational(random.randint(-2,2),7))
X = sp.eye(4) + R*R.T/3   # symmetric positive-ish, g^-1 f = X^2 consistency: f = g X^2 need f symmetric -> use X g-symmetric instead
# use the standard trick: X such that gX is symmetric: X = g^-1 * S with S symmetric pos
S = randsym()/3 + sp.diag(3,3,3,3)
# define X2 = g^-1 S  (so f=S=g X2, and X=sqrt(g^-1 f) satisfies g X sym). We just need ANY X with gX symmetric:
# take X = sqrt of M := g^-1 S via eigen (rationals -> use sympy sqrt of matrix numerically)
import mpmath as mp
gn = mp.matrix([[float(g[i,j]) for j in range(4)] for i in range(4)])
Sn = mp.matrix([[float(S[i,j]) for j in range(4)] for i in range(4)])
M = gn**-1 * Sn
Xn = mp.sqrtm(M)
a, b = 0.7, 0.4
geff = a*a*gn + a*b*(gn*Xn + (gn*Xn).T) + b*b*Sn   # alpha^2 g + 2ab gX + b^2 f  (gX symmetric up to numerics)
lhs = mp.det(geff)
rhs = mp.det(gn) * (mp.det(a*mp.eye(4) + b*Xn))**2
print("(a) det(geff) = det(g) det(aI+bX)^2 :", mp.almosteq(lhs, rhs, rel_eps=1e-12))
# and det(aI+bX) = sum_n a^(4-n) b^n e_n(X)
import itertools
lam = mp.eig(Xn, left=False, right=False)
es = [1,0,0,0,0]
for n in range(1,5):
    es[n] = sum(mp.re(mp.fprod(c)) for c in itertools.combinations(lam,n))
poly = sum((a**(4-n))*(b**n)*es[n] for n in range(5))
print("(a') det(aI+bX) = sum a^{4-n}b^n e_n(X):", mp.almosteq(mp.det(a*mp.eye(4)+b*Xn), poly, rel_eps=1e-10))

# ---------- (b) seam metric square root ----------
t,x,y,z = sp.symbols('t x y z')
B = sp.Rational(3,7)
f_,p_,q_,r_,w_ = sp.Rational(2), sp.Rational(3), sp.Rational(5), sp.Rational(7), sp.Rational(1,2)
g2 = sp.Matrix([[-f_,0,w_,0],[0,p_,0,0],[w_,0,q_,0],[0,0,0,r_]])
nu = sp.zeros(4,1); nu[0]=1/sp.sqrt(f_)
# normalize n to unit timelike wrt g2 (g2 has cross term; recompute normalization)
norm = (nu.T*g2*nu)[0]
nu = nu/sp.sqrt(-norm)
nl = g2*nu
gt = g2 + B*nl*nl.T
Minv = g2.inv()*gt          # g^{-1} g~ = I + B n^mu n_nu
Pn = -nu*nl.T               # projector onto n: P^mu_nu = -n^mu n_nu, P^2=P
Xseam = sp.eye(4) + (sp.sqrt(1-B)-1)*Pn
print("(b) P^2=P:", sp.simplify(Pn*Pn-Pn)==sp.zeros(4,4))
print("(b) X^2 = g^{-1} g~ :", sp.simplify(Xseam*Xseam - Minv)==sp.zeros(4,4))
print("(b) gX symmetric:", sp.simplify(g2*Xseam-(g2*Xseam).T)==sp.zeros(4,4))
print("(b) e_n(X):", [sp.simplify(sum(sp.Matrix(Xseam).eigenvals(multiple=True)[i] for i in [])) if False else None][0] or "skip")
ev = Xseam.eigenvals()
print("(b) eigenvalues of X:", ev)
