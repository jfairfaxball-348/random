# P4-S090 — Nonlinear self-reading defeats countable-coset robustness

Date: 2026-10-10. Phase 4 Mathematics ONLY; selected CAND-01.
Incoming main: `560f8a1e16a69aaf98a6b8328bfc893b09398d30`.

**Disposition: the authorized alternative (C) is proved. R₂ ⊊ R₂^{cdz}, and OH^iso ⊊ OH^aff. R₂ versus MLR remains unresolved.**

There is z ∈ R₂^{cdz} ∖ MLR and a total computable one-hole scan T of K_mix(z) such that every prediction made by T on this source is correct and T makes infinitely many predictions. Thus

  G_* := F_T ∘ K_mix ∈ F₂,  G_*(z) ∉ CR,  K_mix(z) ∉ OH.

The map destroys the selected source on a singleton fibre. It is not one of the CR-preserving fixed-hold maps. No spectral gap or Conjecture R is assumed. The essential addition to S088/S089 is a uniform conditional separation estimate, together with a small **control-only stall cover** compatible with every true-run state. This defeats the beacon-mimic obstruction without demanding deterministic separation by each parity.

## 0. Entry, review and frozen authority

Git `ls-remote` and an independent GitHub API `git/ref/heads/main` read both returned the incoming SHA. Its parent is `0009e00dff9d75b70539e513e544f4b89b8040f4`, the S088 outgoing SHA. S089's close record identifies its outgoing checkpoint as its own atomic close commit; commit metadata identifies that commit as the incoming SHA. No discrepancy. There was no S090 record or session branch at entry; pre-existing S090 mentions were forward handoffs only. The repository handoff is archived in `P4-S090_INCOMING_HANDOFF.md` (the repository text, not a claim of byte identity with the user's formatting).

Review used the cumulative authority and outcome records for S001–S089, with targeted checks of S003–S008, S011–S012, S032–S033 and S081–S089. The proof dependencies below were read in detail: S082 potentials, savings and compactness; S083 class separation and fooling; S084 predictable errors and restart argument; S087 dispersal and counting obstruction; S088 Theorem C and Proposition D; S089 mathematics, validation, close and audit. CAND-01 selection, Gate-3 PASS and both Phase-4 pivots were checked. This is not a claim to have re-proved all historical results.

Source access is unchanged: SRC-0015, SRC-0019, SRC-0060, SRC-0069 and SRC-0071 remain STATEMENT_INSPECTED, with the particular proofs previously read recorded in their existing notes; SRC-0070 and SRC-0072 remain ABSTRACT_INSPECTED. SRC-0071's journal version remains METADATA_ONLY. No external literature was fetched or promoted. R_tot = MLR remains the S083 programme deduction from the inspected preprint.

All S001–S089 theorems, including S089's conditional statements and experiment/theorem distinction, are preserved. Original CR Y, unchanged globally use-clipped self-avoiding wtt M, repeated H with A=[101;110;111], and X=H⁻¹(Y) are untouched. PA-0001, DEF-0020 and the gates are unchanged. No prohibited detour is used.

## 1. Restricted parity runs still survive every CDZ₂ observer

Use S088's conventions: a_j=x_{2j}, b_j=x_{2j+1}, and CDZ₂ consists of the total computable fair maps of global fibre size at most two whose double-fibre difference vectors occupy countably many cosets of the density-zero subgroup, almost surely on outputs. Use exactly S088's enumeration of strategies, validity set V, savings transforms, weights, Ψ, γ, Φ and Γ. V need not be computable or arithmetical. Guessed runs are computable; their true branch is selected non-effectively as in S088.

Fix a computable injection ι from nonempty finite binary strings into ℕ. For each string s put

  D_s = {j ≥ 0 : v₂(j+1)=ι(s)}.

These are disjoint computable arithmetic progressions of positive density in the **data index** j. Every constraint used below has the form

  L(b)=⊕_{j∈J}b_j=β,

where J is finite and nonempty. Along a run, consecutive supports satisfy

  min J_next ≥ max J_previous + 2.                         (1)

At stage i of R(ε), restrict every candidate support to D_{ε↾(i+1)}. Constraints involve no control coordinate a_j. All support choices and values are determined by the finite guessed run, not by the source subsequently selected.

