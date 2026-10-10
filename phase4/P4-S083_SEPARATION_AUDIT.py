#!/usr/bin/env python3
"""P4-S083 finite audit (exact arithmetic) for the tail-coded-hole separation.

Checks, on finite truncations, the finite facts behind
phase4/P4-S083_MATHEMATICS.md:

  Part 1  Lemma 2.1 (tail-coded hole): for v = D'(z), flipping v_q is the same
          as complementing the raw tail z_[q,M); z_j = z_{q-1} xor v_q xor ...
          xor v_j for j >= q; any absolute value z_F (F >= q) determines v_q.
  Part 2  Lemma 3.2 (class separation) on a toy family of class-separated runs:
          runs are nested along guesses, and the fixes made by an incomparable
          run from its divergence stage on avoid every true-run fix.
  Part 3  The scan T* on D'(z) (toy threshold): total, no-repeat, at most one
          unread coordinate below its filler frontier; every resolution
          predicts v_q correctly unless z lies in the fooling cylinder
          B(q, eps') of the selected run (checked as an exact equivalence);
          an adversarial completion shows fooling is possible, so the
          exclusion of W in Proposition 3.6 is needed.
  Part 4  Exact fibre count: on all 2^14 raw prefixes, each T*-transcript of
          D'(x) has at most two raw preimage prefixes.
  Part 5  Exact series: sum_{q>=0} sum_{m>=1} 2^m 2^{-(q+2m+4)} = 1/8, and the
          compactness constant 4*(1 - 1/8) = 7/2 > 2.

It does NOT verify statements about infinite transcripts, the Pi^0_2 guessing,
compactness, computable randomness, Martin-Lof randomness or OH membership;
those rest on the written proofs (and on the frozen P4-S082 audit for the
potential lemmas).
"""
import hashlib
import itertools
import random
from fractions import Fraction as Fr


def hbit(*parts):
    return hashlib.sha256(repr(parts).encode()).digest()[0] & 1


def Dprime(z):
    return [z[0]] + [z[i] ^ z[i - 1] for i in range(1, len(z))]


def Dprime_inv(v):
    z, acc = [], 0
    for b in v:
        acc ^= b
        z.append(acc)
    return z


# ---------------------------------------------------------------------------
# Part 1: tail-coded hole algebra
# ---------------------------------------------------------------------------
def part1(rng, trials=400, L=24):
    checks = 0
    for _ in range(trials):
        z = [rng.randrange(2) for _ in range(L)]
        v = Dprime(z)
        assert Dprime_inv(v) == z
        for q in range(L):
            zz = z[:q] + [1 - b for b in z[q:]]
            vv = Dprime(zz)
            assert vv == v[:q] + [1 - v[q]] + v[q + 1:]
            zq1 = z[q - 1] if q > 0 else 0
            acc = zq1 ^ v[q]
            for j in range(q, L):
                if j > q:
                    acc ^= v[j]
                assert z[j] == acc
                # pi_j: everything except v_q; z_F and pi_F determine v_q
                pi = zq1
                for i in range(q + 1, j + 1):
                    pi ^= v[i]
                assert z[j] ^ pi == v[q]
                checks += 1
    return checks


# ---------------------------------------------------------------------------
# Part 2: toy class-separated runs
# Strings eps of length <= MAXLEN; idx(eps) canonical; class C_eps =
# { idx(eps) + NSTR * j }.  Stage s of run eps fixes 2s+2 coordinates, each the
# least element of C_{eps|(s+1)} above the current max, with a hash value
# (a stand-in for the potential-minimizing choice).
# ---------------------------------------------------------------------------
MAXLEN = 3
STRINGS = [""] + ["".join(p) for n in range(1, MAXLEN + 1) for p in itertools.product("01", repeat=n)]
IDX = {s: i for i, s in enumerate(STRINGS)}
NSTR = len(STRINGS)


