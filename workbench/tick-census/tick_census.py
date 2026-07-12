#!/usr/bin/env python3
"""
THE GRAVITATIONAL TICK-CENSUS -- a two-clock cosmology.

Meters coarse-grained chronology on entropy-exchange ("entropic time",
operationalized in cold atoms by Yates et al., arXiv:2509.07745, PRResearch 2026:
tau = normalized cumulative coarse-grained entropy exchange of an observed sector).

Applied to cosmology: per-channel comoving entropy PRODUCTION rates dS_i/dln a
across cosmic history, then per-sector entropic clocks
    tau_i(a) = int^a dS_i / int^{a0} dS_i .

Channels
  photon-baryon : Silk-damping dissipation (mu/y era), recombination photon burst,
                  post-recombination residual Compton coupling (solved T_gas ODE),
                  reionized-IGM Compton/y.
  nuclear       : starlight (Madau-Dickinson 2014 SFH; radiation entropy at an
                  effective photosphere+dust temperature). BBN handled analytically
                  in text (negligible: DeltaS/S_gamma ~ 5e-9).
  grav-structure: violent relaxation / virialization; rate ~ d F_coll/dln a
                  (Press-Schechter, BBKS sigma(M), exact LCDM growth factor),
                  amplitude = s_grav [k_B per proton-mass of collapsed matter],
                  scanned over 30 decades (it barely moves the crossover).
  BH horizons   : stellar BHs (S ~ cumulative SFR; anchored to Egan-Lineweaver
                  5.9e97 k today) and SMBHs (Soltan-argument accretion history +
                  seed tail; S ~ Sum M^2 ~ rho_BH^2 at fixed comoving number;
                  anchored to Egan-Lineweaver 3.1e104 k today).

Anchors: Egan & Lineweaver 2010 (ApJ 710, 1825): S_SMBH=3.1e104 k, S_sBH=5.9e97 k,
S_gamma=5.4e89 k, S_nu=5.2e89 k (frozen), S_CEH=2.6e122 k (excluded: not an
exchange channel between matter sectors; observer-dependent).

Outputs: budget table dS_i/dln a vs z, tau curves, crossover redshifts,
dark-ages divergence numbers, PNG figures, CSV grid.
"""

import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import interp1d
from scipy.special import erfc

# ----------------------------------------------------------------------
# constants (SI) and cosmology (Planck 2018)
# ----------------------------------------------------------------------
c      = 2.998e8
G      = 6.674e-11
hbar   = 1.055e-34
kB     = 1.381e-23
sigT   = 6.652e-29
a_rad  = 7.566e-16          # J m^-3 K^-4
m_e    = 9.109e-31
m_u    = 1.661e-27
Msun   = 1.989e30
Mpc    = 3.086e22
yr     = 3.156e7

h0     = 0.674
H0     = h0 * 100 * 1e3 / Mpc          # s^-1
Om, Ob, OL = 0.315, 0.0493, 0.685
Orad   = 9.15e-5                        # photons + massless nu (for H(z))
T0     = 2.725
ns, sig8 = 0.965, 0.811
Yp     = 0.245

rho_c  = 3 * H0**2 / (8 * np.pi * G)                    # kg m^-3
n_b0   = Ob * rho_c / m_u                               # baryons m^-3 (0.253)
n_H0   = (1 - Yp) * n_b0
f_He   = Yp / (4 * (1 - Yp))
rho_m_Mpc3 = Om * rho_c * Mpc**3 / Msun                 # Msun / Mpc^3 (comoving)

R_obs  = 46.3e9 * 9.461e15                              # comoving radius, m
V0     = 4/3 * np.pi * R_obs**3                         # 3.5e80 m^3
V0_Mpc = V0 / Mpc**3                                    # ~1.2e13 Mpc^3
N_bary = n_b0 * V0                                      # baryons in obs. universe
N_eq   = Om * rho_c * V0 / m_u                          # "proton-equivalents" of all matter

S_gamma = (4/3) * a_rad * T0**3 / kB * V0               # ~5.2e89 k  (frozen comoving)
S_nu    = 0.955 * S_gamma                               # frozen at t ~ 1 s
S_SMBH0, S_sBH0 = 3.1e104, 5.9e97                        # Egan-Lineweaver 2010

