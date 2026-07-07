"""
Verify, on a deliberately non-trivial metric:
 1. C^l_mn = Gamma~ - Gamma = (1/2) gt^{lr} (D_m h_rn + D_n h_rm - D_r h_mn),  h = B n x n, D = g-connection  (EXACT)
 2. det(gt) = (1-B) det(g)
 3. gt^{-1} = g^{-1} - B/(1-B) n^a n^b
 4. Kinematic decomposition D_m n_n = -n_m a_n + (theta/3) P_mn + sigma_mn + omega_mn
 5. Closed form of C in congruence variables:
    C^l_mn = n^l/(1-B) * [ (1/2)(DB_m n_n + DB_n n_m) + B((theta/3)P_mn + sigma_mn) ]
             - (1/2)(D^l B) n_m n_n  + (1/2) Bdot/(1-B) n^l n_m n_n     [via D^l B = DperpB^l - Bdot n^l]
             - B a^l n_m n_n + B (n_n omega_m^l + n_m omega_n^l)
    (form derived by hand below; sympy is the referee)
"""
import sympy as sp

t, x, y, z = sp.symbols('t x y z', real=True)
X = [t, x, y, z]
f = sp.Function('f', positive=True)(t, x)   # lapse^2
p = sp.Function('p', positive=True)(t, x)
q = sp.Function('q', positive=True)(t, x)
r = sp.Function('r', positive=True)(t, x)
w = sp.Function('w')(t, x)                  # t-y cross term -> vorticity
B = sp.Function('B')(t, x)

g = sp.Matrix([[-f, 0, w, 0],
               [0,  p, 0, 0],
               [w,  0, q, 0],
               [0,  0, 0, r]])
ginv = g.inv()

# unit timelike n ~ d_t  (n^m = f^{-1/2} delta^m_0);  g(n,n) = g_tt/f = -1
nu = sp.Matrix([1/sp.sqrt(f), 0, 0, 0])          # n^mu
nl = g * nu                                       # n_mu = (-sqrt f, 0, w/sqrt f, 0)
assert sp.simplify((nu.T*g*nu)[0]) == -1

h = B * nl * nl.T
gt = g + h
gtinv = gt.inv()

def christoffel(gm, gmi):
    G = [[[0]*4 for _ in range(4)] for _ in range(4)]
    for l in range(4):
        for m in range(4):
            for n in range(4):
                G[l][m][n] = sp.simplify(sum(gmi[l, s]*(sp.diff(gm[s, m], X[n]) + sp.diff(gm[s, n], X[m]) - sp.diff(gm[m, n], X[s])) for s in range(4))/2)
    return G

Gam  = christoffel(g, ginv)
Gamt = christoffel(gt, gtinv)

# ---- (2) determinant ----
print("det check:", sp.simplify(gt.det() - (1-B)*g.det()) == 0)

# ---- (3) inverse ----
print("inverse check:", sp.simplify(gtinv - (ginv - (B/(1-B)) * nu*nu.T)) == sp.zeros(4, 4))

# ---- covariant derivative of h with g-connection ----
def cov_d_02(T):  # T_{rn} -> D_m T_{rn}
    D = [[[0]*4 for _ in range(4)] for _ in range(4)]  # D[m][r][n]
    for m in range(4):
        for rr in range(4):
            for n in range(4):
                D[m][rr][n] = sp.diff(T[rr, n], X[m]) \
                    - sum(Gam[s][m][rr]*T[s, n] for s in range(4)) \
                    - sum(Gam[s][m][n]*T[rr, s] for s in range(4))
    return D

Dh = cov_d_02(h)

# ---- (1) exact C formula ----
ok = True
Cdir = [[[0]*4 for _ in range(4)] for _ in range(4)]
for l in range(4):
    for m in range(4):
        for n in range(4):
            Cdir[l][m][n] = sp.simplify(Gamt[l][m][n] - Gam[l][m][n])
            rhs = sum(gtinv[l, rr]*(Dh[m][rr][n] + Dh[n][rr][m] - Dh[rr][m][n]) for rr in range(4))/2
            if sp.simplify(Cdir[l][m][n] - rhs) != 0:
                ok = False
                print("MISMATCH C formula at", l, m, n)
