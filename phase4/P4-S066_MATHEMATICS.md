# P4-S066 — actual-source localization of infinite-horizon gate hazards

Date: 2026-10-08
Session: P4-S066
Incoming live main: f1ecb939367d6ccd1246cfa5f2647c0fa14ccb7d
Disposition: **VALIDATED PATHWISE NECESSARY SUMMABILITY AT A PERMANENT CR STALL; NO VERIFIED SOURCE-X RECURRENCE**

## 0. Authority, frozen scope and unchanged controller

Incoming GitHub main matched the exact P4-S065 outgoing SHA. Its recursive tree contained P4-S001–P4-S065 mathematics, validation and close records and no P4-S066 record. Inspected all mathematics records in session order, the P3-S007 CAND-01 selection, P3-S008 Gate-3 PASS, the post-S031 pivot, especially S008, S011, S012, S027, S033, S039, S041 and S044–S065. All validated prior proofs and formulations are frozen.

Retain
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]
Preserve the committed computably random Y, the syntactically self-avoiding globally use-clipped wtt autoreduction M, the repeated-block computable fair-coin homeomorphism H and X=H^{-1}(Y). H(X)=Y is not in OH; X in OH and R_2=OH remain unresolved.

Fix ANY total computable prospective tenure L and the UNMODIFIED P4-S057 success-gated four-run one-hole controller T_L. The old s is the least unread raw coordinate, each future block is the least wholly unread disjoint (t,u,v), v and the clipped outside finite-use frontier are exposed, and exactly four paired representative M(q) traces are simulated. Only a finite positive ordinary wrong-output/nonbinary halt before protected consumption licenses a gate. At a positive gate the exact fair three-coordinate wager has terminal ZERO on the one excluded atom, 8/7 on each of the other seven, with the intermediate fair ledger unchanged; it consumes s,t,u. Every finite timeout consumes t,u at ZERO stake and performs its mandatory non-s sweep WITHOUT OLD RESET. All branches remain total, no-repeat, fair-coin preserving and of global fibre cardinality at most two. No new controller is proposed.

## 1. A genuinely transcript-local exact next-gate hazard

Fix a valid finite epoch-start OUTPUT word h. Let p_0=h. Whenever the TRUE controller completes its n-th unsuccessful reservation after h, with real t/u zero-stake release and non-s sweep and still no old reset, let p_n denote the entire emitted OUTPUT prefix at the start of the next reservation. These p_n include every actually exposed control bit, released future bit, use-closure bit, and sweep bit. For any valid such p, let E_p be the event, among fair independent future OUTPUT bits of the TRUE scan, that the next single finite reservation ends in a GENUINE timeout, rather than a positive gate. Define
\[
r(p)=\lambda_{\mathrm{output}}(E_p\mid[p]),\qquad
\gamma(p)=1-r(p).
\]
These are uniformly computable exact rational numbers for valid p (indeed dyadic), by finite exhaustive branching through the total prospective L, capped four M traces and genuine terminal action. A reservation is finite on ALL sibling histories and has a terminating effective finite output decision tree. On a genuine timeout p_n to p_{n+1}, necessarily r(p_n)>0. No semantic source-X runtime or off-line eventual M halt is consulted.

On a hypothetical permanent stall write
\[
\gamma_n(Z,h)=\gamma(p_n(Z)),\quad r_n=1-\gamma_n.
\]
This is a computable function of each actually observed finite transcript, but its infinite series is not computable in advance. Crucially the p_n are the REAL endogenous fresh-block trajectory, not a compulsory-old-reset shadow and not the surviving-frontier ensemble. Flipping only the permanently unread old s does not change p_n or gamma_n until the old bit is consumed.

P4-S065's c_n(h)=1-q_{n+1}(h)/q_n(h) is instead the weighted mean of gamma(p) over ALL p on the n-timeout surviving frontier, conditional on survival. Equality of that average with the value gamma(p_n(Z)) is NOT asserted.

## 2. An exact computable OUTPUT martingale on the local timeout tree

**Lemma 1 (finite-reservation timeout hedge).** Starting at a valid next-reservation output prefix p with capital C>=0 and r(p)>0, there is a uniformly computable rational fair output martingale, run only until the end of that reservation, which pays C/r(p) on its genuine timeout leaves and ZERO on its positive-gate leaves.

