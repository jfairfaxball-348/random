#!/usr/bin/env python3
"""P4-S081 finite audit (exact rational arithmetic).

Checks the finite bookkeeping behind Theorem A (bounded-hole collapse),
Corollary A4 (window predictors) and Theorem B (even/odd factor split) on
truncations.  It does NOT verify statements about infinite transcripts,
computable randomness or OH membership; those rest on the written proofs in
phase4/P4-S081_MATHEMATICS.md.

Scan model: an h-hole "buffer scan".  Each step reads exactly one fresh
coordinate: either a postponed (buffered) coordinate, or the next new
coordinate after possibly postponing some new coordinates into a buffer of
size <= h.  Unread coordinates below the pointer p are exactly the buffer, and
p_t >= t/2, so the computable frontier n_t = floor(t/2) satisfies |U_t| <= h
(c(n) = 2n).  All decisions and stakes are deterministic functions of the
transcript (hash-seeded), as a scan requires.
"""
import hashlib
import random
from fractions import Fraction

STAKES = [Fraction(k, 4) for k in (-3, -2, -1, 0, 1, 2, 3)]


def h_int(*parts):
    s = repr(parts).encode()
    return int.from_bytes(hashlib.sha256(s).digest()[:8], "big")


class BufferScan:
    """Deterministic h-hole buffer scan; state is a function of the transcript."""

    def __init__(self, h, seed):
        self.h, self.seed = h, seed

    def run(self, oracle, steps):
        """Return list of (query, bit, stake) for `steps` steps."""
        transcript, reads, buf, p = [], [], [], 0
        out = []
        for t in range(steps):
            key = (self.seed, tuple(transcript))
            r = h_int(*key)
            if buf and r % 10 < 3:
                q = buf.pop(h_int(self.seed, "pick", tuple(transcript)) % len(buf))
            else:
                k = 0
                while len(buf) < self.h and h_int(self.seed, "post", tuple(transcript), k) % 10 < 3:
                    buf.append(p)
                    p += 1
                    k += 1
                q = p
                p += 1
            theta = STAKES[h_int(self.seed, "stake", tuple(transcript)) % len(STAKES)]
            b = oracle(q)
            out.append((q, b, theta))
            transcript.append(b)
            reads.append(q)
        assert len(set(reads)) == len(reads), "scan repeated a coordinate"
        return out


def frontier(t):
    return t // 2


def colour_run(h, seed, z, N):
    """Run T, compute U_t, entries, first-fit colours; return data and check invariants."""
    T = BufferScan(h, seed)
    run = T.run(lambda q: z[q], N)
    qs = [q for q, _, _ in run]
    read_time = {q: s for s, q in enumerate(qs)}
    colour, U_hist = {}, []
    active = set()
    for t in range(N + 1):
        nt = frontier(t)
        readset = set(qs[:t])
        U = {q for q in range(nt) if q not in readset}
        assert len(U) <= h, ("frontier invariant", t, U)
        for q in sorted(U - active):
            used = {colour[o] for o in U if o in colour and o != q}
            c = min(set(range(1, h + 1)) - used)
            colour[q] = c
        active = U
        U_hist.append(U)
    # same-colour held intervals disjoint
    iv = {}
    for q, c in colour.items():
        entry = next(t for t in range(N + 1) if q in U_hist[t])
        exit_ = read_time.get(q, N + 1)
        iv[q] = (entry, exit_, c)
    items = list(iv.items())
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            (a, (e1, x1, c1)), (b, (e2, x2, c2)) = items[i], items[j]
            if c1 == c2:
                assert x1 <= e2 or x2 <= e1, ("same colour overlap", a, b)
    assert all(1 <= c <= h for c in colour.values())
    return run, U_hist, colour


def pull_scan(h, run, U_hist, colour, z, which):
    """Simulate S_i (which=i) or F (which='F') up to T-time N.

    Only coordinates already read by this scan are consulted when simulating T.
    Returns (reads, capital_by_tau)."""
    N = len(run)
    known, reads, stakes_out = {}, [], []
    cap = Fraction(1)
    cap_by_tau = [cap]
    tau = 0

    def read(q, stake):
        nonlocal cap
        assert q not in known, ("repeat", which, q)
        b = z[q]
        known[q] = b
        reads.append(q)
        cap = cap * (1 + stake * (2 * b - 1))

    while tau < N:
        U = U_hist[tau]
        pulls = sorted(q for q in U if q not in known and (which == "F" or colour[q] != which))
        if pulls:
            read(pulls[0], Fraction(0))
            continue
        # all pulls for T-time tau done: unread below frontier is own-colour only
        nt = frontier(tau)
        unread = {x for x in range(nt) if x not in known}
        if which == "F":
            assert not unread, ("F left unread below frontier", tau, unread)
        else:
            assert all(colour.get(x) == which for x in unread) and len(unread) <= 1, (which, tau, unread)
        q, b, theta = run[tau]
        if q not in known:
            held = q in colour and any(q in U_hist[s] for s in range(tau + 1))
            if which == "F":
                assert not held, "F met an unpulled held coordinate"
                read(q, theta)
            else:
                assert (not held) or colour[q] == which, "S_i met other-colour held coord"
                read(q, theta if held else Fraction(0))
        tau += 1
        cap_by_tau.append(cap)
    return reads, cap_by_tau


