from fractions import Fraction
from itertools import product

# FINITE TOY ONLY: predict zero at each even output step and hold at odd steps.
# This is not S011's uncomputable-infinite-spine witness.
def bank(t):
    b = 0
    active = 1
    for j, c in enumerate(t):
        if j % 2 == 0 and active:
            if c == '0':
                b += 1
            else:
                active = 0
    return b, active

count = 0
for n in range(12):
    for bits in product('01', repeat=n):
        s = ''.join(bits)
        b, a = bank(s)
        assert sum(sum(bank(s + e)) for e in '01') == 2 * (b + a)
        count += 1

# Test conditional source martingales for fair exact-two first-bit deletion G(az)=z.
def H(n, s):
    L = max(n + 1, len(s))
    acc = 0
    ct = 0
    for z in product('01', repeat=L):
        x = ''.join(z)
        if x.startswith(s):
            acc += bank(x[1:1+n])[0]
            ct += 1
    return Fraction(acc, ct)

for n in range(1, 7):
    for m in range(4):
        for bits in product('01', repeat=m):
            s = ''.join(bits)
            assert 2 * H(n, s) == H(n, s+'0') + H(n, s+'1')

expected = [Fraction(1,2),Fraction(1,2),Fraction(3,4),Fraction(3,4),
            Fraction(7,8),Fraction(7,8),Fraction(15,16),Fraction(15,16)]
actual = [sum((Fraction(bank(''.join(z))[0], 2**m)
               for z in product('01', repeat=m)), Fraction(0))
          for m in range(1,9)]
assert actual == expected
print('PASS', count, 'all-sibling nodes and conditional exact-rational toy martingales')