**Proof.** E_p is computably clopen relative to the finite decision tree. Before termination at a partial output continuation w, set the capital to
\[
D(pw)=\frac{C}{r(p)}\lambda_{\mathrm{output}}(E_p\mid[pw]).
\]
All conditional probabilities are exact computable rationals, and
\(D(pw)=\tfrac12(D(pw0)+D(pw1))\). Its initial value is C, its timeout terminal value is C/r(p), and its gate terminal value is zero. Freeze capital after the terminal action. Where r(p)=0, define the strategy to freeze instead; a genuine timeout is impossible on such a branch. QED.

**Lemma 2 (one global computable timeout martingale).** For any fixed valid h, the hedges in Lemma 1 combine into ONE total computable nonnegative rational fair martingale D_h on output strings. It leaves capital unchanged before h and outside the h-branch, starts with capital one at h, and within that epoch recursively bets on the first timeout, the second timeout, and so forth, stopping at its first positive gate. On a run that really completes N consecutive timeouts without old reset,
\[
D_h(p_N)=\prod_{n<N}\frac1{r(p_n)}
=\exp\left(\sum_{n<N}-\log(1-\gamma(p_n))\right).
\]
**Proof.** Every reservation closes on every continuation after finitely many output bits and every timeout emits t,u plus the required non-s sweep, so no finite output word can contain infinitely many completed reservations. Reconstructing T_L state from the finite output prefix and computing the finite conditional timeout tree makes the composite martingale value a terminating rational computation on EVERY output word. At each successive completed timeout the terminal value of the previous hedge is the initial value of the next hedge. For a completed positive gate, capital becomes zero and freezes. Across the finite pre-h prefix, use a constant martingale; freeze on all incompatible h branches. The exact half-sum identity holds at every output node, including transitions between hedges. QED.

## 3. Pathwise summability is necessary for a permanently stalled CR source

**Theorem 3 (source-local infinite-horizon hazard obstruction).** Let Z be ANY computably random RAW source. Suppose TRUE T_L on Z genuinely reaches h and then finishes infinitely many consecutive TIMEOUT reservations, with t/u ZERO stake release, non-s sweeps and NO positive gate or old reset. Then, for its actual finite-transcript hazards,
\[
\boxed{\quad
\sum_{n=0}^{\infty}\gamma(p_n(Z))<\infty,\qquad
\prod_{n=0}^{\infty}(1-\gamma(p_n(Z)))>0.
\quad}
\]
In particular there is a source- and epoch-dependent positive lower bound on all finite products of next-timeout conditional probabilities. No effective uniform bound or computable modulus is claimed.

**Proof.** Let s be the old sentinel selected at the actual start h. Since it remains unread forever after h, it was never queried by T_L anywhere earlier on this source. Apply P4-S008's *fixed-sentinel permutation completion* to the WHOLE global-k=2 no-repeat scan T_L: first read s, simulate T_L on later fresh coordinates, and if T_L ever requests s, switch to reading every other remaining coordinate in increasing order. On EVERY transcript this P_s is a total computable exhaustive fair-coin scan, hence a computable fair-coin homeomorphism with computable inverse. It sends computably random Z to a computably random output P_s(Z), by P4-S001.

A total computable rational output martingale on T_L output can be copied to the P_s output after the initially ignored s-bit, and frozen if T_L requests s. On the present permanently stalled Z, no switch occurs and the replayed output after the first bit is exactly T_L(Z). Thus success of D_h from Lemma 2 would contradict computable randomness of P_s(Z). Therefore the sequence D_h(p_N) is bounded. But it equals the displayed increasing finite product, so the sum of the nonnegative quantities \(-\log(1-\gamma(p_n))\) is finite. Since \(\gamma\le-\log(1-\gamma)\) for 0<=gamma<1, the displayed hazard series converges, and the timeout product has positive limit. QED.

**Critical transfer guard:** A generic martingale on a nonmonotonic one-hole scan's output does NOT become a computable martingale on the RAW source by naive pullback. Here P4-S008 permits the transfer ONLY because the supposed source path permanently omits a FIXED raw sentinel, while P_s is a genuine computable homeomorphism on all source inputs. This is exactly the structural fact that makes the theorem valid on a CR source without assuming T_L(Z) itself is computably random.

