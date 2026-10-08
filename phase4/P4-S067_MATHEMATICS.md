# P4-S067 — Source-specific testing of local gate-hazard summability

Date: 2026-10-08
Session: P4-S067
Incoming pinned live main: `d607ccf2920511eb87f8647b798b4d2a4dc25a9b`
Scope: Phase 4 — Mathematics ONLY
Disposition: **VALIDATED COMPUTABLE GATE-LEAF DEPTH/CAPACITY OBSTRUCTION AND EXACT INTENSIONAL CLOCK LIMITATION; NO VERIFIED X-SPECIFIC HAZARD DIVERGENCE OR REPEATED GATES**

## 0. Authority, unchanged objects and exact question

At session entry live remote `main` equalled the required P4-S066 outgoing SHA. The complete repository tree had P4-S001–P4-S066 mathematics, validation and close records, and no P4-S067 files. All 66 mathematics records were fetched in order. Inspected P3-S007 selected CAND-01, P3-S008 Gate-3 PASS and `phase4/P4_RESEARCH_PIVOT_AFTER_S031.md`, with targeted close reading of S008/S011/S012/S027/S033/S039/S041 and S044–S066. No conflict with authoritative records and no new session ownership/external blocker was found.

Freeze
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]
Preserve the committed computably random Y; the **committed program** M, syntactically self-avoiding, wtt and globally use clipped; the repeated three-bit fair computable homeomorphism H; and X=H^{-1}(Y), which is computably random, with H(X)=Y not in OH. **X in OH and R_2=OH remain unresolved**.

Fix the exact P4-S057 genuine success-gated controller T_L for any total computable positive prospective L(e,k,p)>=1. On every branch old s is the least unread coordinate; each new reservation selects the least wholly unread disjoint t,u,v block; it exposes v and the clipped finite use closure outside protected s,t,u, and simulates precisely four paired M(q) representative traces with a prospectively fixed finite L. Only a positive ordinary wrong-output/nonbinary halt BEFORE protected consumption licenses a gate. A gate consumes s,t,u, pays zero at exactly ONE forbidden atom and 8/7 at the other SEVEN. Each timeout releases t,u at ZERO stake, makes the mandatory least-unread non-s sweep and **does NOT reset s**. Global totality, no-repeat, fair coin, one-hole fibres and the exact intermediate fair ledger remain unchanged.

P4-S066 constructs, at each valid true post-timeout reservation prefix p, a computable exact rational gate hazard gamma(p). At an infinitely stalled computably random source trajectory (p_n) P4-S066 proves
\[
\sum_n\gamma(p_n)<\infty,\quad \prod_n(1-\gamma(p_n))>0.
\]
This is a pathwise necessary condition, not the P4-S065 averaged c_n. We test what additional finite certificate information it actually yields and whether the committed source automatically violates it.

## 1. Exact finite gate-leaf decomposition

Take any valid **next-reservation start** output prefix p. Follow the unchanged T_L for just ONE reservation on all possible independent future output bits. Stop a branch at the instant the first positive gate decision has been *made before consuming any protected s,t,u bit*; label this terminal node G. On a timeout, follow the genuine release of t,u at zero stake and the mandatory non-s sweep, then label the completed reservation node T. The bounded clipped simulations and prospective L, plus finite release/sweep, give a uniformly computable finite binary decision tree \(\mathcal T_p\). No branch queries a protected value to decide whether it should positively gate. The tree can be completed through zero-stake queries as needed to make the two terminal types a prefix-free complete partition.

Let \(\mathcal G(p)\) be the finite **prefix-free** set of words w of additional output bits ending at first positive gate-decision nodes (not after the s,t,u terminal payoff). For each j set
\[
N_j(p)=|\{w\in\mathcal G(p):|w|=j\}|.
\]
Then the exact identity
\[
\boxed{\gamma(p)=\sum_{w\in\mathcal G(p)}2^{-|w|}
=\sum_{j\ge0}N_j(p)2^{-j}}
\tag{1}
\]
holds. The right-hand sum is finite, dyadic and uniformly computable from the ACTUAL p and controller. Empty \(\mathcal G(p)\) gives gamma(p)=0.

Define the *prospective shortest positive gate-output certificate length*
\[
d(p)=\min\{|w|:w\in\mathcal G(p)\}\in\mathbb N\cup\{\infty\},
\]
with d(p)=infinity when \(\mathcal G(p)\) is empty. This is an exactly computable extended natural number on each valid finite p, including the emptiness case. It counts **fresh controller output bits until an alternative sibling would positively certify**; it is neither the actual-source retrospective M runtime, nor wtt use, nor the number of timeouts, nor a certificate that the ACTUAL sibling gates. Whenever d(p)<infinity,
\[
0<2^{-d(p)}\le\gamma(p)\le1.
\tag{2}
\]
On a true timeout path gamma(p)<1 automatically.