def audit_theorem_A(trials=60, N=160):
    rng = random.Random(81)
    checks = 0
    for trial in range(trials):
        h = 1 + trial % 3
        z = [rng.randrange(2) for _ in range(4 * N + 10)]
        run, U_hist, colour = colour_run(h, 1000 + trial, z, N)
        dT = [Fraction(1)]
        for q, b, th in run:
            dT.append(dT[-1] * (1 + th * (2 * b - 1)))
        capF_reads, capF = pull_scan(h, run, U_hist, colour, z, "F")
        caps = []
        for i in range(1, h + 1):
            _, ci = pull_scan(h, run, U_hist, colour, z, i)
            caps.append(ci)
        for tau in range(N + 1):
            prod = capF[tau]
            for ci in caps:
                prod *= ci[tau]
            assert prod == dT[tau], ("factor identity", trial, tau)
            checks += 1
        # F modulus: q read by F within 2c(q+1)+h+1 outputs, c(n)=2n
        posF = {q: i for i, q in enumerate(capF_reads)}
        for q in range(N // 2 - 2):
            if 2 * (q + 1) <= N:
                assert q in posF and posF[q] <= 2 * (2 * (q + 1)) + h + 1, ("F modulus", q)
    print(f"Theorem A bookkeeping: PASS ({trials} scans, {checks} factor identities)")


def audit_window_A4(N=300):
    rng = random.Random(4)
    L = 6 * N
    z = [rng.randrange(2) for _ in range(L)]
    W = lambda k: [5 * k + 1, 5 * k + 2, 5 * k + 3]
    ctx = lambda k: [5 * k, 5 * k + 4, 5 * k + 10]
    for k in range(L // 5 - 3):
        par = z[ctx(k)[0]] ^ z[ctx(k)[1]] ^ z[ctx(k)[2]]
        if z[W(k)[0]] ^ z[W(k)[1]] ^ z[W(k)[2]] != par:
            z[W(k)[2]] ^= 1
    known, reads, cap, triggers = {}, [], Fraction(1), 0

    def rd(q, prob1=None):
        nonlocal cap
        assert q not in known
        b = z[q]
        known[q] = b
        reads.append(q)
        if prob1 is not None:
            cap = cap * (2 * prob1 if b == 1 else 2 * (1 - prob1))

    k = 0
    while len(reads) < N:
        while any(c in known for c in W(k)):
            k += 1
        win = W(k)
        while len(reads) < N:
            if all(c in known for c in ctx(k)):
                p = known[ctx(k)[0]] ^ known[ctx(k)[1]] ^ known[ctx(k)[2]]
                acc = 0
                for j, c in enumerate(win):
                    rest = len(win) - j - 1
                    # uniform over completions with parity p: P(bit=1)=1/2 unless last
                    if rest == 0:
                        prob1 = Fraction(1 if (acc ^ 1) == p else 0)
                    else:
                        prob1 = Fraction(1, 2)
                    rd(c, prob1)
                    acc ^= known[c]
                triggers += 1
                sweep = min(x for x in range(L) if x not in known)
                rd(sweep)
                break
            f = min(x for x in range(L) if x not in known and x not in win)
            rd(f)
    assert len(set(reads)) == len(reads)
    assert cap == Fraction(2) ** triggers, (cap, triggers)
    print(f"Corollary A4 window scan: PASS ({triggers} correct parity windows, capital 2^{triggers})")


def audit_theorem_B(trials=40, N=200):
    rng = random.Random(5)
    for trial in range(trials):
        x = [rng.randrange(2) for _ in range(N + 5)]
        y = [rng.randrange(2) for _ in range(N + 5)]
        z = lambda q: x[q // 2] if q % 2 == 0 else y[q // 2]
        run = BufferScan(1, 7000 + trial).run(z, N)
        d, a, b = Fraction(1), Fraction(1), Fraction(1)
        for q, bit, th in run:
            f = 1 + th * (2 * bit - 1)
            d *= f
            if q % 2 == 0:
                a *= f
            else:
                b *= f
            assert d == a * b
    print(f"Theorem B even/odd factor split: PASS ({trials} one-hole scans on joins)")


if __name__ == "__main__":
    audit_theorem_A()
    audit_window_A4()
    audit_theorem_B()
    print("ALL P4-S081 AUDITS PASS")
