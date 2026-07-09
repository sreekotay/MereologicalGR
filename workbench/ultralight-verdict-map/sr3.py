import numpy as np
# natural-unit bosenova / quench estimate
Mpl_GeV = 1.221e19   # non-reduced Planck mass
Msun_kg=1.989e30; Mpl_kg=2.176e-8

def MoverMpl2(M_Msun): return (M_Msun*Msun_kg/Mpl_kg)**2

# N needed to change spin by da*: J_BH = a* G M^2/c = a* M^2/Mpl^2 (hbar units); each boson carries m*hbar
def N_spin(M_Msun, dastar, m=1): return dastar*MoverMpl2(M_Msun)/m

# bosenova threshold (Arvanitaki-Dubovsky/Yoshino-Kodama scaling, c0~5):
def N_bose(M_Msun, al, f_GeV, n=2, c0=5.0):
    return c0*(n**4/al**3)*MoverMpl2(M_Msun)*(f_GeV/Mpl_GeV)**2

# single-episode quench condition N_bose < N_spin -> f below f_crit
def f_crit_single(al, dastar=0.1, n=2, m=1, c0=5.0):
    return Mpl_GeV*np.sqrt(dastar*al**3/(m*c0*n**4))

for al in [0.1,0.2,0.4]:
    print(f"alpha={al}: single-bosenova f_crit = {f_crit_single(al):.2e} GeV ; N_bose(10Msun,f=1e15GeV)={N_bose(10,al,1e15):.2e}, N_spin(10Msun,da*=0.1)={N_spin(10,0.1):.2e}")

# BUT cloud regrows: number of bosenova cycles in time T ~ T * Gamma_SR / ln(N_bose->refill ~ few efolds)
# effective quench requires  N_bose * (T Gamma / few) < N_spin
G=6.674e-11; c=2.998e8; hbar=1.0546e-34; eV=1.602e-19; yr=3.156e7
def tg(M): return G*M*Msun_kg/c**3
# Gamma_211 ~ (1/48)*prod*x*al^8 * mu/hbar; use a*=0.9 typical
def Gam(M,al,astar=0.9):
    rtp=1+np.sqrt(1-astar**2); x=astar-2*al*rtp
    prod=(1-astar**2)+x**2
    mu_s = al/tg(M)   # omega in 1/s
    return (1/48)*prod*max(x,0)*al**8*mu_s

for al in [0.1,0.2,0.3]:
    M=10; T=4.5e7*yr
    Ncyc = T*Gam(M,al)/10.0     # ~10 e-folds to regrow after collapse (cloud not fully destroyed)
    fq = f_crit_single(al)*np.sqrt(1/max(Ncyc,1)) if Ncyc>1 else f_crit_single(al)
    print(f"alpha={al}: Gamma={Gam(10,al):.2e}/s, cycles in Salpeter={Ncyc:.2e}, repeated-bosenova f_quench ~ {fq:.2e} GeV")