def class_elems_above(eps, a):
    i = IDX[eps]
    j = 0 if a <= i else -(-(a - i) // NSTR)
    while True:
        yield i + NSTR * j
        j += 1


def run(eps, salt):
    """Return list of stage assignments sigma_0 <= ... <= sigma_{m-1}."""
    sigma, out = {}, []
    for s in range(len(eps)):
        pref = eps[: s + 1]
        for _ in range(2 * s + 2):
            a = 1 + max(sigma) if sigma else 0
            k = next(class_elems_above(pref, a))
            sigma[k] = hbit(salt, pref, k)
        out.append(dict(sigma))
    return out


def stage_of(eps, salt):
    """Map position -> stage at which run eps fixed it."""
    st, prev = {}, set()
    for s, sg in enumerate(run(eps, salt)):
        for k in sg:
            if k not in prev:
                st[k] = s
        prev = set(sg)
    return st


def part2(salt):
    checks = 0
    runs = {e: run(e, salt) for e in STRINGS if e}
    # nesting along guesses: stage s of eps equals stage s of eps|(s+1)
    for e, rr in runs.items():
        for s in range(len(e)):
            assert rr[s] == runs[e[: s + 1]][s]
            checks += 1
    # class separation
    for estar in [e for e in STRINGS if len(e) == MAXLEN]:
        dom_true = set(runs[estar][-1])
        for e2 in STRINGS:
            if not e2 or estar.startswith(e2):
                continue
            div = next(i for i in range(min(len(e2), len(estar)) + 1)
                       if i == len(e2) or e2[i] != estar[i])
            st = stage_of(e2, salt)
            shared = runs[e2][div - 1] if div > 0 else {}
            for k, b in runs[e2][-1].items():
                if st[k] >= div:
                    assert k not in dom_true
                else:
                    assert k in dom_true and runs[estar][-1][k] == b == shared[k]
                checks += 1
    return checks, runs


# ---------------------------------------------------------------------------
# Part 3: the scan T* on v = D'(z)
# ---------------------------------------------------------------------------
def tstar(v, runs, M_lim, rthr):
    """Simulate T* on virtual sequence v, querying only coordinates < M_lim.
    Returns (queries, resolutions) where resolutions is a list of
    (q, selected_eps, prediction, actual, Fs)."""
    q, M = 0, 1
    read = {}
    queries, res = [], []
    order = sorted((e for e in runs), key=lambda e: IDX[e])
    while True:
        # known data
        zpre, acc = [], 0
        for i in range(q):
            acc ^= read[i]
            zpre.append(acc)
        zq1 = zpre[q - 1] if q > 0 else 0
        pi, p = {}, zq1
        for F in range(q, M):
            if F > q:
                p ^= read[F]
            pi[F] = p
        sel = None
        for e in order:
            sg = runs[e][-1]
            if any(k < q and sg[k] != zpre[k] for k in sg):
                continue
            Fs = sorted(k for k in sg if k >= q)[: rthr(q, len(e))]
            if len(Fs) < rthr(q, len(e)) or max(Fs) >= M:
                continue
            imp = {sg[F] ^ pi[F] for F in Fs}
            if len(imp) == 1:
                sel = (e, imp.pop(), Fs)
                break
        if sel is not None:
            queries.append(q)
            read[q] = v[q]
            res.append((q, sel[0], sel[1], v[q], sel[2]))
            q, M = M, M + 1
            if q >= M_lim:
                break
        else:
            if M >= M_lim:
                break
            queries.append(M)
            read[M] = v[M]
            M += 1
    return queries, res, q, M


def part3(rng, runs, salt, trials=60):
    L = 1 + max(max(r[-1]) for r in runs.values()) + 5
    rthr = lambda q, m: 2
    stats = dict(res=0, correct=0, fooled=0, eq_checks=0, true_sel=0)
    for estar in [e for e in STRINGS if len(e) == MAXLEN]:
        sig = runs[estar][-1]
        for _ in range(trials):
            z = [sig.get(i, rng.randrange(2)) for i in range(L)]
            v = Dprime(z)
            queries, res, q, M = tstar(v, runs, L, rthr)
            # no-repeat and one-hole below the filler frontier
            assert len(queries) == len(set(queries))
            unread = [i for i in range(M) if i not in set(queries)]
            assert len(unread) <= 1 and (not unread or unread == [q])
            for (qq, e2, pred, act, Fs) in res:
                stats["res"] += 1
                anti = all(z[F] != runs[e2][-1][F] for F in Fs)
                assert (pred != act) == anti
                stats["eq_checks"] += 1
                if estar.startswith(e2):
                    stats["true_sel"] += 1
                    assert pred == act
                if pred == act:
                    stats["correct"] += 1
                else:
                    stats["fooled"] += 1
    # adversarial completion: anti on a spurious run's distinctive fixes
    estar = "1" * MAXLEN
    sig = runs[estar][-1]
    e2 = "0"
    st = stage_of(e2, salt)
    z = [sig.get(i, 0) for i in range(L)]
    for k, b in runs[e2][-1].items():
        if st[k] >= 0 and k not in sig:
            z[k] = 1 - b
    _, res, _, _ = tstar(Dprime(z), runs, L, rthr)
    adv_fooled = sum(1 for r in res if r[2] != r[3])
    return stats, adv_fooled


# ---------------------------------------------------------------------------
# Part 4: exact fibre count of the toy T*-transcripts on raw prefixes
# ---------------------------------------------------------------------------
def part4(runs, M_lim=14):
    rthr = lambda q, m: 2
    groups = {}
    for bits in itertools.product((0, 1), repeat=M_lim):
        v = Dprime(list(bits))
        queries, _, _, _ = tstar(v, runs, M_lim, rthr)
        key = tuple((i, v[i]) for i in queries)
        groups.setdefault(key, []).append(bits)
    mx = max(len(g) for g in groups.values())
    assert mx <= 2
    return len(groups), mx


# ---------------------------------------------------------------------------
# Part 5: exact series and compactness constants
# ---------------------------------------------------------------------------
def part5():
    total = Fr(0)
    for q in range(0, 60):
        for m in range(1, 60):
            total += Fr(2 ** m, 2 ** (q + 2 * m + 4))
    # closed form: sum_q 2^{-q-4} * sum_{m>=1} 2^{-m} = 2^{-4} * 2 * 1 = 1/8
    closed = Fr(1, 16) * 2 * 1
    assert closed == Fr(1, 8)
    assert total < closed and closed - total < Fr(1, 10 ** 15)
    lower = 4 * (1 - Fr(1, 8))
    assert lower == Fr(7, 2) and lower > 2
    return total, closed, lower


def main():
    rng = random.Random(83)
    c1 = part1(rng)
    print(f"Part 1 (tail-coded hole algebra): {c1} checks PASS")
    salt = "P4-S083"
    c2, runs = part2(salt)
    print(f"Part 2 (toy class-separated runs: nesting + separation): {c2} checks PASS")
    stats, adv = part3(rng, runs, salt)
    print("Part 3 (T* on D'(z), toy threshold r=2): "
          f"{stats['res']} resolutions, {stats['correct']} correct, {stats['fooled']} fooled; "
          f"wrong <=> anti-consistent selected fixes: {stats['eq_checks']} equivalences PASS; "
          f"{stats['true_sel']} selections of true-run prefixes, all correct; "
          f"adversarial completion fooled T* {adv} time(s)")
    assert adv >= 1
    ng, mx = part4(runs)
    print(f"Part 4 (exact fibre count, 2^14 raw prefixes): {ng} transcripts, max preimages {mx} PASS")
    total, closed, lower = part5()
    print(f"Part 5 (series): partial sum {float(total):.12f} < {closed} = closed form; "
          f"compactness lower bound {lower} > 2 PASS")
    print("ALL P4-S083 AUDITS PASS")


if __name__ == "__main__":
    main()