## 2. A quantitative short-gate capacity obstruction on a permanent CR stall

**Theorem 1 (uniform-across-depth necessary capacity law).** Let Z be any computably random RAW source. Assume TRUE T_L reaches some finite epoch start h on Z, then retains the same old s through infinitely many actual completed t/u-release/non-s-sweep timeouts, without one positive gate. Write p_n for the real next-reservation start prefix after n such timeouts, and d_n=d(p_n). Then there exists a **finite source/epoch/controller-dependent** constant C such that, simultaneously for every integer K>=0,
\[
\boxed{\quad
\#\{n\ge0:d_n\le K\}\le C\,2^K,
\qquad
\sum_{n\ge0}2^{-d_n}<\infty.
\quad}
\tag{3}
\]
Here \(2^{-\infty}=0\). In particular \(d_n\to\infty\) in the extended naturals: for every fixed K, only finitely many actual timeout reservations admit any positive-gate sibling with at most K new output bits before its pre-consumption gate decision.

**Proof.** By P4-S066, the single computable timeout hedge at h, transferred through P4-S008's fixed-unread-s permutation completion, is bounded on the computably random source Z. If its bound is A>=1, the finite products satisfy
\[
\sum_{n<N}-\log(1-\gamma(p_n))
=\log\prod_{n<N}(1-\gamma(p_n))^{-1}
\le\log A.
\]
As \(0\le\gamma\le-\log(1-\gamma)\) along genuine timeouts, the nonnegative sum \(\sum_n\gamma(p_n)\) is at most \(\log A\). Equation (2) yields \(\sum_n2^{-d_n}\le\log A\). For every d_n<=K, (2) also gives \(\gamma(p_n)\ge2^{-K}\); hence the number of such n is bounded by \(2^K\sum_n\gamma(p_n)\). Take C=max(1,log A). The same C works for ALL K; no effective source-independent value or computable cutoff is asserted. QED.

**Corollary 2 (finite-tree computable exclusion suppliers).** For the ACTUAL T_L and an actually traced hypothetical infinite timeout sequence, either of the following conditions rules out that sequence on any CR source:
\[
\sum_n2^{-d(p_n)}=\infty,
\tag{4}
\]
or, separately as another sufficient count-based witness, unboundedness over K of
\[
2^{-K}\#\{n:d(p_n)\le K\}.
\tag{5}
\]
The second condition is sufficient, not necessary for (4): in general divergent weighted sums can have uniformly bounded \(2^{-K}\) normalized counts (for example, an abstract depth schedule \(d_n=\lfloor\log_2(n+2)\rfloor\) has this property). Both are **conditional** infinite-history premises; their finite summands/counts are computable from each REAL p_n, but the premises have not been proved for the committed X or its endogenous schedule.

*Proof.* Both contradict (3). No output/RAW martingale pullback beyond the existing fixed-sentinel P4-S008 transfer is used. QED.

**Exact nonconverse.** Merely d_n tending to infinity does NOT imply summable gamma(p_n). An abstract finite decision tree may defer its terminal gate/timeout decision until k future independent bits have been read, and then gate if their first bit is 1. All its gate leaves have length k, so d=k while gamma=1/2. Choosing k=n+2 makes d_n tend to infinity but the formal gamma-series diverge. This is an **abstract finite-tree comparison, NOT a reachable T_L/M/Y/X trajectory or a computably random stalled source**. Gate-leaf *multiplicity*, not only the earliest leaf, controls gamma.

## 3. Exact limitation of transfer from the extensional autoreduction to prospective gate clocks

**Proposition 3 (program-clock padding barrier; alternative witness only).** Let any fixed Y and syntactically self-avoiding globally use-clipped wtt autoreduction M satisfy the settled P4-S011 conditions, and retain the SAME repeated-block H and X=H^{-1}(Y). For every fixed positive integer K one can construct a *different program* \(\widehat M_K\) implementing the SAME partial oracle functional as M, with identical target correctness, same oracle-use bound and syntactic self-avoidance, such that **no ordinary halt of \(\widehat M_K(q)\) occurs within the first K counted machine steps on ANY oracle**. In the otherwise unchanged P4-S057 controller scheme instantiated with \(\widehat M_K\) and legitimate fixed prospective tenure \(L(e,k,p)\equiv K\), every reservation always genuinely times out, its gate set is empty and gamma(p)=0 for every valid p. Every raw source, including the SAME X, then has a permanent fixed old sentinel and genuine repeated zero-stake t/u release and non-s sweeps, with no positive gate.

