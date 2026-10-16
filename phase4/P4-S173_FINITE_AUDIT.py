"""P4-S173 exact FINITE sanity: Petrović encoding and varying-map packet firewall.
No infinite theorem, external proof certification, Lean, or hosted CI is implied.
"""
from collections import Counter
from fractions import Fraction
from itertools import product

def words(n):
    return (''.join(bits) for bits in product('01', repeat=n))

def index(s):
    return 2**len(s) + sum(int(bit) << j for j, bit in enumerate(s))  # 1-based

def decode_prefix(source, n):
    out = ''
    for _ in range(n):
        p = index(out)
        assert p <= len(source)
        out += source[p - 1]
    return out

fair_checks = 0
for n in range(1, 5):
    use = 2**n - 1
    counts = Counter(decode_prefix(source, n) for source in words(use))
    assert len(counts) == 2**n
    assert set(counts) == set(words(n))
    for output in words(n):
        chosen = [index(output[:i]) for i in range(n)]
        assert len(set(chosen)) == n
        assert all(2**i <= chosen[i] < 2**(i + 1) for i in range(n))
        assert counts[output] == 2**(use - n)
        fair_checks += 1

def packet_hit(source, r):
    # G_(r,0) identity / C_(r,0)=[0^(r+2)]
    # G_(r,1) flips first bit / C_(r,1)=[1^(r+2)]
    return source.startswith('0' * (r + 2)) or source.startswith('0' + '1' * (r + 1))

def posterior(r, prefix):
    m = max(r + 2, len(prefix))
    count = sum(packet_hit(w, r) for w in words(m) if w.startswith(prefix))
    return Fraction(count, 2**(m - len(prefix)))

packet_checks = 0
for r in range(1, 7):
    assert posterior(r, '') == Fraction(1, 2**(r + 1))
    assert posterior(r, '') <= Fraction(1, 2**r)
    for depth in range(0, 8):
        for s in words(depth):
            assert posterior(r, s) == (posterior(r, s + '0') + posterior(r, s + '1')) / 2
            packet_checks += 1

for depth in range(0, 7):
    for s in words(depth):
        h = lambda t: sum((2**(r - r//2)) * posterior(r, t) for r in range(1, 7))
        assert h(s) == (h(s + '0') + h(s + '1')) / 2
        assert h(s) >= 0
        packet_checks += 1

print(f'PASS: {fair_checks} exact encoder output rows; {packet_checks} exact packet/posterior/sibling rows')
