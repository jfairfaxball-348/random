#!/usr/bin/env python3
"""P4-S127: exact finite sanity for T_k, not infinite proof."""
from fractions import Fraction

def code(k):
    return ["1"*j+"0" for j in range(k-1)] + ["1"*(k-1)]

def output(k, bits, n):
    p = next(p for p in code(k) if bits.startswith(p))
    return bits[len(p):len(p)+n]

def main():
    cases=0
    for k in range(2,7):
        assert sum((Fraction(1,2**len(p)) for p in code(k)),Fraction())==1
        for n in range(7):
            counts={}
            for i in range(1 << (n+k-1)):
                bits=format(i,f"0{n+k-1}b")
                y=output(k,bits,n)
                counts[y]=counts.get(y,0)+1
            assert len(counts)==(1<<n)
            assert set(counts.values())=={1<<(k-1)}
            cases+=1<<n
    assert cases==635
    print("PASS 635 exact output-cylinder cases, k=2..6, m=0..6 (SANITY only)")

if __name__=="__main__":
    main()
