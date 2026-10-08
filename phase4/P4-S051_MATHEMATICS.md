# P4-S051 — reset-free cross-row escrow and the fixed-sentinel limit

Date: 2026-10-08
Session: P4-S051
Incoming checkpoint: 96bfc1d1cfb351e14eb874202ff1858b0e0709aa
Scope: Phase 4 — Mathematics; one-hole normalization after coded recoding

Result: **TWO POSITIVE SQUARE REFUTATIONS AGAINST OPPOSITE VALUES OF THE SAME UNREAD OLD SENTINEL, AT TWO DIFFERENT FRESH TARGETS, EXCLUDE A JOINT FUTURE-TARGET ATOM. AN EXACT FAIR 4/3 TWO-TARGET HEDGE CAN THEN CONSUME THE TWO FUTURE COORDINATES WITHOUT READING OR RESETTING THE OLD SENTINEL. A FINITELY PROTECTED MULTI-SQUARE ESCROW CONTROLLER IS EVERYWHERE TOTAL, NO-REPEAT, FAIR-COIN PRESERVING AND GLOBALLY AT MOST ONE-HOLE. SAME-TARGET OPPOSITE-ROW REFUTATIONS GIVE A 2X ONE-TARGET HEDGE; A CONSUMED TARGET THAT MATCHES ITS REFUTED VALUE CAN INSTEAD POSITIVELY ORIENT THE OLD SENTINEL. THE NEW RESET-FREE HEDGE IS SHARP AS FINITE INFORMATION, BUT P4-S008 IMPLIES THAT NO COMPUTABLY RANDOM SOURCE CAN SUPPORT INFINITELY MANY PROFITABLE RESET-FREE ESCROW HEDGES WHILE ONE FIXED SENTINEL STAYS OMITTED. TO OBTAIN A SAME-SOURCE ONE-HOLE DESTROYER ONE STILL NEEDS AN EFFECTIVE POLICY MAKING INFINITELY MANY PROFITABLE EXITS ACROSS SENTINEL TURNOVERS; THIS IS NOT PROVED FOR THE COMMITTED X.**

## 0. Authority, uniqueness and retained target

At the start, remote main matched exactly the P4-S050 outgoing checkpoint 96bfc1d1cfb351e14eb874202ff1858b0e0709aa by a GitHub compare returning identical (zero ahead/behind). P4-S051 mathematics did not exist. Read the P4-S001–P4-S050 mathematics records, the required P2-S001/P2-S003/candidates.json and P3-S008 CAND-01 authority, the post-S031 pivot and, especially, P4-S011, P4-S012, P4-S027, P4-S041 and P4-S044–P4-S050. Preserve all previously validated mathematics.

Use the committed P4-S011 computably random source Y and syntactically self-avoiding globally use-clipped wtt autoreduction M, the P4-S033 repeated-block computable fair-coin homeomorphism H, and X=H^{-1}(Y). Retain X in CR, H(X)=Y not in OH, with X in OH unresolved. Retain precisely
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]
A positive square refutation Ref_{s,t}(a,beta) is a finite wrong/nonbinary halt of M on the recoded counterfactual raw source with s=a,t=beta and other raw coordinates as observed. Such a refutation excludes only that raw pair, with no requirement that the current old s be semantically trapped. Absence of a halt is never evidence.

## 1. The three geometries and exact finite-information calculation

Fix a still-unread old coordinate s. Distinguish:
1. At a *semantically* trapped old epoch (P4-S049), any finite refutation is in the wrong future column and hence predicts the future target bit. Recognizing the trap is not a total computable operation.
2. At an arbitrary old epoch, P4-S050 converts one forbidden pair into a guaranteed factor 4/3 by reading both s and t. This resets the old sentinel.
3. Finite positive information can sometimes be combined *across distinct fresh targets* to exclude a target-only tuple. This is the new reset-free route.

**Lemma 1 (two squares, opposite old rows).** Let s,t,u be three pairwise distinct unread raw coordinates, with t and u in fresh recoding blocks different from the old block and one another. Suppose finite positive computations, while all three remain unread, establish
\[
\mathrm{Ref}_{s,t}(a,\beta),\qquad
\mathrm{Ref}_{s,u}(1-a,\gamma).
\]
Then on the committed X,
\[
(X(t),X(u))\ne(\beta,\gamma).
\]
This conclusion does not depend on X(s), old-epoch trap status or knowledge of either actual raw bit.

