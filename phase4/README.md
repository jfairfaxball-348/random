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

Historical next step after P4-S002: **P4-S003**, now completed below.

## P4-S003 — k=2 weighted-sheet and martingale-transfer boundary

P4-S003 strengthens the forced inverse information to a uniform two-prefix list at every requested input precision. It proves that an explicit computable clopen two-sheet decomposition into injective restrictions is sufficient for forward computable-randomness preservation, using conditional component measures, SRC-0015 / THM-0038 and DEF-0036.

The bare k=2 hypothesis does not force that global sheet structure: an explicit marker-and-delete map is fair-coin preserving, exactly two-to-one off one singleton, and has no continuous/clopen two-colouring separating all double fibres. It still preserves computable randomness and has an a.e. sheet description.

The general k=2 preservation/failure question remains unresolved. The remaining weighted obstruction is encoded by the computable bounded martingales w_sigma(tau)=2^{|tau|}lambda([sigma]∩F^{-1}([tau])). The attempted SRC-0061 scan completion fails because filler queries may pre-reveal later betting positions.

Records:
- phase4/P4-S003_MATHEMATICS.md
- phase4/P4-S003_CLOSE.md
- phase4/P4-S003_VALIDATION.md

Next recommended session: **P4-S004**, still bounded to k=2, on the conditional-weight stabilization/transfer obstruction versus an exact k=2 non-conservation witness.

## P4-S004 — k=2 conditional-weight stopping boundary

P4-S004 identifies the exact effectivity gap behind P4-S003's conditional weights. For each source cylinder [sigma], the points whose conditional weight ever falls below epsilon form a uniformly effectively open source set of measure at most epsilon. Hence Martin-Löf-random sources have positive persistent weight, but this is only an ML-test estimate; the computably-random source case still needs computable hitting measures, a computable stopped pullback, or another computable-randomness-level argument.

For every fixed output stage m, the output martingale capital lifts exactly to a uniformly computable normalized source martingale. The unresolved issue is coherence across unbounded m. Static mixtures need a growth rate, and adaptive threshold selection returns to the same effective stopping problem.

An explicit asymmetric collision map F_thin is total computable, fair-coin preserving and globally k=2, with one actual double-fibre sheet satisfying w_0(0^m)=2^{-m}->0. Its thin point is computable and the map is a.e.-invertible off the collision output, so it is not a randomness-destruction witness.

General k=2 preservation/failure remains unresolved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. No k>2, novelty/open-status, Gate-4 or publication claim is made.

Records:
- phase4/P4-S004_MATHEMATICS.md
- phase4/P4-S004_CLOSE.md
- phase4/P4-S004_VALIDATION.md

Historical next step after P4-S004: **P4-S005**, now completed below.

## P4-S005 — k=2 crossing-measure non-effectivity boundary

P4-S005 refutes the direct stopping-effectivization route isolated in P4-S004. An exact total computable fair-coin-preserving k=2 prefix-code map has a computable clopen partition [0],[1] into injective sheets, yet for a fixed c.e. noncomputable set K its low-weight crossing set satisfies
[
\lambda(V_{0,1/3})=\frac18\sum_{e\in K}4^{-(e+1)},
]
which is noncomputable. Thus the forced two-prefix inverse lists do not force computable low-weight hitting probabilities, even under strictly stronger effective sheet information.

A second natural branch-free route also fails uniformly: integrating inverse-point counts against fair coin gives a finite measure whose total mass can encode the same noncomputable set. Hence symmetric fibre counting does not automatically yield one computable pullback martingale.

The new map is not a randomness-destruction witness because its computable clopen injective-sheet split places it inside P4-S003's positive preservation theorem. The SRC-0061 pre-revealed-bet obstruction remains unresolved. General k=2 preservation/failure remains unresolved.

Records:
- phase4/P4-S005_MATHEMATICS.md
- phase4/P4-S005_CLOSE.md
- phase4/P4-S005_VALIDATION.md

Historical next step after P4-S005: **P4-S006**, now completed below.



## P4-S006 — canonical lexicographic two-sheet complexity

P4-S006 computes the canonical sheet complexity without revisiting P4-S005's settled crossing-measure result. The collision relation is effectively closed. Assigning the lexicographically least preimage to the lower sheet and the nonminimum point of a double fibre to the upper sheet gives an effective G-delta lower sheet and effective F-sigma upper sheet; the double-fibre output set is effective F-sigma. The lexicographic minimum and maximum inverse selectors are effective Baire-1 limits of computable continuous selectors from the descending clopen fibre approximants.

This effective Borel information is not enough to run the existing computable-randomness transfer. In the P4-S005 map, viewed only as an internal calibration example, the canonical upper and lower sheet masses encode the same noncomputable base-4 real, so the canonical component measures need not be computable. The selector approximations also have no forced computable stabilization modulus.

A single hidden/rotating filler bit does not repair SRC-0061: revealing one previously masked genuine betting coordinate identifies the common one-bit ambiguity and pre-reveals every other coordinate in that cohort. More complicated delayed-coalescence constructions are not ruled out.

General k=2 preservation/failure remains unresolved. No exact k=2 destroyer is obtained.

Records:
- phase4/P4-S006_MATHEMATICS.md
- phase4/P4-S006_CLOSE.md
- phase4/P4-S006_VALIDATION.md

Next recommended session: **P4-S007**, still bounded to k=2, on delayed-coalescence inverse trees: allow many finite-prefix candidates while requiring at most two final fibre points, and test whether this structure yields one computable martingale transfer or an exact moving-sheet counterexample without the one-hole pre-revelation collapse.