def Hz(z):
    return H0 * np.sqrt(Om*(1+z)**3 + Orad*(1+z)**4 + OL)

def t_of_z(z):
    f = lambda zz: 1.0 / ((1+zz) * Hz(zz))
    return quad(f, z, 3e7, limit=200)[0]

# exact linear growth factor D(a) ~ H(a) * int_0^a da'/(a' H(a'))^3, D(1)=1
def _D_un(a):
    Ha = Hz(1/a - 1)
    integ = quad(lambda x: (H0/(x*Hz(1/x-1)))**3, 1e-6, a, limit=200)[0]
    return Ha/H0 * integ
_Dnorm = _D_un(1.0)
_a_tab = np.logspace(-3.6, 1.7, 400)                    # to a=50 for the far future
_D_tab = np.array([_D_un(a)/_Dnorm for a in _a_tab])
D_of_a = interp1d(np.log(_a_tab), _D_tab, kind='cubic')
def Dz(z):
    a = 1.0/(1+z)
    if a < _a_tab[0]:                                   # matter-era D ~ a
        return _D_tab[0] * a/_a_tab[0]
    return float(D_of_a(np.log(a)))
D_inf = _D_tab[-1]                                      # growth saturates under Lambda

# ----------------------------------------------------------------------
# sigma(M): BBKS transfer, Sugiyama shape, normalized to sigma_8
# ----------------------------------------------------------------------
Gam = Om * h0 * np.exp(-Ob * (1 + np.sqrt(2*h0)/Om))    # ~0.169
def Tbbks(k):                                           # k in Mpc^-1
    q = k / (Gam * h0)
    return (np.log(1+2.34*q)/(2.34*q) *
            (1 + 3.89*q + (16.1*q)**2 + (5.46*q)**3 + (6.71*q)**4)**-0.25)
def W(x): return 3*(np.sin(x) - x*np.cos(x))/x**3
def sigma2_un(R):
    f = lambda lk: (lambda k: k**(3+ns) * Tbbks(k)**2 * W(k*R)**2)(np.exp(lk))
    return quad(f, np.log(1e-5), np.log(1e4/R), limit=300)[0] / (2*np.pi**2)
R8 = 8.0/h0
_snorm = sig8 / np.sqrt(sigma2_un(R8))
def sigma_M(M):                                         # M in Msun
    R = (3*M/(4*np.pi*rho_m_Mpc3))**(1/3)
    return _snorm * np.sqrt(sigma2_un(R))

delc = 1.686
sig_mini = sigma_M(1e6)        # minihalo scale (first DM structures)
sig_atom = sigma_M(3e7)        # atomic-cooling scale (first stars/seeds)

def Fcoll(z, sig):             # Press-Schechter collapsed fraction
    return erfc(delc/(np.sqrt(2)*sig*Dz(z)))
def dF_dlna(z, sig, dlnD):     # exact derivative of the erfc form
    nu = delc/(sig*Dz(z))
    with np.errstate(under='ignore'):
        return np.sqrt(2/np.pi) * nu * np.exp(-nu**2/2) * dlnD

# ----------------------------------------------------------------------
# gas temperature ODE (residual Compton coupling after recombination)
# ----------------------------------------------------------------------
def x_e(z):                     # frozen-out ionization + recombination step
    return 2.0e-4 + (1-2.0e-4)*0.5*(1+np.tanh((z-1150.)/60.))
def Gamma_C(z):
    Tg4 = (T0*(1+z))**4
    return (8*sigT*a_rad*Tg4/(3*m_e*c)) * x_e(z)/(1+f_He+x_e(z))
def dTg_dz(z, T):
    Tgam = T0*(1+z)
    return np.atleast_1d(2*T[0]/(1+z) - Gamma_C(z)*(Tgam-T[0])/(Hz(z)*(1+z)))
sol = solve_ivp(dTg_dz, [1400, 0.01], [T0*1401.], method='Radau',
                dense_output=True, rtol=1e-9, atol=1e-12)
