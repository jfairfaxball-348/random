# P4-S035 — determination-predictable spoiled stakes and infinite cross-block delay

Date: 2026-10-06
Session: P4-S035
Incoming checkpoint: 9751ab899736c606f47f137f78823318c72aa6e6
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding
Result: **THE SPOILED-STAGE OBSTRUCTION SPLITS EXACTLY INTO A FINITE/PREDICTABLE PART AND AN INFINITARY CROSS-BLOCK PART. FOR THE DISPLAYED THREE-BIT RECODING, A COMPUTABLE SUPPORT ORDER GIVES EACH SPOILED VIRTUAL COORDINATE ITS OWN RAW DETERMINATION PIVOT. IF ITS FRACTIONAL STAKE IS UNIFORMLY KNOWN BEFORE THAT PIVOT IS READ, THE ENTIRE SPOILED-GAIN PRODUCT IS A COMPUTABLE RAW MARTINGALE, SO IT CANNOT BE UNBOUNDED ON A COMPUTABLY RANDOM SOURCE. THE WEAKER CLAIM “KNOWN AT DETERMINATION TIME” IS FALSE IF THE STAKE MAY USE THE DETERMINING BIT ITSELF. MORE GENERALLY, EVERY BLOCK-CLOSED, OR UNIFORMLY BOUNDED PACKET-CLOSED, ONE-HOLE WITNESS IS HARMLESS UNDER EVERY REPEATED INVERTIBLE FINITE BINARY BLOCK RECODING: THE WHOLE FINITE PACKET IS COMPRESSED BY AN EXACT RAW DOOB MARTINGALE. BOUNDED DECISION DELAY ALONE IS NOT ENOUGH: AN EXPLICIT ONE-HOLE ARCHITECTURE CAN CHAIN A PENDING SPOILED PARITY IN BLOCK b TO STAKE INFORMATION FIRST REVEALED IN BLOCK b+1, WITH UNIFORMLY BOUNDED INDIVIDUAL DELAY BUT NO FINITE CLOSED PACKET. NO OH NON-INVARIANCE WITNESS IS PROVED.**

## Authority, uniqueness and scope

Live main matched the P4-S034 outgoing checkpoint

9751ab899736c606f47f137f78823318c72aa6e6

before substantive work and again immediately before the first write. Repository search returned no committed P4-S035 record, so P4-S035 was unused.

P4-S001 through P4-S034, the selected CAND-01 authority in phase2/candidates.json, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, phase4/P4-S032_MATHEMATICS.md, phase4/P4-S033_MATHEMATICS.md, and phase4/P4-S034_MATHEMATICS.md were read. All validated mathematics through P4-S034 is frozen. The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence is not reopened.

Retain
\[
R_2=\{x\in CR:(\forall F\in\mathcal F_2)\ F(x)\in CR\},
\]
\[
OH=\{x\in CR:(\forall\hbox{ one-hole scans }T)\ S_T(x)\in CR\},
\]
and
\[
OH^{iso}=\{x\in CR:(\forall H\in\mathcal H)\ H(x)\in OH\}.
\]
The retained inclusions are
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## 1. Displayed recoding and raw determination time

Work blockwise with
\[
u_0=x_0\oplus x_2,\qquad
u_1=x_0\oplus x_1,\qquad
u_2=x_0\oplus x_1\oplus x_2
\]
and
\[
A=
\begin{pmatrix}
1&0&1\\
1&1&0\\
1&1&1
\end{pmatrix}.
\]

Fix a virtual one-hole scan T and a computable nonnegative rational martingale d on its transcript after H. Use the P4-S034 raw support evaluator, but allow the fresh coordinates inside one requested support to be queried in a chosen computable order.

For a virtual coordinate q, let S(q) be its raw support. Along a raw evaluator run, let Q^-_m be the raw coordinates queried before raw query event m, and let p_m be the coordinate queried at that event.

### Definition 1 — raw determination event

The raw determination event of q is the first raw query event
\[
\delta(q)=m
\]
for which
\[
S(q)\subseteq Q^-_m\cup\{p_m\}.
\]

Immediately before this event q has the form, in \(\{\pm1\}\)-notation,
\[
Z_q=\varepsilon_q(\rho^-_m)X_{p_m},
\]
where \(\rho^-_m\) is the finite raw history before querying \(p_m\), \(X_{p_m}\in\{\pm1\}\) is the fresh raw bit, and the orientation
\[
\varepsilon_q(\rho^-_m)\in\{\pm1\}
\]
is computable from the already queried raw support bits.

