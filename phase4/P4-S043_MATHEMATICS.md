# P4-S043 — asynchronous one-role extraction and the recurrent-selector obstruction

Date: 2026-10-07
Session: P4-S043
Incoming checkpoint: 9027605cad65de83cca6ae23e7986cf41ceb9424
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding
Result: **THE P4-S040 ALL-THREE SYNCHRONIZATION IS NOT NECESSARY. FOR ANY COMPUTABLE ONLINE CHOICE OF ONE RAW ROLE, THERE IS A TOTAL COMPUTABLE NO-REPEAT ONE-HOLE SCAN WHICH CLOSES IMMEDIATELY ON ITS OWN POSITIVE CASE-A OR CASE-B CERTIFICATE, RESTORES A FRESH BLOCK BOUNDARY, AND NEVER WAITS FOR THE OTHER TWO DIRECTIONS. IF THE CHOSEN ROLE IS CASE A INFINITELY OFTEN AND IS NEVER TRAPPED BY CASE C, THE ASSOCIATED MARTINGALE SUCCEEDS. HOWEVER RECURRENT NONTRIPLE CASE C DOES NOT SUPPLY A COMPUTABLE CHOICE OF SUCH A ROLE. THE P4-S041 PAIRWISE IMPLICATIONS ARE THE COMPLETE LOCAL A/B/C LAW: EXACTLY 14 STATUS TRIPLES ARE REALIZABLE. FOR EACH FIXED RECURRENT C DIRECTION, A COMPUTABLE FINITE-USE SELF-AVOIDING STRUCTURAL COUNTERMODEL CAN PRESENT ONLY NONTRIPLE C/A PATTERNS AND STILL TRAP EVERY MEMBER OF ANY PRESCRIBED FINITE FAMILY OF WAIT-FOR-OWN-STATUS ROLE POLICIES. FORCING FINITE-TIME ABANDONMENT REMOVES THE TRAP ONLY BY MAKING THE SCAN EXHAUSTIVE, HENCE k=1 AND COMPUTABLE-RANDOMNESS PRESERVING. THUS GLOBAL RECURRENCE OF VISIBLE CASE-A WITNESSES IS NOT THE SAME AS SCAN-REACHABLE RECURRENCE. P4-S043 DOES NOT FORCE RECURRENT TRIPLE CASE C AND DOES NOT DECIDE WHETHER THE COMMITTED X LIES IN OH.**

## Authority, uniqueness and scope

Immediately before substantive work, live main was exactly

\[
\texttt{9027605cad65de83cca6ae23e7986cf41ceb9424},
\]

the final P4-S042 outgoing checkpoint. Repository search and direct path checks found no P4-S043 mathematics, validation or close record, so P4-S043 was unused.

P4-S001 through P4-S042, the selected CAND-01 authority, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, and P4-S032 through P4-S042 were read. Special attention was given to P4-S011, P4-S012 and P4-S039 through P4-S042.

All validated mathematics through P4-S042 is frozen. The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence, P4-S037/P4-S038 backward-price route, ordinary raw-martingale compilation, ambiguity mass and general radius-one totalization are not reopened.

Retain

\[
R_2=\{x\in CR:\text{every total computable fair-coin-preserving global-}k=2\text{ map sends }x\text{ to }CR\},
\]

\[
OH=\{x\in CR:\text{every total computable adaptive no-repeat one-hole scan sends }x\text{ to }CR\},
\]

and

\[
OH^{iso}=\{x\in CR:\text{every computable fair-coin-preserving homeomorphism }H\text{ sends }x\text{ into }OH\}.
\]

The retained inclusions remain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Let \(Y\) be the settled P4-S011 computably random wtt-autoreducible source, \(M\) its committed syntactically self-avoiding wtt autoreduction, \(D\) its one-hole destroyer, and

\[
X=H^{-1}(Y)
\]

under the repeated three-bit recoding

\[
u_0=x_0\oplus x_2,\qquad
u_1=x_0\oplus x_1,\qquad
u_2=x_0\oplus x_1\oplus x_2.
\]

Write

\[
A=
\begin{pmatrix}
1&0&1\\
1&1&0\\
1&1&1
\end{pmatrix},
\qquad
c_0=111,\quad c_1=011,\quad c_2=101.
\]

Retain

\[
X\in CR,\qquad H(X)=Y\notin OH.
\]

The missing source-side statement remains whether \(X\in OH\).

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## 1. The exact local status law

Fix a raw block \(B=\{q_0,q_1,q_2\}\), write the actual virtual block as \(v\), and let