print("C formula check (exact, all 40 components):", ok)

# ---- (4) kinematic decomposition ----
Dn = [[0]*4 for _ in range(4)]   # Dn[m][n] = D_m n_n
for m in range(4):
    for n in range(4):
        Dn[m][n] = sp.diff(nl[n], X[m]) - sum(Gam[s][m][n]*nl[s] for s in range(4))
Dn = sp.Matrix(Dn)

a_l = sp.Matrix([sp.simplify(sum(nu[m]*Dn[m, n] for m in range(4))) for n in range(4)])  # a_n = n^m D_m n_n
P = sp.simplify(g + nl*nl.T)                       # projector (lower)
Pud = sp.simplify(ginv*P)                          # P^m_n
theta = sp.simplify(sum((ginv*Dn)[m, m] for m in range(4)))
# full projection of D_m n_n
proj = sp.zeros(4, 4)
for m in range(4):
    for n in range(4):
        proj[m, n] = sum(Pud[al, m]*Pud[be, n]*Dn[al, be] for al in range(4) for be in range(4))
proj = sp.simplify(proj)
sigma = sp.simplify((proj + proj.T)/2 - theta*P/3)
omega = sp.simplify((proj - proj.T)/2)
recon = sp.simplify(-nl*a_l.T + theta*P/3 + sigma + omega - Dn)
print("kinematic decomposition check:", recon == sp.zeros(4, 4))
print("theta =", sp.simplify(theta))

# ---- (5) closed form of C ----
Bdot = sp.simplify(sum(nu[m]*sp.diff(B, X[m]) for m in range(4)))
dB = sp.Matrix([sp.diff(B, X[m]) for m in range(4)])           # D_m B (lower)
dBu = ginv*dB                                                  # D^m B
au = ginv*a_l
omega_ud = omega*ginv                                          # omega_m^l  (omega_{m s} g^{s l})

okc = True
for l in range(4):
    for m in range(4):
        for n in range(4):
            expr = (nu[l]/(1-B)) * (sp.Rational(1, 2)*(dB[m]*nl[n] + dB[n]*nl[m])
                                    + B*(theta*P[m, n]/3 + sigma[m, n])) \
                   - sp.Rational(1, 2)*dBu[l]*nl[m]*nl[n] \
                   + sp.Rational(1, 2)*(B/(1-B))*Bdot*nu[l]*nl[m]*nl[n] \
                   - B*au[l]*nl[m]*nl[n] \
                   + B*(nl[n]*omega_ud[m, l] + nl[m]*omega_ud[n, l])
            if sp.simplify(Cdir[l][m][n] - expr) != 0:
                okc = False
                print("closed-form mismatch at", l, m, n, sp.simplify(Cdir[l][m][n] - expr))
print("congruence closed-form check:", okc)

# ---- C = 0 theorem: Dh = 0  =>  B const and Dn = 0 (shown by contraction identities) ----
# n^r n^n D_m h_rn = D_m B  (uses n.n=-1, n^r D n_r =0):
lhs = sp.Matrix([sp.simplify(sum(nu[rr]*nu[n]*Dh[m][rr][n] for rr in range(4) for n in range(4)) - sp.diff(B, X[m])) for m in range(4)])
print("contraction identity n^r n^n D_m h_rn = D_m B:", sp.simplify(lhs) == sp.zeros(4, 1))
# -n^n D_m h_rn - (D_m B) n_r = B D_m n_r :
ok2 = True
for m in range(4):
    for rr in range(4):
        e = sp.simplify(-sum(nu[n]*Dh[m][rr][n] for n in range(4)) - sp.diff(B, X[m])*nl[rr] - B*Dn[m, rr])
        if e != 0:
            ok2 = False
print("contraction identity  -n^n D_m h_rn - (D_m B) n_r = B D_m n_r:", ok2)
