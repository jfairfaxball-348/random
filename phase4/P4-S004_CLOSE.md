# P4-S004 close

Date: 2026-10-05
Session: P4-S004
Incoming checkpoint: 08b2d04dba6adb57435857369cd2b5317c508940
Scope: selected CAND-01; k=2 conditional-weight / stopping boundary only
Status: **COMPLETED**

## Result

P4-S004 sharpens P4-S003's conditional-weight obstruction without resolving the general k=2 preservation/failure question.

For each source cylinder [sigma], the reciprocal conditional weight is the likelihood-ratio martingale between fair coin and the pushforward of fair coin conditioned on [sigma]. Hence the source points in [sigma] whose conditional weight ever drops below epsilon form a uniformly effectively open set of fair-coin measure at most epsilon. This proves positive persistent weight for Martin-Löf-random sources, but only at Martin-Löf-test strength. Since CAND-01 assumes merely computable randomness, the missing effectivity is now exact: one would need computable hitting measures, a computable stopped pullback, or another computable-randomness-level mechanism.

Every fixed output stage of a computable martingale has a uniformly computable normalized source martingale whose capital eventually equals that output capital along the source point. What is missing is one coherent source martingale across unbounded output stages; static mixtures require a growth rate and adaptive stopping again requires effective hitting probabilities.

An explicit asymmetric collision map F_thin verifies that bare k=2 does not force positive persistent sheet weight: it is everywhere total computable, fair-coin preserving, has exactly one double fibre, and one actual sheet has w_0(0^m)=2^{-m}->0. The thin source point is computable, and the map has an a.e.-computable inverse off the collision output, so this is not a randomness-destruction witness.

The SRC-0061 filler route remains blocked. A masked/XOR filler postpones disclosure but can reveal its partner when one endpoint is later queried; no globally k=2 winning construction was completed. No exact k=2 computable-randomness-destroying witness is claimed.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard, P4-S001 through P4-S003 and DEF-0020 are preserved exactly. No conclusion is made for k>2. Gate 4 is NOT REVIEWED. Phase 5 remains CLOSED. No owner/external blocker exists.

Validation: phase4/P4-S004_VALIDATION.md.

Next: P4-S005, still bounded to k=2, on whether the low-weight crossing sets forced by P4-S004 become Schnorr/computable-randomness null under the two-prefix inverse-list structure, or whether a computably random source can be realized on a genuinely thin sheet whose image is not computably random.
