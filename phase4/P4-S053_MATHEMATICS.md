# P4-S053 — effective cross-epoch promptness and the finite-window latency barrier

Date: 2026-10-08
Session: P4-S053
Incoming authoritative main: 255c83c9e7638d91c452447a9525ec7de135c127
Scope: Phase 4 Mathematics only; selected CAND-01; post-recoding one-hole normalization.

Result: **An explicit adaptive finite-window controller has an exact trace-effective prompt-escrow condition that suffices for infinitely many profitable old-sentinel turnovers. The condition quantifies certificate arrival before BOTH future releases and is not supplied for the committed X. All-continuation positive reset at any reached epoch is already an effectively bounded bar; imposing it at every epoch collapses the scan to an exhaustive computable isomorphism. A computable delayed-publication model defeats any fixed finite-window success-gated scheduler despite eventually providing complementary, sound, opposite-row certificates for every spent target. This is a policy-relative timing obstruction, NOT a realizable-M counterexample or an OH classification. Escrow improves reset freedom, not earliest certificate availability; on shielded X the enhanced 8/3 orientation is excluded.**

## 0. Frozen authority

Incoming live main was independently checked to equal the checkpoint above; P4-S053 had no records. The committed P4-S001–P4-S052 mathematics, required CAND-01 authority, Phase-4 post-S031 research pivot, and later sessions were inspected, with focus on P4-S008, P4-S011, P4-S012, P4-S027 and P4-S044–P4-S052.

Keep the P4-S011 computably random Y with syntactically self-avoiding use-clipped wtt autoreduction M; the P4-S033 repeated-block computable fair-coin homeomorphism H; and X=H^{-1}(Y) in CR, while H(X)=Y is not in OH. Keep, without strengthening,

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Neither X in OH nor R_2=OH is decided. A positive Ref(s,t;a,beta) is a FINITE observed wrong/nonbinary M-equation under the specified raw counterfactual, all other accessed raw bits supplied by the transcript. Silence, a timeout and divergence are not certificates. At the P4-S049 genuinely shielded epoch only the incorrect future value can occur in a positive refutation; semantic shielding is not a controller test.

## 1. Finite-window clock and promptness condition

Fix a deterministic total computable tenure rule B. Its two positive integer outputs L(e,k,p) and K(e,k,p,w) depend only on finite observed transcript p, epoch e, reservation k, and, for K, the finite first certificate w. This permits adaptive windows selected from prior observed delays. Each output is a finite integer; neither bound is an oracle for X nor a semantic trap detector.

Define a controller S_B on arbitrary raw inputs as follows.

* At epoch e take s to be the least unread raw coordinate. At reservation k choose t to be the least unread coordinate in a block other than s. Protect s,t for at most L(e,k,p) ordinary rounds.
* Every ordinary round computes a finite symmetric dovetail of the first N input M-equations at the four (s,t) corners for at most N steps each, with a global unbounded integer clock N. A missing outside support coordinate is queued for actual fresh zero-stake query. A query into a protected coordinate suspends that simulation, not the entire scan. Alternate least pending outside support with a least-unread outside sweep; output exactly one fresh unprotected raw bit per round.
* If a first positive Ref(s,t;a,beta) becomes visible while s,t are unread, choose u to be the least unread coordinate in a third recoding block and protect s,t,u during a closure window of K(e,k,p,w) further rounds. Continue the finite symmetric (s,u) computations using the same outside-support queue and sweep. (An already queried support bit is reused, never queried again.)
* If a positive Ref(s,u;1-a,gamma) becomes visible before either t or u is consumed, execute the P4-S051 fair t-then-u hedge. Its actual terminal capital is 4C/3 because (beta,gamma) is excluded. Then query s: all-in only upon a separate positively verified old orientation, otherwise at zero stake. All three protected coordinates are now consumed; begin epoch e+1.
* If the initial window times out, query t at zero stake and retain s. If closure times out, query BOTH t,u at zero stake and retain s. Begin reservation k+1. There is NO old-sentinel timeout. A late certificate cannot produce a retroactive bet on an already read t or u. Other optional certified one-bit exits are deliberately omitted from this minimal controller, to keep the promptness statement exact.

This is a specific code schema: for example the fully computable base rule L=2^(e+k+3) and K=2^(e+k+4) is valid. A genuinely adaptive choice is L=2^(e+k+3)(1+d), K=2^(e+k+4)(1+d), where d is the greatest finite certificate discovery delay previously observed and recorded (default 0). Such choices may change captured paths but confer no universal source-specific latency bound.

Define P_B(e,X) *operationally* at an epoch reached by S_B on X: after finitely many mandatory failed reservation releases, there is a reservation k whose first positive pair certificate is visible before the L release of its still-unread t AND whose opposed-old-row certificate at a distinct unread u is visible before the K release of t,u, with every required outside support value actually observed in time. The certificate bits and simulation steps are part of the finite transcript, not an after-the-fact semantic existence assertion.

