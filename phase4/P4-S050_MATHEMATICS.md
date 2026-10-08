# P4-S050 — forbidden-pair hedge, globally legal square exits, and reset obstruction

Date: 2026-10-08
Session: P4-S050
Incoming checkpoint: 9d03117f2674bd0a942634520ff4bed0890f5e1b
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding

Result: **A SINGLE FINITE REFUTATION OF ONE TWO-RAW-BIT CORNER, DISCOVERED BEFORE EITHER RAW COORDINATE IS READ, SUPPORTS AN EXACT NONNEGATIVE COMPUTABLE SEQUENTIAL FAIR HEDGE WITH TERMINAL CAPITAL 4/3 ON EACH OF THE OTHER THREE CORNERS. THIS IS UNCONDITIONAL ON TRAPPED-OLD-EPOCH SEMANTICS. A TOTAL COMPUTABLE GLOBAL ONE-HOLE SCAN CAN EXECUTE THAT HEDGE, CONSUME BOTH RAW COORDINATES, AND RESTART, OR TIME OUT THE TRANSIENT FUTURE COORDINATE AT ZERO STAKE WHILE KEEPING THE OLD SENTINEL. A COMBINED OLD-BRANCH/SQUARE POLICY GAINS AT LEAST 4/3 PER POSITIVE EXIT, AND INFINITELY MANY EXITS (IN PARTICULAR INFINITELY MANY EXECUTED SQUARE CAPTURES) IMPLY X NOT IN OH. UNDER HYPOTHETICAL X IN OH, EACH COMPUTABLE COMBINED POLICY MAKES ONLY FINITELY MANY POSITIVE EXITS AND THEREAFTER HAS ONE PERSISTENT OLD SENTINEL WITH NO FINITE OLD-BRANCH REFUTATION AND NO FURTHER CAPTURE BEFORE TRANSIENT TIMEOUT. HOWEVER A GUARANTEED ONE-REFUTATION HEDGE MUST CONSUME BOTH OLD AND FUTURE BITS: IT DOES NOT REUSE ONE TRAPPED OLD SENTINEL, AND THE COMMITTED SOURCE HAS NO PROVED INFINITE CROSS-EPOCH CAPTURE SCHEDULE. NEITHER X IN OH NOR X NOT IN OH IS ESTABLISHED.**

## 0. Authority and frozen boundary

Live main equalled the exact outgoing P4-S049 checkpoint 9d03117f2674bd0a942634520ff4bed0890f5e1b, without mismatch. The tree contained the completed P4-S049 mathematics/validation/close records and no P4-S050 records. P4-S050 was unique.

Read the P4-S001–P4-S049 mathematics sequence, required CAND-01 authority (phase2/P2-S001_DISCOVERY.md, phase2/P2-S003_FORMULATION_ALIGNMENT.md, phase2/candidates.json and P3-S008 gate authorization), phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, and the special-focus records P4-S011, P4-S012, P4-S027, P4-S041 and P4-S044–P4-S049. All validated mathematics through P4-S049 remains frozen; no ticket/reserve, backward-price, generic radius-one, or other settled local route is reopened.

Retain exactly

\[
R_2=\{x\in CR:\text{all total computable fair-coin-preserving global-}k=2\text{ maps send }x\text{ into }CR\},
\]
\[
OH=\{x\in CR:\text{all total computable adaptive no-repeat one-hole scans send }x\text{ into }CR\},
\]
\[
OH^{iso}=\{x\in CR:H(x)\in OH\text{ for every computable fair-coin-preserving homeomorphism }H\},
\]
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Use the P4-S011 computably random wtt-autoreducible target Y, its syntactically self-avoiding use-clipped partial implementation M, the established destroyer D, and X=H^{-1}(Y) for the repeated three-bit invertible recoding. We have X in CR and H(X)=Y not in OH. The assertion X in OH remains unresolved.

## 1. Positive square exclusion, with no trap oracle

Fix distinct unread raw coordinates s=(b,i) and t=(c,j) in different recoding blocks, with the current finite observed source history agreeing with X. For each a,beta in {0,1}, let

\[
W_{a,\beta}=H(X\text{ with raw values at }s,t\text{ set to }a,\beta).
\]

