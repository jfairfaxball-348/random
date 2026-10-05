# P4-S002 close

Date: 2026-10-05
Session: P4-S002
Incoming checkpoint: 834d945b0f3796906f0d9e93cd3e1369e252d866
Scope: selected CAND-01; k=2 structural inverse-information boundary only
Status: **COMPLETED**

## Result

P4-S002 proves that the exact k=2 hypotheses force a uniform descending sequence of computable clopen fibre approximants A_m(y)=F^{-1}([y↾m]), with intersection equal to the one- or two-point fibre. A chosen fibre point becomes computable from y once an isolating input prefix is supplied.

They do **not** force an everywhere-total computable selector or an everywhere-total computable two-branch fibre enumeration. The explicit map F_* in the mathematics record is total computable, fair-coin preserving, has exactly one double fibre, and makes every global selector/listing discontinuous at that branch-collision output.

This negative inverse-information result is not a randomness-destruction theorem. F_* has an a.e.-computable measure-preserving inverse, so SRC-0015 / THM-0038 gives computable-randomness invariance for F_*. The exact two-to-one shift supplies a complementary k=2 positive example: it has computable branches and preserves computable randomness by a direct martingale lift, even though no single selector is an a.e. inverse identity.

Accordingly, the general k=2 forward computable-randomness question remains unresolved in P4-S002. The precise remaining issue is whether the forced finite-fibre approximation can always be upgraded to weaker a.e./weighted inverse data or a direct martingale transfer, or whether a genuine k=2 non-conservation example exists.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard and exact P4-S001 k=1 result are preserved. DEF-0020 and catalogue records are unchanged. No conclusion is made for k>2.

Phase 4 remains OPEN. Gate 4 is NOT REVIEWED. Phase 5 remains CLOSED. Fairfax-Ball Randomness is not defined. No owner/external blocker exists.

Validation: phase4/P4-S002_VALIDATION.md.

Next: P4-S003, still bounded to k=2, testing whether an a.e.-effective/weighted two-sheet decomposition or direct martingale-transfer theorem is forced, with a k=2 non-conservation construction as the alternative.