**Proof.** Add K+1 explicit dummy internal computation steps, with no oracle queries or outputs, to the front of M. Afterward simulate M exactly. This preserves the computed partial functional, all oracle queries, the global computable use clip and avoidance of the input coordinate, and halts correctly on Y at every target input, merely later. On all four paired representative computations the capped simulation of K ordinary steps sees no halt and hence cannot produce an ordinary positive wrong-output or nonbinary certificate. With L=K, every reservation is therefore a REAL timeout on all sibling histories. By the global legality theorem of P4-S057 the prescribed t/u releases and non-s sweeps make the scan total, no-repeat, fair coin and one-hole, while leaving the least unread old s unconsumed forever. Thus \(\mathcal G(p)=\varnothing\), d(p)=infinity and gamma(p)=0 on every valid next-reservation start. QED.

**Scope guard.** This is a precise **representation/time-indexing non-implication**, not a claim that the ACTUALLY COMMITTED program M has been changed, padded, or behaves this way. The committed controller under investigation remains T_L built from the committed M. The proposition proves that *extensional data alone* ("Y computably random; a self-avoiding wtt autoreduction exists and halts correctly on Y; finite uses are clipped; H/X are as given") cannot force nonsummable local next-gate hazards for every legitimate total computable deadline. A successful source-X recurrence proof must establish an additional property of the **particular committed program and chosen prospective L**, including the exact on-scan timing and *weighted quantity of reachable positive gate leaves*. It does not rule out that some more capable computable L succeeds for the committed program.

## 4. Testing the committed source and actual endogenous schedule

For each genuinely reached p_n on X the next fresh q_n comes from the least wholly unread block AFTER all preceding real timeout release/sweep actions; no prechosen computable sequence of q_n is authorized. By P4-S054–P4-S057, after the actual outside-use values are exposed, the true target \(M^Y(q_n)\) eventually halts correctly, and the paired q_n representative logic yields a finite *retrospective* positive certificate at some stage \(\sigma(p_n)>0\). On an actual timeout the only verified numerical comparison is
\[
L(e,k,p_n)<\sigma(p_n)\le T_Y(q_n)<\infty,
\]
where the appropriate post-closure state and real reservation indices are understood as in P4-S057. This supplies neither a positive bounded-decision \(\gamma(p_n)\), nor a computable lower bound \(2^{-d(p_n)}\), nor recurrence of shallow gate leaves. The target's eventual M halt is on the TRUE outside-valuation, whereas (1) measures all finitely explored *counterfactual fresh-output valuations* and requires halts by the prospective L. Finite use closes values, NOT halting times or the count/weight of sibling certificates.

The authoritative P4-S052 shielded-old no-orientation theorem and P4-S053 all-transcript bar prohibition still prevent substituting a semantic trap oracle or retrospective deadlines. P4-S056 compulsory-old-reset slowness is a different controller. P4-S057–P4-S065's budget/spacing/marked/deficit/averaged-hazard results remain conditional on real successes where so stated. None yields (4) or (5) for the committed X on a hypothetical perpetual stall.

**Disposition.** Equations (1)–(3) give an exact auditable finite-tree *short-certificate capacity* restriction for every computably random permanently stalled trajectory; Proposition 3 provides a rigorous clock-representation countermodel to an attempted automatic M^Y-to-gamma lower-bound transfer. No unbounded short-depth count, nonsummable weighted gate-leaf mass, actual X-specific hazard divergence, infinite profitable resets, X in OH, X not in OH, or R_2=OH has been established. This is a narrower mathematical obstruction, NOT a solution to the normalization question.

PA-0001 stays **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 unchanged; Gate 3 PASS; Phase 4 OPEN; Phase 5 CLOSED; Gate 4 NOT REVIEWED. No novelty, openness, prior-art, publication or outreach claim.

**Next bounded target P4-S068 (no owner/external blocker):** examine whether the exact committed M program and the true source-X fresh-block sequence force any recurrence or weighted lower bound for \(\mathcal G(p_n)\) that breaks (3), or whether the actual four-run use/timeout geometry admits a further demonstrable certificate-multiplicity/timing obstruction. Do not infer recurrence from padded alternative programs, potential sibling leaves, stage-unbounded M^Y halts, finite c_n averages, abstract Pi^0_2 membership or retrospective clocks.