**Lemma 1 (positive-density pool version of S088 Lemma C3).** Its dispersal conclusion remains valid if all candidate functionals must be supported on odd raw coordinates {2j+1:j∈D_s}, above any prescribed finite cutoff.

*Proof.* Choose the same finite set Q of dominant cosets as in C3, and write d=|Q|. Enumerate the allowed raw coordinates above the cutoff and partition them into H groups of d+1 successive allowed coordinates. In each group choose a nonempty subset whose parity annihilates every v∈Q, by the same d-dimensional linear dependence argument. The group supports are disjoint.

For a density-zero error vector u, the number h of groups meeting supp(u) is at most the number of its nonzero coordinates below the last group endpoint. Since the pool is an arithmetic progression, that endpoint is O(H), with a constant depending on s,d and the fixed cutoff. Consequently h/H→0. The probability that two of N uniformly chosen distinct groups meet supp(u) is at most binom(N,2)(h/H)². Dominated convergence under each finite measure (2+B_∞^e)λ, plus the discarded-coset mass, gives the original C3 conclusion. Nothing requires Q or a density convergence modulus to be computable. ∎

**Construction.** Use Theorem C's stage lengths ℓ_i=2i+2, N_i=3·2^{i+3}ℓ_i and ε_i=2^{−(i+4)}/ℓ_i, including its exact candidate-tuple/time search and minimizing choices. Restrict candidate tuples to the pool just specified, and impose the cutoff (1) relative to the previously chosen support. No spacing condition between the alternative candidates in one tuple is needed. Once one is selected, the next search starts beyond its maximum plus one unused data position.

The search remains a dovetailed Σ⁰₁ search over finite candidates and finite successful computations. Invalid guesses may hang. Syntactically reject malformed computations; every completed run still adds the prescribed number of independent, nonempty, disjoint data constraints.

**Lemma 2 (invariant, null class, and compatibility).** Let ε* be the characteristic sequence of V, P_i^* the true stage-i state, and S=⋂_i P_i^*. Then:

1. Every true stage completes, and Φ(P_i^*,τ_i^*)<2−2^{−i}.
2. Every length-m completed run fixes m(m+1) independent data parities, hence has measure 2^{−m(m+1)}. The unions over all length-m completed guesses form an ML test, with measure at most 2^{−m²}. In particular S∩MLR=∅.
3. For any completed run and any P_i^*, each of its parity constraints either is an identical, same-valued constraint already in P_i^*, or its support is disjoint from every support in P_i^*. All its distinct constraints have disjoint supports.
4. Conditioned on P_i^*, the entire control sequence a remains fair and independent of the constrained data sequence b.

*Proof.* Lemma 1 supplies exactly the halting estimate required in S088 Theorem C; C1/C2 give its unchanged invariant and measure calculation. For (3), before the first guess disagreement the runs coincide. Afterwards their stage classes D_s are disjoint from all true-run stage classes: unequal stage lengths give different strings, and equal lengths retain the first disagreement. True-run constraints not yet in P_i^* lie strictly beyond its supports. This is S083 class separation applied to whole supports rather than individual coordinates. Item (4) follows because P_i^* is defined solely by parities of b. ∎

This lemma alone is not the session's result. The next sections construct and validate an observer that defeats a point surviving **all** CDZ₂ strategies.

## 2. Uniform conditional readability in K_mix

Retain exactly S088's causal fair homeomorphism

  (K_mix x)_{2j}=a_j,
  (K_mix x)_{2j+1}=b_j⊕b_{j−2}⊕(1⊕a_j)b_{j−1},

with b_{−1}=b_{−2}=0. Hold the virtual data bit at raw virtual coordinate h=2q+1. The two inverse completions have the same controls and data difference

  δ_j^q=0 (j<q),  δ_q^q=1,
  δ_j^q=δ_{j−2}^q⊕(1⊕a_j)δ_{j−1}^q (j>q).               (2)

Its state (δ_{j−1},δ_j) is always one of 01,10,11 after q. Given controls through j−1, δ_j is fair if δ_{j−1}=1, and is 1 if δ_{j−1}=0. For a nonempty data support J above q, write

  s_J(a)=⊕_{j∈J}δ_j^q(a).

This says whether the parity separates the two candidates, and depends only on finitely many controls.

