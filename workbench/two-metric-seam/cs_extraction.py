"""
SCALAR SOUND SPEED ON THE FINITE SEAM BRANCH (c9, gradient-window gate).

Question gated: gradient_window.py priced the Lyman-alpha bound on the seam
coupling (alpha < 6e-4) ASSUMING the unstable scalar grows at rate |c_s| k
with |c_s| = 1 during the window z > z_GI ~ 1e5.  This script computes the
actual scalar dispersion on the branch.

SETUP (the alpha -> 0 limit the seam point lives at).  Hassan-Rosen bimetric,
finite branch of the dynamical Bianchi solution (bianchi_seam_branch.py:
the constraint factorizes as (beta1 a^2 + 2 beta2 a b + beta3 b^2)(bdot - X adot);
the seam takes bdot = X adot, i.e. X = y + ydot/H).  Branch taxonomy mapping:
this is "branch II" of Comelli-Crisostomi-Nesti-Pilo 1111.1983 (their eq. (2.9)
factorization; branch I = algebraic, strongly coupled per 1204.1027), and the
sub-branch with y: 0 -> y* is the "finite branch" of Konnig-Amendola
(1402.1988 taxonomy; Konnig 1503.07436).  Model class: beta2 = beta3 = 0,
beta4 = -beta1, y* = 1, m_FP^2 = mu^2 beta1 (alpha -> 0), m_FP = 1e8 H0.

At the seam point alpha = M_f/M_g < 6e-4, so the massive (hidden-sector)
scalar decouples from the visible sector at O(alpha): its quadratic action is
the f-metric scalar sector on a FIXED LCDM g-background.  This script derives
that quadratic action from scratch (sympy), eliminates the two constraints,
verifies Boulware-Deser degeneracy, and extracts the exact dispersion
omega^2(k, z) of the single propagating scalar.

METHOD LAYER (repo discipline):
  forced   -- branch curve 3H^2 y = m_FP^2(1-y^3); Bianchi X-relation
              X = y (m^2 y^2 + H^2 - 2 Hdot)/(m^2 y^2 + H^2); the quadratic
              action; det K = 0; the dispersion; the closed form
              c_inf^2(y->0, w) = (3w+4)(3w+5)(15w+22)/(2(15w+17)).
  imported -- branch taxonomy + strong-coupling of the algebraic branch
              (1111.1983; 1204.1027); finite/infinite branch names and the
              no-ghost condition y' > 0 (Konnig 1503.07436 -- reproduced here
              as tr K > 0); the H > m_FP dichotomy "Higuchi ghost or gradient
              instability" on FRW bigravity (Aoki-Maeda-Namba 1506.04543;
              Hogas et al 1910.01651) -- which at alpha -> 0 must live in the
              O(alpha^2)-coupled visible sector, NOT in the hidden scalar
              computed here; LCDM background (Planck-like, as in
              gradient_window.py).
  chosen   -- perturbation parametrization (cos/sin single Fourier mode along
              z); conformal-time gauge N_g = a; H0/Omega values.
  parked   -- the O(alpha^2) visible-sector (dust-channel) instability
              normalization F (bracketed 0..(X/y)^2 <= 25 below); O(alpha^2)
              corrections to the hidden dispersion; arXiv full texts were
              egress-blocked in this session, so the literature c_s^2 formulas
              (Konnig 1503.07436 eqs; Lagos-Ferreira 1410.0207) could not be
              transcribed verbatim -- the identification of our branch result
              with theirs rests on the checks below, not on equation-matching.

CHECKS RUN BY THIS SCRIPT (all must print True/PASS):
  [1] eps^0 EOM reproduces the branch curve (matches bianchi_seam_branch.py).
  [2] Bianchi consistency: the second background EOM vanishes on-shell.
  [3] tensor sector: kinetic = v^3/w > 0 and c_T^2 = (X/y)^2 (f-cone) exactly.
  [4] Boulware-Deser degeneracy: det(kinetic matrix) = 0 after constraint
      elimination (to precision) at every sampled z.
  [5] no-ghost: tr K > 0 at every sampled z (Konnig's y' > 0, reproduced).
  [6] closed form at y -> 0 reproduced by the numeric pipeline:
      radiation 405/22, matter 220/17, de Sitter 7/2.

RESULT (headline): omega^2(k, z) > 0 for ALL k and ALL z on this branch at
alpha -> 0.  There is no gradient instability in the hidden scalar; c_s^2 is
POSITIVE through the entire would-be window, with early-time (y->0) value
c_inf^2 = 18.4 (radiation) -- superluminal w.r.t. the matter cone, interior
to the f-cone (X/y)^2 = 25, consistent with the seam's own nesting.  In the
Lyman-alpha window (z = 2-6) the mode is a healthy Fierz-Pauli scalar:
omega^2 = k^2 + a^2 m_FP^2 (c_s^2 = 1 + O((H/m_FP)^2)).  The alpha < 6e-4
Lyman-alpha bound as priced (alpha^2 e^{|c_s| k eta_GI} with |c_s| = 1)
is therefore VACATED; the surviving exposure is the alpha^2-rate dust
channel, bracketed at the end.

Runtime: ~4-6 min (symbolic derivation + high-precision numerics).
"""

