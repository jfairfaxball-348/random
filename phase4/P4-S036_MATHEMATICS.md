# P4-S036 — finite dependency closure, savings normalization and infinite-ray effectivity

Date: 2026-10-06
Session: P4-S036
Incoming checkpoint: de5905a3b32cb091f2d5ff906606dff891e0632b
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding
Result: **THE UNIFORM PACKET-SIZE HYPOTHESIS OF P4-S035 IS UNNECESSARY. EVERY COMPUTABLY FINITE CLOSED PACKETIZATION, EVEN WITH UNBOUNDED PACKET SIZES, IS HARMLESS: A STANDARD THRESHOLD-STOPPING SAVINGS TRANSFORM MAKES SUCCESS PERSIST TO PACKET BOUNDARIES, AFTER WHICH THE P4-S035 FINITE DOOB COMPRESSION APPLIES PACKET BY PACKET. MORE GENERALLY, ANY TOTAL COMPUTABLE ONLINE CLOSED-PACKETIZER RETURNING A COMPLETE FINITE PACKET AT ENTRY SUFFICES. BY CONTRAST, FINITE FORWARD DEPENDENCY CLOSURE, WELL-FOUNDEDNESS, FINITE RANK AND EVEN COMPUTABLE RANK DO NOT BY THEMSELVES PRODUCE SUCH A PACKETIZER. A RANK-1 HALTING-CODED FAMILY SHOWS THAT FINITE CLOSURES MAY FAIL TO BE UNIFORMLY DISCOVERABLE, AND A FULLY COMPUTABLE RANK-1 OVERLAP GRAPH SHOWS THAT UNIFORMLY COMPUTABLE FINITE FORWARD CLOSURES MAY STILL HAVE ONE INFINITE SYMMETRIZED INTERACTION COMPONENT. FOR THE P4-S035 RAY, EVERY FINITE TRUNCATION ADMITS FINITE CONDITIONAL-EXPECTATION COMPRESSION, BUT NO FINITE RAW CUT CLOSES ALL CLAIMS; CLASSICAL BOUNDED/UNIFORMLY-INTEGRABLE LIMITS DO NOT SUPPLY THE MISSING EFFECTIVE TERMINAL VALUE. NO OH NON-INVARIANCE WITNESS IS PROVED.**

## Authority, uniqueness and scope

Live main matched the P4-S035 outgoing checkpoint

de5905a3b32cb091f2d5ff906606dff891e0632b

immediately before the first write. Direct path lookup found no P4-S036 mathematics record, so P4-S036 was unused.

P4-S001 through P4-S035, the selected CAND-01 authority in phase2/candidates.json, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, and P4-S032/P4-S033/P4-S034/P4-S035 were read. All validated mathematics through P4-S035 is frozen. The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence is not reopened.

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
The retained inclusions remain
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## 1. Dependency objects: exact stake dependence versus operational closure

Fix a repeated invertible finite binary block recoding \(H_A\), a total computable one-hole virtual scan \(T\), a computable nonnegative rational martingale \(d\) on the virtual transcript, and a fixed computable raw evaluator such as the P4-S034/P4-S035 support evaluator.

A virtual coordinate \(q\) is a **spoiled claim** once its raw value has become determined while \(q\) is still unrequested. The claim stays open until \(T\) requests \(q\); if a branch later commits to omitting \(q\), the claim never produces a wager.

Two related dependency objects are useful.

### Definition 1 — essential stake-dependence witness

Let \(q\) lie in block \(B\), and let \(s\) be a finite evaluator state immediately after \(q\) has become raw-determined but before \(T\) requests it.

A finite pair of virtual branch simulations is an **essential \(B\to C\) stake-dependence witness** if:

1. both simulations extend the same state \(s\);
2. both eventually reach a request for \(q\);
3. before that request, their answers agree at every queried virtual coordinate outside block \(C\);
4. every difference between the two finite simulations is first exposed through queried virtual information from block \(C\);
5. the signed fractional stake chosen by \(d\) at the request for \(q\) is different in the two simulations.

Write
\[
B\to_d C
\]
when such a finite witness exists.

