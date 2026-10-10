#!/usr/bin/env python3
"""P4-S089 finite audit: halving potentials, the two-frame structure, level
decomposition, no-local-frustration, and (optionally) the numerical record.

Parts 1-5 are exact (integers / Fractions) on finite truncations.
Part 6 reproduces the smaller instances of the Section 4 EXPERIMENT record and
needs numpy and scipy; it is skipped if they are unavailable.
Finite checks only: every infinitary claim rests on the written proofs in
phase4/P4-S089_MATHEMATICS.md.
"""
import random, sys
from fractions import Fraction as Fr
from itertools import product

random.seed(89)
CHECKS = 0
def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

# ---------------------------------------------------------------- Part 1
# Lemma 1.2 (i)-(iv) for a 2-to-1 fair map G = (permutation, then delete last bit).
def part1(trials=40, n=7):
    N = 1 << n
    for _ in range(trials):
        perm = list(range(N)); random.shuffle(perm)
        T = n - 1                                   # output length
        def G(x, t):                                # first t output bits as int
            return perm[x] >> (n - t)
        # random rational martingale on outputs up to length T
        d = {(0, 0): Fr(1)}
        for t in range(T):
            for w in range(1 << t):
                th = Fr(random.randint(-4, 4), 4)
                d[(t + 1, 2 * w)] = d[(t, w)] * (1 + th)
                d[(t + 1, 2 * w + 1)] = d[(t, w)] * (1 - th)
        P = set(x for x in range(N) if random.random() < 0.6) or {0}
        C = set(x for x in range(N) if random.random() < 0.5)
        lamP = Fr(len(P), N)
        def cells(t):
            cl = {}
            for x in range(N):
                cl.setdefault(G(x, t), []).append(x)
            return cl
        def Psi(Q, t, cl):
            lq = Fr(len(Q), N)
            return sum(Fr(1, 1 << t) * d[(t, w)] for w, xs in cl.items()
                       if any(x in Q for x in xs)) / lq
        def gam(Q, Cs, t, cl):
            lq = Fr(len(Q), N)
            tot = Fr(0)
            for w, xs in cl.items():
                inQ = [x for x in xs if x in Q]
                if any(x in Cs for x in inQ) and any(x not in Cs for x in inQ):
                    tot += Fr(1, 1 << t) * d[(t, w)]
            return tot / lq
        prevPsi = prevGam = None
        for t in range(T + 1):
            cl = cells(t)
            ps, ga = Psi(P, t, cl), gam(P, C, t, cl)
            if prevPsi is not None:
                ok(ps <= prevPsi and ga <= prevGam, "Lemma 1.2(i) monotonicity")
            prevPsi, prevGam = ps, ga
            # (ii) domination
            dom = sum(d[(t, G(x, t))] for x in P) / N / lamP
            ok(dom <= ps, "Lemma 1.2(ii) domination")
            # (iii) weighted refinement identity
            P0 = P & C; P1 = P - C
            if P0 and P1:
                al = Fr(len(P0), len(P))
                lhs = al * Psi(P0, t, cl) + (1 - al) * Psi(P1, t, cl)
                ok(lhs == ps + ga, "Lemma 1.2(iii) identity")
        # (iv) at full output precision the cell is the fibre pair
        cl = cells(T)
        for w, xs in cl.items():
            ok(len(xs) == 2, "fibres of size two")
            both = xs[0] in P and xs[1] in P
            sep = both and ((xs[0] in C) != (xs[1] in C))
            inQ = [x for x in xs if x in P]
            s_def = any(x in C for x in inQ) and any(x not in C for x in inQ)
            ok(sep == s_def, "Lemma 1.2(iv) limit identification")
        # fairness of G at every output length
        for t in range(T + 1):
            cnt = {}
            for x in range(N):
                cnt[G(x, t)] = cnt.get(G(x, t), 0) + 1
            ok(all(c == N >> t for c in cnt.values()) and len(cnt) == 1 << t, "fairness")

# ---------------------------------------------------------------- Part 2
# Proposition 2: K_mix / K'_mix structure.  Raw x as list of bits, length 2n.
def kmix(x, n):
    a = x[0::2]; b = x[1::2]; y = list(x)
    for j in range(n):
        bm1 = b[j-1] if j >= 1 else 0; bm2 = b[j-2] if j >= 2 else 0
        y[2*j+1] = b[j] ^ bm2 ^ ((1 ^ a[j]) & bm1)
    return y
