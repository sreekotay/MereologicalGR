"""Build a 2D causal set (Poisson sprinkling of the diamond |u|,|v| < 1) plus a uniformly
accelerated writer's ticks, and its Sorkin-Johnston two-point function, from the order alone.
Usage: python3 build.py N a seed out.npz"""
import sys, time, numpy as np
N, a, seed, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
rng = np.random.default_rng(seed)
u = rng.uniform(-1, 1, N); v = rng.uniform(-1, 1, N)
th = np.linspace(-1.75, 1.75, 36)                      # a*tau along the writer
tw = np.sinh(th)/a; xw = (np.cosh(th) - 1)/a
U = np.concatenate([u, tw - xw]); V = np.concatenate([v, tw + xw])
t0 = time.time()
C = ((U[None, :] < U[:, None]) & (V[None, :] < V[:, None]))      # C[x,y]: y precedes x
iD = 0.5j*(C.astype(float) - C.T.astype(float))                   # i * Pauli-Jordan; G_R = C/2 (2D massless)
lam, vec = np.linalg.eigh(iD)
pos = lam > 1e-10
W = (vec[:, pos]*lam[pos]) @ vec[:, pos].conj().T                 # SJ: positive spectral part
print(f"N={N} a={a} seed={seed}: eigh {time.time()-t0:.0f}s, max |u|,|v| of writer = {max(abs(tw-xw).max(), abs(tw+xw).max()):.2f}")
np.savez(out, W=W.astype(np.complex64), U=U, V=V, C=C, th=th, a=a, N=N)
