#!/usr/bin/env python3
"""Finite record-use comparisons; run: python checks.py --output results.json.

Python >=3.10; numpy and scipy. All physical assumptions and analytic proofs
are in README.md. Checks corroborate finite identities, not empirical claims.
"""
from __future__ import annotations
import argparse
import json
import platform
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import block_diag
from scipy.optimize import minimize_scalar
from scipy.special import xlogy

BASE = 'c2c7815b50d96b3b24494bb8391666ea4588d453'
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
CHECKS: list[str] = []


def close(a, b, tol=2e-10):
    if not np.allclose(a, b, atol=tol, rtol=tol):
        raise AssertionError(f'Not close: {a!r} != {b!r}')


def passed(name: str):
    CHECKS.append(name)


def h2(p):
    p = np.asarray(p, dtype=float)
    if np.any((p < -1e-14) | (p > 1 + 1e-14)):
        raise ValueError('Probability outside [0,1]')
    p = np.clip(p, 0, 1)
    return -(xlogy(p, p) + xlogy(1-p, 1-p)) / np.log(2)


def gain(r):
    return 1-h2((1-np.asarray(r))/2)


def validate(K):
    K = np.asarray(K, dtype=float)
    if K.ndim != 2 or K.shape[0] != 2 or not np.isfinite(K).all():
        raise ValueError('Expected finite 2-by-n record channel')
    if (K < 0).any():
        raise ValueError('Negative channel probability')
    close(K.sum(axis=1), np.ones(2))
    return K


def posterior(K):
    K = validate(K)
    py = K.sum(axis=0)/2
    keep = py > 0
    py = py[keep]
    p1 = K[1, keep]/(2*py)
    q = 1-2*p1
    return py, p1, q


def metrics(K):
    py, p1, q = posterior(K)
    return dict(recovery=float(np.dot(py, (1+abs(q))/2)),
                work_bits=float(1-np.dot(py, h2(p1))),
                phase_fisher=float(np.dot(py, q*q)))


def flagged_channel(weights, reliability):
    """Output (j,b), j independent of S, b a BSC report of reliability r_j."""
    w, r = np.asarray(weights, float), np.asarray(reliability, float)
    if w.shape != r.shape or (w < 0).any() or (r < 0).any() or (r > 1).any():
        raise ValueError('Invalid flagged-channel parameters')
    close(w.sum(), 1)
    K = np.zeros((2, 2*len(w)))
    for j, (wj, rj) in enumerate(zip(w, r)):
        for s in range(2):
            K[s, 2*j+s] = wj*(1+rj)/2
            K[s, 2*j+1-s] = wj*(1-rj)/2
    return validate(K)


def compress_map(K):
    K = validate(K)
    label = np.argmax(K, axis=0)  # ties deterministically assigned 0
    G = np.eye(2)[label]
    return K @ G, label


def rho_phase(theta, q):
    return (I+q*(np.cos(theta)*X+np.sin(theta)*Y))/2


def drho_phase(theta, q):
    return q*(-np.sin(theta)*X+np.cos(theta)*Y)/2


def qfi(rho, derivative):
    close(rho, rho.conj().T)
    close(np.trace(rho), 1)
    ev, U = np.linalg.eigh(rho)
    if ev.min() < -2e-12:
        raise AssertionError('Nonpositive density matrix')
    D = U.conj().T @ derivative @ U
    den = ev[:, None]+ev[None, :]
    take = den > 1e-13
    return float(np.sum(2*np.abs(D[take])**2/den[take]))


def cq_qfi(K, theta):
    py, _, q = posterior(K)
    rho = block_diag(*[p*rho_phase(theta, z) for p, z in zip(py, q)])
    drho = block_diag(*[p*drho_phase(theta, z) for p, z in zip(py, q)])
    return qfi(rho, drho)


def measurement_fi(K, theta, axis_angle):
    """Actual two-outcome equatorial sensor readout, plus retained record Y."""
    py, _, q = posterior(K)
    axis = np.cos(axis_angle)*X+np.sin(axis_angle)*Y
    answer = 0.0
    for p, z in zip(py, q):
        for s in [-1, 1]:
            effect = (I+s*axis)/2
            prob = float(np.trace(effect @ rho_phase(theta, z)).real)
            derivative = float(np.trace(effect @ drho_phase(theta, z)).real)
            if prob > 1e-13:
                answer += p*derivative**2/prob
    return float(answer)


def explicit_recovery(p1):
    bell = np.array([1, 0, 0, 1], complex)/np.sqrt(2)
    B = np.outer(bell, bell.conj())
    IZ = np.kron(I, Z)
    noisy = (1-p1)*B+p1*(IZ @ B @ IZ)
    return max(float(np.vdot(bell, R @ noisy @ R.conj().T @ bell).real)
               for R in [np.eye(4), IZ])