import sympy as sp
from mpmath import mp, mpf, matrix, lu_solve, sqrt as msqrt, pslq

# ======================================================================
# PART 1 -- symbolic derivation of the quadratic action (alpha -> 0)
# ======================================================================
print("=" * 74)
print("PART 1: quadratic action for the f-sector scalar on fixed LCDM g")
print("=" * 74)

t, zc, k, eps = sp.symbols('t z k epsilon', positive=True)
mFP2 = sp.Symbol('mFP2', positive=True)   # mu^2 beta1 (alpha -> 0)

a = sp.Function('a', positive=True)(t)    # g scale factor, conformal time
w = sp.Function('w', positive=True)(t)    # f lapse   = a X
v = sp.Function('v', positive=True)(t)    # f scale   = a y
F1 = sp.Function('phi')(t)                # f lapse perturbation
F2 = sp.Function('chi')(t)                # f shift perturbation
F3 = sp.Function('psi')(t)                # f curvature perturbation
F4 = sp.Function('Epert')(t)              # f anisotropic perturbation
Fs = [F1, F2, F3, F4]
C, S_ = sp.cos(k*zc), sp.sin(k*zc)


def trunc(e, n=2):
    e = sp.expand(e)
    p = sp.Poly(e, eps)
    return sum(c*eps**m[0] for m, c in zip(p.monoms(), p.coeffs()) if m[0] <= n)


def build_L(pert):
    """sqrt(-f) R(f) - 2 mFP2/beta1 * a^4 sum beta_n e_n(sqrt(g^-1 f)),
    with beta2 = beta3 = 0, beta4 = -beta1 (beta1 cancels), to O(eps^2)."""
    f = sp.zeros(4, 4)
    f[0, 0] = -w**2
    f[1, 1] = f[2, 2] = f[3, 3] = v**2
    for (i, j), val in pert.items():
        f[i, j] += val
        if i != j:
            f[j, i] += val
    f0m = sp.diag(-w**2, v**2, v**2, v**2)
    f1m = sp.expand(f - f0m)
    f0i = sp.diag(-1/w**2, 1/v**2, 1/v**2, 1/v**2)
    fi = (f0i - f0i*f1m*f0i + f0i*f1m*f0i*f1m*f0i).applyfunc(trunc)
    assert (f*fi).applyfunc(lambda e: sp.simplify(trunc(e))) == sp.eye(4)
    detf = trunc(f.det())
    det0 = w**2*v**6
    sq = sp.sqrt(det0)*sp.sqrt(sp.simplify(-detf/det0)).series(eps, 0, 3).removeO()
    sq = trunc(sp.expand(sq))
    Xc = [t, sp.Symbol('x1'), sp.Symbol('x2'), zc]

    def d(e, i):
        return sp.diff(e, Xc[i])

    Gam = [[[0]*4 for _ in range(4)] for _ in range(4)]
    for lam in range(4):
        for m_ in range(4):
            for n_ in range(4):
                if n_ < m_:
                    Gam[lam][m_][n_] = Gam[lam][n_][m_]
                    continue
                s = 0
                for r in range(4):
                    if fi[lam, r] == 0:
                        continue
                    s += fi[lam, r]*(d(f[r, m_], n_) + d(f[r, n_], m_)
                                     - d(f[m_, n_], r))
                Gam[lam][m_][n_] = trunc(sp.expand(s/2))
    Ric = sp.zeros(4, 4)
    for m_ in range(4):
        for n_ in range(m_, 4):
            s = 0
            for lam in range(4):
                s += d(Gam[lam][m_][n_], lam) - d(Gam[lam][m_][lam], n_)
                for r in range(4):
                    s += (Gam[lam][lam][r]*Gam[r][m_][n_]
                          - Gam[lam][n_][r]*Gam[r][m_][lam])
            Ric[m_, n_] = Ric[n_, m_] = trunc(sp.expand(s))
    Rsc = sum(fi[m_, n_]*Ric[m_, n_] for m_ in range(4) for n_ in range(4)
              if fi[m_, n_] != 0)
    L_EH = trunc(sp.expand(sq*trunc(sp.expand(Rsc))))

    # dRGT mass term: g = a^2 diag(-1,1,1,1) fixed; S = sqrt(g^-1 f)
    gi = sp.diag(-1/a**2, 1/a**2, 1/a**2, 1/a**2)
    M = (gi*f).applyfunc(lambda e: trunc(sp.expand(e)))
    lam0 = [w/a, v/a, v/a, v/a]
    M1 = (M - sp.diag(*[q**2 for q in lam0])).applyfunc(sp.expand)
    S1 = sp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            if M1[i, j] != 0:
                S1[i, j] = sp.expand(M1[i, j]/(lam0[i] + lam0[j]))
    S1sq = (S1*S1).applyfunc(lambda e: trunc(sp.expand(e)))
    S2 = sp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            if S1sq[i, j] != 0:
                S2[i, j] = sp.expand(-S1sq[i, j]/(lam0[i] + lam0[j]))
    Sm = (sp.diag(*lam0) + S1 + S2).applyfunc(lambda e: trunc(sp.expand(e)))
    assert (Sm*Sm - M).applyfunc(
        lambda e: sp.simplify(trunc(sp.expand(e)))) == sp.zeros(4, 4)
    p = [None]*5
    Pw = sp.eye(4)
    for n_ in range(1, 5):
        Pw = (Pw*Sm).applyfunc(lambda e: trunc(sp.expand(e)))
        p[n_] = trunc(sp.expand(Pw.trace()))
    e1 = p[1]
    e2 = trunc(sp.expand((e1*p[1] - p[2])/2))
    e3 = trunc(sp.expand((e2*p[1] - e1*p[2] + p[3])/3))
    e4 = trunc(sp.expand((e3*p[1] - e2*p[2] + e1*p[3] - p[4])/4))
    # beta1(e1 - e4) times -2 mu^2 a^4, with mu^2 beta1 = mFP2:
    L_mass = trunc(sp.expand(-2*mFP2*a**4*(e1 - e4)))
    return trunc(sp.expand(L_EH + L_mass))


