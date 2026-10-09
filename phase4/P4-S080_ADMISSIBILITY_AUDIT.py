#!/usr/bin/env python3
"""Exact finite audits for P4-S080.

The infinite statements (computable randomness, OH membership, wtt-autoreducibility on
infinite sequences, global one-hole legality) are proved in P4-S080_MATHEMATICS.md.
This script only checks the finite combinatorics those proofs rely on:

  1. GL(3,F2): the invertible matrices with NO unit column form exactly the double coset
     S3*A*S3 of the committed A=[101;110;111], which is closed under inversion.
  2. The greedy spreading bijection tau of Lemma 1 for several nondecreasing caps U:
     injective, initial segments exhausted, and j>U(i), k>U(j) in every triple.
  3. A toy finite model of Lemma 1/Theorem 2: for synthetic self-avoiding, use-capped,
     partially defined predictors N on a finite W, the chained-substitution predictor
     M_V never reads its own V-block and returns the correct V-bit; the derived raw
     predictor for X1=H^{-1}(V) never reads its own raw block and is correct.
  4. Role refutation (Proposition 6): for every target in-block query pattern and every
     raw role r, the false single-hole candidate Y xor a_r is refuted by equation q
     whenever q is in supp(a_r) and the target computation at q queries no other
     coordinate of supp(a_r).
"""
import itertools, random

# ---------- 1. GL(3,F2) double-coset audit ----------
def mm(U, V):
    return tuple(tuple(sum(U[i][k] * V[k][j] for k in range(3)) % 2 for j in range(3)) for i in range(3))

def det(M):
    a = M
    return (a[0][0]*(a[1][1]*a[2][2]+a[1][2]*a[2][1]) + a[0][1]*(a[1][0]*a[2][2]+a[1][2]*a[2][0])
            + a[0][2]*(a[1][0]*a[2][1]+a[1][1]*a[2][0])) % 2

def inv(M):
    I = ((1,0,0),(0,1,0),(0,0,1))
    for N in GL:
        if mm(M, N) == I:
            return N
    raise AssertionError

allm = [tuple(tuple((m >> (3*i+j)) & 1 for j in range(3)) for i in range(3)) for m in range(512)]
GL = [M for M in allm if det(M) == 1]
assert len(GL) == 168
A = ((1,0,1),(1,1,0),(1,1,1))
assert A in GL
perms = [tuple(tuple(1 if p[i] == j else 0 for j in range(3)) for i in range(3)) for p in itertools.permutations(range(3))]
coset = {mm(mm(P, A), Q) for P in perms for Q in perms}
def colweights(M):
    return tuple(sum(M[r][c] for r in range(3)) for c in range(3))
nounit = {M for M in GL if 1 not in colweights(M)}
assert coset == nounit, (len(coset), len(nounit))
assert all(inv(M) in coset for M in coset)
assert inv(A) in coset
assert all(1 in colweights(M) for M in GL if M not in coset)
print('1. GL(3,2): |GL|=168, no-unit-column matrices = S3*A*S3 (size %d), closed under inverse: PASS' % len(coset))

# ---------- 2. spreading bijection tau ----------
def build_tau(U, nblocks):
    used, triples = set(), []
    def least_unused(lo):
        x = lo
        while x in used:
            x += 1
        return x
    for _ in range(nblocks):
        i = least_unused(0); used.add(i)
        j = least_unused(U(i) + 1); used.add(j)
        k = least_unused(U(j) + 1); used.add(k)
        triples.append((i, j, k))
    return triples, used

caps = {
    'U=2i+3': lambda i: 2*i + 3,
    'U=i^2+1': lambda i: i*i + 1,
    'U=3i+7': lambda i: 3*i + 7,
    'U=i+1': lambda i: i + 1,
}
for name, U in caps.items():
    triples, used = build_tau(U, 400)
    flat = [x for t in triples for x in t]
    assert len(flat) == len(set(flat))
    for (i, j, k) in triples:
        assert j > U(i) and k > U(j) and k > U(i)
    # every number below the 400th first-coordinate is already used (exhaustion of initial segments)
    last_i = triples[-1][0]
    assert all(x in used for x in range(last_i + 1))
print('2. greedy tau: injective, initial segments exhausted, j>U(i), k>U(j) for 4 caps x 400 blocks: PASS')

