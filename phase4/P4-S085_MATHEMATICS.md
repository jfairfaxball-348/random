# P4-S085 — Exact width-two filtration universality test for R₂ versus MLR

Date: 2026-10-10. Phase 4 Mathematics ONLY. Selected CAND-01.
Incoming independently pinned remote main: `2a481595f6c35bec361a84da4648c9a5d0bfc282` (P4-S084 outgoing). P4-S085 unused on entry.
Disposition: **GLOBAL EXACT REFORMULATION AND STRUCTURAL OBSTRUCTION; R₂ versus MLR NOT DECIDED.** The equivalence below combines the S007 coherent width-two inverse information with the S083 SRC-0071 sequence-set strategy formulation; it is not claimed as a new separation or a solution.

## 0. Frozen authority and source controls

Reviewed the cumulative Phase-4 mathematics and the selected individual results S004, S007, S008, S011/S012, S032/S033, S081–S084; S084 validation and close; CAND-01, Gate-3 PASS, P4 research pivot after S031 and strategic pivot after S069. Source scope stays at its recorded access: SRC-0019 and SRC-0060 statement inspected; SRC-0069 statement/proof as previously recorded; SRC-0070 and SRC-0072 abstract inspected; SRC-0071 preprint statements and internal proofs inspected, journal version metadata only. R_tot=MLR is only the recorded programme deduction relying on SRC-0071. No new source-access promotion or literature-dependent proof.

Retain, for every integer k≥2,
MLR=R_tot ⊆ R_fin ⊆ R_k ⊆ R₂ ⊆ OH^iso ⊊ OH^blk ⊆ OH^lin3 ⊆ OH=OH_h=R_k^scan ⊊ CR,
also R₂⊊OH, MLR⊊OH and KLR⊆TKLR⊆OH.
All original Y, clipped M, H with A=[101;110;111], X=H⁻¹(Y), and prior results are unchanged.

## 1. Effective dyadic filtrations

A **computable fair dyadic filtration** is a uniformly computable collection of clopen sets (C_τ:τ∈2^{<ω}) satisfying
(1) C_empty=2^ω;
(2) C_τ is the disjoint union C_{τ0} ⊔ C_{τ1};
(3) λ(C_τ)=2^{-|τ|}.
Each finite clopen set is given effectively by a finite prefix code. Every x has exactly one descending sequence of cells; write T_C(x) for its binary cell-address transcript.

For raw precision n and output precision m define
P_C(n,τ)={σ∈2^n : [σ]∩C_τ≠∅} for |τ|=m;
W_C(n,m)=max_{|τ|=m}|P_C(n,τ)|.
These finite sets and integer widths are computable uniformly from the partition presentation. The maxima are global over **all** output cells, not merely the cells on one winning transcript.

**Theorem 1 (exact global two-fibre condition).** The following are equivalent.
(a) Every fibre of T_C has size at most two.
(b) For every n there is m with W_C(n,m)≤2.
(c) There is a total computable (not necessarily bounded-growth) c:ω→ω such that W_C(n,c(n))≤2 for every n.
Moreover T_C is everywhere-total computable and fair-coin preserving; every total computable fair-coin-preserving Cantor self-map arises this way by taking inverse images of output cylinders.

**Proof.** Computable clopen membership yields each successive address bit from a finite prefix of x; λ(C_τ)=2^{-|τ|} proves fairness. Conversely the inverse image of every output cylinder under an everywhere-total computable Cantor map is uniformly effectively clopen (effective compactness/uniform continuity), and fairness gives its measure.

For (a)⇒(b), suppose for some n no m has width≤2. Let B be the tree of output strings τ for which C_τ meets at least three distinct n-cylinders. B is computable, prefix-closed and has a node at every height. König's lemma gives an infinite address y all of whose prefixes lie in B. For each fixed n-cylinder, intersections with the descending compact C_{y↾m} are nested; since there are finitely many n-cylinders, at least three of them intersect C_{y↾m} at every sufficiently large m. Compactness gives three distinct inputs in ∩_m C_{y↾m}=T_C^{-1}(y), contradiction.

For (b)⇒(c), search m=0,1,... until the finite decidable condition W_C(n,m)≤2 holds. The search halts by (b), so c is computable; no non-effective last-injury/selector/orientation is assumed. For (c)⇒(a), three distinct preimages of one y have three distinct n-prefixes for some n; these remain in P_C(n,y↾c(n)), contradicting the width bound. ∎

This recasts the S003/S007 inverse skeleton as an exact criterion on filtration trees; it does **not** give either inverse branch computably.

**Corollary 2 (one-bit posterior support and entropy obstruction).** If C satisfies Theorem 1, then for every n there is a computable c(n) such that, conditional on every nonempty output cell C_τ with |τ|≥c(n), the random variable X↾n is supported on at most two values. Hence its conditional Shannon entropy is at most one bit for every such cell, irrespective of the sheet probabilities. In particular a computable dyadic strategy whose posterior n-prefix entropy remains >1 bit at arbitrarily deep output levels for some n cannot be realized as a GLOBAL at-most-two-fibre map without replacing its underlying partitions.