The live program simulates M on the four counterfactual oracles using hypothesis values for s,t, and obtains every other required raw value only by zero-stake queries of still unread coordinates (or reuses recorded values). The computable recoding H and wtt use permit every finite trace to be simulated. No actual value of s or t is used as a program parameter.

Define Ref(a,beta) to mean that a finite computation M^{W_{a,beta}}(n) halts with a nonbinary output or an output different from W_{a,beta}(n). A finite Ref witness is positive c.e. data relative to the revealed outside-pair transcript. No inference is drawn from absence of a halt.

**Lemma 1 (uniform pair exclusion).** If Ref(a,beta) is discovered with s,t unread, then the actual pair (X(s),X(t)) differs from (a,beta), on *every* epoch, trapped or not.

**Proof.** Were both raw hypotheses actual, W_{a,beta}=Y. The committed target equations M^Y(n)=Y(n) are total, binary, and correct. A finite wrong/nonbinary halt on Y is impossible. This does not require either individual raw bit to be predictable. ∎

Distinguish:
- pair exclusion: one positive Ref eliminates exactly one atom;
- individual-bit prediction: needs a whole row or column excluded, or a separate sound source-specific premise such as P4-S049 shielding at a truly trapped old epoch;
- pair hedge: a fair finite bet earns on the three allowed atoms without identifying either individual bit.

## 2. Exact two-bit fair hedge

**Theorem 2 (forbidden-pair sequential hedge).** Suppose Ref(a,beta) is found while both s and t are unread. From initial capital C>0, query s first with next-bit capital values

\[
C_s(a)=\frac23 C,\qquad C_s(1-a)=\frac43 C.
\]

If s=a, query t with next-bit capital values 0 when t=beta and 4C/3 when t=1-beta. If s=1-a, query t at zero stake and retain 4C/3. The terminal payoff is

\[
G(x_s,x_t)C=
\begin{cases}
0,&(x_s,x_t)=(a,\beta),\\
4C/3,&\text{otherwise}.
\end{cases}
\]

Every branch is nonnegative and every single next-bit bet is fair. In particular, on the actual source the terminal multiplier is deterministically 4/3, without a trapped-epoch premise or a prediction of either individual bit.

**Proof.** The first-stage mean is (2/3+4/3)C/2=C. Conditional on s=a, the t-stage mean is (0+4/3)C/2=2C/3. Conditional on s=1-a, its mean is 4C/3. Thus the two wagers are fair, including the zero-stake second branch. All numbers are nonnegative computable rationals times C. The terminal mean is (0+3(4/3))C/4=C. By Lemma 1 the actual forbidden atom is impossible, so terminal capital on X equals 4C/3. Nothing is bet on either coordinate until the finite witness is visible; queries occur in s-then-t order, and both are fresh. ∎

The intermediate capital can dip to 2C/3. The guaranteed gain is a **completed-pair** gain, not monotonicity after the first query.

The square simulation and hedge choice are reconstructible from the output transcript and the fixed controller, so the strategy defines one total computable rational-valued fair output martingale, not an oracle for s, t, or the semantic trap.

## 3. Smallest positive orientation and escrow upgrades

At any epoch, two finite exclusions in one old-value row (a,0),(a,1) positively force X(s)=1-a. Two exclusions in one future-value column (0,beta),(1,beta) positively force X(t)=1-beta. Two diagonal exclusions leave the other diagonal, which fixes the parity relation but neither bit separately; the fair terminal payoff 2 on those two allowed atoms and 0 on the two refuted atoms gives a guaranteed factor 2 *after both coordinates are consumed*. Three excluded atoms identify both bits and support factor 4. More generally a positive finite set E of r distinct refuted atoms, 1<=r<=3, gives the exact fair terminal hedge

\[
G_E(u,v)=\frac4{4-r}\mathbf1[(u,v)\notin E],
\]

implemented in the order s,t by its conditional fair-coin expectations. These are finite positive-information upgrades. An old-branch refutation independently predicts s, and may close the epoch without the pair hedge. A later refutation after t has already been consumed can be used to predict s only when its future hypothesis equals the now-known t value; then it is just a finite refutation of an old one-bit completion. The absent-halt case never supplies orientation.

