#!/usr/bin/env python3
"""P4-S088 finite audit (exact arithmetic, truncations only).

Part 1  G_asym: explicit computable fair <=2-to-1 map with an asymmetric
        (1/4, 3/4) positive-measure double locus, truncated to three blocks.
Part 2  translation pairs G_c and Gaussian-elimination frames (Theorem B).
Part 3  the entropy inequality used in Theorem B(i), on random causal maps.
Part 4  coset dispersal: annihilating group functionals (Lemma C3).
Part 5  affine-constraint potentials: refinement identity, monotonicity,
        domination (Lemma C1).

Every infinitary claim rests on the written proofs in P4-S088_MATHEMATICS.md.
"""
import itertools
import math
import random
from fractions import Fraction as Fr

random.seed(88)
CHECKS = 0


def check(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)


# ---------------------------------------------------------------- Part 1
def ell(j):
    return j + 2


def a_(j):
    return sum(ell(i) for i in range(j))


JMAX = 3                      # blocks 0,1,2 ; a_3 = 9
A3 = a_(JMAX)
LIN = A3 + 2                  # input precision 11


def allowed_blocks(j):
    return [format(b, "0%db" % ell(j)) for b in range(2 ** ell(j) - 1)]


def forbidden(j):
    return "1" * ell(j)