\[
Z_i=Y[B\leftarrow v+c_i].
\]

The local direction status is:

- Case A if one of the three local equations halts wrong or nonbinary;
- Case B if all three halt with the companion's assigned bits;
- Case C if no local equation gives a finite refutation and at least one required equation diverges.

P4-S041 gives

\[
B_0\Rightarrow A_1,A_2,\qquad
B_1\Rightarrow A_0,\qquad
B_2\Rightarrow A_0.
\]

These implications are not merely necessary. At the level of a syntactically self-avoiding finite local table they are complete.

### Proposition 1 — exactly 14 local status triples are realizable

The realizable triples \((s_0,s_1,s_2)\in\{A,B,C\}^3\) are exactly

\[
\begin{array}{ccccccc}
AAA,&AAB,&AAC,&ABA,&ABB,&ABC,&ACA,\\
ACB,&ACC,&BAA,&CAA,&CAC,&CCA,&CCC.
\end{array}
\]

Equivalently, the only exclusions are those forced by

\[
B_0\Rightarrow A_1,A_2,\qquad
B_1\Rightarrow A_0,\qquad
B_2\Rightarrow A_0.
\]

#### Proof

It remains only to show realizability.

Take target block \(000\). Let the three local self-avoiding partial tables be

\[
f_0(u_1,u_2),\qquad
f_1(u_0,u_2),\qquad
f_2(u_0,u_1),
\]

with

\[
f_0(00)=f_1(00)=f_2(00)=0
\]

so the target equations are correct.

Write

\[
a=f_0(11),\quad b=f_1(11),\quad c=f_1(01),\quad d=f_2(01),
\]
\[
e=f_0(01),\quad f=f_2(10),\quad g=f_2(11),
\]

where \(\uparrow\) denotes divergence.

The three companions are

\[
111,\qquad011,\qquad101.
\]

Direction \(0\) tests \((a,b,g)\) against \(111\), direction \(1\) tests \((a,c,d)\) against \(011\), and direction \(2\) tests \((e,b,f)\) against \(101\).

The following assignments realize all 14 triples:

\[
\begin{array}{c|ccccccc}
(s_0,s_1,s_2)&a&b&c&d&e&f&g\\ \hline
AAA&0&0&0&0&0&0&0\\
AAB&0&0&0&0&1&1&0\\
AAC&0&0&0&0&1&\uparrow&0\\
ABA&0&0&1&1&0&0&0\\
ABB&0&0&1&1&1&1&0\\
ABC&0&0&1&1&1&\uparrow&0\\
ACA&0&0&1&\uparrow&0&0&0\\
ACB&0&0&1&\uparrow&1&1&0\\
ACC&0&0&1&\uparrow&1&\uparrow&0\\
BAA&1&1&0&0&0&0&1\\
CAA&1&1&0&0&0&0&\uparrow\\
CAC&1&\uparrow&0&0&1&1&1\\
CCA&\uparrow&1&1&1&0&0&1\\
CCC&\uparrow&\uparrow&1&1&1&1&1
\end{array}
\]

Direct inspection gives the claimed statuses. Every table is finite-use and syntactically self-avoiding. ∎

Thus no additional local A/B/C implication is available merely from self-avoidance and the three recoding columns.

## 2. Exact fixed-C pattern lists

Proposition 1 gives the requested classification.

### Direction \(0\) is Case C

If \(C_0\) holds, neither \(B_1\) nor \(B_2\) is possible because either would force \(A_0\). Also \(B_0\) is excluded by \(C_0\).

Hence the only patterns are

\[
(C,A,A),\qquad
(C,A,C),\qquad
(C,C,A),\qquad
(C,C,C).
\]

Every nontriple \(C_0\)-block therefore has Case A in direction \(1\) or direction \(2\), and no Case B occurs anywhere on such a block.

### Direction \(1\) is Case C

\(B_0\) is impossible because \(B_0\Rightarrow A_1\). Direction \(2\) may be B only when direction \(0\) is A.

The exact patterns are

\[
(A,C,A),\qquad
(A,C,B),\qquad
(A,C,C),\qquad
(C,C,A),\qquad
(C,C,C).
\]

In particular

\[
C_1\wedge B_2
\]

forces exactly the visible pattern

\[
(A,C,B).
\]

Every nontriple \(C_1\)-block has a Case-A direction: either \(A_0\) or \(A_2\).

### Direction \(2\) is Case C

Symmetrically the exact patterns are