**Corollary 4 (exact local divergence exclusion).** On any source Z in CR, no genuinely permanent old-sentinel stall can coexist with \(\sum_n\gamma(p_n(Z))=\infty\). Hence a verified *actual-source-specific* divergence assertion for every hypothetical perpetual no-gate epoch of a fixed L would force a first real positive gate at every reached epoch and therefore infinitely many sound profitable 8/7 resets on the committed X. This is a CONDITIONAL supplier only: NO such divergence has been verified on X or on its committed endogenous schedule.

## 4. Strict distinction from frontier-averaged summability

At positive q_n(h), P4-S065 gives exactly
\[
c_n(h)=\mathbb{E}[\gamma(p_n)\mid A_{h,n}],
\]
where the expectation ranges over ALL n-timeout survivors and their different revealed prefixes. Theorem 3 instead constrains the series of \(\gamma(p_n(Z))\) on each individual CR permanently stalled path. Summability of \(\sum_n c_n(h)\) does NOT, as a purely mathematical point, imply convergence of the pathwise series on every infinite surviving path.

**Abstract sharpness model (NOT a T_L or M/Y/X witness).** After a fair switch bit, let the 0 arm lock into certain timeouts forever. On the 1 arm, each fresh independent fair control bit gives an immediate gate if it is 1, and a genuine timeout if 0. Supplement each timeout with harmless fresh releases/sweeps; omit an unrelated old bit forever. For n>=0 the survival probability from before the switch is
\[
q_n=\frac12+\frac12\,2^{-n},
\]
so q_infty=1/2 and the averaged c_n series converges. Yet the single surviving risky path with switch 1 and every later control bit 0 has gamma_n=1/2 at EVERY trial: its local sum diverges. This path is not CR (Theorem 3 forbids CR there in the fixed-hole setting). The abstract model demonstrates that a positive averaged survival floor does not provide a uniform local bound on arbitrary individual survivor trajectories; it is NOT a legal committed four-run certificate model.

Conversely, if q_infty(h)>0 then P4-S065 Corollary 4 ensures SOME CR member of F_h; by Theorem 3 its individual hazard series necessarily converges. Therefore a universal all-F_h-paths divergence claim at a positive-survival h cannot hold. This does NOT rule out a separate, stronger source-X-specific argument excluding the committed X from F_h even when some off-X CR siblings remain there.

## 5. Actual-source boundary and frozen invariants

Theorem 3 is an unconditional necessary property of EVERY hypothetically permanently stalled computably random source, stronger in its *individual-transcript* quantifier than the P4-S065 averaged necessity. It does not compute the permanent-stall membership decision, force a positive \(\gamma_n\) lower bound, give a computable summability modulus, establish divergence on X, or prove a repeated positive gate. In particular neither Y/X highness, eventual M^Y(q) halts, globally clipped finite values, total preselected L, nor an abstract effective Pi^0_2 progress specification supplies the missing genuine gate recurrence.

The P4-S065 statements q_infty>0, summable frontier c_n, and every finite B deficit >=q_infty at any permanently stalled CR epoch remain unchanged; these are distinct from the new pathwise product condition. The P4-S008 persistent-hole safety, P4-S052 shielded-old no-orientation, P4-S053 all-transcript reset bar, P4-S056 forced-reset theorem, and P4-S057–P4-S065 conditional renewal/rarity/dependence laws are all frozen. All actual exact least-unread/fresh-block, four-paired-M, positive-certificate, deadline, timeout, fair 8/7/zero and global one-hole rules remain unchanged.

**Disposition:** verified a stronger source-local necessity at a hypothetical infinite timeout path; NOT a verification that such a path is taken by X and NOT an infinite positive-renewal theorem. Thus X in OH, X not in OH, R_2=OH and OH non-invariance remain unresolved. PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS; Phase 4 OPEN; Phase 5 CLOSED; Gate 4 not reviewed. No novelty, openness, prior-art, publication or outreach claim.

**P4-S067 bounded target (no owner/external blocker):** determine whether the particular Y/M/H and its endogenous true timeout sequence imposes any *verified* violation of the necessary local summability law on a hypothetically permanently stalled X, or a still sharper fixed-hole effective local obstruction. Avoid inferring actual infinite success from the finite g(p), from averaged c_n, or from an abstract non-stall assumption.