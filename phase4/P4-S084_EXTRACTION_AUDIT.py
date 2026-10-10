#!/usr/bin/env python3
"""P4-S084: finite predictable extraction and exact geometric-tail audit.
Finite checks only; infinitary proofs are in P4-S084_MATHEMATICS.md.
"""
from fractions import Fraction
from itertools import product

def steps(bits):
    q, M, read, out = 0, 1, set(), []
    for t in range(len(bits)):
        if M-q >= 3 and (t % 3 != 1):
            coord, pred, resolve = q, sum(b for _, b, _ in out[-3:]) % 2, True
            q, M = M, M+1
        else:
            coord, pred, resolve = M, 0, False
            M += 1
        if coord >= len(bits):
            break
        assert coord not in read
        read.add(coord)
        out.append((coord, bits[coord], (pred if resolve else None)))
    return out

def capital(output):
    d = Fraction(1)
    errors = []
    for _, actual, predicted in output:
        if predicted is not None:
            err = actual ^ predicted
            errors.append(err)
            d *= Fraction(3, 2) if err else Fraction(1, 2)
    return d, tuple(errors)

checks = 0
for n in range(1, 12):
    for bits in product((0, 1), repeat=n):
        out = steps(bits)
        assert len(set(x[0] for x in out)) == len(out)
        assert len(set(range(max((x[0] for x in out), default=-1)+1)) - set(x[0] for x in out)) <= 1
        actual, errors = capital(out)
        expected = Fraction(3,2)**sum(errors) * Fraction(1,2)**(len(errors)-sum(errors))
        assert actual == expected
        checks += 1

for depth in range(12):
    for prefix in product((0, 1), repeat=depth):
        def selected_cap(eta):
            c=Fraction(1)
            for t,bit in enumerate(eta):
                if t%4 in (1,3):
                    prediction = sum(eta[:t])%2
                    c *= Fraction(3,2) if (bit^prediction) else Fraction(1,2)
            return c
        assert selected_cap(prefix+(0,))+selected_cap(prefix+(1,)) == 2*selected_cap(prefix)
        checks += 1

for Q in range(12):
    bound = Fraction(1, 2**(Q+3))
    truncated = sum((Fraction(2**m, 2**(q+2*m+4)) for q in range(Q,Q+24) for m in range(1,24)), Fraction(0))
    assert truncated < bound
    assert bound + Fraction(1,2**(Q+1)) <= Fraction(1,2**Q)
    checks += 1
print('P4-S084 FINITE AUDIT PASS', checks)