Because the witness is finite, all such labelled witnesses can be enumerated effectively by dovetailing finite virtual-answer trees. Thus the exact essential-dependence graph is uniformly c.e. The negative assertion that no such future witness exists need not be decidable.

This definition does not hide future information: every edge comes with the explicit finite later transcript on which the stake changes.

### Definition 2 — spoiled-exposure graph

For packet closure one needs a conservative operational object. Put
\[
B\leadsto C
\]
when some finite virtual run has a spoiled claim \(q\) from block \(B\) open and, before \(q\) is requested, \(T\) queries a virtual coordinate from block \(C\).

Again the edge has a finite witness and is uniformly c.e. Every essential stake edge is witnessed inside spoiled exposure, but \(\leadsto\) may also record later information which turns out not to alter the stake.

### Definition 3 — return interaction

Put an undirected return edge
\[
B\mathrel{-_r}C
\]
when a finite run visits block \(B\), then queries a coordinate in block \(C\), and later returns to another coordinate of \(B\).

Let \(G^{cl}\) be the undirected closure graph generated by the symmetrizations of \(\leadsto\) and the return edges. This is the graph relevant to the finite-packet compiler: packet compression requires both delayed-decision dependence and block revisits to remain inside the same finite episode.

The three levels should not be conflated:

- \(B\to_d C\): information in \(C\) can genuinely change a spoiled stake originating in \(B\);
- \(B\leadsto C\): \(C\) is exposed while a \(B\)-claim is still open;
- \(G^{cl}\): operational interaction that must be closed together by the P4-S035 packet proof.

Same-block dependence is the case \(B=C\). Finite packet dependence means a finite set of blocks contains all relevant closure interaction. A directed infinite ray is stronger than merely having an infinite component of \(G^{cl}\).

## 2. A persistent-savings transform

The only use of P4-S035's uniform packet-size bound was to deduce that unbounded capital somewhere inside packets forces unbounded capital at packet exits. That can be removed before doing any recoding.

Normalize \(d(\varnothing)=1\). For each integer \(k\ge1\), let \(\tau_k\) be the first virtual stage at which
\[
d\ge 2^k,
\]
if such a stage occurs, and let \(d^{[k]}\) be \(d\) stopped at \(\tau_k\).

Define
\[
\widehat d
=
\sum_{k\ge1}2^{-k}d^{[k]}.
\]

### Lemma 4 — computable persistent savings

\(\widehat d\) is a total computable nonnegative rational martingale. If \(d\) is unbounded on a path, then
\[
\widehat d_t\longrightarrow\infty
\]
along that path.

**Proof.**

Each \(d^{[k]}\) is a computable stopped martingale. At a finite transcript \(\sigma\), compute
\[
M(\sigma)=\max_{\tau\preceq\sigma}d(\tau).
\]
Choose \(K\) with \(2^K>M(\sigma)\). For every \(k>K\), threshold \(2^k\) has not been reached on \(\sigma\), so
\[
d^{[k]}(\sigma)=d(\sigma).
\]
Hence the infinite tail is the exact rational geometric tail
\[
d(\sigma)\sum_{k>K}2^{-k}.
\]
Therefore \(\widehat d(\sigma)\) is exactly computable and rational. Termwise martingale averaging is justified by the same exact finite-plus-geometric representation.

A binary nonnegative martingale can increase by at most a factor \(2\) in one step. Hence after threshold \(2^k\) is first reached,
\[
2^k\le d^{[k]}<2^{k+1},
\]
so the permanently stopped summand \(2^{-k}d^{[k]}\) is at least \(1\) forever afterwards.

If \(d\) is unbounded, then for each \(K\) all thresholds \(2,4,\ldots,2^K\) are eventually reached. From then on the first \(K\) stopped summands contribute at least \(K\) permanently. Thus \(\widehat d_t\to\infty\). ∎

This is the only savings normalization needed in this session. No P4-S015–P4-S031 ticket or reserve machinery is used.

## 3. Unbounded finite packets are safe

Let the repeated block size be \(n\ge2\). A **computable finite packet partition** is a computable partition of the block indices into nonempty finite packets, with the exact finite list of blocks in each packet computable. Packet cardinalities need not have a uniform bound.

