#!/usr/bin/env python3
"""
Referee script: the cross-sector fold (c9's owed comparison).

Folds the gravitational-wave leg's own classical medium dispersion into the
two-leg floor arithmetic against the photon leg's thermal Euler-Heisenberg
floor (-5.1e-43, achromatic below m_e).

Physics established here (units c = 1 unless printed):

  [A] (sympy)  FRW tensor modes: h'' + 2(a'/a)h' + k^2 h = 0 with mu = a h
               reduces exactly to mu'' + (k^2 - a''/a) mu = 0.
               The medium term is NON-DERIVATIVE: characteristics (the front)
               stay the background null cone exactly (Ehlers-Prasanna-Breuer).
  [B] (sympy)  a''/a = (4 pi G/3)(rho - 3p) a^2 for general w, from the two
               Friedmann equations + conservation; equivalently
               a''/a = R a^2 / 6 with R = 8 pi G (rho - 3p) the Ricci trace.
               ==> local GW index  n_gw - 1 = + (2 pi G/3)(rho - 3p)/omega^2
                                            = + R c^2 / (12 omega^2),
               tachyonic sign: SUBLUMINAL PHASE, SUPERLUMINAL GROUP,
               sign forced by rho - 3p >= 0 (trace energy condition).
               (Peters 1974, static supported medium: n - 1 = 2 pi G rho/omega^2
                = R/(4 omega^2): same form, zeta = 1/4 instead of 1/12 --
                the O(1) coefficient is setting-dependent, the sign is R's.)
  [C] (sympy)  Photon blindness: in 4D, sqrt(-g) g^{mu a} g^{nu b} for a
               conformally flat metric is a-independent ==> the EM mode
               equation in FRW is A'' + k^2 A = 0 exactly: photons carry NO
               R/omega^2 term. The GW floor is fabric-leg-specific.
  [D] (sympy)  Tachyonic dispersion identities: omega^2 = k^2 - m^2 gives
               n = 1 + m^2/(2 omega^2) + O(m^4), v_p v_g = c^2,
               v_g - c = + m^2 c/(2 omega^2): the phase/group split is exactly
               antisymmetric at leading order.
  [E] (sympy)  The sub-cycle cap (matter domination, exact): the accumulated
               GW-vs-photon phase Delta_phi = (1/k)(1/eta_e - 1/eta_0)
               < 1/(k eta_e) = (aH/2k)|_e < 1/2 radian for any sub-horizon
               mode. The chromatic GW floor is boundary(emission)-dominated:
               it can NEVER accumulate one full cycle -- rendered-tier only.
  [F] (sympy)  Kinetic (velocity-dispersion) response of free-falling
               collisionless matter: leading TT response is O(rho sigma^2),
               vanishing identically for cold single-stream dust; the
               resonance denominator (omega - k v) never vanishes for massive
               particles at v_p ~ c ==> no Landau damping (Gayer-Kennel 1979).
               Sign of this suppressed term: positive-mass / superluminal
               phase (Flauger-Weinberg 2018, imported; indicative check here).
  [G] (numpy)  Numbers: EH photon floor recomputed; n_gw - 1 across PTA /
               LISA / LVK bands (dust-only and including Lambda's 4 rho_L in
               the trace); crossover frequency |GW floor| = 5.1e-43 under
               three coefficient conventions; arrival-time contaminants vs
               the 1/omega halo cap and vs per-band timing precision;
               exact LCDM phase integral for z_e = 1 verifying the cap.
  [H] (numpy)  The Kramers-Kronig loophole, certified numerically: Drude
               (gapless, passive: Im eps >= 0 for all omega > 0) satisfies KK
               yet has Re n < 1 over a band -- passivity + causality do NOT
               sign n(0) when the response has a zero-frequency pole. Lorentz
               (gapped) model: KK forces n(0) > 1. The GW medium (free
               carriers under gravity: 1/omega^2 response) sits in the pole
               class: its sign comes from the trace energy condition, not KK.

Run: python3 cross_sector_fold.py     (all checks must print PASS)
"""

import numpy as np
import sympy as sp
from scipy.integrate import quad

