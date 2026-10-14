#!/usr/bin/env python3
"""Exact finite SANITY for P4-S130, not an infinite-randomness proof."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json

def historical_one_surplus(c):
    n=2**c; tags=[0,0]+list(range(1,n-1)); children=[(i,b,tags[i]) for i in range(n) for b in range(2)]
    rows=switches=predictions=0
    for subset in combinations(range(2*n),n):
        s=set(subset); buckets=[[children[j] for j in range(2*n) if (j in s)==(b==0)] for b in (0,1)]
        assert len(buckets[0])==len(buckets[1])==n
        valid=[]
        for b,bucket in enumerate(buckets):
            pop=Counter(t for _,_,t in bucket)
            if len(pop)==n-1 and sorted(pop.values())==[1]*(n-2)+[2]:
                new=next(t for t in pop if pop[t]==2)
                if new!=0: valid.append((b,new))
        assert len(valid)<=1
        for b,new in valid:
            assert not any(t==new for _,_,t in buckets[1-b])
            for i,bit,tag in buckets[b]:
                if tag!=new:
                    assert [bb for ii,bb,_ in buckets[b] if ii==i]==[bit]
                    predictions+=1
            switches+=1
        rows+=1
    return dict(c=c,rows=rows,switches=switches,forced_predictions=predictions)

def t_code(k):
    if k==1:return ['']
    return ['1'*j+'0' for j in range(k-1)]+['1'*(k-1)]

def finite_tagged_cap(a,depth=7):
    # G(b p u)=b u, p in P_a if b=0, p in P_3 if b=1.
    counts=0
    for m in range(1,depth+1):
        for bits in product('01',repeat=m):
            t=''.join(bits); k=a if t[0]=='0' else 3
            assert sum((Fraction(1,2**(len(p))) for p in t_code(k)),Fraction())==1
            assert len([t[0]+p+t[1:] for p in t_code(k)])==k
            counts+=1
    return {'lower_degree':a,'high_degree':3,'tested_output_cylinders':counts}

def fat_boundary(levels=4):
    sizes=[n+3 for n in range(1,levels+1)]
    kept=1; price=Fraction(1); stages=[]; total=0
    for n,d in enumerate(sizes,1):
        patch_count=kept; kept*=2**d-1; total+=patch_count
        price*=Fraction(2**d-1,2**d)
        stages.append({'stage':n,'block_length':sum(sizes[:n]),'new_patch_cylinders':patch_count,
                       'survivor_cylinders':kept,'remaining_measure':str(price)})
    assert price>=Fraction(7,8)
    assert sum((Fraction(1,2**(n+3)) for n in range(1,30)),Fraction())<Fraction(1,8)
    return {'stage_table':stages,'lower_bound_infinite_boundary':'7/8','finite_patch_cylinders':total}

def patch_prefix(w,m):
    offset=0;n=0
    while True:
        n+=1;d=n+3;end=offset+d
        if end>=m:return w[:m]
        if w[offset:end]=='0'*d:return w[:end]+w[end+n:m+n]
        offset=end

def patch_price_check(max_output_bits=8):
    # An input prefix of 2m bits decides the first m output bits.
    cases=0;source_cells=0
    for m in range(1,max_output_bits+1):
        price=Counter(patch_prefix(''.join(z),m) for z in product('01',repeat=2*m))
        assert len(price)==2**m
        assert set(price.values())=={2**m}
        cases+=2**m;source_cells+=2**(2*m)
    return {'checked_output_cylinders':cases,'source_words':source_cells,
            'measure_test':'all_m_cylinders_have_2^m_preimages_at_input_level_2m'}

def sheet_divisibility(c=3):
    n=2**c;records=[]
    for a in range(1,n+1):
        q=Fraction(1,a)
        dyadic=q.denominator&(q.denominator-1)==0
        records.append({'cells':a,'required_clopen_image_measure':str(q),'dyadic_possible':dyadic})
    assert [x['cells'] for x in records if x['dyadic_possible']]==[1,2,4,8]
    return records

def historical_fallback(depth=9):
    tree={'':(False,['0','1'])};cases=events=0
    for m in range(depth):
        for tau in sorted(t for t in tree if len(t)==m):
            bad,cells=tree[tau]
            invalid=not bad and tau.endswith('1') and m%3==1
            if invalid:
                assert Counter([0,0,0,1])!={0:2,1:2};bad=True;events+=1
            outputs=[0,1,0,1] if bad or m%2 else [0,0,1,1]
            children={0:[],1:[]}
            for j,w in enumerate(cells):
                for b in (0,1):children[outputs[2*j+b]].append(w+str(b))
            for b in (0,1):
                assert len(children[b])==2
                tree[tau+str(b)]=(bad,children[b]);cases+=1
        assert not tree['0'*(m+1)][0]
    return {'cylinders':cases,'fallback_events':events}

def historical_late_mixture():
    def account(w,i):
        z=Fraction(1)
        for j,ch in enumerate(w):
            if j>=i+1:z*=2 if int(ch)==i%2 else 0
        return z
    def W(w):
        n=len(w)
        return sum((Fraction(1,2**(i+1))*account(w,i) for i in range(n)),Fraction(1,2**n))
    count=0
    for n in range(8):
        for bits in product('01',repeat=n):
            w=''.join(bits)
            assert W(w+'0')+W(w+'1')==2*W(w);count+=1
    return count

if __name__=='__main__':
    data={'label':'SANITY_ONLY_NOT_INFINITE_PROOF','s129_rows':[historical_one_surplus(i) for i in (2,3)],
          's129_fallback':historical_fallback(),'s129_late_mixture':historical_late_mixture(),
          'variable_f3':[finite_tagged_cap(1),finite_tagged_cap(2)],'fat_closed_boundary':fat_boundary(),
          'fat_boundary_cylinder_check':patch_price_check(),'constant_sheet_divisibility_c3':sheet_divisibility()}
    assert [x['rows'] for x in data['s129_rows']]==[70,12870]
    assert data['s129_fallback']=={'cylinders':1022,'fallback_events':21}
    assert data['s129_late_mixture']==255
    print(json.dumps(data,indent=2))
