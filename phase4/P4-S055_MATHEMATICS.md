# P4-S055 — paired cube clocks and the exact source-runtime obstruction

Date: 2026-10-08
Session: P4-S055
Incoming authoritative main: 3f5fa3271f0313cbcd881603cdaff005e8aa3e9b
Scope: Phase 4 Mathematics only; source-reached cube-clock totalization for selected CAND-01.

**Outcome.** The P4-S054 eight-corner clock has an EXACT four-computation halting normal form. A pair of raw corners differing in both fresh future bits corresponds to virtual oracles differing ONLY at the target q, so the two clipped M(q) computations are identical. If either halts, one of the pair is a mechanically identifiable finite wrong-output certificate. On every X-derived value-closed cube this four-run clock halts, but it remains only partial computable away from the committed source. The target-source runtime T_Y(q) is a total Y-computable, non-computably-dominated function, by the established no-truth-table-autoreduction boundary for computable randomness. Under hypothetical X in OH, every total computable q-indexed tenure b produces a final-sentinel infinite sequence of fresh q_k on which b(q_k) < sigma(p_k) <= T_Y(q_k). This is a sharper, scheduler-specific, actual-source latency obstruction, NOT infinite capture or a classification of X.**

## 0. Authority, uniqueness and frozen findings

Live GitHub main was pinned to the exact P4-S054 outgoing SHA above. P4-S055 mathematics/validation/close files were absent. Read P4-S001 through P4-S054 mathematics, the CAND-01 discovery/selection authority, the active post-S031 research pivot, and later records, emphasizing P4-S008, P4-S011, P4-S012, P4-S027, P4-S033, P4-S039, P4-S041 and P4-S044–P4-S054. Retain every validated result through P4-S054, especially the persistent-hole prohibition, the shielded-old restriction and the all-transcript-reset-bar theorem.

Retain the computably random target Y, the syntactically self-avoiding globally use-clipped wtt autoreduction M with M^Y(n)=Y(n), the three-bit repeated-block computable fair-coin homeomorphism H and X=H^{-1}(Y) in CR. The image H(X)=Y is not in OH. Retain precisely
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]
The assertions X in OH and R_2=OH remain unresolved.

The committed block map is
\[
(u_0,u_1,u_2)=(x_0\oplus x_2,\ x_0\oplus x_1,\ x_0\oplus x_1\oplus x_2).
\]
For q=3b, t=3b, u=3b+1 and v=3b+2, changing raw (t,u) together carries to virtual e_q. The old unread s is in another block. Let U(q) be the strict computable clipped virtual use cap and V(q)=3\lceil U(q)/3\rceil the computable raw value frontier. A value-closure procedure reads v and ALL as-yet-unread raw coordinates below V(q) except s,t,u, at zero stake. Previously read values are reused. No protected coordinate is actually read. For any such finite observed p, all synthetic M(q) computations have complete finite oracle-answer tables below the clipped cap.

## 1. Paired-corner invariance and exact four-run normal form

Fix any value-closed p, whether source-reached on X or not. Label the eight counterfactual completions by (a,beta,gamma) in {0,1}^3, assigning raw (s,t,u)=(a,beta,gamma), and retaining p's genuinely observed outside values. For every a,beta,gamma, pair it with (a,1-beta,1-gamma). The paired raw oracles differ only at t,u, hence their virtual oracles differ ONLY at q.

**Lemma 1 (exact paired computation).** The two globally clipped M(q) computations on either member of a pair have identical instruction traces, oracle queries and replies, halting/divergence status, running time if halting, and output if halting. Their required virtual q-bits are opposite.

**Proof.** The inverse-support calculation for the fixed H says the paired virtual oracles differ exactly at q. Syntactic self-avoidance makes the M(q) program never query q on ANY oracle; any attempted outside-use query is clipped identically in both runs. Hence every oracle reply seen by M is identical on the pair. But H changes q, so the candidate's q-bit flips. QED.

Choose four representatives
\[
(a,\beta,\gamma)=(a,0,c), \qquad a,c\in\{0,1\}.
\]
Their mates are (a,1,1-c). Simulate the four M(q) runs fairly and synchronously. If a representative halts with binary output z, exactly ONE member of its pair has q-bit unequal to z. Its identity is effectively determined from p, v and the output z. If it halts nonbinary, either member is a wrong/nonbinary certificate. Clipped-out attempts and divergent runs are NOT certificates.

Let rho(p) be the least r>=1 at which one of these FOUR representative runs has a finite ordinary halt with an output, and undefined if all four do not halt. Use the same raw machine-step convention as the retained eight-run sigma(p), with no extra cost for finite-table virtual-answer decoding.

**Theorem 2 (exact clock reduction).**
\[
\operatorname{dom}(\rho)=\operatorname{dom}(\sigma),\qquad
\rho(p)=\sigma(p)\quad\hbox{whenever defined}.
\]
In particular, the first eight-corner wrong/nonbinary certificate appears at EXACTLY the first halting time among the four representatives. This equivalence holds for arbitrary finite value-closed p; no randomness hypothesis is used.

