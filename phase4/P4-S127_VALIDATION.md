# P4-S127 — Independent-in-method SAME-AGENT hostile validation

This is a second mathematical derivation, not external peer review, formal verification, hosted CI, or a novelty search. Incoming live main `ddc6afe4e1a9678d949b772fb36a4728a041dea2`; S127 unused at entry. Distinguish inherited S101–S103 and S102 E-ISO source grade from claims proved in S127.

## A: adversarial quantifier test
Proposed: existence of three inverse points implies R2\R3. Countermodel: T3 has exactly three inverse points above every y but maps ALL CR sources to CR. First broken line is confusing ∃G∈F3 and ∃x∈CR with G(x) nonCR (not even shown for T3) with ∃x∈R2 surviving ALL F2. No equality compiler or ML detector; A OPEN.

## B: independent tree and measure replay
At c=2 output τ length m, source words depth m+2 are a disjoint cylinder partition of the full preimage, so 2^{-m}/2^{-(m+2)}=4. Check m=0: exactly four words; m=1: each binary output must have four words at depth 3. Kraft on P3: 1/2+1/4+1/4=1. For each τ the compatible words are two extensions of 0τ (since 0τ has one unused slot), plus 10τ and 11τ, total four; infinite inverse streams exactly 0y,10y,11y. The finite ghost in the 0 sector dies at the next output bit; no fourth actual inverse. For arbitrary triple x_i, if surplus compatible cells outside fixed disjoint clopen cones persisted infinitely often, closedness/finite branching and nested output prefixes would give an additional inverse; contradiction. Not EFFECTIVE in y.

Hostile local rotation check: parent A1,A2,B1,C1 gives eight source-child cells; assigning child-0 A1 one+B1 two+C1 one=4 and child-1 A1 one+A2 two+C1 one=4 validates exactly one row, but child-1 A=3,C=1 risks four full inverses. No all-output extension or total F3 claim. The dream of free asynchronous rotation is NOT proved.

Independently compute E[v(child)|τ] = q(1−q)−δ² from E[q_child²]=q²+δ². Hence v+∑δ² is an exact rational martingale, ≥0. If an observed child changes by >=1/4, its δ²≥1/16 and the capital sum diverges on infinitely many changes. This detects nonCR OUTPUTS, not nonCR SOURCES. No appeal to convergence on bad target. B PROVED restricted, circulation OPEN.

## C: order and counterexamples
For H∘F, first enumerate u∈H^{-1}(y) (≤a), then each F^{-1}(u) (≤b); different u create disjoint sets. T2∘T2 gives four preimages; thus an unqualified F2-composition claim fails. The cross-level implication uses x∈R_ab before image F(x), not the reverse. If F2 fails closure on R2, G∘F is F4 and yields the SAME x∈R2\R4. Absence of factorization theorem is not evidence of nonfactorization. C PROVED exact restrictions.

## D: quantifiers
Formal countermodel to stagewise survivor compactness: Q_k=M∪{z_n:n≥k}. Each Q_k\M nonempty but ⋂Q_k=M. No enumerability/forcing result claimed. D LOGICALLY PROVED boundary only, substantive hierarchy OPEN.

## E: alternate all-source argument
Uniform input x conditioned on p∈P gives an independent fair suffix u. H_p sends fair suffix to fair output; mixing with Kraft weights returns fair λ exactly. For any y, H_p^{-1}(y) is exactly one point (not a finite approximant), so inverse count k exactly. Tagging output by first |p| source bits in L preserves total fairness and fibre cap j; pK(u) nonCR whenever K(u) nonCR. Thus pu∈R_j forces u∈R_j, and H_p transports R_j by composing arbitrary F_j tests. M(s) source account: before code end, a selected leaf receives capital 1 at its exact p; after code end it follows d. At a pre-leaf prefix, sum of weights of descendant leaves is exactly the contribution written, and binary splitting conserves capital. M(root)=1 by Kraft. No illegal convergence of real capital or unsupported computable measure. E PROVED INTERNAL.

## Computational finite sanity (not proofs)
Exact arithmetic Python exhaustive enumeration: k=2,3,4,5,6 and all output lengths m=0..6. For each k, all 2^{m+k−1} source words of aligned use depth counted. Every output prefix appeared exactly 2^{k−1} times; all 635 output-word cases PASS. This checks only finite cylinders for the explicit T_k program, not R_j preservation, infinite fibres, the q martingale, all F3 observers or formal proof.

## Scorecard (status / falsifier)
- A R2/R3: **OPEN**. Falsifier of naive third-inverse destruction = T3 preserves CR. No same-source witness nor equality.
- B three fibres and four cells: **PROVED INTERNALLY** for T3 and occupancy / volatility; **OPEN** persistent global circulation. Falsifier for naïve row gluing = sibling with potential four actual paths.
- C R4 composition: **PROVED INTERNALLY** product, sharpness and F_b(R_ab)⊆R_a; **OPEN** unrestricted iteration/equality. Falsifier = T2∘T2 exactly four.
- D finite threshold: **OPEN**; quantifier confusion **REFUTED** by abstract Q_k model. No survivor or threshold.
- E general-k: **PROVED INTERNALLY** finite-code homeomorphism-sheet theorem, cap sharpness and rational prefix compiler; scope not all F_k. Falsifier to overreach = no representation of arbitrary boundary-fold map.
No fatal inconsistency detected within exact restricted claims. Review remains SAME-AGENT INTERNAL, not independent externally, CI or Lean/Palomar.