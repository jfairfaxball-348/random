"""Exact finite sanity; no infinite-fibre, CR, or central-target certification."""
from fractions import Fraction as Q
from itertools import combinations, product
import json

checks = 0
def check(value):
    global checks
    assert value
    checks += 1

# Independent distribution calculation over all 70 balanced four-row tables.
tables = [set(t) for t in combinations(range(8), 4)]
hist = {}
for table in tables:
    types = [sum(2*i+b in table for b in (0,1)) for i in range(4)]
    kind = tuple(sorted(types))
    hist[str(kind)] = hist.get(str(kind), 0)+1
    for group in (set(), {0}, {0,1}, {0,1,2}, set(range(4))):
        n = len(group)
        a = sum(2*i+b in table for i in group for b in (0,1))
        b = 2*n-a
        q, q0, q1 = Q(n,4), Q(2*n-a,4), Q(a,4)
        delta = (q0-q1)/2
        v = lambda t: t*(1-t)
        check((q0+q1)/2 == q)
        check((v(q0)+v(q1))/2 + delta*delta == v(q))
        if q0 == q:
            check(q1 == q)  # hostile correction: stable child forces stable sibling
        for i in group:
            for bit in (0,1):
                out = int(2*i+bit in table)
                offspring = a if out else b
                if offspring == 1:
                    check(types[i] == 1)  # unique actual child forbids constant row

check(hist == {'(1, 1, 1, 1)':16, '(0, 1, 1, 2)':48, '(0, 0, 2, 2)':6})

# Build finite fair reservoirs by source-cell enumeration, independently of q algebra.
for root_index in range(70):
    levels = [{tuple(s): () for s in product((0,1), repeat=2)}]
    for depth in range(5):
        prev = levels[-1]
        nodes = {}
        for s,tau in prev.items():
            nodes.setdefault(tau, []).append(s)
        nxt = {}
        for tau, candidates in nodes.items():
            check(len(candidates) == 4)
            candidates.sort()
            t = tables[(root_index+depth*13+sum(tau)*7)%70]
            for i,s in enumerate(candidates):
                for bit in (0,1):
                    nxt[s+(bit,)] = tau+(int(2*i+bit in t),)
        levels.append(nxt)
    qlevels = []
    for level in levels:
        counts = {}
        for s,tau in level.items():
            counts.setdefault(tau,[0,0])[s[0]] += 1
        for n in counts.values():
            check(sum(n) == 4)
        qlevels.append({t:Q(n[0],4) for t,n in counts.items()})
    M = {():qlevels[0][()]*(1-qlevels[0][()])}
    accumulated = {():Q(0)}
    for depth in range(5):
        for tau,q in qlevels[depth].items():
            q0,q1 = qlevels[depth+1][tau+(0,)],qlevels[depth+1][tau+(1,)]
            delta=(q0-q1)/2
            for bit,qchild in ((0,q0),(1,q1)):
                child=tau+(bit,)
                accumulated[child]=accumulated[tau]+delta*delta
                M[child]=qchild*(1-qchild)+accumulated[child]
            check((M[tau+(0,)]+M[tau+(1,)])/2 == M[tau])
    # Balanced-chart normalization with a permanent fair fallback.
    # Convert the two first-bit-0 original cells into a normalized label and tail.
    norm = {(0,):((0,0),(),False), (1,):((0,1),(),False)}
    for depth in range(4):
        bynode={}
        for s,(orig,tau,mode) in norm.items():
            bynode.setdefault(tau,[]).append((s,orig,mode))
        nextnorm={}
        for tau,rows in bynode.items():
            check(len(rows)==2)
            childouts=[]
            if not rows[0][2]:
                for s,orig,mode in rows:
                    childouts.extend(levels[depth+1][orig+(b,)][-1] for b in (0,1))
            mode=rows[0][2] or sum(childouts)!=2
            for s,orig,_ in rows:
                for b in (0,1):
                    out=b if mode else levels[depth+1][orig+(b,)][-1]
                    nextnorm[s+(b,)]=(orig+(b,),tau+(out,),mode)
        norm=nextnorm

# Nonlinear permutation and source block capital: use nonuniform d endpoint values.
def toffoli(w):
    w=list(w)
    for j in range(0,len(w),3):
        w[j+2] ^= w[j]*w[j+1]
    return tuple(w)
def d(w):
    value=Q(1)
    for j,b in enumerate(w):
        stake=Q(1,3) if j%2 else Q(-1,2)
        value *= 1+stake*(2*b-1)
    return value
for length in (3,6,9):
    endpoints={w:d(toffoli(w)) for w in product((0,1),repeat=length)}
    check(len({toffoli(w) for w in endpoints}) == 2**length)
    check(all(toffoli(toffoli(w)) == w for w in endpoints))
    values=endpoints.copy()
    for depth in range(length-1,-1,-1):
        for w in product((0,1),repeat=depth):
            values[w]=(values[w+(0,)]+values[w+(1,)])/2
            direct=sum(endpoints[w+z] for z in product((0,1),repeat=length-depth))/2**(length-depth)
            check(values[w] == direct)
    check(values[()] == d(()))
check(toffoli((1,1,0))[2] ^ toffoli((1,0,0))[2] ^
      toffoli((0,1,0))[2] ^ toffoli((0,0,0))[2] == 1)

print(json.dumps({'grade':'FINITE_SANITY_ONLY_NOT_INFINITY_OR_CR_PROOF',
                  'assertions':checks,'balanced_tables':70,'row_histogram':hist,
                  'reservoir_depths':5,'normalization_depths':4,
                  'nonlinear_block_lengths':[3,6,9],
                  'result':'PASS'},indent=2))
