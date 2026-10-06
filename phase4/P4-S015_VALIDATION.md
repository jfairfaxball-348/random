# P4-S015 validation

Date: 2026-10-06
Incoming baseline: 7c47680ab22d21e9fd21cb1d276165f0406bc0e8
Pre-validation main checked: 1f342786dd2755730aaf0eefa53f15b20982ff4b

Result: **PASS** for uniqueness, k=2 scope discipline, stake-weighted finite-ticket transfer, strict separation from the P4-S014 raw-tail condition, the future-envelope effectivity obstruction, the necessary P4-S011 violation, authority synchronization and preserved guards.

## Repository and scope checks

- live main matched the P4-S014 outgoing checkpoint exactly before substantive work;
- P4-S015 mathematics, close and validation records were absent on the incoming checkpoint and repository search returned no P4-S015 record, so P4-S015 was unique;
- P4-S001 through P4-S014 and required CAND-01 authority were read;
- P4-S005 through P4-S014 were treated as settled;
- the incoming-to-pre-validation comparison changes only P4-S015 records and current authority/index/summary files;
- no P4-S001 through P4-S014 mathematics/close/validation record appears in the changed-file set;
- phase3/prior-art.json is unchanged and PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- catalog/definitions.json is unchanged and DEF-0020 is preserved;
- the session stays at k=2 and makes no novelty, Gate-4, publication or outreach claim.

## Mathematical checks

1. **Positive skipped-gain loss is the correct local quantity.**
   - For a nonnegative martingale at positive capital, the sentinel child multiplier is 1+theta(2b-1), with theta in [-1,1].
   - If the multiplier is at most one, skipping the already-revealed sentinel wager cannot reduce the completion/source comparison.
   - The only multiplicative damage is therefore ell=max(0,theta(2b-1)), which lies in [0,1].

2. **The savings wrapper is a total computable martingale and does not enlarge stakes.**
   - Its risk account uses the original martingale's fractional stake and transfers one unit to a cash account whenever provisional risk reaches at least two.
   - Reallocation does not change total child capital, so the fair martingale equation is preserved.
   - Total fractional stake is (R/(S+R))theta and therefore no larger in magnitude than the original stake.
   - If the original martingale is unbounded but only finitely many transfers occurred, the post-last-transfer risk account would remain a fixed positive multiple of the original and eventually force another transfer. Hence transfers are infinite and total savings-wrapped capital tends to infinity along all sufficiently late prefixes.

3. **The leaf-dependent ticket price is exact and computable.**
   - At a reachable epoch, A_s intersect 2^{H(s)} is a finite computable set.
   - On the sentinel-first completion, the prequeried sentinel bit and the H fresh filler answers are fair fresh bits.
   - Self-avoidance makes the horizon-miss geometry independent of the sentinel bit.
   - A ticket paying w(s,b,rho) exactly on a miss leaf has fair initial price 2^{-(H+1)} times the sum of its leaf payouts.
   - Unit payouts recover P4-S014's raw price p(s); a uniform epoch cap a(s) gives the coarser price p(s)a(s).

4. **The weighted ticket martingale is total and catches divergent realized loss.**
   - A finite computable pathwise budget on sum c(s) prevents the initial reserve from being overdrawn.
   - Every resolved realized miss adds its leaf payout w to cash.
   - Hence divergent realized miss-weight sum forces unbounded capital without any independence assumption.

5. **The restart-scale calculation is correct.**
   - On good epochs the P4-S014 finite conditional-expectation hedge preserves the current scale exactly.
   - After a miss it copies the savings martingale on fresh fillers.
   - If a later sentinel multiplier is g<=1, skipping it cannot lower the scale.
   - If g>1, the envelope gives g<=1+w, so the scale loses at most a factor 1+w.
   - When the realized weight sum is finite, product(1+w) is finite because log(1+w)<=w, leaving a positive scale lower bound.
   - If the savings martingale is zero at a restart state, the construction freezes there; zero is absorbing and such a branch cannot be an output-success branch. This makes the martingale total on all branches.

6. **The one-martingale dichotomy is complete.**
   - Divergent realized miss weight gives success of the weighted ticket martingale.
   - Finite realized miss weight plus output success gives success of the truncated/restart martingale because the savings-wrapped output martingale tends to infinity at all late restart prefixes.
   - A permanently nontriggering missed epoch is covered because the restart martingale copies the savings martingale forever on fillers.
   - Their sum succeeds whenever the original output martingale succeeds.
   - The settled P4-S014 sentinel-first completion is a P4-S001 effective isomorphism, so one computable source martingale follows.

7. **The strict separation example satisfies the advertised bounds.**
   - The self-avoiding functional queries j+1 and, after a first zero, j+2; it triggers on controls 1 or 01 and diverges after 00.
   - Induction shows these are the first one or two fresh fillers at each new epoch.
   - A 00 branch permanently omits only the sentinel, while triggering branches consume it, giving the settled total/no-repeat/fair-coin/global-k=2 geometry.
   - Permanent avoidance has conditional probability 1/4 at every reached epoch, so every finite horizon has raw miss probability at least 1/4.
   - Infinite all-trigger runs exist, so no P4-S014 finite uniform raw-tail budget can exist for any horizon selector.
   - With horizon one and stake a_j=2^{-(j+1)}, only sentinel bit one on the miss leaf can suffer positive skipped gain a_j, giving exact ticket price a_j/4.
   - Sentinels strictly increase, so the uniform weighted budget is at most (1/4) sum_j 2^{-(j+1)}=1/4.

8. **The exact minimal future-loss envelope is not silently assumed computable.**
   - A uniform c.e. noncomputable trigger family which eventually exposes an all-in sentinel stake exactly when e enters a fixed c.e. noncomputable set has minimal future loss one or zero according to membership.
   - Uniform computation of that exact envelope would decide the noncomputable set.
   - P4-S015 therefore requires a computable envelope or stronger effective data; it does not reopen or solve P4-S010's exact optional-projection problem.

9. **P4-S011 necessarily violates the weighted certificate.**
   - Its target sentinel wagers are all-in and correct, so every target horizon miss followed by the eventual trigger has positive skipped gain exactly one.
   - If infinitely many target horizons miss, the weighted ticket martingale would succeed.
   - If only finitely many miss, the restart martingale would eventually track the savings-wrapped winning martingale at positive scale and succeed.
   - A finite P4-S015 certificate would therefore yield a computable martingale succeeding on the P4-S011 computably random source after the settled completion/isomorphism transfer, contradiction.
   - No stronger per-epoch lower bound than what is justified by the all-in realized losses is asserted.

## Synchronization checks

- authoritative/STATE.json parses and records P4-S015 as the last mathematics session, P4-S016 as next, and the new k=2 weighted-loss result;
- phase2/candidates.json parses and records the P4-S015 CAND-01 result without changing the candidate formulation or prior-art disposition;
- authoritative/NEXT_SESSION_PROMPT.md contains a bounded P4-S016 prompt restricted to incremental postmiss loss tickets;
- AGENTS.md, README.md, ROADMAP.md, authoritative/START_HERE.md, authoritative/SESSION_LEDGER.md, authoritative/DECISION_LOG.md, docs/FAILURE_AND_LESSON_LEDGER.md and phase4/README.md are synchronized with the same result;
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE and DEF-0020 is unchanged.

Owner/external blocker: **NONE**.

This is bookkeeping/manual proof validation, not proof-assistant verification and not a novelty theorem.
