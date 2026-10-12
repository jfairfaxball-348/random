#!/usr/bin/env python3
"""P4-S106 finite sanity audit. Not an infinitary Cantor proof."""
from itertools import product

def bits(n):
    return map("".join, product("01", repeat=n))

def Hprefix(x, m):
    j = x.find("1")
    if j < 0 or j >= m:
        return "0" * m
    return x[:j+1] + x[j+2:j+2+(m-j-1)]

def pi(x):
    return x[1:]

checks = 0
for m in range(1, 10):
    for y in bits(m):
        pre = [x for x in bits(m+1) if Hprefix(x, m) == y]
        assert len(pre) == 2
        checks += 1
        for r in range(1, m+1):
            d = len({x[:r] for x in pre}) == 2
            k = y.find("1")
            should = k >= 0 and k+1 < r
            assert d == should
            checks += 1
            if d:
                vals = sorted(pre, key=lambda x: x[:r])
                assert vals[0][:r] < vals[1][:r]
                checks += 1
        count = sum(1 for x in bits(m+2) if Hprefix(pi(x), m) == y)
        assert count == 4
        checks += 1
print("PASS", checks, "finite identities, m=1,...,9")
