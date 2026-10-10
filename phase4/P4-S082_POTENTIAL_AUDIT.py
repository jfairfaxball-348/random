#!/usr/bin/env python3
"""P4-S082 finite audit (exact rational arithmetic).

Checks, on finite truncations, the finite identities and inequalities behind
the consistency-potential method of phase4/P4-S082_MATHEMATICS.md:

  Lemma 2.1  Psi(sigma,t) = 2^|sigma| E_lambda[X_t C^sigma_t] is non-increasing in t;
  Lemma 2.2  2^|sigma| E_lambda[X_t 1_[sigma]] <= Psi(sigma,t);
  Lemma 2.3  avg_b Psi(sigma+(k,b),t) = Psi(sigma,t) + gamma(sigma,k,t)  (exact);
  Lemma 3.1  for a one-hole scan and t >= c(n): sum_{k<n, k notin dom sigma}
           gamma(sigma,k,t) <= Psi(sigma,t)  (and <= h*Psi for h-hole scans);
  Lemma 2.4  savings transform: X_t' >= X_t - 2 and bounded X => bounded d;
  Lemma 3.2  (and Lemmas 2.1-2.3) for one-hole scans of a blockwise recoding
           K(z) (3-blocks, GL(3,F2) including the committed A), with candidates
           in distinct blocks;
  Construction: a finite run of the stage construction keeps Phi < 2 and leaves
           a completion on which every weighted capital stays below 2.
  Examples E1 (unbounded width) and E2 (cumulative-difference 2-to-1 map)
           illustrating the cost obstruction and neutralization of Section 7.

It does NOT verify statements about infinite transcripts, Pi^0_2 guessing,
compactness, computable randomness, Martin-Lof randomness or OH membership;
those rest on the written proofs.
"""
import hashlib
import itertools
import random
from fractions import Fraction as Fr

STAKES = [Fr(k, 4) for k in (-4, -3, -2, -1, 0, 1, 2, 3, 4)]


def h_int(*parts):
    return int.from_bytes(hashlib.sha256(repr(parts).encode()).digest()[:8], "big")


# ---------------------------------------------------------------------------
# Scans driven by a bit transcript.  A scan is a deterministic function of the
# transcript: next_query(transcript) and stake(transcript).  The buffer scan
# keeps at most h postponed coordinates; unread coordinates below the pointer
# are exactly the buffer, and the pointer is >= t/2, so n_t = floor(t/2)
# (c(n) = 2n) is a valid frontier with |U_t| <= h.
# ---------------------------------------------------------------------------
class BufferScan:
    def __init__(self, h, seed):
        self.h, self.seed = h, seed

    def queries(self, transcript):
        """Replay: return the list of queried coordinates q_0..q_{len}."""
        buf, p, qs = [], 0, []
        for t in range(len(transcript) + 1):
            pre = tuple(transcript[:t])
            if buf and h_int(self.seed, "pull", pre) % 10 < 3:
                q = buf.pop(h_int(self.seed, "pick", pre) % len(buf))
            else:
                k = 0
                while len(buf) < self.h and h_int(self.seed, "post", pre, k) % 10 < 3:
                    buf.append(p)
                    p += 1
                    k += 1
                q = p
                p += 1
            qs.append(q)
        assert len(set(qs)) == len(qs)
        return qs

    def stake(self, transcript):
        return STAKES[h_int(self.seed, "stake", tuple(transcript)) % len(STAKES)]


class IdentityScan:
    def __init__(self, seed):
        self.seed = seed

    def queries(self, transcript):
        return list(range(len(transcript) + 1))

    def stake(self, transcript):
        return STAKES[h_int(self.seed, "stake", tuple(transcript)) % len(STAKES)]


def savings_path(thetas_bits):
    """Savings transform along one transcript.  Input: list of (theta, bit).
    Returns list of capitals X_0..X_t of the savings martingale and of the
    original d_0..d_t."""
    A, B, d = Fr(1), 0, Fr(1)
    X, D = [A + B], [d]
    for th, b in thetas_bits:
        sgn = 1 if b == 1 else -1
        A = A * (1 + th * sgn)
        d = d * (1 + th * sgn)
        while A >= 2:
            A -= 1
            B += 1
        X.append(A + B)
        D.append(d)
    return X, D


def capital_and_reads(scan, bits):
    """Savings capital X_t and the read sequence along transcript `bits`."""
    qs = scan.queries(bits)
    pairs = [(scan.stake(bits[:s]), bits[s]) for s in range(len(bits))]
    X, _ = savings_path(pairs)
    return X[-1], qs[: len(bits)]


