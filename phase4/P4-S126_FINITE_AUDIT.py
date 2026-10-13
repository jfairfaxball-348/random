from fractions import Fraction as Q

# P4-S126: exact finite sanity only, not the topological/measure-theoretic proof.
def actual_pair_success(pair, output_regime):
    if output_regime == "K":
        return {a for a, b in pair} == {0, 1}
    c = int(output_regime[-1])
    return set(pair) == {(c, 0), (c, 1)}

D = [(0, 0), (1, 0)]
P0 = [(0, 0), (0, 1)]
P1 = [(1, 0), (1, 1)]
assertions = 0
for regime in ("K", "U0", "U1"):
    assert sum((Q(1, 3) * actual_pair_success(p, regime)
                for p in (D, P0, P1)), Q(0)) == Q(1, 3)
    assertions += 1
    assert (Q(1, 2) * actual_pair_success(D, regime) +
            (Q(1, 2) if regime != "K" else Q(0))) == Q(1, 2)
    assertions += 1

for denominator in range(1, 40):
    partial_best = max(min(Q(a, denominator), Q(denominator-a, denominator))
                       for a in range(denominator+1))
    assert partial_best <= Q(1, 2)
    assertions += 1
    total_best = max(min(Q(a, denominator), Q(b, denominator),
                         Q(denominator-a-b, denominator))
                     for a in range(denominator+1)
                     for b in range(denominator-a+1))
    assert total_best <= Q(1, 3)
    assertions += 1

assert assertions == 84
print("P4-S126: 84 exact finite assertions PASS (SANITY ONLY)")
