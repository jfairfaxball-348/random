# P4-S023 — semantic anti-Zeno plus uniform effective tail convergence

Date: 2026-10-06
Session: P4-S023
Incoming checkpoint: 6cae7e038730450463293da2559a0a31ead04daf
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 least-fresh ticket/restart architecture only

Result: **UNDER THE STRONG P4-S021 TAIL FORM — COMPUTABLE GLOBAL EXHAUSTION OF EVERY FIXED POSITIVE LOSS SCALE TOGETHER WITH A COMPUTABLY AND UNIFORMLY VANISHING SUBSCALE TAIL — THE SEMANTIC ANTI-ZENO CONDITION FORCES P4-S022 SEARCHABLE STRICT FRONTIER SEPARATION. IF FALSE Reach(K,m) HAD NO STRICT FRONTIER GAP, NEAR-m BAD-CAPITAL NODES AT FINER AND FINER QUIET SCALES WOULD HAVE A COMPACT DIAGONAL LIMIT. UNIFORM TAIL CONVERGENCE FORCES THAT LIMIT BRANCH TO HAVE LOSS m, WHILE FALSE Reach KEEPS EVERY FINITE PREFIX BELOW m. THIS IS EXACTLY THE FORBIDDEN NONATTAINING ZENO BRANCH. HENCE Reach(K,m) IS DECIDABLE UNDER THE PROMISE AND P4-S020'S WITNESS MODULUS IS RECOVERABLE. AN INCOMPATIBLE-BRANCH HALTING ESCAPE CANNOT SATISFY ALL OF THESE HYPOTHESES.**

## Authority, uniqueness and scope

Live main matched the requested checkpoint exactly before substantive work. The incoming tree contained P4-S001 through P4-S022 and no P4-S023 mathematics, close or validation record; repository search likewise found no committed P4-S023 record. The session identifier was unused.

P4-S001 through P4-S022 and required CAND-01 selection/Gate-3 authority were read. P4-S005 through P4-S022 are treated as settled. P4-S011's exact global-k=2 destroyer and P4-S015 through P4-S022 are preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. This session stays strictly at k=2. No novelty, Gate-4, publication or outreach claim is made.

## 1. Strong P4-S021 tail form

Keep the settled notation:

- E(v) is cumulative realized positive skipped gain;
- W*(v) is running maximum ticket capital;
- B_K = {v : W*(v)<K};
- Reach(K,m) means that some v in B_K has E(v)>=m.

P4-S021's boundary construction had a stronger property than its basic positive theorem, and P4-S022 made the associated fixed-scale frontiers explicit. P4-S023 assumes exactly that strong form.

For every K and n there are computable data:

1. a global exhaustion depth G(K,n) after which no continuation inside B_K realizes a payout at least 2^-n; and
2. a rational bound T(K,n) on the total contribution of payouts below 2^-n in B_K,

with T(K,n) tending effectively to 0 as n tends to infinity for fixed K.

Replace G by the computable monotone closure

Ghat(K,n)=max(n,G(K,0),...,G(K,n)).

At an n-quiet node v, P4-S022's residual cap is

Q(K,n,v)=max(0,T(K,n)-E_<n(v)).

Every continuation w of v which remains in B_K satisfies

0 <= E(w)-E(v) <= Q(K,n,v) <= T(K,n).

The last inequality is the uniform Cauchy control used below.

## 2. Semantic anti-Zeno

Fix an integer boundary m.

The bad-capital tree is **semantically anti-Zeno at m** when there is no infinite branch X through B_K such that every finite prefix has E<m while the prefix losses converge to m.

This is only a semantic promise. No algorithm deciding whether the anti-Zeno property holds is assumed.

The question is whether strong effective tails make that semantic promise sufficient to find the P4-S022 strict frontier certificate whenever Reach(K,m) is false.

## 3. Uniform tails give a continuous branch-limit loss

### Lemma 1 — uniform convergence

For every infinite branch X through B_K, the monotone sequence of prefix losses has a finite limit L_K(X). If s is at or beyond Ghat(K,n), then

0 <= L_K(X)-E(X at s) <= T(K,n).

Therefore convergence to L_K is uniform over all bad-capital branches and has a computable modulus.

Proof. After the n-quiet frontier every future payout is below 2^-n, and the entire contribution at that subscale is bounded by T(K,n). Since T(K,n) tends to zero, the prefix-loss process is uniformly Cauchy. QED.

