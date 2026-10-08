# P4-S054 — actual autoreduction cube certificates and the source-specific latency law

Date: 2026-10-08
Session: P4-S054
Incoming authoritative main: 66da740a0132fd376d7d367e1dd26fb80cfa5e06
Scope: Phase 4 Mathematics only, selected CAND-01, source-specific effective capture after coded recoding.

Result: **The committed self-avoiding use-clipped wtt autoreduction forces a positive finite wrong-output certificate in every fully value-closed three-raw-bit cube formed by one old sentinel and the two future raw coordinates implementing a virtual unit flip. This is an actual M/Y/X law absent from the P4-S053 abstract publication calendar. The first-certificate clock is partial computable from the finite already-observed outside bits and is defined at every such state reached on X, but has no proved total computable upper bound. A computable finite-window cube controller is total, no-repeat, fair-coin preserving and globally one-hole, and a timely certificate licenses an exact 8/7 fair three-bit old-reset gain. Under hypothetical X in OH every computable member of this controller family has a final old sentinel and every later value-closed cube has a finite certificate clock strictly beyond its chosen finite protection tenure. Neither infinitely many timely old turnovers nor X in OH or R_2=OH is established.**

## 0. Authority, frozen mathematics, and exact scope

Live main matched the specified P4-S053 outgoing checkpoint, with no P4-S054 records before the write. Reviewed P4-S001–P4-S053 mathematics and the selected CAND-01 authority (P2-S001, P2-S003, candidates.json, P3-S008), the active post-S031 pivot and the later mathematical chain, especially P4-S008, P4-S011, P4-S012, P4-S027 and P4-S044–P4-S053. No earlier validated mathematics is changed.

Retain the committed computably random Y, syntactically self-avoiding globally use-clipped wtt autoreduction M, M^Y(n)=Y(n) for all n, and the blockwise computable fair-coin homeomorphism H with X=H^{-1}(Y) in CR. H(X)=Y is not in OH. Retain precisely
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]
Both X in OH and R_2=OH remain unresolved.

A finite WRONG/NONBINARY halt under a synthetically completed raw oracle is a positive certificate only when its other accessed raw values have been genuinely exposed, and the simulated input/output equation is checked against that same synthetic completion. Off-target silence, timeout, nontermination and clipping abandonment are never certificates. A target-correct run of M on Y is the sole source-specific premise used below.

## 1. Exact recoding and forced virtual-unit-flip witness

The committed three-bit recoding on block B_b={3b,3b+1,3b+2} is
\[
(u_0,u_1,u_2)=(x_0\oplus x_2,\ x_0\oplus x_1,\ x_0\oplus x_1\oplus x_2).
\]
Thus the RAW pair (t,u)=(3b,3b+1) has difference vector (1,1,0), carried by H to virtual unit vector (1,0,0). In particular, for q=3b,
\[
H(X\oplus e_t\oplus e_u)=Y\oplus e_q.
\]
The third raw coordinate v=3b+2 is unchanged. The old sentinel s is required to lie outside B_b.

Let U(q)>0 be the strict total computable wtt cap of the committed P4-S027 normalization: a halting M-computation on the source Y at input q uses only virtual coordinates below U(q), never queries q, and the clipped program abandons any out-of-cap query on a sibling oracle. Define the computable raw frontier
\[
V(q)=3\left\lceil U(q)/3\right\rceil.
\]
Every raw bit needed to answer any permitted M(q) virtual query is below V(q). If U(q) is smaller than q+1, this formula still works; v must separately be read to compute the expected virtual q-bit of each candidate.

Fix any finite scan state on X with a still unread old s, and pick any completely fresh B_b disjoint from the old block. Keep s,t,u unread. First read v, and then actually read every still unqueried raw coordinate r<V(q) except s,t,u, at ZERO stake. Values already recorded are reused. This is a finite total *value-closure phase*: afterward all eight raw counterfactual completions (s=a,t=beta,u=gamma), a,beta,gamma in {0,1}, have fully specified virtual oracle answers at every coordinate M(q) can request. These finite tables and their expected q-th virtual values can be computed from the observed transcript with synthetic protected bits. No actual protected bit has been read.