Retain the P4-S035 definition: \(T\) is packet-closed if, after first entering a packet, it performs every virtual query it will ever make from that packet before its first query outside it and never returns.

### Theorem 5 — arbitrary finite closed-packet normalization

For every repeated invertible finite binary block recoding \(H_A\) of block size \(n\ge2\), every total computable one-hole scan which is closed with respect to a computable finite packet partition preserves computable randomness after the recoding.

Equivalently, if \(x\in CR\), \(T\) is packet-closed and every packet is finite and computably given, then
\[
S_T(H_A(x))\in CR.
\]
No uniform bound on packet size is required.

**Proof.**

Suppose a computable nonnegative rational martingale \(d\) succeeds on \(S_T(H_A(x))\). Replace \(d\) by the persistent-savings martingale \(\widehat d\) from Lemma 4. Then \(\widehat d\) tends to infinity, not merely along a subsequence.

When \(T\) first enters one finite packet \(P\), condition on the entry transcript. For each complete virtual assignment \(u\) to \(P\), simulate the finite packet episode until \(T\) leaves \(P\). Packet closure guarantees that all virtual queries from \(P\) occur before this exit and there is no later return. Let
\[
D_P(u)
\]
be \(\widehat d\)'s exit capital.

This finite adaptive episode is a stopped fair-coin martingale, so the average of \(D_P\) over the uniform virtual assignments to \(P\) equals the packet-entry capital.

The repeated block map restricted to \(P\) is a finite bijection of raw packet assignments. Therefore
\[
R_P(z)=D_P(A_Pz)
\]
has the same mean over raw assignments \(z\).

Query every raw coordinate of \(P\) in a fixed computable order and use the finite Doob conditional expectations of \(R_P\). This gives an exact computable nonnegative raw martingale segment whose entry capital equals \(\widehat d\)'s packet-entry capital and whose exit capital equals \(\widehat d\)'s packet-exit capital on the target.

Because every packet contains at least one \(n\)-bit block and \(n\ge2\), a one-hole scan cannot omit an entire packet. Hence \(T\) must enter every packet. The raw packet evaluator therefore queries every raw coordinate exactly once and is an effective adaptive permutation.

By Lemma 4, once \(\widehat d\) exceeds a level it never loses the stopped savings which produced that level. Consequently its packet-exit capitals are unbounded, indeed tend to infinity along sufficiently late packet exits. The concatenated raw Doob martingale therefore succeeds on an effective permutation of \(x\), contradicting \(x\in CR\). ∎

### Corollary 6 — the P4-S035 size bound was inessential

Theorem 8 of P4-S035 remains true with “uniformly bounded finite packet partition” replaced by “computable finite packet partition”.

Thus larger and larger finite closed packets cannot themselves support coded-hole destruction.

## 4. Online finite closed episodes are also safe

A static partition is stronger than the proof needs.

### Definition 7 — total computable closed packetizer

A **closed packetizer** for \(T\) is a total computable procedure \(\Pi\) which, whenever the virtual run first enters an as-yet unassigned block, takes the current finite transcript and outputs an exact finite set \(P\) of as-yet unassigned blocks containing that block, such that on every continuation from that entry state:

1. every query from a block in \(P\) which will ever occur is made before the first query from a block outside \(P\);
2. after the first query outside \(P\), \(T\) never returns to \(P\);
3. packets produced successively on a run are disjoint.

No bound on \(|P|\) is required.

### Theorem 8 — computably finite closed-episode normalization

The conclusion of Theorem 5 still holds when the static packet partition is replaced by a total computable closed packetizer.

**Proof.**

At packet entry, \(P=\Pi(\text{entry transcript})\) is already known completely and is finite. Therefore the same finite terminal-payoff table and finite raw Doob conditional expectations can be computed before any raw coordinate of that packet is queried.

The packetizer hypotheses make the episode closed on every continuation represented in the finite table. Successive packets are disjoint, so no raw coordinate is queried twice.

A one-hole scan enters every source block of size \(n\ge2\): otherwise it would omit at least two virtual coordinates. Hence every block is eventually assigned to some packet and the raw packet scan is exhaustive.