**Lemma 3 (conditional quarter bound and repeated readability).** Suppose J₁,…,J_L are fixed nonempty data supports above q, in increasing order and satisfying (1). Then

  Pr(s_{J_l}=1 | a through max J_{l−1}) ≥ 1/4             (3)

for l>1, for every assignment of those earlier controls. The first support has the same unconditional bound (indeed conditional on a through q). Consequently, for every positive integer r,

  Pr(Σ_{l≤L}s_{J_l}<r) ≤ 2^r(7/8)^L.                    (4)

*Proof.* Let p=max J_l and t=max J_{l−1}. For l>1, p≥t+2. Conditional on controls through t, the probability δ_{p−1}=1 is at least 1/2: condition further through p−2 and use the transition description following (2). On δ_{p−1}=1, the fresh control a_p makes δ_p fair, while every earlier summand of s_{J_l} is already determined. Thus (3) follows. For the first support p>q: if p=q+1 then δ_q=1, and otherwise the same argument applies.

Put S_l=Σ_{k≤l}s_{J_k}. The previous S_{l−1} is measurable from controls through max J_{l−1}. Therefore

  E[2^{−S_l} | past] = 2^{−S_{l−1}}(1−Pr(s_{J_l}=1|past)/2)
                      ≤ (7/8)2^{−S_{l−1}}.

Iterate, then use 1_{S_L<r}≤2^r 2^{−S_L}. Independence of different separation indicators is **not** assumed. ∎

The spacing in (1) is a convenient sufficient condition used in this proof; no necessity claim is made. The essential distinction from S088 Proposition D(ii) is that (3) is conditional on every earlier control assignment, so it can be iterated. A one-shot marginal estimate alone would not justify (4).

## 3. A control-only cover of all permanent stalls

Set r(q,m)=q+2m+4. Choose m_q computably by searching for any positive integer m with L₀=m(m+1)−q−1≥0 and

  2^{r(q,m)}(7/8)^{L₀} ≤ 2^{−q−6}.                     (5)

The rational test is decidable and the search terminates, since L₀ is quadratic and r is linear in m.

Consider the constraints of the true run of length m_q. At most q+1 have min J≤q, since their nonempty supports are disjoint. At least L₀ therefore lie entirely above q. Let H_q be the set of control sequences for which fewer than r(q,m_q) of these latter constraints separate the hold q. It is clopen, although its finite description uses the true validity guesses. By Lemma 3 and (5),

  λ_a(H_q) ≤ 2^{−q−6}.

Let H be the union of the corresponding cylinders on full (a,b) space. Then H is open and, by Lemma 2(4), for every i,

  λ(H∩P_i^*) ≤ (1/32)λ(P_i^*).                          (6)

This is a topological open cover, c.e. relative to V; it is not claimed to be effectively open without V. That suffices for compactness. The **observer** below never uses H, m_q's true guesses, or V: it simulates all finite guessed runs. No extra advice is used in its next-query rule or in the ML test of Lemma 2.

## 4. The computable self-reading one-hole scan

The scan T reads v=K_mix(x). It initially reads control v₀ at zero stake, then holds h=1, with filler frontier M=2. In an ordinary hold state h=2q+1, its read set is [0,M)∖{h}.

At output time t, simulate a computably bounded finite list of runs R(ε), each for t steps. A completed length-m run supplies its m(m+1) parity equations. Only inspect it for qualification once **all** coordinates through its last data support are below M. This ensures the following selection depends on the full finite list of constraints, not a data-dependent truncated choice.

From the already read controls, compute δ^q through that list. Among constraints whose min J>q and s_J=1, take the first r(q,m) in run order; reject the run if fewer exist. Compute the raw inverse prefix b^(0) obtained by setting v_h=0 and using the observed other bits. Each selected equation L_l(b)=β_l implies the held-bit prediction

  ν_l=β_l⊕L_l(b^(0)).                                    (7)

The run qualifies if all these predictions agree. Choose the qualifying run with least fixed computable code. Query h and wager all capital on the common ν. If none qualifies, query M at zero stake and increment M.

After a resolution all bits below M have been read. If M is odd, make M the next hold and set the frontier to M+1. If M is even, first read this control at zero stake, then hold M+1 with frontier M+2. In either case the new hold is odd and strictly larger than the old one. The query following a resolution is determined by the transcript, including a possible single control-reading step.

