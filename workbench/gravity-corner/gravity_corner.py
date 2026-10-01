"""Referee for workbench/gravity-corner: gravity read at the null corner.

gravity = ordering + influence + energy-momentum carries no flow. The light-sheet is where
flow is stripped and gravity still acts (Raychaudhuri). This script checks what gravity looks
like there, and what it cannot see.
"""
import sympy as sp

checks = []
def check(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)

eta = sp.diag(-1, 1, 1, 1)

# ---- 1. the corner sees a symmetric tensor only up to a multiple of g ----------------------
S = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"S{min(i,j)}{max(i,j)}"))
th, ph = sp.symbols('theta phi', real=True)
def null(t, p):
    return sp.Matrix([1, sp.sin(t)*sp.cos(p), sp.sin(t)*sp.sin(p), sp.cos(t)])
samples = [(0, 0), (sp.pi, 0), (sp.pi/2, 0), (sp.pi/2, sp.pi), (sp.pi/2, sp.pi/2),
           (sp.pi/2, 3*sp.pi/2), (sp.pi/4, 0), (sp.pi/4, sp.pi/2), (sp.pi/2, sp.pi/4),
           (3*sp.pi/4, sp.pi/4)]
eqs = [sp.expand((null(t, p).T*S*null(t, p))[0]) for t, p in samples]
sol = sp.solve(eqs, list(S.free_symbols), dict=True)[0]
Ssol = S.subs(sol)
c = Ssol[1, 1]
check("1. S(k,k)=0 for all null k  =>  S = c*g (the corner is blind to the g-part)",
      sp.simplify(Ssol - c*eta) == sp.zeros(4))

# ---- 2. Lambda and vacuum energy are pure g-parts -------------------------------------------
k = null(th, ph)
check("2. Lambda g_kk = 0 and vacuum T_kk = -rho g_kk = 0 for every null k",
      sp.simplify((k.T*eta*k)[0]) == 0)

# ---- 3. the corner equation + Bianchi + conservation returns GR with Lambda a constant -----
# R_ab - 8 pi G T_ab = f g_ab  (from 1). Divergence: (1/2) dR = df (Bianchi, dT_ab = 0).
# Trace: R - 8 pi G T = 4 f.
G_, R, T, dR, dT, C = sp.symbols('G R T dR dT C')
f = (R - 8*sp.pi*G_*T)/4
df = (dR - 8*sp.pi*G_*dT)/4
sol_dR = sp.solve(sp.Eq(dR/2, df), dR)[0]
check("3a. R + 8 pi G T is constant (d of it vanishes)", sp.simplify(sol_dR + 8*sp.pi*G_*dT) == 0)
# with R = C - 8 pi G T, G_ab = R_ab - R/2 g = 8 pi G T_ab + (f - R/2) g
coef = sp.simplify((f - R/2).subs(R, C - 8*sp.pi*G_*T))
check("3b. G_ab = 8 pi G T_ab - (C/4) g_ab: Lambda = C/4 is an integration constant",
      sp.simplify(coef + C/4) == 0)

# ---- 4. Jacobson: the flow normalisation and hbar both cancel --------------------------------
a, hbar, kap, eta_s, Rkk, Tkk, I = sp.symbols('a hbar kappa eta R_kk T_kk I', positive=True)
# boost field chi -> a chi: kappa -> a kappa, dQ -> a dQ.  dQ = kappa * I_T, I_T = int lam T_kk
dQ = a*kap*I*Tkk
Temp = hbar*a*kap/(2*sp.pi)
dA = I*Rkk          # magnitude of -int lam R_kk  (Raychaudhuri, same integral I)
Rsol = sp.solve(sp.Eq(eta_s*dA, dQ/Temp), Rkk)[0]
check("4a. normalisation a drops out of dQ/T", sp.diff(sp.simplify(dQ/Temp), a) == 0)
check("4b. with eta = 1/(4 G hbar): R_kk = 8 pi G T_kk, hbar gone",
      sp.simplify(Rsol.subs(eta_s, 1/(4*G_*hbar)) - 8*sp.pi*G_*Tkk) == 0)

# ---- 5. Schwarzschild-de Sitter: Lambda acts on flow, not at the corner ---------------------
t, r, thh, phh = sp.symbols('t r th ph', positive=True)
M, Lam = sp.symbols('M Lambda', positive=True)
F = 1 - 2*M/r - Lam*r**2/3
x = [t, r, thh, phh]
g = sp.diag(-F, 1/F, r**2, r**2*sp.sin(thh)**2)
gi = g.inv()
n = 4
Gam = [[[sp.simplify(sum(gi[a_, d]*(sp.diff(g[d, b_], x[c_]) + sp.diff(g[d, c_], x[b_])
         - sp.diff(g[b_, c_], x[d])) for d in range(n))/2) for c_ in range(n)] for b_ in range(n)]
       for a_ in range(n)]