\[
(A,A,C),\qquad
(A,B,C),\qquad
(A,C,C),\qquad
(C,A,C),\qquad
(C,C,C).
\]

In particular

\[
C_2\wedge B_1
\]

forces exactly

\[
(A,B,C).
\]

Every nontriple \(C_2\)-block has \(A_0\) or \(A_1\).

### Pigeonhole guard

If \(C_i\) occurs on infinitely many raw blocks, finite pigeonhole implies that at least one pattern in the corresponding finite list occurs infinitely often.

If triple C occurs only finitely often among those blocks, at least one nontriple pattern recurs, hence at least one named Case-A direction occurs infinitely often **as a raw-block property**.

This statement alone says nothing yet about whether a fixed computable scan reaches infinitely many of those blocks.

## 3. The all-three synchronization in P4-S040 is unnecessary

P4-S040 synchronized three raw scans until all three local statuses were visible. That is stronger than required for a scan which cares only about its own sentinel.

Let a **role policy** be a total computable rule \(\pi\) which, at the start of a fresh target epoch, chooses one local raw role

\[
i\in\{0,1,2\}
\]

from the finite scan transcript accumulated before opening the block.

### Theorem 2 — asynchronous one-role extraction

For every computable role policy \(\pi\) there is a total computable adaptive no-repeat raw one-hole scan \(S_\pi\) and a computable output martingale \(d_\pi\) with the following target behavior.

At the start of an epoch, let \(i=\pi\) be the selected role and let \(B\) be the first completely fresh block above the scan's restored queried prefix.

1. \(S_\pi\) withholds \(x_i^{(B)}\) and queries the other two raw coordinates of \(B\) at zero stake.
2. It dovetails the local computations for the two raw completions compatible with those two observed bits.
3. If one completion gets a finite wrong/nonbinary refutation, \(S_\pi\) predicts that the other completion is the target value, bets all current capital on the sentinel accordingly, and queries the sentinel immediately.
4. If both completions become locally accepted, \(S_\pi\) places zero stake and queries the sentinel immediately.
5. It does **not** wait for the status of either unselected raw direction.
6. After closing the sentinel, it consumes at zero stake every already exposed coordinate needed to restore a complete raw prefix through a block boundary and starts the next fresh block.
7. While its own pair is unresolved, it continues a least-fresh background sweep outside the sentinel while dovetailing the two local simulations.

On the actual \(X\):

- selected Case A gives a correct all-in wager;
- selected Case B gives zero stake and immediate restart;
- selected Case C never supplies either positive resolution and is therefore an absorbing target epoch.

If the target run completes infinitely many epochs and the selected role is Case A on infinitely many completed epochs, then \(d_\pi\) succeeds on \(S_\pi(X)\), hence

\[
X\notin OH.
\]

#### Proof

The two candidate block values are finite hypotheses, so all inside-block oracle questions are answered from the hypothesis. Outside-block virtual queries are answered by exposing fresh raw support coordinates. The wtt use bound makes each positive acceptance or refutation witness finite, but no bound on its time is needed.

On \(X\), the actual completion is never finitely refuted. Hence a finite refutation of one endpoint certifies the other endpoint's sentinel bit correctly. If the companion is Case B, both endpoints are eventually accepted. If it is Case C, after the actual endpoint is accepted the companion is neither accepted nor finitely refuted, so the selected race never resolves.

The scan never stops producing output. On an unresolved epoch the least-fresh sweep eventually queries every raw coordinate other than the current sentinel, so the resulting complete transcript has exactly one hole. If an epoch resolves, the sentinel is consumed. The restoration sweep makes the next target block completely fresh and, on an infinite sequence of completed epochs, drives the queried prefix to infinity.

Thus every complete transcript omits at most one raw coordinate. No coordinate is repeated, and the next query is computable from the finite transcript. Hence \(S_\pi\) is an everywhere-total computable adaptive no-repeat one-hole scan.

The martingale holds on all fillers and Case-B sentinels and bets all capital only on positively certified Case-A sentinels. Every such target wager is correct. Infinitely many such wagers therefore give unbounded capital. ∎

### Corollary 3 — exact necessary online obstruction under \(X\in OH\)

If \(X\in OH\), then for every computable role policy \(\pi\), its asynchronous target run has one of the following two behaviors:

1. it eventually selects a Case-C direction and thereafter stays in that absorbing epoch; or
2. it completes infinitely many epochs but selects Case A only finitely often.

This is an online statement about the blocks actually reached by that policy. It is stronger than P4-S040 as scan geometry, but weaker than a statement about all raw blocks.

