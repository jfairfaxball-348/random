# P4-S044 — wtt value horizons, moving reservations and the fresh-target obstruction

Date: 2026-10-07
Session: P4-S044
Incoming checkpoint: dfd593bd3d0e2bc68d9b2e2097b31c5dbc443c17
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding
Result: **THE COMMITTED WTT USE BOUND COMPUTES A UNIFORM RAW VALUE HORIZON FOR EVERY LOCAL RAW-ADJACENT A/B/C TEST, BUT IT DOES NOT COMPUTE A FRESH-TARGET HORIZON. AFTER THE VALUE HORIZON IS EXHAUSTED, A/B STATUS NEEDS NO NEW SOURCE VALUES, YET ITS POSITIVE CERTIFICATE MAY APPEAR ARBITRARILY LATE. A GLOBALLY ONE-HOLE SCAN CANNOT BOTH KEEP THE CURRENT UNRESOLVED SENTINEL AND PROTECT A FIXED FUTURE SENTINEL UNTIL THAT UNBOUNDED CERTIFICATE ARRIVES: ON THE CASE-C CONTINUATION ONE OF THEM MUST BE CONSUMED AT FINITE TIME. THUS A FIXED PRECOMPUTED NEXT BLOCK MUST EITHER BE ABANDONED OR THE CURRENT SENTINEL MUST BE ABANDONED, AND THE ACTUAL NEXT TARGET REMAINS CERTIFICATE-TIME ENDOGENOUS. FINITE HORIZON LANES EXIST EXACTLY WHEN THE ASSOCIATED DEPENDENCY INTERVALS HAVE UNIFORMLY BOUNDED OVERLAP; A BARE COMPUTABLE WTT USE BOUND DOES NOT FORCE THIS, WHILE COUNTABLY MANY LANES DO NOT SUPPORT INFINITE PIGEONHOLE. ZERO-STAKE SUPPORT REUSE AND FINITE TRANSIENT MULTI-SENTINEL RACES DO NOT REMOVE THE SAME NO-RATE OBSTRUCTION. A COMPUTABLE FINITE-USE STRUCTURAL MODEL WITH UNBOUNDED HORIZON OVERLAP, RECURRENT NONTRIPLE C, AND VISIBLE A WITNESSES REALIZES THE FAILURE. NO CLAIM X IN OH OR X NOTIN OH IS OBTAINED.**

## Authority, uniqueness and scope

Immediately before substantive work, live main was exactly

\[
\texttt{dfd593bd3d0e2bc68d9b2e2097b31c5dbc443c17},
\]

the final P4-S043 repository tip, whose tip commit is P4-S043 record selector failures. The P4-S043 mathematics record identifies its incoming checkpoint as

\[
\texttt{9027605cad65de83cca6ae23e7986cf41ceb9424}.
\]

The Phase-4 directory at the pinned tip contains P4-S001 through P4-S043 and no P4-S044 mathematics, validation or close record. Repository search for P4-S044 returned no hit. Hence P4-S044 was unused.

P4-S001 through P4-S043 were read from the pinned committed state. The selected CAND-01 authority in phase2/candidates.json and phase2/P2-S001_DISCOVERY.md, the sustained pivot phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, and P4-S032 through P4-S043 were checked directly. Special attention was given to P4-S011, P4-S012, P4-S027 and P4-S039 through P4-S043.

All validated mathematics through P4-S043 is frozen. The P4-S015–P4-S031 bankroll line, P4-S037/P4-S038 backward-price route, ordinary raw-martingale compilation, ambiguity mass, general radius-one totalization and one-off remote-divergence localization are not reopened.

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

Let \(Y\) be the settled P4-S011 computably random wtt-autoreducible source, \(M\) its committed syntactically self-avoiding wtt autoreduction, \(D\) its one-hole destroyer, and let

\[
X=H^{-1}(Y)
\]

under the repeated three-bit recoding

\[
u_0=x_0\oplus x_2,\qquad
u_1=x_0\oplus x_1,\qquad
u_2=x_0\oplus x_1\oplus x_2,
\]

with

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

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. Phase 4 remains OPEN and Phase 5 CLOSED. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## 1. The exact computable value horizon

