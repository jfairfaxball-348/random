# P4-S057 — success-gated four-run renewal: the unbounded-miss-budget obstruction

Date: 2026-10-08
Session: P4-S057
Incoming authoritative main: 142104e6f727c3986872a0413c925e9fc5bb9009
Scope: Phase 4 — Mathematics, selected CAND-01; genuine success-gated four-run renewal only.

**Outcome.** An unconditional *necessary* actual-source law survives retaining the old sentinel on every timeout. For each fixed total computable success-gated four-run controller on the committed computably random X, either it executes only finitely many profitable old resets, **or**, if it executes infinitely many, then the number of fully failed, mandatory t/u-release reservations before the next positive old reset exceeds **every total computable epoch-start budget infinitely often**. This is not P4-S056's false extension of compulsory-reset eventual minimum-clock slowness. The proof uses a finite-prefix, bounded-renewal compulsory-reset *shadow* only for contradiction, never changes the true controller's timeout rule. It establishes neither alternative for X, and in particular neither X in OH nor R_2=OH.

## 0. Authority and frozen guards

GitHub main was independently pinned to the specified P4-S056 outgoing commit. The P4-S057 mathematics/validation/close files were absent. Reviewed P4-S001–P4-S056, CAND-01 selection and Gate-3 authority, the post-S031 research pivot and all later mathematics; especially P4-S008, P4-S011, P4-S012, P4-S027, P4-S033, P4-S039, P4-S041, P4-S044–P4-S056. Preserve all earlier mathematical statements unchanged.

Retain the computably random wtt-autoreducible Y; syntactically q-avoiding, globally use-clipped partial M with computable strict cap U(q); the fair-coin computable homeomorphism H repeated on blocks of length three; and X=H^{-1}(Y) in CR, with H(X)=Y not in OH. Retain exactly
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]
X in OH and R_2=OH remain unresolved. P4-S008 disallows success on a computably random source with one permanently omitted fixed hole; P4-S052 blocks old orientation from shielded actual-future columns; P4-S053 supplies the all-continuation reset-bar/isomorphism guard. None is weakened.

## 1. Fully explicit *success-gated* scan and its first finite event

Fix ANY total computable integer tenure L(e,k,p)>=1, where e counts consumed old sentinels (successful epochs), k counts temporary reservations within the current epoch, and p is the complete already observed finite *value-closed* state. The tenure is computed before any of the protected coordinates is consumed. No dependence on the actual Y-oracle runtime, on a future bit, or on a retrospective halting certificate is allowed.

At an epoch start R is the finite table of queried raw indices and values, and s=min(N\R) is the unread old sentinel. On reservation k choose the least b such that the ENTIRE raw block B_b={3b,3b+1,3b+2} is unread and is not the block containing s. Set t=3b,u=3b+1,v=3b+2,q=3b. Keep s,t,u unread. Query v at zero stake; then query all still-unread raw r<V(q)=3 ceil(U(q)/3), r not in {s,t,u}, in increasing order at zero stake. This is genuine finite *value closure*, using previously read raw values without querying them again.

For each (a,c) in {0,1}^2 synthesize (s,t,u)=(a,0,c) with the observed outside bits. Simulate the FOUR globally clipped M(q) traces for ordinary machine steps r=1,...,L(e,k,p), with a fixed least-(r,a,c) tie rule. The two configurations (a,0,c) and (a,1,1-c) differ only at virtual q, never queried by the syntactically self-avoiding M(q); they have exactly the same capped trace, and opposite expected q-bit. Since virtual q on a representative is v, a binary halt z rules out the representative if z!=X(v) and otherwise rules out its mate; a nonbinary halt rules out the representative. Only an ordinary positive wrong/nonbinary halt counts, never clipping, timeout, or divergence. Its forbidden raw cube atom (a,beta,gamma) is mechanically checkable from the finite trace and observed p.

