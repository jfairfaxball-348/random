#!/usr/bin/env python3
"""P4-S092 exact finite audit: orientation reader, partner logic, left-c.e. one-sidedness.

Finite checks only; they supplement, and cannot replace, the written proofs in
P4-S092_MATHEMATICS.md. Integer/Fraction arithmetic only. Deterministic seed.
"""
import itertools
import random
import sys
from fractions import Fraction

random.seed(92092)
CHECKS = 0


def check(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)


# ---------------------------------------------------------------- frames
def raw_to_virtual(frame, x):
    if frame == "raw":
        return list(x)
    if frame == "dprime":  # D'(z)_0 = z_0, D'(z)_i = z_i xor z_{i-1}
        return [x[0]] + [x[i] ^ x[i - 1] for i in range(1, len(x))]
    raise ValueError(frame)


def virtual_to_raw(frame, v):
    if frame == "raw":
        return list(v)
    if frame == "dprime":  # prefix parity
        out, acc = [], 0
        for b in v:
            acc ^= b
            out.append(acc)
        return out
    raise ValueError(frame)


# ---------------------------------------------------------------- reader
def run_reader(frame, v, family, nlev, steps):
    """Simulate T_{K,W,n,true} on virtual input v for `steps` queries.

    family(m, t) -> list of strings (tuples) in W_{m,t}.
    Returns list of events and the query order. Raw windows have length M
    (both frames here have l(M)=M).
    """
    h, M = 0, 1
    queried = []
    events = []
    for t in range(steps):
        if M >= len(v):
            break
        read = set(queried)
        # read set must be [0,M) minus {h}
        check(read == set(range(M)) - {h}, "read set is [0,M) minus hold")
        cands = []
        for b in (0, 1):
            u = [v[i] for i in range(M)]
            u[h] = b
            cands.append(tuple(virtual_to_raw(frame, u)))
        c = [False, False]
        for sigma in family(nlev(h), t):
            if len(sigma) > M:
                continue
            for b in (0, 1):
                if cands[b][: len(sigma)] == sigma and cands[1 - b][: len(sigma)] != sigma:
                    c[b] = True
        if c[0] != c[1]:
            b = 0 if c[0] else 1
            check(h not in read, "hold unread at resolution")
            queried.append(h)
            events.append(("resolve", h, b, v[h]))
            h, M = M, M + 1
        elif c[0] and c[1]:
            queried.append(h)
            events.append(("tie", h, None, v[h]))
            h, M = M, M + 1
        else:
            check(M not in read and M != h, "filler unread")
            queried.append(M)
            events.append(("fill", M, None, v[M]))
            M += 1
    check(len(queried) == len(set(queried)), "no repeated query")
    return events, queried


def part1_legality_and_fibres():
    """Legality on random inputs and exhaustive fibre bound on short prefixes."""
    for frame in ("raw", "dprime"):
        for trial in range(60):
            N = 18
            fam_list = []
            for _ in range(40):
                L = random.randint(1, 10)
                fam_list.append((random.randint(0, 25), random.randint(1, 6),
                                 tuple(random.randint(0, 1) for _ in range(L))))

            def family(m, t, fam_list=fam_list):
                return [s for (st, lev, s) in fam_list if st <= t and lev >= m]

            x = [random.randint(0, 1) for _ in range(N)]
            v = raw_to_virtual(frame, x)
            run_reader(frame, v, family, lambda h: min(6, h + 1), 16)
        # exhaustive fibre check: same family, all virtual inputs of length 9
        fam_list = [(0, 3, (0, 1, 1)), (2, 2, (1, 0)), (3, 4, (1, 1, 0, 1)), (1, 1, (0,)),
                    (4, 3, (0, 0, 1, 0)), (5, 2, (1, 1, 1))]

        def family(m, t):
            return [s for (st, lev, s) in fam_list if st <= t and lev >= m]

        outputs = {}
        n = 9
        for v in itertools.product((0, 1), repeat=n):
            v = list(v)
            events, queried = run_reader(frame, v, family, lambda h: min(4, h + 1), 7)
            out = tuple(v[q] for q in queried)
            key = (tuple(queried), out)
            outputs.setdefault(key, set()).add(tuple(v[: max(queried) + 2]))
        for key, pres in outputs.items():
            queried = key[0]
            top = max(queried) + 2
            # inputs agreeing on all queried coordinates below `top` with the
            # same transcript: they differ at most at unqueried coordinates
            # below top; the reader leaves at most one unqueried below its frontier.
            unq = [i for i in range(top) if i not in queried]
            check(len(unq) <= 2, "at most hold and one fresh coordinate unread below top")
            # count distinct completions on [0, max(queried)+1)
            frontier = max(queried) + 1
            comps = {p[:frontier] for p in pres}
            check(len(comps) <= 2, "<=2 compatible prefixes per output transcript (fibre bound)")


