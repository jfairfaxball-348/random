#!/usr/bin/env python3
"""P4-S094 finite exact audit: not an infinitary randomness proof."""
from fractions import Fraction
def d(s):
    return Fraction(1) if not s else Fraction(3,2) if s[0]=='1' else Fraction(1,2)
def psi(t,h,tail):
    fixed={0:'1',h:'1'}
    fixed.update({h+1+i:b for i,b in enumerate(tail)})
    measure=Fraction(1,2**(2+len(tail)))
    total=Fraction(0)
    for k in range(1<<t):
        s=format(k,f'0{t}b') if t else ''
        if all(s[i]==b for i,b in fixed.items() if i<t):
            total+=Fraction(1,2**t)*d(s)
    return total/measure
checks=0
for h in range(2,9):
    for tail in ('','0','1','01','10','001'):
        for t in range(h+len(tail)+4):
            p=psi(t,h,tail)
            assert p>=Fraction(3,2)
            if t>=h+1+len(tail): assert p==Fraction(3,2)
            checks+=1
assert d('0')+d('1')==2*d('')
print(f'P4-S094 ASSCL finite audit PASS ({checks} exact inequalities)')
