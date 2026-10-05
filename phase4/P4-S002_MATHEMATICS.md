# P4-S002 — k=2 finite-valued inverse boundary

Date: 2026-10-05
Session: P4-S002
Incoming checkpoint: 834d945b0f3796906f0d9e93cd3e1369e252d866
Scope: Phase 4 — Mathematics; selected CAND-01 only; first genuinely non-injective case k=2
Result: **K2 FORCES EFFECTIVE CLOSED-FIBRE APPROXIMATION, NOT TOTAL COMPUTABLE FIBRE ENUMERATION; GENERAL COMPUTABLE-RANDOMNESS PRESERVATION REMAINS UNRESOLVED**

## Authority, uniqueness and scope

Live main matched the incoming checkpoint exactly before substantive work. The committed phase4 directory contained only P4-S001 records, repository code search returned no P4-S002 record, and authoritative state named P4-S002 only as the next session. P4-S002 was therefore unused.

Gate 3 is PASS and Phase 4 is OPEN for selected CAND-01. Phase 5 remains CLOSED. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The Gate-3 guard is preserved as a historical pre-Phase-4 statement: before Phase 4, no computable-randomness consequence of the bare global finite-cardinality fibre bound had been established.

P4-S001 is used only as a boundary condition. Its exact k=1 result remains unchanged: injectivity forces a computable fair-coin-preserving homeomorphism with computable inverse, and SRC-0015 / THM-0038 gives computable-randomness invariance; no class-wide inverse-use bound is forced.

This session investigates k=2 only. It makes no claim for arbitrary k>2, novelty, openness, Gate 4, publication or outreach. DEF-0020 is unchanged.

## Exact k=2 hypotheses

Let lambda be fair-coin measure on Cantor space. Let F:2^omega -> 2^omega be everywhere-total computable, lambda-preserving, and satisfy |F^{-1}(y)| <= 2 for every y. No selector, fibre enumeration, inverse branch or disintegration is assumed.

## Forced information

### Lemma 1 — surjectivity still holds

Every such F is onto.

**Proof.** F is continuous, so its compact range is closed. If y were outside the range, some nonempty basic cylinder [tau] containing y would miss the range. Then F^{-1}([tau]) is empty, contradicting lambda(F^{-1}([tau]))=lambda([tau])>0. This argument does not use k=2. ∎

### Lemma 2 — every fibre has a uniform descending clopen name

From a Type-2 program for F one can compute a forward-use bound u_F(m) exactly as in P4-S001. Hence, uniformly from a finite word tau of length m, one can compute the clopen set F^{-1}([tau]) as a finite union of length-u_F(m) input cylinders.

For y in 2^omega put A_m(y)=F^{-1}([y↾m]). Then uniformly in y:

1. A_{m+1}(y) is contained in A_m(y);
2. A_m(y) is nonempty clopen;
3. lambda(A_m(y))=2^{-m};
4. F^{-1}(y)=intersection_m A_m(y), which has one or two points.

Thus k=2 forces an effective negative/compact approximation to the inverse fibre even though it does not yet choose its elements.

### Lemma 3 — a fibre point is computable from y once an isolating input prefix is supplied

Fix y and x in F^{-1}(y). Because the fibre has at most two points, some finite prefix sigma of x isolates it inside the fibre: F^{-1}(y) intersection [sigma] = {x}.

Given y and such a sigma, x is computable. For requested length r, compute the descending clopen sets A_m(y) and search for m such that the nonempty clopen set A_m(y) intersection [sigma] lies inside one r-cylinder [rho]. Containment of finite clopen unions is decidable, and compactness plus the singleton intersection guarantees that such an m eventually appears. Then rho=x↾r.

The missing uniform datum is therefore not an approximation to the whole fibre; it is an effective way to choose/isolate a persistent sheet.

## Sharp counterexample mechanism — one double fibre already destroys global branch continuity

Let a=0^omega, b=1^omega, and c=0^omega, where a,b are domain points and c is the distinguished output point. For n>=0 define

C_{n,0}=[0^{n+1}1],   C_{n,1}=[1^{n+1}0],

and

D_{n,0}=[0^n10],      D_{n,1}=[0^n11].

The C_{n,i} partition the domain except for {a,b}; the D_{n,i} partition the codomain except for {c}; and corresponding cylinders have the same measure 2^{-(n+2)}.

Define F_* by

F_*(a)=F_*(b)=c,

F_*(0^{n+1}1 z)=0^n10 z,

F_*(1^{n+1}0 z)=0^n11 z.

### Lemma 4 — F_* satisfies the exact k=2 hypotheses

F_* is everywhere-total computable, fair-coin preserving, and has fibres of size at most two.

**Computability/continuity.** On each C_{n,i}, F_* is a same-length prefix replacement followed by the identity on the tail. To determine the first m output bits, it is enough to inspect the first m+1 input bits: if the first change of the initial constant bit has not occurred, the first m output bits are 0; otherwise the relevant prefix replacement and tail are already determined. At a and b, longer constant input prefixes map to longer zero output prefixes, so continuity holds there as well.

**Measure preservation.** Each prefix replacement C_{n,i}->D_{n,i} is a measure-preserving homeomorphism between equal-measure cylinders. The exceptional sets {a,b} and {c} have measure zero. Since the two cylinder families partition the complements of those null sets, lambda(F_*^{-1}(B))=lambda(B) for every Borel B.

