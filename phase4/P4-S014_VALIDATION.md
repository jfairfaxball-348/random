# P4-S014 validation

Date: 2026-10-06
Incoming baseline: 50d9e2154e7e6dea34d804a1270905a097110d78
Pre-validation main checked: f2dd7c60a4bf3a5a46a424a94864e20290fc0cf1

Result: **PASS** for uniqueness, k=2 scope discipline, the computably budgeted avoidance-tail theorem, strict weakening of P4-S013, necessary violation by P4-S011, authority synchronization and preserved guards.

## Repository and scope checks

- live main matched the requested incoming baseline exactly before substantive work;
- P4-S014 mathematics, close and validation records were absent on the incoming checkpoint, so P4-S014 was unique;
- P4-S001 through P4-S013 were read as authority;
- P4-S005 through P4-S013 were treated as settled;
- the incoming-to-pre-validation comparison changes only P4-S014 records and current authority/index/summary files;
- no P4-S005 through P4-S013 mathematics/close/validation record appears in the changed-file set;
- synchronized JSON files parse successfully;
- phase3/prior-art.json is unchanged and PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- catalog/definitions.json is unchanged and DEF-0020 is preserved;
- the session stays at k=2 and makes no novelty, Gate-4, publication or outreach claim.

## Mathematical checks

1. **Finite-horizon miss probabilities are computable.**
   - For a reachable epoch state s and computable finite horizon H(s), the P4-S013 avoidance tree A_s is computable.
   - Therefore p(s)=2^{-H(s)}|A_s∩2^{H(s)}| is an exact computable rational conditional probability.

2. **The sentinel-first completion is globally exhaustive.**
   - It physically queries the current sentinel before simulating its logical least-fresh epoch.
   - If the logical epoch never triggers, its fillers enumerate every other coordinate, so the physical completion still queries every coordinate.
   - If all epochs trigger, the least-unqueried argument consumes every coordinate.
   - Hence the completion is a total computable no-repeat adaptive permutation, fair-coin preserving, with computable inverse; P4-S001 applies.

3. **The miss-ticket martingale is fair and total.**
   - The horizon-miss event depends only on finitely many fresh filler bits and is independent of the prequeried sentinel by self-avoidance.
   - A finite indicator ticket has exact fair price p(s).
   - Starting with the supplied finite pathwise budget B_0 and converting p(s) reserve into each ticket never overdraws reserve on any run.
   - Each miss pays one unit, so infinitely many misses force unbounded capital without an independence assumption.

4. **The truncated hedge is exact through the horizon.**
   - Before physically querying the sentinel, define the finite terminal payoff: scaled d-capital immediately after sentinel consumption when triggering occurs by H, otherwise scaled d-capital after H fillers.
   - This is a bounded finite stopping tree, so repeated martingale averaging gives an exact finite conditional-expectation hedge starting at the current completion capital.
   - No infinite-horizon trigger probability or optional projection is used.

5. **Restart after a miss preserves success.**
   - On a miss, terminal hedge capital is the same fixed positive scale of d after H fillers.
   - Beyond H the completion martingale copies d on each fresh filler.
   - If the epoch never triggers, it therefore copies the successful output martingale forever.
   - If it later triggers, the already-revealed sentinel wager is skipped with no physical capital jump; at the next epoch a new scale is computed.
   - On any path where d succeeds, d never reaches zero at a restart state. If only finitely many misses occur, after the last miss the hedge tracks one fixed positive multiple of d forever.

6. **One-martingale dichotomy is complete.**
   - Infinitely many misses imply success of the ticket martingale.
   - Finitely many misses plus output success imply success of the truncated/restart martingale.
   - A permanently nontriggering missed epoch is covered by the latter's filler copying.
   - Their sum is one computable completion martingale succeeding whenever d succeeds.
   - P4-S001 effective-isomorphism transfer therefore yields one computable source martingale.

7. **The condition is strictly weaker than finite deadlines.**
   - For the zero-stake functional which searches j+1,j+2,... for the first 1, every reached epoch has the all-zero infinite avoiding sibling, so no finite deadline exists.
   - At the r-th reached epoch, H_r=r+2 gives exact miss probability 2^{-(r+2)} and total budget at most 1/2.
   - Thus P4-S014 does not collapse to P4-S013.

8. **P4-S011 necessarily violates the condition.**
   - If its exact destroyer had a P4-S014 horizon selector and finite pathwise miss budget, the theorem would transfer its successful output martingale to a computable martingale succeeding on the P4-S011 computably random source.
   - This contradicts the settled P4-S011 source-randomness theorem.
   - No stronger per-epoch positive lower bound is inferred.

## Synchronization checks

- authoritative/STATE.json records P4-S014 as the last completed mathematics session and P4-S015 as next;
- phase2/candidates.json records the P4-S014 CAND-01 result without changing its exact candidate formulation or prior-art disposition;
- authoritative/NEXT_SESSION_PROMPT.md contains a bounded P4-S015 prompt restricted to stake-weighted loss budgets;
- AGENTS.md, README.md, ROADMAP.md, authoritative/START_HERE.md, authoritative/SESSION_LEDGER.md, authoritative/DECISION_LOG.md, docs/FAILURE_AND_LESSON_LEDGER.md and phase4/README.md are synchronized;
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE and DEF-0020 is unchanged.

Owner/external blocker: **NONE**.
