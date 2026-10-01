"""4D Schwarzschild: does a static writer's diamond count carry the period 2 pi i / kappa?

Diamond between writer events p = (0, r0, axis) and q = (dt, r0, axis). The spacetime is static,
so J+(p) = {t >= T(x)} with T the first-arrival (Fermat / optical) time from the writer, and
J-(q) = {t <= dt - T(x)}. Hence, exactly,

    V(dt) = int d^3x sqrt(-g) (dt - 2 T(x))_+ ,     sqrt(-g) = r^2 sin(theta)

so every Lorentzian count is fixed by one static function, the optical distance T(x).

Split V into a near-horizon zone (r < r_c, inside the photon sphere) and the rest. The claim
under test: the near-horizon part of the count approaches its limit as a series in e^{-kappa dt}
with INTEGER harmonics (rates kappa, 2 kappa, ...), the same kappa for every writer. Integer
harmonics in real dt are the real-axis face of an imaginary period 2 pi i / kappa. Their source:
T(x) + r*(r) is analytic in (r - 2M) at the future horizon -- the horizon is a regular null
surface (the null corner), crossed at finite advanced time.

D(dt) := uncovered near-horizon weight (r_c = 2.5M) = int_{r<r_c} sqrt(-g) Theta(2T - dt) d^3x
       = 2 pi int sin(theta) [(r_lim^3 - 8M^3)/3] d(theta),   T(r_lim, theta) = dt/2.
"""
import numpy as np
import warnings
warnings.filterwarnings('ignore')
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import lambertw

checks = []
def check(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)

M = 1.0
kappa = 1/(4*M)
bc = 3*np.sqrt(3)*M
f = lambda r: 1 - 2*M/r
rstar = lambda r: r + 2*M*np.log(r/(2*M) - 1)
def r_of_rstar(rs):                       # r - 2M = 2M W(exp(r*/2M - 1)), precise when tiny
    return 2*M*(1 + lambertw(np.exp(rs/(2*M) - 1)).real)

def phi_ray(r, b, r0):
    """azimuth swept by an inward null ray (impact b < b_c) from r0 down to r."""
    g = lambda x: b/(x**2*np.sqrt(max(1 - b**2*f(x)/x**2, 1e-300)))
    pts = [3*M] if r < 3*M < r0 else None
    return quad(g, r, r0, points=pts, limit=400, epsabs=1e-13, epsrel=1e-12)[0]

def G_ray(r, b, r0):
    """t(r;b) = r0* - r*(r) + G: G is finite as r -> 2M (regular horizon crossing)."""
    g = lambda x: (1/np.sqrt(max(1 - b**2*f(x)/x**2, 1e-300)) - 1)/f(x)
    pts = [3*M] if r < 3*M < r0 else None
    return quad(g, r, r0, points=pts, limit=400, epsabs=1e-13, epsrel=1e-12)[0]

def b_of(r, theta, r0):
    return brentq(lambda b: phi_ray(r, b, r0) - theta, 0.0, bc*(1 - 1e-9), xtol=1e-15)

R_C = 2.5*M                               # near zone: inside the photon sphere

def r_lim(theta, half_dt, r0):
    """solve T(r, theta) = half_dt near the horizon, by fixed-point in r* (contraction: G is smooth).
    Requires the front to have passed r_c at this theta (checked by the caller's dt choice)."""
    b = b_of(R_C, theta, r0)
    assert rstar(r0) - rstar(R_C) + G_ray(R_C, b, r0) < half_dt, "front has not reached r_c"
    r = 2*M*(1 + 1e-12)
    for _ in range(6):
        b = b_of(max(r, 2*M*(1 + 1e-14)), theta, r0)
        rs = rstar(r0) + G_ray(r, b, r0) - half_dt
        r = r_of_rstar(rs)
    return r

def D(dt, r0, nth=24):
    xs, ws = np.polynomial.legendre.leggauss(nth)
    th = 0.5*np.pi*(xs + 1)*0.999 + 1e-4        # stay off the axis endpoints
    tot = 0.0
    for t_, w_ in zip(th, ws):
        rl = r_lim(t_, dt/2, r0)
        x = rl - 2*M
        tot += w_*np.sin(t_)*x*(rl**2 + 2*M*rl + 4*M**2)/3
    return 2*np.pi*tot*0.5*np.pi*0.999