**Lemma 3 (one-pair reset cost).** Given only exclusion of (a,beta), with no other source-specific premise, there is no one-bit fair wager solely on t which earns a strict factor >1 on every allowed pair while s stays permanently unread. The analogous statement holds for a wager solely on s.

**Proof.** Both (1-a,0) and (1-a,1) are allowed. A fair single-bit payoff on t has arithmetic mean C, so its two outputs cannot both exceed C. Similarly both (0,1-beta) and (1,1-beta) are allowed for s alone. Therefore the universal strictly profitable hedge must settle the joint exposure by querying both coordinates, or else acquire further finite positive information. ∎

This explains a new **reset cost**: the unconditional hedge consumes the old sentinel; it cannot repeatedly monetize refutations against the same trapped old hole by retaining s, unlike the conditional P4-S049 future-bit prediction at a known trapped epoch.

## 4. A globally legal live square-exit controller

**Protocol S_sq.** Maintain a finite queried set and recorded raw answers. Begin each epoch with the least unread coordinate s as old sentinel. Never query s during preparatory simulation. Choose a fresh t in a different raw block and reserve it only for a finite, computably specified tenure (e.g. a finite number of dovetail rounds depending on the current epoch and reservation index).

During each tenure:
1. dovetail all four counterfactual M computations and all inputs, symmetrically, in finite rounds; hypothesis answers at s,t are synthetic;
2. request and read every needed other raw coordinate at zero stake, or use its already stored value; run the background least-unread sweep, excluding s,t;
3. if the first positive finite pair refutation is visible while both s,t are unread, immediately execute Theorem 2, query s followed by t, and restart a fresh epoch;
4. if no such event is visible by the finite timeout, consume t at zero stake, retain s, and select a new transient future target.

The controller can give priority to a caught pair refutation over a simultaneous old-branch event. The *combined* protocol S_comb also symmetrically dovetails both one-bit old completions H(X with s=h) in the background. If an old-branch finite refutation is first visible, correctly wager all capital on X(s)=1-h, consume s; consume any currently reserved t at zero stake, then start a new epoch. A square event instead executes the two-bit hedge. The old-completion simulations may not consume s; if they need the current transient t, the query is deferred until t is released by a timeout. This preserves the one-hole no-event fallback.

All finite simulations are scheduled in computably bounded slices between successive emitted source bits. Never wait for an oracle computation to halt. For example, after each bounded slice either make an eligible zero-stake support query, a zero-stake least-unread sweep query, a wager query, or consume the timed-out t. Choose the schedule so every fixed raw coordinate except a persistent s is eventually swept in an infinite no-exit epoch, and every fixed old-completion computation is eventually resumed on that branch.

**Theorem 4 (global legality).** Both S_sq and S_comb are everywhere-total computable adaptive no-repeat scans. On every infinite transcript they omit at most one raw coordinate and preserve fair coin. Their fibres have cardinality at most two.

**Proof.** Every output step has finite effective internal work and queries a fresh coordinate; support and sweep queries never consume either protected coordinate. Every tenure ends finitely by timeout or a positive event. A successful square exit consumes s,t; an old-branch exit consumes s and releases t. On an infinite sequence of exiting epochs, each epoch starts with the least unread s and eventually consumes it, so each fixed coordinate is eventually consumed. If exits eventually cease, there is a final s; every transient t is consumed after finite tenure, and the least-unread background sweep consumes every other coordinate in the remaining infinite epoch. Hence at most that final s can be permanently omitted. For any output prefix of length m, its m distinct queried coordinates are determined by preceding output bits, so its fair-coin preimage has measure 2^{-m}. An output fixes all queried bits, leaving at most one free bit, proving the fibre bound. ∎

The total controller is a genuinely global algorithm. It does not hard-code the actual old bit or the semantically first trapped epoch.

## 5. Captured square events, success, and exact quantifiers

A **captured square event** is a positive finite Ref(a,beta) produced by the live simulation while the currently active s,t are still unread. An **executed capture** means the policy consequently applies the hedge and consumes both. S_sq/S_comb execute every captured event unless the controller has already taken a separately visible old-branch exit, in which case the pair no longer counts as active.

**Theorem 5 (infinite square exits destroy).** If a single total computable globally one-hole-safe S_sq/S_comb policy executes infinitely many captured square events on X, then X not in OH. More generally infinitely many combined positive exits (pair-refutation exits or old-branch-refutation exits) suffice.

