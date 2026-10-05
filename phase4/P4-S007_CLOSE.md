# P4-S007 close

Date: 2026-10-05
Session: P4-S007
Incoming checkpoint: b25136e24991cb988dc1186567a5639a3c41b38c
Scope: selected CAND-01; k=2 delayed-coalescence inverse-tree boundary only
Status: **COMPLETED**

## Result

P4-S007 shows that the raw many-candidate delayed-coalescence picture can be normalized much further than was explicit in P4-S006.

Using the P4-S003 finite search at each input precision and taking a monotone diagonal, one obtains a computable function c(n) such that the compatible n-prefixes after y↾c(n) form a coherent tree of width at most two, whose infinite paths are exactly F^{-1}(y).

For a double fibre, once the two true preimages first differ, every later skeleton level consists exactly of their two prefixes. For a singleton fibre there is one true prefix and at most one phantom; if phantoms recur, their first disagreement with the true point must drift arbitrarily far right. At each fixed precision the raw approximation has a computable finite mind-change bound and at most one post-c(n) injury, but no computable last-injury time is forced.

This yields a real bounded-information statement—one choice bit per precision—and a uniform partial inverse on singleton fibres. It does not supply the conditional masses, persistence decisions or stopping data required by the existing computable-randomness transfer arguments. P4-S004/P4-S005 remain controlling on those points.

The session also generalizes P4-S006's one-hole collapse. After c(n), any unresolved first-n source information is encoded by one binary choice between two prefixes. Revealing one later betting coordinate on which those prefixes differ selects the entire n-prefix and pre-reveals every other differing coordinate below n. Therefore any SRC-0061-style k=2 completion must satisfy a new global freshness condition relative to c(n). The committed SRC-0061 mechanism provides no such condition, so it is not reused.

No exact k=2 randomness-destruction witness is established. General k=2 forward computable-randomness preservation/failure remains unresolved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard, P4-S001 through P4-S006 and DEF-0020 are preserved exactly. No conclusion is made for k>2. Gate 4 is NOT REVIEWED. Phase 5 remains CLOSED. No owner/external blocker exists.

Validation: phase4/P4-S007_VALIDATION.md.

Next: P4-S008, still bounded to k=2, on the freshness obstruction forced by the coherent width-two skeleton: determine whether a total adaptive scan completable to global k=2 can retain enough genuinely fresh nonmonotonic bets to defeat a computably random source, or whether the freshness constraint yields a computable martingale/permutation-style preservation theorem.