Apply Lemma 4 exactly as in Theorem 5. ∎

This is the strongest positive theorem obtained in P4-S036.

The operative hypothesis is not a numerical packet-size bound. It is **effective knowledge of a complete finite closure before the raw packet is opened**.

## 5. Nonuniform finite closure does not give a total compiler

Finite set-theoretic closure is not enough if the compiler cannot know when the finite set is complete.

### Proposition 9 — rank-one halting-coded closure

There is a uniformly c.e. family of directed dependency graphs \(G_e\) such that:

- every \(G_e\) is well-founded;
- every vertex has rank at most \(1\);
- every forward closure is finite;
- but no total computable procedure, given \(e\), outputs the complete forward closure of a distinguished vertex \(b_e\).

**Construction.**

Use vertices \(b_e,c_e\). Enumerate the single possible edge
\[
b_e\to c_e
\]
iff machine \(e\) halts.

Then
\[
\operatorname{cl}^+(b_e)=
\begin{cases}
\{b_e\},& e\text{ does not halt},\\
\{b_e,c_e\},& e\text{ halts}.
\end{cases}
\]
All closures are finite and every rank is at most \(1\). A total procedure returning the complete closure would decide whether \(e\) halts. ∎

The same pattern can be realized operationally by a computable delayed-decision routine which changes a pending stake using a later block exactly when a simulated machine eventually halts. The resulting edge remains finitely witnessed when it exists.

Therefore:

### Consequence 10

Set-theoretic finite closure, effective well-foundedness as a semantic promise, finite rank, and even a fixed computable rank bound do not by themselves supply the negative information needed by the closed-packet compiler.

If the dependency relation is only c.e., the missing datum is an effective **closure-completion certificate**.

## 6. Uniformly computable forward closures still need not packetize

Even stronger forward information does not solve the overlap problem.

Consider computable vertices
\[
a_0,a_1,\ldots,\qquad c_0,c_1,\ldots
\]
with directed edges
\[
a_n\to c_n,\qquad a_n\to c_{n+1}.
\]

Every successor list is computable. Every forward closure is computable and has size at most \(3\):
\[
\operatorname{cl}^+(a_n)=\{a_n,c_n,c_{n+1}\},
\qquad
\operatorname{cl}^+(c_n)=\{c_n\}.
\]
The graph has rank \(1\) and no infinite directed forward ray.

But its symmetrization is one infinite chain
\[
c_0-a_0-c_1-a_1-c_2-a_2-\cdots.
\]
Any packet partition which keeps the endpoints of every dependency edge together must put this whole component into one packet. Hence no finite packet partition can close all edges.

### Proposition 11 — finite forward closure is weaker than finite packet closure

Uniformly computable finite forward closures, computable rank \(1\), and absence of infinite directed rays do not imply finite closed packetizability.

This obstruction is not merely abstract. It can be realized by an exact computable virtual schedule:

- expose two rows of an \(A_n\)-block and leave one spoiled parity \(q_n\) pending;
- expose deciding bits in \(C_n\);
- open \(q_{n+1}\);
- expose deciding bits in \(C_{n+1}\);
- then request \(q_n\) with a stake which genuinely changes with the \(C_n,C_{n+1}\) information.

All coordinates can subsequently be exhausted. Thus the architecture itself can be harmless while its essential dependency graph already has the rank-one overlap shape.

This is important: **graph rank is not a randomness invariant**. It is only one compiler-complexity parameter.

The positive graph-theoretic condition supplied by Theorem 8 is stronger: the interaction must admit a total computable decomposition into finite closed episodes, equivalently a computable packetizer. One sufficient special case is that the symmetrized operational closure components are uniformly computable finite sets and the scan never interleaves distinct components.

## 7. The genuine P4-S035 ray cannot be fixed by reordering raw coordinates

Return to
\[
u_0=x_0\oplus x_2,\qquad
u_1=x_0\oplus x_1,\qquad
u_2=x_0\oplus x_1\oplus x_2.
\]

The first two rows have supports
\[
S_0=\{0,2\},\qquad S_1=\{0,1\}.
\]
Their union is all three raw coordinates.