def T_gas(z):
    z = np.atleast_1d(np.asarray(z, float))
    out = np.where(z >= 1400, T0*(1+z), sol.sol(np.clip(z, 0.01, 1400))[0])
    return out

# ----------------------------------------------------------------------
# channel production rates  dS/dln a  [k_B, whole observable universe, comoving]
# ----------------------------------------------------------------------
lna  = np.linspace(np.log(1/(1+3.0e6)), 0.0, 6000)
zg   = 1/np.exp(lna) - 1
Hg   = Hz(zg)
Dg   = np.array([Dz(z) for z in zg])
dlnD = np.gradient(np.log(Dg), lna)

def compton_rate(z):            # k_B per obs.universe per ln a
    Tg, Tgam = T_gas(z), T0*(1+z)
    n_tot = n_H0*(1+f_He+x_e(z))*(1+z)**3
    sigdot = 1.5*n_tot*Gamma_C(z)*(Tgam-Tg)**2/np.maximum(Tg*Tgam, 1e-30)
    return sigdot * V0/(1+z)**3 / Hz(z)

ch = {}
# 1) Silk damping (acoustic dissipation -> mu,y distortions), 1100<z<2e6
DS_silk = 1e-8 * S_gamma
ch['silk'] = np.where((zg>1100)&(zg<2e6), DS_silk/np.log(2e6/1100), 0.0)
# 2) recombination photon burst: 13.6 eV/H at T~3000K => ~52 k_B per H
DS_rec = 52.5 * (1-Yp)*N_bary * 0.0    # amplitude via gaussian below
rec_g  = np.exp(-0.5*((lna-np.log(1/1151.))/0.06)**2)
ch['recomb'] = 52.5*(1-Yp/ (4*(1-Yp)) )*0 + 3.6e81/ (0.06*np.sqrt(2*np.pi)) * rec_g
# 3) residual Compton coupling (the dark-age baryonic whisper), 10<z<1400
ch['compton'] = np.where((zg>10)&(zg<1400), compton_rate(zg), 0.0)
# 4) reionized IGM Compton/y (T_e ~ 1e4 K vs CMB), z<7.7
def reion_rate(z):
    Te, Tgam = 1.0e4, T0*(1+z)
    n_tot = n_H0*(1+f_He+1.08)*(1+z)**3
    G = (8*sigT*a_rad*Tgam**4/(3*m_e*c)) * 1.08/(1+f_He+1.08)
    sigdot = 1.5*n_tot*G*(Te-Tgam)**2/(Te*Tgam)
    return sigdot * V0/(1+z)**3 / Hz(z)
ch['reion_y'] = np.where(zg < 7.7, reion_rate(np.maximum(zg,0.0)), 0.0)
# 5) stars (nuclear channel): Madau-Dickinson SFH, first stars turn on z~28
def psi_MD(z):                  # Msun / yr / Mpc^3
    return 0.015*(1+z)**2.7/(1+((1+z)/2.9)**5.6)
turn_on = np.where(zg > 35., 0.0, 0.5*(1+np.tanh((28.-zg)/2.)))  # first stars z~28
eps_rad = 7e-4                  # fraction of formed stellar mass radiated (nuclear)
Teff_inv = 0.5/5772. + 0.5/45.  # half direct starlight, half dust-reprocessed (45 K)
Lden = psi_MD(zg)*turn_on * Msun/yr * eps_rad*c**2      # W / Mpc^3
ch['stars'] = (4/3)*Lden*Teff_inv/kB / Hg * V0_Mpc
# 6) gravitational structure: violent relaxation / virialization
s_grav = 10.0                   # fiducial: k_B per proton-mass of collapsed matter
ch['struct'] = s_grav * N_eq * np.array(
    [dF_dlna(z, sig_mini, dd) for z, dd in zip(zg, dlnD)])
