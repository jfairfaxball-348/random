from fractions import Fraction
from itertools import product
Q=(1,2,3)
rows=[(q,t,2*q-t,Fraction(t,2*q)) for q in Q for t in Q if 0<=2*q-t<=4]
assert {(q,t,s) for q,t,s,p in rows}=={(1,1,1),(1,2,0),(2,1,3),(2,2,2),(2,3,1),(3,2,4),(3,3,3)}
edges={(q,t) for q,t,s,p in rows}
walks=0
for n in range(1,9):
    for path in product(Q,repeat=n+1):
        if all((path[i],path[i+1]) in edges for i in range(n)):
            v=Fraction(1)
            for i in range(n): v*=Fraction(path[i+1],path[i])
            assert v==Fraction(path[-1],path[0]) and Fraction(1,3)<=v<=3
            walks+=1
for k in range(1,26):
    p=Fraction(1,2**(4*k))
    h=Fraction(1,2**(3*k+1))  # shift G, all-zero output, prefix zero^k
    assert h<=2**k*p and Fraction(1,2**k)/h>=2**(2*k)
assert len(rows)==7 and walks==5736
print("PASS 7 transitions; 5736 telescoping walks; 25 priced delayed-account tests; FINITE SANITY ONLY")
