"""Small exact finite audit of the variable/nonconsecutive block boundary.

No infinitary randomness or compactness claim is certified by this script.
Run with: python phase4/P4-S101_BOUNDARY_AUDIT.py
"""
from fractions import Fraction as F
from itertools import product

checks = 0


def check(p):
    global checks
    assert p
    checks += 1


bits = list(product((0, 1), repeat=8))
blocks = ((0, 3, 7), (1, 4), (2, 5, 6))


def recode(x):
    y = list(x)
    for j, b in enumerate(blocks):
        u = sum(x[k] << s for s, k in enumerate(b))
        if j < 2:
            v = (3 * u + 1) % (1 << len(b))
            for s, k in enumerate(b):
                y[k] = (v >> s) & 1
        else:
            a, c, d = (x[k] for k in b)
            y[b[0]], y[b[1]], y[b[2]] = a ^ d, c ^ d ^ (a & d), d
    return tuple(y)


check(len({recode(x) for x in bits}) == 256)


def scan_prefix(v, t):
    # Query 0 first, then all but a transcript-selected final hole.
    hole = 6 if v[0] else 7
    order = [0] + [q for q in (5, 2, 4, 1, 7, 6, 3) if q != hole]
    return tuple(v[q] for q in order[:t])


def capital(w):
    c = F(1)
    for s, b in enumerate(w):
        theta = F((-1) ** s * (s % 3 + 1), 5)
        c *= 1 + theta * (2 * b - 1)
    return c


def engine(cells, sigma, k=None):
    scale = 2 ** len(sigma)
    total = F(0)
    split = F(0)
    mean = F(0)
    for w, xs in cells.items():
        compatible = [x for x in xs if all(x[q] == b for q, b in sigma.items())]
        weight = F(1, 2 ** len(w)) * capital(w)
        if compatible:
            total += weight * scale
        if k is not None and {x[k] for x in compatible} == {0, 1}:
            split += weight * scale
        mean += F(len(compatible), 256) * capital(w) * scale
    return total, split, mean


def cells_at(t, raw=False):
    cells = {}
    for x in bits:
        w = scan_prefix(x if raw else recode(x), t)
        cells.setdefault(w, []).append(x)
    check(len(cells) == 2 ** t)
    check(all(len(xs) == 2 ** (8 - t) for xs in cells.values()))
    return cells


states = [{}] + [{q: b} for q in range(8) for b in (0, 1)]
states += [{0: a, 5: b} for a, b in product((0, 1), repeat=2)]
for raw in (False, True):
    all_cells = [cells_at(t, raw) for t in range(8)]
    for sigma in states:
        last = None
        for cells in all_cells:
            psi, _, mean = engine(cells, sigma)
            check(mean <= psi)
            if last is not None:
                check(psi <= last)
            last = psi
            for k in range(8):
                if k in sigma:
                    continue
                _, gamma, _ = engine(cells, sigma, k)
                p0 = engine(cells, sigma | {k: 0})[0]
                p1 = engine(cells, sigma | {k: 1})[0]
                check((p0 + p1) / 2 == psi + gamma)
        # At t=7 every virtual block is entirely inside the tested frontier 8.
        candidates = [k for k in ((0, 1, 2) if not raw else range(8)) if k not in sigma]
        psi = engine(all_cells[7], sigma)[0]
        check(sum((engine(all_cells[7], sigma, k)[1] for k in candidates), F(0)) <= psi)

# Dropping distinct-block condition is genuinely unsafe: two raw candidates
# in the same mixed block both split on the branch holding virtual coordinate 6.
mixed = cells_at(7)
# Restrict to first virtual bit 1, so ONLY the coordinate-6 hold branch remains.
branch = {w: xs for w, xs in mixed.items() if w[0] == 1}
check(engine(branch, {}, 2)[1] == engine(branch, {})[0])
check(engine(branch, {}, 6)[1] == engine(branch, {})[0])
check(engine(branch, {}, 2)[1] + engine(branch, {}, 6)[1] > engine(branch, {})[0])

for i in range(12):
    ell, n = 2 * i + 2, 2 ** (i + 4) * (2 * i + 2)
    check(F(1, 2 ** (i + 2)) + F(2 * ell, n) < F(2, 2 ** i))
    check((i + 1) * (i + 2) - (i + 1) == (i + 1) ** 2)
    check(F(2 ** (i + 1), 2 ** ((i + 1) * (i + 2))) <= F(1, 2 ** i))
for q in range(8):
    for m in range(1, 12):
        if m * m - m >= 2 * q + 4:
            check(m * (m + 1) - q >= q + 2 * m + 4)
check(F(1, 16) * 2 * 1 == F(1, 8))
check(4 * (1 - F(1, 8)) == F(7, 2) > 2)
print(f'PASS: {checks} exact finite block/refinement/budget checks; no infinitary certification')
