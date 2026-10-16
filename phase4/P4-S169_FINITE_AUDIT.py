#!/usr/bin/env python3
"""P4-S169 local finite sanity only: T versus finite homeomorphism cutoffs."""
from collections import Counter

def scan(bits, m, cutoff=None):
    output, used = [], set()
    for t in range(m):
        if (cutoff is None or t < cutoff) and not any(output):
            q = 2 * t
        else:
            q = 0
            while q in used:
                q += 1
        assert q not in used
        used.add(q)
        output.append(bits[q])
    return tuple(output)

checks = 0
for m in range(1, 8):
    totals = Counter()
    approximations = {n: Counter() for n in range(m + 1)}
    for a in range(1 << (2 * m)):
        bits = tuple((a >> j) & 1 for j in range(2 * m))
        target = scan(bits, m)
        totals[target] += 1
        for n in approximations:
            trial = scan(bits, m, n)
            approximations[n][trial] += 1
            if n == m:
                assert trial == target
            checks += 1
    assert len(totals) == 1 << m and set(totals.values()) == {1 << m}
    for n, counts in approximations.items():
        assert len(counts) == 1 << m and set(counts.values()) == {1 << m}
print("PASS:", checks, "finite-prefix evaluations")