Proof. The conditional support lies inside P_C(n,τ), and conditioning on a refinement cannot introduce new compatible n-prefixes. Entropy of a probability law on at most two atoms is at most log₂2=1. ∎

**Sharp elementary stress test.** Identity has W(n,m)=2^{max(n−m,0)} and hence width 1 once m≥n. Left shift x↦x₁x₂… has W(n,m)=2^{1+max(n−m−1,0)} for n≥1, hence width 2 once m≥n−1. Even-coordinate projection x↦x₀x₂x₄… has W(n,m)=2^{n−min(m,ceil(n/2))}, hence persistent width 2^{floor(n/2)} for m≥ceil(n/2). For n=4 this is 4, so no global two-fibre map has that *same* partition tree; its posterior n-prefix entropy is floor(n/2), not 1. All three maps are total and fair. The even projection's unbounded fibres are a genuine global failure, not a numerical approximation.

## 2. Necessary-and-sufficient decision criterion

A **width-two betting tree** means such a computable dyadic filtration C with condition (c), together with a total computable nonnegative rational-valued binary martingale d. Say it catches x when sup_m d(T_C(x)↾m)=∞.

**Theorem 3 (exact universal-test reduction).** Fix any universal Martin-Löf test (U_j)_{j∈ω}, with N=∩_j U_j the class of non-Martin-Löf-random sequences. Then:
(1) R₂ is exactly the class of x caught by NO width-two betting tree.
(2) R₂=MLR if and only if **each x∈N** is caught by SOME width-two betting tree (the tree and martingale may depend on x).
(3) MLR⊊R₂ if and only if **some x∈N** is caught by NO width-two betting tree.
In (3) the witness is automatically computably random, because the identity filtration is width one and its output martingales include every ordinary computable martingale.

**Proof.** By Theorem 1, a width-two filtration is exactly a total computable fair map with global fibres at most two. By the computable martingale characterization of CR, an output is not CR precisely when some total computable nonnegative rational martingale succeeds on its output prefixes. Taking every pair (C,d) proves (1) directly, including CR of x via the identity. MLR⊆R₂ is frozen from randomness conservation, so the two alternatives in (2)–(3) follow by complementation relative to N. ∎

**Corollary 4 (test for a proposed universal pair; only sufficient).** If the two SRC-0071-style computable fair partition strategies for a universal ML test can be chosen so that BOTH satisfy Theorem 1's uniform global width-two condition and their computable winning martingales catch every x∈N, then R₂=MLR. The same holds for any finite or countable family satisfying those precise requirements. No converse asserting a finite pair from R₂=MLR is proved. In particular the actual SRC-0071 preprint pair cannot be simply assumed to satisfy this condition: its maps have unbounded fibres in the reviewed S083 calibration.

**Non-repair observation.** If a proposed strategy's map F has an output fibre of size at least three, composing F with a computable output homeomorphism and/or precomposing with a computable input homeomorphism leaves the fibre size unchanged. Postcomposing with any deterministic map cannot reduce it. Thus re-encoding *the same* strategy by homeomorphisms or changing only its capital schedule cannot yield the required width-two filtration. To follow Route A one must change the source partition geometry while proving success is retained. This is a global obstruction to a specific compilation method, not an impossibility proof for ALL bounded-width universal strategies.

## 3. Routes attempted and exact limitations

**Route A.** Attempted to transfer SRC-0071's universal pair by replacing its output martingales or by a homeomorphic relabeling. Theorem 1 and Corollary 4 expose the missing requirement: bounded compatible raw prefixes **uniformly over every output cell**. Since fibre cardinality is unchanged by the proposed recodings, this does not supply a universal width-two pair. Neither an arbitrary non-MLR source nor the universal ML test was assigned a correct global-width-two destroying map.

**Route B.** Theorem 3(3) is an exact diagonalization specification, but no x was built avoiding every width-two betting tree. Verification against the S083 tail-coded T* class or even all finite-block recodings would not suffice for this quantifier. As S084 proves, on infinitely resolving T* transcripts from any putative R₂ source, the entire prediction-error stream must be computably random and have limiting mistake frequency 1/2. A single wrong prediction is insufficient; no diagonal construction meeting this condition and the global k=2 tests was obtained.

**Status/meaning.** Theorem 1's map/width equivalence is derived from S003/S007; Theorem 3 is the fully quantified reformulation of R₂ plus the universal ML test, NOT a proof of universality. Corollary 2 supplies a quantitative global obstruction for any *given filtration*; it is not an impossibility theorem for all alternative filtrations. These results refine the exact decision problem but DO NOT satisfy the stronger requested decision of R₂=MLR or MLR⊊R₂. There is no established independent no-go for ALL possible width-two universalization schemes. Preserve these limitations in the handoff.

No escrow, hazards, residues, unit columns, record-only z₀, multi-hole variants, changes to Y/M/H/X, or use of S057. R₂ versus OH^iso, U(H), X∈OH and fixed-S preservation stay separate and unresolved. No novelty, openness, priority, Gate-4, publication or outreach claim.
