"""Which cone do detected gravitational waves ride in c9's realization? (side finding of R2)

c9 realizes the seam in singly-coupled Hassan-Rosen bigravity: matter on g (Planck mass M_g),
the seam metric f hidden (M_f = alpha M_g), f-cone wider. The C/D timing model
(two-metric-seam/verify_flrw_timing.py) puts photons on the content cone and GWs on the fabric
cone. Here: tensor modes of g and f, canonically normalised, high-k Fourier mode,

    omega^2 v = (k^2 C + M) v,   C = diag(1, c_f^2),
    M = m^2/(1+alpha^2) [[alpha^2, -alpha], [-alpha, 1]]       (massless + massive FP pair)

Matter sources the g-component. Report the eigenmode matter excites at LIGO k: its f-content
and its speed offset from the matter (photon) cone.
"""
from mpmath import mp, mpf, matrix, eig, sqrt

mp.dps = 80
checks = []
def check(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)

m_FP = mpf('1.4e-25')                         # eV (c9)
k = 2*mp.pi*100*mpf('6.582119569e-16')        # hbar*omega at f = 100 Hz, in eV (c = 1)
for alpha in [mpf('1e-3'), mpf('1e-2'), mpf('10'), mpf('1e3')]:   # alpha = M_f/M_g, both sides
    for B in [mpf('1e-16'), mpf('1e-2')]:     # today's seam; an early-time-sized seam for contrast
        cf2 = 1 + B
        M = (m_FP**2/(1 + alpha**2))*matrix([[alpha**2, -alpha], [-alpha, 1]])
        K = matrix([[k**2, 0], [0, k**2*cf2]]) + M
        E, ER = eig(K)
        # pick the eigenvector with the larger g-component
        best = max(range(2), key=lambda i: abs(ER[0, i])/sqrt(abs(ER[0, i])**2 + abs(ER[1, i])**2))
        vg, vf = ER[0, best], ER[1, best]
        frac_f = abs(vf)/sqrt(abs(vg)**2 + abs(vf)**2)
        speed_off = sqrt(E[best])/k - 1
        print(f"  alpha={float(alpha):.0e} B={float(B):.0e}:  f-content of matter-sourced mode "
              f"{float(frac_f):.2e},  (v - c_matter)/c = {float(speed_off):.2e},  fabric-cone offset "
              f"would be {float(sqrt(cf2) - 1):.2e}")
        check(f"alpha={float(alpha):.0e} B={float(B):.0e}: matter-sourced GW rides the matter cone "
              f"(offset < 1e-6 of the fabric offset)", abs(speed_off) < mpf('1e-6')*(sqrt(cf2) - 1))

print()
print(f"{sum(o for _, o in checks)}/{len(checks)} checks passed")
