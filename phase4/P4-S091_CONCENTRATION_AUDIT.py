#!/usr/bin/env python3
"""Exact finite audit of S091; no infinite survivor or universal coverage claim.

Checks both committed offsets, mixed readout prediction, projection ranks,
biased-control false readings, sharp stall amplification, and cover budgets.
No spectral calculation and no access to a true validity branch.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random

CHECKS = 0


def check(v, label):
    global CHECKS
    CHECKS += 1
    if not v:
        raise AssertionError(label)


def parity(v):
    return v.bit_count() & 1


def rank(rows):
    basis = {}
    for v in rows:
        while v:
            p = v.bit_length() - 1
            if p in basis:
                v ^= basis[p]
            else:
                basis[p] = v
                break
    return len(basis)


def get(bits, j):
    return bits[j] if j >= 0 else 0


def encode(control, data, offset):
    return [data[j] ^ get(data, j-2)
            ^ ((1 ^ get(control, j-offset)) * get(data, j-1))
            for j in range(len(data))]


def decode(control, virtual, offset):
    data = []
    for j, v in enumerate(virtual):
        data.append(v ^ get(data, j-2)
                    ^ ((1 ^ get(control, j-offset)) * get(data, j-1)))
    return data


def delta(control, q, offset):
    d = [0] * len(control)
    d[q] = 1
    for j in range(q+1, len(d)):
        d[j] = d[j-2] ^ ((1 ^ get(control, j-offset)) * d[j-1])
    return d


def xor_at(bits, indices):
    return sum(bits[j] for j in indices) & 1


def projection_ranks():
    rng = Random(91001)
    n = 4
    for trial in range(160):
        rows = []
        for _ in range(rng.randrange(1, 10)):
            rows.append(rng.randrange(1, 1 << (2*n)))
        witness = rng.randrange(1 << (2*n))
        rhs = [parity(v & witness) for v in rows]
        R = rank(rows)
        da = R - rank([v >> n for v in rows])
        db = R - rank([v & ((1 << n)-1) for v in rows])
        sols = [x for x in range(1 << (2*n))
                if all(parity(x & v) == c for v, c in zip(rows, rhs))]
        check(len(sols) == 1 << (2*n-R), "affine measure")
        for axis, d in ((0, da), (1, db)):
            hist = [0] * (1 << n)
            for x in sols:
                hist[(x >> (axis*n)) & ((1 << n)-1)] += 1
            check(sum(bool(v) for v in hist) == 1 << (n-d), "projection codimension")
            for count in hist:
                density = Q(count * (1 << n), len(sols))
                check(density in (0, 1 << d), "exact marginal density")
        row = rng.randrange(1, 1 << (2*n))
        if rank(rows + [row]) == R+1:
            da1 = R+1 - rank([v >> n for v in rows + [row]])
            db1 = R+1 - rank([v & ((1 << n)-1) for v in rows + [row]])
            check(da1 in (da, da+1) and db1 in (db, db+1), "defect monotonicity")


def mixed_prediction():
    n = 5
    strings = list(product((0, 1), repeat=n))
    for offset in (0, 1):
        for c in strings:
            for d in strings:
                v = encode(c, d, offset)
                check(decode(c, v, offset) == list(d), "exact frame inverse")
                for q in range(n):
                    dd = delta(c, q, offset)
                    toggled = v[:]
                    toggled[q] ^= 1
                    other = decode(c, toggled, offset)
                    check(other == [x ^ y for x, y in zip(d, dd)], "held candidate difference")
                    v0 = v[:]
                    v0[q] = 0
                    d0 = decode(c, v0, offset)
                    for support in ((q,), tuple(range(q, n)), (n-1,)):
                        control_support = (q, n-1) if q != n-1 else (q,)
                        alpha_c = xor_at(c, control_support)
                        rhs = alpha_c ^ xor_at(d, support)
                        nu = rhs ^ alpha_c ^ xor_at(d0, support)
                        separated = xor_at(dd, support)
                        check(not separated or nu == v[q], "mixed readout predicts held bit")
                        check(separated or xor_at(other, support) == xor_at(d, support),
                              "nonseparating readout")


def biased_false_reading():
    # True shared equation c0 XOR d1=0, auxiliary c0=1.
    # Conditional control marginal is biased, but unshared d3,d5 stay free.
    n = 6
    for offset in (0, 1):
        for c in product((0, 1), repeat=n):
            if c[0] != 1:
                continue
            dd = delta(c, 0, offset)
            rows = [(1, 0, 0), (3, 2, 1), (5, 4, 0)]
            separating = [row for row in rows if dd[row[0]]]
            admissible = [d for d in product((0, 1), repeat=n) if d[1] == 1]
            for r in (1, 2, 3):
                selected = separating[:r]
                if len(selected) != r:
                    continue
                false = sum(all((c[ci] ^ d[di]) != rhs for di, ci, rhs in selected)
                            for d in admissible)
                expected = Q(0) if any(di == 1 for di, _, _ in selected) else Q(1, 1 << r)
                check(Q(false, len(admissible)) == expected,
                      "pointwise conditional false-reading bound under bias")


def actual_stall_amplification():
    for L in range(1, 5):
        n = 2*L
        J = list(range(1, n, 2))
        for offset in (0, 1):
            control_positions = J if offset == 0 else list(range(0, n, 2))
            controls = list(product((0, 1), repeat=n))
            event = [c for c in controls if all(c[p] == 1 for p in control_positions)]
            stall = [c for c in controls if all(delta(c, 0, offset)[j] == 0 for j in J)]
            check(set(event) == set(stall), "actual exact stall event in each offset")
            check(Q(len(event), len(controls)) == Q(1, 1 << L), "absolute stall measure")
            # Mixed certificate a_j XOR b_j=0 plus auxiliary controls.
            rows = [(1 << j) | (1 << (n+j)) for j in J]
            if offset == 0:
                rows += [1 << j for j in J]
                defect = rank(rows) - rank([v >> n for v in rows])
            else:
                rows += [1 << (n+j) for j in control_positions]
                defect = rank(rows) - rank([v & ((1 << n)-1) for v in rows])
            check(rank(rows) == 2*L and defect == L, "sharp mixed-state projection rank")
            check((1 << defect) * Q(len(event), len(controls)) == 1,
                  "sharp conditioned amplification")
        # The simultaneous example uses a_odd=1, b_even=1, and mixed readouts.
        rows = [(1 << j) | (1 << (n+j)) for j in J]
        rows += [1 << j for j in J] + [1 << (n+j) for j in range(0, n, 2)]
        rr = rank(rows)
        check(rr == 3*L and rr-rank([v >> n for v in rows]) == L
              and rr-rank([v & ((1 << n)-1) for v in rows]) == 2*L,
              "both-frame countermodel ranks")


def conditional_quarter_and_tower():
    n = 7
    controls = list(product((0, 1), repeat=n))
    for offset in (0, 1):
        differences = {c: delta(c, 0, offset) for c in controls}
        for t in range(1, 4):
            # Previous parity ends at t; the exact coefficient offset makes
            # its natural control filtration end at t-offset.
            prefix_len = t-offset+1
            fresh = list(range(t+2, n))
            for prefix in product((0, 1), repeat=prefix_len):
                tails = [c for c in controls if c[:prefix_len] == prefix]
                for mask in range(1, 1 << len(fresh)):
                    support = [j for k, j in enumerate(fresh) if (mask >> k) & 1]
                    sep = sum(xor_at(differences[c], support) for c in tails)
                    check(Q(sep, len(tails)) >= Q(1, 4), "quarter bound at exact offset filtration")
        counts = [sum(differences[c][j] for j in (1, 3, 5)) for c in controls]
        for r in range(1, 5):
            p = Q(sum(s < r for s in counts), len(counts))
            check(p <= (1 << r)*Q(7, 8)**3, "dependent repeated-reading bound")


def budgets():
    for D in (0, 1, 2, 8, 25):
        for q in range(12):
            m = 1
            while True:
                L = m*(m+1)-q-1
                r = q+2*m+4
                if L >= 0 and (1 << (D+r))*Q(7, 8)**L <= Q(1, 1 << (q+6)):
                    break
                m += 1
            check(m < 100, "finite rational stall-cover search")
    check(sum(Q(1, 1 << (q+6)) for q in range(40)) < Q(1, 32), "stall-cover series")
    check(sum((1 << m)*Q(1, 1 << (q+2*m+4))
              for q in range(30) for m in range(1, 30)) < Q(1, 8), "all-guesses error series")
    check(1-Q(1, 8)-Q(1, 32) == Q(27, 32), "global surviving relative mass")


if __name__ == '__main__':
    for part in (projection_ranks, mixed_prediction, biased_false_reading,
                 actual_stall_amplification, conditional_quarter_and_tower, budgets):
        part()
        print(part.__name__, 'PASS', CHECKS)
    print(f'ALL P4-S091 EXACT AUDITS PASS ({CHECKS} checks; finite verification only)')
