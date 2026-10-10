#!/usr/bin/env python3
"""P4-S087 finite sanity audit (exact rational arithmetic).

Checks, on finite truncations only:
  Part 1  the termwise excess inequality  sum_k gamma <= Psi + E  and its
          components, for four width-two maps on L-bit inputs:
            (a) a raw one-hole scan F_T,
            (b) Q o F_T with Q a non-causal output pair-swap (non-scan cells),
            (c) F_T o K with K the committed 3-bit block matrix A,
            (d) F_T o D' (tail-coded hole);
          for (a)-(c) with block-separated candidates E = 0, hence
          sum_k gamma <= Psi; for (d) violations sum_k gamma > Psi exist.
  Part 2  monotonicity of the split count f_t along output branches.
  Part 3  the graded frame J (J(z)_i = sum_l C(f(i),l) z_{i-l}, f(i)=isqrt(i))
          turns the tail-coded fibre pairs of F_T o D'^j (j=1,2) into
          finitely supported differences, while raw-frame differences are tails.
The infinitary statements of P4-S087 rest on the written proofs, not on this audit.
"""
from fractions import Fraction as Fr
from itertools import product
from math import comb, isqrt
import random

random.seed(87)
L = 9
INPUTS = list(product((0, 1), repeat=L))
A = [[1, 0, 1], [1, 1, 0], [1, 1, 1]]  # committed block matrix


def scan_transcript(v):
    """One-hole scan of v (length L): hold q, filler frontier M.
    Resolve (read the hold) when the last filler read is 1 and M-q>=2."""
    q, M, out, last = 0, 1, [], None
    while len(out) < L - 1:
        if last == 1 and M - q >= 2:
            out.append(v[q]); q, M, last = M, M + 1, None
        else:
            out.append(v[M]); last = v[M]; M += 1
    return tuple(out)


def Dprime(z):
    return tuple(z[0] if i == 0 else z[i] ^ z[i - 1] for i in range(len(z)))


def block_A(z):
    out = list(z)
    for b in range(0, len(z) - len(z) % 3, 3):
        x = z[b:b + 3]
        for r in range(3):
            out[b + r] = sum(A[r][c] * x[c] for c in range(3)) % 2
    return tuple(out)


def pair_swap(t):
    t = list(t)
    for i in range(0, len(t) - 1, 2):
        t[i], t[i + 1] = t[i + 1], t[i]
    return tuple(t)


MAPS = {
    'a_raw_scan': lambda z: scan_transcript(z),
    'b_swap_after_scan': lambda z: pair_swap(scan_transcript(z)),
    'c_scan_of_blockA': lambda z: scan_transcript(block_A(z)),
    'd_scan_of_Dprime': lambda z: scan_transcript(Dprime(z)),
}


def savings_martingale(seed):
    rng = random.Random(seed)
    stakes = {}

    def theta(w):
        if w not in stakes:
            stakes[w] = Fr(rng.choice([-3, -2, -1, 0, 1, 2, 3]), 4)
        return stakes[w]
    memo = {(): (Fr(1), Fr(1), Fr(0))}  # d0, active A, bank B

    def get(w):
        if w in memo:
            return memo[w]
        d0p, Ap, Bp = get(w[:-1])
        th = theta(w[:-1])
        d0 = d0p * (1 + th * (2 * w[-1] - 1))
        Anew = Ap * (d0 / d0p) if d0p != 0 else Ap
        Bnew = Bp
        while Anew >= 2:
            Anew -= 1; Bnew += 1
        memo[w] = (d0, Anew, Bnew)
        return memo[w]

    def d(w):
        _, a, b = get(w)
        return a + b
    return d


def cells(G, m):
    c = {}
    for z in INPUTS:
        c.setdefault(G(z)[:m], []).append(z)
    return c


def consistent(z, sigma):
    return all(z[k] == b for k, b in sigma.items())


