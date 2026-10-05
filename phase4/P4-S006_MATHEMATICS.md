# P4-S006 — canonical lexicographic two-sheet complexity

Date: 2026-10-05
Session: P4-S006
Incoming checkpoint: b5881ac82a636c03c0b7c3ad9d6a36b5b47de123
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 only
Result: **THE CANONICAL LEXICOGRAPHIC SHEETS ARE EFFECTIVE BOREL / BAIRE-1 BUT NEED NOT HAVE COMPUTABLE MASS; THIS DOES NOT SUPPLY A COMPUTABLE-RANDOMNESS TRANSFER; A ONE-HOLE ROTATING-MASK COMPLETION STILL COLLAPSES WHEN A MASKED BET IS REVEALED; GENERAL k=2 PRESERVATION/FAILURE REMAINS UNRESOLVED**

## Authority, uniqueness and scope

Live `main` matched the incoming checkpoint exactly before substantive work, and repository search returned no committed P4-S006 record. P4-S006 was therefore unused.

Gate 3 is PASS and Phase 4 is OPEN for selected CAND-01. Phase 5 remains CLOSED. P4-S001 through P4-S005 are preserved exactly. This session stays strictly at k=2. P4-S005's negative stopping result is treated as settled: no attempt is made to recover computability of the P4-S004 low-weight crossing measures.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard remains historical. DEF-0020 and all catalogue/source convention guards are unchanged. No k>2, novelty/open-status, Gate-4, publication or outreach claim is made.

## Exact k=2 setting

Let lambda be fair-coin measure and let
\[
F:2^\omega\to2^\omega
\]
be everywhere-total computable, lambda-preserving, and satisfy
\[
|F^{-1}(y)|\le 2
\]
for every y.

By P4-S002/P4-S003, F is onto and for each output y its fibre is a nonempty one- or two-point compact set with uniformly computable clopen approximants
\[
A_m(y)=F^{-1}([y\upharpoonright m]).
\]

Write < for lexicographic order on Cantor space.

## Lemma 1 — the collision relation is effectively closed

Define
\[
R_F=\{(x,z):F(x)=F(z)\}.
\]

Then R_F is a uniformly effective closed (Pi^0_1) subset of \(2^\omega\times2^\omega\).

**Proof.** Inequality of two Cantor outputs is semidecidable by finding their first differing bit. Equivalently,
\[
R_F=\bigcap_m\{(x,z):F(x)\upharpoonright m=F(z)\upharpoonright m\}.
\]
For each fixed m, total computability of F gives a finite source use, so the displayed equality set is computable clopen. The intersection is therefore effectively closed. ∎

For every finite source string rho, the image
\[
K_\rho=F([\rho])
\]
is computably compact and hence uniformly effectively closed.

## Lemma 2 — exact effective complexity of the canonical source sheets

Assign every singleton fibre to the lower sheet and, on each double fibre, put its lexicographically smaller point on the lower sheet and its larger point on the upper sheet. Thus
\[
U=\{x:\exists z<x\;F(z)=F(x)\},
\qquad
L=2^\omega\setminus U.
\]

Then:

1. \(U\) is uniformly effective \(F_\sigma\), i.e. Sigma^0_2;
2. \(L\) is uniformly effective \(G_\delta\), i.e. Pi^0_2;
3. \(F|L\) is injective and meets every fibre exactly once;
4. \(F|U\) is injective and meets exactly the double fibres once.

More explicitly,
\[
U=\bigcup_{\rho\in2^{<\omega}}
\Bigl([\rho1]\cap F^{-1}(K_{\rho0})\Bigr).
\]

**Proof.** If x has a smaller colliding point z, let rho be their common prefix immediately before their first differing bit. Then z is in [rho0], x is in [rho1], and F(x) belongs to K_{rho0}. Conversely, membership in one displayed term supplies a smaller colliding point in [rho0]. Each K_{rho0} is effectively closed, its preimage under computable F is effectively closed, and intersecting with [rho1] preserves that complexity. Taking the effective countable union gives Sigma^0_2. The complement is Pi^0_2.

Because every fibre has at most two elements, there is exactly one lexicographic minimum in every fibre and at most one nonminimum point. The injectivity statements follow. ∎

