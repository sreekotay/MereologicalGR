"""Item 2: OCB game causal bound, deterministic enumeration.

Game: Alice gets a in {0,1}, outputs x. Bob gets b,b' in {0,1}, outputs y.
p_succ = 1/2 [ P(x=b | b'=0) + P(y=a | b'=1) ],  all inputs uniform.

Causally ordered strategies with one-way classical communication of an
arbitrary message (alphabet size 4 is fully general for deterministic
strategies here, since the sender's input space has <= 4 values and any
deterministic message is a function of the sender's inputs):

A<B :  x = f(a);            m = g(a);        y = h(b, b', m)
B<A :  y = h(b, b');        m = g(b, b');    x = f(a, m)

Deterministic strategies are the extreme points of the causal polytope
(mixtures of the two orders, incl. shared randomness); p_succ is linear
in the behaviour P(x,y|a,b,b'), so max over the polytope = max over the
deterministic strategies enumerated below.
"""
import itertools
import numpy as np

MSG = range(4)
BIT = (0, 1)


def score(x_of, y_of):
    """x_of(a,b,b'), y_of(a,b,b') deterministic outputs."""
    s1 = sum(x_of(a, b, 0) == b for a in BIT for b in BIT) / 4
    s2 = sum(y_of(a, b, 1) == a for a in BIT for b in BIT) / 4
    return 0.5 * (s1 + s2)


# A < B: f: a->x (4), g: a->m (16), h: (b,b',m)->y; h only matters at b'=1,
# and there it can be chosen greedily per (b,m) — exact inner maximization.
best_AB = 0.0
for f in itertools.product(BIT, repeat=2):
    s1 = sum(f[a] == b for a in BIT for b in BIT) / 4
    for g in itertools.product(MSG, repeat=2):
        # P(y=a|b'=1) = (1/4) sum_{a,b} [h(b,1,g(a)) = a]; choose h greedily per (b,m)
        s2 = 0.0
        for b in BIT:
            for m in MSG:
                cnt = [sum(1 for a in BIT if g[a] == m and a == y) for y in BIT]
                s2 += max(cnt)
        s2 /= 4.0
        best_AB = max(best_AB, 0.5 * (s1 + s2))

best_BA = 0.0
# B < A: h: (b,b')->y (16), g: (b,b')->m (256), f: (a,m)->x greedily per (a,m).
for h in itertools.product(BIT, repeat=4):        # h[(b<<1)|b']
    s2 = sum(h[(b << 1) | 1] == a for a in BIT for b in BIT) / 4
    for g in itertools.product(MSG, repeat=4):    # g[(b<<1)|b']
        # P(x=b|b'=0) = (1/4) sum_{a,b} [f(a, g(b,0)) = b]; greedy per (a,m)
        s1 = 0.0
        for a in BIT:
            for m in MSG:
                cnt = [sum(1 for b in BIT if g[(b << 1) | 0] == m and b == x) for x in BIT]
                s1 += max(cnt)
        s1 /= 4.0
        best_BA = max(best_BA, 0.5 * (s1 + s2))

print("max p_succ, deterministic A<B strategies:", best_AB)
print("max p_succ, deterministic B<A strategies:", best_BA)
print("causal bound = max of both =", max(best_AB, best_BA), " (claim: 3/4)")

# Brute-force cross-check with full 1-bit-message enumeration, no greedy:
bf = 0.0
for f in itertools.product(BIT, repeat=2):            # x=f(a)
    for g in itertools.product(BIT, repeat=2):        # m=g(a)
        for h in itertools.product(BIT, repeat=8):    # y=h(b,b',m)
            x_of = lambda a, b, bp: f[a]
            y_of = lambda a, b, bp: h[(b << 2) | (bp << 1) | g[a]]
            bf = max(bf, score(x_of, y_of))
print("brute force A<B (1-bit msg, all 4096 h):", bf)
