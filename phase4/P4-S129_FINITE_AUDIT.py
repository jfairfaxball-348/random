#!/usr/bin/env python3
"""Exact finite SANITY checks. Does not prove infinite fibres or randomness."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json


def row_exhaustion(c):
    N = 2**c
    tags = [0, 0] + list(range(1, N-1))
    children = [(i, b, tags[i]) for i in range(N) for b in (0, 1)]
    rows = switches = predictions = 0
    for zero in combinations(range(2*N), N):
        zero = set(zero)
        buckets = [[children[j] for j in range(2*N) if (j in zero) == (b == 0)]
                   for b in (0, 1)]
        assert all(len(k) == N for k in buckets)
        valid = []
        for b, bucket in enumerate(buckets):
            pop = Counter(t for _, _, t in bucket)
            if len(pop) == N-1 and sorted(pop.values()) == [1]*(N-2)+[2]:
                new = next(t for t in pop if pop[t] == 2)
                if new != 0:
                    valid.append((b, new))
        assert len(valid) <= 1
        for b, new in valid:
            assert len([q for q in buckets[1-b] if q[2] == new]) == 0
            for i, bit, tag in buckets[b]:
                if tag != new:
                    options = [bb for ii, bb, tt in buckets[b] if ii == i]
                    assert options == [bit]
                    predictions += 1
            switches += 1
        rows += 1
    return dict(c=c, rows=rows, switches=switches, forced_predictions=predictions)


def branching(c, steps, clock):
    N = 2**c; r = N-1
    root = [(format(i, f'0{c}b'), 0 if i < 2 else i-1, 'active') for i in range(N)]
    tree = {'': ('active', 0, root)}
    capitals = {w: Fraction(1) for w, _, _ in root}
    cylinders = incidences = martingale_edges = 0
    for m in range(steps):
        for tau in sorted(t for t in tree if len(t) == m):
            mode, old, cells = tree[tau]
            kids = {0: [], 1: []}; bets = {}
            if mode == 'active':
                counts = Counter(t for _, t, _ in cells)
                assert counts[old] == 2 and len(counts) == r
                do_switch = m % (2 if clock == 0 else 3) == 0
                new = (old+1) % r if do_switch else old
                preferred = 0 if clock == 0 or not tau else int(tau[-1])
                pair = sorted(w for w, t, _ in cells if t == old)
                if do_switch:
                    kids[preferred].append((pair[0]+'0', old, 'active'))
                    kids[1-preferred].append((pair[0]+'1', old, 'solo'))
                    kids[1-preferred].extend((pair[1]+b, old, 'pair') for b in '01')
                    bets[pair[0]] = 0
                    for w, t, _ in cells:
                        if t == new:
                            kids[preferred].extend((w+b, t, 'active') for b in '01')
                        elif t != old:
                            for b in (0, 1): kids[b].append((w+str(b), t, 'active' if b == preferred else 'solo'))
                            bets[w] = preferred
                    tree[tau+str(preferred)] = ('active', new, kids[preferred])
                    tree[tau+str(1-preferred)] = ('safe', -1, kids[1-preferred])
                else:
                    for b, w in enumerate(pair):
                        kids[b].extend((w+j, old, 'active') for j in '01')
                    for w, t, _ in cells:
                        if t != old:
                            for b in (0, 1): kids[b].append((w+str(b), t, 'active'))
                    for b in (0, 1): tree[tau+str(b)] = ('active', old, kids[b])
            else:
                pair = sorted(w for w, t, typ in cells if typ == 'pair')
                assert len(pair) == 2
                for b, w in enumerate(pair):
                    kids[b].extend((w+j, -1, 'pair') for j in '01')
                for w, t, typ in cells:
                    if typ == 'solo':
                        for b in (0, 1): kids[b].append((w+str(b), t, 'solo'))
                for b in (0, 1): tree[tau+str(b)] = ('safe', -1, kids[b])
            for w, _, _ in cells:
                cap = capitals[w]
                for b in (0, 1):
                    capitals[w+str(b)] = cap if w not in bets else (2*cap if b == bets[w] else Fraction(0))
                assert capitals[w+'0']+capitals[w+'1'] == 2*cap
                martingale_edges += 1
            for b in (0, 1):
                kind, tag, child = tree[tau+str(b)]
                assert len(child) == N and len({w for w, _, _ in child}) == N
                assert Fraction(len(child), 2**(m+c+1)) == Fraction(1, 2**(m+1))
                if kind == 'safe':
                    assert Counter(typ for w, t, typ in child) == {'pair': 2, 'solo': N-2}
                cylinders += 1; incidences += N
        source_words = [w for t, (_, _, ws) in tree.items() if len(t) == m+1 for w, _, _ in ws]
        assert len(source_words) == len(set(source_words)) == 2**(m+c+1)
    # A finite approximation to one ACTIVE path; correct accounts grow in EVERY tag.
    target = ''; active_switches = 0
    for m in range(steps):
        do_switch = m % (2 if clock == 0 else 3) == 0
        b = (0 if clock == 0 or not target else int(target[-1])) if do_switch else m % 2
        target += str(b); active_switches += do_switch
    mode, old, cells = tree[target]
    assert mode == 'active'
    for tag in range(r):
        tagcaps = [capitals[w] for w, t, _ in cells if t == tag]
        assert max(tagcaps) >= 2**(active_switches//2)
    return dict(c=c, clock=clock, cylinders=cylinders, incidences=incidences,
                source_martingale_edges=martingale_edges, active_switches=active_switches)


def normalized_fallback(steps=9):
    tree = {'': (False, ['0', '1'])}; checks = fallbacks = 0
    for m in range(steps):
        for tau in sorted(q for q in tree if len(q) == m):
            fallback, cells = tree[tau]
            # A 3:1 original row off the all-zero target; it MUST trigger fallback.
            invalid = not fallback and tau.endswith('1') and m % 3 == 1
            fold = not invalid and m % 2 == 0
            if invalid:
                original = [0, 0, 0, 1]
                assert Counter(original) != {0: 2, 1: 2}
                fallback = True; fallbacks += 1
            outputs = [0, 1, 0, 1] if fallback or not fold else [0, 0, 1, 1]
            kids = {0: [], 1: []}
            for j, w in enumerate(cells):
                for b in (0, 1): kids[outputs[2*j+b]].append(w+str(b))
            for b in (0, 1):
                assert len(kids[b]) == 2
                assert Fraction(2, 2**(m+2)) == Fraction(1, 2**(m+1))
                tree[tau+str(b)] = (fallback, kids[b]); checks += 1
        assert tree['0'*(m+1)][0] is False
    assert fallbacks > 0
    return dict(cylinders=checks, fallback_events=fallbacks)


def late_mixture():
    # Four late all-in accounts and an exact unstarted rational tail.
    def account(s, i):
        cap = Fraction(1)
        for n, bit in enumerate(s):
            if n >= i+1: cap *= 2 if int(bit) == i % 2 else 0
        return cap
    def W(s):
        n = len(s)
        return sum((Fraction(1, 2**(i+1))*account(s, i) for i in range(n)), Fraction(1, 2**n))
    checks = 0
    for n in range(8):
        for j in range(2**n):
            s = format(j, f'0{n}b') if n else ''
            assert W(s+'0')+W(s+'1') == 2*W(s)
            checks += 1
    return dict(exact_mixture_nodes=checks)


if __name__ == '__main__':
    results = {'label': 'SANITY_ONLY_NOT_INFINITE_PROOF',
               'rows': [row_exhaustion(c) for c in (2, 3)],
               'branching': [branching(c, 10 if c == 2 else 8, clock) for c in (2, 3) for clock in (0, 1)],
               'normalized_fallback': normalized_fallback(), 'late_mixture': late_mixture()}
    print(json.dumps(results, indent=2))