def potentials(G, d, sigma, K0, m):
    psi = Fr(0); gsum = Fr(0); exc = Fr(0); f_of = {}
    for w, pts in cells(G, m).items():
        sp = [z for z in pts if consistent(z, sigma)]
        weight = Fr(1, 2 ** m) * d(w)
        if not sp:
            f_of[w] = 0
            continue
        psi += weight
        f = sum(1 for k in K0 if len({z[k] for z in sp}) == 2)
        f_of[w] = f
        gsum += weight * f
        exc += weight * max(f - 1, 0)
    s = Fr(2 ** len(sigma))
    return s * psi, s * gsum, s * exc, f_of


checks = 0
violations = {}
for name, G in MAPS.items():
    violations[name] = 0
    for trial in range(12):
        d = savings_martingale(1000 * trial + len(name))
        sigma = {0: random.randint(0, 1)} if trial % 2 else {}
        free = [k for k in range(L) if k not in sigma]
        if name.startswith('c'):
            K0 = [3 * j + random.randint(0, 2) for j in (1, 2)]  # distinct blocks
        else:
            K0 = sorted(random.sample([k for k in free if k >= 1], 3))
        K0 = [k for k in K0 if k not in sigma]
        psi, gsum, exc, _ = potentials(G, d, sigma, K0, L - 1)
        assert gsum <= psi + exc, (name, trial)
        checks += 1
        if name[0] in 'abc':
            assert exc == 0 and gsum <= psi, (name, trial, exc)
            checks += 1
        if gsum > psi:
            violations[name] += 1
# deterministic tail-coded violation: sigma empty, K0 above the hold region
d = savings_martingale(7)
psi, gsum, exc, _ = potentials(MAPS['d_scan_of_Dprime'], d, {}, [5, 6, 7], L - 1)
assert gsum > psi, (gsum, psi)
violations['d_scan_of_Dprime'] += 1
checks += 1
assert all(violations[n] == 0 for n in ('a_raw_scan', 'b_swap_after_scan', 'c_scan_of_blockA'))
assert violations['d_scan_of_Dprime'] >= 1
print('Part 1 PASS: excess inequality; E=0 and sum gamma<=Psi for (a)-(c);',
      'tail-coded violations found:', violations['d_scan_of_Dprime'])

# Part 2: monotonicity of f_t along branches
for name, G in MAPS.items():
    for trial in range(4):
        sigma = {1: trial % 2}
        K0 = [3, 5, 7]
        prev = None
        for m in range(1, L):
            _, _, _, f_of = potentials(G, savings_martingale(trial), sigma, K0, m)
            if prev is not None:
                for w, fv in f_of.items():
                    assert fv <= prev[w[:-1]], (name, m)
                    checks += 1
            prev = f_of
print('Part 2 PASS: split counts non-increasing along output branches')

# Part 3: graded frame J localizes D'^j tail differences
N = 40


def J(z):
    out = []
    for i in range(len(z)):
        f = isqrt(i)
        out.append(sum(comb(f, l) % 2 * z[i - l] for l in range(0, min(f, i) + 1)) % 2)
    return out


def Dprime_inv_power(v, j):
    z = list(v)
    for _ in range(j):
        acc, w = 0, []
        for b in z:
            acc ^= b; w.append(acc)
        z = w
    return z


for j in (1, 2):
    for q in range(0, 12):
        v = [random.randint(0, 1) for _ in range(N)]
        v2 = list(v); v2[q] ^= 1
        z, z2 = Dprime_inv_power(v, j), Dprime_inv_power(v2, j)
        raw_diff = [i for i in range(N) if z[i] != z2[i]]
        Jd = [i for i in range(N) if J(z)[i] != J(z2)[i]]
        assert raw_diff and raw_diff[-1] >= N - 2  # raw difference reaches the tail
        assert Jd and max(Jd) <= q + 2 * j + 6 * (j + 1) ** 2, (j, q, Jd)
        checks += 2
print('Part 3 PASS: raw tail differences become finitely supported in the graded frame')

print('checks:', checks)
print('ALL P4-S087 AUDITS PASS')
