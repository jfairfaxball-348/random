#!/usr/bin/env python3
"""P4-S108 exact finite prefix audit of tree-switch quotient (NOT infinite proof)."""
from collections import Counter

def in_tree(word: str, L: int) -> bool:
    # No prefix equal to sigma + 0^(2|sigma|+L) + 1, for any sigma.
    for n in range((len(word) - L - 1) // 3 + 1):
        q = 3*n + L
        if word[n:q] == '0' * (2*n+L) and word[q] == '1':
            return False
    return True

def output_prefix(source: str, m: int, L: int) -> str:
    a, u = source[0], source[1:]
    assert len(u) >= m
    n = next((j for j in range(1, m+1) if not in_tree(u[:j], L)), None)
    return u[:m] if n is None or n == m else u[:n] + a + u[n+1:m]

def check(m: int, L: int) -> int:
    cnt = Counter()
    for i in range(1 << (m+1)):
        x = format(i, f"0{m+1}b")
        y = output_prefix(x, m, L)
        assert len(y) == m
        cnt[y] += 1
        if m>1:
            assert output_prefix(x, m-1, L) == y[:m-1]
    assert len(cnt) == (1 << m)
    assert all(v==2 for v in cnt.values())
    return 1 << (m+1)

if __name__ == "__main__":
    total=sum(check(m,5) for m in range(1,13))
    assert total == 16380
    for L in (1,2,3,5,8):
        for m in range(1,11):
            total+=check(m,L)
    assert total == 36840
    print(f"PASS {total} exact finite source-prefix assignments; infinity theorems require symbolic proof")