# ---------------------------------------------------------------------------
# Raw potential quantities, computed exactly by enumerating all 2^t transcripts
# (under the fair-coin measure the read bits of a no-repeat scan are iid fair).
# ---------------------------------------------------------------------------
def psi_raw(scan, sigma, t, k=None):
    """Return (Psi, E[X 1_[sigma]] * 2^|sigma|, gamma_k) for raw scan."""
    psi = Fr(0)
    exact = Fr(0)
    gam = Fr(0)
    w = Fr(1, 2 ** t)
    for bits in itertools.product((0, 1), repeat=t):
        bits = list(bits)
        X, reads = capital_and_reads(scan, bits)
        val = dict(zip(reads, bits))
        C = all(val[q] == b for q, b in sigma.items() if q in val)
        if not C:
            continue
        unread = sum(1 for q in sigma if q not in val)
        psi += w * X
        exact += w * X * Fr(1, 2 ** unread)
        if k is not None and k not in val:
            gam += w * X
    s = 2 ** len(sigma)
    return psi * s, exact * s, gam * s


def check_raw_lemmas(trials=40, T=9):
    rng = random.Random(82)
    n_l1 = n_l2 = n_l3 = n_l4 = 0
    for tr in range(trials):
        h = 1 if tr % 4 else 2
        scan = BufferScan(h, ("raw", tr)) if tr % 5 else IdentityScan(("id", tr))
        nfix = rng.randint(0, 3)
        dom = rng.sample(range(0, 5), nfix)
        sigma = {q: rng.randint(0, 1) for q in dom}
        prev = None
        for t in range(T + 1):
            psi, exact, _ = psi_raw(scan, sigma, t)
            assert exact <= psi, ("Lemma 2.2", tr, t)
            n_l2 += 1
            if prev is not None:
                assert psi <= prev, ("Lemma 2.1", tr, t, psi, prev)
                n_l1 += 1
            prev = psi
        # Lemma 2.3 exact identity, Lemma 3.1 one-hole bound
        t = T
        n = t // 2  # frontier n_t for the buffer scan; identity frontier is t
        psi, _, _ = psi_raw(scan, sigma, t)
        total = Fr(0)
        for k in range(0, n):
            if k in sigma:
                continue
            _, _, g = psi_raw(scan, sigma, t, k)
            p0, _, _ = psi_raw(scan, {**sigma, k: 0}, t)
            p1, _, _ = psi_raw(scan, {**sigma, k: 1}, t)
            assert (p0 + p1) / 2 == psi + g, ("Lemma 2.3", tr, k)
            n_l3 += 1
            total += g
        bound = (scan.h if isinstance(scan, BufferScan) else 1) * psi
        assert total <= bound, ("Lemma 3.1", tr, total, bound)
        n_l4 += 1
    return n_l1, n_l2, n_l3, n_l4


def check_savings(trials=300, steps=60):
    rng = random.Random(5)
    for _ in range(trials):
        pairs = [(rng.choice(STAKES), rng.randint(0, 1)) for _ in range(steps)]
        X, D = savings_path(pairs)
        for t in range(len(X)):
            for u in range(t, len(X)):
                assert X[u] > X[t] - 2, "savings drop"
        if max(X) < 3:  # no bank transfer beyond the first unit: A tracks d
            pass
    # a winning path: savings capital must exceed any bound when d does
    pairs = [(Fr(1, 2), 1)] * 80
    X, D = savings_path(pairs)
    assert D[-1] > 10 ** 10 and X[-1] > 20
    return trials


# ---------------------------------------------------------------------------
# Virtual scans through a blockwise recoding K (3-blocks, matrices in GL(3,2)).
# y = K(z): y_block = M_j z_block (over F2).  The scan reads virtual bits.
# Consistency: exists raw z' in [sigma] agreeing with the virtual reads.
# ---------------------------------------------------------------------------
A = ((1, 0, 1), (1, 1, 0), (1, 1, 1))  # committed rows: y0=x0+x2, y1=x0+x1, y2=x0+x1+x2


def matvec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) % 2 for i in range(3))


def gl3():
    out = []
    for rows in itertools.product(itertools.product((0, 1), repeat=3), repeat=3):
        imgs = {matvec(rows, v) for v in itertools.product((0, 1), repeat=3)}
        if len(imgs) == 8:
            out.append(rows)
    return out


