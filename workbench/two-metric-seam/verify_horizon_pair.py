"""
Referee computation for the c5 wave-optics caveat on the two-temperature horizon pair.

PART A (symbolic, sympy):
 A1. Take g = Schwarzschild in ingoing Painleve-Gullstrand form, n = the radially
     infalling unit geodesic congruence (n_mu = -dt_PG: hypersurface-orthogonal,
     regular at the horizon -- c5's composite member).  Build gt = g + B n x n
     with constant B.  Show gt is EXACTLY Schwarzschild with
         rt_s = r_s / (1-B)
     under the constant rescaling t -> t/sqrt(1-B) (matter-sector time units).
     Cross-check: Ricci(gt) = 0 identically.
     => The matter field on gt sees one clean global Schwarzschild geometry.
        No structure of g pollutes it at ANY order in B (for this member);
        r = r_s is not a special locus of gt at all.  The "shell" is a
        two-metric comparison object; no single field's wave equation contains it.
 A2. Static-n control (c5's realization note): n ~ normalized d_t in static
     coordinates blows up at r = r_s; the fixed-n member cannot reach the horizon.
 A3. Surface gravities per sector, computed globally per metric:
         T_i = hbar c_i / (4 pi k_B r_{s,i}),  r_{s,i} = 2GM/c_i^2  (same G, M!)
     =>  T_i = hbar c_i^3 / (8 pi G M k_B)         -- the cube, exact
         T_m/T_f = (c_m/c_f)^3 = (1-B)^{3/2} = 1 - 3 eps + O(eps^2),  eps = B/2
     and the matter trapping radius rt_s = r_s(1 + 2 eps + O(eps^2)) -- both
     matching c5's quoted forms (matter-cold, radially outer, causally inner).

PART B (numeric): what wave optics makes of the shell, for M = 1 M_sun,
     Sgr A* (4.3e6 M_sun), M87* (6.5e9 M_sun):
     coordinate vs PROPER shell thickness (the caveat's 1/eps used coordinate
     thickness against asymptotic wavelength -- near-horizon proper thickness is
     ~ 2 r_s sqrt(2 eps), i.e. sqrt(eps)-small, not eps-small);
     peeling e-folds needed to tell the two kappas apart (1/eps) vs the
     sub-Planckian budget (~ln(r_s/l_P) ~ 90);
     statistical distinguishability of the two thermal channels
     (N ~ 1/eps^2 quanta; time vs Hubble time and evaporation time);
     the O(eps) inter-channel heat-mismatch entropy rate (k_B per yr);
     dispersive robustness margin (Corley-Jacobson class corrections ~ T_H/E_P
     vs the split eps).
"""
import sympy as sp

# ---------------------------------------------------------------- PART A
t, r, th, ph, rs, B = sp.symbols('t r theta phi r_s B', positive=True)
X = [t, r, th, ph]
v = sp.sqrt(rs / r)                      # PG infall velocity (c_f = 1 units)

# ingoing PG-Schwarzschild:  ds^2 = -(1-v^2)dt^2 + 2 v dt dr + dr^2 + r^2 dO^2
def pg_metric(vfun):
    return sp.Matrix([[-(1 - vfun**2), vfun, 0, 0],
                      [vfun,           1,    0, 0],
                      [0, 0, r**2,            0],
                      [0, 0, 0, r**2 * sp.sin(th)**2]])

g = pg_metric(v)
ginv = g.inv()

# n = infalling unit geodesic congruence: n_mu = -dt  (exact PG time covector)
nl = sp.Matrix([-1, 0, 0, 0])            # n_mu
nu = sp.simplify(ginv * nl)              # n^mu
assert sp.simplify((nl.T * ginv * nl)[0]) == -1          # unit timelike
assert sp.simplify(nu[1] + v) == 0                       # infalling: n^r = -v

gt = sp.simplify(g + B * nl * nl.T)      # gt = g + B n x n

# A1: rescale t = t' / sqrt(1-B); claim gt == PG-Schwarzschild with
#     rt_s = r_s/(1-B) and vt = sqrt(rt_s/r), in units where c_m = 1 for t'.
#     (substitute B = 1-u, u in (0,1), so sympy can resolve the radicals)
u = sp.symbols('u', positive=True)       # u = 1 - B
S = sp.diag(1/sp.sqrt(1 - B), 1, 1, 1)   # dt = dt'/sqrt(1-B)
gt_p = sp.simplify(S.T * gt * S)
vt = sp.sqrt((rs / (1 - B)) / r)
target = pg_metric(vt)
resid = sp.simplify((gt_p - target).subs(B, 1 - u))
print("A1 gt == Schwarzschild(rt_s = r_s/(1-B)) exactly:", resid == sp.zeros(4, 4))

def ricci(gm, coords):
    gmi = gm.inv()
    n = len(coords)
    Gam = [[[sp.simplify(sum(gmi[l, s]*(sp.diff(gm[s, m], coords[k])
                                        + sp.diff(gm[s, k], coords[m])
                                        - sp.diff(gm[m, k], coords[s]))
                             for s in range(n))/2)
             for k in range(n)] for m in range(n)] for l in range(n)]
    Ric = sp.zeros(n, n)
    for m in range(n):
        for k in range(n):
            Ric[m, k] = sp.simplify(
                sum(sp.diff(Gam[l][m][k], coords[l]) for l in range(n))
                - sum(sp.diff(Gam[l][m][l], coords[k]) for l in range(n))
                + sum(Gam[l][l][s]*Gam[s][m][k] for l in range(n) for s in range(n))
                - sum(Gam[l][k][s]*Gam[s][m][l] for l in range(n) for s in range(n)))
    return Ric

