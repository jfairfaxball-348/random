# P4-S001 close

Date: 2026-10-05
Session: P4-S001
Incoming checkpoint: d451cf0c65b9a508b8215ade9916c09fa239f7ad
Scope: selected CAND-01; k=1 injective base case only
Status: **COMPLETED**

## Result

P4-S001 proves that every everywhere-total computable fair-coin-preserving Cantor self-map with one-point fibres is a computable fair-coin-preserving homeomorphism with an everywhere-total computable inverse. SRC-0015 / THM-0038 then yields computable-randomness invariance, so every computably random x remains computably random under every F in F_1.

A class-wide fixed inverse-use bound is not forced: coordinate permutations can move the first input bit arbitrarily far out.

The inverse/homeomorphism lemmas are new programme mathematics; the randomness-transfer step depends on the existing statement-inspected THM-0038. No literature novelty claim is made.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The Gate-3 guard is preserved historically: before Phase 4 no computable-randomness consequence of bare finite fibres had been established. P4-S001 establishes only k=1; k>=2 and general finite multiplicity remain unresolved here.

Phase 4 remains OPEN. Gate 4 is NOT REVIEWED. Phase 5 remains CLOSED. Fairfax-Ball Randomness is not defined. No owner/external blocker exists.

Validation: phase4/P4-S001_VALIDATION.md.

Next: P4-S002, bounded k=2 effective-fibre / inverse-branch analysis.
