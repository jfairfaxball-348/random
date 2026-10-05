# Phase 4 — Mathematics records

Status: **OPEN** after formal Gate-3 PASS in P3-S008.

Selected candidate: **CAND-01 — Computable randomness under finite-ambiguity observations**.

The exact formulation remains unchanged: for every fixed k>=1, consider everywhere-total computable fair-coin-preserving Cantor self-maps with at most k preimages of each point, with no effective inverse branches assumed.

## Completed mathematics

### P4-S001 — k=1 injective base case

P4-S001 proves that k=1 forces a computable fair-coin-preserving homeomorphism with an everywhere-total computable inverse. SRC-0015 / THM-0038 then yields computable-randomness invariance.

The inverse has a computable use modulus for each particular map, but there is no single fixed inverse-use bound across the whole class; coordinate permutations witness arbitrarily delayed inverse use.

This is programme mathematics, not a novelty result. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The Gate-3 no-consequence guard is preserved as the pre-Phase-4 baseline. P4-S001 establishes only k=1; k>=2 and general finite multiplicity remain unresolved here.

Publication remains CLOSED. Fairfax-Ball Randomness is not defined.

Records:
- phase4/P4-S001_MATHEMATICS.md
- phase4/P4-S001_CLOSE.md
- phase4/P4-S001_VALIDATION.md

Historical next step after P4-S001: **P4-S002**, now completed below.

## P4-S002 — k=2 finite-valued inverse boundary

P4-S002 proves that every k=2 map has a uniform descending computable-clopen presentation of each fibre, but the cardinal bound does not force an everywhere-total computable selector or a total two-branch fibre enumeration. An explicit total computable fair-coin-preserving map with exactly one double fibre makes every global selector/listing discontinuous at the collision output.

That obstruction does not itself destroy computable randomness: the example has an a.e.-computable measure-preserving inverse, so SRC-0015 / THM-0038 applies. The exactly two-to-one left shift gives a complementary positive example, preserving computable randomness by a direct martingale lift despite having no single a.e. inverse identity.

The general k=2 preservation/failure question therefore remains unresolved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No result is asserted for k>2, Gate 4 is not reviewed, and Phase 5 remains CLOSED.

Records:
- phase4/P4-S002_MATHEMATICS.md
- phase4/P4-S002_CLOSE.md
- phase4/P4-S002_VALIDATION.md

Next recommended session: **P4-S003**, still bounded to k=2, on a.e./weighted inverse decomposition or direct martingale transfer versus genuine k=2 non-conservation.
