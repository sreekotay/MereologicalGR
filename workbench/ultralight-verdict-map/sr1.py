import numpy as np

# constants (SI)
G=6.674e-11; c=2.998e8; hbar=1.0546e-34; Msun=1.989e30; eV=1.602e-19
yr=3.156e7

# alpha = G M mu / (hbar c) with mu = mass;  mu_eV = mu c^2 / eV
def alpha(M_Msun, mu_eV):
    mu = mu_eV*eV/c**2
    return G*(M_Msun*Msun)*mu/(hbar*c)

# invert: mu_eV for given alpha, M
def mu_of_alpha(al, M_Msun):
    return al*hbar*c/(G*M_Msun*Msun) * c**2/eV

print("check alpha(10 Msun, 1e-12 eV) =", alpha(10,1e-12))
print("alpha = 0.75 * (M/10Msun) * (mu/1e-12 eV)?  ->", alpha(10,1e-12)/0.75)

for M in [5,10,30,60,1e6,1e7,1e8,1e9,6.5e9]:
    print(f"M={M:9.3g} Msun: mu(alpha=0.02)={mu_of_alpha(0.02,M):8.2e} eV, mu(0.1)={mu_of_alpha(0.1,M):8.2e}, mu(0.5)={mu_of_alpha(0.5,M):8.2e} eV")

# GM/c^3 timescale
def tg(M_Msun): return G*M_Msun*Msun/c**3
print("GM/c^3 (10 Msun) =", tg(10), "s ; (1e8 Msun)=", tg(1e8), "s")

# Horizon angular velocity, Kerr: Omega_H = (a*/2r+) c^3/(GM), rp = 1+sqrt(1-a*^2) in GM/c^2 units
def OmegaH(M_Msun,astar):
    rp = 1+np.sqrt(1-astar**2)
    return astar/(2*rp) / tg(M_Msun)

# superradiance condition omega ~ mu c^2/hbar < m * OmegaH
# => alpha < m * a*/(2 rp)   (since omega*GM/c^3 = alpha at leading order)
for astar in [0.5,0.9,0.998]:
    rp=1+np.sqrt(1-astar**2)
    print(f"a*={astar}: SR condition alpha < m*a*/(2rp) = {astar/(2*rp):.4f} * m")