**Proof.** Each representative halt at time r yields a wrong/nonbinary halt at time r in its own pair by Lemma 1, hence sigma<=rho. Every wrong/nonbinary halt in one of the eight corners is also a halt of its corresponding representative at exactly the same machine time, hence rho<=sigma. QED.

This reduces the number of distinct machine traces but does not decide whether any trace halts. It does not generate two opposite-old-row certificates: the two mates of a HALTING representative are in the SAME old row, with one wrong and the other, on binary output, correct.

**Corollary 3 (exact actual-source runtime bound).** At every X-derived value-closed p with fresh target q, the target computation M^Y(q) lies in one of these four trace-pairs. It halts correctly at finite time T_Y(q), so
\[
0<\sigma(p)=\rho(p)\le T_Y(q)<\infty.
\]
The inequality is relative to the common idealized M-step clock used to define sigma; a fixed computable simulator overhead can be absorbed into any implemented integer tenure. The bound T_Y is Y-computable, not proved computable without Y. An earlier off-source halting trace can make sigma MUCH smaller than T_Y; they are not asserted equal.

## 2. Exact non-domination of the full target runtime

Define the total function
\[
T_Y(n)=\min\{r:M^Y(n)\hbox{ has halted within }r\hbox{ M steps}\}.
\]
It is total and computable with oracle Y because M^Y(n)=Y(n) for every n.

**Theorem 4 (target-runtime hyperimmunity).** There is NO total computable g such that T_Y(n)<=g(n) for all sufficiently large n. Equivalently, every total computable g has infinitely many n with T_Y(n)>g(n).

**Proof.** Suppose T_Y were eventually computably bounded by g. Enlarge g at the finitely many exceptional inputs by finitely many hard-coded integer constants; this gives a total computable bound G for T_Y at EVERY input. Simulate the globally use-clipped M(n) for only G(n) steps on an arbitrary oracle; if it has not halted with a binary answer, output the fixed default bit 0. This is a total computable bounded-use, syntactically n-avoiding functional that agrees with Y(n) on Y. Indeed its finite table can uniformly be computed for each n by exhaustively testing all oracle-answer assignments below U(n) for G(n) steps. It therefore gives a truth-table autoreduction of Y. P4-S041 retains the exact source-side fact that a computably random sequence cannot be truth-table autoreducible. Contradiction. QED.

This theorem rules out q-only computable domination of the complete TARGET M^Y run. It is NOT a theorem that sigma is hyperimmune along legally reached p: sigma is the MINIMUM of four sibling-run halting times and can be earlier than T_Y. Nor does it show that the fixed source has, or lacks, infinitely many timely old turnovers. It sharpens the reason why replacing sigma by the known target runtime is not an effective source-free deadline.

## 3. A concrete four-trace finite-window controller

Fix any total computable positive integer tenure L(e,k,p), where p includes the finite value-closed observed transcript and the named q. A useful subfamily is
\[
L_b(e,k,p)=\max(1,b(q))
\]
for any given total computable integer b. There is NO appeal to a clock oracle.

At epoch e let s be the least unread raw coordinate. In reservation k choose the least ENTIRELY UNREAD raw three-bit block B_b disjoint from the block of s, and let t=3b,u=3b+1,v=3b+2,q=3b. Protect {s,t,u}, read v, then perform the finite zero-stake sweep of all not-yet-seen raw coordinates r<V(q) other than the protected three. Compute p and the finite tenure L(e,k,p). During each bounded round r=1,...,L, simulate r machine steps from scratch for each of the FOUR representatives, identifying on any positive halt the mechanically wrong mate of its pair BEFORE any of s,t,u is queried. If no halt, output one zero-stake least-unread raw coordinate outside {s,t,u}. A positive event immediately invokes the three-coordinate hedge below, querying s,t,u in that order, and starts epoch e+1. On finite tenure expiration without a positive event, mandatorily query t and then u at ZERO stake, never use them again, keep old s unread, and start reservation k+1. All ties and fresh-coordinate selections use least-index rules.

A positively forbidden atom (a,beta,gamma) gives rational terminal payoffs 0 on that atom and 8C/7 on each of the other seven. The exact sequential FAIR conditional capitals are: on querying s, (6C/7,8C/7); in the matching old row on querying t, (4C/7,8C/7); in the matching old-and-future row on querying u, (0,8C/7); elsewhere both children are 8C/7. Every parent is the arithmetic mean of its children. No bankruptcy, nonfair wager or prior peek at s,t,u occurs.

**Theorem 5 (global legality and exact capture).** This FOUR-run variant of the retained P4-S054 controller is an everywhere-total computable no-repeat adaptive scan, fair-coin preserving, with every fibre of size at most 2. Its exact rational nonnegative capital process is an everywhere-total computable fair martingale. At each X-derived value-closed reservation p, a profitable executed old turnover occurs IF AND ONLY IF
\[
\sigma(p)=\rho(p)\le L(e,k,p).
\]
Such an exit multiplies the capital by 8/7.