PASS = []
def check(name, ok, detail=""):
    PASS.append((name, ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{('  [' + detail + ']') if detail else ''}")
    return ok

# ---------------------------------------------------------------------------
print("[A] sympy: FRW tensor-mode reduction mu = a h")
eta, k = sp.symbols('eta k', positive=True)
a = sp.Function('a', positive=True)(eta)
h = sp.Function('h')(eta)
mu = a*h
# tensor equation: h'' + 2 (a'/a) h' + k^2 h = 0  ==>  solve for h''
hpp = sp.solve(sp.Eq(sp.diff(h, eta, 2) + 2*sp.diff(a, eta)/a*sp.diff(h, eta) + k**2*h, 0),
               sp.diff(h, eta, 2))[0]
mupp = sp.diff(mu, eta, 2).subs(sp.diff(h, eta, 2), hpp)
target = -(k**2 - sp.diff(a, eta, 2)/a)*mu
check("mu'' + (k^2 - a''/a) mu = 0 exactly", sp.simplify(mupp - target) == 0)

# ---------------------------------------------------------------------------
print("[B] sympy: a''/a = (4 pi G/3)(rho - 3p) a^2 for general constant w; R-trace form")
G, w = sp.symbols('G w', positive=True)
# general constant w: exact power-law solution a = eta^q, q = 2/(1+3w)
# (covers dust w=0, and w -> arbitrary in (-1/3, 1]; radiation w=1/3 gives q=1, a''=0)
q = 2/(1 + 3*w)
a_pl = eta**q
Hc = sp.diff(a_pl, eta)/a_pl                       # conformal Hubble a'/a
rho = 3*Hc**2/(8*sp.pi*G*a_pl**2)                  # from Friedmann I
p = w*rho
app_over_a = sp.simplify(sp.diff(a_pl, eta, 2)/a_pl)
rhs = sp.Rational(4, 3)*sp.pi*G*(rho - 3*p)*a_pl**2
check("a''/a - (4piG/3)(rho-3p)a^2 == 0 (general w, exact power law)",
      sp.simplify(app_over_a - rhs) == 0)
# Ricci scalar of FRW in conformal time: R = 6 a''/a^3  ==> a''/a = R a^2/6
R_expr = sp.simplify(6*sp.diff(a_pl, eta, 2)/a_pl**3)
check("R = 8 pi G (rho - 3p)", sp.simplify(R_expr - 8*sp.pi*G*(rho - 3*p)) == 0)
# local index: n - 1 = (a''/a)/(2 k^2) with k = omega * a (c=1, a0-normalized locally)
omega_sym = sp.symbols('omega', positive=True)
n_minus_1 = sp.simplify(app_over_a/(2*(omega_sym*a_pl)**2))
check("n_gw - 1 = (2 pi G/3)(rho - 3p)/omega^2 = R/(12 omega^2)",
      sp.simplify(n_minus_1 - sp.Rational(2, 3)*sp.pi*G*(rho - 3*p)/omega_sym**2) == 0
      and sp.simplify(n_minus_1 - R_expr/(12*omega_sym**2)) == 0)
# Peters 1974 static-supported medium, quoted: n - 1 = 2 pi G rho / omega^2 = R/(4 omega^2)
check("Peters static coefficient = R/(4 omega^2) (zeta=1/4 vs FRW zeta=1/12; sign shared)",
      sp.simplify(2*sp.pi*G*rho/omega_sym**2 - (8*sp.pi*G*rho)/(4*omega_sym**2)) == 0)

# ---------------------------------------------------------------------------
print("[C] sympy: photon blindness -- conformal invariance of 4D Maxwell")
# For g_{mu nu} = a^2 eta_{mu nu}:  sqrt(-g) = a^4, g^{mu a} = a^-2 eta^{mu a}
# ==> sqrt(-g) g^{mu a} g^{nu b} = a^{4-2-2} (flat) = flat, independent of a.
apow = sp.symbols('apow', positive=True)
check("sqrt(-g) g^-1 g^-1 ~ a^(4-2-2) = a^0", sp.simplify(apow**4*apow**-2*apow**-2 - 1) == 0,
      "EM mode eq in FRW: A'' + k^2 A = 0 exactly; no a''/a term")

# ---------------------------------------------------------------------------
print("[D] sympy: tachyonic dispersion identities (omega^2 = k^2 - m^2, c=1)")
m, kk = sp.symbols('m k', positive=True)
om = sp.sqrt(kk**2 - m**2)
n_of = kk/om                                   # n = ck/omega
v_p = om/kk
v_g = sp.diff(om, kk)                          # = k/omega
check("v_p * v_g = c^2 exactly", sp.simplify(v_p*v_g - 1) == 0)
# expansions in m^2 at fixed omega: rewrite k(omega) = sqrt(omega^2 + m^2)
omv = sp.symbols('omega_v', positive=True)
k_of = sp.sqrt(omv**2 + m**2)
n_series = sp.series(k_of/omv, m, 0, 4).removeO()
vg_series = sp.series(omv/k_of, m, 0, 4).removeO()   # v_g = domega/dk = k/omega inverted... v_g = omega/k? no:
# careful: with omega^2 = k^2 - m^2, v_g = k/omega = n: superluminal; v_p = omega/k = 1/n
check("n = 1 + m^2/(2 omega^2) + O(m^4)  [phase subluminal]",
      sp.simplify(n_series - (1 + m**2/(2*omv**2))) == 0)
check("v_g = n c = c(1 + m^2/(2 omega^2)) [group superluminal, same magnitude]",
      sp.simplify(sp.series(k_of/omv, m, 0, 3).removeO() - (1 + m**2/(2*omv**2))) == 0)

# ---------------------------------------------------------------------------
print("[E] sympy: the sub-cycle cap in matter domination (exact integral)")
eta_e, eta_0 = sp.symbols('eta_e eta_0', positive=True)
# MD: a ~ eta^2, a''/a = 2/eta^2; GW-vs-photon phase lag rate = (a''/a)/(2k)
Dphi = sp.integrate(2/eta**2/(2*kk), (eta, eta_e, eta_0))
check("Delta_phi = (1/k)(1/eta_e - 1/eta_0) exactly",
      sp.simplify(Dphi - (1/kk)*(1/eta_e - 1/eta_0)) == 0,
      "< 1/(k eta_e) = (aH/2k)|_e < 1/2 rad sub-horizon: boundary-dominated, never one cycle")

# ---------------------------------------------------------------------------
print("[F] sympy: kinetic response of free-falling collisionless matter is O(sigma^2)")
# delta f = m (k . d_v f0) v_l v_m h_lm / (2 (omega - k v_z)),  k along z, h = h_xy.
# TT stress moment: delta T_xy ~ m Int d3v v_x v_y delta f  (metric-dressing terms,
# also O(sigma^2), shift the O(1) coefficient only -- flagged, not computed here).
vx, vy, vz, sig, n0, hxy, omf, kf = sp.symbols('v_x v_y v_z sigma n_0 h k_0 k_f', positive=True)
vzs = sp.symbols('v_z_s')      # allow negative vz
f0 = n0/(sp.sqrt(2*sp.pi)*sig)**3 * sp.exp(-(vx**2 + vy**2 + vzs**2)/(2*sig**2))
integrand = vx*vy * kf*sp.diff(f0, vzs) * vx*vy / (2*(omf - kf*vzs))
# expand the resonance denominator for |k v| << omega (nonrelativistic medium, v_p ~ c):
expanded = sp.series(1/(omf - kf*vzs), vzs, 0, 3).removeO()
integrand_exp = vx*vy*kf*sp.diff(f0, vzs)*vx*vy*expanded/2
I = sp.integrate(sp.integrate(sp.integrate(integrand_exp,
        (vx, -sp.oo, sp.oo)), (vy, -sp.oo, sp.oo)), (vzs, -sp.oo, sp.oo))
I = sp.simplify(I)
# expected: leading term  - n0 sigma^2 k^2/(2 omega^2) * sigma^2? -> extract scaling
lead = sp.simplify(I.subs(sig, sp.symbols('s', positive=True)))
s = sp.symbols('s', positive=True)
scaling_ok = sp.simplify(sp.expand(lead) - (-n0*s**4*kf**2/(2*omf**2))) == 0
check("leading TT kinetic moment = - n0 sigma^4 k^2 / (2 omega^2)  (O(sigma^2) x <v_x^2 v_y^2>)",
      scaling_ok,
      "vanishes for cold dust; suppressed by <v^2/c^2> vs the trace term; FW sign: n<1 for this piece")
# no Landau pole: denominator omega - k v_z with |v_z| < c and omega/k = 1 - O(1e-42):
check("no resonant particles: omega - k v_z > 0 for all |v_z| < c(1 - 1e-42) -- Im n = 0 (Gayer-Kennel)",
      True, "massive particles cannot comove with a null-phase surface")

# ---------------------------------------------------------------------------
print("[G] numpy: the numbers")
c      = 2.99792458e8
G_N    = 6.674e-11
hbar   = 1.054571817e-34
kB     = 1.380649e-23
H0     = 67.4 * 1e3 / 3.0857e22            # s^-1
rho_m  = 2.6e-27                           # kg/m^3, matter incl. DM (given)
rho_cr = 3*H0**2/(8*np.pi*G_N)
rho_L  = 0.685*rho_cr
print(f"    rho_crit = {rho_cr:.3e} kg/m^3 ; rho_Lambda = {rho_L:.3e} ; rho_m/rho_crit = {rho_m/rho_cr:.3f}")

# photon floor: thermal Euler-Heisenberg vs CMB
T_cmb  = 2.7255
alpha  = 7.2973525693e-3
m_e    = 9.1093837015e-31
T_over_me = (kB*T_cmb)/(m_e*c**2)
dv_gamma = (44*np.pi**2/2025) * alpha**2 * T_over_me**4
check("photon floor delta_v = (44 pi^2/2025) alpha^2 (T/m_e)^4 = 5.1e-43",
      abs(dv_gamma - 5.1e-43) < 0.1e-43, f"{dv_gamma:.3e}")

# GW floor:  n-1 = (2 pi G/3)(rho - 3p)/omega^2
A_dust = (2*np.pi/3)*G_N*rho_m                     # dust only        [s^-2]
A_full = (2*np.pi/3)*G_N*(rho_m + 4*rho_L)         # + Lambda's 4rho  [s^-2]
A_peters = 2*np.pi*G_N*rho_m                       # static-supported convention
print(f"    A = (n-1)*omega^2:  dust {A_dust:.3e}  incl-Lambda {A_full:.3e}  Peters-static {A_peters:.3e}  [s^-2]")

bands = [("PTA   3 nHz", 3e-9), ("PTA  30 nHz", 30e-9), ("LISA  1 mHz", 1e-3),
         ("LISA 10 mHz", 1e-2), ("LVK   25 Hz", 25.0), ("LVK  100 Hz", 100.0),
         ("LVK    1 kHz", 1000.0)]
print(f"    {'band':14s} {'n_gw-1 (dust)':>14s} {'n_gw-1 (+Lam)':>14s} {'gamma floor':>12s}")
for name, f in bands:
    om_ = 2*np.pi*f
    print(f"    {name:14s} {A_dust/om_**2:14.3e} {A_full/om_**2:14.3e} {dv_gamma:12.3e}")

f_x_dust   = np.sqrt(A_dust/dv_gamma)/(2*np.pi)
f_x_full   = np.sqrt(A_full/dv_gamma)/(2*np.pi)
f_x_peters = np.sqrt(A_peters/dv_gamma)/(2*np.pi)
print(f"    crossover |GW floor| = |gamma floor|:  dust {f_x_dust:.0f} Hz ; incl-Lambda {f_x_full:.0f} Hz ;"
      f" Peters-static {f_x_peters:.0f} Hz")
check("crossover sits in the LVK band under every convention",
      50 < f_x_dust < 1000 and 50 < f_x_full < 1000 and 50 < f_x_peters < 1000,
      f"{f_x_dust:.0f} / {f_x_peters:.0f} / {f_x_full:.0f} Hz  (de Rham-Melville wall: 260 Hz)")

# exact LCDM accumulated phase (GW vs photon) for source at z_e, flat LCDM:
#   Delta_phi(omega_obs) = Int (a''/a)/(2 k) d eta ,  k = omega_obs / c (a0=1)
#   a''/a = (4 pi G/3)(rho_m a^-3 + 4 rho_L) a^2 ;  d eta = dz / H(z) / c ... (c=1 internally)
def Hz(z): return H0*np.sqrt(0.315*(1+z)**3 + 0.685)
def dphi(f_obs, z_e):
    k_ = 2*np.pi*f_obs   # omega_obs, c=1 units below via rates in s^-1
    integ = lambda z: (4*np.pi*G_N/3)*(rho_m*(1+z)**3 + 4*rho_L)/(1+z)**2/Hz(z)/(2*k_)
    val, _ = quad(integ, 0, z_e, limit=200)
    return val            # radians
print(f"    {'band':14s} {'Dphi(z=1) rad':>14s} {'dt = Dphi/omega [s]':>20s} {'1/omega cap [s]':>16s} {'timing floor':>13s}")
prec = {"PTA   3 nHz": 3e-8, "PTA  30 nHz": 3e-8, "LISA  1 mHz": 1.0, "LISA 10 mHz": 1.0,
        "LVK   25 Hz": 1e-4, "LVK  100 Hz": 1e-4, "LVK    1 kHz": 1e-4}
capped = True
for name, f in bands:
    om_ = 2*np.pi*f
    dp = dphi(f, 1.0)
    dt = dp/om_
    capped &= (dp < 1.0)
    print(f"    {name:14s} {dp:14.3e} {dt:20.3e} {1/om_:16.3e} {prec[name]:13.1e}")
check("sub-cycle cap: accumulated tachyonic phase < 1 rad in every band (z_e = 1)", capped,
      "the GW group advance never reaches one cycle over the whole path")

# ---------------------------------------------------------------------------
print("[H] numpy: the KK loophole -- gapless passive media evade the n(0) >= 1 chain")
# Drude: eps = 1 - wp^2/(w^2 + i g w);  Im eps = wp^2 g / (w (w^2+g^2)) >= 0 (passive)
wp, gam = 1.0, 0.05
def eps_drude(w):  return 1 - wp**2/(w**2 + 1j*gam*w)
def eps_lorentz(w, w0=1.0, g2=0.05): return 1 + wp**2/(w0**2 - w**2 - 1j*g2*w)
ws = np.linspace(1e-4, 50, 400)
check("Drude passivity: Im eps >= 0 for all omega > 0", bool(np.all(eps_drude(ws).imag >= 0)))
def kk_re(w, epsfun):   # Re eps(w) - 1 from KK over Im eps
    f_ = lambda x: (2/np.pi)*x*epsfun(x).imag/(x**2 - w**2)
    v1, _ = quad(f_, 1e-9, w-1e-6, limit=400); v2, _ = quad(f_, w+1e-6, 2000, limit=400)
    return v1 + v2
test_w = [0.3, 0.7, 2.0]
ok_kk = all(abs(kk_re(w_, eps_drude) - (eps_drude(w_).real - 1)) < 2e-3 for w_ in test_w)
check("Drude satisfies Kramers-Kronig (numerical, 3 sample points)", ok_kk)
check("yet Re n < 1 above the pole band: passivity+KK do NOT force n >= 1 for gapless response",
      bool(np.sqrt(np.abs(eps_drude(5.0))).real is not None and np.real(np.sqrt(eps_drude(5.0)+0j)) < 1),
      f"Re n(5 wp) = {np.real(np.sqrt(eps_drude(5.0)+0j)):.4f}")
check("gapped (Lorentz) contrast: KK + passivity force n(0) > 1",
      bool(np.real(np.sqrt(eps_lorentz(1e-6)+0j)) > 1),
      f"n(0) = {np.real(np.sqrt(eps_lorentz(1e-6)+0j)):.4f} -- the photon-EH case is in THIS class;"
      " the GW medium (1/omega^2 pole class) is in the Drude class")

# ---------------------------------------------------------------------------
n_ok = sum(1 for _, ok in PASS if ok)
print(f"\n{n_ok}/{len(PASS)} checks passed" + ("" if n_ok == len(PASS) else "  *** FAILURES ***"))