# 7) stellar BH horizons: S ~ cumulative SFR (fixed IMF => Sum M^2 ~ N_BH)
tg = cumulative_trapezoid(1/Hg, lna, initial=0) + t_of_z(zg[0])  # smooth t(a) grid
rho_form = cumulative_trapezoid(psi_MD(zg)*turn_on/yr, tg, initial=0)
S_sBH = S_sBH0 * rho_form/rho_form[-1]
ch['stellarBH'] = np.gradient(S_sBH, lna)
# 8) SMBH horizons: Soltan accretion (SFH-shaped, peaked z~1.9, steeper at high z)
#    + seed tail tracking atomic-cooling halos; S ~ rho_BH^2 (growth at fixed n)
rho_BH0 = 4.5e5                 # Msun/Mpc^3 today
qdot = psi_MD(zg)*turn_on/(1+zg)   # accretion-rate shape (no accretion pre-first-stars)
rho_acc = cumulative_trapezoid(qdot, tg, initial=0)
F_at = np.array([Fcoll(z, sig_atom) if Dz(z)*sig_atom > 0.12 else 0. for z in zg])
rho_seed = 2.0 * F_at/max(Fcoll(20., sig_atom), 1e-99)  # ~2 Msun/Mpc^3 by z=20
rho_BH = rho_acc/rho_acc[-1]*(rho_BH0-2.0) + np.minimum(rho_seed, 2.0)
S_SMBH = S_SMBH0 * (rho_BH/rho_BH[-1])**2
ch['SMBH'] = np.maximum(np.gradient(S_SMBH, lna), 0.0)

for k in ch: ch[k] = np.maximum(np.nan_to_num(ch[k]), 0.0)

BAR  = ['silk','recomb','compton','reion_y','stars']
GRAV = ['struct','stellarBH','SMBH']
rate_bar  = sum(ch[k] for k in BAR)
rate_grav = sum(ch[k] for k in GRAV)
rate_tot  = rate_bar + rate_grav

def cum(r):  return cumulative_trapezoid(r, lna, initial=0)
C = {k: cum(ch[k]) for k in ch}
cum_bar, cum_grav, cum_struct = cum(rate_bar), cum(rate_grav), cum(ch['struct'])
tau_bar    = cum_bar/cum_bar[-1]
tau_grav   = cum_grav/cum_grav[-1]
tau_struct = cum_struct/cum_struct[-1]     # = the dark-sector (DM) clock

iz = lambda z: np.argmin(np.abs(zg - z))

# ----------------------------------------------------------------------
# report
# ----------------------------------------------------------------------
print(f"sanity: S_gamma={S_gamma:.2e} k  (EL10: 5.4e89) | N_b={N_bary:.2e}"
      f" | sigma(1e6 Msun)={sig_mini:.2f} sigma(3e7)={sig_atom:.2f}"
      f" | D_inf/D_0={D_inf:.3f}")
print(f"thermal decoupling check: T_gas/T_cmb at z=150: "
      f"{T_gas(150)[0]/ (T0*151):.3f}; at z=17: {T_gas(17)[0]:.1f} K "
      f"(std ~7 K)\n")

hdr = ['z','silk','recomb','compton','reion_y','stars','struct','stellarBH','SMBH','TOTAL']
print('dS/dln a  [k_B, observable universe, comoving]')
print(('{:>8}'+'{:>11}'*9).format(*hdr))
for z in [2e6,1e4,1100,300,150,100,50,30,25,20,17,10,6,3,2,1,0.5,0]:
    i = iz(z)
    row = [ch[k][i] for k in hdr[1:-1]] + [rate_tot[i]]
    print(('{:>8.6g}'+'{:>11.2e}'*9).format(z,*row))

print('\ncumulative S_i(z) [k_B, obs. universe]  and clocks')
print(('{:>8}'+'{:>12}'*6).format('z','S_bar','S_grav','S_struct','tau_bar','tau_grav','tau_DM'))
for z in [1100,300,150,100,50,30,20,17,10,6,3,1,0]:
    i = iz(z)
    print(('{:>8.5g}'+'{:>12.3e}'*3+'{:>12.4e}'*3).format(
        z, cum_bar[i], cum_grav[i], cum_struct[i],
        tau_bar[i], tau_grav[i], tau_struct[i]))

# crossovers ------------------------------------------------------------
def first_z_below(mask):
    j = np.where(mask)[0]
    return zg[j[0]] if len(j) else None