def part2_orientation_logic():
    """Theorem 1: with a z-pinned family the partner is never covered; injected
    partner cylinders create errors exactly in the race sense."""
    for frame in ("raw", "dprime"):
        for trial in range(120):
            N = 22
            x = [random.randint(0, 1) for _ in range(N)]
            v = raw_to_virtual(frame, x)
            inject = {}
            for h in range(N):
                if random.random() < 0.3:
                    inject[h] = random.randint(0, 6)  # stage of partner cylinder

            def family(m, t, x=x, v=v, inject=inject):
                out = []
                # z-pinned cylinders of every length >= m, available from stage m
                for L in range(m, N + 1):
                    if t >= L // 2:
                        out.append(tuple(x[:L]))
                for h, st in inject.items():
                    if t >= st and m == h + 1:
                        u = list(v)
                        u[h] ^= 1
                        p = virtual_to_raw(frame, u)
                        out.append(tuple(p[: h + 2]))
                return out

            events, queried = run_reader(frame, v, family, lambda h: h + 1, N - 2)
            for ev in events:
                kind, h, b, truth = ev
                if kind == "resolve" and h not in inject:
                    check(b == truth, "uninjected hold resolves correctly (O2)")
                if kind == "resolve" and b != truth:
                    check(h in inject, "every error is a separately covered partner")
                if kind == "tie":
                    check(h in inject, "every tie is a separately covered partner")


# ---------------------------------------------------------------- left-c.e.
def bits_of(fr, n):
    """First n bits of the terminating expansion of a dyadic Fraction in [0,1)."""
    out = []
    for _ in range(n):
        fr *= 2
        if fr >= 1:
            out.append(1)
            fr -= 1
        else:
            out.append(0)
    return out


def real_of(bits):
    return sum(Fraction(b, 2 ** (i + 1)) for i, b in enumerate(bits))


def part3_left_ce():
    """Lemmas 5.2, 5.3, 5a on random finite approximations below a random real."""
    for trial in range(400):
        N = 26
        zb = [random.randint(0, 1) for _ in range(N)]
        zb[-1] = 1  # finite truncation; a tail is appended implicitly below
        tail = Fraction(1, 2 ** (N + 2))  # makes r(z) non-dyadic at precision N+2
        rz = real_of(zb) + tail
        # random nondecreasing dyadic approximations strictly below rz
        approx, r = [], Fraction(0)
        while len(approx) < 70:
            gap = rz - r
            mode = random.random()
            if mode < 0.4:
                step = gap * Fraction(random.randint(1, 9), 10)
            elif mode < 0.7:
                step = gap * Fraction(random.randint(1, 4), 100)
            else:
                step = gap * Fraction(random.randint(90, 99), 100)
            r = r + step
            den = 2 ** (N + 6)
            r = Fraction(int(r * den), den)  # round down to a dyadic rational
            if r >= rz:
                r = rz - Fraction(1, den)
            approx.append(r)
        check(all(approx[i] <= approx[i + 1] for i in range(len(approx) - 1)), "nondecreasing")
        check(all(a < rz for a in approx), "approximations below r(z)")
        for g in (lambda k: k, lambda k: 2 * k + 1):
            K = 30

            def family(m, t, g=g):
                out = []
                for k in range(0, min(t, K) + 1):
                    if g(k) >= len(approx):
                        break
                    rb = bits_of(approx[g(k)], N)
                    for L in range(m, min(k, N) + 1):
                        out.append(tuple(rb[:L]))
                return out

            events, queried = run_reader("raw", zb, family, lambda h: h + 1, N - 3)
            for kind, h, b, truth in events:
                if kind == "resolve" and b == 1:
                    check(truth == 1, "Lemma 5.2: proposed 1 implies z_h = 1")
                if kind in ("resolve", "tie"):
                    jump = all(not (bits_of(approx[g(k)], h + 1) == zb[:h] + [0])
                               for k in range(h + 1, K + 1) if g(k) < len(approx))
                    if truth == 0:
                        check(kind == "resolve" and b == 0, "Lemma 5.3: 0-bit holds resolve to 0")
                    elif jump:
                        check(kind == "resolve" and b == 1, "Lemma 5.3: jump-over resolves to 1")
                    else:
                        check(kind == "tie" or b == 0, "Lemma 5.3: non-jump-over never proposes 1")
            # Lemma 5a betting rule never loses
            for h in range(N - 1):
                if g(h + 1) >= len(approx):
                    break
                rb = bits_of(approx[g(h + 1)], h + 1)
                if rb[:h] == zb[:h] and rb[h] == 1:
                    check(zb[h] == 1, "Lemma 5a: early agreement bet is correct")


def part4_lemma4_martingale():
    """Each summand 2^{|s|} lambda(S cap [s]) is an exact martingale (Lemma 4)."""
    for trial in range(200):
        L = random.randint(2, 7)
        S = {tuple(random.randint(0, 1) for _ in range(L)) for _ in range(random.randint(1, 6))}

        def mass(sigma):
            tot = Fraction(0)
            for c in S:
                k = min(len(c), len(sigma))
                if c[:k] == sigma[:k]:
                    tot += Fraction(1, 2 ** max(len(c), len(sigma)))
            return tot * 2 ** len(sigma)

        for n in range(0, L):
            for sigma in itertools.product((0, 1), repeat=n):
                s = tuple(sigma)
                check(mass(s + (0,)) + mass(s + (1,)) == 2 * mass(s), "measure martingale identity")


def part5_octave():
    """Skip ratio: tau/(tau+2^{-h-1}) < 1/2 for tau in (0, 2^{-h-1})."""
    for h in range(0, 12):
        for j in range(1, 64):
            tau = Fraction(j, 64 * 2 ** (h + 1))
            check(tau / (tau + Fraction(1, 2 ** (h + 1))) < Fraction(1, 2), "octave skip ratio")


if __name__ == "__main__":
    part1_legality_and_fibres()
    part2_orientation_logic()
    part3_left_ce()
    part4_lemma4_martingale()
    part5_octave()
    print(f"{CHECKS} exact checks")
    print("ALL P4-S092 AUDITS PASS")