At every fixed finite depth, prefix loss is locally constant on branch space. Hence L_K is the uniform limit of finite-prefix functions and is continuous on the compact path space [B_K].

## 4. Semantic anti-Zeno forces a strict compactness gap

Assume Reach(K,m) is false. Every finite bad-capital history then has E<m. A branch limit cannot exceed m: if it did, monotonicity would force a finite crossing.

Semantic anti-Zeno removes equality, so every infinite branch X satisfies L_K(X)<m.

Classically, continuity on compact [B_K] already implies that the supremum of L_K is strictly below m. The effective issue is whether the corresponding gap is searchable. It is.

### Theorem 2 — searchable strict frontier separation

Under the strong tail hypothesis and semantic anti-Zeno at (K,m), if Reach(K,m) is false then for some n:

1. no bad-capital node through depth Ghat(K,n) has E>=m; and
2. every bad-capital node v at depth Ghat(K,n) satisfies E(v)+Q(K,n,v)<m.

This is exactly the P4-S022 strict frontier certificate, with the harmless monotone closure of the frontier depth.

Proof. Clause 1 is automatic from false Reach. Suppose clause 2 failed for every n. Choose v_n at depth Ghat(K,n) with

E(v_n)+Q(K,n,v_n) >= m.

Because Q<=T,

m-T(K,n) <= E(v_n) < m.

Thus these finite histories have losses approaching m from below, while their depths tend to infinity.

The tree is finitely branching. By the standard compactness/diagonal argument, choose a subsequence converging to an infinite branch X through B_K: for every fixed depth d, all sufficiently late chosen nodes have the same prefix X at depth d.

Fix r. For sufficiently late chosen nodes, their depth is beyond Ghat(K,r) and they extend X at depth Ghat(K,r). Since that prefix is r-quiet,

E(v_n)-E(X at Ghat(K,r)) <= T(K,r).

Together with E(v_n)>=m-T(K,n), and then letting n tend to infinity along the subsequence, this gives

E(X at Ghat(K,r)) >= m-T(K,r).

Let r tend to infinity. Since T(K,r) tends to zero, the branch limit is at least m. False Reach gives the reverse inequality and keeps every finite prefix strictly below m. Hence X has loss converging to m from below without finite attainment, contradicting semantic anti-Zeno. QED.

This proof directly handles the proposed incompatible-branch escape. The near-boundary nodes need not initially lie on one branch. Uniform tail convergence prevents a late side branch from adding substantial loss after it diverges from a common prefix, so compactness turns arbitrarily fine incompatible near-boundary nodes into one forbidden Zeno branch.

## 5. Exact Reach is decidable under the semantic promise

### Theorem 3 — semantic anti-Zeno plus strong effective tails decides Reach

Dovetail two searches.

- Positive search: enumerate finite bad-capital histories until one with E>=m appears.
- Negative search: for n=0,1,2,... compute the finite tree through Ghat(K,n) and test the P4-S022 strict frontier certificate.

If Reach is true, the positive search halts. If Reach is false, Theorem 2 guarantees that the negative search halts. The strict certificate is sound, so the outcomes cannot conflict.

The algorithm does not receive an anti-Zeno modulus; semantic anti-Zeno is used only to prove termination on false instances.

By P4-S020's settled equivalence, decidable Reach uniformly recovers a computable witness modulus D(K,m): on a true instance enumerate until a witness appears and return its depth; on a false instance return any default depth.

Thus P4-S023 respects P4-S022's final-strength limitation. The gain is that the effective strict-gap certificate is now derived from a semantic condition plus strong uniform tail convergence rather than supplied as primitive data.

## 6. No incompatible-branch halting construction under the strong hypothesis

The negative alternative requested for P4-S023 would require all of the following:

- strong uniform effective tail convergence;
- false Reach(K,m);
- semantic anti-Zeno on every bad-capital branch; and
- failure of every searchable strict frontier gap.

Theorem 2 shows that these four requirements are inconsistent.

Any attempted moving-branch coding which defeats every strict frontier supplies near-m nodes at finer quiet scales. Their compact diagonal limit is a bad-capital branch. Uniform tail convergence forces the loss of that limit branch to be m. False Reach says the boundary was never attained finitely. The result is a forbidden Zeno branch.

Therefore incompatibility of the finite near-boundary nodes is not enough to hide halting information while the strong uniform tail property is retained.

## 7. Relation to P4-S021's geometric halting example

P4-S021's geometric machine-tail construction remains the sharp one-branch obstruction under tail control alone.

