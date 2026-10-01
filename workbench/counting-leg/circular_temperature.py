"""Does the writer's diamond count predict how (non-)thermal it is? The circular test.

The massless Wightman function in 3+1 is -1/(4 pi^2 sigma), sigma the interval between writer
events; the 4D diamond count is V = (pi/24) sigma^2, so W ~ V^(-1/2): the detector response is a
Fourier transform of a function of the writer's diamond count.

Counting reading, sharpened:
  exact imaginary period of V(tau)     -> single temperature (KMS)          [linear, de Sitter]
  no period                            -> gap-dependent T_eff(E)            [circular]
  large-gap T_eff = 1 / y*, y* = distance from the real axis to the nearest zero of V(tau)
     (Fourier asymptotics: the nearest singularity sets the exponential tail)
For circular motion the nearest zero solves sinh(x)/x = 1/v, y* = 2 x gamma v / a, so in the
ultrarelativistic limit T_large -> a/(2 sqrt 3) = (pi/sqrt 3) * a/(2 pi).
The zero is a property of the interval, not of the field's propagator power, so the same large-gap
limit should hold in 2+1 (BEC-analogue dimension), where W ~ sigma^(-1/2).

Response formulas (stationary trajectories, switching-free, Louko-Satz / Hodgkinson-Louko):
  3+1:  F(E) = -E/(2 pi) Theta(-E) + 1/(2 pi^2) int_0^inf cos(E s) [1/s^2 - 1/sigma(s)] ds
  2+1:  F(E) = 1/4 - 1/(2 pi) int_0^inf sin(E s) / sqrt(sigma(s)) ds
"""
from mpmath import mp, mpf, sinh, sin, cos, sqrt, quadosc, log, pi, findroot, inf

mp.dps = 50
checks = []
def check(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)

def F31(E, sigma):
    def g(s):
        if s < mpf('1e-6'):                       # integrand is finite at 0; avoid 0/0
            s = mpf('1e-6')
        return cos(E*s)*(1/s**2 - 1/sigma(s))
    I = quadosc(g, [0, inf], omega=abs(E))
    return (-E/(2*pi) if E < 0 else 0) + I/(2*pi**2)

def F21(E, sigma):
    g = lambda s: sin(E*s)/sqrt(sigma(s)) if s > 0 else mpf(0)
    I = quadosc(g, [0, inf], omega=abs(E))
    return mpf(1)/4 - I/(2*pi)

def Teff(E, sigma, F):
    return E/log(F(-E, sigma)/F(E, sigma))

a = mpf(1)
# ---- 1. calibration: linear acceleration gives a/2pi at every gap ------------------------------
sig_lin = lambda s: 4*sinh(a*s/2)**2/a**2
for E in [mpf('0.5'), mpf('2')]:
    T = Teff(E, sig_lin, F31)
    print(f"   linear, 3+1, E={float(E)}: T_eff = {float(T):.5f}   a/2pi = {float(a/(2*pi)):.5f}")
    check(f"1. linear 3+1, E={float(E)}: T_eff = a/2pi", abs(T/(a/(2*pi)) - 1) < 1e-3)
T = Teff(mpf(1), sig_lin, F21)
check("1b. linear 2+1, E=1: T_eff = a/2pi (detailed balance; 2+1 statistics differ, ratio does not)",
      abs(T/(a/(2*pi)) - 1) < 1e-3)

# ---- 2. circular: gap-dependent, large-gap limit from the nearest zero of the count --------------
def circ(gamma):
    v = sqrt(1 - 1/gamma**2)
    gw = a/(gamma*v)                        # gamma * omega
    R = gamma**2*v**2/a
    sigma = lambda s: gamma**2*s**2 - 4*R**2*sin(gw*s/2)**2
    x = findroot(lambda x: sinh(x)/x - 1/v, mpf(1)/gamma*sqrt(3))
    ystar = 2*x*gamma*v/a
    return sigma, ystar, v

for gamma in [mpf(5), mpf(20)]:
    sigma, ystar, v = circ(gamma)
    T_pred = 1/ystar
    print(f"   circular gamma={float(gamma)}: nearest zero y* = {float(ystar):.4f}  -> T_large = {float(T_pred):.4f}"
          f"   (a/2pi = {float(a/(2*pi)):.4f}, a/(2 sqrt3) = {float(a/(2*sqrt(3))):.4f})")
    rows = []
    for E in [mpf('0.2'), mpf('1'), mpf('3'), mpf('8'), mpf('12')]:
        T3 = Teff(E, sigma, F31)
        T2 = Teff(E, sigma, F21)
        rows.append((E, T3, T2))
        print(f"      E={float(E):5.1f}:  T_eff(3+1) = {float(T3):.4f}   T_eff(2+1) = {float(T2):.4f}")
    check(f"2a. gamma={float(gamma)}: T_eff varies with the gap (no period -> no single temperature)",
          abs(rows[0][1] - rows[-1][1])/rows[-1][1] > 0.05)
    # extract y* from the two largest gaps, allowing for the prefactor power of the tail:
    #   3+1: pole of 1/sigma      -> ln[F(-E)/F(E)] = E y* + 1.0 ln E + c
    #   2+1: branch of sigma^-1/2 -> ln[F(-E)/F(E)] = E y* + 0.5 ln E + c
    (E1, T31, T21), (E2, T32, T22) = rows[-2], rows[-1]
    y31 = ((E2/T32 - E1/T31) - 1.0*(log(E2) - log(E1)))/(E2 - E1)
    y21 = ((E2/T22 - E1/T21) - 0.5*(log(E2) - log(E1)))/(E2 - E1)
    print(f"      y* extracted: 3+1 {float(y31):.4f}, 2+1 {float(y21):.4f}   nearest zero of the count: {float(ystar):.4f}")
    check(f"2b. gamma={float(gamma)}: 3+1 large-gap tail set by the count's nearest zero (1%)",
          abs(y31/ystar - 1) < 0.01)
    check(f"2c. gamma={float(gamma)}: 2+1 large-gap tail set by the same zero (2%): dimension-independent",
          abs(y21/ystar - 1) < 0.02)

# ---- 3. against the published ultrarelativistic asymptote ----------------------------------------
# Biermann et al. 2020 (PRD 102, 085006): F(E)/F(-E) ~ (a/(4 sqrt3 E)) exp(-2 sqrt3 E/a)
sigma, ystar, v = circ(mpf(20))
E = mpf(10)
lit = E/(2*sqrt(3)*E/a + log(4*sqrt(3)*E/a))
ours = Teff(E, sigma, F31)
print(f"   gamma=20, E=10: T_eff ours {float(ours):.5f}  vs published asymptote {float(lit):.5f};"
      f"  nearest zero 1/y* = {float(1/ystar):.5f} -> a/(2 sqrt3) = {float(a/(2*sqrt(3))):.5f}")
check("3. matches the published large-gap asymptote (0.5%), whose exponent 2 sqrt3/a is the "
      "ultrarelativistic nearest zero", abs(ours/lit - 1) < 0.005 and abs(ystar*a/(2*sqrt(3)) - 1) < 0.002)

print()
print(f"{sum(o for _, o in checks)}/{len(checks)} checks passed")