The same condition can be phrased as a finite positive execution trace E(e,k,w_1,w_2): w_1 and w_2 are machine halting records with sound wrong/nonbinary values, the witnessed old rows are opposite, the future coordinates are different fresh blocks, and both witnesses are scheduled and verified strictly before the corresponding protected-bit consumption. For fixed B, each finite E is mechanically checkable. The statement that P_B occurs at every consecutively reached target epoch is an infinite path condition, not decidable from one prefix.

**Theorem 1 (effective prompt cross-epoch sufficiency).** S_B is an everywhere-total computable no-repeat fair-coin-preserving scan of global fibre size at most two, with a total rational nonnegative fair output martingale. If P_B(e,X) holds at every epoch e=0,1,2,... actually reached from the empty transcript, then infinitely many profitable old turnovers are executed and X is not in OH. The same implication holds for any computable success-gated controller whose executed successful epochs include infinitely many mechanically certified positive 4/3 (or correct 2x) exits, provided it never closes an epoch in another way that invalidates the asserted epoch trace.

**Proof.** No ordinary round waits for M or an unsupported oracle bit. Every active future reservation is released at a finite computably selected deadline, while the old least-unread s survives a timeout. Each round exposes a fresh nonprotected bit. If there are finitely many resets, the least-unread sweep and future releases eventually query every coordinate except possibly the final s. If there are infinitely many resets, all least-unread old sentinels are eventually consumed. Thus all completed transcripts omit at most one source coordinate. Each next query is fixed by earlier output bits, so the inverse measure of every m-bit output cylinder is 2^-m. Every hedge uses fair child capitals: the initial t split (2C/3,4C/3), the conditional u children (0,4C/3) in the matching t branch, and identity children otherwise; the old reset is (D,D) unless a separately checked old orientation warrants (0,2D). Hence fairness holds on ALL transcripts, including transcripts where an alleged excluded pair would have been incorrect. Positive certificates are sound on the actual X, so completed escrow capital is exactly 4C/3 and any certified old double is correct. By P_B, induction executes the next profitable turnover in finite time after every prior one; after e turnovers capital is at least (4/3)^e. All such epochs consume s. Thus one computable output martingale succeeds on the one-hole scan of X. QED.

**Critical limitation.** No P_B(e,X) for all e, or even for arbitrarily many successively reachable epochs, follows from P4-S011 target correctness, P4-S027 use clipping, P4-S044 value horizons, recurrence of semantic actual A, c.e. witness existence, or B tending to infinity. This theorem is conditional and NOT a new classification of X.

## 2. Exact adaptive-window comparison

**Proposition 2 (local first-certificate dominance, not global domination).** Suppose an opposed-old-row escrow completes at old s and first future t. Its first witnessed Ref(s,t;a,beta) was already available while s,t were unread. At that exact finite state, P4-S050 could instead consume s then t using its unconditional one-excluded-pair fair hedge for a guaranteed 4/3 on the actual source. Therefore the extra requirement of a second certificate at u does not accelerate the earliest possible locally profitable RESET. On a shielded old epoch the executed escrow cash-out is the double nonmatch, so its old zero-stake turnover also has total 4/3; the 8/3 oriented upgrade is absent.

This is NOT a simulation between entire controllers. The immediate two-bit reset changes the next sentinel, support history and future certificate scheduling, while escrow can retain the old sentinel until the second witness and can choose whether to reset. A later sequence of opportunities on X may differ. Thus neither the earlier two-bit reset architecture nor adaptive two-target escrow is proved globally stronger on committed X.

**Proposition 3 (adaptive windows alone give no capture modulus).** A total computable finite window chosen from earlier transcript data is still a finite window on each reached finite state. An eventual finite positive witness supplies no upper bound on its arrival relative to the protection deadline. Discovering an M-computation's finite wtt VALUE support does not decide its HALTING time on counterfactuals. Waiting indefinitely with s and one other future unread would violate global one-hole safety on a no-event continuation. Thus arbitrarily increasing or observation-adapted L and K cannot, without additional target trace information, prove P_B(e,X).

## 3. Effectively bounded bar versus genuinely avoidable turnover

For a reached finite transcript p with old s unread, consider the event that S_B executes a positive old turnover at some later finite output stage. This event is open in the output-continuation tree: whether it has occurred is decidable from the finite scan transcript. The no-positive-turnover prefixes form a computable finitely branching prefix tree, relative to the known finite p and fixed controller.

**Theorem 4 (positive-turnover bar dichotomy).** Exactly one of the following holds for any reached p:
(a) there is an infinite continuation of p along which the old s is never consumed by a positive turnover; or
(b) a finite computable-searchable integer D(p) bounds the first positive turnover on EVERY continuation of p. If (b) holds, the bound is found by simulating the scan on all binary output extensions of increasing common length until each has turned over.