def split_container(B, S, j):
    """Split container (B,S) at block j into N children (slot, unit).
    Returns dict value -> (slot, unit, kind) with kind in {'B','S','X'}."""
    N = 2 ** ell(j)
    Lu = a_(j + 1) + 2
    Bslots = [B + format(i, "0%db" % (Lu - 1 - len(B))) for i in range(N)]
    Sslots = [S + format(i, "0%db" % (Lu - 1 - len(S))) for i in range(N // 2)]
    children = []
    if N % 3 == 1:
        t, s = (2 * N - 2) // 3, (N - 1) // 3
    else:
        t, s = (2 * N - 1) // 3, (N - 2) // 3

    def pack(slots, cnt, kind):
        whole = slots[:cnt]
        rest = slots[cnt:]
        units = []
        k = 0
        while len(units) < cnt:
            units += [rest[k] + "0", rest[k] + "1"]
            k += 1
        used_units = units[:cnt]
        left_units = units[cnt:]
        left_slots = rest[k:]
        out = [(whole[i], used_units[i], kind) for i in range(cnt)]
        return out, left_slots, left_units

    cb, lsB, luB = pack(Bslots, t, "B")
    cs, lsS, luS = pack(Sslots, s, "S")
    children = cb + cs
    if N % 3 == 1:
        check(len(lsB) == 1 and not luB and not lsS and len(luS) == 1,
              "leftover shape N=1 mod 3")
        strad = (lsB[0], luS[0], "X")
    else:
        check(not lsB and len(luB) == 1 and len(lsS) == 1 and not luS,
              "leftover shape N=2 mod 3")
        strad = (lsS[0], luB[0], "X")
    vals = allowed_blocks(j)
    check(len(children) == len(vals), "child count")
    res = {v: children[i] for i, v in enumerate(vals)}
    res[forbidden(j)] = strad
    return res


def cyl_contains(p, q):
    return q.startswith(p)


def build_containers():
    cont = {"": ("1", "01")}
    strad = {}
    level = [""]
    for j in range(JMAX):
        nxt = []
        for w in level:
            B, S = cont[w]
            ch = split_container(B, S, j)
            pieces = []
            for v, (sl, un, kind) in ch.items():
                check(len(sl) == a_(j + 1) + 1 and len(un) == a_(j + 1) + 2,
                      "slot/unit lengths")
                check(cyl_contains(B, sl) or cyl_contains(S, sl), "slot in parent")
                check(cyl_contains(B, un) or cyl_contains(S, un), "unit in parent")
                pieces += [sl, un]
                if kind == "X":
                    strad[w + v] = (sl, un)
                else:
                    par = B if kind == "B" else S
                    check(cyl_contains(par, sl) and cyl_contains(par, un),
                          "collapsing child inside one parent cylinder")
                    lcp = len(os_commonprefix(sl, un))
                    check(lcp >= a_(j) + 1, "collapse lcp")
                    cont[w + v] = (sl, un)
                    nxt.append(w + v)
            for x, y in itertools.combinations(pieces, 2):
                check(not (cyl_contains(x, y) or cyl_contains(y, x)),
                      "children pieces disjoint")
            tot = sum(Fr(1, 2 ** len(p)) for p in pieces)
            check(tot == Fr(1, 2 ** len(B)) + Fr(1, 2 ** len(S)), "children fill parent")
        level = nxt
    return cont, strad, level


def os_commonprefix(x, y):
    k = 0
    while k < min(len(x), len(y)) and x[k] == y[k]:
        k += 1
    return x[:k]


def in_A_prefix(z):
    """True iff every complete block of z is allowed; returns (ok, v) where v
    is the first forbidden block prefix if any."""
    for j in range(JMAX):
        lo, hi = a_(j), a_(j + 1)
        if len(z) < hi:
            return True, None
        if z[lo:hi] == forbidden(j):
            return False, z[:hi]
    return True, None


def G_asym_prefix(x, cont, strad):
    if x.startswith("00"):
        z = x[2:]
        ok, v = in_A_prefix(z)
        if ok:
            return z, 0
        return v + "00" + z[len(v):], 0
    w = ""
    for j in range(JMAX):
        B, S = cont[w]
        found = None
        for v in allowed_blocks(j) + [forbidden(j)]:
            key = w + v
            if key in strad:
                sl, un = strad[key]
                if x.startswith(sl):
                    return key + "1" + x[len(sl):], 1
                if x.startswith(un):
                    return key + "01" + x[len(un):], 1
            else:
                sl, un = cont[key]
                if x.startswith(sl) or x.startswith(un):
                    found = key
                    break
        check(found is not None, "side-1 input lies in some child")
        w = found
    return w, 1


def part1():
    cont, strad, level = build_containers()
    check(len(level) == 3 * 7 * 15, "number of A-prefixes at a_3")
    counts = {}
    side0 = {}
    for xi in range(2 ** LIN):
        x = format(xi, "0%db" % LIN)
        y, side = G_asym_prefix(x, cont, strad)
        check(len(y) >= A3, "output determined to a_3")
        w = y[:A3]
        counts[w] = counts.get(w, 0) + 1
        if side == 0:
            side0[w] = side0.get(w, 0) + 1
    check(len(counts) == 2 ** A3, "every output prefix hit")
    for w, c in counts.items():
        check(c == 2 ** (LIN - A3), "fairness at precision a_3")
    for w in level:
        check(side0.get(w, 0) == 1 and counts[w] == 4, "weights 1/4, 3/4 on A-prefixes")
    for L in range(A3):
        agg = {}
        for w, c in counts.items():
            agg[w[:L]] = agg.get(w[:L], 0) + c
        for w, c in agg.items():
            check(c == 2 ** (LIN - L), "fairness at shorter precision")
    lamA = Fr(1)
    for j in range(JMAX):
        lamA *= 1 - Fr(1, 2 ** ell(j))
    check(Fr(len(level), 2 ** A3) == lamA, "lambda(A_3) product formula")
    prod = 1.0
    for k in range(2, 80):
        prod *= 1 - 2.0 ** (-k)
    check(abs(prod - 0.5775761901732) < 1e-9, "lambda(A) numerical value")
    print("Part 1 G_asym: containers, fairness, weights 1/4-3/4 ok;",
          "lambda(A) ~ %.10f" % prod)


# ---------------------------------------------------------------- Part 2
def part2():
    n = 24
    for _ in range(200):
        c = [1] + [random.randint(0, 1) for _ in range(n - 1)]

        def K(x):
            return [x[i] ^ (x[0] & (c[i] ^ (1 if i == 0 else 0))) for i in range(n)]

        x = [random.randint(0, 1) for _ in range(n)]
        check(K(K(x)) == x, "K_c involution")
        out = K(x)[1:]
        x2 = [xi ^ ci for xi, ci in zip(x, c)]
        check(K(x2)[1:] == out, "G_c fibre {x, x+c}")
        check(K(x)[0] == x[0], "K_c causal at 0")
    for _ in range(150):
        r = random.randint(1, 5)
        vecs = [[random.randint(0, 1) for _ in range(n)] for _ in range(r)]
        basis = []
        for v in vecs:
            v = v[:]
            for b, p in basis:
                if v[p]:
                    v = [a ^ bb for a, bb in zip(v, b)]
            if any(v):
                p = v.index(1)
                for k in range(len(basis)):
                    bb, pp = basis[k]
                    if bb[p]:
                        basis[k] = ([a ^ q for a, q in zip(bb, v)], pp)
                basis.append((v, p))
        basis.sort(key=lambda t: t[1])
        for b, p in basis:
            for b2, p2 in basis:
                if p2 != p:
                    check(b[p2] == 0, "reduced echelon")

        def T(x, b, p):
            return [x[i] ^ (x[p] & (b[i] ^ (1 if i == p else 0))) for i in range(n)]

        def J(x):
            for b, p in basis:
                x = T(x, b, p)
            return x

        pivots = {p for _, p in basis}
        for b, p in basis:
            check(J(b) == [1 if i == p else 0 for i in range(n)], "J b_j = e_pj")
        for v in vecs:
            jv = J(v)
            check(all(jv[i] == 0 for i in range(n) if i not in pivots),
                  "J maps span into pivot coordinates")
        x = [random.randint(0, 1) for _ in range(n)]
        for b, p in basis:
            check(T(T(x, b, p), b, p) == x, "transvection involution")
            tx = T(x, b, p)
            check(all(tx[i] == x[i] for i in range(p + 1)), "transvection causal")
    print("Part 2 translation pairs and elimination frames ok")


# ---------------------------------------------------------------- Part 3
def hinv(t):
    lo, hi = 0.0, 0.5
    for _ in range(60):
        mid = (lo + hi) / 2
        h = 0.0 if mid == 0 else -mid * math.log2(mid) - (1 - mid) * math.log2(1 - mid)
        if h < t:
            lo = mid
        else:
            hi = mid
    return lo


def part3():
    for p in [i / 20 for i in range(21)]:
        for q in [i / 20 for i in range(21)]:
            check(p * (1 - q) + (1 - p) * q >= min(p, 1 - p) - 1e-12, "affine min bound")
    ts = [i / 50 for i in range(51)]
    hs = [hinv(t) for t in ts]
    for i in range(1, 50):
        check(hs[i - 1] + hs[i + 1] >= 2 * hs[i] - 1e-9, "h^{-1} convex")
    n = 8
    for trial in range(12):
        tables = [{} for _ in range(n)]

        def f(i, pre):
            key = tuple(pre)
            if key not in tables[i]:
                tables[i][key] = random.randint(0, 1)
            return tables[i][key]

        def J(x):
            return [x[i] ^ f(i, x[:i]) for i in range(n)]

        Jt = {}
        for xi in range(2 ** n):
            x = [(xi >> (n - 1 - i)) & 1 for i in range(n)]
            Jt[xi] = J(x)
        check(len({tuple(v) for v in Jt.values()}) == 2 ** n, "causal map bijective")
        for k in (1, 2, 3):
            rho = [1] + [random.randint(0, 1) for _ in range(k - 1)]
            tot = 0
            for ri in range(2 ** (n - k)):
                r = [(ri >> (n - k - 1 - i)) & 1 for i in range(n - k)]
                c = rho + r
                cint = int("".join(map(str, c)), 2)
                for xi in range(2 ** n):
                    a, b = Jt[xi], Jt[xi ^ cint]
                    tot += sum(1 for i in range(n) if a[i] != b[i])
            avg = tot / (2 ** (n - k) * 2 ** n * n)
            check(avg >= hinv(1 - k / n) - 1e-9, "entropy lower bound on E D_n")
    print("Part 3 entropy inequality ok")


# ---------------------------------------------------------------- Part 4
def part4():
    W = 60
    for _ in range(100):
        m = random.randint(1, 5)
        Q = [[random.randint(0, 1) for _ in range(W)] for _ in range(m)]
        groups = [list(range(g, g + m + 1)) for g in range(0, W - m, m + 1)]
        funcs = []
        for g in groups:
            found = None
            for size in range(1, m + 2):
                for S in itertools.combinations(g, size):
                    if all(sum(v[j] for j in S) % 2 == 0 for v in Q):
                        found = S
                        break
                if found:
                    break
            check(found is not None, "dependent subset exists in m+1 coordinates")
            funcs.append(set(found))
        for _ in range(20):
            v = random.choice(Q)
            s = [0] * W
            for j in random.sample(range(W), 3):
                s[j] = 1
            d = [a ^ b for a, b in zip(v, s)]
            for F in funcs:
                check(sum(d[j] for j in F) % 2 == sum(s[j] for j in F) % 2,
                      "functional sees only the density-zero part")
                check(sum(v[j] for j in F) % 2 == 0, "functional annihilates Q")
    print("Part 4 coset dispersal functionals ok")


# ---------------------------------------------------------------- Part 5
def part5():
    n = 7
    for trial in range(25):
        perm = list(range(2 ** n))
        random.shuffle(perm)

        def Gp(xi, t):
            return perm[xi] >> (n - t)

        dvals = {}

        def d(w, t):
            if t == 0:
                return Fr(1)
            key = (w, t)
            if key not in dvals:
                par = d(w >> 1, t - 1)
                st = Fr(random.randint(-4, 4), 4)
                bit = w & 1
                dvals[key] = par * (1 + st) if bit else par * (1 - st)
                dvals[(w ^ 1, t)] = par * (1 - st) if bit else par * (1 + st)
            return dvals[key]

        ncons = random.randint(0, 2)
        cons = []
        while len(cons) < ncons:
            c = random.randint(1, 2 ** n - 1)
            cons.append((c, random.randint(0, 1)))

        def inP(xi, cs):
            return all(bin(xi & c).count("1") % 2 == b for c, b in cs)

        def rank(cs):
            rows = [c for c, _ in cs]
            r = 0
            for bit in reversed(range(n)):
                piv = None
                for i in range(r, len(rows)):
                    if rows[i] >> bit & 1:
                        piv = i
                        break
                if piv is None:
                    continue
                rows[r], rows[piv] = rows[piv], rows[r]
                for i in range(len(rows)):
                    if i != r and rows[i] >> bit & 1:
                        rows[i] ^= rows[r]
                r += 1
            return r

        if rank(cons) < len(cons):
            continue
        Pset = [xi for xi in range(2 ** n) if inP(xi, cons)]
        if not Pset:
            continue
        lamP = Fr(len(Pset), 2 ** n)
        check(lamP == Fr(1, 2 ** len(cons)), "independent constraints are fair")

        def Psi(cs, t):
            pts = [xi for xi in range(2 ** n) if inP(xi, cs)]
            lam = Fr(len(pts), 2 ** n)
            ws = {Gp(xi, t) for xi in pts}
            return sum(Fr(1, 2 ** t) * d(w, t) for w in ws) / lam

        newc = random.randint(1, 2 ** n - 1)
        if rank(cons + [(newc, 0)]) < len(cons) + 1:
            continue
        for t in range(1, n + 1):
            P0 = cons + [(newc, 0)]
            P1 = cons + [(newc, 1)]
            check(Fr(len([x for x in range(2 ** n) if inP(x, P0)]), 2 ** n) == lamP / 2,
                  "fresh functional halves P")
            gam = Fr(0)
            for w in range(2 ** t):
                cell = [xi for xi in Pset if Gp(xi, t) == w]
                vals = {bin(xi & newc).count("1") % 2 for xi in cell}
                if len(vals) == 2:
                    gam += Fr(1, 2 ** t) * d(w, t)
            gam /= lamP
            check((Psi(P0, t) + Psi(P1, t)) / 2 == Psi(cons, t) + gam,
                  "affine refinement identity")
            if t < n:
                check(Psi(cons, t + 1) <= Psi(cons, t), "monotone in t")
            dom = sum(Fr(1, 2 ** n) * d(Gp(xi, t), t) for xi in Pset) / lamP
            check(dom <= Psi(cons, t), "domination")
    print("Part 5 affine potentials ok")


if __name__ == "__main__":
    part1()
    part2()
    part3()
    part4()
    part5()
    print("total checks:", CHECKS)
    print("ALL P4-S088 AUDITS PASS")
