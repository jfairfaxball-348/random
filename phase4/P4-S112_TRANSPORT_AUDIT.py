#!/usr/bin/env python3
"""Exact bounded sanity for S112. No infinite/randomness theorem is tested here."""
import json
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

checks = Counter()

def check(ok, group):
    assert ok, group
    checks[group] += 1

def words(n):
    return map(''.join, product('01', repeat=n))

# Independent abstract inverse-count audit: ALL paired permutations on four
# atoms, including moved K (odd fibres) and mismatched labels (0/4 fibres).
K, U0, U1 = {0, 1}, {2}, {3}
for p0 in permutations(range(4)):
    for p1 in permutations(range(4)):
        inv0 = {v: i for i, v in enumerate(p0)}
        inv1 = {v: i for i, v in enumerate(p1)}
        k0, k1 = {p0[v] for v in K}, {p1[v] for v in K}
        a0, a1 = {p0[v] for v in U0}, {p1[v] for v in U1}
        fibres = Counter()
        # Explicit input atoms: each key has one source over each K atom and
        # two independent b-variants over each of its supported exit atoms.
        for a, p in enumerate((p0, p1)):
            for v in K:
                fibres[p[v]] += 1
            for v in (U0 if a == 0 else U1):
                for b in (0, 1):
                    fibres[p[v]] += 1
        for y in range(4):
            n = int(y in k0) + int(y in k1) + 2*int(y in a0) + 2*int(y in a1)
            check(fibres[y] == n, 'abstract_actual_inverse_count')
        exact_two = all(fibres[y] == 2 for y in range(4))
        partition = k0 == k1 and not (a0 & a1) and (a0 | a1) == set(range(4))-k0
        q = tuple(inv1[p0[v]] for v in range(4))
        relative = {q[v] for v in K} == K and {q[v] for v in U0} == U0
        check(exact_two == partition == relative, 'relative_compatible_classification')
        if exact_two:
            for a in (0, 1):
                for v in range(4):
                    check((p0 if a == 0 else p1)[v] == p1[q[v] if a == 0 else v], 'factorization')