Use the P4-S027 harmless use-clipped normal form. Let \(u(n)\) be a computable wtt use bound for \(M(n)\), and fix a strict computable cap

\[
U(n)>u(n)
\]

such that the normalized machine never queries a virtual oracle coordinate greater than or equal to \(U(n)\). Attempting an out-of-cap query on a sibling simply makes that sibling computation permanently nontriggering. The target computation on \(Y\) is unchanged.

Index raw and virtual three-bit blocks by

\[
B_b=\{3b,3b+1,3b+2\}.
\]

Put

\[
V(b)=\max_{r<3}U(3b+r)
\]

and define the raw block horizon

\[
h(b)=\max\left\{b+1,\left\lceil \frac{V(b)}3\right\rceil\right\}.
\]

Equivalently, every virtual coordinate below \(V(b)\) is determined by raw coordinates in blocks strictly below \(h(b)\).

### Theorem 1 — uniform local value-horizon theorem

Fix a target block \(B_b\). For any raw direction \(i\), expose the two non-sentinel raw bits and consider the two affine raw completions. Across the two endpoints and the three local autoreduction equations there are six raw-adjacent endpoint computations

\[
M^{Y[B_b\leftarrow v]}(3b+r),\qquad r=0,1,2.
\]

Every oracle query made by any of these six computations, whether the computation later halts or diverges, is to a virtual coordinate below \(V(b)\). Therefore every outside-block source value ever needed by the local A/B/C test is determined by raw blocks below \(h(b)\).

In particular:

1. a finite Case-A refutation uses only raw values below the raw horizon \(3h(b)\), together with the finite endpoint hypothesis in the current block;
2. a finite Case-B certificate uses only those same raw values;
3. after all source values requested inside this finite horizon have been exposed, any later discovery of A or B depends only on additional machine simulation time, not on any future source bit;
4. divergence can nevertheless persist for infinite time.

The same source-value bound also covers the full finite family of local candidate computations at the block, because the input indices remain \(3b,3b+1,3b+2\).

#### Proof

The wtt cap depends only on the input index, not on the candidate oracle or on whether the computation halts. Hence every local input \(3b+r\) has all of its possible oracle queries below \(U(3b+r)\le V(b)\).

A virtual query in another block is answered by the three-bit raw recoding inside that same raw block. Every virtual coordinate below \(V(b)\) lies in a raw block below \(\lceil V(b)/3\rceil\le h(b)\).

Queries into the current candidate block are answered from the finite endpoint hypothesis and do not require querying the withheld raw sentinel. Therefore all genuine outside source values used by the local status test lie below the displayed raw horizon.

Once those finitely many source values have been fixed, continuing the simulations can reveal a late halt but cannot request a source value outside the cap. ∎

### Corollary 2 — value closure is not certificate-time closure

The wtt horizon removes the P4-S043 dependence of a positive A/B witness on arbitrarily remote **source values**.

It does not give any computable bound on when a positive A/B witness appears.

This is the same value/time distinction already visible in P4-S027: after the use frontier has been exhausted, trigger data are independent of future filler bits, but a delayed trigger can still appear after arbitrarily much computation.

## 2. Why a fixed fresh-block map is not obtained

One might now choose a computable block

\[
G(b)>h(b)
\]

and try to keep \(B_{G(b)}\) completely fresh while waiting for the selected role at \(B_b\) to resolve.

The value horizon is not enough for that.

### Theorem 3 — fixed future reservation dichotomy

Consider an everywhere-total computable no-repeat scan during an epoch with current unread sentinel \(s\). Suppose the selected local test has no positive A/B event on some complete continuation.

Let \(t\ne s\) be a fixed prospective future sentinel which the construction intends to keep unread until the current A/B event occurs.

Then on that no-event continuation at least one of \(s,t\) must be queried after finite interaction.

Equivalently, the scan cannot simultaneously guarantee:

1. indefinite retention of the current sentinel if the selected role is Case C;
2. indefinite freshness of a fixed different future sentinel until the current role resolves;
3. the global one-hole condition.

#### Proof

If neither \(s\) nor \(t\) were ever queried on the no-event continuation, the resulting complete transcript would omit at least two source coordinates. That contradicts the global one-hole requirement.