On its nonhalting selected-e branch, loss stays below m_e at every finite stage while the exact remaining geometric mass equals the current gap and tends to zero. Hence that branch converges to m_e from below without finite attainment.

It therefore fails the P4-S023 semantic anti-Zeno hypothesis exactly where its halting information lives. If the machine halts, the remaining residual is paid by a finite correction and the boundary is reached.

P4-S023 does not reopen or alter that construction. It proves that once such Zeno behavior is semantically excluded and convergence is uniform over the whole bad-capital tree, no incompatible-branch variant survives.

## 8. Absolute premium summability is not restored

The settled one-sided-trigger harmonic account remains a calibration example. For each fixed bad-capital level its E/W* relation gives effective bad-capital control, fixed positive loss scales are exhausted effectively, and its remaining bad-capital tail vanishes effectively. Its bad-capital branches do not exhibit a nonattaining integer-boundary Zeno limit.

Nevertheless its unbounded all-trigger run retains the divergent harmonic exact-premium sum. Thus P4-S023 does not restore P4-S016 absolute premium summability.

## 9. Explicit P4-S011 check

Let Y be the settled P4-S011 computably random source and fix any computable horizon selector. Suppose, as in P4-S019 through P4-S022, that a finite reserve makes the associated canonical full-ticket account globally admissible.

P4-S016 gives divergent realized skipped gain on the sentinel-first completion C(Y). Global admissibility makes the full-ticket account a total nonnegative computable martingale, so its running capital is bounded on that computably random completion. Choose K above that bound.

P4-S021 already proves that for every n the cumulative realized gain contributed by terms below 2^-n is unbounded along prefixes of C(Y) remaining in B_K. Consequently no finite T(K,n) exists, much less an effectively vanishing family.

Therefore P4-S011 fails before the P4-S023 semantic anti-Zeno theorem applies. Its exact k=2 destroyer is unchanged. The settled stronger failure of set-theoretic loss-properness under global admissibility is preserved. Bare admissibility remains unruled-out.

## 10. Exact boundary after P4-S023

P4-S023 closes the semantic anti-Zeno question posed by P4-S022.

Positive result:

- strong P4-S021 uniform tail convergence makes bad-capital loss uniformly Cauchy;
- the branch-limit loss is continuous on compact branch space;
- false Reach plus semantic anti-Zeno puts every branch limit strictly below m;
- failure of a finite strict frontier gap would compactify to a forbidden branch with limit m;
- therefore a strict P4-S022 certificate is eventually found;
- exact Reach is decidable and P4-S020's witness modulus is recoverable.

Negative alternative excluded:

- an incompatible-branch shrinking-scale halting construction cannot retain the strong uniform-tail and semantic anti-Zeno hypotheses while defeating all strict frontiers.

The next sharpness question is whether the **uniform** effective tail hypothesis can be weakened. P4-S023 does not address merely pointwise or nonuniform branchwise convergence.

## Successes and limits

Successful:

1. Semantic anti-Zeno plus strong uniform effective tail convergence forces searchable strict frontier separation.
2. Exact Reach is decidable under that promise.
3. P4-S020's witness modulus is recovered as required by the settled equivalence.
4. Incompatible finite near-boundary branches cannot evade the theorem.
5. P4-S021's geometric halting example is located exactly outside the theorem through its Zeno branch.
6. Divergent absolute premium sums remain compatible with the new boundary.
7. P4-S011 is checked explicitly and fails the strong tail hypothesis before anti-Zeno is relevant.

Not claimed:

1. No decision procedure for the semantic anti-Zeno promise itself is supplied.
2. No theorem is proved for merely pointwise or nonuniform branchwise tail convergence.
3. No new randomness-destruction witness is claimed.
4. No settled P4-S005 through P4-S022 result is reopened.
5. No result is claimed for k>2.
6. No novelty, Gate-4, publication or outreach claim is made.

## Preserved boundaries

P4-S005 through P4-S022 remain settled.
P4-S011's exact k=2 destroyer is unchanged.
P4-S015 through P4-S022 are preserved exactly.
PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
DEF-0020 is unchanged.

## Next bounded question

P4-S024 should remain strictly at k=2 and test only the sharpness of the uniform-tail assumption: whether semantic anti-Zeno still forces searchable strict frontier separation under a strictly weaker pointwise or branchwise effective tail-convergence hypothesis, or whether an exact incompatible-branch comb can then hide halting information while every individual bad-capital branch remains non-Zeno. Check P4-S011 explicitly.