**Fibres.** F_*^{-1}(c)={a,b}. Every y!=c belongs to exactly one D_{n,i} and has exactly one preimage obtained by reversing the corresponding prefix replacement. ∎

### Theorem 5 — total computable selection and total computable two-branch enumeration are not forced at k=2

There is no continuous, hence no everywhere-total computable, function G with F_*(G(y))=y for every y.

For n>=0 let

y_n^0=0^n10 0^omega,   y_n^1=0^n11 1^omega.

Both sequences converge to c. Their unique preimages are respectively

x_n^0=0^{n+1}1 0^omega -> a,

x_n^1=1^{n+1}0 1^omega -> b.

A right inverse is forced to take G(y_n^0)=x_n^0 and G(y_n^1)=x_n^1. But G(c) must be either a or b, so G is discontinuous along one of these two sequences.

Stronger still, there are no two continuous total functions G_0,G_1 whose values enumerate each fibre, even allowing duplication on singleton fibres: {G_0(y),G_1(y)}=F_*^{-1}(y). For y!=c the fibre is a singleton, so both G_i are forced to equal its unique inverse there; each therefore inherits the same discontinuity at c.

Consequently, the exact CAND-01 k=2 hypotheses do **not** force global computable inverse branches or an everywhere-total computable finite list of the fibre.

## Why this does not yet give a randomness counterexample

The same F_* has an a.e.-computable inverse G on 2^omega\{c}. Given y!=c, wait for its first 1, inspect the next bit, and reverse the corresponding prefix replacement. Its domain has measure one, F_*∘G=id there, and G∘F_*=id outside the null set {a,b}. Since F_* pushes lambda to lambda, G also pushes lambda to lambda.

Therefore the already-catalogued SRC-0015 / THM-0038 applies to the pair (F_*,G): **F_* preserves computable randomness in both directions on random points.**

This is the key boundary: failure of an everywhere-total selector is real, but by itself it is too weak to imply failure of computable-randomness preservation.

## A second k=2 boundary example — persistent double fibres can also preserve computable randomness

Let S(bz)=z be the one-bit left shift. S is everywhere-total computable, fair-coin preserving and exactly two-to-one. It has two computable branches y->0y and y->1y, but no single right inverse can satisfy G∘S=id almost everywhere: a selector chooses only one of the two equally weighted first-bit preimages in each fibre, so its selected image has measure 1/2.

Nevertheless S preserves computable randomness directly. If d is a computable martingale succeeding on S(x), define e by e(empty)=d(empty), and e(b sigma)=d(sigma) for b in {0,1}. Then e is a computable martingale and succeeds on x. Thus non-randomness of S(x) would imply non-randomness of x.

So even within k=2 there are at least two different positive mechanisms:
- F_*: no total branch enumeration, but an a.e. inverse pair gives THM-0038;
- S: global computable branches exist, no single a.e. inverse identity exists, but a direct martingale lift gives preservation.

## Precise obstruction isolated in P4-S002

The k=1 proof relied on pairwise disjoint images of same-level input cylinders and effective finite separation. At k=2 those compact images may overlap because two genuinely different input points may share an output. The fibre is still uniformly available as a descending sequence of computable clopen sets, but that negative information does not uniformly choose a persistent component.

F_* makes the obstruction exact: two inverse sheets can collide at one output point in a way that forces every total selector/listing to be discontinuous. Hence the bare cardinal bound cannot be silently upgraded to total effective inverse branches.

What P4-S002 does **not** establish is whether every k=2 map has some weaker a.e.-effective sheet decomposition, weighted inverse structure, or direct martingale-transfer construction sufficient to preserve computable randomness. The forced descending-clopen fibre name has not been proved sufficient for that purpose, and no k=2 randomness-destruction counterexample is produced here.

## Failed / abandoned approaches

1. **Reuse the k=1 image-separation proof.** It fails because same-level cylinder images may legitimately overlap at outputs with two preimages.
2. **Choose the lexicographically least preimage.** F_* refutes this as a general computable strategy: off c the selector is forced, and the two approach directions make any choice at c discontinuous.
3. **Infer randomness failure from nonexistence of total branches.** F_* blocks this inference because it has an a.e.-computable measure-preserving inverse and therefore preserves computable randomness by THM-0038.
4. **Treat THM-0038 as the universal k=2 route.** The shift S preserves computable randomness but no single selector can be an a.e. inverse identity, so a general proof—if true—must allow a different mechanism.
5. **Promote the descending clopen fibre name to an exact effective enumeration.** The present lemmas give negative compact information and isolation-with-advice only; no uniform method for choosing the persistent sheet is established.

## Proof dependencies and guards

New programme mathematics in this session uses only elementary effective compactness/continuity on Cantor space, fair-coin cylinder measure, and the computable-martingale definition DEF-0004. The randomness conclusion for F_* alone uses the already statement-inspected SRC-0015 / THM-0038. No new literature theorem is imported.

- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- The Gate-3 no-consequence statement remains preserved as the pre-Phase-4 baseline.
- P4-S001 is unchanged exactly.
- No general k=2 computable-randomness preservation or failure theorem is claimed.
- No result is claimed for k>2.
- DEF-0020 and all source/convention guards are unchanged.
- Catalogue records are unchanged.
- Gate 4 is not reviewed. Phase 5 remains CLOSED.