def Riem(a_, b_, c_, d_):
    return sp.simplify(sp.diff(Gam[a_][b_][d_], x[c_]) - sp.diff(Gam[a_][b_][c_], x[d_])
                       + sum(Gam[a_][c_][e]*Gam[e][b_][d_] - Gam[a_][d_][e]*Gam[e][b_][c_]
                             for e in range(n)))
Rm = [[[[Riem(a_, b_, c_, d_) for d_ in range(n)] for c_ in range(n)] for b_ in range(n)]
      for a_ in range(n)]
Ric = sp.Matrix(n, n, lambda b_, d_: sp.simplify(sum(Rm[a_][b_][a_][d_] for a_ in range(n))))
check("5a. SdS: R_ab = Lambda g_ab", sp.simplify(Ric - Lam*g) == sp.zeros(4))
kr = sp.Matrix([1/F, 1, 0, 0])                 # radial null
check("5b. radial null: R_kk = 0 (null focusing blind to Lambda)", sp.simplify((kr.T*Ric*kr)[0]) == 0)
ut = sp.Matrix([1/sp.sqrt(F), 0, 0, 0])        # static timelike
check("5c. static timelike: R_uu = -Lambda (Lambda defocuses flow-bearing congruences)",
      sp.simplify((ut.T*Ric*ut)[0] + Lam) == 0)
# Weyl^2 = Kretschmann - 2 Ric^2 + R^2/3
Rdown = [[[[sp.simplify(sum(g[a_, e]*Rm[e][b_][c_][d_] for e in range(n))) for d_ in range(n)]
           for c_ in range(n)] for b_ in range(n)] for a_ in range(n)]
Kret = 0
for a_ in range(n):
    for b_ in range(n):
        for c_ in range(n):
            for d_ in range(n):
                if Rdown[a_][b_][c_][d_] != 0:
                    Kret += Rdown[a_][b_][c_][d_]**2 * gi[a_, a_]*gi[b_, b_]*gi[c_, c_]*gi[d_, d_]
Kret = sp.simplify(Kret)
Ric2 = sp.simplify(sum(Ric[i, j]**2*gi[i, i]*gi[j, j] for i in range(n) for j in range(n)))
Rs = sp.simplify(sum(gi[i, i]*Ric[i, i] for i in range(n)))
W2 = sp.simplify(Kret - 2*Ric2 + Rs**2/3)
check("5d. SdS Weyl^2 = 48 M^2/r^6: the tidal/shear part is Lambda-free", sp.simplify(W2 - 48*M**2/r**6) == 0)

# ---- 6. the seam breaks the corner's vacuum blindness -------------------------------------
A, B = sp.symbols('A B', positive=True)
nvec = sp.Matrix([1, 0, 0, 0])
n_dn = eta*nvec
gt = A*(eta + B*n_dn*n_dn.T)
check("6a. det g~ = A^4 (1-B) det g  =>  sqrt(-g~) = A^2 sqrt(1-B) sqrt(-g)",
      sp.simplify(gt.det() - A**4*(1 - B)*eta.det()) == 0)
# content-sector vacuum: T~^ab = -rho g~^ab. Seen at the fabric's null corner (k null for g):
rho = sp.symbols('rho', positive=True)
gti = sp.simplify(gt.inv())
kf = null(th, ph)
k_dn = eta*kf
proj = sp.simplify((k_dn.T*(-rho*gti)*k_dn)[0])
check("6b. content vacuum is NOT invisible at the fabric corner: -rho g~^ab k_a k_b != 0 for B != 0",
      sp.simplify(proj.subs(B, 0)) == 0 and sp.simplify(proj) != 0)
check("6c. ... and its visible part is rank-1 along n, = rho B/(A(1-B)) (n.k)^2",
      sp.simplify(proj - rho*B/(A*(1 - B))*((nvec.T*k_dn)[0])**2) == 0)

# ---- 7. gravitational-wave polarisations survive the seam --------------------------------------
# wave along z in the n-frame: transverse plane (x,y). TT tensors there stay TT under g~.
ep = sp.diag(0, 1, -1, 0)
ex = sp.zeros(4); ex[1, 2] = ex[2, 1] = 1
for e, nm in [(ep, "+"), (ex, "x")]:
    tr_g = sum((eta.inv()*e)[i, i] for i in range(4))
    tr_gt = sp.simplify(sum((gti*e)[i, i] for i in range(4)))
    check(f"7. {nm}-polarisation traceless under g and g~ (transverse block g~ = A g)",
          tr_g == 0 and tr_gt == 0)

print()
print(f"{sum(o for _, o in checks)}/{len(checks)} checks passed")
