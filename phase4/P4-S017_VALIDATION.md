# P4-S017 validation

Date: 2026-10-06
Incoming baseline: 4f587d38ff58c3eb6314c4f1d22bfd57594c77ea
Pre-validation main checked: 6376bf5531f2a3f8f5d70dbc683074d08fcaba1e

Result: **PASS** for uniqueness, k=2 scope discipline, coercive self-financing reserve transfer, fixed-horizon separation from absolute premium summability, the bare-solvency obstruction, explicit P4-S011 exclusion, authority synchronization and preserved guards.

## Repository and scope checks

- live main matched the requested incoming baseline exactly before substantive work;
- repository search returned no committed P4-S017 record on that incoming checkpoint, so P4-S017 was unique;
- P4-S001 through P4-S016 and required CAND-01 authority were read;
- P4-S005 through P4-S016 were treated as settled;
- P4-S011's exact destroyer, P4-S015's weighted theorem and P4-S016's envelope-free last-chance theorem are preserved;
- the incoming-to-pre-validation changed-file set contains only P4-S017 records and synchronized programme authority/index/summary files;
- no P4-S001 through P4-S016 mathematics/close/validation record was edited;
- authoritative/STATE.json and phase2/candidates.json parse successfully and record P4-S017 as latest with P4-S018 next;
- phase3/prior-art.json is byte-for-byte unchanged from the incoming checkpoint and PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- catalog/definitions.json is byte-for-byte unchanged from the incoming checkpoint and DEF-0020 is preserved;
- the session stays strictly at k=2 and makes no novelty, Gate-4, publication or outreach claim.

## Mathematical checks

1. **The self-financing account is exactly fair.**
   - At visited last-chance node i, the full ticket costs pi_i=(L_i(0)+L_i(1))/2 and pays L_i(a) after one fresh fair filler bit.
   - Therefore replacing pi_i units of cash by the full ticket preserves the martingale equation.
   - The account capital after resolved tickets is initial reserve plus cumulative payouts minus cumulative premiums.

2. **Admissibility is the exact no-borrowing condition.**
   - Before ticket i, affordability is equivalent to current cash being at least pi_i.
   - The recorded inequality R+sum_{j<i}e_j-sum_{j<=i}pi_j>=0 is exactly that condition after paying the current premium.
   - If it holds on every run at every ticket node, the canonical ticket process is total and nonnegative.

3. **Coercivity closes the P4-S016 dichotomy.**
   - The settled restart hedge succeeds on every d-success path with finite cumulative realized positive skipped gain.
   - If that realized loss diverges, coercivity requires the self-financing ticket martingale itself to be unbounded.
   - A permanently nontriggering missed epoch remains covered by the settled restart hedge copying q forever.
   - Hence the sum of the two accounts succeeds whenever d succeeds.

4. **The source transfer uses only settled effective isomorphism.**
   - The sentinel-first completion is unchanged from P4-S014 through P4-S016 and remains an everywhere-total computable fair-coin adaptive permutation with computable inverse.
   - P4-S001 therefore transfers the completion martingale to one computable source martingale.
   - No infinite optional projection, future supremum or advance loss envelope is computed.

5. **P4-S016 implies the new reserve condition.**
   - Under an absolute premium budget B, starting the ticket account with R=B prevents overdraft.
   - Its capital after n resolved tickets is B+E_n-P_n with P_n<=B, hence is at least E_n.
   - Divergent realized payout therefore forces unbounded capital, so every P4-S016 certificate is a P4-S017 coercive reserve certificate for the same H.

6. **The fixed-H separation arithmetic is correct.**
   - In the two-filler trigger-on-second-1 example with H=1, after r prior correct sentinel wins the savings wrapper has total r+1 and positive sentinel gain ell_r=1/(r+1).
   - On a stored positive sentinel, the two second-filler child losses are 0 and ell_r, so the exact premium is ell_r/2.
   - A winning ticket nets ell_r/2 and reaches another epoch; a losing ticket loses ell_r/2 but enters permanent nontriggering, after which all further premiums are zero.
   - R=1/2 therefore suffices globally, and whenever payouts diverge account capital grows as 1/2+E/2.
   - Along the all-trigger positive-sentinel run the premium sum is one half of the harmonic series and diverges.
   - The record correctly limits this strictness claim to the fixed H/ticket stream and does not claim failure of every re-optimized P4-S016 horizon.

7. **Bare admissibility really is insufficient for this architecture.**
   - In the always-trigger-after-second-filler variant with H=1 and a stored positive sentinel, both children have the same loss ell_r, so the fair premium and certain payout are both ell_r.
   - A reserve of one can therefore remain exactly constant while cumulative realized loss diverges harmonically.
   - The restart hedge skips each positive sentinel multiplier 1+ell_r; the reciprocal scale losses telescope against q's linear savings growth, so its absolute epoch-boundary capital can remain bounded.
   - Thus no-overdraft alone does not establish success of the standard ticket-plus-restart sum.
   - No stronger impossibility for arbitrary transfer martingales is inferred.

8. **The stronger reserve-floor condition is only sufficient.**
   - If a computable nondecreasing unbounded g satisfies W_n>=g(E_n), divergent E_n forces the ticket account unbounded.
   - P4-S017 does not assert that every semantically coercive reserve admits such a computable uniform modulus.
   - That effectivity question is correctly deferred to P4-S018.

9. **P4-S011 violates every coercive certificate.**
   - P4-S016 already proves that for every computable horizon selector the cumulative realized positive skipped gain diverges on the settled computably random target Y.
   - A P4-S017 coercive admissible account would therefore be a total computable martingale succeeding on the sentinel-first completion C(Y).
   - C is a P4-S001 effective isomorphism, so C(Y) is computably random, contradiction.
   - The record correctly does not claim that bare no-overdraft admissibility itself is impossible for P4-S011.

## Synchronization checks

- authoritative/STATE.json records P4-S017 as the last mathematics session, P4-S018 as next, and the self-financing reserve result;
- phase2/candidates.json records the P4-S017 CAND-01 result without changing the exact candidate formulation or prior-art disposition;
- authoritative/NEXT_SESSION_PROMPT.md contains a bounded P4-S018 prompt restricted to the effectivity of coercivity;
- README.md, ROADMAP.md, AGENTS.md, authoritative/START_HERE.md, authoritative/SESSION_LEDGER.md, authoritative/DECISION_LOG.md, docs/FAILURE_AND_LESSON_LEDGER.md and phase4/README.md are synchronized with the same boundary;
- durable decision D-0039 and lesson FL-065 are recorded;
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE and DEF-0020 is unchanged.

Owner/external blocker: **NONE**.

This is manual mathematical/bookkeeping validation, not proof-assistant verification and not a novelty theorem.