def virtual_state(Ms, vreads, sigma):
    """For each block touched by virtual reads or sigma, the raw block values
    consistent with both.  Returns dict block -> list of raw 3-tuples."""
    blocks = {q // 3 for q in vreads} | {q // 3 for q in sigma}
    out = {}
    for b in blocks:
        M = Ms[b % len(Ms)]
        cands = []
        for x in itertools.product((0, 1), repeat=3):
            y = matvec(M, x)
            ok = all(y[q % 3] == v for q, v in vreads.items() if q // 3 == b)
            ok = ok and all(x[q % 3] == v for q, v in sigma.items() if q // 3 == b)
            if ok:
                cands.append(x)
        out[b] = cands
    return out


def psi_virtual(scan, Ms, sigma, t, k=None):
    psi = Fr(0)
    exact = Fr(0)
    gam = Fr(0)
    w = Fr(1, 2 ** t)
    for bits in itertools.product((0, 1), repeat=t):
        bits = list(bits)
        X, reads = capital_and_reads(scan, bits)
        vreads = dict(zip(reads, bits))
        st = virtual_state(Ms, vreads, sigma)
        if any(len(c) == 0 for c in st.values()):
            continue
        psi += w * X
        # exact conditional probability of [sigma] given the virtual reads
        pr = Fr(1)
        for b, cands in st.items():
            # raw values consistent with the virtual reads only
            M = Ms[b % len(Ms)]
            allc = [x for x in itertools.product((0, 1), repeat=3)
                    if all(matvec(M, x)[q % 3] == v for q, v in vreads.items() if q // 3 == b)]
            pr *= Fr(len(cands), len(allc))
        exact += w * X * pr
        if k is not None:
            cands = st.get(k // 3)
            if cands is None:
                # block untouched: both values possible
                gam += w * X
            elif len({x[k % 3] for x in cands}) == 2:
                gam += w * X
    s = 2 ** len(sigma)
    return psi * s, exact * s, gam * s


def check_virtual_lemmas(trials=24, T=9):
    rng = random.Random(7)
    G = gl3()
    assert len(G) == 168 and A in G
    n1 = n3 = n4 = 0
    for tr in range(trials):
        Ms = [A] if tr % 3 == 0 else [rng.choice(G) for _ in range(4)]
        scan = BufferScan(1, ("virt", tr))
        dom = rng.sample(range(0, 6), rng.randint(0, 2))
        sigma = {q: rng.randint(0, 1) for q in dom}
        prev = None
        for t in range(T + 1):
            psi, exact, _ = psi_virtual(scan, Ms, sigma, t)
            assert exact <= psi, ("V-Lemma 2.2", tr, t)
            if prev is not None:
                assert psi <= prev, ("V-Lemma 2.1", tr, t)
                n1 += 1
            prev = psi
        t = T
        n = t // 2
        psi, _, _ = psi_virtual(scan, Ms, sigma, t)
        # candidates: one per block, whole block below the frontier
        cands = []
        for b in range(n // 3):
            ks = [3 * b + r for r in range(3) if 3 * b + r not in sigma]
            if ks:
                cands.append(ks[h_int(tr, b) % len(ks)])
        total = Fr(0)
        for k in cands:
            _, _, g = psi_virtual(scan, Ms, sigma, t, k)
            p0, _, _ = psi_virtual(scan, Ms, {**sigma, k: 0}, t)
            p1, _, _ = psi_virtual(scan, Ms, {**sigma, k: 1}, t)
            assert (p0 + p1) / 2 == psi + g, ("V-Lemma 2.3", tr, k)
            n3 += 1
            total += g
        assert total <= psi, ("V-Lemma 3.2", tr, total, psi)
        n4 += 1
    return n1, n3, n4


# ---------------------------------------------------------------------------
# Finite run of the stage construction (Section 4) with several valid scans.
# ---------------------------------------------------------------------------
def finite_construction(T=10, nstrat=4, seed=3):
    scans = [IdentityScan(("c", 0))] + [BufferScan(1, ("c", e)) for e in range(1, nstrat)]
    sigma, weights, phis = {}, [], []

    def Phi(sig, t):
        return sum(w * psi_raw(scans[e], sig, t)[0] for e, w in weights)

    def Gam(sig, k, t):
        return sum(w * psi_raw(scans[e], sig, t, k)[2] for e, w in weights)

    t = T
    n = t // 2  # common frontier for buffer scans (identity frontier is larger)
    nextfree = 0
    for i in range(nstrat):
        P = psi_raw(scans[i], sigma, t)[0]
        w = Fr(1, 2 ** (i + 2)) / (P + 1)
        weights.append((i, w))
        # fix one coordinate per stage among candidates below the frontier
        cand = [k for k in range(nextfree, n) if k not in sigma]
        if not cand:
            break
        before = Phi(sigma, t)
        k = min(cand, key=lambda c: (Gam(sigma, c, t), c))
        g = Gam(sigma, k, t)
        assert g * len(cand) <= before, "Lemma 3.1 averaging"
        b = min((0, 1), key=lambda v: (Phi({**sigma, k: v}, t), v))
        sigma[k] = b
        after = Phi(sigma, t)
        assert after <= before + g, "refinement increase exceeds gamma"
        nextfree = k + 1
        phis.append(after)
        assert after < 2
    # some completion keeps the weighted capital below 2 at every time <= T
    best = None
    free = [q for q in range(2 * T + 4) if q not in sigma]
    rng = random.Random(seed)
    ok_found = False
    for _ in range(4000):
        z = {**sigma, **{q: rng.randint(0, 1) for q in free}}
        good = True
        for tt in range(T + 1):
            D = Fr(0)
            for e, w in weights:
                sc = scans[e]
                bits, qs = [], []
                for s in range(tt):
                    q = sc.queries(bits)[s]
                    bits.append(z[q])
                X, _ = capital_and_reads(sc, bits)
                D += w * X
            if D >= 2:
                good = False
                break
        if good:
            ok_found = True
            break
    assert ok_found, "no good completion found"
    return len(sigma), phis


# ---------------------------------------------------------------------------
# Examples for Section 7.
# ---------------------------------------------------------------------------
class EvenOddScan:
    """Unbounded width: read z_0, then all odd coordinates if z_0 = 0,
    else all even coordinates >= 2; never return to the other parity."""

    def __init__(self, seed):
        self.seed = seed

    def queries(self, transcript):
        qs = [0]
        if transcript:
            par = 1 if transcript[0] == 0 else 0
            nxt = 1 if par == 1 else 2
            for _ in range(len(transcript)):
                qs.append(nxt)
                nxt += 2
        return qs

    def stake(self, transcript):
        return STAKES[h_int(self.seed, "stake", tuple(transcript)) % len(STAKES)]


def example_E1(T=9):
    sc = EvenOddScan("E1")
    psi, _, _ = psi_raw(sc, {}, T)
    costs = [psi_raw(sc, {}, T, k)[2] for k in range(1, 8)]
    # every coordinate k >= 1 is unread on (at least) one parity branch forever
    assert all(c > 0 for c in costs)
    assert sum(costs) > psi, "sum of costs exceeds Psi: no one-hole Lemma 3.1 bound"
    return psi, costs


def example_E2(m=7):
    """Cumulative-difference map F(z)_i = z_i + z_{i+1}: every output prefix of
    length m has exactly two compatible source prefixes of length m+1, which
    differ in every coordinate.  With sigma empty every coordinate is split;
    after fixing one coordinate no coordinate is split."""
    rng = random.Random(11)
    thetas = {}

    def theta(w):
        if w not in thetas:
            thetas[w] = rng.choice(STAKES)
        return thetas[w]

    def run(sigma, k):
        psi = gam = Fr(0)
        for z in itertools.product((0, 1), repeat=m + 1):
            out = tuple((z[i] + z[i + 1]) % 2 for i in range(m))
            X = Fr(1)
            for i in range(m):
                X *= 1 + theta(out[:i]) * (1 if out[i] else -1)
            comp = [z, tuple(1 - c for c in z)]
            cons = [c for c in comp if all(c[q] == v for q, v in sigma.items())]
            if not cons:
                continue
            w = Fr(1, 2 ** (m + 1))
            psi += w * X
            if len({c[k] for c in cons}) == 2:
                gam += w * X
        s = 2 ** len(sigma)
        return psi * s, gam * s

    psi0, g0 = run({}, 3)
    assert g0 == psi0 and psi0 > 0, "empty sigma: coordinate split on all outputs"
    psi1, g1 = run({0: 1}, 3)
    assert g1 == 0, "after one fixing the double fibre is neutralized"
    return psi0, g0, psi1, g1


def main():
    print("Lemmas 2.1, 2.2, 2.3, 3.1 (raw one-hole/two-hole/identity scans):", check_raw_lemmas(), "checks PASS")
    print("Lemma 2.4 (savings transform):", check_savings(), "paths PASS")
    print("Lemmas 2.1, 2.3, 3.2 (virtual scans through blockwise GL(3,2) recodings incl. A):",
          check_virtual_lemmas(), "checks PASS")
    nfixed, phis = finite_construction()
    print("Finite construction: fixed", nfixed, "coordinates; Phi after each stage =",
          [str(p) for p in phis], "all < 2; good completion found: PASS")
    psi, costs = example_E1()
    print("Example E1 (unbounded width): Psi =", psi, "; sum of costs k=1..7 =", sum(costs),
          "> Psi: PASS (illustrates failure of Lemma 3.1 without bounded width)")
    print("Example E2 (cumulative difference):", [str(v) for v in example_E2()],
          "split at sigma=empty, neutralized after one fixing: PASS")
    print("ALL P4-S082 AUDITS PASS")


if __name__ == "__main__":
    main()