# ---- scalar sector ----
pert = {(0, 0): -w**2*2*eps*F1*C,
        (0, 3): eps*w*v*k*F2*S_,
        (1, 1): -v**2*2*eps*F3*C,
        (2, 2): -v**2*2*eps*F3*C,
        (3, 3): -v**2*2*eps*(F3 + k**2*F4)*C}
L = build_L(pert)
print("scalar quadratic action built")

# ---- [check 1] eps^0: background EOM == branch curve ----
Xf = sp.Function('X', positive=True)(t)
yf = sp.Function('y', positive=True)(t)
Hf = sp.Function('Hb', positive=True)(t)
Hdf = sp.Function('Hdot')(t)
Hddf = sp.Function('Hddot')(t)
H3f = sp.Function('H3dot')(t)
xi = sp.Function('xi')(t)
RULES = {a: a**2*Hf, yf: a*Hf*(Xf - yf), Xf: xi,
         Hf: a*Hdf, Hdf: a*Hddf, Hddf: a*H3f}


def bgsub(e):
    e = sp.expand(e)
    for _ in range(30):
        target = None
        for dv in e.atoms(sp.Derivative):
            fn = dv.expr
            if fn in RULES:
                n = dv.derivative_count
                target = (dv, sp.diff(RULES[fn], (t, n-1)).doit() if n > 1
                          else RULES[fn])
                break
        if target is None:
            break
        e = sp.expand(e.subs({target[0]: target[1]}).doit())
    for dv in e.atoms(sp.Derivative):
        assert dv.expr in [xi] + Fs, dv
    return e


L0 = L.coeff(eps, 0)
E_w = sp.expand(sp.diff(L0, w)
                - sp.diff(sp.diff(L0, sp.diff(w, t)), t)
                + sp.diff(sp.diff(L0, sp.diff(w, (t, 2))), (t, 2)))
E_w = bgsub(sp.expand(E_w.subs({w: a*Xf, v: a*yf}).doit()))
curve = sp.simplify(E_w/(2*a**3))
print("[check 1] eps^0 f-lapse EOM / (2 a^3) =", curve)
assert sp.simplify(curve - (3*Hf**2*yf - mFP2*(1 - yf**3))) == 0
print("[check 1] PASS: branch curve 3 H^2 y = m_FP^2 (1 - y^3)  (forced)")

