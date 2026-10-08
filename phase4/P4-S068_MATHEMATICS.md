# P4-S068 — Actual-source gate-certificate multiplicity and recurrence

Date: 2026-10-08
Session: P4-S068
Incoming live remote \`main\`: \`2fb48831de500cebff79f8f34337f5dbaeb09ffb\`
Scope: Phase 4 — Mathematics ONLY
Disposition: **VALIDATED CONTROLLER-SPECIFIC VALUE-CLOSURE CERTIFICATE MULTIPLICITY IDENTITY AND PERMANENT-CR-STALL WEIGHTED CAPACITY; NO VERIFIED ACTUAL-X RECURRENCE OR INFINITE PROFITABLE EXITS**

## 0. Authority, objects, uniqueness

At entry the most recent GitHub commit on \`main\` was exactly the required outgoing P4-S067 commit. The P4-S068 mathematics path returned 404 at that checkpoint; \`authoritative/STATE.json\` named P4-S067 completed and P4-S068 next, with no owner/external blocker. Read the 67 mathematics records in session order (S001–S067), with focused examination of S008/S011/S012/S027/S033/S039/S041, S044–S067, the selected CAND-01 P3-S007 decision, P3-S008 Gate-3 PASS, the post-S031 Phase-4 pivot and the authoritative session and state records. Frozen mathematics is unchanged.

Retain
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]
Keep the committed computably random Y, **the fixed** syntactically self-avoiding globally use-clipped wtt autoreduction M, the repeated-block fair computable homeomorphism
\[
H(x)_{3b}=x_{3b}\oplus x_{3b+2},\quad
H(x)_{3b+1}=x_{3b}\oplus x_{3b+1},\quad
H(x)_{3b+2}=x_{3b}\oplus x_{3b+1}\oplus x_{3b+2},
\]
and X=H^{-1}(Y) in CR. H(X)=Y is not in OH; **X in OH and R_2=OH are unresolved**. P4-S011 obtains Y/M from the cited existence theorem and P4-S027 fixes a globally use-clipped normal form. Neither that commitment nor P4-S067's hypothetical padded *different* program is altered here.

Fix the **unaltered P4-S057 success-gated four-run controller T_L**, for any total computable positive prospective tenure L(e,k,p). At each epoch old s is the least unread raw coordinate. Each reservation chooses the least wholly unread block disjoint from s's block, with t=3b, u=3b+1, v=3b+2, q=3b. It protects s,t,u; exposes v and every as-yet-unread outside raw bit below the clipped frontier V(q)=3 ceil(U(q)/3); then fixes L from this genuinely value-closed finite state; simulates exactly four paired representative M(q) traces; and takes a positive gate only upon an **ordinary** wrong-output/nonbinary finite halt before consuming protected bits. Its bounded simulator may emit zero-stake least-index nonprotected fillers. On positive gate it consumes s,t,u with terminal ZERO at exactly one excluded atom and 8/7 at each of the other seven. On every timeout it releases t,u at ZERO stake and performs the mandatory non-s sweep WITHOUT resetting old s. Totality, freshness/no-repeat, fair-coin preservation, global one-hole fibres and rational fair intermediate ledger remain as in S057.

P4-S066 proved that on every hypothetical permanent stall on a CR raw source the **actual** next-reservation hazards gamma(p_n) have finite sum. P4-S067 wrote gamma(p) as the weighted sum of all first positive-gate output decision leaves and obtained a necessary shortest-leaf capacity law. We sharpen the gate *multiplicity representation for this particular controller*.

## 1. Effective closure cylinder and inert-filler compression

Fix any **valid next-reservation start** p, before the new reservation's zero-stake value closure. Its finite already-read raw-coordinate set R and counters are reconstructible from p and T_L. Selection of s, the entirely unread block (t,u,v), q and the ordered finite value-closure query list
\[
C(p)=(r_0,\ldots,r_{c(p)-1})
\]
is **independent of the values still to be read**: the block and closure use only the finite read set and computable U(q). The list contains v and all other as-yet-unread r<V(q) outside protected s,t,u; every element is fresh. Write c=c(p), a computable natural number. (This includes v even when other frontier values were read in earlier reservations.)

For each eta in {0,1}^c, follow this closure with exactly these values and obtain the finite value-closed p_eta. It fixes the prospective integer L(e,k,p_eta)>=1 before the four-run search. Define a **finite decidable positive predicate**
\[
B_p(\eta)=1
\quad\Longleftrightarrow\quad
\text{at least one of the four clipped paired M(q) traces has an ordinary halt by }L(e,k,p_\eta).
\tag{1}
\]
By P4-S055 paired-q invariance, a binary halt identifies the uniquely wrong member of its virtual-q-flip pair, and a nonbinary halt supplies an ordinary refutation. Thus (1) is equivalent to *a permitted positive pre-consumption gate*, not merely an arbitrary halt. Clipping or timeout is NEVER a gate. The full M-step convention and fixed tie rule are unchanged. Define
\[
A(p)=\{\eta\in 2^c:B_p(\eta)=1\},\qquad a(p)=|A(p)|.
\]
Both c(p) and the **integer** a(p) are uniformly computable from each finite valid p **with the fixed M/U/L descriptions supplied as part of T_L**: exhaust the 2^c closure assignments and run each of the four bounded traces. No oracle for Y, X, actual runtimes or semantic partial fixedness is used.

**Lemma 1 (value-closure gate-cylinder law).** For the *true unchanged* T_L, the event that the next reservation makes a positive gate decision before protected consumption is exactly the union of the 2^{-c} closure cylinders indexed by A(p), independently of all later emitted filler values. Consequently
\[
\boxed{\qquad \gamma(p)=\frac{a(p)}{2^{c(p)}}. \qquad}
\tag{2}
\]
In particular gamma(p)=0 iff a(p)=0, and gamma(p)>0 iff at least one closure assignment supplies a finite timely ordinary certificate.

*Proof.* The closure query list is fixed given the prior read set. Its values are c successive independent fair output bits. After closure, all possible ordinary M(q) oracle answers lie below U(q): values outside protected s,t,u are observed, while protected values are supplied synthetically in the four representative configurations. The prospective L is computed from p_eta. In each later bounded simulation round the optional next nonprotected filler coordinate is outside the **already exhausted** clipped value frontier (or was queried previously); no filler bit can change a synthetic bounded M(q) oracle reply, L, the step at which any representative halts, or the halt output. It merely provides a fresh fair output step while the deterministic bounded computation advances. Thus the positive decision occurs on **every** continuation of eta exactly when B_p(eta)=1, and on **no** continuation otherwise. Positive decisions precede all protected s,t,u queries; terminal 8/7/zero branches and timeout t/u-release/sweep branches are excluded from this decision event. The c-bit cylinders are disjoint and each has fair conditional probability 2^{-c}, proving (2). QED.

**Leaf reconciliation.** P4-S067's literal output decision leaves G(p) may include extra, causally *irrelevant* filler bits before the bounded computation declares a gate; the resulting leaves can have varying greater depths. By disjoint cylinder refinement, each eta in A(p) has all of its filler continuations positive; summing their prefix-free first-decision leaf weights gives exactly 2^{-c}. Hence
\[
\sum_{w\in G(p)}2^{-|w|}
=\sum_{\eta\in A(p)}2^{-c(p)}.
\tag{3}
\]
This is a lossless *probability compression*, NOT a licence to move the actual gate earlier or to omit any mandatory real filler steps.

## 2. Source-reached multiplicity/closure-capacity law

**Theorem 2 (necessary closure-certificate summability).** Let Z be any computably random raw source on which T_L genuinely reaches a fixed epoch start h and then finishes infinitely many actual timeout reservations without one positive gate or old-sentinel reset. Write p_n for the actual next-reservation start after n genuine timeouts, with its **real endogenous** read set, fresh block and mandatory non-s sweeps. Set c_n=c(p_n), a_n=a(p_n). There is a finite source/epoch/controller-dependent B such that
\[
\boxed{\quad \sum_{n=0}^\infty a_n2^{-c_n}\le B<\infty. \quad}
\tag{4}
\]
For every integer K>=0, simultaneously,
\[
\#\{n:a_n>0,\ c_n\le K\}\le B\,2^K,
\tag{5}
\]
and, more generally, for any nonnegative integer m_n<=a_n selected at each actual stage,
\[
\sum_n m_n2^{-c_n}<\infty.
\tag{6}
\]
In particular, among real stalled reservations with positive finite-closure certificate multiplicity, the sum of their **single-certificate weights** 2^{-c_n} is finite.

*Proof.* P4-S066 gives an actual-path upper bound B>=sum_n gamma(p_n) from its globally computable timeout hedge and P4-S008 fixed-sentinel effective permutation completion; B is not promised computable or source-independent. Substitute the exact identity (2), obtaining (4). On the set in (5), a_n>=1 and 2^{-c_n}>=2^{-K}, so each such index contributes at least 2^{-K} to (4). Equation (6) follows termwise. QED.

**Corollary 3 (multiplicity-sensitive infinitary exclusion supplier).** On any hypothetical actual-X permanent stall, each of the following *independently sufficient* hypotheses would contradict X in CR:
\[
\sum_n a(p_n)\,2^{-c(p_n)}=\infty;
\tag{7}
\]
or the weaker-to-check *conditional supplier*
\[
\exists(m_n\in\mathbb N)\,
[\,0\le m_n\le a(p_n)\ \forall n
\ \land\ \sum_n m_n2^{-c(p_n)}=\infty\,].
\tag{8}
\]
A particularly useful special case is: infinitely many indices n have at least a fixed fraction delta>0 of all closure assignments leading to timely positive gates. Then gamma(p_n)>=delta at infinitely many n, contradicting (4). Another special case is a set I of genuine stages each admitting one positive closure certificate and with sum_{n in I}2^{-c_n}=infinity. These are **conditional infinite-history suppliers**; no such fact has been established for X.

**Sharper than minimum full-leaf depth.** If positive gates require many machine filler rounds, the minimum full-output certificate depth d(p) can be far larger than c(p). Nevertheless **one** positive closure assignment already costs hazard 2^{-c}, irrespective of its later gate announcement depth. A high multiplicity a(p) costs its exact weighted closure fraction. This is a genuine controller-specific improvement over relying only on S067's lower bound 2^{-d(p)}. Conversely, if c_n grows very quickly, even a_n=1 at every n can have summable hazards; if a_n=0 then no positive gate is possible under that tenure despite target eventual M^Y halting.

## 3. What actual M/Y/X and the endogenous schedule do NOT force

Along a genuine no-gate timeout on X, the **actual** closure assignment eta_n is outside A(p_n), because the bounded four-run test did not gate. P4-S054/S055 guarantee that the true-target paired M^Y(q_n) ultimately halts, so the *unbounded* four-run minimum clock sigma(p_{n,eta_n}) is finite; by actual timeout,
\[
L(e,k,p_{n,\eta_n})<\sigma(p_{n,\eta_n})\le T_Y(q_n)<\infty.
\tag{9}
\]
The inequality says **nothing** about B_{p_n}(eta) at different closure assignments eta. A target halt after the genuine deadline does not become a timely sibling halt by altering filler values (Lemma 1: fillers are inert), and neither syntactic avoidance nor finite use clipping bounds halting times on those siblings. The fresh q_n and the unread support c_n are determined by the *actual prior timeout t/u releases, closure and sweep*, not by a preselected computable q sequence.

The construction of the committed Y and M is fixed in the record by a **mathematical existence theorem** (S011, S027) and a specific normal-form prescription, not by a supplied executable machine index and computable presentation of Y. The formula (2) is uniform *relative to the fixed effective controller description*; it does **not** turn the existential witness in the research record into concrete executable code from which numeric a(p_n) or true source p_n can be extracted. This is an evidence/presentation limitation, not a proof that the required X-specific multiplicity law is false. P4-S067's alternative padded-program theorem remains merely an extensional non-implication, NOT evidence about timing of the unchanged M.

The P4-S049/P4-S052 shielded-old restriction still bars a semantic old-orientation oracle. The P4-S053 all-continuation finite-reset bar still bars replacing real timeouts by compulsory old resets. P4-S056 applies to the compulsory-reset shadow, not to actual success-gated recurrence. P4-S057–S065 conditional progress/rarity/overrun/frontier results and P4-S066/S067 pathwise budget results remain frozen and complementary. (2)–(8) neither refute a hypothetical permanent stall on X nor prove even one new actual reset, much less infinitely many profitable 8/7 exits.

**Disposition.** Established an exact *closure-cylinder* compression of the literal positive-gate output leaf set for the genuine four-run controller, and a sharpened **multiplicity/geometry weighted necessary restriction on EVERY hypothetical computably random permanent stall**. Actual X-specific divergence (7), any verified recurrence of a(p_n)>0 at adequately small c_n, infinite actually executed profitable resets, X in OH, X not in OH and R_2=OH remain UNRESOLVED.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 unchanged; Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claim.

**Next P4-S069 target, conditional on no owner/external blocker:** test whether the committed paired M-trace structure, actual value-closure geometry and true X-driven fresh-block schedule prove an infinite lower bound on a(p_n)2^{-c(p_n)} on every hypothetical no-gate X tail, or prove a further rigorous limitation on such lower bounds specific to the fixed M. Keep the exact T_L timeout and filler semantics; do not infer success from a possible closure cylinder or a retrospective M^Y runtime.
