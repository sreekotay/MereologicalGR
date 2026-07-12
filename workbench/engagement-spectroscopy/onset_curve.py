"""
THE ONSET CURVE: thermality quality of a uniformly accelerated UdW detector
coupled for a FINITE time, vs dimensionless episode length a*Dtau (c=1, a=1).

P(omega) = int ds K(s) e^{-i omega s} W0(s),  K = window autocorrelation.
Split W0 = f_reg + W_M;  P_M handled with distributional identity (see text).

Metrics:
  Q_DB(band)   : max |2 pi T_DB(w) - 1| over band, T_DB = w/ln(P(-w)/P(w))
  Planck fit   : fit A, Theta to P(w) ~ A w/(e^{w/Theta}-1) over w in [0.3,2.5]
                 report |2 pi Theta - 1| and max fractional residual.
Windows: Gaussian (aD), cos^2-tapered plateau (ramp tr, plateau Tp).
"""
import numpy as np
from scipy.optimize import curve_fit

def f_reg(s):
    out = np.empty_like(s)
    small = np.abs(s) < 1e-3
    big = s > 40.0
    mid = (~small) & (~big)
    sb = s[mid]
    out[mid] = -(1.0/(4*np.pi**2))*(1.0/(4.0*np.sinh(sb/2.0)**2) - 1.0/sb**2)
    ss = s[small]
    out[small] = -(1.0/(4*np.pi**2))*(-1.0/12.0 + ss**2/240.0)
    out[big] = 1.0/(4*np.pi**2*s[big]**2)
    return out

def response(Kfun, Kpfun, K0, w, smax, ds=0.002):
    s = np.arange(ds/2, smax, ds)
    Ks, Kps = Kfun(s), Kpfun(s)
    Preg = 2.0*np.sum(Ks*f_reg(s)*np.cos(w*s))*ds
    PM = -(1.0/(4*np.pi**2))*(2.0*np.sum((Kps*np.cos(w*s) - w*Ks*np.sin(w*s))/s)*ds
                              + np.pi*w*K0)
    return Preg + PM

def T_DB(Pp, Pm, w):
    return w/np.log(Pm/Pp)

def metrics(Kfun, Kpfun, K0, smax):
    # detailed-balance bands
    out = {}
    for name, band in [('QDB_hi', (0.5, 2.0)), ('QDB_lo', (0.25, 1.0))]:
        ws = np.linspace(band[0], band[1], 12)
        dev = []
        ok = True
        for w in ws:
            Pp = response(Kfun, Kpfun, K0, w, smax)
            Pm = response(Kfun, Kpfun, K0, -w, smax)
            if Pp <= 0 or Pm <= 0:
                ok = False; break
            dev.append(abs(2*np.pi*T_DB(Pp, Pm, w) - 1.0))
        out[name] = max(dev) if ok else np.inf
    # emission-side Planck fit (what analog experiments do)
    ws = np.linspace(0.3, 2.5, 23)
    Ps = np.array([response(Kfun, Kpfun, K0, w, smax) for w in ws])
    if np.all(Ps > 0):
        def planck(w, A, Th):
            return A*w/np.expm1(w/Th)
        try:
            popt, _ = curve_fit(planck, ws, Ps, p0=[Ps[0]*np.expm1(ws[0]*2*np.pi)/ws[0], 1/(2*np.pi)],
                                maxfev=20000)
            resid = np.max(np.abs(planck(ws, *popt)/Ps - 1.0))
            out['Theta_dev'] = 2*np.pi*popt[1] - 1.0
            out['fit_resid'] = resid
        except Exception:
            out['Theta_dev'] = np.nan; out['fit_resid'] = np.nan
    else:
        out['Theta_dev'] = np.nan; out['fit_resid'] = np.nan
    return out

print("=== sanity: infinite-time limit (Gaussian, aD=200, smax=12D) ===")
D = 200.0
Kf = lambda s: np.sqrt(np.pi)*D*np.exp(-s**2/(4*D**2))
Kp = lambda s: np.sqrt(np.pi)*D*(-s/(2*D**2))*np.exp(-s**2/(4*D**2))
for w in [0.5, 1.0, 2.0]:
    P = response(Kf, Kp, np.sqrt(np.pi)*D, w, smax=12*D, ds=0.004)
    F0 = (1.0/(2*np.pi))*w/np.expm1(2*np.pi*w)
    print(f"  w={w}: P/K0 = {P/(np.sqrt(np.pi)*D):.6e}   F0 = {F0:.6e}   ratio {P/(np.sqrt(np.pi)*D)/F0:.4f}")

print("\n=== Gaussian window scan ===")
print("  aD   aDtau_eff   QDB[0.5,2]   QDB[0.25,1]   2piTheta-1   fit_resid")
for D in [2.0, 3.0, 4.0, 6.0, 8.0, 12.0, 16.0, 24.0, 32.0, 48.0]:
    K0 = np.sqrt(np.pi)*D
    Kf = lambda s, D=D: np.sqrt(np.pi)*D*np.exp(-s**2/(4*D**2))
    Kp = lambda s, D=D: np.sqrt(np.pi)*D*(-s/(2*D**2))*np.exp(-s**2/(4*D**2))
    smax = max(60.0, 12.0*D)
    m = metrics(Kf, Kp, K0, smax)
    print(f"  {D:5.1f} {2*np.sqrt(np.pi)*D:8.1f}  {m['QDB_hi']:11.4e}  {m['QDB_lo']:11.4e}"
          f"  {m['Theta_dev']:+11.4e}  {m['fit_resid']:9.2e}")

print("\n=== cos^2-tapered plateau window (ramp tr, plateau Tp) ===")
def tapered_K(Tp, tr, du=0.002):
    L = Tp + 2*tr
    n = int(np.ceil(L/du)) + 1
    u = np.linspace(0, L, n)
    chi = np.ones_like(u)
    m1 = u < tr
    chi[m1] = np.sin(0.5*np.pi*u[m1]/tr)**2
    m2 = u > L - tr
    chi[m2] = np.sin(0.5*np.pi*(L - u[m2])/tr)**2
    npad = 1 << int(np.ceil(np.log2(2*n)))
    C = np.fft.irfft(np.abs(np.fft.rfft(chi, npad))**2, npad)*du
    lags = np.arange(n)*du
    K = C[:n]
    Kp = np.gradient(K, du)
    Dt_eff = (np.trapezoid(chi, u))**2/np.trapezoid(chi**2, u)
    Kfun = lambda s: np.interp(s, lags, K, right=0.0)
    Kpfun = lambda s: np.interp(s, lags, Kp, right=0.0)
    return Kfun, Kpfun, K[0], L, Dt_eff

print("  tr     Tp   aDtau_eff  QDB[0.5,2]  QDB[0.25,1]  2piTheta-1  fit_resid")
cases = [(2.0,20.0),(2.0,80.0),(4.0,20.0),(4.0,40.0),(4.0,80.0),
         (6.0,20.0),(6.0,40.0),(6.0,80.0),(6.0,160.0),
         (8.0,40.0),(8.0,80.0),(10.0,40.0),(10.0,80.0),(10.0,160.0),
         (14.0,80.0),(14.0,160.0)]
for tr, Tp in cases:
    Kfun, Kpfun, K0, L, Dte = tapered_K(Tp, tr)
    m = metrics(Kfun, Kpfun, K0, L)
    print(f"  {tr:5.1f} {Tp:6.1f} {Dte:8.1f}  {m['QDB_hi']:11.4e} {m['QDB_lo']:11.4e}"
          f"  {m['Theta_dev']:+11.4e}  {m['fit_resid']:9.2e}")
