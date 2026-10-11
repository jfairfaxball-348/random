"""P4-S095: auxiliary exact finite sanity checks. NOT a proof of infinite statements."""
from fractions import Fraction as Q
from random import Random

def raw(s: str) -> Q:
    """r=1/2+sum_{n>=1}2^(-n-1)m_n, with block B_n length n+10."""
    ans = Q(1, 2)
    start = 0
    n = 1
    while start < len(s):
        k = min(n + 10, len(s) - start)
        u = s[start:start+k]
        m = (1 << k) if "0" not in u else 0
        ans += Q(1, 1 << (n+1)) * m
        start += n + 10
        n += 1
    return ans + Q(1, 1 << n)

def stopped(s: str) -> Q:
    for j in range(len(s)+1):
        v = raw(s[:j])
        if v >= 4:
            return v
    return raw(s)

def d(s: str) -> Q:
    return (12 + stopped(s)) / 13

rng = Random(95095)
checks = 0
assert d("") == 1
checks += 1
for _ in range(1200):
    s = "".join(str(rng.randrange(2)) for _ in range(rng.randrange(0,75)))
    assert d(s+"0") + d(s+"1") == 2*d(s), s
    assert Q(12,13) <= d(s) <= Q(20,13), s
    checks += 2

# h=11 lies in B_2; the all-ones first block B_1 is legal evidence.
A = "1"*12
assert stopped(A) >= 4
checks += 1
for t in range(21):
    if t < len(A):
        pot = (1 << (len(A)-t))*d(A[:t])
    elif t == len(A):
        pot = d(A)
    else:
        gap = t-len(A)
        pot = sum((d(A+format(j, f"0{gap}b")) for j in range(1<<gap)), Q(0))/(1<<gap)
    assert pot >= Q(16,13), (t,pot)
    checks += 1

h = 3
for bits in range(1<<9):
    x = [(bits>>i)&1 for i in range(9)]
    y = x.copy()
    y[h] ^= 1
    def bad(z):
        return z[0]==0 or z[h]==1
    def select(z):
        return bad(z) and (z[0]==1 or z[h]==0)
    assert bad(x) or bad(y)
    assert select(x) != select(y)
    checks += 2
print(f"P4-S095 local exact finite checks PASS ({checks})")