### Lemma 12 — no exact raw-coordinate evaluator can retain a block-\(b\) pivot after producing \(u_0^{(b)},u_1^{(b)}\)

Any exact evaluator which has determined both \(u_0^{(b)}\) and \(u_1^{(b)}\) from raw coordinate values of \(B_b\) has queried all three raw coordinates of \(B_b\). Hence \(u_2^{(b)}\) is already determined.

**Proof.**

To determine a binary linear form exactly from a subset of raw coordinates, every coordinate in its support must be known. Determining both first rows therefore requires all coordinates in
\[
S_0\cup S_1=\{0,1,2\}.
\]
No reordering changes this set-theoretic requirement. ∎

So the P4-S035 chain
\[
B_0\to B_1\to B_2\to\cdots
\]
cannot be repaired by retaining a different raw pivot inside \(B_b\).

A different compiler would have to do something genuinely nonlocal, for example:

- keep a conditional value rather than materializing the virtual branch immediately;
- maintain several virtual states;
- price an open claim against future blocks;
- or use another source-side martingale construction.

## 8. Finite ray truncations have exact Doob prices

The infinite ray is not locally mysterious. Cut it after finitely many blocks.

For every finite \(N\), stop at a cut after all delayed claims originating before the last boundary block have been resolved. The finite terminal virtual capital is a computable function of finitely many virtual block assignments, hence after the invertible recoding a computable function of finitely many raw block assignments.

Therefore:

### Lemma 13 — every finite dependency-ray truncation has an exact raw conditional-expectation martingale

For every finite closure depth \(N\), finite Doob conditional expectations give an exact computable raw martingale reproducing the chosen finite terminal payoff.

The obstruction is not failure of finite conditional expectation.

The obstruction is that extending the cut exposes a new boundary claim. There is no finite stage at which the family closes once and for all.

## 9. Why classical convergence is not enough

One might stop a successful martingale at a fixed savings threshold. The stopped process is bounded, so ordinary measure-theoretic uniform integrability and martingale convergence are available. That still does not provide the required computable source martingale.

The issue is effective convergence of the terminal payoff.

### Lemma 14 — bounded computable martingales can have noncomputable pointwise limits

There is a bounded computable nonnegative martingale \(M\) whose limit on a computable path is a noncomputable real.

**Construction.**

For each machine index \(e\), reserve pair-coded coordinates \(\langle e,t\rangle\). If machine \(e\) halts for the first time at stage \(t\), run one mean-zero one-step fair wager of size \(2^{-e-3}\) on coordinate \(\langle e,t\rangle\), and otherwise never activate that \(e\)-component.

Sum all components on top of constant capital \(1\). The total possible negative variation is below \(1/2\), so \(M\) stays positive and bounded. At any finite string only finitely many reserved coordinates have been reached and the remaining tail has a computable geometric bound, so \(M\) is exactly computable.

On the all-1 path,
\[
\lim M
=
1+\sum_{e\in K}2^{-e-3},
\]
where \(K\) is the halting set. This real is noncomputable. ∎

Thus boundedness and classical uniform integrability do not yield a computable terminal-value functional or a computable modulus of convergence.

Applied to the infinite-ray strategy:

- each finite closure has a computable conditional-expectation compiler;
- threshold-stopping can make the finite-horizon payoffs uniformly bounded;
- a classical limit may exist;
- but no effective modulus or computable terminal value follows from the dependency graph alone.

The precise surviving resource is therefore **effective nonclosure of the backward fair price of open claims**, not merely existence of an infinite graph.

## 10. A sharper view of the ray: an open-boundary price process

The P4-S035 chain has very small local width. At each step one old pending parity is closed while the next block creates a new pending parity. A finite truncation can therefore be viewed as a finite backward-pricing problem with a finite boundary state.

For the displayed three-bit chain, the unresolved boundary state can be taken to include the pending bit \(u_2^{(b)}\) together with the finite virtual control state. Backward finite-closure pricing produces a computable finite vector of fair prices indexed by that boundary state.

As the closure depth increases, these price vectors need not stabilize effectively. A successful infinite compiler would require either:

