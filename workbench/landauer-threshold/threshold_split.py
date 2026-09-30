#!/usr/bin/env python3
"""
Does the finite-time Landauer excess carry the erasure threshold?

a5 §8.1 reads the erasure invoice as a count/duration split:

    W = kT ln2            +  B/tau
        count-metered        duration-metered
        (per bit,            (finite-time
         duration-blind)      dissipation)

PB-2.2 rides on the first term being a COUNT, not a duration. The open question
(this run): is B independent of the success threshold p, or does the threshold
leak into the duration term?

PRIOR ART -- this run rederives published structure. Proesmans, Ehrich &
Bechhoefer, "Finite-Time Landauer Principle" (arXiv:2006.03242, PRL) and
"Optimal finite-time bit erasure under full control" (arXiv:2006.03240) give
W >= kT ln2 + gamma D(p_i,p_f)^2/tau, and state the imperfect-erasure case as
an explicit h(eps) vanishing as eps -> 0. The threshold dependence of the excess
is therefore NOT a finding here. The crossover below is arithmetic on those two
published terms. What this run is for is internal: it corrects a5 §8.1's
independent-metering reading and bounds where PB-2.2 may cite this register.

IMPORTED (Layer 3):
  imperfect-erasure bound   W_min(p) = kT[ln2 - H(p)],  H in nats
                            (Dillenschneider-Lutz class; generalized Landauer)
  finite-time excess        W_ex >= W_2(rho_i, rho_f)^2 / (mu tau)
                            with mu = 1/gamma the mobility and W_2 the
                            2-Wasserstein distance -- the refined second law
                            for fast processes (Aurell et al.; Dechant;
                            Van Vu & Hasegawa). Saturable by optimal transport.
  Berut et al. 2012 apparatus scale (silica bead in water, two wells ~1 um)

PROJECTED (Layer 2, computed here):
  B(p) from the transport distance of a p-dependent final distribution
  the crossover tau*(p) where the two terms cross
  the divergence of tau* as the threshold relaxes
"""
import math

kB   = 1.380649e-23
T    = 300.0
kT   = kB*T
eta  = 1.0e-3          # water, Pa s
a    = 1.0e-6          # bead radius, m
gam  = 6*math.pi*eta*a # Stokes drag
L    = 1.0e-6          # well separation, m
ln2  = math.log(2.0)

def H(p):
    "Shannon entropy in nats of (p, 1-p)"
    if p <= 0 or p >= 1: return 0.0
    return -(p*math.log(p) + (1-p)*math.log(1-p))

def W_bound(p):
    "count term: the imperfect-erasure bound, duration-blind"
    return kT*(ln2 - H(p))

def W2sq(p):
    """transport cost of the p-dependent final distribution.

    initial   (1/2, 1/2)  over wells {0, 1}
    final     (p, 1-p)    -- success probability p into well 0
    mass moved = 1/2 - (1-p) = p - 1/2, each over distance L
    W_2^2 = (mass moved) * L^2
    """
    return max(p-0.5, 0.0) * L*L

def B(p):
    "duration term coefficient: W_ex = B(p)/tau"
    return W2sq(p)*gam

def tau_star(p):
    "crossover: B(p)/tau = W_bound(p)"
    b = W_bound(p)
    return B(p)/b if b > 0 else float('inf')

print(f"kT = {kT:.3e} J   gamma = {gam:.3e} kg/s   L = {L:.1e} m")
print(f"kT ln2 = {kT*ln2:.3e} J\n")
print(f"{'p':>7} {'count kT[ln2-H]':>18} {'B(p) [J s]':>14} {'tau* [s]':>12}")
for p in (0.50, 0.55, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99, 0.999, 1.0):
    print(f"{p:7.3f} {W_bound(p)/kT:18.4f} {B(p):14.3e} {tau_star(p):12.3f}")

print("\n-- outcome: correction, not finding (prior art above) --")
print("1. B depends on p. B(p) = (p - 1/2) L^2 gamma, linear in the threshold,")
print("   zero at p = 1/2 (nothing to erase), maximal at p = 1.")
print("   So the two terms are NOT independently metered: both carry p.")
print("2. What survives: the bound is still duration-blind (no tau anywhere in")
print("   W_bound). 'Count, not duration' holds for the bound; 'independent")
print("   metering' does not.")

# asymptotics of the crossover as the threshold relaxes
print("\n3. Crossover asymptotics. Put p = 1/2 + e:")
print("   ln2 - H(1/2+e) = 2e^2 + O(e^4);  B ∝ e")
print("   => tau*(e) ∝ e/e^2 = 1/e  -- DIVERGES as the threshold relaxes.")
for e in (0.2, 0.1, 0.05, 0.02, 0.01):
    p = 0.5+e
    exact = tau_star(p)
    approx = (e*L*L*gam)/(kT*2*e*e)
    print(f"     e={e:5.3f}  tau*_exact={exact:9.3f} s   1/e form={approx:9.3f} s")

print("\n4. Strict limit p -> 1:")
tinf = (0.5*L*L*gam)/(kT*ln2)
print(f"   tau* -> L^2 gamma /(2 kT ln2) = {tinf:.2f} s  (a diffusive crossing time)")
print(f"   Berut et al. ran tau ~ 5-40 s, so tau* ~ {tinf:.1f} s sits at the")
print("   bottom of their range: shortest runs near crossover, longest")
print("   count-dominated. Consistent with the measured approach to kT ln2.")

print("\n5. CAVEATS. Point wells: real W_2 includes intra-well spread, adding a")
print("   p-independent B_0, so B(p) = B_0 + (p-1/2)L^2 gamma and B does not")
print("   vanish at p=1/2. The bound is saturable only by optimal protocols, so")
print("   measured B exceeds this; the scaling is the claim, not the coefficient.")
print("\n6. Consequence for a5 §8.1: the split needs one qualifier. The bound is")
print("   count-metered and duration-blind (PB-2.2's form survives). The excess")
print("   is duration-metered with a THRESHOLD-DEPENDENT coefficient, so the")
print("   two terms share the p dependence and are not separately dialable.")
print("   The threshold is not a knob on the count alone -- it moves both.")
