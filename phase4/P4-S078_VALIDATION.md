# P4-S078 VALIDATION — global single-shear criterion (algebraic, not preservation)

Date 2026-10-09. Pinned incoming live main `178948859e2cf6853a90bbb36fcb8837bf59292b`. P4-S078 unique: exactly 77 incoming complete mathematics/validation/close triplets, zero S078 triplets. P3-S007 CAND-01 selected, P3-S008 Gate-3 PASS, both pivots and S001–S077 mathematics reviewed (focused S011/12, S032–044, S057, S069–077). S077 validation/close reviewed.

**PASS for algebraic global reduction and explicit finite X-chain ONLY. NOT a universal OH preservation theorem, not a witness of nonpreservation, not a resolution of R₂=OH, R₂=OH^iso or X∈OH.**

1. On blocks j∉E, Q_E=identity and S²=identity. On j∈E, the exact F₂ matrix word `q s q s q` equals s. This is an identity on each block independently of all other blocks and holds on the full infinite product; it is NOT a limit of finite-support transfers.
2. Q_E is always an everywhere-computable coordinate permutation because E is decidable, hence preserves OH in both directions by S033. If the single full-support S preserves OH, twice invoking preservation in the word proves all E. Converse chooses E=ℕ. S070 provides equivalence with H and computable blockwise GL3. No general computable-homeomorphism invariance is assumed.
3. Counterexample reduction: either the first S call on Q_E(z) exits OH or, after Q_E transports the intermediate inside OH, the second S call must exit. Both candidate sources are CR. This does not yield an algorithm deciding OH status.
4. Exact eight-step H path has three S factors and five R/Q swaps. Intermediate row words after R,S,Q,R,S,Q,R,S equal `010/100/001`, `010/101/001`, `010/001/101`, `001/010/101`, `001/111/101`, `001/101/111`, `101/001/111`, `101/110/111`; last equals H matrix `101/110/111`.
5. For the committed X chain with final Y∉OH, ASSUMING X∈OH gives one of three explicit S transitions out of OH; no unconditional classification of X follows.
6. Exact exhaustive four-block audit compared Q_E S Q_E S Q_E to S_E on all 16 supports and all 4096 source assignments: 65,536 integer equality checks, zero differences. Independent local BFS with generators S,Q,R reached exactly 168 GL3 matrices with maximum discovery depth 10; shortest path to the committed A uses 8 operations. These finite checks do not certify any randomness assertion.

Frozen governance: all validated S001–S077 and original Y/M/H/X preserved, S057 exact controller not invoked. S037/S073–S077 unchanged. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE, DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED; no novelty, openness, prior-art, publication or outreach action. Blocker NONE.
