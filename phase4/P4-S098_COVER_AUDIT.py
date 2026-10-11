from fractions import Fraction
from itertools import product

def hit(prefix, k):
    # Conditional-density martingale for the computable clopen C_k=[1^(2k)].
    w = (1,)*(2*k)
    if len(prefix) <= len(w):
        return Fraction(2**len(prefix)) if tuple(prefix)==w[:len(prefix)] else Fraction(0)
    return Fraction(2**len(w)) if tuple(prefix[:len(w)])==w else Fraction(0)

checks=0
for k in range(1,9):
    assert hit((),k)==1;checks+=1
    for n in range(0,7):
        for p in product((0,1),repeat=n):
            assert hit(p+(0,),k)+hit(p+(1,),k)==2*hit(p,k)
            checks+=1
for n in range(1,9):
    weighted=sum(Fraction(1,2**k)*hit((1,)*(2*n),k) for k in range(1,n+1))
    assert weighted==2**(n+1)-2
    checks+=1
for n in range(1,25):
    N=2**(n+2);q=Fraction(1,2**(2*n+4))
    assert 2*N*q==Fraction(1,2**(n+1))<=Fraction(1,2**n)
    checks+=1
for m in range(1,17):
    assert Fraction(2**m-1,2**m)==1-Fraction(1,2**m)
    checks+=1
print('P4-S098 rational finite audit PASS:', checks, 'assertions')