# (a) structure vs pre-stellar baryonic thermal (compton+silk+recomb)
bar_thermal = ch['silk']+ch['recomb']+ch['compton']
print('\n(a) grav-structure rate overtakes baryonic THERMAL rate (no stars):')
for s in [1,10,1e3,1e6,1e10,1e20,1e30]:
    r = (s/s_grav)*ch['struct'] - bar_thermal
    zx = first_z_below((r>0)&(zg<500)&(zg>2))
    print(f'    s_grav={s:8.0e} k_B/mp  ->  z_cross = {zx:5.1f}')

# (b) BH horizon cumulative overtakes ALL thermal+relic entropy (gamma+nu)
S_BH_cum = C['stellarBH'] + S_SMBH   # S_SMBH already cumulative-by-construction
zb = first_z_below(S_BH_cum > (S_gamma+S_nu))
print(f'\n(b) cumulative BH-horizon entropy exceeds S_gamma+S_nu={S_gamma+S_nu:.2e}: z = {zb:.1f}')
print(f'    (one 1e6 Msun seed alone: {4*np.pi*G*(1e6*Msun)**2/(hbar*c):.2e} k_B '
      f'= CMB entropy of {4*np.pi*G*(1e6*Msun)**2/(hbar*c)/(S_gamma/V0_Mpc):.2e} Mpc^3)')

# (c) SMBH production overtakes every other channel's production
other = rate_tot - ch['SMBH']
zc = first_z_below((ch['SMBH'] > other) & (zg < 100))
print(f'(c) SMBH horizon production rate exceeds ALL other channels combined: z = {zc:.1f}')
zd = first_z_below((ch['stellarBH']+ch['SMBH'] > rate_bar+ch['struct']) & (zg<100))
print(f'    BH-horizon channel (stellar+SMBH) rate exceeds everything else: z = {zd:.1f}')

# quietest epoch ---------------------------------------------------------
m = (zg>5)&(zg<1050)
iq = np.where(m)[0][np.argmin(rate_tot[m])]
print(f'\nquietest epoch: min of total dS/dln a between recombination and today: '
      f'z = {zg[iq]:.1f}, rate = {rate_tot[iq]:.2e} k_B/lna '
      f'({np.log10(rate_tot[iz(1100)]/rate_tot[iq]):.1f} dex below recombination, '
      f'{np.log10(rate_tot[iz(0)]/rate_tot[iq]):.1f} dex below today)')

# dark-ages divergence ----------------------------------------------------
i1100,i150,i30,i17,i6 = (iz(x) for x in (1100,150,30,17,6))
print('\nDARK AGES (recombination z=1100 -> cosmic dawn z=30):')
print(f'  coordinate time: t(1100)={t_of_z(1100)/yr/1e6:.2f} Myr -> '
      f't(30)={t_of_z(30)/yr/1e6:.1f} Myr  (Delta ln a = {np.log(1101/31):.2f})')
dbar = (cum_bar[i30]-cum_bar[i1100]); dstr = (cum_struct[i30]-cum_struct[i1100])
print(f'  baryonic channel ticks accumulated:      {dbar:.2e} k_B '
      f'({dbar/N_bary:.2e} k_B/baryon; mostly recombination-burst tail + first starlight)')
dcomp = C['compton'][i30]-C['compton'][i1100]
print(f'  ...of which residual Compton whisper (150>z>30 quiescent gas): '
      f'{dcomp:.2e} k_B = {dcomp/N_bary:.2f} k_B/baryon '
      f'(whisper over all time: {C["compton"][-1]:.2e})')
print(f'  grav-structure ticks accumulated:        {dstr:.2e} k_B')
print(f'  as fraction of each clock TO z=6 (end of dark ages):')
print(f'     Delta tau_bar  = {dbar/cum_bar[i6]:.2e}   '
      f'Delta tau_struct = {dstr/cum_struct[i6]:.2e}')
print(f'  as fraction of each clock to TODAY:')
print(f'     Delta tau_bar  = {dbar/cum_bar[-1]:.2e}   '
      f'Delta tau_struct = {dstr/cum_struct[-1]:.2e}   '
      f'Delta tau_grav = {(cum_grav[i30]-cum_grav[i1100])/cum_grav[-1]:.2e}')
