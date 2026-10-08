# P4-S050 Validation

Date: 2026-10-08
Session: P4-S050
Incoming checkpoint: 9d03117f2674bd0a942634520ff4bed0890f5e1b
Mathematics record: phase4/P4-S050_MATHEMATICS.md
Disposition: **PASS — conditional results only**

## Authority and uniqueness
- Live main matched the P4-S049 outgoing hash exactly, and P4-S050 did not exist in the committed tree.
- Read P4-S001–P4-S049, CAND-01 authority, active Phase-4 pivot, and the special-focus P4-S011/P4-S012/P4-S027/P4-S041/P4-S044–P4-S049 records.
- All prior validated mathematics retained; no frozen technical route reopened. PASS.

## Positive witness and four-atom calculation
- If the actual raw pair equalled a refuted square atom, its counterfactual oracle would be the total correctly autoreduced target Y, contradiction. PASS.
- Normalized payoff table in order (a,beta),(a,1-beta),(1-a,beta),(1-a,1-beta): (0,4/3,4/3,4/3). Fair expectation =1.
- First s-query branch capitals 2/3,4/3 have mean 1. On the 2/3 branch, t-query child capitals 0,4/3 have mean 2/3. On the 4/3 branch, zero-stake t-query preserves 4/3.
- All values nonnegative, rational, query-order compatible, and known before the respective wager. PASS.

## Scan implementation
- Four counterfactual simulations mask s,t; any other raw bit needed is acquired by a legal zero-stake support query; other computations are boundedly dovetailed and never awaited indefinitely.
- Timeout always releases t, while preserving s; positive square exit queries s then t; positive old exit consumes s and zero-stake releases t.
- In infinitely many exits the least-unread old sentinels are all eventually consumed. In finitely many exits, the final epoch's least-unread sweep consumes all coordinates except possibly its s. Hence global <=1 omitted coordinate and global fibre size <=2. PASS.
- Adaptive no-repeat scanning gives fair-coin output cylinders of measure 2^{-m}; decisions are computable from the finite transcript. PASS.
- Concrete scheduler check: global round N increases, per-reservation tenure L(e,k)=2^{e+k+2} is finite, every round executes bounded first-N simulations, support/sweep output rounds alternate, and timeouts consume t. The mandatory sweep and unbounded N guarantee old-witness eventual detection in a final no-exit epoch without claiming square-certificate timing control. PASS.

## Success and limiting quantifiers
- Each executed captured square gives factor 4/3; each positively refuted old branch gives factor 2. All other wagers have factor 1. Infinite exits force unbounded capital for the *single fixed computable* output martingale. PASS.
- Under hypothetical X in OH, each fixed combined policy must have finitely many exits; its final sentinel is old-refutation-free by exhaustive c.e. fair dovetail and has no further timely square capture. This is algorithm-relative, not a global square-event nonexistence theorem. PASS.
- A lone pair exclusion cannot guarantee strict gain on t alone while s stays unread: the two allowed outcomes in row 1-a defeat any such fair one-bit payoff. PASS.
- An arbitrary passive policy's infinitely many square observations do not automatically give infinitely many completed pair hedges. The conditional theorem explicitly restricts to executing square-exit policies. PASS.

## Guard audit
- No infinite capture for the committed source established.
- No unconditional X not in OH, no X in OH, no OH non-invariance, no strict R_2 vs OH separation.
- R_2 subseteq OH^iso subseteq OH retained. PA-0001 unresolved under inspected evidence, DEF-0020 unchanged, Phase 4 OPEN and Phase 5 CLOSED. PASS.

Overall result: **VALIDATED**, with the effective capture-and-reset obstacle explicitly unresolved.