**Proof.** Finite value closure, bounded machine rounds and timeout all terminate on EVERY transcript. All actually queried coordinates are fresh. Both temporary targets t,u are compulsorily queried after a finite time unless the positive exit consumes them together with s. If there are finitely many positive exits, the final s persists but least-unread fillers/closure/mandatory releases consume every other coordinate; if there are infinitely many, each old least-unread s is consumed and the sequence of least-unread indices tends to infinity. Thus every output transcript omits at most one source coordinate. Every fresh unbiased source query has conditional fair probability one half, so the output map preserves fair coin and the fibre bound is 2. The fair ledger applies even on off-target transcripts where the selected forbidden atom may actually occur and lose; global martingale fairness never uses source correctness. The exact clock criterion follows from Theorem 2 and the pre-release r-step simulations. QED.

This uses no second permanent sentinel, no unbounded wait in a source query, no oracle trap flag, no unspent future after timeout and no retrospective certificate.

## 4. The stronger source-runtime escape required by hypothetical OH

**Theorem 6 (quantified fresh-block slow-trace escape).** Assume ONLY here that X belongs to OH. For EVERY total computable b:N->N, run the globally legal controller of Theorem 5 with L=L_b. It has finitely many positive old turnovers and hence a final old sentinel s. Thereafter it executes infinitely many reservations with pairwise distinct fresh virtual target indices q_k=3b_k tending to infinity, and at EVERY such value-closed p_k,
\[
\boxed{\quad \max(1,b(q_k))<\sigma(p_k)=\rho(p_k)\le T_Y(q_k)<\infty.\quad}
\]

**Proof.** Infinite positive exits would make the valid output martingale unbounded on X by the 8/7 factor, contradicting X in OH. Finite exits imply a final old s. Each failed finite reservation compulsorily consumes t,u, so no selected entirely-unread block can recur; the process has infinitely many next reservations and their distinct block indices tend to infinity. P4-S054 and Theorem 2 force finite sigma at every actual p_k. Theorem 5 says any sigma<=L would consume the old sentinel, which no longer happens. Corollary 3 gives sigma<=T_Y(q_k). QED.

The theorem exhibits a policy-dependent infinite sequence of ACTUAL SOURCE target computations outrunning that policy's computable q-clock. It is stronger in its explicit pairing, target-runtime and fresh-block quantifiers than the bare source-independent theorem that T_Y has no computable global upper bound. The sequence q_k is dependent on the observed X transcript and the chosen b; it is NOT claimed computable, fixed across b, or decidable before the source is queried. Theorem 6 remains a NECESSARY law under hypothetical X in OH, not evidence that the hypothesis is true.

Conversely, a total computable b which bounds sigma at at least one reservation in every consecutively reached later epoch of its own run would yield infinitely many 8/7 resets and establish X not in OH. P4-S055 does NOT prove such a b exists. A source-specific finite certificate may be found by an unbounded search that halts on X while diverging on a sibling; that is not an admissible total controller tenure. In particular Theorem 4 does not establish the opposite quantifier for the minimum four-run clock.

## 5. Structural guards and validated boundary

- The target-runtime theorem uses the already retained no-tt-autoreduction CR boundary, not an independent new literature or novelty claim.
- Four representative runs are a smaller exact search, not a second old-row refutation. No P4-S052 shielded-old orientation or 8/3 gain is obtained.
- The only automatic promised positive witness on X is from a virtual UNIT flip implemented by TWO raw future bits; no raw one-bit prediction is inferred.
- One positively forbidden cube atom licenses only a three-coordinate 8/7 wager that consumes s. Infinite gains with a fixed unread s are excluded by P4-S008; mandatory resets on all continuations would invoke the P4-S053 all-transcript computable-isomorphism bar.
- Source-time non-domination, finite wtt use, increasing timeouts, semantic recurrence and late discoveries do NOT prove infinite promptly captured epochs. No numerical runtime, source index, or computable X advice is supplied.
- The frozen P4-S015–P4-S031 ticket programme, P4-S037/P4-S038 backward prices, and general compiler lines are not reopened.

**Stopping point.** Established: exact four-computation normal form for the eight-corner partial clock; a source-specific total Y-computable target-runtime function with no computable eventual domination; a fully specified legal four-run finite-window controller and exact capture criterion; and, under hypothetical X in OH, infinitely many policy-selected actual target computations beyond every given total computable q-tenure AFTER the final old sentinel. NOT established: a computable promptness/thickness principle for sigma, X in OH, X not in OH, R_2=OH or strictness of R_2 below OH.

PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. Phase 4 OPEN; Phase 5 CLOSED. No novelty, openness, prior-art, Gate-4, publication or outreach finding.

**Next P4-S056 bounded target.** Study whether the four-run minimum clock admits source-specific frequently prompt representatives on one controller's evolving fresh-block schedule despite hyperimmune full target runtimes. Seek a justified effective thickness principle, or a concrete obstruction specific to the committed M; do not mistake Theorem 6's necessary slow-trace law for a classification.