def optimized_work(p1):
    if p1 <= 1e-12 or p1 >= 1-1e-12:
        return 1.0
    def objective(v):
        return -(p1*np.log(2*v)+(1-p1)*np.log(2*(1-v)))/np.log(2)
    out = minimize_scalar(objective, bounds=(1e-14, 1-1e-14), method='bounded',
                          options={'xatol': 1e-12})
    if not out.success:
        raise RuntimeError('Piston optimization failed')
    return -float(out.fun)


def dephase(rho, eta):
    if not 0 <= eta <= 1:
        raise ValueError('eta must be in [0,1]')
    return (1+eta)/2*rho+(1-eta)/2*(Z @ rho @ Z)


def instrument(rho, sign, eta):
    out = dephase(rho, eta)/2
    return out if sign == 1 else Z @ out @ Z


def instrument_circuit(rho, sign, eta):
    """Independent dilation: copy to marker, dephase marker, measure marker X."""
    CNOT = np.array([[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]], complex)
    marker = np.diag([1, 0]).astype(complex)
    joint = CNOT @ np.kron(rho, marker) @ CNOT.conj().T
    IZ = np.kron(I, Z)
    joint = (1+eta)/2*joint+(1-eta)/2*(IZ @ joint @ IZ)
    ket = np.array([1, sign], complex)/np.sqrt(2)
    A = np.kron(I, ket.conj().reshape(1, 2))
    return A @ joint @ A.conj().T


