#!/usr/bin/env python3
"""Exact Fraction finite sanity for P4-S157. NEVER an infinite proof."""
from fractions import Fraction
from itertools import product
blocks = (2, 3, 4)
N = sum(blocks)
def rotate(x):
    y = []
    a = 0
    for b in blocks:
        y += list(x[a+1:a+b]) + [x[a]]
        a += b
    return tuple(y)
def cutoff(n):
    if n == 0: return 0
    a = 0
    for b in blocks:
        a += b
        if a >= n: return a
    raise AssertionError("bad n")
def capital(z):
    d = Fraction(1)
    for b in z:
        d *= Fraction(3,2) if b == 0 else Fraction(1,2)
    return d
words = list(product((0,1), repeat=N))
G = {x:rotate(x) for x in words}
assert len(set(G.values())) == 2**N
e = {}
checks = 0
for n in range(N+1):
    m = cutoff(n)
    for s in product((0,1), repeat=n):
        images = {G[x][:m] for x in words if x[:n] == s}
        e[s] = 2**n * sum((capital(t)*Fraction(1,2**m) for t in images), Fraction(0))
        for x in words:
            if x[:n] == s:
                assert e[s] >= Fraction(1,2**(1+m-n))*capital(G[x][:m])
                checks += 1
nodes=0
for s in e:
    if len(s)<N:
        assert e[s+(0,)]+e[s+(1,)]==2*e[s]
        nodes+=1
assert e[()]==1 and checks==5120 and nodes==511
print("PASS: 5120 Fraction inequalities, 511 martingale equations, all-output bijection")