For such a value-closed transcript p, define the partial computable integer
\[
\sigma(p)=\min\{r\ge1:\hbox{within r steps of each of the eight clipped M(q) simulations, a wrong/nonbinary output is seen at some cube corner}\}.
\]
If no corner gives a wrong/nonbinary halt, sigma is undefined. This is a partial computable function of the FINITE OBSERVED transcript and the fixed M,H; it does not consult X, semantic shielding or the unread protected bits. A finite value-closed p may have no such certificate on a sibling source, so no totality assertion is made for arbitrary p.

**Theorem 1 (source-specific cube-certificate totality).** At EVERY value-closed p produced from the committed X as above, sigma(p) is finite. More concretely, writing a=X(s), beta=1-X(t), gamma=1-X(u), the cube corner (a,beta,gamma) has a finite wrong-output M(q) halt. Its simulated runtime is exactly the runtime T_Y(q) of M^Y(q), apart from a fixed implementation overhead in translating virtual queries. Thus sigma(p) is bounded by the finite simulation clock for that target computation once value closure is complete.

**Proof.** In this corner the old s retains its true value, the two future raw bits are jointly flipped, and every other raw coordinate is its actual X-value. Hence its virtual source is Y xor e_q. The target run M^Y(q) halts with output Y(q) and syntactically never queries q; therefore the same sequence of oracle replies and the same output occur when M(q) runs on Y xor e_q. At the counterfactual input oracle, however, the q-th virtual bit equals 1-Y(q), so this finite binary output is WRONG. The P4-S027 clip does not intervene on the target computation. Value closure ensures all real outside-support bits are already observed; the old and future protected replies are synthesized. Thus the wrong halt is visible in the symmetric eight-corner dovetail after finite computation, independent of whether the controller knows a,beta,gamma. QED.

This theorem is about the single virtual-unit-flip *pair* t,u, NOT about a flip of one raw future bit. A single raw coordinate changes two or three virtual coordinates and does not inherit automatic unit-flip refutation. Theorem 1 also does NOT assert a positive wrong-halt in each old row, any ordinary two-bit square Ref(s,t), or a computable halting-time bound as a function of b alone.

**Corollary 2 (partial clock versus computable value frontier).** Source-specifically, the finite value-closure transcript p always lies in the c.e. domain of sigma; one can compute sigma(p) by unbounded search after seeing p on X. This does NOT define an everywhere-total finite-tenure rule: on other finite transcript states the search can diverge, and a total scan cannot block fresh outputs while protecting three unread bits indefinitely. The explicit computable bound V(q) is a bound on VALUE DEPENDENCE, not on sigma or T_Y(q). The map q -> T_Y(q) is computable with oracle Y, but no ordinary computable upper bound or controller-available predictive bound is established. In particular the theorem supplies no fixed L(p) dominating sigma(p) on all source-reached states.

The positive result differs from P4-S053's arbitrary c.e. calendar: every actual X-value-closed cube has at least one concrete M-witness. It does not refute that calendar's *timing* obstruction, since the present certificate still may appear after every prescribed finite protection deadline.

## 2. One cube exclusion and exact fair 8/7 old-reset wager

A positive wrong-output certificate in any of the eight cube corners (a,beta,gamma) rules out precisely that triple for X, independently of semantic old shielding. Treat all other triples as potentially possible. Starting with rational capital C>=0, define the terminal payoff on the next three raw bits, queried in order s,t,u, to be ZERO on the excluded triple and 8C/7 on each of the other seven triples.

**Theorem 3 (minimal cube flat hedge).** This terminal payoff is implemented by the following nonnegative, exact FAIR successive conditional expectations, with ALL three raw coordinates still unread at the first wager:
- On querying s, child capital is 6C/7 for s=a and 8C/7 for s=1-a.
- Given s=a, querying t gives 4C/7 for t=beta and 8C/7 for t=1-beta; given s!=a both children equal 8C/7.
- Given s=a,t=beta, querying u gives 0 for u=gamma and 8C/7 for u=1-gamma; at all other nodes the u children both equal 8C/7.

Every parent equals the arithmetic mean of its two children: (6+8)/14=1 at the root; (4+8)/14=6/7 and (0+8)/14=4/7 at the relevant children. The terminal average is (7*(8/7)+0)/8=1. The actual cube on X cannot be the positively refuted triple, so the completed wager multiplies C by 8/7. It consumes old s, t and u; it is NOT a reset-free hedge. No extra certificate is needed, but the gain 8/7 is smaller than the P4-S050 two-bit 4/3 where a pair, rather than a triple, has been eliminated. This is an effective *local* success, not a claim of infinitely many successes.

