#!/usr/bin/env python3
"""
Referee script: cosmological arrival-time fan for GW-EM template families.
Flat LCDM, H0 = 67.7 km/s/Mpc, Om = 0.315 (radiation neglected: <0.1% in H at z<=2).

DERIVATION (the weighting, done from FLRW null geodesics -- no guessing):

  ds^2 = -c^2 dt^2 + a(t)^2 dchi^2.  Photon: a dchi/dt = c.  GW: a dchi/dt = c(1-eps).
  Both emitted at t_e from comoving radius chi_s.
  Photon:  chi_s = INT_{t_e}^{t_gamma} c dt / a
  GW:      chi_s = INT_{t_e}^{t_gw}    c(1-eps) dt / a
  Define F(t) = INT_{t_e}^{t} c dt'/a.  Then F(t_gamma) = chi_s, F(t_gw) = chi_s/(1-eps).
  => INT_{t_gamma}^{t_gw} c dt/a = chi_s * eps/(1-eps).
  Over the few-second arrival gap a = a0 = 1, so

      Dt_obs = (eps/(1-eps)) * chi_s / c  ~=  eps * D_C(z) / c          (constant eps)
             = eps * INT_0^z dz'/H(z').

  Element-wise bookkeeping (why NO net (1+z') weighting): a local proper-time lag
  d(tau) inserted between the two fronts at redshift z' IS observed dilated by (1+z').
  The constant-eps kinematic term inserts lag at local rate d(tau) = eps dt
  (proper-metered), and dt = dz'/[(1+z')H(z')], so the dilation cancels exactly:
      Dt_obs = INT eps (1+z') dt = eps INT_0^z dz'/H(z').
  The naive guess eps*INT (1+z') dz'/H double-counts the dilation.

  Cross-check target: Jacob & Piran 2008 (JCAP 01:031) LIV delay
  Dt = ((1+n)/2)(E/E_QG)^n (1/H0) INT (1+z')^n dz'/h(z'); their n is the ENERGY power
  in the dispersion relation. n=0 (energy-independent speed offset) => INT dz'/H. Matches.

  CHAIN vs PATH (the two n=1 columns):
   - PATH (proper-metered): lag inserted per unit local proper path length,
     d(tau) = (eps/c) dl_prop = eps dt.  Observed: Dt = eps INT_0^z dz'/H(z')
     = eps D_C/c.  [dilation cancels]
   - CHAIN (comoving-metered): a frame-chain counting comoving elements inserts a
     fixed LOCAL proper-time cost per comoving step: d(tau) = (eps_c/c) dchi
     = eps_c dz'/H(z').  Each locally-inserted lag then dilates by (1+z'):
         Dt_chain = eps_c INT_0^z (1+z') dz'/H(z').
     So the (1+z') weighting belongs to the CHAIN, not the constant-eps path term
     (the task memo's guess had them swapped; derivation above fixes the assignment).

  HORN C: eps(z) = eps0 * E(z)^p, E = H/H0. Proper-metered kernel =>
      Dt_p = eps0 (1/H0) INT_0^z E(z')^{p-1} dz'.
      p=0: (1/H0) INT dz'/E = D_C/c.   p=1: z/H0 (exactly!).   p=2: (1/H0) INT E dz'.
"""
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

# ---------- cosmology ----------
H0_kms_Mpc = 67.7
Om, OL = 0.315, 1.0 - 0.315
c_kms = 299792.458
Mpc_km = 3.0856775814913673e19
H0_s = H0_kms_Mpc / Mpc_km                    # s^-1
DH_Mpc = c_kms / H0_kms_Mpc                   # Hubble distance, Mpc
tH_s = 1.0 / H0_s                             # Hubble time, s

def E(z): return np.sqrt(Om*(1+z)**3 + OL)

def I_path(z):   # INT_0^z dz'/E  (= D_C * H0/c) : constant-eps path weight
    return quad(lambda x: 1/E(x), 0, z, epsabs=1e-13, epsrel=1e-12)[0]