Before each of the L finite simulation rounds the controller may emit one zero-stake least-index unread nonprotected filler bit; thus no unbounded computation is required between successive output bits. On a positive halt, **immediately query s,t,u in order with the exact fair 8/7 three-bit hedge**, consume s, and start epoch e+1 with the next least-unread s. On a timeout, **query t then u at zero stake, retain s unread**, and increment k. After every timeout additionally query one least-index currently unread raw coordinate different from s at zero stake as a deterministic sweep; this makes the global one-hole proof independent of any growth assumption on U(q). Then begin the next reservation. The sweep is legal after t,u release and never consumes s. No future t/u can be protected indefinitely.

Denote this exact controller by T_L. If its reservation after closure has state p, then on X
\[
\text{positive executed turnover}\quad\Longleftrightarrow\quad
0<\sigma(p)=\rho(p)\le L(e,k,p),
\]
and each timeout is precisely L(e,k,p)<sigma(p)<=T_Y(q)<infinity on X. The last inequality is the retained P4-S055 source certificate law; q changes with the ACTUAL transcript and is not a computable fixed target list.

## 2. Totality, one-hole fibres, and exact rational capital

**Lemma 1 (global legality).** T_L is an everywhere-total computable adaptive no-repeat fair-coin-preserving scan. Every infinite output transcript queries all source positions or omits exactly one; in particular every fibre has size at most two. Its accompanying computable nonnegative rational martingale is exactly fair on *every* source.

**Proof.** Each value closure, each L-step trace search, each bounded filler action and every terminal s,t,u or t,u release is finite. There is always an entirely unread raw block outside the old block and a least nonprotected filler. Every raw coordinate is queried at most once. If infinitely many successful epochs occur, each consumes the least unread s, so all source coordinates are eventually queried. Otherwise, after the last successful epoch, indefinitely many finite timeout reservations occur with the same least-unread s. Their mandated t,u release plus the least-unread non-s sweep consume every other raw position: any fixed n!=s eventually becomes the least eligible unqueried position and is swept or queried earlier in closure. Hence at most s is omitted, *on every sibling transcript*. Fresh fair-coin bits give each output cylinder preimage measure 2^{-length}; the standard omitted-coordinate fibre calculation gives cardinality 1 or 2. QED.

For completeness the exact positive capital ledger from initial capital C is:
- On s=a: 6C/7; on s!=a: 8C/7.
- On s=a,t=beta: 4C/7; on s=a,t!=beta: 8C/7; if s!=a, both t-children remain 8C/7.
- On s=a,t=beta,u=gamma: 0; on s=a,t=beta,u!=gamma: 8C/7; all other u-children remain 8C/7.

The parent is the arithmetic mean of its two children at EVERY node: (6+8)/14=1, (4+8)/14=6/7 and (0+8)/14=4/7. The terminal table is (0,8C/7,...,8C/7). On X the actual triple cannot be a positively excluded corner, so capital after a positive exit is 8C/7. At timeout and during value closure/fillers/sweep all children equal current capital. No P4-S052 shielded-old orientation, old all-in stake, or 8/3 cash-out is being invoked.

## 3. The renewal count is prospectively observable, not an oracle

For an actual X-run of T_L, let p_e be the *finite transcript and state at the START of epoch e*, BEFORE any fresh reservation's closure. If epoch e eventually has a positive old reset, let
\[
W_e=\#\{\text{completed, negative L-deadline reservations at epoch e before the first positive one}\}.
\]
The count is a natural number and has a concrete finite trace: the W_e wrong-side inequalities L(e,k,p_{e,k})<sigma(p_{e,k}), each with actual mandatory t,u release, followed by the first positive four-run trace satisfying sigma<=L, then the fair three-bit s,t,u wager. Both a recorded timeout and a recorded positive halt are mechanically decidable from a finite real scan transcript plus the bounded M simulation. The negative timed-out event does NOT certify M divergence or permanent absence of a witness.

