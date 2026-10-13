#!/usr/bin/env python3
"""P4-S125 exact finite sanity, not an infinity proof. Python stdlib only."""
from collections import Counter
from itertools import product

def pi(a, i):
    if a == 0:
        return i + 1 if i % 2 == 0 else i - 1
    if i == 0:
        return 0
    return i + 1 if i % 2 else i - 1

def output(src, m):
    a, b, c = src[:3]
    if b == 0:
        head = (0, 0) if a == 0 else (1, 1)
    else:
        head = (0, 1) if c == 0 else (1, 0)
    tail = src[3:]
    return head + tuple(tail[pi(a, i)] for i in range(m - 2))

checks = 0
for m in range(2, 10):
    cnt = Counter(output(x, m) for x in product((0, 1), repeat=m+2))
    assert len(cnt) == 2**m
    for y in product((0, 1), repeat=m):
        assert cnt[y] == 4, (m, y, cnt[y])
        checks += 1
    print(f"m={m}: {2**m} output cells, exactly four source cells each")
print(f"PASS: {checks} finite cylinder checks; INFINITY CLAIMS REQUIRE PROOF")