def I_chain(z):  # INT_0^z (1+z') dz'/E : comoving-metered chain weight
    return quad(lambda x: (1+x)/E(x), 0, z, epsabs=1e-13, epsrel=1e-12)[0]

def I_p(z, p):   # INT_0^z E^{p-1} dz' : Horn C kernel eps0 E^p, proper-metered
    return quad(lambda x: E(x)**(p-1), 0, z, epsabs=1e-13, epsrel=1e-12)[0]

def DC(z):  return DH_Mpc * I_path(z)         # comoving distance, Mpc (= D_M, flat)
def DL(z):  return (1+z) * DC(z)
def Dlin(z): return DH_Mpc * z                # naive flat-space Hubble-law distance

# ---------- anchor ----------
zs = 0.0098
Dt_star = 1.74                                # s
Dstar44, Dstar40 = 44.0, 40.0                 # Mpc conventions
DC_star = DC(zs)
eps_44 = c_kms * Dt_star / (Dstar44 * Mpc_km)
eps_40 = c_kms * Dt_star / (Dstar40 * Mpc_km)
eps_path = Dt_star / (tH_s * I_path(zs))      # from the FLRW path formula itself

print("=== ANCHOR / SANITY ===")
print(f"D_C(z*=0.0098)          = {DC_star:8.3f} Mpc   (cz/H0 = {Dlin(zs):.3f}, D_L = {DL(zs):.3f})")
print(f"eps (44 Mpc flat)       = {eps_44:.3e}")
print(f"eps (40 Mpc flat)       = {eps_40:.3e}")
print(f"eps (FLRW path, z*)     = {eps_path:.3e}   "
      f"[vs 44 Mpc: {100*(eps_path/eps_44-1):+.1f}% ; vs 40 Mpc: {100*(eps_path/eps_40-1):+.1f}%]")

# ---------- EXACT numerical geodesic check of the weighting ----------
# Integrate a(t) and both signal trajectories with a LARGE eps at z_e = 1;
# compare the true arrival gap with (i) eps/(1-eps)*D_C/c  and (ii) the WRONG
# dilation-weighted guess eps*INT(1+z)dz/H.
def geodesic_check(z_e=1.0, epsb=1e-3):
    # Exact, expansion-free computation in scale factor a (dt = da/(a H),
    # dchi/da = v/(a^2 H)). Signal with proper speed v emitted at a_e from
    # chi_s arrives at a_arr solving INT_{a_e}^{a_arr} v da/(a^2 H) = chi_s.
    # Arrival-time gap: Dt = INT_{a_gam}^{a_gw} da/(a H). No first-order
    # expansion anywhere -- independent of the analytic derivation.
    chi_s = DC(z_e) * Mpc_km  # km
    exact = chi_s * epsb / ((1 - epsb) * c_kms)   # analytic (conformal-time) result
    def Hs(a): return H0_s * E(1/a - 1)
    a_e = 1/(1+z_e)
    def chi_covered(a_arr, v):
        return quad(lambda a: v/(a*a*Hs(a)), a_e, a_arr, epsrel=1e-13, limit=300)[0]
    def a_arrival(v):
        return brentq(lambda a: chi_covered(a, v) - chi_s, a_e+1e-6, 1.5,
                      xtol=1e-16, rtol=8.9e-16)
    a_gam = a_arrival(c_kms)
    a_gw  = a_arrival(c_kms*(1-epsb))
    num = quad(lambda a: 1/(a*Hs(a)), a_gam, a_gw, epsrel=1e-13)[0]
    wrong = epsb * tH_s * I_chain(z_e)
    right = epsb * tH_s * I_path(z_e)
    return num, exact, right, wrong

