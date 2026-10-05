# P4-S009 close

Date: 2026-10-05
Session: P4-S009
Incoming checkpoint: 90f4441e1edde8f1c3a4e85652c2514e18cb77ac
Scope: selected CAND-01; k=2 singleton moving-hole / dynamic-sentinel boundary only
Status: **COMPLETED**

## Result

P4-S009 sharpens the P4-S008 singleton moving-hole obstruction without resolving the general scan-preservation question.

For a finite scan transcript tau and a fresh proposed sentinel j, the continuations avoiding j form a computable binary tree. If every continuation eventually consumes j, that tree is finite and a uniform finite consumption deadline is computably searchable. If no such deadline exists, König's lemma supplies a sibling continuation that omits j forever; under global k=2 that sibling queries every other coordinate.

When a finite deadline H is available, the apparent pre-revelation loss can be eliminated completely. Query j first, simulate T until it consumes j, and define the completion-stream capital as the finite conditional expectation of d's terminal capital after the j-step. This is a computable fair martingale starting at d(tau) and ending at exactly the post-consumption d-capital. Thus bounded sentinel turnovers can be concatenated with no factor-two loss.

The unresolved singleton case is therefore exactly the branchwise-avoidable case: the target consumes each moving hole, but another continuation can keep that hole forever, preventing a computably certified terminal horizon. Finite-horizon portfolio splits have tail weights tending to zero, so across infinitely many turnovers no rate-free lower bound follows from output-martingale unboundedness alone. Savings/restart does not compute the missing unbounded deferred-wager value.

A simple globally k=2 fair-coin singleton-spine comb shows that infinitely many avoidable-but-consumed holes are combinatorially compatible with the fibre constraint, but its naive spine fixes bits on a computable control set and is not computably random. No adaptive replacement with full freshness/non-pre-revelation checks is completed, and SRC-0061 is not reused.

Accordingly, no exact k=2 randomness-destruction witness and no full global-k=2 scan preservation theorem is established.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard, P4-S001 through P4-S008 and DEF-0020 are preserved exactly. No conclusion is made for k>2. Gate 4 is NOT REVIEWED. Phase 5 remains CLOSED. No owner/external blocker exists.

Validation: phase4/P4-S009_VALIDATION.md.

Next: P4-S010, still bounded to k=2, on the branchwise-avoidable deferred-wager value isolated here: determine whether the capped eventual-consumption/threshold value has enough computable tail control to yield an optional-projection martingale, or whether an exact adaptive singleton-spine scan can encode the missing tail while retaining a computably random winning source.
