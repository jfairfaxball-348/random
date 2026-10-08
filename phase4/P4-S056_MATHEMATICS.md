# P4-S056 — four-run minimum-clock anti-promptness under compulsory old reset

Date: 2026-10-08
Session: P4-S056
Incoming authoritative main: 727d31976c7bb69f91f06040e2751549ec1382f7
Scope: Phase 4 Mathematics only; selected CAND-01; source-specific minimum-clock thickness versus total pre-consumption protection.

**Outcome.** For EVERY total computable finite positive tenure policy, the canonical **compulsory-old-reset** four-run cube controller has only finitely many timely positive cube exits on the committed X. Consequently, along its infinitely many actual source-derived value-closed epochs, the four-run minimum clock is eventually STRICTLY GREATER than the policy's tenure, yet finite and at most T_Y at each selected fresh target. Unlike P4-S055's success-gated final-sentinel obstruction, this is UNCONDITIONAL on X in OH: it follows from X in CR and from compulsory old consumption making the scan an effective isomorphism. It does not apply to success-gated retention of the old sentinel and does not settle X in OH or R_2=OH.

## 0. Authority and frozen mathematics

Incoming GitHub main matched exactly the P4-S055 outgoing commit above; the three P4-S056 records were absent. Read P4-S001–P4-S055 mathematics, the selected CAND-01 authority, the post-S031 research pivot and later records, emphasizing P4-S008, P4-S011, P4-S012, P4-S027, P4-S033, P4-S039, P4-S041 and P4-S044–P4-S055. All mathematics through P4-S055 is retained, especially the P4-S008 permanent-hole guard, P4-S052 shielded-old restriction and P4-S053 all-transcript reset bar.

Retain the computably random Y, syntactically q-avoiding globally use-clipped wtt autoreduction M, its total computable strict use cap U(q), the repeated three-bit computable fair-coin homeomorphism H, and X=H^{-1}(Y) in CR. H(X)=Y is not in OH. Retain exactly

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Both X in OH and R_2=OH remain unresolved. PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged.

## 1. An exact compulsory-reset clock controller

Fix any TOTAL computable positive integer policy L(e,p), where e is the epoch count and p is the complete finite value-closed observed history. Its value can depend on observed source bits, prior clock outcomes and the fresh q. L cannot depend on unseen bits or on whether M diverges. Define S_L on EVERY raw input as follows.

At epoch e, let R be the finite set of already queried raw coordinates with their bits, and let s=min(N\R) be the old sentinel. Choose the LEAST b with the whole block B_b={3b,3b+1,3b+2} disjoint from R AND from the block containing s. This search halts because R is finite. Put t=3b, u=3b+1, v=3b+2, q=3b, and V(q)=3 ceil(U(q)/3).

1. Protect s,t,u against reading. Query v at zero stake, followed in increasing order by every still-unread raw r<V(q) other than s,t,u, also at zero stake. Reuse already read bits and query nothing twice. This finite value-closure stage leaves a finite p from which all capped virtual M(q) oracle-answer tables on the eight synthetic (s,t,u) cubes are computable. All three protected bits remain genuinely unread. If s is outside the cap, the relevant synthetic traces simply do not use it.
2. Compute L=L(e,p)>=1. For r=1,...,L, synchronously simulate each of the FOUR representative capped M(q) computations for r ordinary M steps, using the finite tables for (s,t,u)=(a,0,c), with a,c in {0,1}. Clip violations/divergence are not positive halts. The simulations may equivalently be run once for L steps; they are BOUNDED even on every off-target transcript. Choose the first ordinary halt using least (r,a,c) lexicographic tie breaking. No further raw bit is consumed during the finite calculation.
3. On a positive ordinary halt, calculate a certified forbidden corner by pairing the halting representative (a,0,c) with (a,1,1-c). These synthetic virtual inputs differ only at the never-queried virtual q; the M traces and outputs are identical, while their expected q values are opposite. More explicitly the representative's q-bit equals X(v), known from closure; if the binary output equals X(v), choose the mate, otherwise the representative. A nonbinary output may choose the representative. Only a genuinely halted wrong/nonbinary corner is used; timeouts, clipped abandonments and divergence never count.
4. For a positive event with forbidden corner (a,beta,gamma), place the exact fair conditional-expectation 8/7 hedge on the NEXT THREE raw queries s,t,u in that order. If no positive halt appears by r=L, query s,t,u IN THAT ORDER at ZERO stake. In EITHER case consume the old sentinel and both temporary future bits in finitely many output steps, and start epoch e+1.