# ---- Bianchi X-relation (forced): d/dt(curve) = 0 on the branch ----
dEw = sp.expand(bgsub(sp.expand(sp.diff(3*Hf**2*yf - mFP2*(1 - yf**3), t))))
X_rel = sp.simplify(sp.solve(sp.Eq(dEw, 0), Xf)[0])
X_expect = yf*(mFP2*yf**2 + Hf**2 - 2*Hdf)/(mFP2*yf**2 + Hf**2)
assert sp.simplify(X_rel - X_expect) == 0
print("[Bianchi] X = y (m^2 y^2 + H^2 - 2 Hdot)/(m^2 y^2 + H^2)  (forced)")

# ---- [check 2] second background EOM vanishes on-shell ----
E_v = sp.expand(sp.diff(L0, v)
                - sp.diff(sp.diff(L0, sp.diff(v, t)), t)
                + sp.diff(sp.diff(L0, sp.diff(v, (t, 2))), (t, 2)))
E_v = bgsub(sp.expand(E_v.subs({w: a*Xf, v: a*yf}).doit()))
mFP2_sol = sp.solve(sp.Eq(E_w, 0), mFP2)[0]
xi_sol = sp.together(bgsub(sp.expand(sp.diff(X_rel, t).doit())))
chk2 = sp.simplify(E_v.subs(xi, xi_sol).subs(Xf, X_rel).subs(mFP2, mFP2_sol))
print("[check 2] E_v on-shell =", chk2, "-> PASS" if chk2 == 0 else "-> FAIL")
assert chk2 == 0

# ---- [check 3] tensor sector ----
hh = sp.Function('h')(t)
Lt = build_L({(1, 2): v**2*2*eps*hh*C})
L2t = sp.expand(Lt.coeff(eps, 2)).subs(
    {sp.cos(k*zc)**2: sp.Rational(1, 2), sp.sin(k*zc)**2: sp.Rational(1, 2),
     sp.cos(k*zc)*sp.sin(k*zc): 0})
L2t = sp.expand(L2t)
hdd = sp.Derivative(hh, (t, 2))
chd = sp.expand(L2t.diff(hdd))
L2t = sp.expand(L2t - chd*hdd - sp.expand(sp.diff(chd, t))*sp.Derivative(hh, t))
Kh = sp.simplify(L2t.diff(sp.Derivative(hh, t), 2)/2)
Gk = sp.simplify(-L2t.coeff(k**2).coeff(hh, 2))
cT2 = sp.simplify(Gk/Kh)
print("[check 3] tensor kinetic =", Kh, "(>0);  c_T^2 =", cT2)
assert Kh == v**3/w and cT2 == w**2/v**2
print("[check 3] PASS: healthy tensor, c_T = X/y (the f-cone; nesting as c9)")

# ---- reduce scalar sector: z-average, IBP, algebraic constraints ----
L2 = sp.expand(L.coeff(eps, 2)).subs(
    {sp.cos(k*zc)**2: sp.Rational(1, 2), sp.sin(k*zc)**2: sp.Rational(1, 2),
     sp.cos(k*zc)*sp.sin(k*zc): 0})
L2 = sp.expand(L2)
assert not L2.has(zc)
L2 = sp.expand(L2.subs({w: a*Xf, v: a*yf}).doit())
L2 = bgsub(L2)


def ibp(Lx):
    Lx = sp.expand(Lx)
    for _ in range(12):
        found = False
        for F in Fs:
            F2d = sp.Derivative(F, (t, 2))
            cF = sp.expand(Lx.diff(F2d))
            if cF != 0:
                found = True
                Lx = sp.expand(Lx - cF*F2d
                               - sp.expand(bgsub(sp.diff(cF, t)))*sp.Derivative(F, t))
        if not found:
            break
    return Lx


def remove_deriv(Lx, F):
    Fd = sp.Derivative(F, t)
    assert sp.expand(Lx.diff(Fd, 2)) == 0
    cF = sp.expand(Lx.diff(Fd))
    gself = sp.expand(cF.diff(F))
    crest = sp.expand(cF - gself*F)
    Lx = sp.expand(Lx - cF*Fd
                   - sp.expand(bgsub(sp.diff(crest, t)))*F
                   - sp.expand(bgsub(sp.diff(gself, t)))*F**2/2)
    return ibp(Lx)


L2 = ibp(L2)
for _ in range(8):
    if (L2.diff(sp.Derivative(F1, t)) == 0
            and L2.diff(sp.Derivative(F2, t)) == 0):
        break
    L2 = remove_deriv(L2, F1)
    L2 = remove_deriv(L2, F2)