A *prospective budget* B(e,p_e)>=1 is a total computable integer chosen from only the epoch-start finite transcript and counters, BEFORE the forthcoming W_e misses are seen. A posteriori setting B=W_e+1 is invalid. B may be arbitrarily large and may vary with source-observed epoch starts, but must terminate on all finite histories. We make no claim that W_e or e->p_e is computable without access to X.

## 4. Finite-prefix compulsory-reset shadow lemma

**Lemma 2 (bounded-renewal tail is impossible on CR X).** Fix T_L and a total computable positive epoch-start budget B. It is impossible that, for some E, the actual T_L-run on X has a profitable positive reset at EVERY epoch e>=E, each after W_e<B(e,p_e) timeouts.

**Proof.** Assume such E exists. The actual finite transcript before epoch E is a particular finite binary word h, and its already queried raw indices are computable from T_L and h. Finite h may be *hard-coded into the description of a machine*: no oracle or uniform method of finding h or E is asserted.

Construct a new total computable fresh scan Q_{B,h}. It first queries, at zero stake, exactly the finitely many source coordinates queried along h, in their h-order. On a mismatch it abandons the emulation and queries all remaining coordinates in increasing order at zero stake forever. On exact match it resumes T_L at epoch E with precisely h's saved table/counters. In each ensuing epoch it computes B(e,p_e) at the epoch START and permits at most B such finite reservations. If a positive event arrives within the budget, it makes the identical certified fair 8/7 s,t,u wager and resets. If B consecutive reservations time out, it consumes the still-unread old s **at zero stake**, and enters a fresh epoch. Here compulsory old reset is a feature only of the SHADOW, not of T_L.

On every input branch Q_{B,h} is total, computable and no-repeat; every finite-budget epoch ends and consumes its least unread sentinel. The initial mismatch branch is exhaustive, as is the matching branch after bounded epochs. Thus Q_{B,h} is a fair-coin-preserving computable homeomorphism with total computable inverse: from any output, replay until the desired raw index is queried. Its rational fair output martingale is zero stake on prelude, mismatch and timeout, and the exact 8/7 hedge at positive exits.

On X the initial word is h. By the assumed tail bound, *the shadow never uses its compulsory timeout reset on X*: it follows T_L identically and gains factor 8/7 infinitely many times. Therefore the output martingale succeeds on Q_{B,h}(X). But X is computably random and Q_{B,h} is an effective fair-coin isomorphism; P4-S001/SRC-0015/THM-0038 says its image is computably random. Contradiction. QED.

The hard-coded finite prelude is necessary: naive comparison with a shadow run from the empty history can diverge at its FIRST failure and provides no theorem about the actual success-gated schedule. The contradiction starts after the hypothetical LAST over-budget episode. This is a legitimate existential computable witness in the CR definition, not noncomputable advice delivered to a running controller.

## 5. New actual-source success-gated obstruction

**Theorem 3 (every computable renewal budget is exceeded infinitely often, conditional on infinite success).** Fix ANY total computable tenure L(e,k,p) and the genuinely success-gated T_L of Section 1. On the committed computably random X, exactly the following necessary alternative holds:
\[
\boxed{\quad
(\text{only finitely many positive old turnovers})
\ \lor\
\bigl[\forall\text{ total computable }B\ge1\
\exists^\infty e:\ W_e\ge B(e,p_e)\bigr].
\quad}
\]
In the second arm there are infinitely many positive resets (so W_e is defined for every e), and for each budget B the infinitely many large W_e epochs have B ACTUALLY EXECUTED finite failed reservations, each preserving the old s while releasing t,u at zero stake, before eventually executing a fresh positive 8/7 reset. The quantifier over B is *per fixed T_L* and source-reached p_e, not uniform across changes of L.

**Proof.** If T_L has only finitely many resets, the first arm holds. Otherwise every finite epoch ends in a positive reset, p_e and W_e are defined for all e, and each q_{e,k} is a previously wholly unread fresh target. If there existed any total computable B for which W_e<B(e,p_e) for all but finitely many epochs, choose E after the exceptions; Lemma 2 contradicts X in CR. Negation gives infinitely many W_e>=B(e,p_e) for every such B. QED.

