"""Common utilities: tensor helpers, Choi maps, process-matrix probability rule.

Conventions (fixed by the physical wire test in test_convention()):
  * |I>> = sum_i |ii>   (unnormalized maximally entangled vector)
  * Choi of a CP map M: A_I -> A_O  (Kraus {K}):
        C(M) = sum_ij |i><j|_{A_I} (x) M(|i><j|)_{A_O}
             = (id (x) M)(|I>><<I|),   ordering  A_I (x) A_O.
  * Party operator entering the probability rule: which of C or C^T is
    correct is determined empirically in test_convention() against the
    physical prediction of a causally-ordered wire circuit.
  * Probability rule: P = Tr[ W (M_A (x) M_B (x) 1_F) ].
"""
import numpy as np

I2 = np.eye(2)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)


def kron(*ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


def op_on(op_dict, dims):
    """Embed operators on selected tensor factors; identity elsewhere.
    op_dict: {position: matrix}; dims: list of factor dims."""
    ops = [op_dict.get(k, np.eye(d)) for k, d in enumerate(dims)]
    return kron(*ops)


def choi_from_kraus(kraus_list, din=2, dout=2):
    """C = sum_ij |i><j| (x) K|i><j|K^dag  on  H_in (x) H_out."""
    C = np.zeros((din * dout, din * dout), dtype=complex)
    for K in kraus_list:
        v = np.zeros(din * dout, dtype=complex)
        for i in range(din):
            # |i>_{in} (x) K|i>_{out}
            v[i * dout:(i + 1) * dout] += K[:, i]
        C += np.outer(v, v.conj())
    return C


def random_cptp_kraus(din=2, dout=2, nk=4, rng=None):
    rng = rng or np.random.default_rng()
    X = rng.normal(size=(nk * dout, din)) + 1j * rng.normal(size=(nk * dout, din))
    # polar: V = X (X^dag X)^{-1/2} is an isometry
    u, s, vh = np.linalg.svd(X, full_matrices=False)
    V = u @ vh
    return [V[k * dout:(k + 1) * dout, :] for k in range(nk)]


def random_instrument_chois(n_out=2, din=2, dout=2, nk=2, rng=None):
    """Random n_out-outcome instrument; returns list of Choi ops (sum is CPTP)."""
    rng = rng or np.random.default_rng()
    X = rng.normal(size=(n_out * nk * dout, din)) + 1j * rng.normal(size=(n_out * nk * dout, din))
    u, s, vh = np.linalg.svd(X, full_matrices=False)
    V = u @ vh
    chois = []
    for o in range(n_out):
        ks = [V[(o * nk + k) * dout:(o * nk + k + 1) * dout, :] for k in range(nk)]
        chois.append(choi_from_kraus(ks, din, dout))
    return chois


def maxent_vec(d=2):
    v = np.zeros(d * d, dtype=complex)
    for i in range(d):
        v[i * d + i] = 1.0
    return v


def test_convention(verbose=True):
    """Wire circuit W = rho^{A_I} (x) |I>><<I|^{A_O B_I} (x) 1^{B_O}/1.
    Alice applies unitary U; Bob measures POVM {E, 1-E} and discards.
    Physical prediction: P(E) = Tr[E U rho U^dag].
    Determine whether party operators must be C or C^T."""
    rng = np.random.default_rng(7)
    # random complex rho, U, E
    A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    rho = A @ A.conj().T
    rho /= np.trace(rho)
    H = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    H = H + H.conj().T
    from scipy.linalg import expm
    U = expm(1j * H)
    B = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    E = B @ B.conj().T
    E = E / (np.linalg.norm(E, 2) * 1.5)  # 0 <= E <= 1

    phi = maxent_vec(2)
    PhiPhi = np.outer(phi, phi.conj())
    dims = [2, 2, 2, 2]  # A_I A_O B_I B_O
    # W = rho_{A_I} (x) |I>><<I|_{A_O B_I} (x) 1_{B_O}
    W = np.kron(np.kron(rho, PhiPhi), I2)

    C_A = choi_from_kraus([U])
    # Bob: measure E then prepare fixed state s (traced by nobody -> just prepare 1/2)
    # CP map for outcome E:  rho -> Tr[E rho] * (1/2)
    # Kraus: {|0><psi_k| ...}; easier to build Choi directly:
    # C = sum_ij |i><j| Tr... : M(|i><j|) = <j|E^T? careful: Tr[E |i><j|] = <j|E|i>
    C_B = np.zeros((4, 4), dtype=complex)
    for i in range(2):
        for j in range(2):
            M = (E[j, i]) * (I2 / 2)   # Tr[E |i><j|] = <j|E|i> = E[j,i]
            C_B += np.kron(np.outer(np.eye(2)[i], np.eye(2)[j]), M)

    target = np.trace(E @ U @ rho @ U.conj().T).real
    results = {}
    for name, (MA, MB) in {
        'C,C': (C_A, C_B),
        'CT,CT': (C_A.T, C_B.T),
        'C,CT': (C_A, C_B.T),
        'CT,C': (C_A.T, C_B),
    }.items():
        P = np.trace(W @ np.kron(MA, MB)).real
        results[name] = P
    if verbose:
        print(f"physical target P = {target:.6f}")
        for k, v in results.items():
            print(f"  convention {k:6s}: P = {v:.6f}  {'<== MATCH' if abs(v-target)<1e-9 else ''}")
    best = min(results, key=lambda k: abs(results[k] - target))
    return best, target, results


if __name__ == '__main__':
    test_convention()