Let \(\beta(q)\) be the later virtual betting event at which T actually requests q and d chooses its fractional stake on q. A virtual query is **spoiled** exactly when \(\delta(q)\) occurs strictly before \(\beta(q)\). The distinction is temporal: q is already a measurable function of the raw history when d eventually chooses its wager.

### Definition 2 — pre-pivot forecastability

A spoiled stake is **determination-predictable** if there is one total computable forecast procedure which, from the finite evaluator state and the raw history \(\rho^-_{\delta(q)}\) *before the determining pivot is read*, outputs a rational
\[
\widehat s(q,\rho^-_{\delta(q)})\in[-1,1]
\]
such that on every continuation on which q is later requested, d's actual signed fractional stake at q is exactly this value.

The continuation quantifier is essential. The hypothesis may not inspect later virtual information and then merely report the value seen on the target path.

This is stronger than saying that the stake is computable from the raw history *after* the determining bit has been read.

## 2. A separating support schedule for the displayed matrix

There is a computable way to order raw support queries so that no raw query event first determines two still-unrequested virtual coordinates.

For a previously untouched block:

- if the first requested row is \(u_0\), query \(x_2,x_0\) in that order;
- if the first requested row is \(u_1\), query \(x_1,x_0\) in that order;
- if the first requested row is \(u_2\), query \(x_0,x_2,x_1\) in that order.

After a first \(u_0\)-query, the only fresh raw bit is \(x_1\); whichever of \(u_1,u_2\) is requested next uses it, and the other row becomes determined at the same event. The \(u_1\)-first case is symmetric.

If \(u_2\) is requested first, then after \(x_0\) no other row is determined, after \(x_2\) exactly \(u_0\) is newly determined, and after \(x_1\) exactly \(u_1\) is newly determined in addition to the current live row \(u_2\).

Hence:

### Lemma 3 — spoiled-determination separation

For the displayed matrix there is a total computable support evaluator such that at every raw query event at most one not-yet-requested virtual coordinate becomes newly determined.

The evaluator is still the P4-S034 one-hole support evaluator. Because every raw column of A has weight at least two, it is exhaustive on every transcript exactly as in P4-S034.

## 3. Early-decision spoiled-stake normalization

Write the target multiplicative factor of d at virtual coordinate q as
\[
m_q=1+s_q Z_q,
\]
where \(s_q\in[-1,1]\) is the signed fractional stake and \(Z_q\in\{\pm1\}\) is the virtual bit in sign notation.

### Theorem 4 — determination-predictable spoiled gain transfers exactly

Let x be computably random. Let T be a total computable one-hole virtual scan and d a computable nonnegative rational martingale. Suppose d succeeds on
\[
S_T(H(x)).
\]

Use the separating support schedule of Lemma 3. If every spoiled virtual stake is determination-predictable, then there is a computable nonnegative rational martingale e on the raw evaluator transcript whose target capital is exactly the product of d's spoiled multiplicative factors. Consequently such a d cannot succeed.

**Proof.**

P4-S034 already gives a computable raw martingale \(e_L\) which copies every live virtual wager. Since the displayed raw evaluator is exhaustive, it is an effective permutation, so its output on x is computably random. Hence the live product is bounded.

Because d succeeds, P4-S034 Corollary 5 gives that the product of spoiled factors is unbounded.

Now consider a raw query event m. If no still-unrequested virtual coordinate becomes newly determined, e holds. If exactly one such coordinate q becomes determined, Lemma 3 says there is no second spoiled claim competing for this raw bit. By determination-predictability its eventual stake \(s_q\) is already computable from \(\rho^-_m\). Also
\[
Z_q=\varepsilon_q(\rho^-_m)X_{p_m}.
\]
Therefore e bets the signed raw fraction
\[
s_q\varepsilon_q(\rho^-_m)
\]
on the fresh bit \(X_{p_m}\).

Its multiplier is exactly
\[
1+s_qZ_q=m_q.
\]

On branches where q is ultimately omitted, this is simply an extra legal fair wager; no replication claim is needed there. On the target path, T is exhaustive by the retained P4-S008 singleton-fibre argument because H(x) is computably random. Thus every such q is eventually requested, and e's target capital is exactly the product of all spoiled factors.

