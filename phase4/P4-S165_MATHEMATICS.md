# P4-S165 — Adaptive exact-two boundary above a Schnorr-random destructive output

15 October 2026. INTERNAL same-agent mathematics, NOT externally checked or formalised. Entry live main `087c53d34a286cc5ebfb36b9e8bd1370b2cc08e1`, tree `e8fcd85d12fd7ce91f75fbada4fab12bc6a1633f`, previous S164 PR #64 integrated exactly at its authored single-parent SHA; its sole parent `9cac7391ea9634d3c5f3493379b14b403cac031f` and 19 changed paths independently checked. No open PR or competing S165 branch/record; Actions workflows/runs 0, check runs 0, individual status contexts 0: ABSENT_NOT_PASS; rulesets [], protection API inaccessible UNKNOWN_403. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.

## A165 — Central target attempted first, not solved

Recall F_k: globally fair total computable Cantor-space maps with at most k ACTUAL COMPLETE inverse streams at every output; R_k = sources taken to CR by EVERY such map. For equality R2=R3, given x in R2 and a destructive G in F3, one must give an F2 detector for the SAME x. For strictness one must exhibit a single source x surviving EVERY F2 but destroyed by some F3. Additive-two means |G(x)|_m is computable from x restricted to m+2 input bits.

S164's clock theorem does not give source finance. The construction below resolves a narrower GEOMETRIC obstacle: an actual additive-two F3 can have an EXACT-TWO fibre over a Schnorr-random nonCR output, without restricting the exceptional outputs to an effective null closed tree. No randomness class for either inverse source is claimed, so E-08/E-00/S-00 remain OPEN.

## B165 — New internal constructive theorem: adaptive global F3 with two inverse streams over an exceptional Schnorr output

**Theorem B165.1 (all-output, fixed-use).** Let p:2^{<omega} -> {none,0,1} be ANY total computable next-bit prediction schedule. There is a uniformly computable total fair additive-two G_p in F3 with these properties:

(i) Each finite output tau has EXACTLY FOUR distinct length-(|tau|+2) source cylinders, and every sibling row is globally partitioned by its eight source children.

(ii) If an output y has infinitely many stages n with p(y|n) equal to y(n), and NO stage with p(y|n) defined and unequal to y(n), then |G_p^{-1}{y}|=2, with one complete inverse rooted in sector A and one in sector B.

(iii) Every other output has at most THREE complete inverse streams (in fact any output that ever fails a prediction has EXACTLY THREE). This includes outputs on which the schedule eventually stops predicting.

**Construction.** A row is a list of four tagged distinct source words of length m+2. Start at m=0 with R(empty)=[A:00,A:01,A:10,B:11] in ACTIVE phase 0 (A3/B1). All instructions below distribute every one of the eight source children exactly once. For convenience a_i0 means append bit 0 to source word a_i, NOT compute the output bit. At each ACTIVE output prefix tau, consult p(tau).

* ACTIVE phase 0, row [A:a0,A:a1,A:a2,B:b0]. If p(tau)=none, output-0 row is [A:a0 0,A:a0 1,A:a1 0,B:b0 0] and output-1 row is [A:a1 1,A:a2 0,A:a2 1,B:b0 1], BOTH remaining phase 0. If p(tau)=beta, put [A:a0 0,A:a0 1,B:b0 0,B:b0 1] at winning output tau beta (phase 1, A2/B2); put [P:a1 0,P:a1 1,S:a2 0,S:a2 1] at losing output tau(1-beta) (SAFE).

* ACTIVE phase 1, row [A:a0,A:a1,B:b0,B:b1]. If no prediction, output-0 row is [A:a0 0,A:a0 1,B:b0 0,B:b0 1] and output-1 row is [A:a1 0,A:a1 1,B:b1 0,B:b1 1], BOTH remaining phase 1. If p(tau)=beta, put [A:a0 0,A:a0 1,A:a1 0,B:b0 0] at the winning output tau beta (phase 0, A3/B1); put [P:a1 1,P:b0 1,S:b1 0,S:b1 1] at losing output tau(1-beta) (SAFE).

* SAFE row [P:p0,P:p1,S:s0,S:s1]: output-0 row [P:p0 0,P:p0 1,S:s0 0,S:s1 0]; output-1 row [P:p1 0,P:p1 1,S:s0 1,S:s1 1]. Both SAFE forever, regardless of p.

In each case the source-child sets of the two target rows are disjoint and exhaust all eight children, by direct inspection. Induction gives a partition of ALL length-(m+2) source words into the rows R(tau), |tau|=m. Consequently the output map is total computable with use m+2, continuous, onto, and globally fair: |G_p^{-1}[tau]| in measure is 4*2^{-(m+2)}=2^{-m} for EVERY tau, not just an exceptional ray. The row count is finite-source multiplicity, NOT the infinite fibre count.

**Full inverse audit.** Upon the FIRST incorrect predicted bit the output enters SAFE. In a SAFE suffix the two P cells at each stage descend from only ONE of the previous P cells (depending on that output bit), so there can be at most one complete P path; compactness shows at least one. Each of the two S cells contributes exactly one coherent full path, so the SAFE fibre has exactly 1+2=3 full paths. This remains true when the incorrect branch has crossed an A/B tag boundary.