Because the scan is no-repeat and the complete continuation is infinite, whichever of \(s,t\) is not permanent is consumed at some finite stage. ∎

This dichotomy is more informative than the slogan that two holes are forbidden.

- If the construction consumes \(s\), it has **abandoned the current unresolved role**. An arbitrarily late A/B certificate at \(B_b\) may then be lost.
- If it consumes \(t\), it has **abandoned the fixed future target**. The next fresh target must be chosen elsewhere.
- If it tries to keep all three raw coordinates of a fixed future block fresh, the violation is stronger still.

Thus a value horizon does not license a fixed protected \(G(b)\)-orbit.

### Corollary 4 — the next target remains certificate-time endogenous

A completed A/B epoch can certainly choose a next fresh block above every coordinate actually consumed so far, and Theorem 1 gives a computable lower bound above the local value horizon.

But a globally one-hole scan cannot pre-protect one fixed next block for an unbounded amount of certificate time while also preserving the current sentinel on a possible Case-C branch.

Therefore the actual next fresh block can still depend on how long the A/B certificate takes to appear.

P4-S043's endogeneity has been narrowed from **source-value footprint endogeneity** to **certificate-time endogeneity**. It has not disappeared.

## 3. Moving reservations are legal but time-selected

The fixed-reservation obstruction does not forbid a transient moving reservation.

A scan may temporarily leave a prospective block untouched, later consume it, and move the reservation farther out while the current sentinel remains unresolved. On a genuine Case-C continuation every prospective reservation can eventually be consumed, leaving only the current sentinel permanently unread.

If the A/B certificate appears at a finite stage, the scan may freeze whichever prospective block is reserved at that stage, close the current sentinel, restore a finite prefix beneath the reservation, and continue there.

### Proposition 5 — moving-reservation normal form

After the value horizon at \(B_b\) is exposed, a total one-hole implementation may arrange a computable increasing sequence of transient prospective blocks

\[
g_0(b)<g_1(b)<g_2(b)<\cdots,
\qquad g_0(b)\ge h(b),
\]

such that:

- on a no-event continuation every \(g_s(b)\) is eventually consumed and only the current sentinel remains permanently unread;
- if a positive A/B event appears while \(g_s(b)\) is the active reservation, that block can be retained as the next target.

The target chosen on an A/B path is therefore \(g_s(b)\) for a finite index \(s\) determined by the certificate time.

This is a genuine improvement over arbitrary footprint selection: all possible next targets may be placed on a computable reservation sequence.

It still does not convert an arbitrary infinite ambient A-set into a recurrent reached A-set. An infinite set can avoid the event-time-selected reservation positions, or meet them only finitely often.

## 4. Horizon lanes and the exact finite-cover criterion

The value horizon defines an interval geometry on block indices.

Put

\[
I_b=[b,h(b)).
\]

Call an increasing set of block indices

\[
L=\{\ell_0<\ell_1<\ell_2<\cdots\}
\]

a **horizon lane** if

\[
\ell_{s+1}\ge h(\ell_s)
\]

for every \(s\). Then later lane blocks lie beyond the value horizon of every earlier lane block.

Define the overlap depth

\[
d(t)=\bigl|\{b\le t:t<h(b)\}\bigr|.
\]

### Theorem 6 — exact finite-lane criterion

The raw blocks can be partitioned into finitely many computable horizon lanes if and only if

\[
\sup_t d(t)<\infty.
\]

More precisely, if the maximum overlap depth is at most \(m\), \(m\) lanes suffice; conversely any partition into \(m\) lanes forces \(d(t)\le m\) for every \(t\).

#### Proof

The intervals \(I_b\) form a computable interval graph. Two blocks conflict precisely when their dependency intervals overlap in the sense relevant to being consecutive members of one lane.

If \(m\) lanes exist, at a fixed point \(t\) no two intervals covering \(t\) can have their left endpoints in the same lane before the later interval starts, so at most one such interval belongs to each lane. Hence \(d(t)\le m\).

Conversely, process blocks in increasing order and assign \(b\) the least colour not used by an earlier interval still active at \(b\). At most \(m-1\) colours are forbidden when the overlap depth is at most \(m\), so a colour is available. The assignment is computable from \(h\). Each colour class is a lane. ∎

