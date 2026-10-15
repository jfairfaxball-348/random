#!/usr/bin/env python3
"""P4-S168 local finite sanity ONLY; no randomness or infinite-fibre proof."""
from collections import Counter

def query(t, transcript, queried):
    if "1" not in transcript:
        return 2 * t
    return next(i for i in range(2 * t + 1) if i not in queried)

def scan(source, m):
    out, seen = "", []
    for t in range(m):
        j = query(t, out, seen)
        assert j not in seen and 0 <= j < 2*m
        seen.append(j)
        out += source[j]
    return out

def query_trace(y):
    out, seen = "", []
    for t, bit in enumerate(y):
        j = query(t, out, seen)
        assert j not in seen
        seen.append(j)
        out += bit
    return seen

total = 0
for m in range(1, 8):
    n = 2*m
    counts = Counter(scan(format(i, f"0{n}b"), m) for i in range(2**n))
    assert len(counts) == 2**m
    assert set(counts.values()) == {2**m}
    total += 2**n
    print(f"m={m}: {2**n} input words, {2**m} outputs, {2**m} input words per output")
assert total == 21844
assert query_trace("000000") == [0, 2, 4, 6, 8, 10]
assert query_trace("001000") == [0, 2, 4, 1, 3, 5]
assert query_trace("100000") == [0, 1, 2, 3, 4, 5]
assert query_trace("000100") == [0, 2, 4, 6, 1, 3]
for n in range(8):
    y = "0"*n + "1" + "0"*20
    q = query_trace(y)
    fixed = {2*i for i in range(n+1)}
    assert q[:n+1] == [2*i for i in range(n+1)]
    assert q[n+1:] == [j for j in range(80) if j not in fixed][:20]
print("PASS: 21,844 finite prefix evaluations; infinite proofs separate.")