1. an exact telescoping identity making the boundary price harmless;
2. a computable convergence modulus for the finite-horizon price vectors;
3. a uniform positive upper/lower bound which lets savings absorb the boundary factor;
4. or another source-side mechanism not expressible as finite backward pricing.

This finite-state boundary-price formulation is strictly sharper than saying only that the packet is infinite. It selects the next attack.

## 11. What P4-S036 says about the recoded P4-S011 witness

Let \(D\) and \(Y\) be the settled P4-S011 scan destroyer and vulnerable computably random source, let \(H\) be the displayed repeated three-bit homeomorphism, and let
\[
X=H^{-1}(Y).
\]
Then \(X\in CR\) and
\[
D(H(X))=D(Y)\notin CR.
\]

P4-S034 already implies that the spoiled multiplicative gain of this witness is unbounded.

The P4-S011 wtt autoreduction gives each individual sentinel computation a computable finite use bound. Hence every individual deciding computation depends on only finitely many virtual coordinates. This does **not** imply a global finite packetization: successive epochs can overlap the three-bit block boundaries, and finite decision closures can chain through overlap.

Theorem 8 now yields an exact negative structural consequence:

### Corollary 15 — the recoded P4-S011 witness has no computable finite closed packetizer

The virtual P4-S011 witness \(D\) relative to the displayed recoding cannot admit a total computable closed packetizer of the form in Definition 7.

Otherwise Theorem 8 would imply
\[
D(H(X))\in CR,
\]
contradicting the settled P4-S011 destruction.

This does not prove that its essential graph contains a directed infinite ray. It may instead realize an infinite overlap component assembled from individually finite wtt decision closures. Distinguishing those two cases requires further analysis of the actual autoreduction schedule.

Most importantly, this still does not prove
\[
X\in OH.
\]
The only established source fact is \(X\in CR\). An actual OH non-invariance witness still requires proving
\[
X\in OH,\qquad H(X)=Y\notin OH.
\]
That source-side OH statement remains missing.

## 12. Exact positive boundary after P4-S036

The following are now on the positive side for every repeated invertible finite binary block recoding of block size at least two:

1. block-closed witnesses;
2. uniformly bounded packet-closed witnesses;
3. arbitrary computably finite packet-closed witnesses;
4. more generally, witnesses admitting a total computable finite closed packetizer.

No uniform packet cardinality bound is needed.

The following conditions alone are **not enough to invoke that compiler**:

1. every individual stake has finite future dependence;
2. every forward dependency closure is finite only set-theoretically;
3. semantic well-foundedness;
4. finite rank or computable rank;
5. even uniformly computable finite forward closures, if their symmetrized interaction components overlap into an infinite component.

These are compiler statements only. No condition in the second list is claimed to support actual destruction.

## 13. Separation status

No computably random
\[
x\in OH
\]
with
\[
H(x)\notin OH
\]
is proved.

Therefore no OH non-invariance theorem and no strict
\[
R_2\subsetneq OH
\]
conclusion is available.

The comparison class remains
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

P4-S032 null-ambiguity preservation remains unchanged. Ambiguity mass is not reinstated as an invariant.

## 14. Exact next target

P4-S037 should attack **rolling finite-state normalization on an infinite interaction component**, not return to packet size or bankrolls.

The most informative test cases are:

1. the P4-S035 simple dependency ray with one pending parity carried from block to block;
2. the rank-one overlap architecture of Proposition 11, where no directed ray exists but the symmetrized component is infinite;
3. the actual recoded P4-S011 schedule.

The central object should be the finite-horizon backward fair-price vector of the open boundary claims.

Test whether bounded open-claim width, finite boundary-state dimension, a computable contraction of price ratios, or a computable projective/Cauchy modulus forces a single raw martingale compiler. If not, construct an exact computable infinite-component architecture whose backward price vectors fail effective convergence or have unbounded boundary distortion.

For the recoded P4-S011 witness, determine whether the obstruction is a genuine directed ray or only overlapping finite wtt closures. Do not infer \(X\in OH\) from compiler failure.

## Guards

All mathematics through P4-S035 is preserved. The P4-S015–P4-S031 bankroll/ticket/frontier/recycling line remains frozen as the default route.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made. Phase 4 remains OPEN; Phase 5 remains CLOSED.
