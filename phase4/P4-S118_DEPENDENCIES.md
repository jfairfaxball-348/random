# P4-S118 — Claim dependencies and failure boundaries

| Claim | Assumptions | Disposition |
|---|---|---|
| Hostile posterior q and M check | S116 finite grid + elementary quadratic expansion | RETAINED S117, OUTPUT only |
| Eventual-one-cell source compiler | additive use, eventual unique B candidate, p=d+1 | RETAINED S117, excludes neither two-cell ghosts nor one-CR DP2 |
| A118-1 onto-twin rigidity | P0/P1 total computable ONTO, combined global cap2; fairness only for CR corollary | INTERNAL proof; true with no conditional component fairness |
| A118-2 overlap interior | fair F2, split by source first bit, output in int(I0 intersect I1); S117 priced certificate | INTERNAL special-case proof, recovers S106 clopen safety |
| A118-3 finite-fibre relative computability | effectively compact preimages of output prefixes, FINITE ACTUAL fibre | INTERNAL nonuniform y-oracle proof; not a uniform selector |
| B118-1 paired ghost reset | additive use2, eventual two candidates in each cone, ONE actual inverse per cone, stabilized 1/2 | INTERNAL finite branching + compactness; folds not necessarily simultaneous |
| B118-2 CR image Schnorr | total computable fair G, standard CR=>Schnorr and pullback of Schnorr tests | STANDARD fact rederived; no CR conservation |
| Clopen beta construction | overlap interior gives effectively clopen injective B and computable beta=lambda|B | CONDITIONAL scoped construction, not general boundary beta |
| Existing Y/M/H/X, A-C, E-ISO, source grades | S101-S103 and S106-S117 frozen evidence | RETAINED, no source access upgrade |

F118-1: two individually onto L1 maps cannot be glued under global cap2 without becoming bijections, independent of their fairness.
F118-2: on a stable two-candidate cone the only transitions are perm/permutive or fold/opposite-constant; the latter resets a ghost. Both sides need infinitely many folds, but these can occur at different output depths.
F118-3: a fold destroys the p-output-ratio martingale law if one bets as if its row were permutive. Freezing restores fairness of source capital but may miss arbitrarily many output gains.
F118-4: computable stopping-time prices at finite stages are not uniformly computable measures of infinite output hitting sets. The Schnorr pullback is insufficient for CR output transfer.
F118-5: finite-fibre x<=T y is NONUNIFORM and computes neither canonical inverse measures nor a source-capital compiler.
F118-6: local overlap interior has computable dominated beta; boundary can have noncomputable mass/positive measure and admits no automatic beta extracted from finite q.
F118-7: EQ needs EVERY CR nonMLR input, SEP needs ONE source against ALL F2; no such proofs. S083 wrong-source and general cap4 composition shortcuts remain invalid.

No central theorem achieved; all conditional and inherited literature-access grades unchanged. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.
