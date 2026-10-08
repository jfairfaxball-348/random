# P4-S071 Validation — global shear evaluator and exposure bound

Date: 2026-10-08
Incoming pinned main: 303cbb1ce2d4fc202462901bc0071bcbf7cc8b7a
Disposition: **PASS — QUANTITATIVE SAME-SOURCE CONDITIONAL PRESERVATION; GENERAL SHEAR QUESTION OPEN**

## Authority and uniqueness — PASS

Live main matched requested SHA. Recursive tree had P4-S001–S070 complete and NO P4-S071. P3-S007 selection, P3-S008 Gate-3 PASS, both Phase-4 pivots and S070 mathematics/validation/close inspected; prior mathematics S001–S070 reviewed, particularly S008/S011/S012/S027/S032–S044/S052–S057/S065–S070. All previous results frozen. Phase 4 OPEN; Phase 5 CLOSED; no blocker.

## Infinite source-side legality — PASS

For EACH selected shear block, raw a comes from virtual u, raw b is queried fresh when virtual v is requested, and raw c is queried at first virtual request for either v or w; for v-before-w it is a genuine zero-stake filler. Unselected blocks copy identity requests. Thus raw omissions in E blocks can be caused only by virtual u or v omissions. A virtual one-hole transcript cannot omit both v and w, so cannot leave raw c unread. Every complete raw transcript omits at most one raw position, globally. Virtual w silently skipped after v is taken from one of finitely many previously read c positions at any fixed raw stage; infinite silence is impossible, so next raw query is a total computable operation. Fairness follows from every real output querying one fresh raw bit.

## Martingale and exposure — PASS

For rational d, fractional s(tau) in [-1,1] is uniformly exactly computable at all positive parent-capital nodes; zero parent nodes get zero stake. Raw c fillers carry zero stake. At live requests raw e copies the virtual factor (flipping sign for b xor known c). At a spoiled w request d receives m_t<=1+|s(tau_t)| and e gets no raw output or bet. Therefore d_m<=e_{n(m)} product_spoiled(1+|s|)<=e_{n(m)} exp(B_m) for every source. z in OH bounds e on the legal raw scan; this gives the restricted preservation theorem and the necessary log(d_m)<=C+B_m for every putative OH separator. No uniform/c.e. bound on B_m has been assumed.

## Independent finite sanity check — PASS (NOT proof)

Enumerated two blocks, all 7 omissions (none or one of six virtual positions), all remaining virtual permutations, all 64 raw assignments and E empty/alternating/all, 276,480 tests: zero counterexamples to one-hole missing-set or the discounted-capital inequality under representative rational stake rules. The infinite proof is in P4-S071_MATHEMATICS.md, not inferred from these tests.

## Scope and governance — PASS

The resulting general raw evaluator is a legitimate same-source one-hole scan but not an exact factorization of the virtual map or a full preservation theorem: later c bets are skipped and can accumulate unbounded gain. Case C is not solved and no CR-in-OH witness was produced. S034–S036 previous live/spoiled/packet results are retained rather than re-labelled as new. No P4-S057 controller was invoked; original Y/M/H/X and all exact four-trace, prospective deadline, zero-stake t/u release/non-s sweep WITHOUT old reset, seven 8/7/one ZERO payoffs frozen.

X in OH, H-pres, R_2=OH, R_2=OH^iso and general OH invariance remain unresolved. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED; no novelty/prior-art/openness/publication/outreach claims. Blocker NONE. P4-S072 runnable.
