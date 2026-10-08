# P4-S051 Validation — cross-target escrow

Date: 2026-10-08
Session: P4-S051
Incoming checkpoint: 96bfc1d1cfb351e14eb874202ff1858b0e0709aa
Mathematics: phase4/P4-S051_MATHEMATICS.md
Disposition: **PASS — conditional finite-information theorem only**

## Authority and uniqueness
- Incoming main compared identical with 96bfc1d1cfb351e14eb874202ff1858b0e0709aa; no P4-S051 mathematics file existed. PASS.
- P4-S001 through P4-S050 mathematics, required CAND-01 authority, active pivot and all designated special-focus records inspected. Prior results frozen. PASS.
- P4-S011 Y, self-avoiding wtt M, P4-S033 H and X=H^{-1}(Y), the CR inclusion chain and unresolved X in OH all retained. PASS.

## Three-coordinate implication
- Ref_{s,t}(a,beta) excludes actual (s,t)=(a,beta).
- Ref_{s,u}(1-a,gamma) excludes actual (s,u)=(1-a,gamma).
- If both t=beta and u=gamma, the first forces s=1-a and the second forces s=a: impossible. PASS.
- No semantic trapped-epoch oracle, actual old bit constant in code, or nonhalting inference used. PASS.

## Fair wagers
- With normalized initial capital 1, t-branch children: 2/3 on beta, 4/3 on 1-beta; mean 1.
- On t=beta, u-children: 0 on gamma, 4/3 on 1-gamma; mean 2/3.
- On t=1-beta, u-children: 4/3,4/3; mean 4/3.
- Terminal table (beta,gamma),(beta,1-gamma),(1-beta,gamma),(1-beta,1-gamma): 0,4/3,4/3,4/3; mean 1.
- Each wager precedes the corresponding fresh raw query; s is never read by this hedge. PASS.
- Same-target opposite rows at a common future beta force t=1-beta and give factor 2; same old row across both beta only forces s and requires reading s for doubled capital. PASS.

## Finite projection criterion
- For each target tuple v, old support A(v) is the intersection of the old values not excluded by any E_i at v_i. A tuple is genuinely excluded iff A(v) is empty.
- If all 2^m tuples survive, a nonnegative fair terminal target-only payoff cannot be strictly above 1 at every tuple. If r>=1 tuples are ruled out, the flat payoff 2^m/(2^m-r) on all allowed tuples, zero elsewhere, has mean one and strictly positive gain. PASS.
- Sequential binary conditional expectations give rational nonnegative fair stakes for any fixed finite list of targets. PASS.

## Escrow implementation
- Initial phase protects s,t; a finite positive witness initiates a finite closure phase protecting s,t,u; no permanent second hole is permitted. PASS.
- Any outside protected support is queried only at zero stake and is recorded; protected supports are suspended. Simulations of all four corners are finite bounded slices, with no assumed halting-time bound. PASS.
- At a matched positive closure the algorithm reads fresh t,u and retains s. At finite timeout it consumes protected t,u and retains s; orientation/old-branch reset reads s only with positive evidence. PASS.
- Alternating least-unread sweep plus bounded tenures queries all outside a final permanent s. Infinitely many s-resets consume successive least-unread coordinates, so any fixed coordinate is eventually queried. Consequently no infinite transcript omits more than one coordinate. PASS.
- Query index depends only on previous output bits, all indices are fresh, so cylinder probability is exactly 2^{-m}; global fair coin and fibre size <=2. PASS.

## Success and P4-S008 guard
- Every completed positive escrow earns 4/3; positively forced one-bit bets earn 2; zero-stake passages leave capital unchanged. Infinite completed positive exits yield one computable succeeding output martingale. PASS **conditional on actual infinite executions**.
- On a computably random X, infinitely many such gains with one permanently omitted fixed s would violate the P4-S008 fixed-sentinel permutation-completion theorem. Hence the reset-free approach is locally finite on a fixed never-reset epoch of a CR source. PASS.
- No source-specific theorem ensures an infinite sequence of such exits with effective old-sentinel turnover. PASS.
- Any certificates found after either wager target is read are expressly **not** counted as matched unread closures. PASS.

## Final guard audit
- No proof X in OH, X not in OH, R_2=OH, OH non-invariance, or strict R_2 versus OH separation.
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim.
- Phase 4 OPEN, Phase 5 CLOSED. Overall **VALIDATED conditional mathematical result**.
