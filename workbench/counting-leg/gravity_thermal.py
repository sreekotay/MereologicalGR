"""Gravity and thermal metrology in the counting reading.

(1) 1+1 static writers: the second derivative of the writer's diamond count, V''(dt), is the
    conformal factor sampled at the diamond's corners. In Schwarzschild it has imaginary period
    2 pi i / kappa in Killing time -> Tolman's local temperature in the writer's own count; the
    writer's count deficit (local acceleration) differs from it except at the horizon.
(2) A thermometer moving through a bath: no imaginary period along its count -> no single
    temperature (the Planck/Ott 'transformation' question is malformed); its large-gap reading
    is set by the nearest singularity: the forward-Doppler temperature T sqrt((1+v)/(1-v)).
"""
import sympy as sp
import mpmath
from mpmath import mp, mpf, cos, coth, quadosc, log, pi, inf, sqrt as msqrt

checks = []
def check(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)

# ---- 1a. 1+1 diamond count of a static writer in a conformally flat metric ds^2 = f(-dt^2+dr*^2) --
dt, y, r0 = sp.symbols('dt y r0', real=True)
f = sp.Function('f')
V = sp.integrate((dt - 2*y)*(f(r0 + y) + f(r0 - y)), (y, 0, dt/2))
V2 = sp.simplify(sp.diff(V, dt, 2))
check("1a. V''(dt) = [f(r0* + dt/2) + f(r0* - dt/2)]/2: the count's curvature samples the corners",
      sp.simplify(V2 - (f(r0 + dt/2) + f(r0 - dt/2))/2) == 0)

# ---- 1b. Schwarzschild: f(r*) has imaginary period 4 pi i M in r*, so V'' has 2 pi i/kappa in dt ---
M = sp.symbols('M', positive=True)
rs = sp.symbols('rstar')
r_of = 2*M*(1 + sp.LambertW(sp.exp(rs/(2*M) - 1)))          # inverts r* = r + 2M ln(r/2M - 1)
fS = 1 - 2*M/r_of
val = lambda e: complex(sp.N(e.subs({M: 1, rs: sp.Rational(37, 10)})))
check("1b. f(r*) = 1 - 2M/r(r*) is periodic under r* -> r* + 4 pi i M",
      abs(val(fS.subs(rs, rs + 4*sp.pi*sp.I*M)) - val(fS)) < 1e-12)
kappa = 1/(4*M)
check("1c. hence V''(dt) has imaginary period 8 pi i M = 2 pi i / kappa in Killing time",
      sp.simplify(2*(4*sp.pi*sp.I*M) - 2*sp.pi*sp.I/kappa) == 0)

# ---- 1d. in the writer's own count tau = sqrt(f0) dt: Tolman; vs the deficit (local acceleration) --
r = sp.symbols('r', positive=True)
f0 = 1 - 2*M/r
T_loc = kappa/(2*sp.pi*sp.sqrt(f0))                         # period 2 pi sqrt(f0)/kappa in tau
a_loc = sp.diff(f0, r)/(2*sp.sqrt(f0))                      # static writer's proper acceleration
ratio = sp.simplify(T_loc/(a_loc/(2*sp.pi)))
check("1d. Tolman from the period: T_loc = kappa / (2 pi sqrt f)", True)
check("1e. period vs deficit: T_loc / (a/2pi) = r^2 / (4 M^2) -> equal only at the horizon",
      sp.simplify(ratio - r**2/(4*M**2)) == 0)

# ---- 1f. de Sitter and Rindler satisfy the same V'' reading ------------------------------------------
tau, a_, H = sp.symbols('tau a H', positive=True)
V_r = (sp.cosh(a_*tau) - 1)/a_**2                       # 2D Rindler diamond count
V_ds = 4/H**2*sp.log(sp.cosh(H*tau/2))                  # 2D de Sitter (counting_leg.py)
check("1f. Rindler V'' = cosh(a tau), dS V'' = 1/cosh^2(H tau/2): periods 2 pi i/a, 2 pi i/H",
      sp.simplify(sp.diff(V_r, tau, 2) - sp.cosh(a_*tau)) == 0
      and sp.simplify(sp.diff(V_ds, tau, 2) - 1/sp.cosh(H*tau/2)**2) == 0)

# ---- 2. thermometer moving through a bath --------------------------------------------------------
# massless scalar, temperature 1/beta: W = [coth(pi(r-t)/beta) + coth(pi(r+t)/beta)]/(8 pi beta r);
# along the writer t = gamma tau, r = gamma v tau. Thermal part dW = W - W_vac is regular on the axis.
mp.dps = 40
beta = mpf(1)
def response(E, v):
    g = 1/msqrt(1 - v**2)
    def dW(s):
        s = max(s, mpf('1e-4'))
        t, rr = g*s, g*v*s
        if v == 0:                                  # the r -> 0 limit
            return -1/(4*beta**2*mpmath.sinh(pi*t/beta)**2) + 1/(4*pi**2*t**2)
        W = (coth(pi*(rr - t)/beta) + coth(pi*(rr + t)/beta))/(8*pi*beta*rr)
        return W - 1/(4*pi**2*(rr**2 - t**2))
    I = quadosc(lambda s: cos(E*s)*dW(s), [0, inf], omega=abs(E))
    return (-E/(2*pi) if E < 0 else 0) + 2*I

def Teff(E, v):
    return E/log(response(-E, v)/response(E, v))

T_check = Teff(mpf(3), 0)
check("2a. calibration, writer at rest in the bath: T_eff = 1/beta", abs(T_check*beta - 1) < 1e-3)
v = mpf('0.6')
Ts = [(E, Teff(E, v)) for E in [mpf(1), mpf(4), mpf(10), mpf(16), mpf(22)]]
for E, T in Ts:
    print(f"   v=0.6, E={float(E):5.1f}: T_eff = {float(T):.4f}")
fwd = msqrt((1 + v)/(1 - v))/beta
print(f"   forward-Doppler T sqrt((1+v)/(1-v)) = {float(fwd):.4f};  1/beta = 1;  T/gamma = {float(msqrt(1-v**2)):.4f}")
check("2b. moving thermometer: T_eff depends on the gap (no period along its count; no single T)",
      abs(Ts[0][1] - Ts[-1][1])/Ts[-1][1] > 0.05)
# slope of ln ratio between the two largest gaps; the pole tail carries a power p: fit y*, p, c
(E1, T1), (E2, T2), (E3, T3) = Ts[-3:]
import mpmath
A = mpmath.matrix([[E1, log(E1), 1], [E2, log(E2), 1], [E3, log(E3), 1]])
b = mpmath.matrix([E1/T1, E2/T2, E3/T3])
ystar, p, c = mpmath.lu_solve(A, b)
print(f"   fitted tail: 1/y* = {float(1/ystar):.4f} (power p = {float(p):.2f})")
check("2c. large-gap reading = nearest singularity = forward-Doppler temperature (2%)",
      abs((1/ystar)/fwd - 1) < 0.02)

print()
print(f"{sum(o for _, o in checks)}/{len(checks)} checks passed")
