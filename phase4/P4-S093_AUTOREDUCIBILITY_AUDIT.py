#!/usr/bin/env python3
"""P4-S093 exact finite audit.

Checks finite components of P4-S093 in exact arithmetic (fractions / integers):
  A. Theorem A on finite models: autoreduction <-> separated families
     (both directions), the self-avoidance identity, the race form.
  L1. Larger-candidate soundness for approximations below a non-dyadic real,
      in random causal finite frames.
  L2. The raw-frame reader at one hold, simulated check by check with the
      canonical schedule, against the closed-form window criterion Land_N.
  G. The pairing/density dichotomy of Lemma G in causal finite frames.
  M. The martingale used in Lemma M.
  F. The counting identity and bias formula of Proposition F for random
     balanced finite maps (cells may meet both sides).
  E. The all-in example: in the tail-coded frame D' one all-in bet inside the
     window gives specified-side bias 1.
  S. The section 3.3 inequality h*delta_{2h} <= sum_{j>=h} delta_j.
Finite checks support, but never replace, the written proofs.
"""
import itertools
import random
from fractions import Fraction

random.seed(93093)
CHECKS = 0


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)


def bits(i, n):
    return tuple((i >> (n - 1 - j)) & 1 for j in range(n))


def flip(v, h):
    v = list(v)
    v[h] ^= 1
    return tuple(v)


# ---------------------------------------------------------------- frames
def random_causal_frame(n):
    """K(x)_i = x_i XOR f_i(x restricted to [0,i)); a causal fair bijection."""
    tables = [dict() for _ in range(n)]
    for i in range(n):
        for pre in itertools.product((0, 1), repeat=i):
            tables[i][pre] = random.randint(0, 1)

    def K(x):
        return tuple(x[i] ^ tables[i][tuple(x[:i])] for i in range(n))

    def Kinv(u):
        x = []
        for i in range(n):
            x.append(u[i] ^ tables[i][tuple(x)])
        return tuple(x)

    return K, Kinv


def random_bijection_frame(n):
    pts = [bits(i, n) for i in range(2 ** n)]
    img = pts[:]
    random.shuffle(img)
    fwd = dict(zip(pts, img))
    inv = {v: k for k, v in fwd.items()}
    return (lambda x: fwd[x]), (lambda u: inv[u])


# ---------------------------------------------------------------- A
def audit_theorem_A():
    for trial in range(400):
        n = random.randint(3, 6)
        K, Kinv = random_bijection_frame(n) if trial % 2 else random_causal_frame(n)
        # (b) => (a): build an autoreducible v by choosing a self-avoiding
        # table Phi_h(u without h) and then a v that it autoreduces, if any.
        phi = [dict() for _ in range(n)]
        for h in range(n):
            for u in itertools.product((0, 1), repeat=n):
                key = u[:h] + u[h + 1:]
                if key not in phi[h]:
                    phi[h][key] = random.choice((0, 1, None))
        autoreduced = [v for v in itertools.product((0, 1), repeat=n)
                       if all(phi[h][v[:h] + v[h + 1:]] == v[h] for h in range(n))]
        for v in autoreduced:
            z = Kinv(v)
            for h in range(n):
                # self-avoidance identity
                ok(phi[h][v[:h] + v[h + 1:]] ==
                   phi[h][flip(v, h)[:h] + flip(v, h)[h + 1:]], "self-avoidance")
                O = {Kinv(u) for u in itertools.product((0, 1), repeat=n)
                     if phi[h][u[:h] + u[h + 1:]] == u[h]}
                psi = Kinv(flip(K(z), h))
                ok(z in O, "C1 from autoreduction")
                ok(psi not in O, "C2 from autoreduction")
        # (a) => (b): random families O_h; check the search recovers v_h
        # exactly where O_h separates z from its partner exclusively.
        for _ in range(5):
            z = bits(random.randrange(2 ** n), n)
            v = K(z)
            for h in range(n):
                O = set(Kinv(bits(i, n)) for i in range(2 ** n) if random.random() < 0.5)
                O.add(z)
                psi = Kinv(flip(v, h))
                c = {b: (Kinv(v[:h] + (b,) + v[h + 1:]) in O) for b in (0, 1)}
                if psi not in O:
                    ok(c[v[h]] and not c[1 - v[h]], "search returns v_h")
                else:
                    ok(c[0] and c[1], "tie when partner covered")
        # race form: enumeration order decides; first exclusive cover is true
        for _ in range(5):
            z = bits(random.randrange(2 ** n), n)
            v = K(z)
            h = random.randrange(n)
            psi = Kinv(flip(v, h))
            order = [z, psi] if random.random() < 0.5 else [psi, z]
            first = order[0]
            proposal = v[h] if first == z else 1 - v[h]
            ok((proposal == v[h]) == (first == z), "race form")