print(f'  rate ratio grav/baryon: z=100: {rate_grav[iz(100)]/rate_bar[iz(100)]:.1e}'
      f'  z=50: {rate_grav[iz(50)]/rate_bar[iz(50)]:.1e}'
      f'  z=30: {rate_grav[iz(30)]/rate_bar[iz(30)]:.1e}'
      f'  z=17: {rate_grav[iz(17)]/rate_bar[iz(17)]:.1e}'
      f'  z=6: {rate_grav[iz(6)]/rate_bar[iz(6)]:.1e}'
      f'  z=2: {rate_grav[iz(2)]/rate_bar[iz(2)]:.1e}')
print(f'  Compton whisper decays ~(1+z)^1.5: rate(z=150)={ch["compton"][i150]:.2e}, '
      f'rate(z=17)={ch["compton"][i17]:.2e} k_B/lna')

# event-metered comparison -------------------------------------------------
for z in [1200, 300, 100, 17]:
    ev = 4.11e8*(1+z)**3 * sigT*c * x_e(z)/(1+f_He) / Hz(z)
    print(f'  event-metered (Thomson scatterings per baryon per ln a) z={z}: {ev:.2e}')

# median ticks and the future ----------------------------------------------
for name, tau in [('tau_bar',tau_bar),('tau_grav',tau_grav),('tau_DM(struct)',tau_struct)]:
    zmed = zg[np.argmin(np.abs(tau-0.5))]
    print(f'  median tick of {name}: z = {zmed:.2f}')
nu_now, nu_inf = delc/(sig_mini*1.0), delc/(sig_mini*D_inf)
F_now, F_inf = erfc(nu_now/np.sqrt(2)), erfc(nu_inf/np.sqrt(2))
print(f'\nfuture of the DM clock: F_coll(today)={F_now:.3f}, F_coll(a->inf)={F_inf:.3f}'
      f'  -> fraction of all dark-sector ticks already spent: {F_now/F_inf:.3f}')

# ----------------------------------------------------------------------
# figures + csv
# ----------------------------------------------------------------------
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))
cols = {'silk':'#888','recomb':'#c69','compton':'#c33','reion_y':'#e94',
        'stars':'#d81','struct':'#2a7','stellarBH':'#46c','SMBH':'#219'}
for k in ch:
    ax[0].loglog(1+zg, np.maximum(ch[k],1e60), color=cols[k], label=k)
ax[0].loglog(1+zg, np.maximum(rate_tot,1e60), 'k--', lw=1, label='total')
ax[0].set(xlabel='1+z', ylabel=r'$dS/d\ln a$  [$k_B$, obs. universe]',
          ylim=(1e66,1e106), xlim=(1,3e6), title='entropy-production budget by channel')
ax[0].invert_xaxis(); ax[0].legend(fontsize=8, ncol=2)
ax[1].semilogx(1+zg, tau_bar, '#c33', label=r'$\tau_{\rm baryon}$')
ax[1].semilogx(1+zg, tau_grav, '#219', label=r'$\tau_{\rm grav}$ (BH-dominated)')
ax[1].semilogx(1+zg, tau_struct, '#2a7', label=r'$\tau_{\rm DM}$ (structure only)')
ax[1].axvspan(31, 1101, alpha=0.12, color='k')
ax[1].text(180, 0.55, 'dark ages', fontsize=9)
ax[1].set(xlabel='1+z', ylabel=r'entropic clock  $\tau_i$', xlim=(1,3e3),
          title='two-clock construction'); ax[1].invert_xaxis(); ax[1].legend()
fig.tight_layout()
out = __file__.rsplit('/',1)[0]
fig.savefig(out+'/tick_census.png', dpi=140)

np.savetxt(out+'/tick_census_grid.csv',
           np.column_stack([zg]+[ch[k] for k in ch]+[tau_bar,tau_grav,tau_struct]),
           delimiter=',', header='z,'+','.join(ch)+',tau_bar,tau_grav,tau_DM',
           comments='')
print('\nwrote tick_census.png, tick_census_grid.csv')