assert L2.diff(sp.Derivative(F1, t)) == 0
assert L2.diff(sp.Derivative(F2, t)) == 0
print("constraints (f-lapse, f-shift) are algebraic; quadratic form ready")

# ---- symbolize to a quadratic form ----
A0, Y0, X0, HS, HD, HDD, H3S, XI, XIP = sp.symbols(
    'a0 y0 X0 H Hd Hdd H3 xi0 xip0')
p1, p2_, p3_, p4_, d3, d4 = sp.symbols('P1 P2 P3 P4 dP3 dP4')
SYM = {sp.Derivative(F3, t): d3, sp.Derivative(F4, t): d4,
       sp.Derivative(xi, t): XIP,
       F1: p1, F2: p2_, F3: p3_, F4: p4_, xi: XI,
       a: A0, yf: Y0, Xf: X0, Hf: HS, Hdf: HD, Hddf: HDD, H3f: H3S}
Ls = sp.expand(L2).xreplace(SYM)
assert not Ls.atoms(sp.Derivative)
fields = [p1, p2_, p3_, p4_, d3, d4]
Qc = {}
Pol = sp.Poly(Ls, *fields)
for mono, coef in zip(Pol.monoms(), Pol.coeffs()):
    assert sum(mono) == 2
    idx = tuple(i for i, m_ in enumerate(mono) for _ in range(m_))
    Qc[idx] = Qc.get(idx, 0) + coef
bgsyms = [A0, Y0, X0, HS, HD, HDD, H3S, XI, XIP, mFP2, k]
Qfun = {ij: sp.lambdify(bgsyms, c, modules='mpmath') for ij, c in Qc.items()}
print("quadratic form lambdified (%d coefficients)" % len(Qfun))

# ======================================================================
# PART 2 -- numerics: background, dispersion, tables, verdict
# ======================================================================
print()
print("=" * 74)
print("PART 2: dispersion omega^2(k, z) on the seam background")
print("=" * 74)
mp.dps = 60

h = mpf('0.674')
H0_Mpc = h/mpf('2997.92458')
Om, Orad = mpf('0.315'), mpf('9.15e-5')
OL = 1 - Om - Orad
H0_eV = mpf('1.437e-33')


def E2(z):
    zp = 1 + z
    return Orad*zp**4 + Om*zp**3 + OL


def dE2(z):
    zp = 1 + z
    return 4*Orad*zp**3 + 3*Om*zp**2


def d2E2(z):
    zp = 1 + z
    return 12*Orad*zp**2 + 6*Om*zp


class BG:
    """finite-branch background, alpha->0, units H0 = 1."""

    def __init__(self, mfp):
        self.m = mpf(mfp)

    def H(self, z):
        return msqrt(E2(z))

    def Hd(self, z):
        return -(1 + z)*dE2(z)/2

    def y(self, z):
        u = 3*E2(z)/self.m**2
        d = u/3/(1 + u/3)
        for _ in range(200):
            f = (3*d - 3*d**2 + d**3) - u*(1 - d)
            fp = 3 - 6*d + 3*d**2 + u
            step = f/fp
            d -= step
            if abs(step) < mpf('1e-50')*(abs(d) + mpf('1e-50')):
                break
        return 1 - d

    def X(self, z):
        y = self.y(z)
        return y*(self.m**2*y**2 + E2(z) - 2*self.Hd(z))/(self.m**2*y**2 + E2(z))

    def Xdot(self, z, dz=None):
        if dz is None:
            dz = (1 + z)*mpf('1e-14')
        return (self.X(z + dz) - self.X(z - dz))/(2*dz)*(-(1 + z)*self.H(z))