## 4. Why global recurrence does not imply scan-reachable recurrence

Suppose a fixed direction \(i\) is Case C on infinitely many raw blocks and a nontriple \(C_i\)-pattern recurs infinitely often. Section 2 then supplies an infinite raw set of visible Case-A witnesses in one or more other directions.

Theorem 2 does not automatically harvest them.

There are two distinct reasons.

### 4.1 A selected Case C is absorbing

A role must be chosen before its own A/B certificate is known. If the selected role is C, the scan cannot positively discover that fact and switch later. It continues querying all other coordinates forever with the current sentinel as its one permitted permanent hole.

Thus a fixed direction-\(j\) scan can be stopped by one \(C_j\)-block before arbitrarily many later \(A_j\)-blocks.

### 4.2 The scan chooses an endogenous fresh-block subsequence

To resolve one local status, the wtt computations may request virtual information from later blocks. The scan answers those requests by exposing raw support there.

After a positive A/B resolution it must restore a completely fresh boundary above the coordinates already consumed. The next target block is therefore determined by the scan's own finite evaluation footprint, not by the ambient raw-block order.

Consequently

\[
A_j\text{ on infinitely many raw blocks}
\]

does not imply

\[
A_j\text{ on infinitely many blocks reached by a fixed direction-}j\text{ scan}.
\]

The scan may consume some A-bearing blocks as zero-stake support before they ever become sentinel blocks.

This is the exact recurrence/interleaving obstruction requested by the session. Finite pigeonhole identifies a recurrent raw status pattern; it does not compute a member of the scan's reached subsequence on which that pattern recurs.

## 5. Finite-time abandonment collapses to the safe \(k=1\) regime

One obvious repair is to refuse to wait forever: after some computably determined finite amount of unresolved search, close the sentinel at zero stake and move on.

That removes the absorbing C trap, but it also removes the one-hole resource.

### Theorem 4 — total abandonment makes the role scan exhaustive

Consider any variant of the Theorem 2 architecture with the following property:

> on every source transcript and in every epoch, the current sentinel is eventually queried after a finite computable interaction, whether or not an A/B certificate appears.

Assume the same prefix-restoration rule after each closure.

Then every complete transcript queries every raw coordinate exactly once. The scan is an effective adaptive permutation and therefore preserves computable randomness.

In particular it cannot destroy the already settled

\[
X\in CR.
\]

#### Proof

Every epoch closes its sentinel. Prefix restoration then increases the completely queried raw prefix through another block boundary. Since this happens forever on every infinite transcript, every coordinate is eventually queried. No-repeat gives an adaptive permutation.

As in the settled k=1 theory, the inverse reconstructs source coordinate \(n\) by simulating the output transcript until the scan asks for \(n\). This halts for every \(n\), so the scan is an effective fair-coin isomorphism and preserves computable randomness. ∎

Thus a computable finite deadline, growing timeout, deterministic finite abandonment schedule or any other rule which guarantees eventual closure on every branch cannot by itself produce the required destroyer.

The destroyer must retain at least one branch on which a sentinel can remain permanently omitted. Case C is exactly able to occupy that branch.

This is the same one-hole resource identified earlier, now expressed as the obstruction to asynchronous role switching.

## 6. Exact finite-family obstruction for wait-for-own-status scans

The preceding discussion could still leave hope that a fixed finite family of Theorem 2 role policies covers all nontriple recurrent patterns.

It does not.

### Theorem 5 — nontriple recurrent C can trap every prescribed finite wait-family

Fix a recurrent direction \(i\in\{0,1,2\}\). Let

\[
\pi_1,\ldots,\pi_m
\]

be any prescribed finite family of computable role policies used in the exact wait-for-own-status architecture of Theorem 2.

There is a computable syntactically self-avoiding finite-use functional \(N\) with computable target

\[
Y_*=0^\omega
\]

such that:

1. direction \(i\) is Case C on every raw block;
2. triple Case C occurs on no block;
3. every block has at least one Case-A direction;
4. every scan in the prescribed finite family eventually selects a Case-C direction and is trapped after only finitely many completed epochs.

This is a structural countermodel only. The target \(0^\omega\) is not computably random.

#### Construction for \(i=0\)

Use only the two realizable patterns

\[
(C,C,A)
\]

and

\[
(C,A,C).
\]

Both have \(C_0\), neither is triple C, and each has one visible A role among \(1,2\).

