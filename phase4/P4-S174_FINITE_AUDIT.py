#!/usr/bin/env python3
"""P4-S174 finite SANITY ONLY: chronological Petrović encoding and H completion."""
from fractions import Fraction
from collections import Counter

def p(prefix):
    return (1 << len(prefix)) + sum(int(bit) << i for i, bit in enumerate(prefix))

def encode_p(bits):
    s = ""
    n = 0
    while (1 << (n+1)) - 1 <= len(bits):
        s += bits[p(s)-1]
        n += 1
    return s

def complete_h(bits):
    s = ""
    out = ""
    n = 0
    while (1 << (n+1)) - 1 <= len(bits):
        start = (1 << n)-1
        block = bits[start:start+(1 << n)]
        chosen = p(s)-1-start
        s += block[chosen]
        out += block[chosen] + block[:chosen] + block[chosen+1:]
        n += 1
    return out

def inverse_h(out):
    s = ""
    inp = ""
    n = 0
    while (1 << (n+1)) - 1 <= len(out):
        start = (1 << n)-1
        block = out[start:start+(1 << n)]
        chosen = p(s)-1-start
        inp += block[1:chosen+1] + block[0] + block[chosen+1:]
        s += block[0]
        n += 1
    return inp

def E(s):
    capital = Fraction(1)
    observed = ""
    for i, b in enumerate(s, start=1):
        if i == p(observed):
            capital *= Fraction(3, 2) if b == "0" else Fraction(1, 2)
            observed += b
    return capital

checks = 0
rows = []
for n in range(1, 5):
    L = (1 << n)-1
    h_outputs = set()
    p_counts = Counter()
    for i in range(1 << L):
        x = f"{i:0{L}b}"
        h = complete_h(x)
        assert inverse_h(h) == x
        assert len(h) == L
        assert encode_p(x) == "".join(h[(1 << j)-1] for j in range(n))
        h_outputs.add(h)
        p_counts[encode_p(x)] += 1
        checks += 3
    assert len(h_outputs) == (1 << L)
    assert len(p_counts) == (1 << n)
    assert set(p_counts.values()) == {1 << (L-n)}
    checks += len(p_counts)+1
    rows.append((n, L, len(h_outputs), 1 << (L-n)))
for length in range(8):
    for i in range(1 << length):
        x = f"{i:0{length}b}" if length else ""
        assert E(x+"0") + E(x+"1") == 2*E(x)
        assert E(x) >= 0
        checks += 2
print("P4-S174 PASS", checks, "finite sanity assertions", rows)
assert checks == 99262