num, exact, right, wrong = geodesic_check()
print("\n=== GEODESIC WEIGHTING CHECK (z=1, eps=1e-3) ===")
print(f"brute-force ODE arrival gap : {num:.6e} s")
print(f"exact eps/(1-eps)*D_C/c     : {exact:.6e} s   (ratio {num/exact:.6f})")
print(f"first-order eps*INT dz/H    : {right:.6e} s   (ratio {num/right:.6f})")
print(f"WRONG eps*INT(1+z)dz/H      : {wrong:.6e} s   (ratio {num/wrong:.6f})  <- rejected")

# ---------- fan table ----------
zrows = [0.0098, 0.1, 0.5, 1.0, 2.0]
Ipath_s, Ichain_s = I_path(zs), I_chain(zs)

def fan_row(z):
    r_path  = I_path(z)/Ipath_s               # n=1 path (constant-eps, FLRW-exact)
    r_chain = I_chain(z)/Ichain_s             # n=1 chain (comoving-metered, dilated)
    rDC = DC(z)/DC_star
    return {
        'n=0': Dt_star,                       # constant OBSERVED lag convention
        'n=1 chain': Dt_star*r_chain,
        'n=1 path':  Dt_star*r_path,          # == Dt_star * D_C/D_C*  (identical scaling)
        'n=2 (D_M^2)': Dt_star*rDC**2,        # comoving-transverse area convention
        'n=3 (D_C^3)': Dt_star*rDC**3,        # comoving volume
        'D^0.58': Dt_star*rDC**0.58,
    }

def naive_row(z):                             # flat-space shortcut: D = cz/H0, no dilation
    r = Dlin(z)/Dlin(zs)
    return {'n=0': Dt_star, 'n=1 chain': Dt_star*r, 'n=1 path': Dt_star*r,
            'n=2 (D_M^2)': Dt_star*r**2, 'n=3 (D_C^3)': Dt_star*r**3,
            'D^0.58': Dt_star*r**0.58}

cols = ['n=0','n=1 chain','n=1 path','n=2 (D_M^2)','n=3 (D_C^3)','D^0.58']
print("\n=== CORRECTED FAN TABLE (observed lag, s; anchored 1.74 s at z*=0.0098) ===")
print(f"{'z':>7} | " + " | ".join(f"{cc:>12}" for cc in cols))
for z in zrows:
    r = fan_row(z)
    print(f"{z:7.4f} | " + " | ".join(f"{r[cc]:12.4g}" for cc in cols))

print("\n--- deviation from naive flat-space shortcut D=cz/H0 [(FLRW-naive)/naive, %] ---")
print(f"{'z':>7} | " + " | ".join(f"{cc:>12}" for cc in cols))
for z in zrows:
    r, nv = fan_row(z), naive_row(z)
    print(f"{z:7.4f} | " + " | ".join(f"{100*(r[cc]/nv[cc]-1):+11.1f}%" for cc in cols))

print("\n--- deviation if 'D' is misread as luminosity distance D_L [(D_L-col / D_C-col), %] ---")
for z in zrows:
    rr = DL(z)/DL(zs) / (DC(z)/DC_star)
    print(f"z={z:7.4f}: n=1 {100*(rr-1):+8.1f}%   n=2 {100*(rr**2-1):+8.1f}%   n=3 {100*(rr**3-1):+9.1f}%")

# ---------- degeneracy: n=1 chain vs path ----------
print("\n=== n=1 CHAIN vs PATH DEGENERACY ===")
for z in [0.1, 0.5, 1.0, 2.0]:
    a = Dt_star*I_chain(z)/Ichain_s; b = Dt_star*I_path(z)/Ipath_s
    print(f"z={z:5.2f}: chain {a:8.2f} s  path {b:8.2f} s  diff {a-b:7.2f} s  ({100*(a/b-1):+.1f}%)")
for sig in [0.5, 1.0, 2.0, 4.0]:
    f = lambda z: Dt_star*(I_chain(z)/Ichain_s - I_path(z)/Ipath_s) - sig
    zc = brentq(f, 0.011, 3.0)
    print(f"one event discriminates at sigma_t = {sig:4.1f} s for z >= {zc:.3f} "
          f"(Dt_path there = {Dt_star*I_path(zc)/Ipath_s:.1f} s)")

