# P4-S033 — first one-hole normalization step and the coded-hole obstruction

Date: 2026-10-06
Session: P4-S033
Incoming checkpoint: 1995951e38106e18effb79dcc44e4a96a77c3793
Scope: Phase 4 — Mathematics; sustained one-hole normalization programme
Result: **WIDTH TWO DOES NOT FORCE A RAW COORDINATE HOLE; LITERAL MAP-LEVEL SCAN NORMALIZATION FAILS EVEN FOR A DESTRUCTIVE GLOBAL-k=2 MAP. SAME-SOURCE NORMALIZATION HOLDS FOR OUTPUT-HOMEOMORPHIC ONE-HOLE SCANS UP TO COMPUTABLE SIGNED COORDINATE PERMUTATIONS. R_2 IS INVARIANT UNDER EVERY COMPUTABLE FAIR-COIN-PRESERVING HOMEOMORPHISM, SO R_2=OH REQUIRES HOMEOMORPHISM INVARIANCE OF OH. AN EXPLICIT BLOCKWISE LINEAR SOURCE RECODING TURNS THE P4-S011 DESTROYER INTO A NON-SCAN "CODED-HOLE" DESTROYER AND ISOLATES THE NEXT OBSTRUCTION.**

## Authority, uniqueness and scope

Live `main` matched the requested incoming checkpoint exactly before substantive work and again immediately before the first write. Repository search returned no committed P4-S033 record, so the session identifier was unused.

P4-S001 through P4-S032, the selected CAND-01 authority in `phase2/candidates.json`, `phase4/P4_RESEARCH_PIVOT_AFTER_S031.md`, and `phase4/P4-S032_MATHEMATICS.md` were read. All validated mathematics through P4-S032 is frozen. The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence is not reopened.

This session attacks only the first normalization step selected by P4-S032. It does not decide R_2=OH.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## 1. Retained classes and easy inclusions

Let (mathcal F_2) be the everywhere-total computable fair-coin-preserving Cantor self-maps whose fibres have cardinality at most two. Retain

[
R_2={xin CR:(orall Finmathcal F_2) F(x)in CR}.
]

For a total computable adaptive no-repeat scan (T), write (S_T(x)) for the transcript obtained by successively querying one fresh source coordinate, where the next coordinate is a computable function of the transcript already seen. Say that (T) is **one-hole** if every complete transcript omits at most one source coordinate. Retain

[
OH={xin CR:(orall	ext{ one-hole }T) S_T(x)in CR}.
]

By P4-S032,

[
MLRsubseteq R_2subseteq OHsubsetneq CR.
]

These inclusions are recorded only as inherited facts and are not reproved here.

## 2. What the P4-S007 width-two skeleton does and does not supply

Fix an arbitrary (Finmathcal F_2), (xin CR), (y=F(x)), and a computable martingale (d) succeeding on (y).

P4-S007 supplies a computable nondecreasing sampling function (c(n)) and coherent sets

[
P_n(y)subseteq 2^n,qquad 1leq |P_n(y)|leq 2,
]

whose infinite paths are exactly (F^{-1}(y)). Thus every sampled inverse state contains at most one **binary cohort choice**.

The missing step is stronger: a one-hole scan does not merely have two possible source prefixes. Its two possible preimages, when there are two, differ in one raw source coordinate.

### Lemma 1 — coordinate locality of one-hole scan double fibres

Let (T) be a total computable adaptive no-repeat one-hole scan. If

[
S_T^{-1}(z)={u,v}
]

has two points, then there is exactly one source coordinate (j) omitted by the transcript (z), and (u) and (v) agree at every coordinate other than (j). In particular their Hamming distance is one.

**Proof.** The transcript fixes the value of every queried coordinate. P4-S032's scan fibre calculation identifies the fibre with all assignments to omitted coordinates. A double fibre therefore has exactly one omitted coordinate, and the two assignments differ only there. ∎

### Consequence

Width two is not the same as one raw hole. For a general global-k=2 map, the two nodes in (P_n(y)) may differ at many coordinates. P4-S007 says that those differences are controlled by one binary inverse choice, but it does not canonically localize that choice at a single coordinate.

P4-S002 already exhibits this geometrically: the exceptional double fibre of its collision map is ({0^omega,1^omega}), whose two points differ at every coordinate. That particular map is safe because its ambiguity locus is null, but it shows that the inverse skeleton alone cannot force a scan presentation.

This is the first exact obstruction to a direct skeleton-to-scan conversion.

## 3. (R_2) is invariant under computable fair-coin homeomorphisms

Let (mathcal H) be the class of computable fair-coin-preserving Cantor homeomorphisms. By P4-S001 every (Hinmathcal H) has a computable fair-coin-preserving inverse and preserves computable randomness in both directions.

### Theorem 2 — homeomorphism invariance of (R_2)

For every (Hinmathcal H),

[
xin R_2quadLongleftrightarrowquad H(x)in R_2.
]

