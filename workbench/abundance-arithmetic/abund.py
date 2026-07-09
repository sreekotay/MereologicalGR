import numpy as np

# Constants (GeV units)
Mp   = 2.435e18      # reduced Planck mass
mp   = 0.9383
eta  = 6.1e-10
Obh2 = 0.02237
Och2 = 0.1200
print("Omega_c/Omega_b =", Och2/Obh2)

# Omega h^2 = 2.755e8 (m/GeV) Y  ;  Y=n/s
def Oh2(m,Y): return 2.755e8*m*Y
mY_target = 0.12/2.755e8
print("required m*Y for Oh2=0.12 : %.3e GeV"%mY_target)
Yb = eta*(0.278)/... if False else None
# baryon Yield: n_b/s = eta * n_gamma/s = eta/7.04
Yb = eta/7.04
print("Y_b = %.3e ; m_p Y_b = %.3e GeV ; ratio target mY/mpYb = %.2f"%(Yb, mp*Yb, mY_target/(mp*Yb)))

print("\n--- A1: Planck-suppressed reheating ---")
for mphi in [3e13, 1e13, 1e10]:
    Gam = mphi**3/(8*np.pi*Mp**2)
    g=106.75
    Treh = (90/(np.pi**2*g))**0.25*np.sqrt(Gam*Mp)
    print("m_phi=%.0e  Gamma=%.2e GeV  T_reh=%.2e GeV"%(mphi,Gam,Treh))
Treh_grav = (90/(np.pi**2*106.75))**0.25*np.sqrt((3e13)**3/(8*np.pi*Mp**2)*Mp)
Teq = 0.80e-9   # GeV, matter-radiation equality temperature ~0.80 eV
print("Overclosure: O(1) energy branching to stable matter needs f ~ T_eq/T_reh = %.1e"%(Teq/Treh_grav))
# hot-relic option: species decoupling relativistic with temperature ratio xi
# Omega h2 = (m/93 eV) * (g_ch/2) * xi^3 *(3/4 fermion)... use standard: Oh2 = m/(93.14 eV) * xi^3 * (g_eff/1.5)
for xi in [1.0,0.5,0.3]:
    m_needed = 93.14e-9*0.12/ (xi**3)   # GeV, g_eff~1.5 (one Weyl fermion)
    print("xi=%.1f -> hot-relic m_chi = %.1f eV  (HDM: excluded by Ly-alpha/structure)"%(xi,m_needed*1e9))

print("\n--- A2: PIDM graviton-mediated freeze-in (light m_chi << T_reh) ---")
# my derivation Y = C T_reh^3/(480 Mp^3), C = O(1) summed SM dof
C=1.0
for Trh in [1e15,1e14,1e13,6.6e15]:
    Y = C*Trh**3/(480*Mp**3)
    m_need = mY_target/Y
    print("T_reh=%.1e -> Y=%.2e -> m_chi for Oh2=0.12: %.2e GeV"%(Trh,Y,m_need))
# sensitivity: Omega ~ m T_reh^3 => d(ratio 5.4) requires both knobs
print("Omega scales as m_chi * T_reh^3 : ratio 5.4 = coincidence of two free parameters")

print("\n--- A3: gravitational production from expansion (Ford/CKR) ---")
# Y = f * H_e * T_reh /(4 Mp^2), m ~ H_e, f~1e-2 (exp suppressed for m>H_e)
f=1e-2
for (m,Trh) in [(1e11,1e9),(1e13,1e9),(1e11,1e5),(2e13,1e10)]:
    He=m  # m ~ H_inf for unsuppressed production
    Y=f*He*Trh/(4*Mp**2)
    print("m=H_e=%.0e T_reh=%.0e -> Oh2 = %.2e"%(m,Trh,Oh2(m,Y)))
# exponential sensitivity
print("for m > H_e: n ~ exp(-c m/H_e), c~few => Omega exponentially sensitive to m/H_inf")

print("\n--- B: inflaton branching ---")
# Y_chi = Br * (3/4) T_reh/m_phi  (1 chi per decay)
def Br_needed(mchi,Trh,mphi): return mY_target/( mchi*0.75*Trh/mphi )
for (mchi,Trh,mphi) in [(100,1e10,3e13),(1e3,1e10,3e13),(1e10,1e10,3e13),(1e13,1e10,3e13),(100,1e6,3e13)]:
    print("m_chi=%.0e T_reh=%.0e m_phi=%.0e -> Br_chi = %.2e"%(mchi,Trh,mphi,Br_needed(mchi,Trh,mphi)))
# Br=1 corner
for (Trh,mphi) in [(1e10,3e13),(1e12,3e13),(1e9,1e13)]:
    mchi = mY_target*mphi/(0.75*Trh)
    T_NR = 2*mchi*Trh/mphi   # temperature when p ~ m (p birth = mphi/2)
    print("Br=1: T_reh=%.0e m_phi=%.0e -> m_chi=%.2e GeV ; becomes NR at T=%.2e GeV"%(Trh,mphi,mchi,T_NR))
# warmness bound: require NR before T ~ 1 keV (conservative Ly-alpha proxy)
for (Trh,mphi) in [(1e10,3e13)]:
    mchi_min = 1e-6*mphi/(2*Trh)   # T_NR > 1e-6 GeV
    Br_max = Br_needed(mchi_min,Trh,mphi)
    print("coldness (T_NR>keV): m_chi > %.1f GeV -> Br_chi < %.1e"%(mchi_min,Br_max))

print("\n--- C: mirror sector ---")
# Delta Neff = (4/7) g'*(T') x^4 ; g'*=10.75 at BBN
for x in [1.0,0.5,0.47,0.3,0.2]:
    dN_bbn = 4/7*10.75*x**4
    dN_cmb = 3.36*x**4/(7/8*2*(4/11)**(4/3))
    print("x=%.2f : dNeff(BBN)=%.3f  dNeff(CMB)=%.3f"%(x,dN_bbn,dN_cmb))
print("Planck dNeff<0.30 -> x < %.3f (BBN norm) / %.3f (CMB norm)"%((0.30/6.14)**0.25,(0.30/7.40)**0.25))
print("CMB-S4 dNeff<0.06 -> x < %.3f"%((0.06/6.14)**0.25))
print("ratio: Omega'/Omega_b = (m'/m_p)(eta'/eta) -> 5.4 needs eta'/eta = 5.4 for exact mirror")