print("A1 Ricci(gt) = 0:", sp.simplify(ricci(gt, X)) == sp.zeros(4, 4))

# A2: static-n control -- n ~ d_t normalized in static Schwarzschild coords:
f = 1 - rs / r
n_static_norm = 1 / sp.sqrt(f)           # n^t = f^{-1/2} -> diverges at r_s
print("A2 static-n member diverges at horizon (n^t ~ (1-r_s/r)^{-1/2}):",
      sp.limit(n_static_norm, r, rs, '+') == sp.oo)

# A3: temperatures.  Static form of a PG metric with speed c and radius R:
#     T = hbar c / (4 pi k_B R).  Fabric: (c_f, r_s). Matter: gt is
#     Schwarzschild with radius rt_s = r_s/(1-B) in units c_m = c_f sqrt(1-B).
eps = sp.symbols('epsilon', positive=True)
ratio = sp.sqrt(1 - B) * (1 - B)         # (c_m/c_f) * (r_s/rt_s) = (1-B)^{3/2}
print("A3 T_m/T_f = (1-B)^(3/2):", sp.simplify(ratio - (1 - B)**sp.Rational(3, 2)) == 0)
print("A3 series in eps = B/2:  T_m/T_f =",
      sp.series((1 - 2*eps)**sp.Rational(3, 2), eps, 0, 2))
print("A3 rt_s/r_s =", sp.series(1/(1 - 2*eps), eps, 0, 2), " (matter horizon radially OUTER)")
# same-GM check: rt_s = r_s/(1-B) = (2GM/c_f^2)/(1-B) = 2GM/c_m^2  -- the cube:
cf, G_, M_ = sp.symbols('c_f G M', positive=True)
cm = cf * sp.sqrt(1 - B)
print("A3 rt_s == 2GM/c_m^2 (same G, M):",
      sp.simplify((2*G_*M_/cf**2)/(1 - B) - 2*G_*M_/cm**2) == 0)
print("A3 => T_i = hbar c_i^3 / (8 pi G M k_B): the cube is exact and global.")

# ---------------------------------------------------------------- PART B
import math
hbar, c, G, kB = 1.0546e-34, 2.9979e8, 6.674e-11, 1.3807e-23
Msun, lP = 1.989e30, 1.616e-35
t_hubble = 4.35e17                        # s (~13.8 Gyr)
epsn = 4e-16                              # C1 anchor scale

print("\n--- numbers (eps = %.0e) ---" % epsn)
for name, M in [("1 Msun", Msun), ("SgrA* 4.3e6", 4.3e6*Msun), ("M87* 6.5e9", 6.5e9*Msun)]:
    r_s = 2*G*M/c**2
    T_H = hbar*c**3/(8*math.pi*G*M*kB)
    dr_coord = 2*epsn*r_s                        # coordinate shell thickness
    s_proper = 2*r_s*math.sqrt(2*epsn)           # proper thickness ~ sqrt(eps)
    lam_peak = hbar*c/(kB*T_H)                   # ~ reduced thermal wavelength
    # photon-channel emission rate ~ L / (2.7 kB T), L = hbar c^6/(15360 pi G^2 M^2)
    L = hbar*c**6/(15360*math.pi*G**2*M**2)
    rate = L/(2.7*kB*T_H)                        # quanta / s (order of magnitude)
    N_dist = 1/epsn**2                           # quanta to split T vs T(1+eps)
    t_dist = N_dist/rate
    t_evap = 5120*math.pi*G**2*M**3/(hbar*c**4)
    dSdt = epsn*kB*rate                          # O(eps) channel heat-mismatch
    yr = 3.156e7
    print(f"{name:>12}: r_s={r_s:.2e} m  T_H={T_H:.2e} K  lam~{lam_peak:.1e} m")
    print(f"{'':>12}  shell: coord {dr_coord:.1e} m (lam/dr={lam_peak/dr_coord:.0e});"
          f" PROPER {s_proper:.2e} m (lam/s={lam_peak/s_proper:.0e})")
    print(f"{'':>12}  peeling e-folds to split kappas: 1/eps={1/epsn:.0e}"
          f" vs sub-Planckian budget ln(r_s/l_P)={math.log(r_s/lP):.0f}")
    print(f"{'':>12}  statistics: N=1/eps^2={N_dist:.0e} quanta @ {rate:.1e}/s"
          f" -> t={t_dist:.1e} s = {t_dist/yr:.1e} yr"
          f" = {t_dist/t_hubble:.0e} t_Hub; t_evap={t_evap/yr:.1e} yr"
          f" (within lifetime by 10^{math.log10(t_evap*yr/yr/t_dist):.0f})")
    print(f"{'':>12}  O(eps) entropy-mismatch rate: 1 k_B per {kB/dSdt/yr:.1e} yr;"
          f" dispersive margin: T_H/T_P ~ {T_H/1.42e32:.0e} << eps")