**Proof.** Suppose (xin R_2), and let (Finmathcal F_2). Then (Fcirc H) is everywhere total, computable and fair-coin preserving. Since (H) is bijective,

[
|(Fcirc H)^{-1}(z)|=|F^{-1}(z)|leq2.
]

Hence ((Fcirc H)(x)=F(H(x))) is computably random. Thus (H(x)in R_2). Apply the same argument to (H^{-1}) for the converse. ∎

This invariance is automatic for the arbitrary-map class (R_2), but not from the definition of (OH), whose observer is tied to raw source coordinates.

## 4. The homeomorphism closure of one-hole robustness

Define

[
OH^{iso}={xin CR:(orall Hinmathcal H) H(x)in OH}.
]

Equivalently, (xin OH^{iso}) exactly when every map of the form (S_Tcirc H), with (T) a one-hole scan and (Hinmathcal H), preserves computable randomness on (x). Postcomposition by a computable fair-coin homeomorphism is immaterial by P4-S001.

### Proposition 3 — exact intermediate class

[
MLRsubseteq R_2subseteq OH^{iso}subseteq OHsubsetneq CR.
]

Moreover,

[
OH^{iso}=OH
]

if and only if (OH) is invariant under every computable fair-coin-preserving homeomorphism.

**Proof.** If (xin R_2), Theorem 2 gives (H(x)in R_2subseteq OH) for every (H), so (xin OH^{iso}). The identity homeomorphism gives (OH^{iso}subseteq OH). The remaining inherited inclusions come from P4-S032. The last equivalence is immediate from the definition. ∎

### Corollary 4 — a necessary test for (R_2=OH)

If (R_2=OH), then (OH) is invariant under every computable fair-coin-preserving homeomorphism.

Conversely, if there are (xin OH) and (Hinmathcal H) with (H(x)
otin OH), then

[
xin OHsetminus R_2,
]

so (R_2
eq OH).

**Proof.** Equality transfers Theorem 2's invariance to (OH). For the converse, if (xin R_2), Theorem 2 would give (H(x)in R_2subseteq OH), contradiction. ∎

Thus the normalization problem has a precise first invariant test: **can one-hole robustness survive a computable measure-preserving recoding of the source coordinates?**

## 5. Positive subclass: signed coordinate permutations

Not every source homeomorphism causes a problem. Let (pi) be a computable permutation of (omega) and (ain2^omega) a computable bit sequence. Define

[
H_{pi,a}(x)(n)=x(pi(n))oplus a(n).
]

This is a computable fair-coin-preserving homeomorphism.

### Theorem 5 — (OH) is invariant under signed coordinate permutations

For every (H_{pi,a}),

[
xin OHquadLongleftrightarrowquad H_{pi,a}(x)in OH.
]

More strongly, from a one-hole scan (T) and a computable martingale (d) succeeding on

[
S_T(H_{pi,a}(x))
]

one can uniformly construct a one-hole scan (T') on the same raw source (x) and a computable martingale (e) succeeding on (S_{T'}(x)).