def kmix_inv(y, n):
    a = y[0::2]; b = []; x = list(y)
    for j in range(n):
        bm1 = b[j-1] if j >= 1 else 0; bm2 = b[j-2] if j >= 2 else 0
        bj = y[2*j+1] ^ bm2 ^ ((1 ^ a[j]) & bm1); b.append(bj); x[2*j+1] = bj
    return x
def kp(x, n):
    y = list(x); bt = x[0::2]
    for j in range(n):
        c = x[2*j-1] if j >= 1 else 0
        bm1 = bt[j-1] if j >= 1 else 0; bm2 = bt[j-2] if j >= 2 else 0
        y[2*j] = bt[j] ^ bm2 ^ ((1 ^ c) & bm1)
    return y
def kp_inv(y, n):
    x = list(y); bt = []
    for j in range(n):
        c = y[2*j-1] if j >= 1 else 0
        bm1 = bt[j-1] if j >= 1 else 0; bm2 = bt[j-2] if j >= 2 else 0
        v = y[2*j] ^ bm2 ^ ((1 ^ c) & bm1); bt.append(v); x[2*j] = v
    return x
def flipK(x, n, F):
    y = kmix(x, n)
    for f in F: y[f] ^= 1
    return kmix_inv(y, n)
def flipKp(x, n, F):
    y = kp(x, n)
    for f in F: y[f] ^= 1
    return kp_inv(y, n)
def bits(i, L): return [(i >> k) & 1 for k in range(L)]

def part2(n=7, J=3):
    L = 2 * n; R = n - J
    for i in range(1 << L):
        x = bits(i, L); a = x[0::2]; b = x[1::2]
        ok(kmix_inv(kmix(x, n), n) == x and kp_inv(kp(x, n), n) == x, "inverses")
        # (a) psi_0, psi_1 translate data by delta^0, delta^1 in S(a)
        d0 = [1, 1 ^ a[1]] if n > 1 else [1]
        d1 = [0, 1]
        for j in range(2, n):
            d0.append(d0[j-2] ^ ((1 ^ a[j]) & d0[j-1]))
            d1.append(d1[j-2] ^ ((1 ^ a[j]) & d1[j-1]))
        p0 = flipK(x, n, [1]); p1 = flipK(x, n, [3])
        ok(p0[0::2] == a and [u ^ v for u, v in zip(p0[1::2], b)] == d0, "psi_0 = translation by delta^0")
        ok(p1[0::2] == a and [u ^ v for u, v in zip(p1[1::2], b)] == d1, "psi_1 = translation by delta^1")
        ok(flipK(p0, n, [3]) == flipK(p1, n, [1]), "psi_0 and psi_1 commute")
        # (b) random K-flip sets below 2J act on the window by S_W(a)
        F = random.sample(range(2 * J), random.randint(1, 2 * J))
        z = flipK(x, n, F)
        ok(all(z[2*j] == x[2*j] for j in range(J, n)), "window controls unchanged (K)")
        e = [z[2*j+1] ^ x[2*j+1] for j in range(n)]
        ok(all(e[j] == e[j-2] ^ ((1 ^ a[j]) & e[j-1]) for j in range(J + 1, n)), "window data change in S_W(a)")
        # (c) random K'-flip sets below 2J act on the window by S'_W(b)
        Fp = random.sample(range(2 * J), random.randint(1, 2 * J))
        zp = flipKp(x, n, Fp)
        ok(all(zp[2*j+1] == x[2*j+1] for j in range(J, n)), "window odd coordinates unchanged (K')")
        ep = [zp[2*j] ^ x[2*j] for j in range(n)]
        ok(all(ep[j] == ep[j-2] ^ ((1 ^ x[2*j-1]) & ep[j-1]) for j in range(J + 1, n)), "window even change in S'_W(b)")
    # T_W is a group of order four: tau_s tau_s' = tau_{s xor s'}
    for aw in product([0, 1], repeat=R):
        def sol(s):
            d2, d1 = s; out = []
            for j in range(R):
                dj = d2 ^ ((1 ^ aw[j]) & d1); out.append(dj); d2, d1 = d1, dj
            return out
        for s in product([0, 1], repeat=2):
            for t in product([0, 1], repeat=2):
                st = (s[0] ^ t[0], s[1] ^ t[1])
                ok([u ^ v for u, v in zip(sol(s), sol(t))] == sol(st), "T_W linear in the state")
        ok(len({tuple(sol(s)) for s in product([0, 1], repeat=2)}) == 4, "S_W(a) has four elements")