results = {}
for r0 in [4.0, 6.0, 10.0]:
    dts = np.array([60.0, 72.0, 84.0, 96.0])
    Ds = np.array([D(dt, r0) for dt in dts])
    rates = -np.diff(np.log(Ds))/np.diff(dts)
    results[r0] = (dts, Ds, rates)
    a_loc = M/(r0**2*np.sqrt(f(r0)))
    print(f"   writer r0 = {r0}: near-horizon decay rates (Killing time) {np.round(rates, 6)}"
          f"   kappa = {kappa};  local acceleration a = {a_loc:.4f}")
    check(f"r0={r0}: near-horizon count decays at kappa in Killing time (1e-3)",
          abs(rates[-1]/kappa - 1) < 1e-3)

# integer harmonics: residual after the leading e^{-kappa dt} decays at kappa again (2 kappa total)
r0 = 6.0
dts = np.array([42.0, 45.0, 48.0, 51.0, 54.0, 57.0])
Ds = np.array([D(dt, r0) for dt in dts])
y = Ds*np.exp(kappa*dts)                   # -> c0 + c1 e^{-lambda dt}
d1 = np.diff(y)
lam = -np.diff(np.log(np.abs(d1)))/np.diff(dts[:-1])
print(f"   r0 = 6: subleading rates of D e^(kappa dt): {np.round(lam, 4)}  (integer harmonic -> kappa = {kappa})")
check("next harmonic is the next integer multiple: subleading rate = kappa (5%)",
      abs(lam[-1]/kappa - 1) < 0.05)

# Tolman and the dissociation, 4D
for r0 in [4.0, 6.0, 10.0]:
    T_loc = kappa/(2*np.pi*np.sqrt(f(r0)))
    a_loc = M/(r0**2*np.sqrt(f(r0)))
    print(f"   r0 = {r0}: rate in writer's own count kappa/sqrt(f) -> T_loc = {T_loc:.5f};"
          f"  a/2pi = {a_loc/(2*np.pi):.5f};  ratio = {T_loc/(a_loc/(2*np.pi)):.3f} = r0^2/4M^2 = {r0**2/4:.3f}")
check("writer-independent kappa in Killing time -> Tolman in own count; ratio to a/2pi = r0^2/4M^2",
      all(abs(results[r][2][-1]/kappa - 1) < 1e-3 for r in results))

# ---- contrast: zero temperature. Reissner-Nordstrom near-horizon count, 1+1 (V'' samples f at the
# inner corner, gravity_thermal.py 1a): sub-extremal -> exponential at kappa = (r+ - r-)/(2 r+^2);
# extremal -> power law (no exponential, no period, T = 0).
def rn_rate(Q, dts):
    """f at the inner corner of a writer-at-4M diamond, via the analytic tortoise coordinate."""
    rp = M + np.sqrt(M**2 - Q**2); rm = M - np.sqrt(M**2 - Q**2)
    if rp > rm:
        A = rp**2/(rp - rm); B = rm**2/(rp - rm)
        rs = lambda u: rp + np.exp(u) + A*u - B*np.log(rp + np.exp(u) - rm)       # u = ln(r - r+)
        fx = lambda u: np.exp(u)*(np.exp(u) + rp - rm)/(rp + np.exp(u))**2
        u0 = np.log(4*M - rp)
        return np.array([fx(brentq(lambda u: rs(u) - (rs(u0) - dt/2), -700, u0, xtol=1e-14)) for dt in dts])
    rs = lambda x: (M + x) + 2*M*np.log(x) - M**2/x                                 # x = r - M
    x0 = 3*M
    return np.array([(lambda x: x**2/(M + x)**2)(brentq(lambda x: rs(x) - (rs(x0) - dt/2), 1e-14, x0, xtol=1e-16))
                     for dt in dts])
dts_rn = np.array([60.0, 80.0, 100.0, 120.0])
sub = rn_rate(0.6, dts_rn)
kap_rn = (1.8 - 0.2)/(2*1.8**2)
rate_sub = -np.diff(np.log(sub))/np.diff(dts_rn)
ext = rn_rate(1.0, np.array([1e3, 1e4, 1e5, 1e6]))
slope_ext = np.diff(np.log(ext))/np.diff(np.log([1e3, 1e4, 1e5, 1e6]))
print(f"   RN Q=0.6: inner-corner count density decays at {np.round(rate_sub, 5)};  kappa = {kap_rn:.5f}")
print(f"   RN extremal: log-log slope {np.round(slope_ext, 3)}  (power law: no exponential, T = 0)")
check("sub-extremal RN: rate = kappa = (r+ - r-)/(2 r+^2)", abs(rate_sub[-1]/kap_rn - 1) < 1e-3)
check("extremal RN: power-law approach (slope -> -2), no exponential -> zero temperature",
      abs(slope_ext[-1] + 2) < 0.05)

print()
print(f"{sum(o for _, o in checks)}/{len(checks)} checks passed")
