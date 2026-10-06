# P4-S016 close

Date: 2026-10-06
Session: P4-S016
Incoming checkpoint: 66b77cf8fcb5c6c5feafeb54cd9ce003e2d9342c
Scope: selected CAND-01; k=2 incremental postmiss loss-ticket boundary only
Status: **COMPLETED**

## Result

P4-S016 eliminates the advance computable future-loss envelope required by P4-S015, under a different effective budget.

After the settled finite horizon is missed, use the P4-S014/P4-S015 sentinel-first completion. At any still-unresolved postmiss state, the logical next query is a fresh filler. Before that filler is drawn, simulate both possible filler children. If a child makes the sentinel trigger, the savings-wrapped output martingale's exact positive skipped-sentinel gain on that child is a computable rational; if it does not trigger, assign loss zero. The one-step ticket paying those two child losses has exact fair price equal to their average.

Thus no future supremum or advance majorant is needed. The only new quantitative hypothesis is a finite computable constant uniformly bounding, on every run, the pathwise sum of these automatic one-step fair prices over all unresolved postmiss states.

An insurance martingale funded by that reserve buys every last-chance ticket. If the realized skipped-gain sum diverges, its payouts are unbounded. If the realized skipped-gain sum is finite, the P4-S015 restart hedge loses only the factors 1+ell and therefore retains a positive multiplicative scale while the savings-wrapped output martingale tends to infinity. A permanently nontriggering missed epoch is copied forever. Their sum gives one computable martingale on the exhaustive completion, and P4-S001 transfers it to one computable source martingale.

The local premium is sharp for the one-step architecture: any nonnegative fair one-step hedge which covers both possible next-child losses costs at least their average. No absolute necessity claim is made for more global hedges.

This removes P4-S015's noncomputable-envelope obstruction as an effectivity requirement, but the complete P4-S015 and P4-S016 numerical certificate conditions are not claimed to be ordered: P4-S015 prices risk ex ante at the horizon, while P4-S016 pays conditional premiums along the realized postmiss continuation.

P4-S011 fails the new condition strongly. For every computable horizon selector, finite total realized skipped gain along its computably random winning source Y would already make the restart hedge succeed and contradict Y's computable randomness. Hence the realized skipped gains diverge. Immediately before each missed epoch finally triggers, the last-chance fair premium is at least half the realized loss, so the premium sum diverges on Y itself. No finite uniform premium budget can exist.

P4-S011 through P4-S015 remain unchanged. P4-S005 through P4-S015 remain settled. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Owner/external blocker: **NONE**.

Validation: phase4/P4-S016_VALIDATION.md.

Recommended next bounded session: P4-S017, still at k=2 and inside the same least-fresh stake architecture, testing only whether the absolute pathwise sum budget on last-chance fair premiums can be weakened to a computable self-financing reserve condition.