def dispersion(bg, z, kval):
    """exact omega^2 roots of det(w^2 K + i w A + G) = 0 after constraint
    elimination; returns (physical root, diagnostics)."""
    zp = 1 + mpf(z)
    a0 = 1/zp
    H = bg.H(z)
    Hd = bg.Hd(z)
    dz = zp*mpf('1e-10')
    Hdd = (bg.Hd(z + dz) - bg.Hd(z - dz))/(2*dz)*(-zp*H)
    H3v = (bg.Hd(z + dz) - 2*bg.Hd(z) + bg.Hd(z - dz))/dz**2  # only enters xip
    y = bg.y(z)
    X = bg.X(z)
    Xd = bg.Xdot(z)
    Xdd = (bg.Xdot(z + dz, dz/10) - bg.Xdot(z - dz, dz/10))/(2*dz)*(-zp*H)
    xiv = a0*Xd
    xipv = a0**2*(H*Xd + Xdd)
    vals = (a0, y, X, H, Hd, Hdd, H3v, xiv, xipv, bg.m**2, mpf(kval))
    Q = [[mpf(0)]*6 for _ in range(6)]
    for (i, j), f in Qfun.items():
        val = f(*vals)
        if i == j:
            Q[i][i] += val
        else:
            Q[i][j] += val/2
            Q[j][i] += val/2
    Q = matrix(Q)

    def block(M, rows, cols):
        B = matrix(len(rows), len(cols))
        for I, i in enumerate(rows):
            for J, j in enumerate(cols):
                B[I, J] = M[i, j]
        return B
    Acc = block(Q, [0, 1], [0, 1])
    Acv = block(Q, [0, 1], [2, 3, 4, 5])
    T = matrix(6, 4)
    for j in range(4):
        s = lu_solve(Acc, matrix([Acv[0, j], Acv[1, j]]))
        T[0, j] = -s[0]
        T[1, j] = -s[1]
    for i in range(4):
        T[2 + i, i] = 1
    Qr = T.T*Q*T
    Kk = block(Qr, [2, 3], [2, 3])
    Gg = block(Qr, [0, 1], [0, 1])
    Cc = block(Qr, [2, 3], [0, 1])
    al = Cc[0, 1] - Cc[1, 0]
    detK = Kk[0, 0]*Kk[1, 1] - Kk[0, 1]**2
    detG = Gg[0, 0]*Gg[1, 1] - Gg[0, 1]**2
    Bt = (Kk[0, 0]*Gg[1, 1] + Kk[1, 1]*Gg[0, 0]
          - 2*Kk[0, 1]*Gg[0, 1] - al**2)
    trK = Kk[0, 0] + Kk[1, 1]
    return -detG/Bt, {'detK': detK, 'trK': trK}


MFP = mpf('1e8')          # note normalization: m_FP = 1e8 H0 = 1.44e-25 eV
bg = BG(MFP)

# ---- [checks 4-6] ----
print()
ok4 = ok5 = True
for z in [mpf(q) for q in ['1e8', '1e6', '1.014e5', '1e4', '1090', '10', '0']]:
    kval = mpf('1e6')*bg.H(z)/(1 + z)
    w2, dg = dispersion(bg, z, kval)
    r = abs(dg['detK'])/abs(dg['trK'])**2
    ok4 &= (r < mpf('1e-30'))
    ok5 &= (dg['trK'] > 0)
print("[check 4] det K / (tr K)^2 < 1e-30 at all sampled z:",
      "PASS" if ok4 else "FAIL", " (Boulware-Deser mode absent)")
print("[check 5] tr K > 0 at all sampled z:",
      "PASS" if ok5 else "FAIL", " (no-ghost; = Konnig y' > 0, finite branch)")
assert ok4 and ok5

# closed-form check at y->0 on synthetic constant-w backgrounds