**Proof.** If t=beta and u=gamma, the first sound exclusion forces s ne a, hence s=1-a; the second forces s ne 1-a, a contradiction. Both exclusions are valid relative to the actual outside-square raw transcript by P4-S050 Lemma 1. No simulation is treated as halted merely because its time budget expires. ∎

**Theorem 2 (exact reset-free two-target hedge).** Under Lemma 1, from capital C>0 query t with capital 2C/3 on t=beta and 4C/3 on t=1-beta. If t=beta, query u with capital zero on u=gamma and 4C/3 on u=1-gamma. If t=1-beta, query u at zero stake. The terminal payoff is zero on (beta,gamma) and 4C/3 on each other pair. The actual payoff is 4C/3, and s remains unread.

**Proof.** Each step is a nonnegative rational fair wager: (2/3+4/3)/2=1 and (0+4/3)/2=2/3. The terminal payoff averages C over the four unbiased pairs; Lemma 1 excludes the sole zero atom on X. At the moment of each wager the required coordinate is still unread. No wager uses the actual old value as a program parameter. ∎

**Lemma 3 (same-target and after-consumption rules).**
(a) If Ref_{s,t}(0,beta) and Ref_{s,t}(1,beta) are both positively visible before t is read, t=1-beta. A fair all-in t wager doubles capital while leaving s untouched.
(b) If Ref_{s,t}(a,0) and Ref_{s,t}(a,1) are both visible, then s=1-a. This gives a fair doubled *s* wager only if s is subsequently read; it does not force any value of t.
(c) If Ref_{s,t}(a,beta) is positively certified before or after t is read, and t has since been observed equal to beta, then s=1-a is positively determined. The subsequent correct all-in s bet doubles capital but resets the old sentinel. If observed t=1-beta, the single refutation does not orient s.
(d) If the situation in (c) has oriented s=1-a, and a positive Ref_{s,u}(1-a,gamma) appears before fresh u is read, then u=1-gamma; an all-in u wager doubles capital leaving s unread. By contrast Ref_{s,u}(a,gamma) adds no prospective constraint on u under this orientation.

**Proof.** In (a), both possibilities for the old bit have been excluded at target beta. In (b), both possibilities for t have been excluded at old a. In (c), substituting the actually observed t into the finite pair exclusion rules out old a exactly in the matching case. In (d), substitute the now-known old value in the second finite pair exclusion. Every all-in wager is the ordinary fair child-capital pair (2C,0), ordered according to the positively forced fresh bit. ∎

The second witness need not be available at the time of the first. However, a second witness found *after u is already consumed* cannot retroactively justify a wager on u. Equally, a refutation involving first target t discovered only *after t is consumed* is not an executable two-target hedge. P4-S044's wtt value horizon supplies no certificate-arrival bound.

## 2. Sharpness: exactly which finite exclusions change the projection

For a common old bit s and distinct future bits t_1,...,t_m, let E_i be the set of positively refuted old/future atoms at target t_i; assume soundness on X. On any candidate future tuple v=(v_1,...,v_m), the old values compatible with all certificates are
\[
A(v)=\{a\in\{0,1\}:\ (a,v_i)\notin E_i\ \text{for every }i\}.
\]
The finite positive data exclude v exactly when A(v) is empty. All surviving tuples have at least one old-bit completion.

**Proposition 4 (exact finite projection criterion).** A nonnegative fair terminal strategy that wagers only on the finitely many targets (not s), and guarantees a strict terminal gain on *every* tuple consistent with the certificates, exists exactly when at least one future tuple is excluded by the positive constraints. If r out of the 2^m target tuples are excluded, the exact flat payoff
\[
G(v)=\frac{2^m}{2^m-r}\mathbf 1[A(v)\ne\varnothing]
\]
is computable from the finite certificates and sequentially implementable in any prescribed order of fresh targets by taking successive fair conditional expectations. Here 1<=r<2^m (the latter strict inequality follows from soundness and the existence of the actual tuple).

**Proof.** If every tuple survives, any fair terminal payoff averaged over all 2^m unbiased tuples is C; it cannot exceed C at each tuple. If some tuples are ruled out, the displayed nonnegative payoff has uniform mean one, is strictly above one at all surviving tuples, and the usual binary conditional expectations implement it fairly before each queried coordinate. ∎

