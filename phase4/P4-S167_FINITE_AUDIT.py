#!/usr/bin/env python3
"""S167 local *finite* sanity audit only, not a proof of infinite fibres or CR.
Variable finite-block erasure map P: 1^n 0 b t -> 1^n 0 t (|b|=n);
P(1^omega)=1^omega. Input 2m-prefix suffices for output m-prefix.
"""
from collections import Counter

def image_prefix(bits, m):
    assert len(bits) >= 2 * m
    n = 0
    while n < m and bits[n] == '1':
        n += 1
    if n == m:
        return '1' * m
    return '1' * n + '0' + bits[2*n+1:2*n+1+(m-n-1)]

total = 0
for m in range(1, 8):
    counts = Counter(image_prefix(format(i, f'0{2*m}b'), m)
                     for i in range(4 ** m))
    assert len(counts) == 2 ** m
    assert set(counts.values()) == {2 ** m}, (m, counts)
    total += 4 ** m
    print(f'm={m}: inputs={4**m}; outputs={2**m}; per-output inputs={2**m}')
print(f'PASS {total} finite prefixes; infinite degree and randomness require proofs')
