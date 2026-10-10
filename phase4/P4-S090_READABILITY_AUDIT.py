#!/usr/bin/env python3
"""Exact finite checks for S090's written infinite separation proof.

Checks algebra, conditional probabilities, control-dependent selection and
budget constants. Does not compute the noncomputable true validity branch,
certify a concrete infinite random sequence, or prove Conjecture R.
"""
from fractions import Fraction as Q
from itertools import product

CHECKS = 0


def check(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def xor_at(bits, support):
    return sum(bits[j] for j in support) % 2


def encode(a, b):
    return [b[j] ^ (b[j-2] if j >= 2 else 0)
            ^ ((1 ^ a[j]) * (b[j-1] if j else 0)) for j in range(len(a))]


def decode(a, v):
    b = []
    for j, bit in enumerate(v):
        b.append(bit ^ (b[j-2] if j >= 2 else 0)
                 ^ ((1 ^ a[j]) * (b[j-1] if j else 0)))
    return b


def delta(a, q):
    d = [0] * len(a)
    d[q] = 1
    for j in range(q+1, len(a)):
        d[j] = (d[j-2] if j >= 2 else 0) ^ ((1 ^ a[j]) * d[j-1])
    return d


def algebra():
    n = 6
    for x in product(range(2), repeat=2*n):
        a, b = list(x[::2]), list(x[1::2])
        v = encode(a, b)
        check(decode(a, v) == b, "causal inverse")
        for q in range(n):
            other_v = v.copy()
            other_v[q] ^= 1
            other_b = decode(a, other_v)
            d = delta(a, q)
            check([u ^ w for u, w in zip(b, other_b)] == d,
                  "exact held-bit difference recurrence")
            check(all(d[j-1] or d[j] for j in range(q+1, n)),
                  "nonzero state never reaches 00")
            v0 = v.copy()
            v0[q] = 0
            b0 = decode(a, v0)
            # Control-selected, separated singleton constraints.
            selected = [j for j in range(q+1, n) if d[j]][:2]
            for values in product(range(2), repeat=len(selected)):
                implied = [value ^ b0[j] for j, value in zip(selected, values)]
                if implied and len(set(implied)) == 1:
                    wrong = implied[0] != v[q]
                    check(wrong == all(b[j] != value
                                       for j, value in zip(selected, values)),
                          "wrong prediction iff every selected equation fails")


def conditional_quarter():
    # Every possible incoming nonzero state, and every nonempty parity whose
    # first index is at least two steps beyond the conditioned control prefix.
    for u, v in [(0, 1), (1, 0), (1, 1)]:
        for n in range(2, 9):
            paths = []
            for a in product(range(2), repeat=n):
                d = [u, v]
                for bit in a:
                    d.append(d[-2] ^ ((1 ^ bit) * d[-1]))
                paths.append(d[1:])
            for mask in range(1, 1 << (n-1)):
                support = [j+2 for j in range(n-1) if mask >> j & 1]
                probability = Q(sum(xor_at(d, support) for d in paths), len(paths))
                check(probability >= Q(1, 4), "uniform conditional quarter bound")


def repeated_bound():
    families = [[(2,), (4,), (6,)], [(2, 3), (5, 6), (8, 9)],
                [(2, 4), (6,), (8, 9)], [(2, 3, 4), (6, 7), (9,)]]
    for u, v in [(0, 1), (1, 0), (1, 1)]:
        for family in families:
            n = max(family[-1])
            totals = []
            for a in product(range(2), repeat=n):
                d = [u, v]
                for bit in a:
                    d.append(d[-2] ^ ((1 ^ bit) * d[-1]))
                totals.append(sum(xor_at(d[1:], support) for support in family))
            expectation = sum((Q(1, 2**s) for s in totals), Q(0)) / len(totals)
            check(expectation <= Q(7, 8)**len(family), "iterated Laplace estimate")
            for r in range(1, len(family)+1):
                probability = Q(sum(s < r for s in totals), len(totals))
                check(probability <= 2**r * Q(7, 8)**len(family),
                      "lower-tail bound without independence")


def conditional_fooling():
    n = 7
    # One list shares a true equation; the other has wholly disjoint supports.
    # Which equations the observer uses is chosen by the actual controls.
    families = [[(1,), (3,), (5,)], [(2,), (4,), (5,)]]
    for a in product(range(2), repeat=n):
        d = delta(a, 0)
        for true_values in product(range(2), repeat=2):
            data = [b for b in product(range(2), repeat=n)
                    if b[1] == true_values[0] and b[6] == true_values[1]]
            for family in families:
                values = [true_values[0] if support == (1,) else 0
                          for support in family]
                separating = [(s, value) for s, value in zip(family, values)
                              if xor_at(d, s)]
                for r in [1, 2]:
                    if len(separating) < r:
                        continue
                    selected = separating[:r]
                    probability = Q(sum(all(xor_at(b, s) != value
                                            for s, value in selected) for b in data),
                                    len(data))
                    shares_true = any(s == (1,) for s, _ in selected)
                    check(probability == (0 if shares_true else Q(1, 2**r)),
                          "relative fooling: shared contradiction or independent parities")


def budgets():
    for q in range(101):
        m = 1
        while True:
            L = m*(m+1)-q-1
            r = q+2*m+4
            if L >= 0 and 2**r * Q(7, 8)**L <= Q(1, 2**(q+6)):
                break
            m += 1
        check(L >= r, "enough constraints for the selected stall cover")
        check(2**r * Q(7, 8)**L <= Q(1, 2**(q+6)), "exact stall budget")
    check(Q(1, 64)*2 == Q(1, 32), "sum of stall budgets")
    check(Q(1, 16)*2*1 == Q(1, 8), "sum of fooling budgets")
    check(4*(1-Q(1, 32)-Q(1, 8)) == Q(27, 8) > 2,
          "strict compactness margin")


if __name__ == '__main__':
    for part in [algebra, conditional_quarter, repeated_bound, conditional_fooling, budgets]:
        before = CHECKS
        part()
        print(f'{part.__name__}: {CHECKS-before} exact checks PASS')
    print(f'ALL P4-S090 READABILITY CHECKS PASS ({CHECKS} checks; finite support only)')