**Proof.** Construct the one output martingale by the computable controller's stages. Every pair exit multiplies completed capital by 4/3, by Theorem 2. Every old-branch exit doubles it because a finite wrong old completion excludes that old value. All other source queries have multiplier 1, and no wager loses on X. After N completed exits, capital is at least (4/3)^N. If exits are infinite, capital is unbounded (indeed its completed-exit values diverge). The scan has all global properties of Theorem 4. Hence the output is not computably random, and X not in OH. ∎

The word **executed** is essential. An arbitrary passive scan can collect infinitely many refutations sharing an unread old sentinel but never consume that sentinel. A single excluded atom does not allow an unconditional gain on t alone (Lemma 3). Thus no theorem about *arbitrary passive event capture* is inferred; Theorem 5 is for the explicitly specified square-exit policies.

**Theorem 6 (algorithm-relative persistent-sentinel obstruction).** Assume hypothetically X in OH. Then for **each fixed total computable** S_comb policy of the above class, there are only finitely many positive exits along X. The run therefore reaches a final persistent old sentinel s_* and has:
1. no finite old-branch wrong/nonbinary refutation of either completion which could be eventually exposed by its fair old-branch dovetail;
2. no further captured finite square refutation before any active future reservation's timeout; in particular only finitely many transient reservations in the whole run can produce executed square captures.

**Proof.** Infinite positive exits would contradict X in OH by Theorem 5. A finite number of exits leaves a final epoch, in which the old sentinel persists and all other coordinates are eventually read by Theorem 4. A finite old-branch wrong/nonbinary computation has finite support; after that support is acquired and sufficiently many finite simulation rounds, it must be detected, forcing another exit, contradiction. Likewise any square refutation *caught before its tenure ends* would trigger an exit. This says nothing about a refutation which appears after timeout, or about an untried future square. ∎

The final old sentinel and final-exit index depend on the **chosen algorithm and X**. There is no uniform computable final index, no semantic prohibition of infinitely many actual A blocks, and no claim that every later square lacks a finite refutation. The existence of a finite witness and timely capture of that witness are different assertions.

## 6. Source-specific capture gap and reset barrier

P4-S049 says that at a genuinely trapped old sentinel the actual future column comprises Y and the false old partial fixed point Z, so every finite square refutation lies in the wrong future column. In particular each actual future Case-A_j has a finite positive Ref witness. Theorem 2 now allows a gain from **any** discovered Ref, even before knowing whether s is trapped.

That does **not** establish infinitely many executed captures on the committed X. Every executed unconditional hedge consumes s, changes the subsequent fresh-target schedule, and loses access to the semantic shielding of that old sentinel. In contrast the P4-S049 conditional predictor kept the same genuinely trapped s open and bet on future t. A c.e. finite refutation may appear only after a transient t is consumed, regardless of finite wtt *value* use. Neither infinitely many semantic actual-A blocks, the value horizon of P4-S044, increasing tenure, nor simultaneous dovetailing by itself gives an effective bound on **certificate arrival before consumption** across renewed epochs.

In particular, no infinite-capture theorem, same-source OH non-invariance witness, or computable-randomness contradiction has been obtained. Failure to find such an algorithm also does not prove X in OH.

## 7. Disposition and next question

Established: exact forbidden-pair two-bit hedge with guaranteed 4/3 payoff and no trap oracle; globally fair, total, one-hole-safe square exits; a combined positive old/square protocol; infinite executed exits imply X not in OH; the algorithm-relative eventual persistent-sentinel obstruction under X in OH; and the universal single-pair reset-cost lemma.

Unresolved:
\[
X\in OH\;?,\qquad X\notin OH\;?,\qquad R_2=OH\;?
\]

Retain
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Next bounded mathematics question: can **finite positive square data be carried across an old-sentinel reset** or organized into a computable sequence of pre-consumption captures, overcoming both transient certificate-time lateness and the lost common trapped old hole? Keep the distinction between passive square events and executed square exits exact. Do not posit a trap oracle, an event-time bound from wtt use, or an eventual reset-free source characterization.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 unchanged. Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, Gate-4, publication or outreach claim.
