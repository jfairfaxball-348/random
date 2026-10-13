# P4-S122 — Hostile validation and finite sanity (same-agent, independent in method)

Entry main `343342ccfd4ebdb47af1aeddbfb43c574f690fe7`, its sole parent `dacdc9af4828ab3df66f858a00deb86bc06277f3`, tree `c72dade8e24659036e4c4f9d35d4817f117aaec6`, PR #19 merged non-force; S122 branch and files absent; Phase4 OPEN. Source grades, frozen S101-S103 A-C, Y/M/H/X, DEF-0020/PA-0001 unchanged. Hosted workflow files/runs/jobs/check-runs/status contexts ABSENT_NOT_PASS; rulesets empty; branch protection 403 UNKNOWN. No independent external or formal review.

### Hostile S121 replay

- Enumerated candidate measure indices: a valid nonzero computable finite measure at depth n_e=e+6 has a positive cell, correct rational error <=2^-k ensures q>2^-k eventually. An invalid index pays at most one cylinder regardless of false claims. Cost bound 1/32+1/64 and dense strict extension remain correct.
- Recomputed the noncomputable total mass contradiction: if lambda(U) computable, lambda(U intersect [s]) is the computable difference between lambda(U) and the lower-semicomputable off-[s] part, and is also lower-semicomputable itself; then restriction to K yields a nonzero computable supported measure, contradiction.
- Tested G_U output-prefix inversion by replaying source cells rather than trusting on-path pictures: no release gives 0tau,1tau; after release the key is fixed by emitted bit, and the unconsumed bit is the one free cell. Exactly two length-(m+1) cells. Both infinite inverses real. Key posterior 1/2 before and 0/1 after.
- Tested S121 q_B via conditional expectations on four source cells: exact grid 1/4; the variance compensation M=v+sum(delta^2) is nonnegative and rational. For CR OUTPUT only, infinitely many changes imply unbounded success; no effective last change and no transfer to NONCR target. All support/ramification no-go conclusions explicitly restricted to computable beta supported on K/Ram.

### Hostile A122 compiler audit

Independent index-coefficient check: geometric p_infty=1/2 and p_t=2^-t-2 sum to 1; for n, p(infty or t>=n)=1/2+2^-n-1, EXACT rational, not an approximation. The t/r clocks are independent; a finite prefix involves just (n+1)^2 grouped index choices and finitely many labels. Each XOR mask is fixed before sampling any source bit, so d(s XOR mask) satisfies the exact source martingale law. Two chosen finite/infinite indices carry fixed positive mass, not shrinking with n. Optional finite-flip mixture has fixed-F coefficient >=(1/2)prod epsilon_i and preserves rationality and fairness by sibling averaging. Special F_(U,h) masks are zero BEFORE t; their release bit is a XOR b. No-release requires p_infty>0; dropping that atom would INVALIDATE domination on sources never releasing. Source-key lift preserves root and child average. This is a compiler ONLY for a parametrized XOR-orbit class; source FOLD rows are not XOR permutations.

Potential hostile trap: finite-horizon expectation E[d(F(X)|m)|source-prefix] is NOT a coherent martingale as m varies. A122 does not use it; it takes an ordinary fixed-mask source martingale first, then a single exactly rational mixture of those coherent accounts.

### Hostile B122 oracle audit

At a CR y in K, any alleged total-on-CR selector/posterior routine must output its first bit/value with finite use. A dense triggered continuation extending the same prefix exists; its earliest trigger t is after that prefix because the output-trigger schedule is finite-prefix determined and does not trigger along y. The trigger bit is free until emitted; choosing the opposite key gives a **positive cylinder**, hence some CR y', contradicting selector continuity. For listing both inverses, {0,1} versus {c,c} is the contradiction; for posterior, 1/2 versus c-dependent 0/1. The proof does NOT assert that a given inverse x is not y-Turing-computable nonuniformly; S118's x<=T y remains intact. It also does not assert any nonCR output.

### Exact finite sanity

Local Python stdlib Fraction audit: two independently activated infinite computable masks with 2 labels each, weights including infinity, ordinary d(s)=prod of 3/2 or 1/2 bets. For every binary s at levels n=0..6: 127 exact D_2(s)=(D_2(s0)+D_2(s1))/2 identities PASS. Compose a second independent finite-flip law epsilon_i=2^-i-2: for every s at n=0..4: 31 exact identities PASS. Second independent simulation of a release-at-prior-01 output-trigger transducer, masked/unmasked and m=1..9, finds EXACT two (m+1)-source words per output cylinder, key posterior 1/2 or 0/1, for 2*(2^10-2)=2,044 cases PASS. All finite sanity only, not proof of infinite fibres, all-U, all-masks, or mathematical novelty.

**Hostile failure ledger:** (1) no globally fair legal paired two-CR BAD output; (2) no c2 universal coherent rational compiler; (3) two late XOR clocks are not two source FOLD clocks; (4) no uniform CR-domain selection is NOT general failure of beta-free capital; (5) no EQ/SEP, SAME-SOURCE hierarchy, or unrestricted iteration. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.
