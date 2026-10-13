# P4-S115 — Dependencies, first unproved inferences and failure register

| Item | Mathematical dependencies | Status |
|---|---|---|
| S114 powerset / real pairs | c-bit histories, r-split pending state, late-depth König, all actual limit paths | RECHECKED, no fatal gap |
| S114 rational boundary | finite absorbing Markov chain, undecided-to-dead path bound | RECHECKED, geometric rate |
| B115-1 safety core | S106 D_r Pi01 and clopen interior chart; fairness, CR implies Kurtz | NEW INTERNAL SUFFICIENT criterion, not universal |
| B115-2 rational squeeze | finite clopen D_r over-approximants and safe-open under-approximants | NEW INTERNAL algorithm; computes lambda D_r under the core promise |
| B115-3 moving hazard | decidable nested undecided clopens and effective product-to-zero | NEW INTERNAL sufficient bound |
| C115 perfect E quotient | S108 first-exit exact-two/fair proof + decidable power-of-two predicate | NEW EXPLICIT nonregular instance, all sources/limits accounted |
| Nonregularity of K | ultimately periodic unary acceptance in finite automata; odd powers-of-two gaps | PROVED INTERNALLY |
| Double-fibre CR destruction | S083 singleton witness; S004 vanishing weight; S005 stopping-price warning | NOT FOUND |
| EQ/SEP, R2-R_L1, arbitrary F2 iteration | universal and same-source quantifiers; F2 composition cap issue | GENERAL UNRESOLVED |

FAILURE F115-1: finite-state pair disagreement must be stored through first r bits; coalesced machine states may represent genuinely distinct early source histories.
FAILURE F115-2: a c.e. inner safe-open core whose Pi01 residual has zero measure forces computable D_r mass. Thus noncomputable D1 (S112) prohibits this method even though its map conserves CR.
FAILURE F115-3: nonregular and even perfect infinite ramification boundary can be effectively null, so no logical implication from nonregularity to a paired CR destroyer.
FAILURE F115-4: fat nowhere-dense positive-mass ramification examples show effective-null boundary is not globally valid. Positive boundary alone also does not imply failure of CR conservation.
FAILURE F115-5: pairing a known singleton destroyer requires both all-output inverse counts AND fair cylinder prices; a fixed target-only second inverse is insufficient.
FAILURE F115-6: finite row balance and 48-hybrid transitions remain finite prefixes, not an actual persistent pair.
FAILURE F115-7: R2, R_L1 and iteration require SAME-source and correct globally legal fibre caps, not inference from a composition of cap-two maps.

No source-access upgrades, novelty claim, external review, Lean, Palomar or publication. Gate3 PASS; Gate4 NOT REVIEWED; Phase4 OPEN; Phase5 CLOSED. Y/M/H/X, DEF-0020/PA-0001 and S101–S103 A–C unaffected.