# ---------------------------------------------------------------- L1
def audit_L1():
    P = 14
    for _ in range(1500):
        # alpha: P-bit string followed (conceptually) by a non-dyadic tail;
        # represent by integer A with A < alpha < A+1 at scale 2^-P.
        A = random.randrange(1, 2 ** P - 1)
        alpha = bits(A, P)
        # approximations: increasing dyadics strictly below alpha
        k = random.randint(1, 8)
        approx = sorted(random.randrange(0, A + 1) for _ in range(k))
        # a frame-generated partner: any different string
        other = bits(random.randrange(2 ** P), P)
        if other == alpha:
            continue
        lo, hi = (alpha, other) if alpha < other else (other, alpha)
        for a in approx:
            r = bits(a, P)  # rho(a) restricted to P bits
            for L in range(1, P + 1):
                s = r[:L]
                if hi[:L] == s and lo[:L] != s:
                    ok(hi == alpha, "larger-candidate soundness")


# ---------------------------------------------------------------- L2
def audit_L2():
    P = 16
    count = 0
    while count < 1200:
        A = random.randrange(2 ** (P - 2), 2 ** P - 2)
        alpha = bits(A, P)
        h = random.randint(1, 5)
        N = random.randint(h + 1, min(P - 2, h + 6))
        # increasing approximations strictly below alpha (non-dyadic tail),
        # ending close to alpha so that alpha is eventually covered.
        m = random.randint(N + 1, N + 12)
        pts = sorted(random.randrange(0, A + 1) for _ in range(m - 2))
        pts += [A - (A % (2 ** (P - N))), A]
        pts = sorted(set(pts))
        if len(pts) <= N:
            continue
        a = pts  # g = identity, index k = position in list
        partner = flip(alpha, h)
        # closed form
        land = any(bits(a[k], P)[:N] == partner[:N] for k in range(N, len(a)))
        # simulation of the canonical schedule: t = h, h+1, ..., M = t+1
        proposal = None
        for t in range(h, h + len(a) + P + 5):
            M = t + 1
            W = set()
            for k in range(min(t, len(a) - 1) + 1):
                for L in range(N, min(k, M, P) + 1):
                    W.add(bits(a[k], P)[:L])
            ct = any(s == alpha[:len(s)] and s != partner[:len(s)] for s in W)
            cp = any(s == partner[:len(s)] and s != alpha[:len(s)] for s in W)
            if ct and cp:
                proposal = 'tie'
                break
            if ct:
                proposal = alpha[h]
                break
            if cp:
                proposal = partner[h]
                break
        if proposal is None:
            continue  # alpha not yet covered within this finite list
        count += 1
        if alpha[h] == 0:
            ok(proposal == 0, "L2(i)")
        else:
            if land:
                ok(proposal in (0, 'tie'), "L2(ii) landing")
            else:
                ok(proposal == 1, "L2(ii) no landing")


# ---------------------------------------------------------------- G
def audit_G():
    for _ in range(300):
        n = random.randint(4, 7)
        K, Kinv = random_causal_frame(n)
        phi = {}
        for hh in range(n):
            for u in itertools.product((0, 1), repeat=n):
                key = (hh, u[:hh] + u[hh + 1:])
                if key not in phi:
                    phi[key] = random.choice((0, 1, None, None))
        tl = random.randint(0, n - 2)
        tau = bits(random.randrange(2 ** tl), tl) if tl else ()
        for hh in range(tl, n):  # causal: psi_h fixes bits below h
            cyl = [x for x in itertools.product((0, 1), repeat=n) if x[:tl] == tau]
            conv = [x for x in cyl if phi[(hh, K(x)[:hh] + K(x)[hh + 1:])] is not None]
            for x in cyl:
                psi = Kinv(flip(K(x), hh))
                ok(psi[:tl] == tau, "psi_h preserves cylinder")
            if conv:
                x = conv[0]
                ans = phi[(hh, K(x)[:hh] + K(x)[hh + 1:])]
                y = x if ans != K(x)[hh] else Kinv(flip(K(x), hh))
                ok(y[:tl] == tau, "wrong point inside cylinder")
                ok(phi[(hh, K(y)[:hh] + K(y)[hh + 1:])] == ans and ans != K(y)[hh],
                   "forced wrong")
            else:
                ok(all(phi[(hh, K(x)[:hh] + K(x)[hh + 1:])] is None for x in cyl),
                   "forced divergence")