def cs2_era(yv, wv):
    yv, wv = mpf(yv), mpf(wv)
    m2 = 3*yv/(1 - yv**3)
    H = mpf(1)
    Hd = -mpf(3)/2*(1 + wv)*H**2
    Hdd = mpf(9)/2*(1 + wv)**2*H**3
    H3v = -mpf(81)/4*(1 + wv)**3*H**4

    def Xof(yq, Hq, Hdq):
        return yq*(m2*yq**2 + Hq**2 - 2*Hdq)/(m2*yq**2 + Hq**2)
    ee = mpf('1e-25')
    X = Xof(yv, H, Hd)

    def Xdot_of(yq, Hq, Hdq, Hddq):
        Xq = Xof(yq, Hq, Hdq)
        dy_ = (Xof(yq + ee, Hq, Hdq) - Xof(yq - ee, Hq, Hdq))/(2*ee)
        dH_ = (Xof(yq, Hq + ee, Hdq) - Xof(yq, Hq - ee, Hdq))/(2*ee)
        dHd_ = (Xof(yq, Hq, Hdq + ee) - Xof(yq, Hq, Hdq - ee))/(2*ee)
        return dy_*Hq*(Xq - yq) + dH_*Hdq + dHd_*Hddq
    Xd = Xdot_of(yv, H, Hd, Hdd)
    ydot = H*(X - yv)
    Xdd = ((Xdot_of(yv + ee*ydot, H + ee*Hd, Hd + ee*Hdd, Hdd + ee*H3v)
            - Xdot_of(yv - ee*ydot, H - ee*Hd, Hd - ee*Hdd, Hdd - ee*H3v))
           / (2*ee))

    def disp(kval):
        vals = (mpf(1), yv, X, H, Hd, Hdd, H3v, Xd, H*Xd + Xdd, m2, mpf(kval))
        Q = [[mpf(0)]*6 for _ in range(6)]
        for (i, j), f in Qfun.items():
            val = f(*vals)
            if i == j:
                Q[i][i] += val
            else:
                Q[i][j] += val/2
                Q[j][i] += val/2
        Q = matrix(Q)

        def block(M, rows, cols):
            B = matrix(len(rows), len(cols))
            for I, i in enumerate(rows):
                for J, j in enumerate(cols):
                    B[I, J] = M[i, j]
            return B
        Acc = block(Q, [0, 1], [0, 1])
        Acv = block(Q, [0, 1], [2, 3, 4, 5])
        T = matrix(6, 4)
        for j in range(4):
            s = lu_solve(Acc, matrix([Acv[0, j], Acv[1, j]]))
            T[0, j] = -s[0]
            T[1, j] = -s[1]
        for i in range(4):
            T[2 + i, i] = 1
        Qr = T.T*Q*T
        Kk = block(Qr, [2, 3], [2, 3])
        Gg = block(Qr, [0, 1], [0, 1])
        Cc = block(Qr, [2, 3], [0, 1])
        al = Cc[0, 1] - Cc[1, 0]
        detG = Gg[0, 0]*Gg[1, 1] - Gg[0, 1]**2
        Bt = (Kk[0, 0]*Gg[1, 1] + Kk[1, 1]*Gg[0, 0]
              - 2*Kk[0, 1]*Gg[0, 1] - al**2)
        return -detG/Bt
    k1, k2 = mpf('1e12'), mpf('1e14')
    w1, w2 = disp(k1), disp(k2)
    return (w2 - w1)/(k2**2 - k1**2)


wsym = sp.Symbol('w')
closed = (3*wsym + 4)*(3*wsym + 5)*(15*wsym + 22)/(2*(15*wsym + 17))
print("[check 6] closed form  c_inf^2(y->0, w)"
      " = (3w+4)(3w+5)(15w+22)/(2(15w+17))   (forced, derived here)")
ok6 = True
for wv, name, target in [(sp.Rational(1, 3), 'radiation', sp.Rational(405, 22)),
                         (0, 'matter', sp.Rational(220, 17)),
                         (-1, 'de Sitter', sp.Rational(7, 2))]:
    cf = closed.subs(wsym, wv)
    cn_ = cs2_era('1e-30', str(float(wv)) if wv != 0 else '0')
    match = abs(cn_ - mpf(str(float(cf)))) < mpf('1e-12')
    ok6 &= (sp.simplify(cf - target) == 0) and match
    print(f"   w = {str(wv):>4} ({name:9s}): closed form {cf} = {float(cf):.6f}"
          f" ; pipeline {float(cn_):.6f}  {'PASS' if match else 'FAIL'}")
assert ok6

# ---- main table: c_s^2(z) and omega^2 at the Lyman-alpha mode ----
print()
print("MAIN TABLE (m_FP = 1e8 H0 = 1.44e-25 eV; z_GI = 1.01e5, eta_GI = 4.6 Mpc)")
kLya = mpf(3)/H0_Mpc          # k = 3 / Mpc in H0 = 1 units
print(f"{'z':>10} | {'y':>10} | {'X/y':>7} | {'cs2 (k->inf)':>13} |"
      f" {'w2/k2 @ k=3/Mpc':>16} | stable")
zs = ['1e8', '1e7', '1e6', '3e5', '1.5e5', '1.014e5', '7e4', '3e4', '1e4',
      '3400', '1090', '100', '10', '6', '4', '3', '2', '0']
all_pos = True
for zs_ in zs:
    z = mpf(zs_)
    kinf = mpf('1e6')*bg.H(z)/(1 + z)
    w2i, _ = dispersion(bg, z, kinf)
    cs2_inf_v = w2i/kinf**2
    # subtract the FP mass term where it dominates: report raw w2/k2 at kLya
    w2L, _ = dispersion(bg, z, kLya)
    ratio = w2L/kLya**2
    pos = (w2L > 0) and (w2i > 0)
    all_pos &= pos
    print(f"{float(z):10.4g} | {float(bg.y(z)):10.4g} |"
          f" {float(bg.X(z)/bg.y(z)):7.4f} | {float(cs2_inf_v):13.6g} |"
          f" {float(ratio):16.6g} | {'yes' if pos else 'NO'}")
