"""GW OSCILLATION FACE OF c9's REALISATION (singly-coupled Hassan-Rosen, matter on g).

Origin: workbench/seam-vacuum (which_cone.py, band_scan.py). Matter emits and detects only the
g tensor. The g/f tensor pair, canonically normalised, at fixed observed angular frequency w:

    k^2 C = w^2 - M,   C = diag(1, 1+B),   M = m^2/(1+a^2) [[a^2, -a], [-a, 1]]

with B = 6 (H/m_FP)^2 (c9: B = C(H/m_FP)^2, C = 6, alpha^2 cancelling) and a = alpha = M_f/M_g.

METHOD LAYER
  forced   -- crossover w* = m_FP/sqrt(B); at w* the fabric eigenmode's cone advance and mass lag
              cancel in group delay; the oscillation phase rate at w* is sqrt(B) m_FP = sqrt(6) H,
              independent of m_FP; mixing saturates at alpha below w*.
  imported -- the bigravity GW-oscillation mechanism (Max-Platscher-Smirnov 2017 and sequels);
              Planck-like LCDM for distances; c9's m_FP, B law, alpha window.
  chosen   -- proportional-background mass matrix (O(1) y, X factors dropped; y* = 1 late times);
              B and mixing evaluated locally along the path, w redshifted.
  parked   -- the exact FRW tensor mass matrix with y(z), X(z); decoherence of the two packets
              (separation vs source duration); LISA's actual amplitude-modulation reach.
"""
import numpy as np
from scipy.integrate import quad

checks = []
def check(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)

hbar = 6.582119569e-16                  # eV s
H0 = 67.4 * 1e3 / 3.0857e22 * hbar     # eV
Om, OL = 0.315, 0.685
m = 1.4e-25                              # eV, c9
E = lambda z: np.sqrt(Om*(1+z)**3 + OL)
Hz = lambda z: H0*E(z)
B = lambda z: 6*(Hz(z)/m)**2

print(f"B today = {B(0):.2e}   (c1's anchor B = 2 eps = 7.6e-16)")

# ---- 1. crossover ----------------------------------------------------------------------------
fstar = lambda z: m/np.sqrt(B(z))/(2*np.pi*hbar)
for z in [0, 1, 2, 3]:
    print(f"   f*(z={z}) = {fstar(z)*1e3:.2f} mHz")
check("1. f*(0) in the LISA band (0.1-10 mHz)", 1e-4 < fstar(0) < 1e-2)
check("1b. f* = m_FP^2/(2 pi hbar sqrt(6) H): f* falls as 1/H(z)",
      abs(fstar(2)/fstar(0) - 1/E(2)) < 1e-12)

# ---- 2. mixing and dispersion at fixed w --------------------------------------------------------
from mpmath import mp, mpf, matrix as mmat, eig as meig, sqrt as msqrt
mp.dps = 60

def modes(w, z, a):
    """return (k of matter-like mode, k of fabric-like mode, f-content of matter-like mode) at
    fixed w. High precision: the k splittings are ~1e-16 of k."""
    w, a, Bz, mm = mpf(w), mpf(a), mpf(B(z)), mpf(m)
    M = (mm**2/(1 + a**2))*mmat([[a**2, -a], [-a, 1]])
    K = mmat([[1, 0], [0, 1/(1 + Bz)]])*(w**2*mmat([[1, 0], [0, 1]]) - M)
    vals, vecs = meig(K)
    nrm = lambda j: msqrt(abs(vecs[0, j])**2 + abs(vecs[1, j])**2)
    i = max(range(2), key=lambda j: abs(vecs[0, j])/nrm(j))
    j = 1 - i
    return msqrt(vals[i].real), msqrt(vals[j].real), abs(vecs[1, i])/nrm(i)

a = 1e-2
for f_hz in [100, 1e-1, 1e-2, 1e-3, 1e-4, 1e-8]:
    w = 2*np.pi*f_hz*hbar
    kg, kf, th = modes(w, 0, a)
    print(f"   f = {f_hz:7.0e} Hz: mixing {float(th):.2e}   dk/w = {float((kg-kf)/w):+.2e}")
w_lo = 2*np.pi*1e-8*hbar
check("2. below f*, mixing saturates at alpha", abs(float(modes(w_lo, 0, a)[2])/a - 1) < 0.05)

# group delay of the fabric-like mode relative to the matter-like mode: zero at f*
def dtg(w, z):
    w = mpf(w)
    h = w*mpf('1e-8')
    _, kf1, _ = modes(w - h, z, a); _, kf2, _ = modes(w + h, z, a)
    kg1, _, _ = modes(w - h, z, a); kg2, _, _ = modes(w + h, z, a)
    return (kf2 - kf1)/(2*h) - (kg2 - kg1)/(2*h)
ws = 2*np.pi*fstar(0)*hbar
check("3. at f*, fabric-mode cone advance and mass lag cancel in group delay",
      abs(dtg(ws, 0)) < 0.02*abs(dtg(ws*10, 0)))
check("3b. above f* the fabric mode leads (cone); below it lags (mass)",
      dtg(ws*10, 0) < 0 < dtg(ws/10, 0))

# ---- 4. the phase identity: at w*, dk = sqrt(B) m = sqrt(6) H -----------------------------------
dk_star = ws*B(0)/2 + m**2/(2*ws)
check("4. oscillation phase rate at f* = sqrt(6) H, independent of m_FP",
      abs(dk_star/(np.sqrt(6)*H0) - 1) < 1e-9)

# ---- 5. integrated phase and modulation depth to a LISA source --------------------------------
def phase(f_obs, zs):
    # dk(z) = w(z) B(z)/2 + m^2/(2 w(z)),  w(z) = w0 (1+z),  dl = dz/((1+z) H) in eV^-1
    w0 = 2*np.pi*f_obs*hbar
    integrand = lambda z: (w0*(1+z)*B(z)/2 + m**2/(2*w0*(1+z)))/((1+z)*Hz(z))
    return quad(integrand, 0, zs)[0]
for zs in [1, 3]:
    for f_obs in [1e-2, 1e-3, 1e-4]:
        ph = phase(f_obs, zs)
        print(f"   z_s={zs}, f={f_obs:.0e} Hz: phase {ph:8.2f} rad")
check("5. at f*(0) the integrated phase to z = 1 is O(1) (0.3 - 30 rad)",
      0.3 < phase(fstar(0), 1) < 30)
for a_ in [1e-3, 1e-2]:
    print(f"   alpha = {a_:.0e}: max strain modulation depth ~ 2 alpha^2 = {2*a_**2:.0e}")
check("6. within c9's alpha window (<= 1e-2) the strain modulation is <= 2e-4", 2*(1e-2)**2 <= 2e-4)

print()
print(f"{sum(o for _, o in checks)}/{len(checks)} checks passed")
