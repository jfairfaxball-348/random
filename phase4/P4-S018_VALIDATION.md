# P4-S018 validation

Date: 2026-10-06
Incoming baseline: 5b77d2f6b0d824c9f8a0213908e6fbd6efc245a9
Pre-validation main checked: 7505f5525cf095dedcc6223bb0151bc545e088ab

Result: **PASS** for uniqueness, k=2 scope discipline, effective running-maximum modulus sufficiency, strict separation from absolute premium summability, the cross-branch nonuniformity obstruction, explicit P4-S011 exclusion, authority synchronization and preserved guards.

## Repository and scope checks

- live main matched the requested incoming baseline exactly before substantive work;
- repository search returned no committed P4-S018 record on that incoming checkpoint, so P4-S018 was unique;
- P4-S001 through P4-S017 and required CAND-01 authority were read;
- P4-S005 through P4-S017 were treated as settled;
- P4-S011's exact destroyer, P4-S015's weighted theorem, P4-S016's envelope-free last-chance theorem and P4-S017's coercive self-financing theorem are preserved;
- the incoming-to-pre-validation changed-file set contains only P4-S018 records and synchronized programme authority/index/summary files;
- no P4-S001 through P4-S017 mathematics/close/validation record was edited;
- authoritative/STATE.json and phase2/candidates.json parse successfully and record P4-S018 as latest with P4-S019 next;
- phase3/prior-art.json is byte-for-byte unchanged from the incoming checkpoint (blob 6de1aebd5f1b6b22de9e6535a503f3e0fbafb90c), and PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- catalog/definitions.json is byte-for-byte unchanged from the incoming checkpoint (blob d7052d72a82b5635634544c3f4eedd18383332e9), and DEF-0020 remains n-randomness via oracle jumps;
- the session stays strictly at k=2 and makes no novelty, Gate-4, publication or outreach claim.

## Mathematical checks

1. **The running-maximum modulus is sufficient.**
   - For finite ticket history v, E(v) and W*(v) are computable from the finite history.
   - If a total computable h satisfies E(v)>=h(K) => W*(v)>=K for every integer K and every finite v, then E=infinity on a run forces W* to exceed every K.
   - Hence the ticket account succeeds on every divergent-realized-loss run.
   - The settled restart hedge covers finite realized loss, so the P4-S017 sum-of-two-accounts proof goes through unchanged.

2. **Running maximum is the correct weakest local capital statistic.**
   - Martingale success requires an unbounded supremum, not a permanent current-capital floor.
   - Therefore W*(v)>=g(E(v)) is weaker than requiring W(v)>=g(E(v)) and is the natural local quantitative form of the existing proof architecture.

3. **The condition does not restore absolute premium summability.**
   - In the settled P4-S017 one-sided-trigger fixed-H example, winning positive tickets add half their realized loss to capital, while a losing positive-cost ticket terminates future positive premiums.
   - Thus W*(v) is bounded below by an affine function of E(v), giving a computable modulus.
   - Along the all-trigger positive-sentinel branch the exact premium sum remains one half of the harmonic series and diverges.

4. **The cross-branch construction is semantically coercive.**
   - Mode A is exactly the settled P4-S017 one-sided-trigger coercive gadget.
   - Mode B uses only zero-stake control epochs followed by one finite deterministic-trigger burst and then holds forever.
   - Every Mode-B run therefore has finite total E.
   - Any E-divergent run must lie in Mode A, where ticket capital is unbounded.

5. **No uniform threshold exists even noncomputably.**
   - For K=2, choose a Mode-B unary code selecting N deterministic positive tickets.
   - Each such ticket has price equal to its certain payout, so ticket capital remains 1.
   - On the all-positive stored-sentinel finite branch, cumulative realized loss is the N-th harmonic partial sum.
   - These partial sums are unbounded with N, so for every proposed finite threshold T there is a finite history with E>=T but W*=1<2.
   - Therefore semantic coercivity does not imply any uniform loss-to-capital threshold, computable or otherwise.

6. **The scan remains inside the settled k=2 least-fresh class.**
   - The control logic uses only computable finite state and zero-stake consumed sentinels.
   - The productive and deterministic components are the two P4-S017 gadgets already checked for total adaptive no-repeat fair-coin behaviour.
   - A nontriggering continuation can omit at most its current sentinel; the other epochs consume theirs.
   - Hence the concatenated mode-switch construction remains globally k=2.
   - The example is a boundary construction for the ticket-stream condition, not a new randomness-destruction witness.

7. **The bad-capital-tree formulation is exact.**
   - For B_K={v:W*(v)<K}, semantic coercivity says every infinite branch through B_K has bounded E.
   - A uniform threshold at K is equivalent to E being uniformly bounded over all finite nodes of B_K.
   - The construction has branchwise bounded E but unbounded finite-node E in B_2.
   - Thus cross-branch nonuniformity, not limit computability, is the first obstruction.

8. **Loss-properness isolates the remaining layer.**
   - If b(K)=sup{E(v):W*(v)<K}<infinity, then a set-theoretic threshold exists.
   - If computable upper bounds for b(K) are given uniformly in K, a computable coercivity modulus follows.
   - P4-S018 correctly leaves open whether computability of the k=2 ticket tree plus finiteness of b(K) forces computable upper bounds.

9. **P4-S011 violates every effective modulus.**
   - P4-S016 already establishes E=infinity on the sentinel-first completion C(Y) of the settled computably random P4-S011 target for every computable horizon selector.
   - An effective coercivity modulus would force the total ticket martingale to be unbounded on C(Y).
   - C is the settled P4-S001 effective isomorphism, so C(Y) is computably random, contradiction.
   - As in P4-S017, bare no-overdraft admissibility is not ruled out.

## Synchronization checks

- authoritative/STATE.json records P4-S018 as the last mathematics session, P4-S019 as next, and the effective-coercivity/cross-branch result;
- phase2/candidates.json records the P4-S018 CAND-01 result without changing the exact candidate formulation or prior-art disposition;
- authoritative/NEXT_SESSION_PROMPT.md contains a bounded P4-S019 prompt restricted to finite-versus-computably-bounded loss-properness;
- README.md, ROADMAP.md, AGENTS.md, authoritative/START_HERE.md, authoritative/SESSION_LEDGER.md, authoritative/DECISION_LOG.md, docs/FAILURE_AND_LESSON_LEDGER.md and phase4/README.md are synchronized with the same boundary;
- durable decision D-0040 and lesson FL-066 are recorded;
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE and DEF-0020 is unchanged.

Owner/external blocker: **NONE**.

This is manual mathematical/bookkeeping validation, not proof-assistant verification and not a novelty theorem.