def run():
    rng = np.random.default_rng(20260909)
    for bad in [np.array([[1.2,-.2],[.5,.5]]), np.ones((3,2)), np.ones((2,2))]:
        try:
            validate(bad)
        except (ValueError, AssertionError):
            continue
        raise AssertionError('Invalid channel accepted')
    passed('Invalid channel inputs are rejected')
    close(h2([0,.5,1]), [0,1,0]); passed('Entropy endpoints')

    for q in np.linspace(-1,1,31):
        for theta in [-1.3, 0, .7]:
            close(qfi(rho_phase(theta,q), drho_phase(theta,q)), q*q)
    passed('Spectral density-matrix QFI equals squared signed confidence')
    for p in np.linspace(0,1,23):
        close(explicit_recovery(p), max(p,1-p))
    passed('Bell-state entanglement fidelity agrees with MAP correction')
    for p in np.linspace(.01,.99,31):
        close(optimized_work(p), 1-h2(p), tol=2e-9)
    passed('Independent piston optimization gives entropy functional')

    max_loss = 0.0
    for _ in range(120):
        n = int(rng.integers(2,8))
        K = np.stack([rng.dirichlet(np.ones(n)) for _ in range(2)])
        m = metrics(K)
        close(cq_qfi(K,.37), m['phase_fisher'])
        close(measurement_fi(K,.37,.37+np.pi/2), m['phase_fisher'])
        for alpha in rng.uniform(-np.pi,np.pi,4):
            if measurement_fi(K,.37,alpha) > m['phase_fisher']+2e-10:
                raise AssertionError('Readout exceeded QFI')
        C, labels = compress_map(K)
        mc = metrics(C)
        close(m['recovery'], mc['recovery'])
        py, _, q = posterior(K)
        within = 0.0
        for label in [0,1]:
            take = labels == label
            if take.any():
                mass = py[take].sum()
                mean = np.dot(py[take],q[take])/mass
                within += np.dot(py[take],(q[take]-mean)**2)
        close(m['phase_fisher']-mc['phase_fisher'], within)
        if mc['work_bits'] > m['work_bits']+2e-12:
            raise AssertionError('Free garbling increased work ceiling')
        mu = 2*m['recovery']-1
        if not mu*mu-1e-12 <= m['phase_fisher'] <= mu+1e-12:
            raise AssertionError('Moment inequality failed')
        max_loss = max(max_loss, within)
    passed('120 random channels: direct joint-state QFI')
    passed('120 random channels: explicit locally calibrated measurement attains QFI')
    passed('Random readout axes do not exceed the QFI')
    passed('120 random channels: MAP compression preserves optimal recovery')
    passed('120 random channels: precision loss is conditional confidence variance')
    passed('120 random channels: compression does not improve gross-work ceiling')
    passed('120 random channels: phase precision moment bounds')

    K = flagged_channel([.2,.8],[0,1])
    C, _ = compress_map(K)
    # Ties in the uninformative flag are kept symmetrically for this example.
    G = np.tile(np.eye(2),(2,1))
    C = K @ G
    comp = {'full':metrics(K), 'only_correction_bit':metrics(C)}
    close(comp['full']['recovery'], .9)
    close(comp['only_correction_bit']['recovery'], .9)
    close(comp['full']['phase_fisher'], .8)
    close(comp['only_correction_bit']['phase_fisher'], .64)
    passed('Exact/erased example: same fidelity, phase FI 0.8 versus 0.64')
    close(comp['full']['work_bits'], .8)
    close(comp['only_correction_bit']['work_bits'], gain(.8))
    passed('Same compression lowers reversible work without lowering recovery')

    target = float((gain(.25)+gain(.75))/2)
    x = float((target-gain(.5))/(1-2*gain(.5)))
    A = flagged_channel([x,1-2*x,x],[0,.5,1])
    B = flagged_channel([.5,.5],[.25,.75])
    pair = {'A':metrics(A), 'B':metrics(B), 'x':x,
            'weights_A':[x,1-2*x,x], 'reliability_A':[0,.5,1],
            'weights_B':[.5,.5], 'reliability_B':[.25,.75]}
    close(pair['A']['recovery'], pair['B']['recovery'])
    close(pair['A']['work_bits'], pair['B']['work_bits'])
    if abs(pair['A']['phase_fisher']-pair['B']['phase_fisher']) < .01:
        raise AssertionError('Third task failed to separate matched records')
    passed('Constructed records match both earlier task values but differ in phase QFI')
    close(pair['A']['phase_fisher'], .25+.5*x)
    close(pair['B']['phase_fisher'], .3125)
    passed('Matched example numerical QFI agrees with exact expressions')

    # Marker-mediated instruments agree on record and ignored-record output,
    # but disagree on their joint conditional quantum output.
    for _ in range(60):
        A0 = rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
        rho = A0 @ A0.conj().T; rho /= np.trace(rho)
        for eta in [0,.2,.7,1]:
            total = np.zeros((2,2), complex)
            corrected = np.zeros((2,2), complex)
            for sign in [-1,1]:
                out = instrument(rho,sign,eta)
                close(out, instrument_circuit(rho,sign,eta))
                close(np.trace(out), .5)
                if np.linalg.eigvalsh(out).min() < -1e-12:
                    raise AssertionError('Nonpositive instrument output')
                total += out
                corrected += out if sign==1 else Z @ out @ Z
            close(total, dephase(rho,0))
            close(corrected, dephase(rho,eta))
    passed('60 random inputs: explicit marker circuit realizes each instrument')
    passed('Identical uniform classical outcome channel for all inputs and eta')
    passed('Identical unconditional dephasing channel for all inputs and eta')
    passed('Outcome-controlled correction recovers eta-dependent coherence')
    instrument_rows = []
    for eta in [0,.25,.5,.75,1]:
        rho, drho = rho_phase(.4,1), drho_phase(.4,1)
        joint = block_diag(*[instrument(rho,s,eta) for s in [1,-1]])
        derivative = block_diag(*[instrument(drho,s,eta) for s in [1,-1]])
        j = qfi(joint,derivative)
        close(j,eta*eta)
        ignored = sum(instrument(rho,s,eta) for s in [1,-1])
        dignored = sum(instrument(drho,s,eta) for s in [1,-1])
        close(qfi(ignored,dignored),0)
        instrument_rows.append({'eta':eta, 'joint_phase_fisher':j,
                                'ignored_record_phase_fisher':0.0,
                                'corrected_entanglement_fidelity':(1+eta)/2})
    passed('Same marginal channels, joint phase QFI spans 0 to 1')
    passed('Ignoring marker label leaves zero phase information')

    # Coherent completion: H on the marker, then controlled-Z, with no readout.
    CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], complex)
    H = (X+Z)/np.sqrt(2)
    CZ = np.diag([1,1,1,-1]).astype(complex)
    U = CZ @ np.kron(I,H) @ CNOT
    zero = np.diag([1,0]).astype(complex)
    plus = (I+X)/2
    for _ in range(30):
        A0 = rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
        rho = A0 @ A0.conj().T; rho /= np.trace(rho)
        close(U @ np.kron(rho,zero) @ U.conj().T, np.kron(rho,plus))
    passed('Coherent marker uncomputation recovers arbitrary input without measurement')

    # Independent chain-rule clock check, with an explicit frequency resource.
    K = B
    for omega in [0,.4,2]:
        py,_,q=posterior(K)
        rho=block_diag(*[p*rho_phase(.3*omega,z) for p,z in zip(py,q)])
        drho=block_diag(*[p*omega*drho_phase(.3*omega,z) for p,z in zip(py,q)])
        close(qfi(rho,drho), omega*omega*metrics(K)['phase_fisher'])
    passed('Proper-time QFI scales with clock frequency squared and vanishes clock-off')

    out = {'base_revision':BASE, 'seed':20260909, 'checks_passed':len(CHECKS),
           'checks':CHECKS, 'compression_example':comp, 'matched_pair':pair,
           'instrument_family':instrument_rows,
           'largest_random_compression_precision_loss':max_loss,
           'environment':{'python':platform.python_version(),
                          'numpy':np.__version__,'scipy':scipy.__version__},
           'scope':'Finite model identities; no empirical fit or priority claim.'}
    return out


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('results.json'))
    args=parser.parse_args()
    result=run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f"{result['checks_passed']} grouped checks passed")
    print(json.dumps({k:result[k] for k in ['compression_example','matched_pair',
                                         'instrument_family']},indent=2))
