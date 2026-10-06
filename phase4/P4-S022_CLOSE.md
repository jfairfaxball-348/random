# P4-S022 close

Date: 2026-10-06
Session: P4-S022
Incoming checkpoint: 2abc3b536272fd5c8f903d8087e0328212445d11
Scope: selected CAND-01; k=2 anti-Zeno / boundary-isolation searchability only
Status: **COMPLETED**

## Result

P4-S022 gives a positive local anti-Zeno searchability theorem and identifies its exact effective limit.

Starting from the settled P4-S021 scale-tail hypotheses plus set-theoretic loss-properness, the already-computed bad-capital loss bound U(K), together with the large-loss waiting modulus R(K,n), yields a computable global scale-exhaustion depth G(K,n): after G(K,n), no payout at least (2^{-n}) can occur anywhere in (B_K).

At such an n-quiet node v, the P4-S021 subscale bound gives a computable residual future-loss cap

[
Q(K,n,v)=max{0,T(K,n)-E_{<n}(v)}.
]

Hence

[
E(v)+Q(K,n,v)<m
]

is a finite computable certificate that no continuation of v inside (B_K) reaches the queried integer boundary m.

If every false Reach(K,m) instance eventually admits a finite scale n whose entire scale-exhaustion frontier has this strict residual gap and contains no earlier witness, then exact Reach is decidable: dovetail ordinary positive witness search with the finite strict-separation certificate search.

The proposed local “must cross within computable finite depth” arm is unnecessary. Reach already has c.e. finite witnesses, so the only missing effective content is a positive certificate for the negative Bar(K,m) side.

There is also an unavoidable limitation. P4-S020 proved that decidable Reach, positive semidecidability of Bar and a computable witness modulus D(K,m) are equivalent. Therefore the P4-S022 strict-gap condition is weaker only as primitive local certificate data; once it decides all exact boundaries it compiles back into D. No condition can make Reach decidable while remaining strictly below D in final computability strength.

The P4-S021 geometric halting construction is the sharp witness for strictness. On a nonhalting selected-e branch, after every finite stage the exact computable residual geometric tail equals the remaining gap to (m_e=2e+2). If the machine halts, one finite correction reaches (m_e). Thus nonstrict control (E+Qle m), even with Q effectively tending to zero and every fixed loss scale exhausted by a computable deadline, leaves halting information intact.

The settled one-sided-trigger harmonic account satisfies boundary isolation on each fixed bad-capital tree while retaining a divergent global absolute premium sum, so the condition does not restore P4-S016 premium summability.

P4-S011 fails before this boundary question under global admissibility: P4-S021 already shows that for one fixed bad-capital K and every n its sub-(2^{-n}) realized loss is unbounded on the computably random target completion, so no finite T(K,n) exists. Bare admissibility remains unruled-out.

P4-S005 through P4-S021 remain settled. P4-S011 and P4-S015 through P4-S021 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Phase 4 remains OPEN. Phase 5 remains CLOSED. Owner/external blocker: **NONE**.

Validation: phase4/P4-S022_VALIDATION.md.

## Next bounded task

P4-S023 should stay strictly at k=2 and test only whether P4-S021's strong effective tail convergence plus the **semantic** anti-Zeno condition excluding any bad-capital branch whose loss converges to an integer boundary from below without finite attainment automatically yields a searchable strict frontier gap by effective compactness. Otherwise isolate an incompatible-branch shrinking-scale halting construction. Check P4-S011 explicitly.