At the next block, compute the current role chosen by every still-active policy from its already determined finite all-zero transcript.

- If at least one active policy chooses role \(1\), assign pattern \((C,C,A)\). Every active policy choosing \(0\) or \(1\) is trapped; role \(2\) sees A and may continue.
- If none chooses role \(1\), assign pattern \((C,A,C)\). Then every active policy, which chooses only \(0\) or \(2\), is trapped.

At least one active policy is removed at each stage. Hence after at most \(m\) such blocks all members are trapped. Continue with either pattern forever.

The status choice is computable because each policy chooses its role before the current block's status is opened and all earlier block gadgets are already fixed.

#### Construction for \(i=1\)

Use only

\[
(C,C,A)
\]

and

\[
(A,C,C).
\]

The first traps roles \(0,1\) and lets role \(2\) see A; the second traps roles \(1,2\) and lets role \(0\) see A. The same finite elimination argument applies.

#### Construction for \(i=2\)

Use only

\[
(C,A,C)
\]

and

\[
(A,C,C).
\]

Again the same finite elimination argument applies.

#### Realizing the block patterns

The local table in Proposition 1 already gives finite self-avoiding realizations:

\[
(C,C,A):
\quad
(a,b,c,d,e,f,g)
=
(\uparrow,1,1,1,0,0,1),
\]

\[
(C,A,C):
\quad
(a,b,c,d,e,f,g)
=
(1,\uparrow,0,0,1,1,1),
\]

\[
(A,C,C):
\quad
(a,b,c,d,e,f,g)
=
(0,0,1,\uparrow,1,\uparrow,0).
\]

Apply the chosen local table independently in each three-bit block; on all other inputs output \(0\). This gives one computable finite-use syntactically self-avoiding functional correct on \(0^\omega\). ∎

### Consequence 6 — recurrent triple C is not forced by the tested geometry

The following implication is **not** justified by P4-S041/P4-S042 status information plus the finite-family wait-for-own-status scans:

\[
X\in OH
\Longrightarrow
\text{triple Case C occurs infinitely often}.
\]

Theorem 5 does not refute that implication for the committed computably random source. It proves that any proof of it must use source-specific structure beyond:

- the pairwise status law;
- recurrence of one fixed C direction;
- the existence of a visible A direction on every nontriple block;
- and a fixed finite family of asynchronous wait-for-own-status role scans.

The new missing resource is a computable **online selector/reachability principle**.

## 7. The special \(C_0\) regime

When \(C_0\) recurs, Case B is absent in every direction on those blocks.

The nontriple patterns are

\[
(C,A,A),\qquad
(C,A,C),\qquad
(C,C,A).
\]

Thus finite pigeonhole does imply that if nontriple \(C_0\)-blocks occur infinitely often, then either \(A_1\) or \(A_2\) occurs on infinitely many such raw blocks.

The missing step is exactly the one identified in Section 4.

A direction-\(1\) scan may be trapped by one earlier \(C_1\)-block; a direction-\(2\) scan may be trapped by one earlier \(C_2\)-block. Independent schedules do not repair this automatically, because each schedule chooses its next fresh block only after consuming its own finite evaluation footprint.

Theorem 5 shows that even in the idealized local-use setting, a finite family of pure wait policies can be alternately trapped by the two legal patterns

\[
(C,C,A),\qquad(C,A,C)
\]

without ever using triple C.

Therefore the two-role \(C_0\) structure gives a clean asynchronous scan theorem but not a rate-free extraction theorem.

## 8. Recurrent \(C_1\) and \(C_2\)

The same conclusion holds in the two asymmetric cases.

### \(C_1\) with \(B_2\)

The status is exactly

\[
(A,C,B).
\]

A role-\(0\) Theorem 2 scan which reaches such a block sees a finite Case-A certificate, makes a correct sentinel wager, closes immediately and restarts. It does not need \(C_1\) to resolve and does not need to wait for the visible \(B_2\) certificate.

A role-\(2\) scan may also close at zero stake once \(B_2\) is visible.

What is not proved is that one fixed role-\(0\) scan reaches infinitely many raw blocks of this pattern before a selected \(C_0\) trap or before its support evaluation consumes those blocks as fillers.

### \(C_2\) with \(B_1\)

Symmetrically the status is

\[
(A,B,C).
\]

A reached role-\(0\) block is immediately harvestable, but global recurrence does not imply scan-reachable recurrence.

### Mixed A/C patterns

For recurrent \(C_1\), the difficult mixed patterns include

\[
(A,C,C),\qquad(C,C,A).
\]