If the output NEVER fails and makes only FINITELY MANY predictions, after its last prediction it remains forever in phase 0 or 1 with only FREE transitions. For phase 1, at every FREE step both A descendants originate in just one A parent and both B descendants from just one B parent, so each sector has exactly one infinite inverse path. For phase 0, the ancestor-index maps for the three A child slots on output bits 0 and 1 are respectively (0,0,1) and (1,2,2); BOTH have image size 2. Thus three distinct complete A paths cannot survive any sufficiently late FREE step: at a level separating three paths, all three A cells would need descendants into the next output row, but one of three parents has NO child in that row. Hence at most TWO full A paths, and B supplies exactly ONE. In either phase degree<=3. This argument also covers a schedule that stops forever at the root.

If the output NEVER fails and has infinitely many predictions, the phase toggles on every correct prediction. Therefore arbitrarily late successful phase-0 stages retain only parent a0 of sector A, and arbitrarily late successful phase-1 stages retain only parent b0 of sector B. Two distinct full paths in the same sector would be separated at some finite row, contradicting one of those later unique-parent transitions. Each sector has a full path by compactness: its finite compatible prefix tree is nonempty at every depth, nested and finitely branching. The two root sectors are disjoint. Therefore degree EXACTLY TWO, not 3 or a hidden 4. QED (internal mathematical proof).

**Corollary B165.2 (S011 supplies a genuine Schnorr-exceptional y).** S011 gives a computably random Y and a total computable globally fair cap-two no-repeat scan F with y=F(Y) nonCR. At every output prefix tau its algorithm decides whether the next output bit is a predicted sentinel and, if so, which bit b is predicted. Define p(tau)=b in that case, otherwise none. This is a TOTAL computable schedule. Along y every epoch triggers after finitely many filler outputs; infinitely many sentinel stages occur, and EVERY prediction is correct. Therefore the above G_p is a globally legal fixed-additive-two F3, and |G_p^{-1}{y}|=2. Since Y is CR (hence Schnorr random), and F is total computable fair, y is Schnorr random. Yet the total exact rational S011 output martingale wins on y, so y is NOT CR. By B164 this output martingale has 2^k threshold times eventually later than every total computable schedule. Thus the exact-two F3 exceptional output really has the required SCHNORR-SLOW clock.

No input of G_p over this y is yet shown CR, still less R2. In particular this is NOT a proof that G_p destroys R2 or even CR. The S011 source Y is NOT R2; identifying Y with either inverse of G_p is unjustified. The theorem refutes ONLY the shortcut that exceptional exact-two output geometries must be effectively Schnorr-null, while leaving the SAME-SOURCE hurdle intact.

## C165 — Effective stopping-selection mass obstruction and conditional finance

For a separate TOTAL computable schedule p_K, look at the FIRST 1 in an infinite output at position 2e; after seeing that first 1, predict a 0 once if and when machine e is observed to halt, otherwise never predict. At finite tau this is computable by bounded simulation, with prior-trigger status reconstructed from tau. Let K be a noncomputable c.e. halting set. The set E of outputs having at least one predicted bit is effectively open and has exact measure

  lambda(E)=sum_{e in K} 2^{-(2e+1)}.

These disjoint first-1 cylinders give a base-four coding of K with separated digits, so this real is not computable. The event 'some trigger eventually occurs' does NOT have a computable price merely because the local schedule is total and every finite prefix is decidable. This is a standalone S155-style clock countermodel; NO claim is made that S011's particular p has this noncomputable mass.

For G_p, actual sector inverse selection over the all-correct infinitely-challenged class depends on arbitrarily late decisive stages, and the class is described by a conjunction of 'no incorrect wager' and 'infinitely many wagers'. A finite-level selector measure using a computable output betting law μ can be exactly rational for each bounded stage; but the infinite-success/stall decomposition need not have computable probabilities or effective convergence tails. To invoke C164 and transfer an output winner onto either SAME source, one still needs a uniformly computable-real projective source law nu[s] on EVERY cylinder, and capital divergence along that exact inverse. Neither follows from degree two, existence of pointwise partial selectors, nor convergence of finite-stage laws. This session found no such source law and no legal F2 detector.

## D165 — Controls and full separation of claims

S135's global fixed-use F3 oscillator has exactly two streams over a computably effectively null class T, where S135/S162 already supply source winners. G_p is different: y=F(Y) is Schnorr random and is outside any computably closed null class, yet its actual G_p fibre is two. S158's fixed-use F2 delayed selector shows no uniform posterior cutoff; our infinite challenge schedule has a separate indefinite-stall issue. S155 codes noncomputable fold mass; C165 concerns only a separate first-trigger event. S141's benign positive folds show source-local ambiguity is necessary but insufficient. S117's posterior-volatility output martingale does not by itself yield SOURCE finance. S163's 0/10/11 prefix decoder has exactly THREE inverses for all outputs and preserves CR. S011 itself is an F2 destroyer of Y, not an R2 separator. S109, S129, frozen S101–S103, Y/M/H/X and all source grades unchanged.

Only the B165 geometric result and C165 general effectiveness countermodel are advanced here. E-08/E-00/S-00, R2=R3 equality/strictness and the R2-to-MLR question remain OPEN. No novelty, external verification, hosted CI pass, Lean, Palomar, manuscript or publication assertion.
