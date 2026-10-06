# P4-S016 validation

Date: 2026-10-06
Incoming baseline: 66b77cf8fcb5c6c5feafeb54cd9ce003e2d9342c

Result: **PASS** for uniqueness, k=2 scope discipline, envelope-free one-step pricing, incremental premium transfer, explicit P4-S011 obstruction, authority synchronization and preserved guards.

## Repository and scope checks

- live main matched the requested incoming checkpoint exactly before substantive work;
- P4-S016 mathematics/close/validation records were absent on the incoming checkpoint and repository search returned no committed P4-S016 record;
- P4-S001 through P4-S015 and required CAND-01 authority were read;
- P4-S005 through P4-S015 were treated as settled;
- P4-S011's exact destroyer and P4-S015's weighted theorem are preserved;
- phase3/prior-art.json remains unchanged and PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- catalog/definitions.json remains unchanged and DEF-0020 is preserved;
- the session stays strictly at k=2 and makes no novelty, Gate-4, publication or outreach claim.

## Mathematical checks

1. **The postmiss state still contains fresh randomness.**
   - A horizon miss is counted only when, after the finite-horizon hedge, the epoch remains unresolved and its next logical query is a fresh filler.
   - The sentinel was physically queried earlier by the settled sentinel-first completion, but the next filler bit is still fresh fair coin.
   - Therefore a one-step ticket can still be bought fairly before the bit which may make the trigger visible is drawn.

2. **Immediate child losses are computable.**
   - From a finite unresolved state, the total least-fresh next-query function can be simulated under each hypothetical next filler answer.
   - If that child makes the sentinel the next logical query, the finite pre-sentinel transcript is known and the savings martingale q gives the exact rational positive gain ell.
   - Otherwise the immediate skipped-loss payoff is zero.
   - No infinite-horizon trigger decision or future supremum is used.

3. **The price pi is exactly fair and locally minimal.**
   - The ticket child payoffs are L_v(0),L_v(1), so fairness forces price pi(v)=(L_v(0)+L_v(1))/2.
   - Any nonnegative one-step hedge covering both child losses has child payoffs at least these values, hence current capital at least pi(v).
   - This proves sharpness only for the one-step ticket architecture, not for arbitrary global transfer constructions.

4. **The premium-budget insurance account is total.**
   - The supplied finite computable bound B dominates the sum of all pi(v) visited after horizon misses on every run.
   - Spending pi(v) from reserve at each such node therefore never overdraws.
   - Each purchased ticket is a one-step fair martingale, so reserve plus resolved cash plus outstanding ticket is a total nonnegative computable martingale.

5. **Divergent realized loss is caught exactly.**
   - A ticket pays nonzero precisely when its actual next filler makes the sentinel trigger, and then it pays the exact positive skipped gain ell.
   - Therefore the insurance account has accumulated payout equal to the realized positive skipped-gain sum, up to the bounded premium expenditure.
   - Divergent realized skipped gain forces unbounded insurance capital.

6. **Finite realized loss preserves restart scale.**
   - On good finite-horizon epochs the settled conditional-expectation hedge tracks q exactly.
   - On a missed-then-triggered epoch with positive multiplier 1+ell, skipping the already-revealed sentinel reduces scale by exactly 1/(1+ell); losing or flat sentinel wagers do not reduce scale.
   - Finite sum ell implies product (1+ell) is finite because log(1+ell)<=ell, hence the scale has a positive lower bound.
   - The P4-S015 savings wrapper tends to infinity at all sufficiently late prefixes on any d-success path, so the restart hedge succeeds.
   - A permanently nontriggering missed epoch is handled by copying q forever.

7. **The one-martingale dichotomy is complete.**
   - Infinite realized loss gives success of the insurance martingale.
   - Finite realized loss plus output success gives success of the restart martingale.
   - Their sum is one computable completion martingale succeeding whenever d succeeds.
   - The sentinel-first completion is the settled computable fair-coin effective isomorphism, so P4-S001 gives one computable source martingale.

8. **The advance P4-S015 envelope is genuinely absent.**
   - No value majorizing all later losses is computed or supplied at the horizon.
   - The P4-S015 noncomputability of the pointwise minimal future envelope is therefore not an obstruction to this theorem.
   - The new hypothesis is instead the finite uniform pathwise sum budget on automatically computed conditional one-step premiums.

9. **The relation to P4-S015 is not overstated.**
   - P4-S015 charges ex-ante fair price at the horizon and can exploit a small horizon-miss probability.
   - P4-S016 charges conditional premiums only after the miss along the realized continuation.
   - The session claims removal of the envelope as effective data, not a global numerical implication between all P4-S015 and P4-S016 certificates.

10. **P4-S011 violates the new condition on its target path.**
    - Fix any computable horizon selector on the settled P4-S011 witness Y and use q=Save(d).
    - If the realized positive skipped-gain sum on Y were finite, the restart hedge alone would succeed on the effective-isomorphism completion and therefore yield a computable source martingale succeeding on Y, contradiction.
    - Hence that realized loss sum diverges.
    - Immediately before each missed epoch finally triggers, the actual next-child loss equals ell, so the one-step fair price is at least ell/2.
    - The cumulative premium sum therefore diverges on Y itself.
    - Thus no finite P4-S016 pathwise premium budget exists for P4-S011 for any computable horizon selector.

## Synchronization checks

- authoritative/STATE.json records P4-S016 as the latest mathematics session and P4-S017 as next;
- phase2/candidates.json records the P4-S016 CAND-01 result without changing the candidate formulation or prior-art disposition;
- authoritative/NEXT_SESSION_PROMPT.md contains a bounded P4-S017 prompt restricted to self-financing premium reserves;
- AGENTS.md, README.md, ROADMAP.md, authoritative/START_HERE.md, authoritative/SESSION_LEDGER.md, authoritative/DECISION_LOG.md, docs/FAILURE_AND_LESSON_LEDGER.md and phase4/README.md are synchronized;
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE and DEF-0020 is unchanged.

Owner/external blocker: **NONE**.

This is manual mathematical/bookkeeping validation, not proof-assistant verification and not a novelty theorem.