**Construction.** Maintain the virtual transcript (v) that (T) would see on (H_{pi,a}(x)). If (T), from (v), asks virtual coordinate (q), let (T') ask raw coordinate (pi(q)). If the observed raw bit is (b), append (boplus a(q)) to (v).

No coordinate is repeated because (pi) is a permutation. The raw omitted set is the (pi)-image of the virtual omitted set, so the one-hole condition is preserved.

For a finite raw transcript (z), let (v(z)) be the computably reconstructed virtual transcript and put

[
e(z)=d(v(z)).
]

At each node the two children of (z) are either sent to the two children of (v(z)) in the same order or swapped according to the known bit (a(q)). Hence the martingale equality is preserved exactly. Along (x), (e)'s capital equals (d)'s capital stage by stage. ∎

### Corollary 6 — a nontrivial positive normalization subclass

Suppose

[
F=Kcirc S_Tcirc H_{pi,a},
]

where (Kinmathcal H), (T) is a total computable one-hole no-repeat scan, and (H_{pi,a}) is a signed coordinate permutation. If (xin CR) and (F(x)
otin CR), then an explicitly constructed one-hole scan on the **same source (x)** destroys computable randomness.

**Proof.** P4-S001 removes the output homeomorphism (K): (S_T(H_{pi,a}(x))) is non-computably-random. Apply Theorem 5. ∎

This subclass is genuinely broader than already having a literal scan presentation. For example, take the left-shift one-hole scan and postcompose its transcript by the computable pairwise XOR homeomorphism

[
K(z)_{2m}=z_{2m}oplus z_{2m+1},qquad
K(z)_{2m+1}=z_{2m+1}.
]

The first output bit of the composite depends on two source coordinates, so the composite is not itself a scan, while Corollary 6 still normalizes every destruction witness in this class.

Therefore **multi-coordinate Boolean output mixing is not by itself the obstruction** when that mixing is an invertible computable postprocessing.

## 6. A destructive non-scan coded-hole conjugate

The obstruction becomes exact when the recoding occurs on the **source side**.

Let (D) be the settled P4-S011 one-hole scan destroyer, and let (Yin CR) be its settled vulnerable source, so

[
D(Y)
otin CR.
]

Define a blockwise linear homeomorphism (H) on triples. For each block ((x_0,x_1,x_2)), put

[
u_0=x_0oplus x_2,qquad
u_1=x_0oplus x_1,qquad
u_2=x_0oplus x_1oplus x_2.
]

Its inverse is

[
x_0=u_0oplus u_1oplus u_2,qquad
x_1=u_0oplus u_2,qquad
x_2=u_1oplus u_2.
]

Apply this same invertible linear transformation independently to every successive three-coordinate block. Then (H) and (H^{-1}) are computable fair-coin-preserving homeomorphisms.

Set

[
F=Dcirc H,qquad X=H^{-1}(Y).
]

### Theorem 7 — exact destructive coded-hole map

The pair ((F,X)) satisfies:

1. (X) is computably random;
2. (F) is everywhere-total, computable and fair-coin preserving;
3. every fibre of (F) has size at most two;
4. (F(X)=D(Y)) is not computably random;
5. every double fibre of (F) consists of two raw source points differing in at least two coordinates.

Consequently (F) is not a one-hole scan. More strongly, no representation

[
F=Kcirc S
]

is possible with (K) an output homeomorphism and (S) a one-hole scan.

**Proof.** Items 1–4 follow from P4-S001 and from composition with the bijection (H). Specifically,

[
F^{-1}(z)=H^{-1}(D^{-1}(z)),
]

so fibre cardinalities are unchanged.

For item 5, every double fibre of the scan (D) differs in exactly one (u)-coordinate by Lemma 1. Flipping (u_0) in one triple flips (x_0,x_1); flipping (u_1) flips (x_0,x_2); flipping (u_2) flips all three. Thus the inverse image under (H) of a unit-coordinate difference has Hamming weight respectively (2,2,3). Hence every double fibre of (F) differs in at least two raw coordinates.

A one-hole scan can have only Hamming-distance-one double fibres by Lemma 1, so (F) is not a scan. If (F=Kcirc S) with (K) bijective, then (F) and (S) have exactly the same source fibres, giving the same contradiction. ∎

This is stronger than using P4-S002's safe collision map: it is an **exact destructive global-k=2 witness** outside the literal/output-homeomorphic scan class.

It does **not** separate (R_2) from (OH). The same source (X) might still be vulnerable to some different one-hole scan. Proving or refuting that possibility is now the central issue.

## 7. Null ambiguity check

P4-S032's null-ambiguity theorem is consistent with Theorem 7 and gives an additional check. Since (F) destroys computable randomness, its output ambiguity locus has positive fair-coin measure.

Indeed source precomposition by a bijection does not change the output fibres' cardinalities, so

[
A_F=A_D.
]

P4-S032 already forces (lambda(A_D)>0). No claim is made that this positive mass is the operative invariant.

## 8. Exact obstruction isolated

The first normalization step separates three notions:

1. **binary inverse cohort:** forced for every global-k=2 map by P4-S007;
2. **raw coordinate hole:** forced by a one-hole scan on every double fibre;
3. **coded hole:** one binary cohort spread across several raw coordinates by a computable fair-coin homeomorphism.

The width-two skeleton supplies item 1, not item 2. Output-side invertible Boolean mixing is harmless. Source-side recoding can turn the exact P4-S011 destroyer into item 3 while preserving k=2, measure preservation and destruction.

The remaining source-level question is therefore not whether every destructive map literally is a scan. That is false by Theorem 7. It is whether **coded one-hole vulnerability always implies raw one-hole vulnerability of the same source**.

Equivalently, a necessary first test for (R_2=OH) is whether (OH) is invariant under computable fair-coin-preserving homeomorphisms. The simplest genuinely non-coordinate test case is the explicit blockwise three-bit linear (H) above.

## 9. Selection for P4-S034

The next bounded attack should test homeomorphism invariance of (OH), beginning with the explicit three-bit linear coded-hole homeomorphism.

At the P4-S012 stake level, start from a one-hole scan/stake witness destroying (H(x)) and test whether it can be compiled into a raw-coordinate self-avoiding stake/scan witness on (x). A positive theorem should enlarge Theorem 5 beyond signed permutations. A negative theorem must exhibit a computably random (xin OH) with (H(x)
otin OH); by Corollary 4 that would immediately prove (R_2subsetneq OH).

This stays on the sustained one-hole normalization programme and does not return to the frozen bankroll line.

## Guards

- All validated mathematics through P4-S032 is preserved.
- P4-S011 and the P4-S032 distinction between static final ambiguity and renewable temporal ambiguity are preserved.
- The P4-S015–P4-S031 ticket/reserve/frontier/recycling line remains frozen as the default trajectory.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- DEF-0020 is unchanged.
- No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.
- Phase 4 remains OPEN and Phase 5 CLOSED.