### Corollary 7 — bare wtt finiteness does not force finitely many lanes

The committed wtt hypothesis says only that \(h(b)\) is a total computable finite integer for each \(b\). It gives no uniform overlap bound.

For example,

\[
h(b)=2b+2
\]

is a computable finite horizon function, but

\[
d(t)\to\infty.
\]

Hence no finite lane cover is forced merely by finiteness of every use horizon.

This is not a claim that the particular existentially supplied P4-S011 machine has this exact horizon. It proves that the committed wtt authority, by itself, contains no finite-lane theorem.

### Corollary 8 — countably many lanes are always available but are insufficient

A computable greedy colouring always yields countably many computable lanes, because each new block has only finitely many earlier active conflicts.

Countable pigeonhole cannot be used. An infinite recurrent set \(R\) may satisfy

\[
|R\cap L_j|<\infty
\]

for every lane \(L_j\).

For a fixed countable lane decomposition, the exact additional concentration condition needed for finite pigeonhole is, for example, that some finite union of lanes meet \(R\) infinitely often. Then one lane in that finite union meets \(R\) infinitely often.

No such thickness, density or bounded-lane-index property is supplied by P4-S042/P4-S043 recurrence.

## 5. What lane recurrence would actually suffice

Even an infinite intersection with a horizon lane does not by itself solve the Case-C trap.

Fix a role \(j\). A one-role P4-S043 scan succeeds if its own sequence of reached targets has:

1. no selected Case C;
2. infinitely many selected Case A.

The relevant recurrence is therefore recurrence on the **event-time-selected target subsequence**, not merely recurrence somewhere on the ambient lane.

### Proposition 9 — conditional fresh-lane theorem

Let a computable moving-reservation implementation keep every possible next target inside a computable horizon lane \(L\). Suppose that on the actual run:

- every selected target role resolves as A or B; and
- selected Case A occurs infinitely often.

Then the P4-S043 asynchronous martingale succeeds and

\[
X\notin OH.
\]

A simple sufficient combinatorial condition is that, from some point onward, every block that can be frozen by the reservation selector is Case A in the selected role.

The weaker assertion

\[
A_j\text{ occurs infinitely often somewhere on }L
\]

is not enough: certificate-time selection can skip those A-blocks, and one reached \(C_j\) is absorbing.

Thus finite lanes would be useful only together with a selector-thickness property not currently known for the committed source.

## 6. Zero-stake support consumption cannot always be recycled into a target

The displayed recoding gives

\[
u_0=x_0\oplus x_2,\qquad
u_1=x_0\oplus x_1,\qquad
u_2=x_0\oplus x_1\oplus x_2.
\]

A fresh support block queried only for \(u_0\) can in principle leave raw \(x_1\) unread. A block queried only for \(u_1\) can leave raw \(x_2\) unread.

But an exact query of \(u_2\) on a completely fresh raw block depends on all three raw coordinates. More generally several requested rows can exhaust the block.

### Proposition 10 — no general productive-support theorem from the use bound

The wtt use cap controls **where** a computation may query. It does not restrict **which virtual row** inside a support block it may request.

Therefore the committed horizon data do not force a support order which preserves one raw coordinate in every dependency block.

A structural finite-use machine may, before producing its local A/B/C evidence, query a \(u_2\)-coordinate in a future fresh block and ignore its value. A raw simulator must then expose all three raw coordinates of that support block to answer the exact virtual value. The block is burned as support before it can be used as a completely fresh three-coordinate target.

This does not say support reuse is never possible. It says there is no uniform theorem from the wtt use bound alone.

A finite refutation discovered opportunistically while serving another computation may still be reused. No such reuse is guaranteed on recurrent blocks by the committed data.

## 7. Finite transient multi-sentinel races

Temporary multiple unread coordinates are compatible with the final one-hole condition. The obstruction is what happens on the continuation where none of their positive events ever arrives.

### Theorem 11 — finite transient-race no-rate obstruction

Consider a finite race among prospective sentinels

\[
s_1,\ldots,s_m
\]

whose A/B events are positively semidecidable after finite source-value horizons. Assume the architecture has an everywhere-total one-hole continuation if every selected candidate is Case C.