**Proof.** If no avoiding infinite branch exists, the finitely branching tree of no-turnover prefixes is finite by König's lemma. Consequently it has a maximum level D, which is found effectively by exhaustive bounded simulations of all finite extensions. Conversely if no common finite bound exists, the no-turnover tree has arbitrarily long strings and therefore an infinite avoiding path. Finite simulations terminate since the scan is total. QED.

**Corollary 5 (automatic all-transcript-reset collapse).** If at every reachable epoch prefix of a controller every transcript continuation eventually consumes its current least-unread s (whether on a positive exit or by a timeout), the same bar argument gives a searchable finite reset bound there. All complete transcripts then consume every source coordinate, and the scan is an exhaustive computable adaptive permutation with computable inverse. It preserves CR by P4-S001. Thus the P4-S052 uniformly resettable isomorphism obstruction needs no *given* clock-time reset modulus: eventual reset on all continuations already supplies one by compactness.

On a hypothetical successful CR-destroying run, eventual profitable turnovers along that run must coexist with the controller's possibility of an avoiding continuation somewhere in its globally reachable epoch structure. A bar dichotomy at every individual source prefix should NOT be silently turned into a characterization of the committed X; the actual sequence of reached prefixes can be noncomputable and the existence of alternative paths does not force the actual path to follow them.

## 4. Explicit policy-relative late-publication obstruction

**Proposition 6 (c.e. positive recurrence can miss every finite protection).** Fix any computable success-gated finite-window protocol of the above kind, whose protected future targets are compulsorily consumed in finite time on a no-certificate run. In an ABSTRACT, computably enumerated certificate-publication model, there exists a computable reference bit stream x=0^omega and a computable publication calendar with the following properties:

1. For every spent prospective future target t, after t is consumed the calendar publishes both exclusions Ref(s,t;0,1) and Ref(s,t;1,1) against the current unread s, with s still unconsumed.
2. These exclusions are logically sound on reference x, since x(t)=0, and respect the shield-style rule that only the incorrect future column is finitely refutable. Opposed-old-row refutations are therefore eventually available at every pair of distinct spent targets.
3. No one of them is available before its corresponding target is consumed. The controller executes no profitable positive escrow and performs no old turnover.

**Construction and proof.** Simulate the fixed controller on computable all-zero answers while withholding certificate publications. Each prospective t is released in finite time by the mandatory timeout. At that FINITE release stage enumerate its two wrong-future exclusions, not earlier. The enumeration is computable from the observed simulation; it can also be delayed one further finite stage to avoid ambiguous simultaneous priority. Because no certificate for a live target has been published, the induction makes the controller time out all such targets; each late exclusion mentions a target that is no longer fresh. Its false future value prevents old orientation from the observed actual t=0. Hence the controller remains in its nonexit epoch forever, yet every spent target receives both old-row publications eventually. QED.

**Scope of the obstruction.** This is a certificate-clock model, not a construction of one fixed syntactically self-avoiding wtt functional M producing those wrong halts. In particular x=0^omega is NOT computably random and the calendar is tailored to a given controller. The proposition refutes only the logical inference from c.e. positivity, even extremely redundant eventual refutation, and finite source-value horizons to timely pre-consumption capture. It says nothing by itself about whether the committed M on committed X satisfies some stronger promptness property.

## 5. Exact stopping point

Proved: an explicit bounded-simulation fair global-one-hole controller parameterized by any computable adaptive finite tenure rule; a mechanically checkable two-certificate promptness condition yielding infinite successful turnovers if it holds at EVERY target epoch; local first-refutation reset dominance without global policy dominance; an effectively bounded bar/avoiding-path dichotomy and its all-transcript isomorphism corollary; and an explicit computable abstract late-publication countermodel showing why c.e. eventual certificates are not enough.

Unproved: the requisite promptness profile on X, any successful source-specific cross-epoch infinite capture, X in OH, X not in OH, OH non-invariance, and R_2=OH. In particular do NOT interpret the abstract calendar as an actual counterexample to the committed autoreduction; do NOT use a semantic shielded-epoch oracle; do NOT deduce capture from growing deadlines or passive certificates.

P4-S008 permanently omitted-sentinel obstruction and P4-S052 shielded no-orientation theorem remain in force. PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; no novelty, openness, prior-art, Gate-4, publication or outreach findings. Phase 4 OPEN; Phase 5 CLOSED.

Suggested P4-S054 direction: test an ACTUAL M/X-specific finite-stage promptness invariant or derive a nontrivial necessary law for certified old-turnover timing, beyond abstract c.e. arrivals and without assuming X in OH or choosing a semantic trapped epoch.