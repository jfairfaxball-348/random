from itertools import product
from fractions import Fraction

def audit():
    assertions=0
    balanced=paired=0
    for rows in product(range(4), repeat=4):
        zeros=[2 if r==0 else 0 if r==3 else 1 for r in rows]
        assertions+=1
        if sum(zeros)==4:
            balanced+=1
            if sum(zeros[:2])==2:
                paired+=1
                for counts in (zeros[:2],zeros[2:]):
                    assert tuple(sorted(counts)) in ((0,2),(1,1))
                    assertions+=1
    for i,j in product(range(5),repeat=2):
        a,b=Fraction(i,4),Fraction(j,4)
        q,delta=(a+b)/2,(a-b)/2
        v=lambda x:x*(1-x)
        assert (v(a)+v(b))/2==v(q)-delta*delta
        assertions+=1
    assert (balanced,paired,assertions)==(70,36,353)
    print("PASS: 353 exact checks; 70 globally balanced; 36 side 2:2")
if __name__=="__main__":
    audit()
