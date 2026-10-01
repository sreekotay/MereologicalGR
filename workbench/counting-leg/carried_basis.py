"""The carried-basis face of frame transport (Thomas precession) from counts.

Claim under test: carried-basis transport needs no adjacency leg as an input. The space of
flows (unit timelike directions) is hyperbolic; distances in it are rapidities; rapidities are
Doppler count ratios (Bondi k = e^eta: pure ordering + counts). A gyroscope's precession around
a closed velocity loop is the loop's enclosed area, and the area is fixed by pairwise rapidities
alone (triangulate, three sides per triangle). So: Thomas precession from count ratios only.
Independent referee: Fermi-Walker transport integrated along a circular orbit.
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

checks = []
def check(name, ok):
    checks.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)

# ---- 1. Bondi k: rapidity is a count ratio -------------------------------------------------------
eta_, T = sp.symbols('eta T', positive=True)
# A at rest at x=0; B through the origin with rapidity eta. A emits light at own count T;
# it reaches B when t = T + x and x = tanh(eta) t; B's count there is t / cosh(eta).
tB = sp.solve(sp.Eq(sp.Symbol('t'), T + sp.tanh(eta_)*sp.Symbol('t')), sp.Symbol('t'))[0]
kfac = sp.simplify((tB/sp.cosh(eta_))/T)
check("1. Bondi k = (B's count)/(A's count) = e^eta: rapidity = ln of a count ratio",
      sp.simplify(kfac - sp.exp(eta_)) == 0)

# ---- 2. Thomas angle from pairwise rapidities only --------------------------------------------------
def tri_area(a, b, c):
    """hyperbolic triangle (curvature -1) from its three side lengths: pi - sum of angles."""
    def ang(opp, s1, s2):
        cosA = (np.cosh(s1)*np.cosh(s2) - np.cosh(opp))/(np.sinh(s1)*np.sinh(s2))
        return np.arccos(np.clip(cosA, -1, 1))
    return np.pi - ang(a, b, c) - ang(b, c, a) - ang(c, a, b)

def rapidity(u, w):          # from the count ratio: eta = ln k; here via -u.w = cosh(eta)
    return np.arccosh(max(1.0, u[0]*w[0] - u[1]*w[1] - u[2]*w[2]))

def thomas_from_counts(v, N):
    g = 1/np.sqrt(1 - v**2)
    u0 = np.array([1.0, 0, 0])                                  # the lab flow
    us = [np.array([g, g*v*np.cos(p), g*v*np.sin(p)]) for p in np.linspace(0, 2*np.pi, N, endpoint=False)]
    area = 0.0
    for i in range(N):
        ui, uj = us[i], us[(i + 1) % N]
        area += tri_area(rapidity(ui, uj), rapidity(u0, uj), rapidity(u0, ui))
    return area

for v in [0.3, 0.8, 0.99]:
    g = 1/np.sqrt(1 - v**2)
    A = thomas_from_counts(v, 4000)
    print(f"   v = {v}: area from pairwise rapidities = {A:.6f}   2 pi (gamma - 1) = {2*np.pi*(g-1):.6f}")
    check(f"2. v={v}: velocity-loop area from count ratios = 2 pi (gamma - 1)", abs(A/(2*np.pi*(g - 1)) - 1) < 1e-4)

# ---- 3. independent referee: Fermi-Walker transport along the orbit ---------------------------------
def fw_angle(v, R=1.0):
    g = 1/np.sqrt(1 - v**2); w = v/R
    eta = np.diag([-1.0, 1, 1])
    def u(tau):
        ph = w*g*tau
        return np.array([g, -g*v*np.sin(ph), g*v*np.cos(ph)])
    def acc(tau):
        ph = w*g*tau
        return np.array([0.0, -g*v*w*g*np.cos(ph), -g*v*w*g*np.sin(ph)])
    def rhs(tau, S):
        U, A = u(tau), acc(tau)
        return U*(A @ eta @ S) - A*(U @ eta @ S)      # dS/dtau = u (a.S) - a (u.S)
    S0 = np.array([0.0, 1.0, 0.0])                      # spatial, orthogonal to u(0) = (g, 0, g v)
    Tp = 2*np.pi/(w*g)                                  # one orbit in proper time
    sol = solve_ivp(rhs, (0, Tp), S0, rtol=1e-12, atol=1e-14)
    S1 = sol.y[:, -1]
    # u returns to u(0); compare S1 with S0 inside u(0)'s rest space, in the lab orbit plane
    # S1 lies in span{x, boosted y}: x-component gives cos(angle)
    return np.arccos(np.clip(S1[1], -1, 1))

for v in [0.3, 0.8]:
    g = 1/np.sqrt(1 - v**2)
    ang = fw_angle(v)
    exp = (2*np.pi*(g - 1)) % (2*np.pi)
    exp = min(exp, 2*np.pi - exp)
    print(f"   v = {v}: Fermi-Walker gyroscope turns {ang:.6f} per orbit;  2 pi (gamma-1) mod 2 pi = {exp:.6f}")
    check(f"3. v={v}: Fermi-Walker precession per orbit = 2 pi (gamma - 1) (mod 2 pi)", abs(ang - exp) < 1e-6)

print()
print(f"{sum(o for _, o in checks)}/{len(checks)} checks passed")