## 3. Fully computable finite-window cube scan

Fix ANY total computable positive integer tenure functional L(e,k,p) depending only on the finite observed state after value closure, epoch e and reservation k. For definiteness L=2^(e+k+4) is one valid member. Define S^cube_L and its output martingale d^cube_L as follows.

At the start of epoch e select old s as least unread raw coordinate. For reservation k choose the least-indexed ENTIRELY UNREAD block B_b not containing s. Name t=3b, u=3b+1, v=3b+2, q=3b. Protect s,t,u. Query v at zero stake, then query each as-yet unread r<V(q) outside {s,t,u} exactly once at zero stake. These finite mandatory reads close the value frontier on EVERY transcript; none waits for M. Keep all queried bits in a finite transcript table. Calculate the finite total tenure L(e,k,p) from this p.

For r=1,...,L: run from scratch r bounded machine steps of each of the eight clipped M(q) corner computations using the finite value-closed table, and check positive wrong/nonbinary halts BEFORE the next real query. If the first such event is found, execute Theorem 3's fair s,t,u wager, release all three, and start epoch e+1. If not, emit ONE zero-stake least-unread raw coordinate outside {s,t,u}. If all L rounds expire without a positive certificate, query t then u at zero stake (mandatory future releases), keep old s unread, and proceed to reservation k+1. The mandatory finite value-closure and ordinary rounds never protect any future beyond its own finite tenure. No s reset occurs on timeout. All local event priority, block choice, and simulation rules are fixed and computable; no X bit or trap flag occurs in the code. The controller is the same code on every binary source.

**Theorem 4 (global legality and exact finite trace criterion).** For every such L, S^cube_L is an everywhere-total computable adaptive no-repeat scan, fair-coin preserving and with every fibre of cardinality <=2. The martingale d^cube_L is total computable, rational-valued, nonnegative and fair at every output prefix. The event of a profitable completed cube turnover is mechanically checkable from one finite transcript: the stored original p, the finite halting record for a wrong cube corner found at some r<=L BEFORE release, the actual queried s,t,u, and the fair child-capital ledger.

**Proof.** Every finite frontier sweep uses at most V(q) raw queries; every r-simulation is bounded and terminates; any missing zero-stake next coordinate can be found by a least-unread search outside a finite protected set. t,u are mandatorily read at a finite timeout or event, and all queries are fresh. If only finitely many successful resets occur, the last s stays unread and the repeated least-unread sweep, closure reads and compulsory future releases eventually consume every other coordinate. If infinitely many resets occur, each consumes the then least unread s; strictly increasing least-unread sentinels exhaust all coordinates. Thus every transcript omits at most one source coordinate. Query choice is a total computable function of earlier output bits and each new query is fresh, so every output cylinder of length m has preimage fair measure 2^{-m}; fibres correspond to assignments of the at-most-one omitted coordinate. A positive wrong halt is used only to SELECT a strategy; the stated capital transitions are fair at both children even on off-target inputs where the asserted exclusion might fail. Zero wagers keep both children equal. QED.

**Theorem 5 (source-specific exact window dichotomy).** For a reservation reaching value-closed p on X, the controller executes the fair 8/7 old turnover in this reservation IF AND ONLY IF sigma(p)<=L(e,k,p). If sigma(p)>L(e,k,p), it releases both future bits at zero stake; nevertheless sigma(p) is a finite positive actual-M clock by Theorem 1. If successful reservations are reached at every consecutively renewed epoch (equivalently there are infinitely many successful old turnovers), then completed capital after m turnovers is (8/7)^m and X is not in OH.

**Proof.** After value closure all eight corner computations have all permitted answers and are run for r steps at round r, with a check before each timeout. The first wrong-halt detection therefore occurs exactly at round sigma(p) if it lies within the tenure; otherwise no positive cube exit is executed. After any timely detection the hedge is correct on X by soundness and Theorem 3. The global scan is in the defining OH subclass by Theorem 4. Infinite completed successful epochs produce unbounded capital. QED.

This is strictly a source-specific forced-existence result plus a CONDITIONAL timely-capture statement; no theorem guarantees that even one L chosen without X advice catches infinitely many renewed epochs.