That product is unbounded, so e succeeds on an effective permutation of x, contradicting computable randomness. ∎

### Consequence 5

Any actual destruction through the displayed H must use spoiled gain whose stake is not uniformly determined before its raw determination pivot. Finite Boolean mixing plus early-decided spoiled wagers is not enough.

This is stronger than P4-S034's spoiled-gain necessity: the surviving resource is now **non-predictable late choice relative to raw determination**, not spoiledness by itself.

## 4. Why “known at determination time” is too weak

Suppose a spoiled coordinate q is first determined by raw pivot p at the same event that a currently requested live virtual coordinate r is determined. A later d-stake on q may depend on the just-seen value of r.

Then the stake is computable immediately *after* q becomes raw-determined, but it was not fixed before p was read. Moving it back to p would require choosing a wager after seeing the outcome of the wagered raw bit.

This is not a terminological issue; it produces a real normalization factor.

Assume from the pre-pivot history that
\[
Z_q=\theta X_p
\]
with \(\theta\in\{\pm1\}\). Suppose the later stake on q is synchronously decided from the same pivot, with computable branch values \(s_+\) and \(s_-\) according as \(X_p=+1\) or \(-1\). The desired spoiled multiplier is
\[
g(+)=1+\theta s_+,\qquad
g(-)=1-\theta s_-.
\]

Its raw fair price before the pivot is
\[
c=\frac{g(+)+g(-)}2
 =1+\frac{\theta}{2}(s_+-s_-).
\]

If the target factor is positive then \(c>0\). The normalized pair
\[
g(+)/c,\qquad g(-)/c
\]
has mean one and is therefore one legal raw martingale step.

### Lemma 6 — synchronous late-choice premium

For a collision-free spoiled determination event whose stake is computable from the pre-pivot history plus the pivot outcome, the spoiled factor decomposes exactly as
\[
g(X_p)=c\,h(X_p),
\]
where h is a computable nonnegative mean-one raw martingale factor and c is the computable pre-pivot scalar above.

Thus for a sequence of such events,
\[
\prod g_j
=
\left(\prod c_j\right)
\left(\prod h_j\right).
\]

On a computably random raw evaluator output, the h-product is bounded. Therefore unbounded spoiled gain in this synchronous class forces
\[
\prod_j c_j
\]
to be unbounded.

If \(s_+=s_-\), then \(c=1\) and Lemma 6 collapses to Theorem 4. Hence Theorem 4 is exactly the zero-late-choice-premium case.

This also proves that the weaker hypothesis “the stake is computable from the raw history at the determination time” does not suffice unless “at” means before the determining pivot, or unless the cumulative late-choice premium is separately controlled.

## 5. General repeated finite-block version

Let A be any fixed invertible binary \(n\times n\) matrix repeated on successive blocks.

For a chosen support evaluator and one raw query event m, let \(C_m\) be the set of not-yet-requested virtual coordinates which become newly determined at m.

If every q in \(C_m\) has a pre-pivot forecasted stake, define the cluster payoff
\[
G_m(b)=\prod_{q\in C_m}\left(1+\widehat s_q Z_q(b)\right),
\qquad b\in\{\pm1\},
\]
and its fair price
\[
c_m=\frac{G_m(+1)+G_m(-1)}2.
\]

Whenever \(c_m>0\), \(G_m/c_m\) is one legal raw martingale factor. Thus:

### Theorem 7 — cluster normalization

For every repeated invertible finite block matrix, early-decided spoiled gain factors as

\[
\prod_{\rm spoiled}m_q
=
M_{\rm raw}\cdot\prod_m c_m,
\]

where \(M_{\rm raw}\) is the capital of a computable nonnegative martingale on the raw support evaluator.

Consequently, if the cumulative cluster-price product is bounded above along the target, unbounded spoiled gain transfers to the raw one-hole evaluator.

In particular, if the matrix admits a computable online support schedule with
\[
|C_m|\le1
\]
for every raw query event, then \(c_m=1\) identically and every determination-predictable spoiled product transfers exactly.

Call this the **collision-free determination** class. The displayed three-bit matrix belongs to it by Lemma 3.

No claim is made that this class is maximal among all possible raw compilers. It is the largest exact repeated-block class established here for arbitrary interleaving under the pure early-decision transfer.

## 6. A stronger finite-memory theorem: closed packets are harmless

Late stake choice inside a fixed finite block can be handled without moving individual wagers back at all.

