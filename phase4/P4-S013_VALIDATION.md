# P4-S013 validation

Date: 2026-10-06
Incoming baseline: 8a5409b662cf548d711485f45d7c35a090f9b917
Pre-validation main checked: a05e052f2ee7dde24b9625edb8569eee8575286b

Result: **PASS** for uniqueness, k=2 scope discipline, reachable-sentinel totality/deadline equivalence, effective-isomorphism reduction, source-randomness preservation, authority synchronization and preserved scope guards.

## Repository and scope checks

- live main matched the requested incoming baseline exactly before substantive work;
- P4-S013 mathematics, close and validation records were absent on the incoming checkpoint, so P4-S013 was unique;
- P4-S001 through P4-S012 were read and not edited;
- P4-S005 through P4-S012 were treated as settled;
- P4-S011's exact k=2 destroyer and P4-S012's stake-level boundary are preserved;
- the incoming-baseline comparison before this validation changes only P4-S013 records and current programme authority/index/summary files;
- no P4-S001 through P4-S012 record appears in the changed-file set;
- phase3/prior-art.json is unchanged and PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- catalog/definitions.json is unchanged, so DEF-0020 is preserved;
- the session stays at k=2 and makes no novelty, Gate-4, publication or outreach claim.

## Mathematical checks

1. **Operational avoidance tree is computable.**
   - For a reachable epoch state s with sentinel j, membership of a finite answer string rho in the avoidance tree is defined by simulating the already-total computable least-fresh next-query procedure for exactly |rho| output steps.
   - Membership therefore requires only finite computation and does not assume decidability of arbitrary oracle-machine halting.

2. **Sibling totality gives a finite searched deadline.**
   - An infinite path through the avoidance tree is exactly a compatible continuation on which the current sentinel is never consumed.
   - Reachable-sentinel totality excludes such a path.
   - The tree is binary and finitely branching, so König compactness makes it finite.
   - Searching for the first empty level therefore computes a finite uniform filler deadline from the reachable state. No separate deadline modulus is assumed.

3. **Full oracle-totality is sufficient but stronger than necessary.**
   - Full totality on every oracle and input implies reachable-sentinel totality.
   - The mathematics record gives a self-avoiding functional which diverges on input 1, while coordinate 1 is always consumed as the first epoch's filler and never becomes a sentinel; every reachable sentinel still halts.
   - Thus the weaker condition is genuine.

4. **Reachable-sentinel totality forces global exhaustiveness.**
   - Every reachable epoch ends after finitely many fillers and consumes its least-unqueried sentinel.
   - Any coordinate passed over by later sentinels has already been queried as a filler.
   - Hence every coordinate is eventually queried exactly once on every source.

5. **Effective-isomorphism reduction is valid.**
   - Exhaustiveness and no-repeat make every fibre singleton.
   - The inverse computes a requested source bit by simulating the scan on the output transcript until that coordinate is queried.
   - Fresh source queries give fair-coin preservation.
   - Therefore the induced map lies in the P4-S001 k=1 effective-isomorphism regime, and the already-recorded SRC-0015 / THM-0038 consequence gives computable-randomness invariance.

6. **One-martingale transfer is not overstated.**
   - The searched deadline at each epoch permits the exact finite conditional-expectation hedge from P4-S009.
   - These finite block hedges concatenate into one computable martingale on an exhaustive adaptive-permutation completion stream, agreeing with the output martingale at completed epochs.
   - P4-S001 effective-isomorphism invariance, equivalently DEF-0004 applied after the computable isomorphism, then yields a computable source martingale whenever the output martingale succeeds.
   - No new unbounded optional-projection computation is claimed.

7. **Sharpness guard.**
   - Target-only totality is insufficient by the settled P4-S011 destroyer.
   - P4-S013 does not claim that every branchwise-avoidable least-fresh scan destroys computable randomness, nor that reachable-sentinel totality is necessary for every preserving k=2 scan.
   - No all-correct bit-autoreduction converse is claimed.

## Synchronization checks

- authoritative/STATE.json records P4-S013 as the last completed mathematics session and P4-S014 as the recommended next session;
- phase2/candidates.json records the P4-S013 sibling-totality result for CAND-01 without changing its exact candidate formulation or prior-art disposition;
- authoritative/NEXT_SESSION_PROMPT.md contains a bounded runnable P4-S014 prompt restricted to computable summable avoidance-tail control;
- AGENTS.md, README.md, ROADMAP.md, authoritative/START_HERE.md, authoritative/SESSION_LEDGER.md, authoritative/DECISION_LOG.md, docs/FAILURE_AND_LESSON_LEDGER.md and phase4/README.md are synchronized with the same result;
- all synchronized JSON files parsed successfully during the session;
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE and DEF-0020 is unchanged.

Owner/external blocker: **NONE**.