**Lemma 4 (global legality and fair martingale).** T is total computable, has no repeated queries on any transcript, and every infinite transcript leaves at most one coordinate unread. The associated prediction martingale d_* is total rational computable and fair. Thus G_*=F_T∘K_mix is total computable, fair, and has every fibre of size at most two.

*Proof.* Every step performs only bounded simulations and finite prefix calculations. Every query is a genuinely unread hold, filler, or post-resolution control. If there are finitely many resolutions, fillers eventually query every coordinate except the last hold. If there are infinitely many, the increasing holds and frontiers exhaust every coordinate. The scan-fibre calculation of S008 applies on every transcript, and composition with the fair homeomorphism K_mix preserves the cardinal bound. Before each next bit the prediction and resolution flag are known. Set both martingale children equal at zero-stake steps and set them to 0 and 2d at a prediction step. This is the fair-child identity, even after an earlier error reduces capital to zero. ∎

**Lemma 5 (all holds resolve off H).** If x∈S∖H, every hold reached by T on K_mix(x) is resolved.

*Proof.* At a permanent candidate hold q, the true length-m_q run finishes. Since x∉H_q it supplies at least r(q,m_q) separating constraints above q. Since x∈S they all have their stated values. Hence (7) agrees with the actual v_h for all of them. While the hold persists, the frontier and simulation budget tend to infinity, so this run eventually qualifies. Contradiction to permanence. An earlier qualifying false run may resolve the hold first; this does not affect the assertion. ∎

## 5. False readings remain uniformly small

For q and a completed run ε of length m, define A(q,ε) as follows. Given the controls, select the first r(q,m) separating constraints above q from this run exactly as in §4, and require **all** their equations to fail on b. If there are too few, the event is empty. A(q,ε) is clopen: controls select from a fixed finite list. If the run never finishes, regard the event as empty for its effective enumeration.

**Lemma 6 (relative fooling bound).** Let W be the set of sources on which T makes any incorrect prediction. Then W is effectively open and

  W ⊆ ⋃_{q≥0, ε≠∅} A(q,ε),
  λ(W∩P_i^*) ≤ (1/8)λ(P_i^*)  for every i.                (8)

*Proof.* The actual data equal b^(0)⊕v_h δ^q throughout the inspected prefix. On each selected constraint s_J=1, so (7) is correct iff that equation holds on the actual b. Agreement of all predictions means an incorrect prediction forces all selected equations to fail.

Fix the entire control sequence. The selected constraints now form a deterministic list of r disjoint nonempty data parities. By Lemma 2(3), either one is an identical equation already imposed by P_i^*, making simultaneous failure impossible, or all selected supports are disjoint from every support of P_i^*. In the second case their values are independent fair bits under the conditional data measure, so simultaneous failure has probability 2^{−r}. Integrate over controls; Lemma 2(4) permits this without a change in distribution. The run actually chosen by T may depend on data, but the union bound includes **every** possible run, so no conditional-selection assumption is made.

Finally

  Σ_{q≥0,m≥1} 2^m 2^{−q−2m−4}=1/8.

Wrong predictions are witnessed by finite computations and queried bits, proving effective openness of W. ∎

## 6. The separation theorem

**Theorem 7.** There exists z∈CR∖MLR such that G(z)∈CR for every G∈CDZ₂, but G_*(z)∉CR. In fact K_mix(z)∉OH, and G_* has a singleton fibre at this z. A witness is computable from V′, where V is the same validity set used in §1.

*Proof.* For each valid strategy e use the true-run weight w_e and put L_e=2+4/w_e. Let

  O=⋃_{e valid}{x: ∃t, d̄_e(G_e(x)↾t)>L_e}.

Suppose S⊆O∪W∪H. This is an open cover of the nested compact intersection S. Some P_i^* is covered; compactness then gives a finite subcover, with finitely many capital witnesses (e,t) and finitely many open pieces from W and H. Choose a later true stage j that includes all these e, and a time t above all their witness times and τ_j^*.

On P_j^* outside the selected W/H pieces, some witnessed savings capital previously exceeded 2+4/w_e, and the S082 savings drop bound implies its present value exceeds 4/w_e. Thus the sum of weighted capitals exceeds 4 there. From (6),(8), that region has relative measure at least 1−1/8−1/32=27/32. The domination inequality gives

  Φ(P_j^*,t) > 4·27/32 = 27/8 > 2,