The double-fibre output set
\[
D=\{y:|F^{-1}(y)|=2\}
\]
is also effective \(F_\sigma\):
\[
D=\bigcup_{\rho\in2^{<\omega}} K_{\rho0}\cap K_{\rho1}.
\]
Indeed, two distinct preimages first separate at some rho.

## Lemma 3 — the canonical inverse selectors are effective Baire class 1

Define total selectors
\[
g_-(y)=\min_{\rm lex}F^{-1}(y),
\qquad
g_+(y)=\max_{\rm lex}F^{-1}(y).
\]
They agree on singleton fibres and are the two different inverse points on double fibres.

For each m, let a_m(y) be the lexicographically least point of the computable clopen set A_m(y), and let b_m(y) be its lexicographically greatest point. Then a_m and b_m are uniformly computable continuous functions, depending only on y↾m, and
\[
a_m(y)\to g_-(y),\qquad b_m(y)\to g_+(y)
\]
for every y.

Hence g_- and g_+ are uniformly effective Baire-1 / pointwise-limit-computable selectors. No computable convergence modulus is forced.

Their graphs have the corresponding effective Borel descriptions. In particular,
\[
\operatorname{graph}(g_-)
=\{(y,x):F(x)=y\ \&\ x\in L\}
\]
is Pi^0_2. The partial upper-sheet inverse
\[
h(y)=g_+(y)\quad(y\in D)
\]
has Sigma^0_2 graph
\[
\{(y,x):F(x)=y\ \&\ \exists z<x\;F(z)=y\}.
\]

**Proof of convergence.** The A_m(y) are nested nonempty compact sets with intersection F^{-1}(y). At any requested input precision n, compactness implies that sufficiently deep A_m(y) contain no n-prefix lying strictly to the left of the minimum fibre point and no n-prefix lying strictly to the right of the maximum fibre point. Thus the least and greatest clopen choices stabilize at each coordinate to the two canonical fibre points. ∎

This Baire-1 upper bound is genuinely stronger than continuity but cannot in general be lowered to continuity/computability: P4-S002's one-collision map forces any total inverse selector to be discontinuous at the collision output.

## Lemma 4 — the canonical sheets need not have computable mass

The P4-S005 prefix-code map already gives a sharp obstruction, without reusing its crossing-measure argument.

Recall its computable global first-bit split [0],[1], its prefix-free blocks T_e of measure
\[
q_e=4^{-(e+1)},
\]
and the fixed c.e. noncomputable set K controlling activation.

For the **canonical lexicographic** partition above, every sheet-1 point is the upper point before activation. On an activated block, exactly the local sheet-1 source half with code prefix 1 is sent to singleton fibres, so that half moves from the canonical upper sheet U to the lower sheet L. The source mass removed from U in activated block e is therefore
\[
\frac12\lambda([1t_e])=\frac14 q_e.
\]

Consequently
\[
\lambda(U)=\frac12-\frac14\sum_{e\in K}4^{-(e+1)},
\]
and
\[
\lambda(L)=\frac12+\frac14\sum_{e\in K}4^{-(e+1)}.
\]

The same base-4 gap argument already used in P4-S005 shows that these masses are noncomputable. Therefore the finite measures
\[
\lambda\!\upharpoonright U,\qquad \lambda\!\upharpoonright L
\]
are not uniformly computable, and neither are their unnormalized pushforwards under F, since their total masses are preserved.

This example is still in P4-S003's positive computable-clopen-split regime and still preserves computable randomness. It is used here only to calibrate the effective complexity of the **canonical** split.

## Consequence — canonical Borel sheets do not supply the missing computable transfer

The lexicographic construction gives real inverse information beyond the two-prefix lists, but at the wrong effective level for the available computable-randomness transfer mechanisms.

1. **No effective-isomorphism route.** The canonical selectors are only effective Baire-1 in general; P4-S002 already refutes total continuous/computable selection.
2. **No computable component-measure route.** Lemma 4 shows that even the total masses of the canonical lower/upper source components can be noncomputable. Thus P4-S003's computable-sheet conditioning argument cannot be run uniformly on the canonical sheets.
3. **No branch-label-free normalization from this split.** Any purported uniform procedure producing computable canonical component measures would compute lambda(U) in the P4-S005 example, contradicting Lemma 4.
4. **No repair of P4-S004 fixed-stage incoherence.** The continuous approximants a_m,b_m have no computable stabilization modulus. Using the currently guessed canonical branch therefore yields, at best, a limit-computable branch choice; it does not turn the uniformly computable family of fixed-stage pullbacks e_m into one computable succeeding source martingale.

