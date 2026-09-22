#!/usr/bin/env python3
"""Finite-dimensional/symbolic checks of the B-series' scoped relationships.

These checks validate identities and counterexamples, not continuum QFT theorems,
experimental performance, or historical priority. Run with Python 3, numpy,
scipy and sympy. A failed check raises AssertionError and returns nonzero.
"""
from __future__ import annotations

import numpy as np
import sympy as sp
from scipy.linalg import expm

ATOL = 2e-11
CHECKS: list[str] = []


def checked(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)
    CHECKS.append(name)
    print(f"PASS  {name}")


def close(a: object, b: object) -> bool:
    return bool(np.allclose(a, b, atol=ATOL, rtol=ATOL))


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def entropy(rho: np.ndarray) -> float:
    eigenvalues = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
    if eigenvalues.min() < -ATOL:
        raise ValueError("Input is not a positive density matrix")
    eigenvalues = eigenvalues[eigenvalues > 1e-14]
    return float(-np.sum(eigenvalues * np.log(eigenvalues)))


def partials(rho: np.ndarray, da: int, db: int) -> tuple[np.ndarray, np.ndarray]:
    tensor = rho.reshape(da, db, da, db)
    return np.trace(tensor, axis1=1, axis2=3), np.trace(tensor, axis1=0, axis2=2)


def local(a: np.ndarray, site: int, count: int) -> np.ndarray:
    result = np.array([[1.0]], dtype=complex)
    for j in range(count):
        result = np.kron(result, a if j == site else np.eye(2))
    return result