# ---------------------------------------------------------------- Part 3
# Lemma 3.1 (signed level action), self-adjointness, Lemma 3.2 identity.
CORE3 = [('K', [1]), ('K', [3]), ('P', [0])]
def gen_action(spec, n_pairs):
    kind, F = spec
    L = 2 * n_pairs
    act = []
    for i in range(1 << L):
        x = bits(i, L)
        y = flipK(x, n_pairs, F) if kind == 'K' else flipKp(x, n_pairs, F)
        act.append(sum(v << k for k, v in enumerate(y)))
    return act
def part3(n_pairs=5):
    L = 2 * n_pairs
    acts = [gen_action(g, n_pairs) for g in CORE3]
    for act in acts:
        ok(all(act[act[i]] == i for i in range(1 << L)), "involution")
    for n in range(1, L):
        mask = (1 << n) - 1
        for act in acts:
            # causality: action on level n well defined, and section bit
            lev = {}; sec = {}
            for i in range(1 << L):
                v = i & mask; img = act[i]
                lev.setdefault(v, set()).add(img & mask)
                sec.setdefault(v, set()).add(((img >> n) & 1) ^ ((i >> n) & 1))
            ok(all(len(s) == 1 for s in lev.values()) and all(len(s) == 1 for s in sec.values()), "causal")
            psi = {v: next(iter(s)) for v, s in lev.items()}
            c = {v: next(iter(s)) for v, s in sec.items()}
            ok(all(c[psi[v]] == c[v] for v in psi), "section symmetric => M_n self-adjoint")
            # Lemma 3.1: U_psi f = signed action, f(x) = h(x|n)(-1)^{x_n}
            h = {v: random.randint(-3, 3) for v in range(1 << n)}
            for i in range(1 << (n + 1)):
                v = i & mask; xn = (i >> n) & 1
                img = act[i]                       # high bits beyond n+1 irrelevant
                fimg = h[img & mask] * (-1) ** ((img >> n) & 1)
                ok(fimg == (-1) ** c[v] * h[psi[v]] * (-1) ** xn, "Lemma 3.1 signed action")
        # Lemma 3.2: separation identity for a random clopen C at level n+1
        C = set(u for u in range(1 << (n + 1)) if random.random() < 0.5)
        m1 = (1 << (n + 1)) - 1
        for act in acts:
            f = lambda u: 1 if u in C else -1
            sep = sum(1 for i in range(1 << L) if ((i & m1) in C) != ((act[i] & m1) in C))
            inner = sum(f(i & m1) * f(act[i] & m1) for i in range(1 << L))
            ok(Fr(sep, 1 << L) == Fr(1, 2) * (1 - Fr(inner, 1 << L)), "Lemma 3.2 identity")

# ---------------------------------------------------------------- Part 4
# Theorem 3(ii) algebra: <f,Mf> = m1^2 lam(P) + <g,Mg> for P invariant (exact, small).
def part4(n_pairs=5):
    L = 2 * n_pairs; N = 1 << L
    acts = [gen_action(g, n_pairs) for g in CORE3]
    a = 2; mask = (1 << a) - 1
    # orbits of the level-a action
    lev = [{i & mask: acts[k][i] & mask for i in range(N)} for k in range(3)]
    seen = set(); orbits = []
    for u in range(1 << a):
        if u in seen: continue
        orb = {u}; frontier = [u]
        while frontier:
            v = frontier.pop()
            for lv in lev:
                w = lv[v]
                if w not in orb: orb.add(w); frontier.append(w)
        seen |= orb; orbits.append(orb)
    for orb in orbits:
        P = [i for i in range(N) if (i & mask) in orb]
        Pset = set(P)
        for k in range(3):
            ok(all(acts[k][i] in Pset for i in P), "orbit state is invariant")
        for _ in range(40):
            Cset = set(i for i in P if random.random() < 0.5)
            alpha = Fr(len(Cset), len(P))
            if not (Fr(1, 4) <= alpha <= Fr(3, 4)): continue
            f = {i: (1 if i in Cset else -1) for i in P}
            m1 = 2 * alpha - 1
            g = {i: f[i] - m1 for i in P}
            def form(u):
                return sum(Fr(u[i]) * sum(u[acts[k][i]] for k in range(3)) for i in P) / 3
            ok(form(f) == m1 * m1 * len(P) + form(g), "<f,Mf> splits off the mean")
            sepavg = Fr(sum(sum(1 for i in P if (i in Cset) != (acts[k][i] in Cset)) for k in range(3)), 3)
            ok(sepavg == Fr(1, 2) * (len(P) - form(f)), "averaged separation identity on P")

