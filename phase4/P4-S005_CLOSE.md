# P4-S005 close

Date: 2026-10-05
Session: P4-S005
Incoming checkpoint: beaa3c41f886176cde1b51d74e6e812b8f30974a
Scope: selected CAND-01; k=2 crossing-measure / stopped-pullback boundary only
Status: **COMPLETED**

## Result

P4-S005 gives a sharp negative answer to the proposed crossing-measure effectivization route.

An explicit everywhere-total computable fair-coin-preserving k=2 map is built from prefix-free output blocks and a finite halting-triggered prefix code. The map has the stronger property that [0] and [1] form a computable clopen partition on which the two restrictions are injective. Nevertheless
[
\lambda(V_{0,1/3})=\frac18\sum_{e\in K}4^{-(e+1)}
]
for a fixed c.e. noncomputable K, so the low-weight crossing measure is noncomputable. Thus the forced two-prefix inverse lists do not make the P4-S004 hitting probabilities uniformly computable, and this crossing set cannot itself be promoted to a Schnorr-test component merely by appealing to k=2.

A second natural branch-free construction also fails uniformly: the finite measure obtained by integrating inverse-point counts can have noncomputable total mass even when the output measure is fair coin. Hence symmetric fibre counting does not automatically yield one computable pullback martingale.

The new map is **not** a randomness-destruction witness. Its computable clopen two-sheet split puts it inside P4-S003's positive preservation theorem. The SRC-0061 filler/pre-revealed-bet obstruction remains unresolved, including the one-hidden/rotating-mask variant. No exact total computable fair-coin-preserving k=2 map with a computably random source and non-computably-random image is established.

General k=2 preservation/failure therefore remains unresolved, but the direct “two-prefix lists -> computable crossing measure -> Schnorr stopping” route is now refuted.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard, P4-S001 through P4-S004 and DEF-0020 are preserved exactly. No conclusion is made for k>2. Gate 4 is NOT REVIEWED. Phase 5 remains CLOSED. No owner/external blocker exists.

Validation: phase4/P4-S005_VALIDATION.md.

Next: P4-S006, still bounded to k=2, on the canonical lexicographic/Borel two-sheet split of the compact collision relation and whether its effective complexity suffices for computable-randomness transfer; if not, pursue a genuinely moving-sheet/one-hole counterexample rather than revisiting crossing-measure computability.
