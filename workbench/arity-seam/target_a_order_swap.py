"""Target A: branch-dependent gravitational time dilation and coordinate-order swap.

Derivation (weak field, static clocks):
  proper time on a clock at fixed x:  dtau = (1 + Phi(x)/c^2) dt,  Phi < 0.
  Event defined as "clock X reads tau_X*" occurs at coordinate time
     t_X = tau_X* / (1 + Phi(x_X)/c^2)  ~=  tau_X* (1 - Phi(x_X)/c^2).

  Branch b of the source mass gives potential Phi_b(x). Coordinate separation
  of the two events in branch b:
     dt^(b) = t_B^(b) - t_A^(b)
            = (tau_B* - tau_A*) - [tau_B* Phi_b(x_B) - tau_A* Phi_b(x_A)]/c^2.

  Branch difference (the dilation-induced shift), with tau_A* ~ tau_B* ~ T:
     dt^(2) - dt^(1) = [tau_A* dPhi_A - tau_B* dPhi_B]/c^2
                     ~= (T/c^2) * (dPhi_A - dPhi_B)  ==  T * DPhi / c^2,
  where dPhi_X = Phi_2(x_X) - Phi_1(x_X) and DPhi is the branch-difference of
  the A-B potential difference (a DIFFERENTIAL redshift: a common shift of both
  clocks cancels).

  Order swap: dt^(1) > 0 and dt^(2) < 0  <=>  T*DPhi/c^2 > dt^(1)  (shift
  opposing the initial order). If both orderings must be RESOLVABLE at timing
  precision sigma_t (|dt^(1)|, |dt^(2)| >= sigma_t), then
     T * DPhi / c^2  >=  |dt^(1)| + |dt^(2)|  >=  2 sigma_t
  =>   DPhi / c^2  >=  2 sigma_t / T.        (exact factor: 2)

  Source conversion: mass M at distance r from clock B in one branch, displaced
  by dr in the other (far from clock A):
     DPhi = GM (1/r - 1/(r+dr)) = (GM/r) * dr/(r+dr)
          ~= GM dr / r^2   (dr << r);   saturates at GM/r for dr >~ r.
  Maximal-geometry requirement:
     M/r >= 2 sigma_t c^2 / (G T),   or generally  M dr / r^2 >= 2 sigma_t c^2/(G T).
"""
import math

G = 6.67430e-11
c = 2.99792458e8
c2 = c*c

def M_over_r_required(sigma_t, T, factor=2.0):
    """kg/m needed for order swap (dr ~ r geometry)."""
    return factor * sigma_t * c2 / (G * T)

print("c^2/G = %.4e kg/m per unit of DPhi/c^2" % (c2/G))
cases = [("(i)  sigma_t=1 fs,  T=1 s",   1e-15, 1.0),
         ("(ii) sigma_t=1 ns,  T=1 s",   1e-9,  1.0),
         ("(iii)sigma_t=1 us,  T=100 s", 1e-6,  100.0)]
for label, s, T in cases:
    req = 2*s/T
    mr = M_over_r_required(s, T)
    print("%s : DPhi/c^2 >= %.2e ; M/r >= %.3e kg/m (factor-2), %.3e (order-of-mag, no 2)"
          % (label, req, mr, mr/2))
    # example bodies
    print("    e.g. M at r=1 m: M = %.2e kg ; sphere rho=3000 kg/m^3 -> radius %.0f m"
          % (mr, (3*mr/(4*math.pi*3000))**(1/3)))

# reference: Earth's surface M/R
M_E, R_E = 5.972e24, 6.371e6
print("Earth M/R = %.3e kg/m  (surface potential/c^2 = %.2e)" % (M_E/R_E, G*M_E/(R_E*c2)))

# ---- (3) BMV regime sanity check ----
m, d, T_bmv = 1e-14, 200e-6, 2.5
dPhi_c2 = G*m/(d*c2)                    # full potential of partner mass at closest approach
shift = T_bmv * dPhi_c2
print("\nBMV: m=1e-14 kg, d=200 um:")
print("  DPhi/c^2 (max, Gm/(d c^2))      = %.3e" % dPhi_c2)
# differential across the four configs (250 um split): 1/200um - 1/700um
dPhi_diff = G*m*(1/200e-6 - 1/700e-6)/c2
print("  DPhi/c^2 (config differential)  = %.3e" % dPhi_diff)
print("  time-order shift over T=2.5 s   = %.3e s" % shift)
t_planck = 5.391e-44
print("  = %.1e Planck times; %.1f orders below 1 fs; %.1f orders below 1 zs"
      % (shift/t_planck, math.log10(1e-15/shift), math.log10(1e-21/shift)))
# why phases still work: Compton-frequency amplifier
hbar = 1.054571817e-34
omega_C = m*c2/hbar
print("  Compton frequency m c^2/hbar = %.2e rad/s ->" % omega_C)
print("  phase = (DPhi/c^2)*omega_C*T = %.2f rad (vs order shift %.1e s)"
      % (dPhi_c2*omega_C*T_bmv, shift))