## 4. A sharper necessary latency obstruction under hypothetical X in OH

**Theorem 6 (every total window must eventually outrun its own finite source witnesses in the wrong direction).** Assume, only for this theorem, X in OH. Fix ANY total computable tenure functional L and the corresponding S^cube_L. Its run on X has finitely many successful old turnovers. It therefore has a final permanent old sentinel s and infinitely many subsequent reservations k. For EVERY reservation in that final epoch, after deterministic source-value closure at its p_k,
\[
\boxed{L(e,k,p_k)<\sigma(p_k)<\infty.}
\]
In particular none of these permanently late certificates can be attributed to a missing oracle VALUE: every raw bit in the strict computable use cap has already been exposed or synthesized BEFORE L starts. They are pure finite-simulation latency beyond this scheduler's budget. The hidden actual bit at s is never used in L.

**Proof.** If there were infinitely many successful turnovers the total one-hole scan/martingale would destroy CR at X, contradicting X in OH. Every turnover is successful and each reset is success-gated, hence after finitely many resets the last s persists. Every failed reservation terminates in finite time and the next reservation begins, giving infinitely many p_k. By Theorem 1 each sigma(p_k) is finite. By Theorem 5 a reservation with sigma<=L would be a successful turnover; none occurs in the final epoch. Therefore sigma>L at every one. QED.

This is a necessary condition on a hypothetical OH-robust X, not a demonstration that it holds or that X is OH-robust. It is stronger than the P4-S053 abstract late-publication model in one precise sense: the positive certificate is FORCED BY THE ACTUAL M and has a fixed, computably exposed finite use footprint at every reservation. It does not produce a computable stage modulus, because the finite halting clock can still outrun every chosen total computable finite tenure on a particular sequence of source-reached states.

The theorem does not say that sigma lacks any total computable extension on arbitrary state sets, nor that a target trace can be delayed arbitrarily by changing only runtime without changing M. It says exactly what hypothetical X in OH would require of EVERY stated computable policy. If X is outside OH, that hypothesis fails for at least one one-hole scan, but not necessarily for this specific cube family.

## 5. Geometry, retained restrictions, and next test

- The forced cube certificate is at the virtual UNIT flip implemented by TWO raw future bits, not an ordinary single-future square. Opposed-old-row exclusions are NOT automatic, so the P4-S051 reset-free 4/3 escrow criterion is not recovered. A three-bit 8/7 old-reset hedge consumes s; it cannot finance infinitely many gains against a single permanent s.
- The P4-S049/P4-S052 shielded-old premise is semantic. This cube theorem neither recognizes a shielded epoch nor gives a shielded 8/3 old orientation. At a shielded old row the true old branch still supplies the unit-flip mismatch; the false old row can remain divergence-only.
- The old/future three-coordinate protection is only finite on all continuations. No transcript leaves two future targets permanently unread. A universal all-transcript old-reset guarantee would instead collapse to the P4-S053/P4-S001 computable isomorphism and cannot be inferred from source-specific sigma totality.
- The P4-S008 fixed-sentinel restriction remains intact. All claims of success require infinitely many ACTUALLY EXECUTED old turnovers, not eventual off-line receipts.
- Nothing changes any P4-S001–P4-S053 proof or the CAND-01 finite-cardinal-fibre definition. The ticket/frontier, backward-price and general compiler routes remain frozen.

**Validated stopping point.** Established: a genuinely M/Y/X-specific positive finite cube-witness theorem, a partial computable certificate clock from value-closed finite transcript, an exact 8/7 fair three-coordinate old-reset hedge, a globally legal finite-window success-gated scan, its exact finite trace/clock success criterion, and an algorithm-relative necessary pure-latency condition under hypothetical X in OH. NOT established: a total computable source-independent domination of sigma, infinitely many successful turnovers, X in OH, X not in OH, OH non-invariance, R_2=OH or R_2 proper-subset OH.

PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made. Phase 4 OPEN; Phase 5 CLOSED.

**P4-S055 bounded target:** test whether the *source-reached* c.e. domain/clock sigma from the value-closed forced M-cube can be furnished with a total computable upper bound on a legally reachable infinite sequence of renewed epochs, or prove a sharper source-specific obstruction to any such bound. Do not confuse a partial on-target search with an everywhere-total scheduler or infer a timely gain merely from virtual unit-flip certainty.