On that all-C continuation, at most one of the \(s_k\) may remain unread forever. Hence at least \(m-1\) candidates are consumed at finite stages.

For every candidate consumed in this way, the use bound alone cannot guarantee that its positive A/B event would have appeared before consumption. A finite-use structural machine can delay a finite Case-A refutation beyond that finite consumption stage without making any additional oracle query.

Consequently a finite transient race has no rate-free guarantee of the form:

> if one of the finitely many candidates is A/B, the race will necessarily discover it before all useful candidates are abandoned.

#### Proof

The first statement is the global one-hole condition.

Fix the finite all-C transcript until a particular candidate is consumed. The scan's consumption stage is finite. A local partial computation can use exactly the same finite oracle values and perform more internal machine steps before producing its wrong halt. Choosing the delay beyond the finite consumption stage makes the finite transcript observationally identical up to abandonment, while changing that candidate from C to late A.

For a prescribed finite family of races, these finitely many delays can be selected effectively one after another in a structural construction. ∎

The theorem is an obstruction to the tested finite race architecture, not an impossibility theorem for every conceivable one-hole compiler for the committed \(X\).

It explains exactly why “temporary two or three holes are allowed” does not by itself solve P4-S043: eventual one-hole compliance creates finite abandonment times, while wtt gives no certificate-time modulus.

## 8. Recurrent C0 and the asymmetric patterns

Retain the exact nontriple \(C_0\) patterns

\[
CAA,\qquad CAC,\qquad CCA.
\]

Thus on every nontriple \(C_0\)-block at least one of roles \(1,2\) is A.

The horizon structure does not remove the alternation obstruction:

- a role-1 target can be trapped by a \(CCA\) block;
- a role-2 target can be trapped by a \(CAC\) block;
- \(C_0\) persists in both patterns;
- certificate-time selection can choose a subsequence different from the ambient recurrent A-set.

A finite horizon lane can separate source-value dependencies, but without a selector-thickness or certificate-time bound it does not force one fixed role to see infinitely many A targets before seeing C.

The asymmetric patterns remain

\[
C_1\wedge B_2\Rightarrow(A,C,B),
\]

\[
C_2\wedge B_1\Rightarrow(A,B,C).
\]

They expose \(A_0\), but recurrent ambient \(A_0\) is subject to the same reachability obstruction. The role-0 A certificate is still a positive finite event of unbounded time, and its block can be consumed as support or skipped by the moving reservation before it becomes a target.

No stronger reachability theorem follows merely from the presence of the B arm.

## 9. A sharp structural horizon countermodel

The absence of a finite-lane theorem is not only an artefact of choosing an unnecessarily loose use bound.

### Theorem 12 — computable unbounded-overlap structural model

Fix any prescribed finite family of wait-for-own-status role/lane policies of the P4-S043 type.

There is a computable syntactically self-avoiding finite-use functional \(N\) with computable target

\[
Y_*=0^\omega
\]

having the following properties.

1. Use three-bit blocks \(B_b\).
2. The actual finite query footprint of each local block computation includes a dummy query to \(u_2\) in block
   \[
   d(b)=2b+1.
   \]
3. Hence one may take the genuine raw horizon
   \[
   h(b)=2b+2,
   \]
   whose interval overlap depth is unbounded.
4. Direction \(0\) is Case C on every target block.
5. Triple Case C occurs on no block.
6. Every block has a visible Case-A direction.
7. Every member of the prescribed finite policy family can be made either to select C and become trapped or to have an A-bearing future block consumed as support before it becomes its sentinel.

#### Construction

Start with the P4-S043 finite-family block gadgets using only

\[
CCA\quad\text{and}\quad CAC
\]

for recurrent \(C_0\). These local tables are computable, finite-use and syntactically self-avoiding on \(0^\omega\), and they diagonalize against any prescribed finite family of wait-for-own-status roles.

Before each local table computation acts on its same-block inputs, make one ignored query to the virtual coordinate \(u_2\) in block \(d(b)=2b+1\). The queried coordinate is different from the current input, so self-avoidance is preserved. On the target and on every local raw-adjacent candidate at \(B_b\), the far block is unchanged, and the ignored answer does not alter the A/B/C status.

