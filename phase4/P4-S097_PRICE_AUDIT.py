#!/usr/bin/env python3
"""P4-S097: exact FINITE sanity checks, not an infinitary theorem or hosted CI."""
from fractions import Fraction

checks = 0
for n in range(1, 25):
    N = 2 ** (n + 2)
    q = Fraction(1, 2 ** (2 * n + 4))
    assert 2 * N * q == Fraction(1, 2 ** (n + 1))
    assert 2 * N * q <= Fraction(1, 2 ** n)
    checks += 1

for m in range(1, 17):
    count = sum(any((x >> j) & 1 for j in range(m)) for x in range(1 << m))
    assert Fraction(count, 1 << m) == 1 - Fraction(1, 1 << m)
    checks += 1

for n in range(1, 12):
    capital = Fraction(1)
    for k in range(2 * n):
        if k % 2:
            capital *= Fraction(3, 2)
    assert capital == Fraction(3, 2) ** n
    checks += 1

assert checks == 51
print("PASS: 24 budgets; 16 finite hold-unions; 11 predictable growth factors")