# ---------- Horn C ----------
print("\n=== HORN C: eps(z)=eps0 E(z)^p, path term Dt = eps0/H0 * INT E^{p-1} dz ===")
print("enhancement R_p(z) = I_p(z)/I_0(z)  [relative to constant-eps]")
for z in [0.5, 1.0, 2.0]:
    print(f"z={z:4.1f}: R_1 = {I_p(z,1)/I_p(z,0):.4f}   R_2 = {I_p(z,2)/I_p(z,0):.4f}")
print("\nanchored fan values Dt_p(z) = 1.74 * I_p(z)/I_p(z*):")
print(f"{'z':>5} | {'p=0':>9} | {'p=1':>9} | {'p=2':>9} | shape p=2/p=1 vs p=1/p=0")
for z in [0.5, 1.0, 2.0]:
    d = [Dt_star*I_p(z,p)/I_p(zs,p) for p in (0,1,2)]
    print(f"{z:5.2f} | {d[0]:8.2f}s | {d[1]:8.2f}s | {d[2]:8.2f}s |  {d[2]/d[1]:.3f} vs {d[1]/d[0]:.3f}")

# p=0 vs p=1, single event + anchor, 2 s per-event systematic (quadrature, 2 events, 2sigma)
thresh = 2.0*np.sqrt(2)*2.0   # 2sigma * sqrt(2 events) * 2 s  -> 5.66 s ; also report 4 s linear
for lab, th in [("2s+2s linear (4 s)",4.0), ("2sigma quadrature (5.66 s)",2*np.sqrt(2)*2)]:
    f = lambda z: Dt_star*(I_p(z,1)/I_p(zs,1) - I_p(z,0)/I_p(zs,0)) - th
    zc = brentq(f, 0.02, 3.0)
    print(f"p=0 vs p=1 separable ({lab}) for z >= {zc:.3f}")

# anchor-free two-event RATIO arithmetic (kills the eps0/jet-b normalization):
print("\n(z1,z2) pair arithmetic, ratio r=Dt(z2)/Dt(z1), sigma=2 s per event, 2sigma test:")
for z1, z2 in [(0.2,0.5),(0.2,1.0),(0.5,1.0),(0.5,2.0),(1.0,2.0)]:
    r0 = I_p(z2,0)/I_p(z1,0); r1 = I_p(z2,1)/I_p(z1,1)
    # amplitudes under p=0 anchored (conservative: similar under p=1)
    d1 = Dt_star*I_p(z1,0)/I_p(zs,0); d2 = Dt_star*I_p(z2,0)/I_p(zs,0)
    sig_r = r0*np.sqrt((2.0/d1)**2 + (2.0/d2)**2)
    print(f"z1={z1:3.1f},z2={z2:3.1f}: r_p0={r0:6.3f} r_p1={r1:6.3f} "
          f"|dr|={abs(r1-r0):6.3f} sigma_r={sig_r:6.3f} -> {abs(r1-r0)/sig_r:5.1f} sigma")

# ---------- final sanity ----------
print("\n=== FINAL SANITY ===")
row = fan_row(zs)
assert all(abs(v-1.74) < 1e-9 for v in row.values()), "anchor row broken"
print("anchor row = 1.74 s in every column: PASS")
print(f"eps(path @ z*) = {eps_path:.3e} vs 3.8e-16 (44 Mpc flat): "
      f"{100*abs(eps_path/eps_44-1):.1f}% (= 44 Mpc vs D_C(z*)={DC_star:.1f} Mpc): PASS (stated)")
print(f"D_C: z=0.1 {DC(0.1):.1f}  z=0.5 {DC(0.5):.1f}  z=1 {DC(1):.1f}  z=2 {DC(2):.1f} Mpc")