Let A be an invertible binary \(n\times n\) matrix with \(n\ge2\), repeated blockwise. More generally partition the block indices computably into disjoint **packets**, each containing at most M blocks for one fixed finite M.

A virtual scan T is **packet-closed** if, once it first queries a coordinate from a packet P, every virtual coordinate it will ever query from P is queried before T next queries outside P, and T never returns to P.

Block-closed means M=1.

### Theorem 8 — bounded closed-packet normalization

For every repeated invertible finite binary block recoding and every computable uniformly bounded packet partition, a packet-closed total computable one-hole scan preserves computable randomness after the recoding.

Precisely, if x is computably random, then for every packet-closed one-hole T,
\[
S_T(H_A(x))\in CR.
\]

**Proof.**

Assume a computable nonnegative martingale d succeeds on the virtual scan output.

Consider one packet P when T first enters it. The entire virtual episode in P has at most \(Mn\) queries. Its adaptive query order and all d wagers are computable from the entry state and the virtual bits revealed inside P; no outside virtual information arrives before the episode closes.

For each complete virtual assignment u to P, simulate this finite episode and let
\[
D_P(u)
\]
be d's capital when T leaves P. Conditional on the entry state, this is the terminal value of a finite stopped fair-coin martingale, so its average over all virtual assignments to P equals d's entry capital.

The blockwise map on P is a finite bijection of its raw assignments, so
\[
R_P(z)=D_P(A_Pz)
\]
has the same average over raw packet assignments z.

A raw martingale can therefore query all raw coordinates of P in a fixed order and use the finite Doob conditional expectations of \(R_P\). It begins the packet with d's entry capital and ends it with exactly d's exit capital.

Now follow the packet order chosen by T. Because every packet contains at least \(n\ge2\) virtual coordinates and T omits at most one virtual coordinate globally, T must enter every packet. The raw evaluator therefore queries every raw coordinate exactly once and is an effective adaptive permutation.

By induction, the raw martingale capital at every packet boundary equals d's virtual capital at the corresponding packet boundary.

Inside one packet, d makes at most \(Mn\) bets and each nonnegative martingale multiplier is at most 2. Hence every within-packet capital is at most
\[
2^{Mn}
\]
times the packet-entry capital. If d is unbounded, its packet-boundary capitals are therefore unbounded. The raw martingale succeeds on an effective permutation of x, contradicting computable randomness. ∎

### Corollary 9 — block-local late choice is not the obstruction

For the displayed H, arbitrary late dependence among virtual bits of one block is harmless whenever the scan closes that block before moving elsewhere.

More generally, arbitrary finite-memory dependence inside any uniformly bounded closed packet of adjacent or nonadjacent blocks is harmless.

This theorem covers every repeated invertible finite binary block matrix, not only the displayed A.

A forward triangular block dependency that can be grouped into uniformly bounded closed packets therefore reduces to this theorem.

## 7. Bounded decision delay alone does not reduce to the positive theorem

A uniformly bounded number of intervening virtual queries does not force a finite closed packet.

Write \(u_i^{(b)}\) for virtual row i in block b. Consider the following exact one-hole scan architecture.

Begin with
\[
u_0^{(0)},u_1^{(0)},
\]
leaving \(u_2^{(0)}\) pending and raw-determined.

At stage b, before betting the pending \(u_2^{(b)}\):

1. query \(u_0^{(b+1)}\);
2. query \(u_1^{(b+1)}\);
3. use the newly seen \(u_1^{(b+1)}\) as information which may alter d's stake on \(u_2^{(b)}\);
4. on the designated trigger branch, query \(u_2^{(b)}\), leaving \(u_2^{(b+1)}\) as the new pending coordinate;
5. on a nontrigger branch, omit \(u_2^{(b)}\) forever and switch to an exhaustive fixed tail, so that this is the sole omitted coordinate.

Every transcript omits at most one virtual coordinate. On the all-trigger path every coordinate is eventually queried.

The stake on \(u_2^{(b)}\) has only two intervening virtual queries between raw determination and virtual betting, so the decision delay is uniformly bounded.

Yet it is not determination-predictable: after \(u_0^{(b)}\) and \(u_1^{(b)}\) have both been computed, their support union is
\[
\{x_0^{(b)},x_1^{(b)},x_2^{(b)}\}.
\]
Therefore every raw coordinate of block b has necessarily been consumed, regardless of the support-query order, and \(u_2^{(b)}\) is already fixed before the deciding information from block \(b+1\) exists.