For recurrent \(C_2\), they include

\[
(A,C,C),\qquad(C,A,C).
\]

These are exactly the patterns used by the finite-family countermodel. They expose one visible A role while making another role absorbing.

Thus the asymmetric Case-B companions do not remove the selector obstruction.

## 9. Temporary parallelism does not silently create a second permanent hole

One might run several c.e. status searches in parallel on different prospective sentinels.

Temporary unread coordinates are not forbidden at a finite stage. The restriction concerns complete transcripts.

However P4-S040's one-hole geometry remains decisive: if one candidate sentinel may stay unread forever, every other coordinate must eventually be consumed on that branch. Hence two independent unbounded status searches cannot both keep their own sentinels permanently available.

Any parallel protocol must eventually do one of two things:

1. positively resolve one search and close the other sentinels; or
2. consume all but one unresolved sentinel without positive status information.

The second arm is again an abandonment step and can discard an arbitrarily late Case-A witness. If every unresolved sentinel is always eventually abandoned, Theorem 4 returns the construction to the exhaustive k=1 regime.

No stronger impossibility claim for every conceivable adaptive protocol is made. This section records the exact geometric obstruction faced by the tested finite parallelizations.

## 10. Triple C is therefore not activated in P4-S043

P4-S041 remains available:

\[
C_0\wedge C_1\wedge C_2
\]

gives the shared local divergences

\[
M^{Z_0}(q_0)=M^{Z_1}(q_0)\uparrow,
\]

and

\[
M^{Z_0}(q_1)=M^{Z_2}(q_1)\uparrow.
\]

P4-S043 does not prove that triple C recurs infinitely often for a surviving \(X\in OH\).

Accordingly these shared divergences are not promoted to a cross-block resource here. Divergence remains negatively observable.

## 11. New exact boundary

P4-S043 separates three notions which had been conflated by the synchronized P4-S040 presentation.

### Local exploitability

If the selected direction is visibly A or B, the scan can close immediately and restart. No other status need resolve.

This is now solved by Theorem 2.

### Global raw-block recurrence

A fixed direction may have A, B or C on infinitely many raw blocks. Finite pigeonhole can identify a recurrent status pattern set-theoretically.

This does not identify the blocks reached by a fixed scan.

### Computable online reachability

A successful raw one-hole destroyer needs one computable policy whose **own reached blocks** avoid an absorbing selected C often enough and contain infinitely many selected Case-A certificates.

That is the remaining resource.

The structural obstruction can be summarized as:

> A/B certificates are positive but role choice precedes the relevant certificate. Waiting preserves the one-hole resource but lets C trap the scan. Guaranteed finite abandonment defeats C only by restoring exhaustive k=1 behavior. A finite family of pure waiting policies can be trapped by legal nontriple recurrent patterns.

This is a recurrence/interleaving and online-selection problem, not a new local effectivity problem.

## 12. Separation status

No total raw one-hole destroyer for the actual recoded P4-S011 source \(X\) is obtained unconditionally.

No proof of

\[
X\in OH
\]

is obtained.

No proof that recurrent triple Case C is necessary is obtained.

Therefore no OH non-invariance theorem and no strict inclusion

\[
R_2\subsetneq OH
\]

is claimed.

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

P4-S032 null-ambiguity preservation remains available and ambiguity mass is not reinstated as an invariant.

## 13. Exact next target

The next bounded problem is the **online selector / fresh-block reachability obstruction** exposed above.

P4-S044 should keep the asynchronous Theorem 2 and attack only the gap between raw-block recurrence and recurrence on a computable scan's own fresh-block sequence.

The natural objects are:

- for a target block \(B\), the finite raw support footprint consumed while positively resolving one chosen A/B status;
- the computable map from a completed epoch to the first completely fresh block above that footprint;
- computable role policies on these endogenously selected blocks;
- and transient multi-sentinel races which are allowed finitely but must leave at most one permanent hole on every complete transcript.

The bounded question is whether the actual wtt use structure supplies a computable selector/fresh-lane theorem strong enough to hit infinitely many nontriple A witnesses, or whether one can isolate an exact source-side obstruction in which every computable role policy is eventually C-trapped or skips the recurrent A-bearing blocks.

Do not return to the frozen bankroll line, backward-price normalization, ordinary raw-martingale compilation, ambiguity mass or general radius-one totalization.

## Guards

All validated mathematics through P4-S042 is preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged.

Phase 4 remains OPEN. Phase 5 remains CLOSED.

No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.
