#!/usr/bin/env python3
"""P4-S075 finite exact-rational escrow tables. Algebra only, not a global scan proof."""
from fractions import Fraction as F
from itertools import product

def q(i):
    return 1 - F(1, 2 ** (i + 2))

def hat_d(values):
    """Exact stopped-savings sum from the finite complete virtual wager history."""
    k = 1
    while 2 ** k <= max(values):
        k += 1
    amount = sum((next((x for x in values if x >= 2 ** j), values[-1])
                  * F(1, 2 ** j) for j in range(1, k + 1)), F(0))
    return amount + values[-1] * F(1, 2 ** k)

def extension(values, i, c0, s, r, previous_r):
    first = values[-1] * (1 + q(i) * previous_r * r * c0)
    second = first * (1 + q(i) * r * s)
    return values + [first, second]

def audit():
    assignments = 0
    mirror_checks = 0
    for signs in product((-1, 1), repeat=12):
        triples = [signs[3*i:3*i+3] for i in range(4)]
        values = [F(1)]
        original_e = savings_e = F(1)
        previous_r = 1
        for i, (c0, s, r) in enumerate(triples):
            direct_g = lambda rr: (1 + q(i)*c0*previous_r*rr) * (1 + q(i)*s*rr)
            direct_p = 1 + q(i)**2 * c0*s*previous_r
            assert (direct_g(-1) + direct_g(1))/2 == direct_p
            assert (1 + q(i)**2*c0*previous_r*(-1) +
                    1 + q(i)**2*c0*previous_r*(+1))/2 == 1
            original_e *= direct_p
            original_e *= direct_g(r) / direct_p

            start = hat_d(values)
            w = {ss: {rr: hat_d(extension(values,i,c0,ss,rr,previous_r))/start
                      for rr in (-1,1)} for ss in (-1,1)}
            p = {ss: (w[ss][-1] + w[ss][1])/2 for ss in (-1,1)}
            assert min(p.values()) > 0
            assert (p[-1] + p[1])/2 == 1
            assert (w[s][-1]/p[s] + w[s][1]/p[s])/2 == 1
            savings_e *= p[s]
            savings_e *= w[s][r]/p[s]
            values = extension(values, i, c0, s, r, previous_r)
            assert original_e == values[-1]
            assert savings_e == hat_d(values)
            mirror_checks += 1
            previous_r = r
        assignments += 1
    prices_checked = 0
    half = F(1,2)
    for c0,c1,s in product((-1,1), repeat=3):
        gg = lambda r: (1+half*c0*r)*(1+half*c1*r)*(1+half*s*r)
        price = (gg(-1)+gg(1))/2
        assert price == 1+half**2*(c0*c1+s*(c0+c1))
        prices_checked += 1
    assert (F(7,4)+F(3,4))/2 == F(5,4)
    print('assignments',assignments,'group mirror equalities per compiler',mirror_checks,
          'triple price checks',prices_checked,'discrepancies 0')

if __name__ == '__main__':
    audit()