No filler output inside the bounded computation is required: a total computable no-repeat scan may do any finite computation before its next query. Both the closure and the L-round calculation terminate on EVERY finite transcript. Every epoch consumes at least s,t,u and uses only fresh bits. This differs deliberately from the P4-S055 success-gated controller, which retains s on a failed temporary reservation.

## 2. Exact fair capital and global effective-isomorphism check

Starting capital C>=0, a positive forbidden triple has terminal payoff 0 on that triple and 8C/7 on each of the other seven triples. The sequential fair ledger is:

- Query s: capitals 6C/7 at s=a, 8C/7 at s!=a.
- If s=a, query t: capitals 4C/7 at t=beta, 8C/7 at t!=beta. If s!=a, both t-children are 8C/7.
- If s=a,t=beta, query u: capitals 0 at u=gamma, 8C/7 at u!=gamma. Else both u-children are 8C/7.

Every parent is exactly the mean of its two children. A timeout makes all three child pairs equal to the current capital. The conditional fair ledger is computable, rational, nonnegative and valid even on off-X inputs whose true triple is the forbidden one; correctness on those inputs is NOT assumed.

**Lemma 1 (global isomorphism).** S_L is an everywhere-total computable no-repeat adaptive scan preserving fair coin. It queries EVERY input coordinate on EVERY binary input; it has a total computable inverse from output transcripts and consequently is a computable fair-coin-preserving homeomorphism (all fibres are singleton, hence in particular global k<=2).

**Proof.** Each epoch lasts finitely many raw queries and terminates after consuming its least unread s. If some raw coordinate n were never queried, the least unread sentinel would remain <=n, contrary to strictly increasing sentinel indices across infinitely many terminating epochs. There are infinitely many epochs because a finite input history always leaves whole unqueried blocks. At each output step the query index is computed from the already emitted bits, so every output cylinder has fair preimage measure 2^{-length}. To invert, replay the deterministic scan on an arbitrary output y, assigning y's next bit to its next computed queried raw coordinate. To recover coordinate n, replay until it is queried, which happens after finitely many epochs on EVERY y. The inverse is total and computable, while both directions are continuous. QED.

This is the concrete four-run instance of the P4-S053 all-transcript-reset bar. The proof does NOT claim the success-gated controller is a computable isomorphism: its final old s may remain unread on a sibling continuation.

## 3. Unconditional slow-clock escape along EVERY compulsory-reset tenure

Let p_e be the value-closed history reached at the e-th epoch when S_L runs on committed X, and q_e the selected fresh virtual target. Let sigma(p) be the P4-S055 four-run MINIMUM ordinary-halting clock, and T_Y(q) the true target computation runtime.

**Theorem 2 (actual-source compulsory-reset anti-promptness).** For EVERY total computable positive policy L(e,p),

\[
\boxed{\quad\exists e_0\ \forall e\ge e_0:\quad
L(e,p_e)<\sigma(p_e)\le T_Y(q_e)<\infty.\quad}
\]

The indices q_e are pairwise distinct and tend to infinity. In particular, for EVERY total computable b:N->N, the choice L(e,p)=max(1,b(q)) gives an unconditional policy-dependent actual-source tail

\[
\forall^\infty e\quad \max(1,b(q_e))<\sigma(p_e)\le T_Y(q_e).
\]

Neither the map e->q_e nor the sequence of p_e is claimed computable WITHOUT access to X, and the schedule generally changes when L changes.

**Proof.** Each p_e comes from X and is genuinely value-closed with fresh t,u and old s in another block. By P4-S054/P4-S055, the actual target computation M^Y(q_e) halts, and its companion obtained by jointly flipping t,u finitely refutes a cube corner. Thus 0<sigma(p_e)<=T_Y(q_e)<infinity. Lemma 1 makes S_L(X) computably random by the retained computable-isomorphism preservation theorem for computable randomness (P4-S001 / SRC-0015 / THM-0038). If sigma(p_e)<=L(e,p_e) at infinitely many epochs, the four-run controller positively detects and EXECUTES a hedge at each such epoch. On X its selected wrong corner cannot equal the actual s,t,u triple, because M^Y(q_e) halts CORRECTLY on Y and all synthetic use answers agree with genuinely exposed bits. Its terminal capital therefore multiplies by 8/7 on each such epoch, and remains unchanged on timeout and zero-stake closure. The one total computable rational fair martingale would become unbounded on S_L(X), a contradiction. Hence only finitely many sigma<=L events occur; all subsequent epochs satisfy the displayed STRICT inequality. Each used B_b was entirely unread when chosen and then consumed, so no q_e repeats; infinitely many distinct natural numbers go to infinity. QED.

