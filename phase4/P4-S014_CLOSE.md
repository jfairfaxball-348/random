# P4-S014 close

Date: 2026-10-06
Session: P4-S014
Incoming checkpoint: 50d9e2154e7e6dea34d804a1270905a097110d78
Scope: selected CAND-01; k=2 computably budgeted avoidance-tail boundary only
Status: **COMPLETED**

## Result

P4-S014 establishes a preservation theorem strictly between P4-S013 finite deadlines and P4-S011 arbitrary branchwise avoidance.

For each reachable least-fresh epoch state s, choose a total computable finite horizon H(s). Let p(s) be the exact conditional fair-coin probability that the epoch still has not triggered after H(s) fillers. If there is one finite computable budget B bounding the pathwise sum of p(s) over all reached epoch states on every run, then every computable output-martingale win transfers to one computable source martingale.

The transfer uses a single globally exhaustive sentinel-first adaptive-permutation completion. One completion martingale buys a fair unit ticket at each epoch paying 1 on a horizon miss; the pathwise tail budget keeps its reserve nonnegative and infinitely many misses make it succeed. A second completion martingale uses the P4-S009 finite conditional-expectation hedge only through H(s). If the horizon is met it tracks the deferred sentinel wager exactly; after a miss it copies subsequent filler bets, skips at most the one already-revealed sentinel wager when that epoch eventually triggers, and restarts. Thus finitely many misses are harmless, while a permanently nontriggering missed epoch is also harmless because the second martingale then copies the output martingale forever on fillers.

The sum of the two completion martingales therefore succeeds whenever the output martingale succeeds. The sentinel-first completion is a computable fair-coin-preserving bijection with computable inverse even on permanently avoiding siblings, so P4-S001 transfers the win to one computable source martingale.

The exact pathwise finite budget on p(s) is the weakest effective summability condition established here. A preassigned computable summable sequence epsilon_r bounding each r-th epoch tail is sufficient but stronger. No convergence modulus for the infinite-horizon trigger probability and no exact optional projection are used.

The condition is strictly weaker than P4-S013. A zero-stake functional which, on sentinel j, scans j+1,j+2,... until seeing the first 1 has an infinite all-zero avoiding sibling at every reached epoch. Taking H_r=r+2 gives miss probability 2^{-(r+2)} and total budget at most 1/2.

P4-S011 necessarily violates the P4-S014 condition. Otherwise its successful output martingale would transfer to a computable martingale succeeding on its computably random source, contradicting the settled P4-S011 theorem.

No absolute necessity of the budgeted-tail condition is claimed. The smallest remaining refinement is whether raw tail probabilities may be nonsummable while a computable stake-weighted skipped-wager loss budget is summable.

P4-S011, P4-S012 and P4-S013 remain unchanged. P4-S005 through P4-S013 remain settled. PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Owner/external blocker: **NONE**.

Validation: phase4/P4-S014_VALIDATION.md.

Recommended next bounded session: P4-S015, still at k=2 and inside the least-fresh stake architecture, testing only a computable stake-weighted weakening of the P4-S014 unit miss-ticket budget.