Because \(u_2\) is the parity of all three raw bits of its block, a direct raw evaluator of that exact support value can be forced to consume the entire fresh raw support block \(B_{d(b)}\). Thus the footprint is real rather than an inflated bookkeeping bound.

The finite-family diagonalization from P4-S043 chooses \(CCA\) or \(CAC\) when each active policy reaches a fresh target, trapping at least one active role at each finite elimination stage. The added far query can additionally burn future candidate blocks as support. Continue with either nontriple pattern after the finite family has been eliminated.

All machine uses are computably finite. ∎

This model is **structural only**. Its target \(0^\omega\) is not computably random. It does not show that the actual committed source has unbounded overlap or that \(X\in OH\).

It proves that the currently retained hypotheses—computable finite use, self-avoidance, the exact local status law and recurrent nontriple C—do not force a finite lane selector or productive support reuse.

## 10. Stronger necessary selector obstruction under X in OH

Combining P4-S042, P4-S043 and the present horizon analysis gives the following source-side necessary condition.

### Theorem 13 — no computable successful reservation selector under OH

Assume

\[
X\in OH.
\]

Then there is no computable one-hole moving-reservation/role selector which, on its target run:

1. completes infinitely many epochs;
2. has selected Case C only finitely often, hence none after some point;
3. selects Case A infinitely often.

Otherwise P4-S043 asynchronous extraction would give a computable martingale succeeding on the selector's output.

The new content of P4-S044 is that the wtt value horizon does not automatically build such a selector from ambient recurrent A witnesses. Every attempt still has to solve a certificate-time reservation problem, and finite-lane geometry is available only under an extra bounded-overlap hypothesis.

This is a stronger formulation of the surviving obstruction, not a proof of \(X\in OH\).

## 11. Exact session outcome

P4-S044 obtains the requested **theorem that the actual horizon resource still does not, from the committed hypotheses, turn ambient A recurrence into scan-reachable recurrence**, together with an exact structural countermodel.

The positive part is genuine:

- there is a uniform computable raw source-value horizon \(h(b)\);
- all A/B evidence is source-value closed inside it;
- possible next targets can be constrained to computable moving-reservation sequences;
- finite horizon lanes have an exact interval-overlap characterization.

The negative boundary is also exact:

- no halting/certificate-time modulus follows;
- one fixed protected future target conflicts with indefinite retention of the current Case-C sentinel;
- countably many lanes do not support infinite pigeonhole;
- finite lanes are not forced by wtt finiteness;
- support blocks can be completely consumed;
- finite transient races inherit finite abandonment times and can miss arbitrarily late A certificates.

Therefore no actual raw one-hole destroyer for the committed \(X\) is constructed in this session, and no proof that

\[
X\in OH
\]

is obtained.

No OH non-invariance witness and no strict inclusion

\[
R_2\subsetneq OH
\]

is claimed.

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

P4-S032 null-ambiguity preservation remains available, but ambiguity mass is not reinstated as an invariant.

## 12. Next bounded target

The remaining obstruction is now **certificate-time selector thickness after source-value closure**.

A useful next session should stop asking whether the wtt use bound localizes source values; P4-S044 settles that positively.

The next question is whether the actual committed computably random source supplies any source-specific regularity preventing Case-A certificate times and A-bearing blocks from evading every computable moving-reservation selector.

High-value directions are:

- formalize moving-reservation selectors as computable subsequence operators on horizon-separated candidate blocks;
- identify an exact selector-thickness property of the recurrent A sets that would force one selector to hit A infinitely often while avoiding C;
- test whether computable randomness of \(Y\) or the fact that \(M^Y(n)\) halts for every target input constrains the certificate-time pattern enough to imply such thickness;
- test whether a structural delayed-certificate diagonalization can be strengthened from every prescribed finite family to a uniform family without accidentally making the target non-computably-random or changing the committed source problem;
- determine whether recurrent \(C_0\) or the asymmetric \(ACB/ABC\) patterns give stronger selector-thickness once source-value closure is fixed.

Do not infer \(X\in OH\) from failure of tested selectors.

## Guards

All validated mathematics through P4-S043 is preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

DEF-0020 is unchanged.

Phase 4 remains OPEN. Phase 5 remains CLOSED.

No novelty, openness, prior-art, Gate-4, publication or outreach conclusion is made.