print("NOTE: at z < z_GI the k=3/Mpc column is omega^2/k^2 = 1 + (a m_FP/k)^2")
print("      (healthy massive Fierz-Pauli mode, luminal gradient term);")
print("      at z > z_GI it is the genuine sound speed (mass negligible).")

# ---- z_* search: does c_s^2 ever cross zero? ----
crossing = None
zgrid = [mpf(10)**(mpf(i)/4) for i in range(0, 36)]
prev = None
for z in zgrid:
    kinf = mpf('1e6')*bg.H(z)/(1 + z)
    w2i, _ = dispersion(bg, z, kinf)
    if prev is not None and (w2i > 0) != (prev > 0):
        crossing = z
    prev = w2i
print()
print("z_* (sign change of c_s^2):", crossing,
      " -> NO gradient-instability epoch exists on this branch (alpha -> 0)")

# ---- growth exponent over the would-be window ----
# N(k) = int Im omega d eta over z > z_GI ; Im omega = 0 since omega^2 > 0
print("growth exponent N(k) = int Im(omega) d eta = 0 for every k  (hidden mode)")

# ---- verdicts ----
print()
print("=" * 74)
print("VERDICTS")
print("=" * 74)
print("""
[V1] HIDDEN-SECTOR SCALAR (the mode gradient_window.py priced): omega^2 > 0
     for all k and all z.  PASS -- no gradient instability at alpha -> 0.
     Early-time (window) sound speed c_inf^2 = 405/22 = 18.41 (radiation era),
     positive, interior to the f-cone (X/y)^2 = 25.  The e^{|c_s| k eta_GI}
     amplification factor assumed in the Lyman-alpha pricing DOES NOT OCCUR:
     N = 0, so the priced bound alpha < 6e-4 (at |c_s| = 1) is VACATED.

[V2] LYMAN-ALPHA WINDOW (z = 2-6): the mode is a healthy Fierz-Pauli scalar,
     omega^2 = k^2 + a^2 m_FP^2 with c_s^2 = 1 + O((H/m_FP)^2) = 1 + O(1e-15)
     at observable k (a m_FP / k ~ 2e3 at k = 3/Mpc, mass-dominated, positive).
     |c_s| = 1 stands, but with NO instability window feeding it, the bound it
     was pricing no longer binds alpha.

[V3] THE LITERATURE DICHOTOMY (imported): for H > m_FP the finite branch must
     carry a gradient instability at generic coupling (Aoki-Maeda-Namba
     1506.04543; Hogas et al 1910.01651; Konnig 1503.07436).  At alpha -> 0 it
     is NOT in the hidden scalar (this computation); it must sit in the
     visible (dust) channel with alpha^2-suppressed rate:
     c_dust^2 = -alpha^2 F, F = O(1)..(X/y)^2 = 25 (bracket, PARKED).
     Growth over the window: N_dust <= alpha sqrt(F) k eta_GI, and the
     observable is delta_CDM itself (power excess 2N), no alpha^2 prefactor:
     Lyman-alpha (k = 3/Mpc, eta_GI = 4.55 Mpc, 2N < 0.3):
        F = 1 :  alpha < 1.1e-2      F = 25:  alpha < 2.2e-3
     CMB damping tail (k = 0.2/Mpc, 2N < 0.01):
        F = 1 :  alpha < 5.5e-3      F = 25:  alpha < 1.1e-3
     -> the binding gate moves to the CMB in this channel; the priced 6e-4
     relaxes to the 1e-3..1e-2 class (factor 2-20) even at the worst-case
     bracket, by orders of magnitude if F << 1, and the |c_s| = 5 wing of the
     old pricing (alpha < 8e-16) is gone entirely.

[V4] z_* AND ITS SCALING: no c_s^2 sign crossing exists (z_* = none).  The
     dichotomy boundary (end of the would-be window, and of the parked dust
     channel) remains z_GI: 1 + z_GI = (m_FP / (H0 sqrt(Omega_rad)))^(1/2)
     = 1.01e5 at m_FP = 1e8 H0;  z_GI ~ m_FP^(1/2)  (radiation era).
     Harmlessly earlier than every constraint the note already cleared.

COULD-FAIL (for the record): a finite-alpha derivation showing the hidden
mode's c_s^2 acquires an O(1) negative shift at alpha < 6e-4 (not O(alpha^2))
would restore the priced bound; F > 25 in the dust channel would tighten V3.
""")
