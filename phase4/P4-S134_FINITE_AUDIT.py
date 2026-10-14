#!/usr/bin/env python3
"""S134 exact Fraction finite sanity ONLY: not infinite-fibre proof."""
from fractions import Fraction
import json

def audit(depth=12):
    rows={'':[('A','00'),('A','01'),('A','10'),('B','11')]}
    targets=occurrences=even=odd=safe=0
    for m in range(depth+1):
        allcells=[]
        for tau,row in rows.items():
            targets+=1;occurrences+=4
            assert len(row)==4 and len(set(s for _,s in row))==4
            assert all(len(s)==m+2 for _,s in row)
            assert Fraction(4,2**(m+2))==Fraction(1,2**m)
            allcells += [s for _,s in row]
            if '1' not in tau:
                ab=(sum(t=='A' for t,_ in row),sum(t=='B' for t,_ in row))
                assert ab==((3,1) if m%2==0 else (2,2))
                if m%2: odd+=1
                else: even+=1
            else:
                assert [t for t,_ in row]==['P','P','S','S']
                if tau.index('1')<len(tau)-1:
                    assert row[0][1][:-1]==row[1][1][:-1]
                    assert row[0][1][-1]!=row[1][1][-1]
                safe+=1
        assert len(allcells)==len(set(allcells))==2**(m+2)
        if m==depth:break
        nxt={}
        for tau,row in rows.items():
            if '1' not in tau:
                A=[s for t,s in row if t=='A'];B=[s for t,s in row if t=='B']
                if m%2==0:
                    z=[('A',A[0]+b) for b in '01']+[('B',B[0]+b) for b in '01']
                    o=[('P',A[1]+b) for b in '01']+[('S',A[2]+b) for b in '01']
                else:
                    z=[('A',A[0]+b) for b in '01']+[('A',A[1]+'0'),('B',B[0]+'0')]
                    o=[('P',A[1]+'1'),('P',B[0]+'1'),('S',B[1]+'0'),('S',B[1]+'1')]
            else:
                p,q,r,s=[s for _,s in row]
                z=[('P',p+b) for b in '01']+[('S',r+'0'),('S',s+'0')]
                o=[('P',q+b) for b in '01']+[('S',r+'1'),('S',s+'1')]
            assert len(z)==len(o)==4
            assert set(s for _,s in z+o)=={s+b for _,s in row for b in '01'}
            nxt[tau+'0']=z;nxt[tau+'1']=o
        rows=nxt
    return dict(result='PASS_SANITY_ONLY',levels=depth,output_cylinders=targets,
                aligned_source_occurrences=occurrences,last_input_count=2**(depth+2),
                safe_states=safe,even_spine=even,odd_spine=odd)
if __name__=='__main__':print(json.dumps(audit(),indent=2))