Consequences:
- A lone refuted atom (a,beta) leaves every target value possible through old row 1-a; it cannot force reset-free guaranteed gain on t.
- Refutations confined entirely to one old row cannot exclude any future tuple, because the other old row satisfies all of them.
- Opposite old rows at **one** fresh target with the same future value exclude that target value and give factor 2.
- Opposite old rows at **two distinct** fresh targets exclude at least one joint two-target tuple and give factor 4/3 in the minimal one-atom case (Lemma 1).
- Two diagonal exclusions at the *same* future target, (0,0) and (1,1), leave both possible t values, so no guaranteed t-only gain (though the pair can support a two-bit hedge consuming s).
- Across multiple fresh targets, any asserted amplification must be proved by A(v)=empty for some target tuple. Mere repeated certificates in one old row do not suffice.

This is an information-theoretic sharpness result for the concrete certificate language. It does not assert that arbitrary abstract certificate patterns are realized cofinally on the committed X.

## 3. Explicit computable finite-window multi-square escrow controller

Define S_esc as a total adaptive no-repeat raw scan, with a computable rational fair output martingale. Its input is an arbitrary infinite raw source; its code contains M,H and a fixed computable raw coordinate order, but neither the actual source bits nor a trap oracle.

At the beginning of an epoch select s as the least unread raw coordinate and keep it withheld. Select t as the least unread coordinate in a different recoding block. Start an initial reservation of exactly L(e,k)=2^{e+k+3} ordinary output rounds (epoch number e, reservation number k). The global simulation round counter N grows without bound and is never reset.

In each round do a finite first-N-input/first-N-step symmetric simulation of the four Ref_{s,t} corners. Answer s,t synthetically, reuse recorded outside answers, and put outstanding real outside support requests on a computable queue. Never query s,t as support. Alternate one zero-stake least-pending support query (falling back to least-unread sweep) with one zero-stake least-unread nonprotected sweep query. After each finite simulation slice, before the next real query, check positive events in fixed order.

- If two positive same-target opposite-row exclusions share future value beta, perform Lemma 3(a), query t with the correct all-in wager, keep s, and begin another reservation.
- If a first positive square certificate Ref_{s,t}(a,beta) appears while t,s are unread, retain that actual finite witness and enter an escrow closure window; do *not* yet wager. Choose a new unread u in a block distinct from those of s,t. Protect s,t,u for exactly K(e,k)=2^{e+k+4} ordinary output rounds, still sweeping and answering finite support requests outside the protected triple.
- During closure, dovetail the four Ref_{s,u} corners symmetrically, *suspending* rather than answering any oracle request for protected t. If a visible Ref_{s,u}(1-a,gamma) arrives before t or u has been queried, execute Theorem 2 in t-then-u order. Consume only t,u, retain s, and begin the next reservation. If a same-target opposite-row column refutation for t arrives, execute Lemma 3(a), consume t and release u at zero stake.
- If a finite old-one-bit completion refutation appears while s unread, it may be given priority under a fixed deterministic rule: bet all-in on the complementary s value, consume s, release any protected future targets at zero stake and begin a new epoch. An alternatively certified oriented s from Lemma 3(c) can be closed the same way. Such an exit is a **reset**, not reset-free escrow.
- If an initial reservation times out with no event, consume t at zero stake, retain s and start another reservation. If the finite escrow window times out, consume t and u at zero stake, retain s, and start another reservation; after t is observed, the controller may optionally apply Lemma 3(c) and reset s only if the matching observed value positively orients it. No missing halt is used.

All choices (including event priority and finite windows) are fixed and computable from the observed transcript. Every ordinary round performs finite bounded computation before emitting one fresh output; hedge and timeout steps emit real output immediately in finite additional work. If a support request concerns a protected coordinate, it is suspended until that coordinate is released, never answered speculatively.

**Theorem 5 (global legality).** S_esc is everywhere total, computable, adaptive and no-repeat. Every infinite transcript omits at most one raw coordinate, even though its finite escrow window may momentarily protect three. It preserves fair coin, and all its fibres have size at most two.

**Proof.** Each protected future target is released by a fixed finite timeout or positive exit. In every nonexit epoch, repeated reservations and the mandatory least-unread background sweep eventually consume every raw coordinate other than s; no protected future target is permanently withheld. Whenever the old sentinel is reset, it is consumed, and next epoch uses the least unread raw coordinate. If old sentinels reset infinitely often, every fixed raw coordinate is eventually queried. If they reset finitely often, every raw coordinate except the final s is eventually queried. Thus at most one coordinate can remain omitted on any infinite transcript. At each output stage the next unqueried coordinate is a computable function of preceding output bits, so every length-m output cylinder fixes m independent fair bits and has measure 2^{-m}. The fibre cardinal bound follows from the at-most-one omitted coordinate. All queries are fresh. ∎