**Key quantifier distinction.** This is a theorem about a family of TRANSCRIPT-ADAPTIVE schedules, with each schedule selected by its own computable L and always releasing the old sentinel. It does NOT assert that sigma is hyperimmune on a fixed computable list of q, that a fixed source-independent p sequence exists, or that there is a uniform effective e_0. Its conclusion is stronger than P4-S055's conditional latency conclusion in the removal of the hypothesis X in OH, but narrower in the compulsory-reset geometry.

## 4. Exact boundary for potential thickness

For a fixed legal finite state (R,s) and proposed entirely unread block b, let F be the finite set of outside raw coordinates which value closure would inspect (v and all as-yet-unread r<V(q) except s,t,u). The previously observed bits are fixed. For each assignment eta in {0,1}^F, form the resulting finite value-closed p_eta. For integer r>=1 define

\[
{\rm BAR}_{R,s,b}(r)\iff
\forall\eta\in 2^F\;\exists a,c\in\{0,1\}:
M^{H(p_\eta,a,0,c)}(q)\hbox{ halts ordinarily by step }r.
\]

This is a FINITE DECIDABLE statement for fixed r,R,s,b (all simulations are clipped). A true BAR supplies a uniform positive certificate deadline before any of s,t,u is read, irrespective of all as-yet-unseen closure bits. The existential condition \(\exists r\,{\rm BAR}_{R,s,b}(r)\) is c.e., not generally decidable. A controller may exploit an actually COMPUTABLY DELIVERED valid (b,r), but cannot wait unboundedly for a certificate without breaking global next-output totality.

**Corollary 3 (no total everywhere-renewable certified bar selector).** There is NO total computable procedure which, for every finite state reached on the actual X by its resulting compulsory-reset controller, supplies a legally wholly-unread b and verified finite r satisfying BAR before protecting s,t,u, while also being a globally total scan policy on sibling histories. Otherwise take that b and r each epoch, perform the finite value closure, verify the supplied bar, and execute the above compulsory-old-reset hedge. The bar forces sigma<=r on X EVERY epoch, contradicting Theorem 2. This does not exclude a c.e. sparse set of bars, a nonuniform source-dependent supply, or bars encountered after the selected block has already been consumed.

For clarity, the all-valuation BAR is a stronger, finitely checkable *sufficient* witness than the single actual-state condition sigma(p)<=L; it is NOT asserted necessary for capture. Nor does finite wtt use force BAR: value closure bounds ANSWERS, not M's HALTING TIME. No frequency, density, cofinite BAR reservoir or total computable renewable selector is established for the committed M.

## 5. Relation to the unresolved success-gated source problem

Three separate effectivity levels remain:

1. **Eventual source halt.** Every actual X-derived p has finite four-run sigma, bounded by the Y-oracle computable T_Y(q); this is not a usable pre-consumption deadline.
2. **Total computable pre-consumption tenure.** L(e,p) halts on ALL finite p; the compulsory-reset scan is everywhere total, while the success-gated scan additionally preserves old s upon a miss and is merely globally one-hole.
3. **Executed gains.** Only an actual positive halt before consumption followed by the fair s,t,u wager multiplies capital by 8/7 on X. Passive late halts and counterfactual retrospective bets are not gains.

Theorem 2 says compulsory reset *forces* eventual misses on X for every computable tenure, because infinitely many completed gains would contradict CR of X under a computable isomorphism. Under the P4-S055 success-gated controller, timeout releases only t,u, preserving the old s: the no-reset sibling branch destroys the effective-isomorphism argument. P4-S055's final-sentinel slow-clock escape therefore still requires the HYPOTHESIS X in OH. P4-S008 prohibits infinite profits while a fixed s is permanently omitted; P4-S052 continues to prohibit the shielded-old orientations; P4-S053 prohibits disguising an all-continuation reset bar as a genuinely partial policy.

**Stopping point.** Established an unconditional actual-source policy-relative eventual-slow-minimum law for EVERY computable compulsory-reset clock, a legal exact finite controller and a finite all-valuation BAR test with an explicit total-selector obstruction. No source-specific frequently prompt success-gated schedule, infinitely many executed success-gated turnovers, X in OH, X not in OH, R_2=OH or OH non-invariance is established. No change to PA-0001, DEF-0020, Gate 4 or Phase 5; no novelty, openness, prior-art, publication or outreach determination.

**Next P4-S057 target.** Find an operational separator between this forced-reset anti-promptness theorem and the success-gated one-hole process: either an effectively checkable *branchwise-avoidable* minimum-clock thickness criterion sufficient for infinitely many actual renewed 8/7 turnovers, or a further actual-source restriction that remains valid WITHOUT compulsory old reset. Require full freshness, bounded timeouts and exact fair capital, with no semantic trap detector.