Accordingly, the canonical lexicographic/Borel assignment does **not** close the k=2 computable-randomness transfer problem without additional effective information. This is a failure of this transfer route, not a proof that no different preservation theorem exists.

## One-hole / rotating-mask witness route

The requested negative alternative was pursued only after the canonical split failed to close the transfer.

The SRC-0061 idea would like to interleave genuine nonmonotonic betting bits with filler information while leaving at most one global source bit unresolved. A natural repair is a one-hole mask: keep one hidden bit h and output filler relations such as
\[
c_j=x_j\oplus h
\]
instead of x_j itself.

### Lemma 5 — revealing one masked betting coordinate collapses a one-hole cohort

Suppose a transcript already contains c_j=x_j xor h for every j in a set J. If a later genuine betting step must output x_j in the clear for some j in J, then the transcript immediately determines
\[
h=c_j\oplus x_j
\]
and hence every other
\[
x_k=c_k\oplus h,\qquad k\in J.
\]

Thus all remaining masked coordinates in that cohort become pre-revealed at once. Replacing h afterwards by a fresh hidden bit cannot make those already determined old coordinates unknown again.

The same obstruction is not specific to XOR. Whenever the current filler state leaves exactly two possible assignments to previously processed coordinates, revealing any coordinate on which the two assignments differ identifies which assignment is actual and thereby reveals every other coordinate on which the two assignments differ.

### Consequence for SRC-0061 reuse

A rotating single hole therefore does not globally resolve the P4-S003/P4-S005 pre-revealed-bet obstruction. If two later genuine betting positions have previously been compressed into the same two-way ambiguity, revealing the first can disclose the second before its bet. The unrestricted adaptive scan from SRC-0061 gives no committed guarantee preventing that situation.

A more elaborate construction could postpone compression and allow many finite-prefix possibilities while still arranging final fibres of size at most two. P4-S006 does not rule that out. No such delayed-coalescence construction was completed here.

Hence no exact total computable fair-coin-preserving k=2 map with a computably random source and non-computably-random image is established in this session.

## Successful and failed mechanisms

Successful:

1. Exact effective-closed complexity of the collision relation.
2. Exact effective F-sigma/G-delta complexity of the canonical upper/lower source sheets.
3. Uniform effective Baire-1 lexicographic min/max inverse selectors.
4. Effective F-sigma description of the double-fibre output set.
5. A noncomputable-mass obstruction for the canonical sheets, extracted from the already-settled P4-S005 map without revisiting crossing probabilities.
6. A precise collapse lemma for the single-hidden-bit / rotating-mask filler architecture.

Failed or incomplete:

1. Turning Baire-1 canonical selectors into an everywhere/a.e. computable inverse pair.
2. Computing canonical component masses or conditional measures uniformly.
3. Using canonical branch approximations to coherently combine P4-S004's fixed-stage pullbacks into one computable martingale.
4. Repairing SRC-0061 with one global/rotating hidden bit.
5. Constructing an exact k=2 computable-randomness destroyer.

## Proof dependencies and guards

The new mathematics uses elementary effective compactness on Cantor space, the P4-S002/P4-S003 computable clopen fibre approximants, and the already-committed P4-S005 prefix-code map only as an internal example for canonical-sheet mass. No new literature theorem is imported.

SRC-0061 / THM-0072 is used only as the previously recorded unrestricted scan mechanism. Its filler/pre-revealed-bet obstruction is not claimed resolved.

- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- The pre-Phase-4 Gate-3 guard is preserved historically.
- P4-S001 through P4-S005 are unchanged exactly.
- General k=2 forward computable-randomness preservation/failure remains unresolved.
- No result is claimed for k>2.
- DEF-0020 and catalogue/source convention records are unchanged.
- No novelty/open-status claim is made.
- Gate 4 is not reviewed. Phase 5 remains CLOSED.
