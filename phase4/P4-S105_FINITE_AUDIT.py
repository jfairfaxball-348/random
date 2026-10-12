"""Limited exact sanity checks for S105; not an infinitary theorem proof."""
from fractions import Fraction as F
from itertools import product
import json

checks = 0

# Necessary cell price and the proposed exact finite endpoint completion.
for s in range(1, 7):
    for k in range(2**s):
        p = F(k, 2**s)
        for h in (F(2), F(3), F(5, 2)):
            if h*p > 1:
                continue
            rem = (1-h*p)/(1-p)
            assert rem >= 0
            leaves = [h]*k + [rem]*(2**s-k)
            assert sum(leaves, F(0))/len(leaves) == 1
            row = leaves
            while len(row) > 1:
                row = [(row[j]+row[j+1])/2 for j in range(0, len(row), 2)]
                assert all(v >= 0 for v in row)
            assert row == [F(1)]
            checks += 1

# Wrong cells cannot be repaired just by making their global mass tiny.
for r in range(1, 21):
    cell = F(1, 2**r)
    assert cell > cell/2
    checks += 1

# Enumerate the full finite fair tree for stopped all-in zero accounts.
def bank(bits):
    active, deposited = F(1), F(0)
    alive = True
    for bit in bits:
        if alive:
            active *= 2 if bit == 0 else 0
            alive = bit == 0
        while active >= 2:
            active -= 1
            deposited += 1
        assert 0 <= active < 2
    return active, deposited

for length in range(1, 10):
    vals = [bank(bits) for bits in product((0, 1), repeat=length)]
    assert sum(a+b for a, b in vals)/2**length == 1
    assert sum(b for a, b in vals)/2**length <= 1
    assert bank((0,)*length)[1] == length
    checks += len(vals)+3

assert bank((0, 0))[1] == 2
assert bank((0, 1))[1] == 1
assert bank((1, 0))[1] == 0
assert sum(bank(bits)[1] for bits in product((0, 1), repeat=2))/4 == F(3, 4)
checks += 4

for i in range(20):
    length = 2**(i+1)
    weight = F(1, 2**(i+1))
    assert weight*length == 1
    checks += 1

print(json.dumps({"session": "P4-S105", "finite_checks": checks,
                  "status": "PASS_LIMITED_EXACT_SANITY_ONLY",
                  "infinite_proof_certified": False,
                  "EQ_or_SEP_certified": False}, indent=2))