contradicting monotonicity in t and Lemma 2(1). Hence S∖(O∪W∪H) is nonempty; choose z there.

The exclusion of O bounds every valid savings capital and hence every original computable martingale on every CDZ₂ image. Identity observers are included, so z∈CR. Lemma 2 gives z∉MLR. Lemma 5 gives infinitely many resolutions, and z∉W makes all predictions correct. Therefore d_*(G_*(z)↾t) doubles infinitely often. This proves G_*(z)∉CR and K_mix(z)∉OH. Infinite resolution exhausts the virtual coordinates, so its fibre, and hence the G_* fibre, is singleton.

Finally S is Π⁰₁(V), O and H are Σ⁰₁(V), and W is Σ⁰₁. The nonempty class just constructed is Π⁰₁(V), and has a V′-computable path. No finite arithmetical bound on V is asserted. ∎

**Corollary 8 (strictness and non-invariance).**

* R₂ ⊊ R₂^{cdz}. Indeed z∈R₂^{cdz}∖R₂ and therefore G_*∉CDZ₂.
* OH^iso ⊊ OH^aff. The same z lies in R₂^{cdz}⊆OH^aff∩OH^blk but fails OH after the computable fair homeomorphism K_mix.
* R₂^{cdz} is not invariant under K_mix: K_mix(z)∉OH, whereas R₂^{cdz}⊆OH.
* R₂ remains invariant under every computable fair homeomorphism, by S033. No contradiction: the separated class is R₂^{cdz}.

Thus the strengthened landscape includes

  MLR=R_tot ⊆ R_fin ⊆ R_k ⊆ R₂ ⊆ OH^iso ⊊ OH^aff ⊊ OH^blk ⊆ OH^lin3 ⊆ OH=OH_h=R_k^scan ⊊ CR,
  MLR ⊊ R₂^{cdz} ⊆ R₂^{dz} ⊆ R₂^{fd},
  R₂ ⊊ R₂^{cdz} ⊊ R₂^{fd},  R₂^{cdz} ⊆ OH^aff∩OH^blk,

with k≥2, h≥1. All other frozen inclusions stand.

## 7. Scope of the advance and remaining obstruction

**Why the beacon mimic no longer blocks the proof.** No single parity is required to separate the nonlinear partner on every control assignment. A fixed-difference CDZ₂ observer may mimic it on a particular finite control event. Instead (3) holds conditionally after each separated support, uniformly in every earlier control assignment, and (4) makes persistent failure across quadratically many constraints small. Because true states restrict only data, this smallness remains a relative bound at **every** later state. Excluding the union H costs at most 1/32 throughout the compactness proof. The controls of the final z are not assumed to be independently sampled after the construction; their use is entirely through this finite-state relative-measure calculation.

**Why this is not a proof of R₂=MLR.** The proof selects a destroyed z from a particular null class. It does not show that every point in S is destroyed: points in H or with suitably many false readings remain outside its conclusion. Still less does it show that every CR non-MLR point has a construction of this form. No universal family follows, and S086's quantifier distinction is respected.

**S084's full error stream.** For the chosen z, every infinitely resolving observer in any computable affine frame has CR output by CDZ₂ survival; its entire predictable error stream is therefore CR. In the nonlinear K_mix observer just constructed, the infinite error stream is identically zero. This is a genuine destruction, not a proposed R₂ survivor with only one error inserted. No survivor of the union FD₂^{K_mix}∪FD₂^{K′_mix} is established.

**Counting potentials and rigidity.** S082 §6.3 and S087 §6.2's concentration/overcount obstacle is not solved. The survivor half uses exactly the CDZ₂ cheap-split search and does not replace normalized charges by absolute accounting. The destroyer shows that this restricted survival cannot by itself certify R₂ membership. Conjecture R is neither proved nor refuted; S089's conditional mechanism barrier stays conditional. No global impossibility for all guessed-run constructions is claimed.

**Next mathematical target.** R₂=MLR versus MLR⊊R₂ remains decisive. The next session must confront constraints depending on both controls and data, or a different genuinely universal/survival argument. Extending this separation to another fixed frame alone is not the next target.

R₂=OH^iso, U(H), the original X∈OH, fixed-S preservation and the other frozen questions remain separate and unresolved. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No novelty, external openness, priority, publication or outreach claim. No owner/external blocker.
