import numpy as np
G=6.674e-11; c=2.998e8; hbar=1.0546e-34; Msun=1.989e30; eV=1.602e-19; yr=3.156e7

def tg(M): return G*M*Msun/c**3           # GM/c^3 in s, M in Msun
def alpha(M,mu): return G*M*Msun*(mu*eV/c**2)/(hbar*c)

# Detweiler small-alpha rate, scalar, mode (n=l+1, l, m): 
# Gamma = 2 rtp * C_nl * g_lm(a*) * (m OmegaH - omega) * alpha^(4l+4) * (mu c^2/hbar)... 
# use widely-quoted compact l=m=1 nodeless: Gamma_211 = (1/24) (a* - 2 alpha rtp) alpha^8 * (mu c^2/hbar)
# general leading factor for l: C_l with Gamma ~ alpha^(4l+5) mu when written with (m OmegaH - w) ~ mu*(...)/alpha... 
# We implement l=m=1 (1/24) and l=m=2 (4/885779... ) via Detweiler C_nl:
# C_nl = (2^(4l+1) (n+l)! / (n^(2l+4) (n-l-1)!)) * (l! / ((2l)!(2l+1)!))^2 * prod_{j=1}^{l} (j^2 (1-a*^2) + (a* m - 2 rtp alpha)^2)
# with n = principal number (n >= l+1); Gamma = C_nl * (a* m - 2 rtp alpha)... standard:
def gamma_detweiler(M, mu, astar, l, m, n):
    al = alpha(M,mu)
    rtp = 1+np.sqrt(1-astar**2)
    x = astar*m - 2*al*rtp          # ~ 2 rtp (m OmegaH - omega)/ (c^3/GM)
    from math import factorial
    Cnl = (2.0**(4*l+1) * factorial(n+l) / (n**(2*l+4) * factorial(n-l-1))) \
          * (factorial(l)/(factorial(2*l)*factorial(2*l+1)))**2
    prod = 1.0
    for j in range(1,l+1):
        prod *= (j**2*(1-astar**2) + x**2)
    om = mu*eV/hbar                 # omega ~ mu c^2/hbar
    return Cnl * prod * x * al**(4*l+4) * om   # s^-1

# check 211 against 1/24 a* alpha^8 mu form at small alpha:
M=10.; astar=0.9; mu=2.7e-13   # alpha ~ 0.02
al=alpha(M,mu)
g=gamma_detweiler(M,mu,astar,1,1,2)
approx = (1/24)*(astar-2*al*(1+np.sqrt(1-astar**2)))*al**8*(mu*eV/hbar)
print("alpha=",al," Gamma_211 full=",g," 1/24-form=",approx, " ratio=",g/approx)

# max growth benchmark vs Dolan: alpha=0.3, a*=0.99
for al_t,ast in [(0.3,0.99),(0.42,0.99)]:
    mu_t = al_t*hbar*c/(G*10*Msun)*c**2/eV
    gg=gamma_detweiler(10,mu_t,ast,1,1,2)
    print(f"alpha={al_t}, a*={ast}: Gamma*GM/c^3 = {gg*tg(10):.3e}  (Dolan numeric max ~1.5e-7 at 0.42)")

# instability e-fold count to grow cloud from single quantum to N~1e77-78: ln N ~ 180
NE=180.
def tau_sr(M,mu,astar,l,m,n):
    g=gamma_detweiler(M,mu,astar,l,m,n)
    return NE/g if g>0 else np.inf

# Exclusion windows: scan mu, require tau_sr < t_limit for m=1 (n=2) or m=2 (n=3)
def window(M, astar, t_limit_yr, modes=((1,1,2),(2,2,3))):
    mus=np.logspace(-22,-9,4000)
    ok=np.zeros_like(mus,dtype=bool)
    for (l,m,n) in modes:
        taus=np.array([tau_sr(M,mu,astar,l,m,n) for mu in mus])
        ok |= (taus < t_limit_yr*yr)
    if ok.any():
        return mus[ok].min(), mus[ok].max()
    return None

tSal=4.5e7 # yr, Salpeter
for (M,ast,tl,tag) in [(5,0.9,1e7,"5Msun t=1e7yr"),(10,0.9,tSal,"10Msun tSal"),(21,0.95,5e6,"CygX1-ish t=5Myr"),
                       (30,0.9,tSal,"30Msun tSal"),(14,0.98,4e9,"GRS1915 t~Gyr... use tSal below"),
                       (14,0.98,tSal,"GRS1915 tSal"),
                       (1e6,0.9,tSal,"1e6 SMBH tSal"),(1e7,0.9,tSal,"1e7"),(1e8,0.9,tSal,"1e8"),(1e9,0.9,tSal,"1e9")]:
    w=window(M,ast,tl)
    print(f"{tag:22s} M={M:9.3g} a*={ast}: excluded mu = [{w[0]:.2e}, {w[1]:.2e}] eV" if w else f"{tag}: none")
