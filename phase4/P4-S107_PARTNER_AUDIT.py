"""Finite prefix sanity checks for marker-deletion; NOT an infinite proof."""
from itertools import product
def words(n): return (''.join(t) for t in product('01',repeat=n))
def out(s,n):
    j=s.find('1')
    if j<0 or j>=n: return '0'*n
    return s[:j+1]+s[j+2:j+2+n-j-1]
checks=0
for n in range(2,11):
    d={}
    for s in words(n+1):
        d.setdefault(out(s,n),set()).add(s[:n])
    assert len(d)==2**n
    for a in d.values():
        assert 1<=len(a)<=2
        checks+=1
    assert d['0'*n]=={'0'*n}
    for s in words(n+1):
        k=s.find('1')
        if 0<=k<n-1:
            partner=s[:k+1]+('1' if s[k+1]=='0' else '0')+s[k+2:]
            a=d[out(s,n)]
            assert len(a)==2 and partner[:n] in a
            checks+=1
print('PASS',checks)