Changing the elimination order inside block b cannot leave a raw pivot for \(u_2^{(b)}\). Raw coordinates in block \(b+1\) are independent of the parity in block b and cannot exactly replace such a pivot.

Nor does any finite packet close this dependency. Any packet containing block b and enough information to determine the \(u_2^{(b)}\)-stake must contain block \(b+1\). But on the all-trigger path block \(b+1\) itself leaves \(u_2^{(b+1)}\) pending, whose stake needs block \(b+2\), and so on. Closure propagates indefinitely.

### Theorem 10 — exact temporal obstruction

The displayed three-bit recoding admits a total computable one-hole scan architecture with uniformly bounded per-wager decision delay but an infinite cross-block delayed-decision chain
\[
B_0\longrightarrow B_1\longrightarrow B_2\longrightarrow\cdots
\]
such that:

- every pending spoiled parity in \(B_b\) is already raw-determined before the deciding information in \(B_{b+1}\) is exposed;
- no raw support order inside \(B_b\) can retain a pivot for that parity after both \(u_0^{(b)}\) and \(u_1^{(b)}\) have been produced;
- no uniformly bounded finite packet can contain the full decision closure of the pending wagers on the all-trigger path.

This defeats Theorem 4, Lemma 6 when the late information lies beyond the determining pivot, and Theorem 8's finite-packet compiler.

It does **not** prove that such a scan/martingale succeeds on any computably random source, still less on a source in OH. It is an exact compiler obstruction, not an OH non-invariance witness.

## 8. What is now ruled out

For the displayed H, an actual OH non-invariance witness cannot be explained by any of the following alone:

1. finite-coordinate Boolean mixing;
2. spoiled stages whose stakes are fixed before their determining pivots;
3. synchronous same-pivot late choices with bounded cumulative late-choice premium;
4. arbitrary late choices confined to one closed block;
5. arbitrary finite-memory choices confined to uniformly bounded closed packets.

Thus the first surviving architecture is genuinely infinitary **cross-block decision nonclosure**: a wager on an already raw-determined parity remains open while later blocks are exposed, and the dependency closure of these open wagers is not uniformly finite.

This is strictly sharper than “the pivot was consumed.”

## 9. Separation status and P4-S033/P4-S011 recoding

No computably random
\[
x\in OH
\]
with
\[
H(x)\notin OH
\]
is proved.

The cross-block chain in Theorem 10 is only an obstruction architecture. It does not establish a succeeding martingale on a suitable source and therefore does not imply
\[
R_2\subsetneq OH.
\]

The retained comparison remains
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

The P4-S033 recoded P4-S011 source is not promoted to a separation witness here. The present analysis gives a concrete criterion to test it later—whether its spoiled winning gain actually realizes an infinite cross-block decision-nonclosure chain—but no such source-side OH proof is obtained in this session.

P4-S032 null-ambiguity preservation remains unchanged as a reduction for arbitrary destructive global-k=2 maps. Ambiguity mass is not reinstated as an invariant.

## 10. Exact next target

The finite part of coded-hole delay is now normalized. P4-S036 should attack the infinite dependency closure itself.

The natural object is a directed block-dependency graph: place an edge
\[
B\to C
\]
when a spoiled wager whose parity was already raw-determined in block B uses virtual information first exposed later from block C.

Finite, uniformly bounded closed components are safe by Theorem 8. Theorem 10 supplies an explicit infinite ray which is not covered.

The next bounded questions are:

- does every computably well-founded / finitely closing dependency graph reduce to finite-packet Doob normalization, perhaps without a uniform packet-size bound;
- can a savings/stopping normalization remove the uniform packet-size restriction without re-entering the frozen ticket/reserve programme;
- can an infinite dependency ray be re-threaded by a different raw one-hole scan, or does one-hole geometry force a source-side self-avoiding witness;
- does the recoded P4-S011 witness actually instantiate such an infinite ray with unbounded gain;
- if so, can one prove its raw source lies in OH, which would finally give an OH non-invariance witness.

No conclusion on these questions is asserted here.

## Guards

All mathematics through P4-S034 is preserved. The P4-S015–P4-S031 ticket/reserve/frontier/recycling line remains frozen as the default route.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made. Phase 4 remains OPEN; Phase 5 remains CLOSED.