**Corollary 4 (non-domination of renewal *miss counts*).** Under the hypothetical infinite-success second arm, no total computable B(e,p_e) eventually strictly exceeds W_e. In particular infinitely many profitable epochs must contain at least one miss (B=1), and for each fixed n there are infinitely many profitable epochs with at least n misses (B=n). The miss sequence is unbounded on every tail, and it defeats even computable transcript-adaptive epoch-start budgets. It is NOT a global non-domination theorem for sigma, nor an algorithm that locates the violating epochs.

**Corollary 5 (no eventually bounded-gap four-run thickness on X).** No computable epoch-start budget B can force, along the actual X and this controller, timely positive minimum-clock certificates within its first B fresh-block reservations at *every sufficiently late successful epoch* if those epochs are infinite. This rules out an operational bounded-renewal thickness claim substantially stronger than eventual existence of each source-specific certificate. It does not rule out unbounded, non-effectively prompt, *branchwise-avoidable* repeated success.

## 6. Exactly what this does and does not settle

There are three noninterchangeable levels:

1. **On-source eventual halting:** for each actual X-derived p_{e,k}, the four-run minimum sigma(p_{e,k}) exists and is <=T_Y(q_{e,k}); this is only a retrospective partial-computable search on finite p.
2. **Computable pre-consumption protection:** each tenure L(e,k,p) and epoch-start B(e,p_e) is a terminating finite computation on ALL transcripts. Timely capture is a checked positive halt before s,t,u consumption; a timeout releases t,u, never s, and continues on an unrevealed old coordinate.
3. **Infinitely many executed gains:** this is an infinite *actual scan trace* whose positive terminal s,t,u ledger multiplies by 8/7. It is not supplied by (1) or (2). If it existed it would establish X not in OH, hence a failure of OH invariance under H (since H(X)=Y not in OH), but its existence is **not** established.

P4-S056 gives unconditional eventual slow clocks only on its compulsory-old-reset X-selected schedule. The present result is different: it constrains the *number of real success-gated misses* conditional on possible infinite turnover, and does not say any individual success-gated attempt is eventually always late. Our proof's counterfactual shadow is an everywhere-reset effective isomorphism and therefore cannot itself win on X; it is used solely to refute a hypothesized bounded-renewal tail. It does not assert a reset deadline on all continuations of T_L and does not violate P4-S053.

P4-S008 remains decisive if the success-gated source eventually retains one s forever: infinite profit with that persistent hole is impossible. P4-S052 excludes a shielded-old orientation, not the positive wrong-cube hedge. No ticket/reserve/frontier, backward-price or general compiler investigations are reopened. All randomness, prior-art and authorization guards stay unchanged.

**Stopping point.** Established the unconditional **dichotomy of finite turnovers versus infinitely many epoch-start-budget overruns** for each total computable success-gated four-run controller, plus an explicit finite-prefix shadow proof and legal one-hole/fair-capital controller. Did **not** establish that the second arm occurs on X; did **not** establish a computably checkable sufficient thickness condition VERIFIED for committed M/X; did **not** resolve X in OH, R_2=OH, or the P4-S033 normalization target. PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. Phase 4 OPEN, Phase 5 CLOSED; no novelty, openness, prior-art, Gate-4, publication or outreach claim.

**Next P4-S058 target.** Seek a specifically source-reached, mechanically checkable renewal *lower* condition not collapsed by Theorem 3: e.g. a computable adaptive schedule admitting arbitrarily many unsuccessful fresh reservations and nonetheless infinitely many eventual *timely* positive 8/7 turnovers on X. Alternatively sharpen the conditional overrun law to a nontrivial global quantitative restriction on successful epochs without assuming a fixed computable bound on their number of misses. Never replace success-gated timeouts with compulsory old resets in the proposed winning scan.