# ---------- 3. toy chained-substitution model ----------
random.seed(80)
def toy_trial(U, nblocks):
    triples, used = build_tau(U, nblocks)
    L = 3 * nblocks
    # finite truncation: only the 3*nblocks coordinates covered by the first triples exist
    used_sorted = sorted(used)
    W = {m: random.randint(0, 1) for m in used_sorted}
    # synthetic clipped self-avoiding predictor N(i): query list inside [0,U(i)] minus {i}
    qsets = {}
    for i in used_sorted:
        cand = [m for m in used_sorted if m <= U(i) and m != i]
        qsets[i] = random.sample(cand, min(len(cand), random.randint(0, 4)))
    def N(i, oracle, log):
        # adaptive: second query depends on first answer; diverges (None) on some off-target patterns
        acc = 0
        qs = list(qsets[i])
        for t, m in enumerate(qs):
            assert m != i and m <= U(i)
            b = oracle(m); log.append(m)
            acc ^= b ^ W[m]
            if t == 0 and b != W[m] and (i % 3 == 0):
                return None  # divergence on a sibling
        return W[i] ^ acc
    tau = {}
    for n, (i, j, k) in enumerate(triples):
        tau[(n, 0)], tau[(n, 1)], tau[(n, 2)] = i, j, k
    tinv = {v: kk for kk, v in tau.items()}
    V = [W[tau[(n, r)]] for n in range(nblocks) for r in range(3)]
    def MV(q, Zv, log):
        n, r = divmod(q, 3)
        i, j, k = triples[n]
        sub = {}
        def wor(m):
            if m in sub:
                return sub[m]
            nn, rr = tinv[m]
            assert nn != n, 'read own V-block'
            log.append(3 * nn + rr)
            return Zv[3 * nn + rr]
        out = []
        for c in (i, j, k):
            b = N(c, wor, [])
            if b is None:
                return None
            sub[c] = b
            out.append(b)
        return out[r]
    # block-avoidance on random oracles; correctness on V
    for q in range(L):
        log = []
        assert MV(q, V, log) == V[q]
        assert all(p // 3 != q // 3 for p in log)
        for _ in range(5):
            Z = [random.randint(0, 1) for _ in range(L)]
            log = []
            MV(q, Z, log)
            assert all(p // 3 != q // 3 for p in log)
    # derived raw predictor for X1 = H^{-1}(V)
    Ainv = inv(A)
    def act(Mx, x):
        return tuple(sum(Mx[r][c] * x[c] for c in range(3)) % 2 for r in range(3))
    X1 = []
    for n in range(nblocks):
        X1.extend(act(Ainv, tuple(V[3*n:3*n+3])))
    def PX(p, Zx):
        n, r = divmod(p, 3)
        def Vfrom(q):
            m, s = divmod(q, 3)
            assert m != n, 'raw predictor read own raw block'
            return act(A, tuple(Zx[3*m:3*m+3]))[s]
        Zv = [None] * L
        for q in range(L):
            if q // 3 != n:
                Zv[q] = Vfrom(q)
        vals = []
        for s in range(3):
            b = MV(3 * n + s, Zv, [])
            if b is None:
                return None
            vals.append(b)
        return act(Ainv, tuple(vals))[r]
    for p in range(L):
        assert PX(p, X1) == X1[p]
    return True

for name, U in caps.items():
    for _ in range(25):
        toy_trial(U, 40)
print('3. toy chained substitution: M_V block-avoiding on random oracles and correct on V; raw X1 predictor block-avoiding and correct (4 caps x 25 trials x 40 blocks): PASS')

# ---------- 4. role refutation ----------
cols = [tuple(A[r][c] for r in range(3)) for c in range(3)]  # a_0=(1,1,1), a_1=(0,1,1), a_2=(1,0,1)
assert cols == [(1,1,1), (0,1,1), (1,0,1)]
count = 0
for v in itertools.product((0, 1), repeat=3):
    # target in-block query pattern: Qs[q] = subset of the other two in-block coordinates queried on target
    others = [[p for p in range(3) if p != q] for q in range(3)]
    for pat in itertools.product(*[[tuple(s) for k in range(3) for s in itertools.combinations(o, k)] for o in others]):
        for r in range(3):
            a = cols[r]
            false = tuple(v[t] ^ a[t] for t in range(3))
            supp = [t for t in range(3) if a[t]]
            for q in supp:
                if not any(p in supp for p in pat[q]):
                    # the computation at q reads only target-equal coordinates on the false candidate,
                    # hence returns v[q], while the false candidate claims v[q]^1
                    seen_false = tuple(false[p] for p in pat[q])
                    seen_true = tuple(v[p] for p in pat[q])
                    assert seen_false == seen_true
                    assert false[q] != v[q]
                    count += 1
print('4. role refutation: %d (block value, query pattern, role, equation) cases: PASS' % count)
print('ALL P4-S080 FINITE AUDITS PASS')
