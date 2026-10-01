"""Frequency scan of which_cone.py's two-mode model: where does the matter-sourced GW pick up
fabric-cone content in c9's singly-coupled realisation?

f-content ~ alpha m^2 / (k^2 B + m^2): suppressed while k^2 B >> m^2 (LIGO), saturating at ~alpha
below the crossover k* = m_FP / sqrt(B).
"""
from mpmath import mp, mpf, matrix, eig, sqrt

mp.dps = 80
hbar = mpf('6.582119569e-16')     # eV s
m = mpf('1.4e-25')
checks = []
def check(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)

def fcontent(f_hz, alpha, B):
    k = 2*mp.pi*f_hz*hbar
    M = (m**2/(1 + alpha**2))*matrix([[alpha**2, -alpha], [-alpha, 1]])
    K = matrix([[k**2, 0], [0, k**2*(1 + B)]]) + M
    E, ER = eig(K)
    i = max(range(2), key=lambda j: abs(ER[0, j])/sqrt(abs(ER[0, j])**2 + abs(ER[1, j])**2))
    return abs(ER[1, i])/sqrt(abs(ER[0, i])**2 + abs(ER[1, i])**2)

B = mpf('1e-16')
fstar = m/sqrt(B)/(2*mp.pi*hbar)
print(f"crossover f* = m_FP/(2 pi hbar sqrt(B)) = {float(fstar):.2e} Hz")
for alpha in [mpf('1e-3'), mpf('1e-2')]:
    print(f"alpha = {float(alpha):.0e}")
    for f_hz, band in [(100, "LIGO"), (1e-1, "DECIGO"), (1e-3, "LISA"), (1e-4, "LISA low"), (1e-8, "PTA")]:
        fc = fcontent(mpf(f_hz), alpha, B)
        print(f"   {band:9s} {f_hz:8.0e} Hz : fabric-cone content {float(fc):.2e}  (power {float(fc**2):.1e})")
    check(f"alpha={float(alpha):.0e}: LIGO-band content < 1e-9", fcontent(mpf(100), alpha, B) < mpf('1e-9'))
    check(f"alpha={float(alpha):.0e}: PTA-band content saturates at ~alpha",
          abs(fcontent(mpf('1e-8'), alpha, B)/alpha - 1) < mpf('0.1'))
check("crossover lies in the mHz (LISA) band", mpf('1e-4') < fstar < mpf('1e-2'))
print()
print(f"{sum(o for _, o in checks)}/{len(checks)} checks passed")