A controller variant S_esc+ can use P4-S050's immediate two-bit hedge on a first certificate instead of opening escrow, or can search for either event using a fixed effective time-sharing schedule. This can improve the chance of profitable exits along a particular source, but no source-specific universal capture theorem is inferred.

## 4. Success criteria and the hidden fixed-sentinel limit

Each *completed* opposed-row two-target escrow hedge has terminal factor 4/3, each positively oriented one-target hedge has factor 2, and any old-sentinel wager justified by a positive finite refutation has factor 2. All other output queries have multiplier one; inside a completed two-target hedge the first stage may dip to 2/3. These statements are about the actual committed source X; martingale fairness itself holds on all output paths.

**Theorem 6 (algorithm-relative infinite-exit criterion).** If one fixed computable S_esc+ controller executes infinitely many completed positive hedge exits on X, including reset-free escrows and/or positive old-sentinel resets, its output martingale succeeds and X is not in OH. The scan is globally one-hole safe by Theorem 5.

**Proof.** At every completed profitable exit, actual capital is multiplied by at least 4/3, while completed non-event intervals multiply by one. Infinitely many such exits force unbounded capital along the scan output; the intermediate temporary drawdown is harmless. The program and output martingale are fixed total computable objects. ∎

**Theorem 7 (no infinite fixed-sentinel escrow success on a computably random source).** Let x be computably random. No fixed total computable globally one-hole-safe scan can earn unbounded computable output-martingale capital while leaving a *fixed* coordinate s unqueried forever along x. In particular S_esc cannot execute infinitely many successful reset-free opposed-row escrows on committed X during a single never-reset epoch.

**Proof.** This is exactly the P4-S008 fixed-sentinel permutation-completion theorem: prepend a zero-stake query of the omitted fixed coordinate s, then simulate the scan on other fresh coordinates until it asks for s (if ever), with the standard total computable no-repeat exhaustive completion. A winning output martingale would transfer to a computable source martingale and contradict x in CR. If the final epoch never resets s and executes infinitely many 4/3 gains, its output martingale wins while s is persistently omitted, contradicting that theorem. ∎

Thus the new reset-free hedge is a valid *finite* improvement but cannot by itself produce infinite success while one permanent old hole is held on a computably random source. The desired same-source destruction still requires infinitely many effective old-sentinel turnovers, possibly each preceded by finitely many escrow gains. Merely increasing finite windows, denser dovetailing, or positing infinitely many semantic A blocks does not establish these turnovers.

**Corollary 8 (exact hypothetical OH obstruction).** If X in OH, then for each fixed computable globally legal combined escrow/reset policy there are only finitely many positive completed exits along X. In the final never-reset epoch a persistent old sentinel remains, finite old-branch refutations must eventually be absent under an exhaustive old-branch dovetail, and there cannot be infinitely many timely executable opposed-row escrow closures (indeed, that last fact already follows from X in CR by Theorem 7). This is policy-relative: it does not exclude later finite certificates which emerge after some protected coordinate was consumed, does not bound certificate times uniformly, and does not establish X in OH.

## 5. Exact remaining boundary and next target

What is proved: a sound opposite-old-row cross-target projection rule; exact fair reset-free 4/3 hedge; a sharp finite projection criterion for m target bits; positive after-consumption orientation; explicit bounded-window globally one-hole-safe multi-square controller; conditional infinite-exit destruction; and the stronger P4-S008 constraint that infinitely many reset-free successes at a single permanently withheld old sentinel cannot occur on the known CR source.

What is not proved: opposite-row certificates appearing with both targets fresh infinitely often on committed X; a computable effective trap oracle; an infinite sequence of positive old-sentinel turnovers; X in OH, X not in OH, R_2=OH or its negation.

Natural P4-S052 bounded question: can a *finite* opposed-row escrow payoff be coupled to a **computably certified old-sentinel turnover** and iterated infinitely on the committed X, rather than holding a known CR source at one permanent hole? Distinguish certificate-time conditions for t,u from finite positive information orienting s, and explicitly account for the P4-S008 fixed-sentinel obstruction. Do not return to earlier ticket/frontier, backward-price or generic compiler routes.

PA-0001 stays UNRESOLVED_UNDER_INSPECTED_EVIDENCE. DEF-0020 unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim. Phase 4 OPEN; Phase 5 CLOSED.