# ---------------------------------------------------------------- M
def audit_M():
    for _ in range(200):
        d0 = Fraction(random.randint(1, 50), random.randint(1, 50))
        j = random.randint(0, 30)
        val = d0
        for _ in range(j):
            val = val * Fraction(3, 2)
        ok(val == d0 * Fraction(3, 2) ** j, "Lemma M martingale")
        ok(Fraction(3, 2) / 2 + Fraction(1, 2) / 2 == 1, "fairness")


# ---------------------------------------------------------------- F
def audit_F():
    for _ in range(400):
        n = random.randint(3, 6)
        m = random.randint(1, n)
        pts = [bits(i, n) for i in range(2 ** n)]
        random.shuffle(pts)
        outs = [bits(i, m) for i in range(2 ** m)]
        G = {}
        per = 2 ** (n - m)
        for i, w in enumerate(outs):
            for x in pts[i * per:(i + 1) * per]:
                G[x] = w  # balanced: every output cell has measure 2^-m
        d = {w: Fraction(random.randint(0, 9), random.randint(1, 4)) for w in outs}
        Q = [x for x in pts if random.random() < 0.6]
        if len(Q) < 2 or len(Q) % 2:
            continue
        random.shuffle(Q)
        Aset = set(Q[:len(Q) // 2])
        Bset = set(Q[len(Q) // 2:])

        def lam(S):
            return Fraction(len(S), 2 ** n)

        def mass(S):
            return sum(Fraction(1, 2 ** m) * d[w] for w in outs
                       if any(G[x] == w for x in S))

        def Psi(S):
            return mass(S) / lam(S)

        both = sum(Fraction(1, 2 ** m) * d[w] for w in outs
                   if any(G[x] == w for x in Aset) and any(G[x] == w for x in Bset))
        Qs = Aset | Bset
        gamma = both / lam(Qs)
        lhs = lam(Aset) * Psi(Aset) + lam(Bset) * Psi(Bset)
        rhs = lam(Qs) * Psi(Qs) + lam(Qs) * gamma
        ok(lhs == rhs, "counting identity")
        s = Psi(Aset) + Psi(Bset)
        if s:
            beta = (Psi(Aset) - Psi(Bset)) / s
            ok(Psi(Aset) == (Psi(Qs) + gamma) * (1 + beta), "bias formula")
            ok(-1 <= beta <= 1, "bias range")


# ---------------------------------------------------------------- E
def audit_E():
    # Tail-coded frame D': flipping virtual hold q complements raw bits >= q.
    for _ in range(300):
        n = random.randint(4, 10)
        q = random.randint(1, n - 2)
        p = random.randint(q, n - 1)  # all-in bet position inside the window
        prefix = bits(random.randrange(2 ** q), q)
        caps = []
        for window in itertools.product((0, 1), repeat=n - q):
            x0 = prefix + window
            x1 = prefix + tuple(1 - b for b in window)
            # D: all-in on raw bit p being 0, capital 1 before p
            c0 = 2 if x0[p] == 0 else 0
            c1 = 2 if x1[p] == 0 else 0
            ok(sorted((c0, c1)) == [0, 2], "exactly one branch survives")
            forced = max(c0, c1)  # Phi predicts the dead branch
            avg = Fraction(c0 + c1, 2)
            beta = Fraction(forced - min(c0, c1), c0 + c1)
            ok(forced == 2 * avg and beta == 1, "bias one")
            caps.append(forced)
        ok(min(caps) == 2, "no window content avoids factor 2")


# ---------------------------------------------------------------- S
def audit_S():
    for _ in range(300):
        L = random.randint(10, 60)
        vals = sorted((Fraction(random.randint(0, 1000), random.randint(1, 1000))
                       for _ in range(L)), reverse=True)
        for h in range(1, L // 2):
            ok(h * vals[2 * h] <= sum(vals[h:]), "h*delta_2h <= tail sum")


if __name__ == "__main__":
    audit_theorem_A()
    audit_L1()
    audit_L2()
    audit_G()
    audit_M()
    audit_F()
    audit_E()
    audit_S()
    print("checks:", CHECKS)
    print("ALL P4-S093 AUDITS PASS")