# ---------------------------------------------------------------- Part 5
# Lemma 4: no local frustration, for random causal automorphisms and for core words.
def random_portrait(depth):
    return {n: [random.randint(0, 1) for _ in range(1 << n)] for n in range(depth)}
def apply_portrait(port, v, n):           # image of a level-n vertex (int, bit k = coord k)
    out = 0
    for k in range(n):
        bit = ((v >> k) & 1) ^ port[k][v & ((1 << k) - 1)]
        out |= bit << k
    return out
def part5(depth=10, k=6):
    W = [random_portrait(depth) for _ in range(k)]
    total = Fr(0)
    for port in W:
        m = Fr(1); s = Fr(0)
        for n in range(depth):
            fix = [v for v in range(1 << n) if apply_portrait(port, v, n) == v]
            ok(Fr(len(fix), 1 << n) == m, "m_n recursion")
            Fn = [v for v in fix if port[n][v] == 1]
            s += Fr(len(Fn), 1 << n); m -= Fr(len(Fn), 1 << n)
        ok(s <= 1, "per-automorphism sum <= 1")
        total += s
    ok(total <= len(W), "Lemma 4")
    # frustrated short cycles of the three-core: fraction at level n is summable
    n_pairs = 5; L = 2 * n_pairs
    acts = [gen_action(g, n_pairs) for g in CORE3]
    words = [[]]
    for _ in range(4):
        words = words + [w + [g] for w in words for g in range(3) if not w or w[-1] != g]
    words = [w for w in words if w]
    acc = Fr(0)
    for n in range(L - 1):
        m1 = (1 << (n + 1)) - 1; frus = set()
        for w in words:
            for v in range(1 << n):
                u = v
                for g in w: u = acts[g][u] & m1
                if u == v | (1 << n): frus.add(v)
        acc += Fr(len(frus), 1 << n)
    ok(acc <= len(words), "Lemma 4 for core words of length <= 4")

# ---------------------------------------------------------------- Part 6
def part6():
    try:
        import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
    except Exception:
        print("Part 6 skipped (numpy/scipy unavailable)"); return
    def level_top(n, spec):
        n_pairs = (n + 2) // 2; L = 2 * n_pairs; mask1 = (1 << (n + 1)) - 1
        V = 1 << n; rows = []; cols = []; vals = []
        for g in spec:
            act = gen_action(g, n_pairs)
            red = {}
            for i in range(1 << L): red[i & mask1] = act[i] & mask1
            for v in range(V):
                img = red[v]
                rows.append(v); cols.append(img & (V - 1)); vals.append(-1.0 if (img >> n) & 1 else 1.0)
        M = sp.csr_matrix((vals, (rows, cols)), shape=(V, V)) / len(spec)
        return max(sla.eigsh(M, k=1, which='LA', return_eigenvectors=False))
    rec3 = {7: 0.94381, 8: 0.96347, 9: 0.96376, 10: 0.97015, 11: 0.98049, 12: 0.97516}
    for n, val in rec3.items():
        ok(abs(level_top(n, CORE3) - val) < 1e-4, f"E3 level {n}")
    rec2 = {5: 0.92388, 6: 1.0, 8: 0.98079, 11: 0.99518}
    for n, val in rec2.items():
        ok(abs(level_top(n, [('K', [1]), ('P', [0])]) - val) < 1e-4, f"E4 level {n}")
    print("Part 6 (numerical record, levels <= 12) reproduced")

if __name__ == "__main__":
    part1(); print("Part 1 (Lemma 1.2) PASS", CHECKS)
    part2(); print("Part 2 (Proposition 2) PASS", CHECKS)
    part3(); print("Part 3 (Lemmas 3.1-3.2) PASS", CHECKS)
    part4(); print("Part 4 (Theorem 3 algebra) PASS", CHECKS)
    part5(); print("Part 5 (Lemma 4) PASS", CHECKS)
    if "--no-numeric" not in sys.argv:
        part6()
    print(f"ALL P4-S089 AUDITS PASS ({CHECKS} checks)")
