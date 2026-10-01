#!/usr/bin/env python3
"""
Is the cross-register cliff class non-generic?

The threshold T is pre-registered, so it can be used as a COORDINATE. Define

    cliff class := the functional form of r_c(eps),

the resource ratio at which the declared threshold eps is crossed, as a function
of eps. This is the only definition that uses what pre-registrability supplies;
exponents and knee widths at fixed eps do not.

Claim under test (a5 / CLAIMS engine row, generalised): one declared eps gives a
SHARED r_c(eps) form across registers, with register-specific coefficients only.

Registers, each with its own resource ratio:
  QEC            latency ratio r = tau_dec/tau_cyc
  erasure        duration tau at fixed work budget
  interferometry Delta tau / t_perp  (Zych two-level clock)
"""
import math, sympy as sp

eps = sp.symbols('eps', positive=True)

print("="*68)
print("1. QEC -- commit delay. Errors accrue in the uncorrected window.")
print("   LER(r) ~ L0 + p_phys * r    (linear accumulation, below backlog)")
L0, pph = sp.symbols('L0 p_phys', positive=True)
r_c_qec = sp.solve(sp.Eq(L0 + pph*sp.Symbol('r'), eps), sp.Symbol('r'))[0]
print(f"   r_c(eps) = {sp.simplify(r_c_qec)}")
print("   => LINEAR in eps.")
print("   (and near the backlog boundary the divergence is exponential, so this")
print("    register does not even have one class of its own)")

print("\n" + "="*68)
print("2. Erasure -- fixed work budget W0, demand failure prob <= eps.")
print("   W = kT[ln2 - H(p)] + B(p)/tau,   p = 1-eps")
kT, W0, B = sp.symbols('kT W0 B', positive=True)
p = 1-eps
H = -(p*sp.log(p) + eps*sp.log(eps))
count = kT*(sp.log(2) - H)
tau_c = B/(W0 - count)
ser = sp.series(sp.simplify(count), eps, 0, 2).removeO()
print(f"   kT[ln2 - H(1-eps)] = {sp.simplify(ser)}")
print(f"   tau_c(eps) = B / (W0 - that)")
print("   leading correction goes as  eps*log(eps)")
print("   => EPS*LOG(EPS), not a power law.")

print("\n" + "="*68)
print("3. Interferometry -- Zych two-level clock, V = |cos(pi.dtau/2.t_perp)|.")
print("   demand V >= 1 - eps")
x = sp.symbols('x', positive=True)
sol = sp.series(sp.acos(1-eps), eps, 0, 2).removeO()
print(f"   x <= arccos(1-eps) = {sp.simplify(sol)}")
print("   => SQRT(EPS).")

print("\n" + "="*68)
print("VERDICT")
print("""
  QEC            r_c ~ eps            (linear; exponential near backlog)
  erasure        tau_c ~ eps*log eps  (entropic)
  interferometry x_c  ~ sqrt(eps)     (quadratic optimum)

Three registers, three different eps-scalings. The generalised shared-class
claim is FALSE.

And it fails for a reason that also shows it was never non-generic: r_c(eps) is
read straight off the leading behaviour of whatever degradation function the
register happens to have.

  linear accumulation  -> linear
  entropic term        -> eps log eps
  quadratic maximum    -> sqrt

Any thresholded process returns the power its own Taylor expansion carries, so
the cliff's eps-scaling transports NO cross-register information. Even a match
would have been a coincidence of local analytic structure, not evidence of a
shared grammar.

SCOPE -- what this does and does not kill.
  killed:   the generalised version (any registers, any resource axes), which is
            the version the pre-registered-threshold argument was offered to
            support. Pre-registrability does not buy a cross-register constraint.
  survives: a5's actual bet as written in CLAIMS -- feedback-latency (thermo)
            vs decoder-latency (QEC). Both are control-loop delays and both are
            'error accrues during the uncorrected window', so a shared class
            there is plausible. But it is a SAME-AXIS comparison, and a shared
            class between two instances of the same mechanism is close to
            trivially true -- which makes it weak evidence for the grammar.
""")