def main() -> None:
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.diag([1.0, -1.0]).astype(complex)
    ident = np.eye(2)

    # B1: order-exchange residue and independent tensor-factor operations.
    ax, bz = np.kron(x, ident), np.kron(ident, z)
    checked("B1 separated-factor generators commute", close(comm(ax, bz), 0))
    ua, ub = expm(-0.31j * ax), expm(-0.47j * bz)
    checked("B1 commuting local operations are order-independent", close(ua @ ub, ub @ ua))
    checked("B1 noncommuting orderings have a nonzero residue", np.linalg.norm(comm(x, z)) > 1)
    # Vanishing in one state is weaker than operator commutativity.
    checked("B1 one vanishing expectation does not imply zero operator", close(np.trace(comm(x, z)) / 2, 0) and not close(comm(x, z), 0))

    # B2: a reparametrized clock changes a derivative, not the physical history.
    h0, scale, sigma = sp.symbols('H0 scale sigma', positive=True)
    expansion = sp.exp(h0*sigma/scale)
    checked("B2 clock normalization remains in inferred expansion", sp.simplify(sp.diff(expansion,sigma)/expansion-h0/scale) == 0)

    # B3: same input record, target and threshold; copying versus idle.
    input_sfr = np.zeros((8,8), dtype=complex)
    input_sfr[0,0] = input_sfr[6,6] = 0.5  # |000>, |110>; order S,F,R
    copy_fr = np.zeros((8,8), dtype=complex)
    for bits in range(8):
        copy_fr[bits ^ ((bits >> 1) & 1), bits] = 1
    copied_sfr = copy_fr@input_sfr@copy_fr.conj().T
    matched = [bits for bits in range(8) if ((bits >> 2) & 1) == (bits & 1)]
    checked("B3 copying input record completes target correlation", close(np.diag(copied_sfr)[matched].sum(),1))
    checked("B3 idle same-input operation does not complete target", close(np.diag(input_sfr)[matched].sum(),0.5))

    # B6: positivity and the KMS ratio (hbar = 1).
    q = sp.symbols('q', positive=True)
    n, d = (1 + q) / 2, (1 - q) / 2
    checked("B6 spectral positivity N+D=W+", sp.simplify(n + d - 1) == 0)
    checked("B6 spectral positivity N-D=W-", sp.simplify(n - d - q) == 0)
    for beta_omega in (0.03, 0.7, 4.0):
        weight = np.exp(-beta_omega)
        checked(f"B6 KMS coth ratio at beta*hbar*omega={beta_omega}", close((1 + weight) / (1 - weight), 1 / np.tanh(beta_omega / 2)))

    # B7: accelerated interval and exact proper-time geometry.
    a, s, t = sp.symbols('a s t', positive=True, real=True)
    interval = ((sp.sinh(a*s)-sp.sinh(a*t))**2 - (sp.cosh(a*s)-sp.cosh(a*t))**2) / a**2
    checked("B7 hyperbolic interval", sp.simplify(sp.expand_trig(interval) - 4*sp.sinh(a*(s-t)/2)**2/a**2) == 0)
    eta = sp.symbols('eta', real=True)
    u = sp.Matrix([sp.cosh(eta), sp.sinh(eta)])
    acceleration = sp.diff(u, eta)
    metric = sp.diag(-1, 1)
    checked("B7 u dot a = 0", sp.simplify((u.T*metric*acceleration)[0]) == 0)
    mass, mdot = sp.symbols('mass mdot', positive=True)
    force = mdot*u + mass*acceleration
    checked("B7 parallel force prices rest-energy change", sp.simplify(-(u.T*metric*force)[0]-mdot) == 0)

    # B8: fixed mean energy; different variance. hbar = 1, E0=3, Delta=1.
    energies = np.array([2.0, 3.0, 4.0])
    h = np.diag(energies)
    off = np.array([0.0, 1.0, 0.0])
    on = np.array([1.0, 0.0, 1.0]) / np.sqrt(2)
    checked("B8 matched mean internal energy", close(off @ h @ off, on @ h @ on))
    for dt in (0.0, 0.1, 0.4, 1.2):
        unitary = expm(-1j*h*dt)
        chi_off, chi_on = off @ unitary @ off, on @ unitary @ on
        checked(f"B8 matched-phase overlap at Delta*t={dt}", close(chi_off, np.exp(-3j*dt)) and close(chi_on, chi_off*np.cos(dt)))
    dt = 1e-4
    variance = on @ h @ h @ on - (on @ h @ on)**2
    chi = on @ expm(-1j*h*dt) @ on
    checked("B8 contrast curvature = energy variance/2", abs((1-abs(chi))/dt**2 - variance/2) < 1e-6)
    mixed = np.diag([0.5, 0.0, 0.5])
    unitary = expm(-0.8j*h)
    checked("B8 mixed stationary register can lose contrast", close(unitary@mixed@unitary.conj().T, mixed) and abs(np.trace(mixed@unitary)) < 0.8)

    # B9: no connecting nested commutator below graph distance.
    count = 4
    ham = np.zeros((2**count, 2**count), dtype=complex)
    for j in range(count - 1):
        for pauli in (x, y, z):
            ham += local(pauli,j,count) @ local(pauli,j+1,count)
    aa, bb = local(z,0,count), local(x,3,count)
    nested = aa.copy()
    for order in range(3):
        checked(f"B9 distance-3 support absent at nested order {order}", close(comm(nested, bb), 0))
        nested = comm(ham, nested)
    checked("B9 connecting term present at nested order 3", np.linalg.norm(comm(nested,bb)) > 0.1)
    alpha, clock = 1.7, 0.19
    ua = expm(1j*alpha*ham*clock)
    ub = expm(1j*ham*(alpha*clock))
    checked("B9 coupling rescaling changes time, not graph", close(ua@aa@ua.conj().T, ub@aa@ub.conj().T))

    # B10: marker-only unitary preserves overlap; unmarking uses correlations.
    marker0 = np.array([1.0,0.0], dtype=complex)
    marker1 = np.array([0.3, np.sqrt(0.91)], dtype=complex)
    um = expm(-0.7j*y)
    checked("B10 marker-only unitary preserves overlap", close(np.vdot(um@marker0,um@marker1),np.vdot(marker0,marker1)))
    copied = np.diag([0.5,0.0,0.0,0.5])
    cnot = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], dtype=complex)
    reset = cnot@copied@cnot.conj().T
    source, memory = partials(reset,2,2)
    checked("B10 correlated record reset leaves source intact", close(source,ident/2) and close(memory,np.diag([1.0,0.0])))
    checked("B10 conditional reset preserves joint entropy", abs(entropy(reset)-entropy(copied)) < ATOL)

    # Equality-form Landauer, initially product memory and Gibbs bath.
    beta = 0.8
    eb = np.array([0.0,0.9,1.8])
    weights = np.exp(-beta*eb); weights /= weights.sum()
    rb = np.diag(weights)
    rm = np.diag([0.65,0.35])
    initial = np.kron(rm,rb)
    rng = np.random.default_rng(230922)
    matrix = rng.normal(size=(6,6)) + 1j*rng.normal(size=(6,6))
    unitary = expm(-0.2j*(matrix+matrix.conj().T))
    final = unitary@initial@unitary.conj().T
    mf, bf = partials(final,2,3)
    heat = float(np.real(np.trace(np.diag(eb)@(bf-rb))))
    ds = entropy(rm)-entropy(mf)
    mutual = entropy(mf)+entropy(bf)-entropy(final)
    relative = -entropy(bf)-float(np.real(np.trace(bf@np.diag(np.log(weights)))))
    checked("B10 equality-form Landauer including correlations", abs(beta*heat-ds-mutual-relative) < ATOL)

    # B4: normalized stationary charge and area shrink need no Page transition.
    area, kappa, grav, m, md = sp.symbols('A kappa G M mdot', positive=True)
    charge = kappa*area/(8*sp.pi*grav)
    checked("B4 normalized Wald charge gives area entropy", sp.simplify(2*sp.pi*charge/kappa-area/(4*grav)) == 0)
    adot = sp.diff(16*sp.pi*grav**2*m**2,m)*(-md)
    checked("B4 mass loss already makes area decrease", bool(adot.is_negative))

    v, flux, coeff, aa0 = sp.symbols('v flux C A0', positive=True)
    area_perturbation = coeff*v - 4*sp.pi*grav*flux*v**2
    entropy_perturbation = (area_perturbation-v*sp.diff(area_perturbation,v))/(4*grav)
    checked("B4 linearized entropy change follows flux", sp.simplify(sp.diff(entropy_perturbation,v)-2*sp.pi*v*flux) == 0)
    checked("B4 teleological linear area term cancels", sp.simplify((coeff*v-v*sp.diff(coeff*v,v))/(4*grav)) == 0)

    # B5: metric-compatible flat connection can have torsion (coordinate frame).
    minkowski = np.diag([-1.0,1.0,1.0,1.0])
    gamma = np.zeros((4,4,4))  # Gamma[direction, output, input]
    gamma[1,1,2], gamma[1,2,1] = -1, 1
    checked("B5 metric compatibility does not require torsion-free", all(close(g.T@minkowski+minkowski@g,0) for g in gamma))
    torsion = np.zeros((4,4,4))
    for mu in range(4):
        for nu in range(4):
            torsion[:,mu,nu] = gamma[mu,:,nu]-gamma[nu,:,mu]
    checked("B5 translational residue is nonzero", np.linalg.norm(torsion) > 0)
    checked("B5 same example has zero curvature", all(close(comm(gamma[i],gamma[j]),0) for i in range(4) for j in range(4)))
    print(f"\n{len(CHECKS)} checks passed. Finite/symbolic checks only; scopes are in the source notes.")


if __name__ == '__main__':
    main()