def good_block(s, L):
    # Test patterns directly rather than importing S111 forward code.
    return not any(s[2*q:2*q+2*(2*q+L+1)] == '00'*(2*q+L)+'11'
                   for q in range(len(s)//2+1)
                   if 2*q+2*(2*q+L+1) <= len(s))

def exit_depth(s, L):
    return next((n for n in range(1, len(s)+1) if not good_block(s[:n], L)), None)

def switch(a, u, L):
    n = exit_depth(u, L)
    return u if n is None or n == len(u) else u[:n]+a+u[n+1:]

def flip_exit(v, L):
    n = exit_depth(v, L)
    return v if n is None or n == len(v) else v[:n]+str(1-int(v[n]))+v[n+1:]

def swap(v, L):
    n = exit_depth(v, L)
    cutoff = len(v) if n is None else n
    return ''.join(v[j:j+2][::-1] if j+2 <= cutoff else v[j:j+2]
                   for j in range(0, len(v), 2))

for L in (0, 1, 2):
    for m in range(1, 10):
        common, onesided, hybrid = Counter(), Counter(), Counter()
        for x in words(m+2):
            a, u = x[0], x[1:]
            v = switch(a, u, L)
            common[flip_exit(v, L)[:m]] += 1
            onesided[(flip_exit(v, L) if a == '0' else v)[:m]] += 1
            qv = swap(v, L) if a == '0' else v
            hybrid[flip_exit(qv, L)[:m]] += 1
        for tau in words(m):
            check(common[tau] == 4, 'coherent_mixing_exact_finite_price')
            check(hybrid[tau] == 4, 'noncommon_coherent_hybrid_finite_price')
            n = exit_depth(tau, L)
            expected = 4 if n is None or n == m else (8 if tau[n] == '1' else 0)
            check(onesided[tau] == expected, 'one_sided_zero_four_countermodel')
    for n in range(0, 12):
        for v in words(n):
            rv = flip_exit(v, L)
            check(flip_exit(rv, L) == v, 'common_mixing_involution')
            check(exit_depth(rv, L) == exit_depth(v, L), 'common_mixing_exit_invariance')
            if n >= 1:
                check(rv[:-1] == flip_exit(v[:-1], L), 'common_mixing_prefix_consistency')
            if n % 2 == 0:
                check(swap(swap(v, L), L) == v, 'relative_compatible_block_involution')
    # Infinite inverse formula's finite projections, with tail t explicit.
    for y in words(10):
        n = exit_depth(y, L)
        if n is not None and n < len(y):
            key = str(1-int(y[n]))
            for b in '01':
                u = y[:n]+b+y[n+1:]
                check(flip_exit(switch(key, u, L), L) == y, 'actual_first_exit_inverse_formula')

# Noncomputable-measure counterexample's COMPUTABLE finite tree rule.
# Finite entry schedules test rule consistency, not undecidability of A.
schedule = {0: 7, 1: 2, 2: 12}
def code(e):
    return '1'*(2*e+3)+'0'
def delayed_good(s):
    return not any(stage <= len(s) and s.startswith(code(e))
                   for e, stage in schedule.items())
def delayed_switch(a, u):
    n = next((j for j in range(1, len(u)+1) if not delayed_good(u[:j])), None)
    return u if n is None or n == len(u) else u[:n]+a+u[n+1:]
for m in range(1, 12):
    counts = Counter()
    keys = {}
    for x in words(m+1):
        check(all(delayed_good(x[:j]) for j in range(len(x)+1)) if delayed_good(x) else True,
              'delayed_enumeration_prefix_closed_tree')
        y = delayed_switch(x[0], x[1:])[:m]
        counts[y] += 1
        keys.setdefault(y, set()).add(x[0])
    for y in words(m):
        check(counts[y] == 2, 'noncomputable_stratum_map_exact_finite_price')
        bad = next((j for j in range(1, m+1) if not delayed_good(y[:j])), None)
        check(len(keys[y]) == (2 if bad is None or bad == m else 1), 'D1_prefix_ghost_last_exit')
for e in range(10):
    w = Fraction(1, 4**(e+2))
    tail = w/3
    check(tail+w/12 < w-w/12, 'base_four_digit_recovery_gap')
    for j in range(e):
        check(not code(e).startswith(code(j)) and not code(j).startswith(code(e)), 'prefix_free_halting_code')

# Arbitrary finite fair exact-two tables, all eight source atoms assigned to
# four output atoms (2520 partitions). Closed-chart source sheets have exactly
# computable masses and dominated output submeasures in this finite analogue.
seen = set()
for pp in permutations(range(8)):
    assignment = tuple(tuple(sorted(pp[2*j:2*j+2])) for j in range(4))
    if assignment in seen:
        continue
    seen.add(assignment)
    for mask in range(16):
        selected = [j for j in range(4) if mask & (1 << j)]
        b0 = {assignment[j][0] for j in selected}
        b1 = {assignment[j][1] for j in selected}
        check(not (b0 & b1), 'closed_chart_disjoint_rank_sheets')
        check(Fraction(len(b0)+len(b1), 8) == Fraction(len(selected), 4), 'closed_chart_total_mass_subtraction')
        for j in range(4):
            nu = Fraction(int(j in selected), 8)
            check(nu <= Fraction(1, 4), 'closed_chart_pushforward_domination')

result = {'status': 'PASS', 'finite_only': True, 'checks': dict(checks),
          'total_assertions': sum(checks.values()),
          'not_proved_by_script': ['infinite_fibres', 'CR_conservation', 'R2_conservation',
                                  'noncomputability', 'DP2', 'CP2', 'EQ', 'SEP']}
Path(__file__).with_name('P4-S112_FINITE_AUDIT.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
