# P4-S045 — moving-reservation selector thickness and countable-family diagonalization

Date: 2026-10-07
Session: P4-S045
Incoming checkpoint: 55b203879c3c4ab6cfa88cc32f6dee6dc57d9259
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding
Result: **MOVING RESERVATIONS CAN BE FORMALIZED AS A FAITHFUL ONE-HOLE SELECTOR WHOSE NEXT TARGET IS THE RESERVATION ACTIVE WHEN A POSITIVE A/B CERTIFICATE APPEARS. THE EXACT USEFUL PROPERTY IS EVENT-TIME SELECTOR THICKNESS, NOT AMBIENT RECURRENCE OR ORDINARY DENSITY. COFINITE A ON A C-FREE RESERVATION LANE IS SUFFICIENT; BOUNDED GAPS, POSITIVE DENSITY, FINITE-UNION LANE CONCENTRATION WITHOUT CLOCK CONTROL, AND RECURRENCE ALONG EVERY COMPUTABLE SUBSEQUENCE ARE NOT. AFTER P4-S044 VALUE CLOSURE, CERTIFICATE TIME IS FUTURE-BLIND: IT DEPENDS ONLY ON ALREADY EXPOSED FINITE SOURCE DATA AND INTERNAL COMPUTATION, SO SYSTEMATIC DELAY ALONE GIVES NO COMPUTABLE PREDICTION OF AN UNREAD FUTURE BIT. THE P4-S044 FINITE-FAMILY STRUCTURAL OBSTRUCTION STRENGTHENS TO EVERY MEMBER OF ANY PRESCRIBED UNIFORMLY COMPUTABLE COUNTABLE FAMILY OF FAITHFUL MOVING-RESERVATION SELECTORS, WHILE A UNIVERSAL COMPUTABLE-TARGET COUNTERMODEL OF THE SAME TYPE IS IMPOSSIBLE: AFTER THE MODEL IS BUILT, VISIBLE A CERTIFICATES ON A COMPUTABLE TARGET CAN BE ENUMERATED AND A NEW COMPUTABLE SELECTOR CAN TARGET THEM. THIS PRECISELY EXPOSES THE ACTUAL-SOURCE GAP AS LIVE SOURCE-ACCESS TO FUTURE A CERTIFICATES. NO ACTUAL RAW DESTROYER FOR X AND NO PROOF X IN OH ARE OBTAINED.**

## Authority, uniqueness and scope

Live main was pinned immediately before substantive work at

\[
\texttt{55b203879c3c4ab6cfa88cc32f6dee6dc57d9259},
\]

the exact final P4-S044 tip. The preceding commit message is P4-S044 record horizon selector failures, and the P4-S044 mathematics/validation/close records all agree with that state. Repository search found no P4-S045 mathematics, validation or close record. Hence P4-S045 was unused.

The committed repository was treated as authority. P4-S001 through P4-S044 were read from the pinned state, together with the selected CAND-01 authority in phase2/candidates.json and phase2/P2-S001_DISCOVERY.md, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, and P4-S032 through P4-S044. Special attention was given to P4-S011, P4-S012, P4-S027 and P4-S039 through P4-S044.

All validated mathematics through P4-S044 is frozen. The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence, P4-S037/P4-S038 backward-price route, ordinary raw-martingale compilation, ambiguity mass, general radius-one totalization, one-off remote-divergence localization and local A/B/C enumeration are not reopened.

Retain

\[
R_2=\{x\in CR:\text{every total computable fair-coin-preserving global-}k=2\text{ map sends }x\text{ to }CR\},
\]

\[
OH=\{x\in CR:\text{every total computable adaptive no-repeat one-hole scan sends }x\text{ to }CR\},
\]

\[
OH^{iso}=\{x\in CR:\text{every computable fair-coin-preserving homeomorphism }H\text{ sends }x\text{ into }OH\},
\]

and

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Let \(Y\) be the P4-S011 computably random wtt-autoreducible source, \(M\) its committed syntactically self-avoiding wtt autoreduction, \(D\) its one-hole destroyer, and

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

The source-side question remains whether \(X\in OH\).

## 1. Retained P4-S044 value closure

Use the P4-S027 strict computable use cap \(U(n)\). For

\[
B_b=\{3b,3b+1,3b+2\},
\]

put

\[
V(b)=\max_{r<3}U(3b+r)
\]

and

\[
h(b)=\max\left\{b+1,\left\lceil V(b)/3\right\rceil\right\}.
\]

Every oracle value which can affect any of the six raw-adjacent endpoint computations at \(B_b\) lies in a raw block below \(h(b)\), apart from the finite current-block endpoint hypothesis.

Thus, after the relevant raw values below \(h(b)\) have been exposed, later raw source values cannot change whether an A or B event eventually appears. They can only fail to supply a time bound for that event.

P4-S045 does not reprove this theorem.

## 2. Exact moving-reservation selectors

The P4-S044 phrase moving reservation is now made precise.

### Definition 1 — faithful moving-reservation selector

A faithful moving-reservation selector \(S\) is an everywhere computable no-repeat raw scan protocol with the following epoch structure.

At the beginning of epoch \(e\):

1. the scan has a completely fresh target block \(B_{b_e}\);
2. from the finite prior transcript it chooses a raw role
   \[
   i_e\in\{0,1,2\}
   \]
   before the A/B/C status of that role is known;
3. it withholds the current sentinel
   \[
   s_e=3b_e+i_e
   \]
   and reads the other two raw coordinates of \(B_{b_e}\);
4. it exposes whatever additional raw values below the P4-S044 value horizon are needed to close the source-value dependence of the two raw-adjacent endpoint simulations;
5. it continues dovetailing those endpoint computations while never reading \(s_e\) unless a positive A/B certificate appears.

After value closure, \(S\) maintains a computable stream of pairwise fresh prospective future blocks

\[
g_{e,0}<g_{e,1}<g_{e,2}<\cdots
\]

above the already consumed region and above the current value horizon.

Exactly one \(g_{e,r}\) is called active at a time. While the current A/B event remains unresolved:

- the active block is kept completely fresh;
- the scan continues a zero-stake background sweep of all other fresh coordinates;
- after a finite computably determined tenure, if no event has appeared, the old active block is consumed at zero stake and a farther fresh block becomes active.

If a positive A or B certificate appears while \(g_{e,r}\) is active, \(S\):

- freezes \(g_{e,r}\) as the next target block;
- in Case A bets on the now certified value of the current sentinel and reads it;
- in Case B reads the current sentinel at zero stake;
- restores a queried prefix up to the frozen block while leaving that block completely fresh;
- starts epoch \(e+1\) at
  \[
  b_{e+1}=g_{e,r}.
  \]

On a genuine no-event continuation, the current sentinel \(s_e\) is never consumed. Every transient prospective block is eventually consumed. Therefore the complete no-event transcript omits exactly the current sentinel and no second permanent coordinate.

This last clause is the faithfulness condition. It separates the architecture from a finite-abandonment rule which simply consumes the unresolved current sentinel.

### Proposition 2 — global one-hole validity

Every protocol satisfying Definition 1 is an everywhere-total computable adaptive no-repeat one-hole scan.

#### Proof

At every finite stage the scan emits a fresh raw query according to a computable rule. On a completed epoch the old sentinel is consumed and the frozen reservation becomes the next fresh target.

On a no-event continuation, every active reservation is transient and eventually consumed. The background sweep consumes every coordinate other than the current sentinel. Hence the completed transcript has exactly one hole.

No coordinate is queried twice. ∎

### Three distinct sets

For a fixed role \(i\), write

\[
A_i=\{b:\text{role }i\text{ at }B_b\text{ is Case A on }X\},
\]

and similarly \(B_i,C_i\).

Three objects must not be identified:

1. the ambient block set \(A_i\);
2. an epoch's reservation stream
   \[
   G_e=\{g_{e,0},g_{e,1},\ldots\};
   \]
3. the event-time-selected target subsequence
   \[
   b_{e+1}=g_{e,r_e},
   \]
   where \(r_e\) is the reservation index active when the current positive certificate appears.

The third object is generally source-dependent and need not be a computable subsequence of the ambient block order.

## 3. Exact selector thickness

### Definition 3 — event-time selector thickness

Fix a faithful selector \(S\) and, for simplicity, a fixed raw role \(i\).

The pair \((A_i,C_i)\) is **selector-thick for \(S\) on \(X\)** if the actual target run of \(S\):

1. completes infinitely many epochs, equivalently it never selects a Case-C block; and
2. selects Case A on infinitely many target blocks.

This is the weakest operational property needed by the P4-S043 asynchronous martingale.

### Theorem 4 — selector thickness gives a raw destroyer

If a computable faithful moving-reservation selector \(S\) is selector-thick for some role \(i\) on \(X\), then

\[
X\notin OH.
\]

#### Proof

Use the scan from Definition 1. In each selected Case-A epoch, finite refutation of the alternate endpoint certifies the actual sentinel value. Bet all current capital on that bit. In Case B, wager zero.

All Case-A wagers on \(X\) are correct. Selector thickness gives infinitely many such wagers and no Case-C trap. The output martingale therefore doubles infinitely often. Proposition 2 gives a total computable one-hole scan, so \(X\notin OH\). ∎

Thus, under a hypothetical \(X\in OH\), **every** computable faithful moving-reservation selector must fail selector thickness.

## 4. Stronger sufficient thickness conditions and failed substitutes

The operational definition is exact but source-specific. Several more concrete hypotheses were tested.

### 4.1 C-free cofinite lane is sufficient

Let

\[
L=\{\ell_0<\ell_1<\cdots\}
\]

be a computable reservation lane. Suppose a selector uses only progressively later members of \(L\), and suppose

\[
L\cap C_i=\varnothing
\]

while

\[
L\setminus A_i
\]

is finite.

Then the selector cannot be trapped by C and, after finitely many selected targets, every selected target is A. Hence it is selector-thick.

The C-free clause matters. Mere cofiniteness of A on a lane allows one exceptional early C block, and a faithful selector can be trapped there before reaching the cofinite tail.

### 4.2 Finite possible-index coverage plus clock domination is sufficient

At epoch \(e\), suppose there is a computable finite set \(P_e\) of reservation indices such that the positive current certificate, if it appears, is guaranteed to appear while some index in \(P_e\) is active.

If every candidate

\[
g_{e,r},\qquad r\in P_e,
\]

is C-free, and for infinitely many completed epochs every such candidate is in \(A_i\), then the selected next-target sequence contains infinitely many A blocks.

This is the useful form of a finite-union lane hypothesis: the lane information must be coupled to an effective restriction on the possible active certificate-time indices.

### 4.3 Bounded gaps or positive density are not enough

Suppose, even abstractly, the reservation indices with A status are all even. Then A has gap at most two and density \(1/2\).

If every current certificate appears while an odd-indexed reservation is active, the event-selected subsequence misses A completely.

Therefore bounded-gap or positive-density information relative to reservation index does not imply selector thickness without a theorem coupling certificate time to those indices.

### 4.4 Finite-union lane concentration alone is not enough

Knowing that all relevant A blocks lie in a finite union of computable lanes does not determine which lane is active when a certificate arrives.

If the certificate clock can select among the lanes adversarially, it can repeatedly choose a non-A member even when another lane contains recurrent A.

A finite-lane theorem therefore needs a certificate-time domination or lane-identification principle, not merely a colouring theorem.

### 4.5 Recurrence on every computable subsequence is not enough as stated

The event-time-selected target sequence of a computable scan need not itself be computable without the source.

Its reservation choices may depend on finite source values already exposed in previous epochs, and the active index depends on the halting time of partial sibling computations.

Thus a hypothesis quantifying only over infinite computable subsequences does not automatically apply to the actual selected sequence.

A proof using such a hypothesis must first establish that the event-selected target sequence is computable independently of \(X\). No such theorem follows from P4-S044.

### Thickness hierarchy

The implications justified here are:

\[
\text{C-free A-cofinite reservation lane}
\Longrightarrow
\text{event-time selector thickness},
\]

and

\[
\text{finite possible-index coverage + A coverage}
\Longrightarrow
\text{event-time selector thickness}.
\]

Neither bounded gaps, positive density, finite-union lane concentration, nor recurrence on computable subsequences alone implies event-time selector thickness.

No claim is made that the actual \(A_i\) satisfy either sufficient condition.

## 5. Certificate time is future-blind after value closure

The P4-S044 value horizon gives a stronger negative statement than merely saying no time bound is known.

### Proposition 5 — future-blind certificate clock

Fix a current block \(b\), raw role \(i\), and the finite current-block endpoint hypotheses.

After all raw source values in blocks below \(h(b)\) that can be queried by the endpoint computations have been exposed, then for every machine-step bound \(t\) the statement

> an A/B certificate has appeared within the first \(t\) simulation steps

is completely determined by:

- the machine code of \(M\);
- the finite endpoint hypotheses;
- the already exposed raw source values below \(h(b)\).

It is independent of every raw source coordinate in a block at or above \(h(b)\).

#### Proof

The strict P4-S027 use cap forbids every endpoint computation from querying a virtual coordinate at or above \(V(b)\). The P4-S044 translation from virtual use to raw blocks places every required outside value below \(h(b)\).

Once those finite oracle answers are fixed, the first \(t\) internal simulation steps are an ordinary finite deterministic computation. No later source value is consulted. ∎

### Consequence 6 — systematic delay does not itself predict a future bit

A long wait for an A certificate can tell the selector something about the finite computation on already exposed values. It does not, by itself, determine any unread bit in the active future reservation block.

Therefore the proposed direct computable-randomness contradiction has a missing premise: one would need a computable coupling from the late/early certificate clock to an unread source bit on which to wager.

Target correctness

\[
M^Y(n)\downarrow=Y(n)
\]

does not supply that coupling. It guarantees that the actual endpoint computations halt correctly. A Case-A certificate is instead a wrong/nonbinary halt on an altered sibling oracle.

Syntactic self-avoidance and finite use restrict which values are queried; neither converts off-target runtime into a prediction of a future target bit.

Accordingly P4-S045 obtains no direct source martingale from systematic certificate delay.

This is not a theorem that delayed certificates are compatible with the exact committed source. It is the exact reason the tested delay pattern does not presently contradict computable randomness.

## 6. Target correctness and computable randomness give no generic runtime modulus

There is also a presentation-level guard.

Given any self-avoiding finite-use partial functional \(M\), one may form a target-equivalent functional \(M_D\) which:

1. simulates \(M\);
2. if \(M\) halts, performs an additional computable finite delay \(D(n,\tau)\), where \(\tau\) is the finite observed computation transcript;
3. returns the same output.

This changes no oracle query, no use, no output and no syntactic self-avoidance. If \(M^Y(n)=Y(n)\), then also

\[
M_D^Y(n)=Y(n).
\]

Arbitrarily large computable delays can therefore be inserted without changing the source \(Y\), its computable randomness, or the semantic local A/B/C status.

This does not alter the committed \(M\) and is not used as a replacement for it. It proves only that computable randomness plus target correctness, self-avoidance and finite use cannot by themselves entail a machine-presentation-independent certificate-time modulus.

Any positive theorem for the actual \(M\) must use an additional source-specific property of that presentation.

## 7. Countable-family structural diagonalization

P4-S044 defeated any prescribed finite selector/race family structurally. The finite bound is not essential for faithful moving-reservation selectors.

### Definition 7 — selector scheme family

A selector scheme is a faithful moving-reservation protocol whose decisions are computable from:

- its finite raw transcript;
- the positive A/B certificates it has so far observed;
- its own finite internal state.

It does not receive negative C information as an oracle.

A sequence

\[
(S_e)_{e\in\omega}
\]

is a prescribed uniformly computable countable family if one program uniformly computes the transition rules of \(S_e\), and every \(S_e\) is promised to be an everywhere-total scan scheme.

### Theorem 8 — prescribed countable-family structural countermodel

For every prescribed uniformly computable countable family

\[
(S_e)_{e\in\omega}
\]

of faithful moving-reservation selector schemes, there is a computable syntactically self-avoiding finite-use functional \(N\) with computable target

\[
Y_*=0^\omega
\]

such that:

1. \(N^{Y_*}(n)=0\) for every \(n\);
2. direction \(0\) is Case C on every block;
3. triple Case C occurs on no block;
4. every block has a visible Case-A direction;
5. only the two recurrent patterns
   \[
   CCA,\qquad CAC
   \]
   are needed;
6. every \(S_e\) is eventually trapped on a block whose selected raw role is Case C;
7. the P4-S044 genuine unbounded-overlap horizon can simultaneously be imposed:
   \[
   h(b)=2b+2.
   \]

#### Construction

Use the already validated P4-S043 local finite-use self-avoiding gadgets realizing \(CCA\) and \(CAC\) on \(0^\omega\).

Build the block-pattern function in requirements \(R_0,R_1,\ldots\), maintaining a finite completely assigned initial block prefix after every requirement.

For requirement \(R_e\), simulate \(S_e\) on the all-zero raw target through the currently assigned finite prefix.

If \(S_e\) selects a Case-C role on an already assigned target block, it is already trapped and \(R_e\) is satisfied.

Otherwise every target it selects inside the assigned prefix is A, so its positive certificate appears after finite simulation and faithfulness makes it close and continue. Since the assigned prefix is finite and target blocks are fresh and move outward, \(S_e\) eventually opens a target block whose local pattern is still unassigned.

Let \(i\) be the raw role it has already selected there.

- If \(i=0\) or \(i=1\), assign pattern \(CCA\).
- If \(i=2\), assign pattern \(CAC\).

In either case the selected role is C, direction \(0\) is C, the block is not triple C, and some other role is A.

The selector cannot positively discover C and, by faithfulness, never consumes its current sentinel. It is therefore trapped.

Fill any remaining unassigned blocks up to that new construction frontier by either \(CCA\) or \(CAC\), and proceed to \(R_{e+1}\).

Every requirement finishes after finite simulation under the promised totality of the selector family. The construction frontier tends to infinity. Hence, to compute the pattern of block \(b\), run the finite requirement construction until its assigned prefix passes \(b\). This halts, so the block-pattern function is computable.

Finally prepend to every local block computation the P4-S044 ignored query to virtual row \(u_2\) in block

\[
d(b)=2b+1.
\]

The answer is ignored, the queried coordinate is not the current input, and the local A/B/C status is unchanged. Exact raw evaluation of that \(u_2\) support can consume its whole three-bit block, giving the genuine horizon

\[
h(b)=2b+2
\]

with unbounded interval overlap.

Thus \(N\) is computable, syntactically self-avoiding and finite-use, and every prescribed family member is trapped. ∎

### What Theorem 8 does and does not say

It is a strict strengthening of P4-S044's finite-family structural model.

It does **not** diagonalize against all total computable selectors at once. The family must be prescribed before the structural functional is built.

It is also explicitly a computable-target model. It does not imply anything about the committed computably random \(Y\) or \(X\).

## 8. Why universal computable-target diagonalization fails

The restriction in Theorem 8 is substantive rather than cosmetic.

### Theorem 9 — post-construction A-enumeration defeats universal structural evasion

Let \(Z\) be a computable target and let \(N\) be a computable finite-use self-avoiding functional correct on \(Z\).

Suppose infinitely many blocks have at least one finite Case-A certificate.

Then there is a computable faithful role/target selector which targets only blocks with a pre-certified Case-A role and therefore selects A infinitely often without ever being trapped by C on its target run.

#### Proof

Because \(Z\) is computable, one can simulate, off-line, all raw-adjacent local companion computations on every block and every role.

Case A is positively witnessed by a finite wrong/nonbinary halt. Hence the set of pairs

\[
\{(b,i):b\in A_i\}
\]

is computably enumerable.

If infinitely many blocks have some A role, this c.e. set contains pairs on arbitrarily large block numbers.

Enumerate it until finding a pair \((b_0,i_0)\). Then search until finding a certified pair on a strictly larger block \(b_1\), and continue.

This computes a strictly increasing sequence

\[
(b_0,i_0),(b_1,i_1),\ldots
\]

of already certified A targets.

A faithful scan can use \(B_{b_e}\) as its next target and choose the pre-certified role \(i_e\). On the computable structural target the A certificate is guaranteed to appear, so every epoch closes correctly and the scan proceeds forever with infinitely many A wagers. On arbitrary transcripts, if a selected status fails to resolve, the usual background sweep leaves only its current sentinel, so the scan remains globally one-hole.

Thus a post-construction computable selector escapes every proposed universal evasion model having infinitely many visible A blocks. ∎

### Corollary 10 — no universal version of the P4-S043/P4-S044 structural model

A computable-target structural model cannot simultaneously have:

1. infinitely many blocks with visible A witnesses; and
2. failure of every computable faithful moving-reservation selector.

Theorem 8 can defeat every member of a prescribed uniformly computable countable family only because the escaping selector of Theorem 9 is constructed **after** \(N\) and need not belong to that family.

This also explains why there is no contradiction with countability of the computable selectors: there is no effective enumeration of exactly the total selector programs suitable for a sequential all-requirements construction, and the final model itself can generate a new selector from its c.e. A certificates.

## 9. Why the post-construction escape does not transfer to the committed source

Theorem 9 uses one resource absent for the actual \(X\): off-line knowledge of the target source.

For \(0^\omega\), every source value needed by every finite use horizon is computable without touching the live scan.

For the committed noncomputable \(X\), an A certificate at block \(b\) is only c.e. **relative to the finite raw values needed below \(h(b)\)** together with the endpoint hypothesis. A live scan must expose those source values to run the certificate search.

In particular, pre-certifying a prospective future target can consume source coordinates which must remain fresh if that block is later to be used as a target. Keeping its raw sentinel unread while the current unresolved sentinel is also retained recreates the global one-hole reservation conflict.

Thus the exact new source-side distinction is:

\[
\text{off-line enumerable A on a computable target}
\]

versus

\[
\text{live-source A certification with freshness cost}.
\]

Computable randomness does not make the required finite source values computable off-line.

No theorem in P4-S045 proves that the live-access cost is insurmountable for the committed source. It identifies the resource that a positive selector theorem would have to overcome.

## 10. Recurrent C0: two selectors still face an indistinguishability fork

Retain the nontriple recurrent \(C_0\) patterns

\[
CAA,\qquad CAC,\qquad CCA.
\]

Roles \(1,2\) always contain at least one A witness.

A two-selector strategy might try to keep both roles available until it learns which one is A. The obstruction can now be stated sharply.

### Proposition 11 — two-role C0 abandonment fork

Fix any finite interaction stage at which neither role-1 nor role-2 positive certificate has appeared.

The two legal continuations

\[
CAC
\]

and

\[
CCA
\]

can be made observationally identical through that stage while postponing their A certificate beyond it:

- in \(CAC\), role \(1\) is late A and role \(2\) is C;
- in \(CCA\), role \(1\) is C and role \(2\) is late A.

If a globally one-hole protocol is simultaneously protecting distinct future sentinels for both roles while also retaining the current unresolved sentinel, then on the common no-event prefix it must consume at least one protected sentinel after finite interaction.

Choose the continuation in which the consumed role is the late A role and the surviving role is C. The protocol has abandoned the only finite A certificate it could have harvested and retained the divergent role.

The construction uses no support-block consumption and can be realized with block-local finite use. Therefore the failure is not fundamentally a support-footprint phenomenon.

The ingredients are exactly:

1. role alternation between \(CAC\) and \(CCA\);
2. arbitrarily delayed finite A certificates;
3. the global one-hole fallback rule.

Support consumption can worsen the problem but is not needed for it.

This is a structural no-rate obstruction, not a statement that the committed source realizes the adversarial alternation.

## 11. ACB/ABC: the B clock does not control the A0 clock

Retain

\[
C_1\wedge B_2\Rightarrow(A,C,B),
\]

and

\[
C_2\wedge B_1\Rightarrow(A,B,C).
\]

The visible B arm does not provide a generic synchronization theorem.

### Proposition 12 — independent finite certificate clocks

Take any finite-use self-avoiding local realization of either \(ACB\) or \(ABC\).

For every integer \(T\), one can preserve:

- the target oracle values;
- every oracle query;
- every output;
- the A/B/C status triple;
- the self-avoidance and finite-use bounds;

while inserting at least \(T\) additional internal steps before the wrong/nonbinary halt witnessing \(A_0\), leaving the B-acceptance computations unchanged.

Conversely, the B-acceptance halts can be delayed while leaving the A witness unchanged.

#### Proof

After the relevant computation has made the same finite oracle queries, insert a finite computable dummy loop before returning its already determined output. This does not alter any oracle dependence or output. Apply the delay only to the selected input/candidate computation. ∎

Therefore no bound of the form

\[
\text{time}(A_0)\le f(\text{time}(B))
\]

or its converse follows from the local status law, finite use or self-avoidance alone.

On the actual committed \(M\), a special source-specific coupling could still exist, but none is present in the retained authority and none is proved here.

Hence the B certificate cannot presently be used as a clock that forces a future role-0 reservation to remain active until the A0 certificate.

## 12. Computable-randomness compatibility remains unresolved

P4-S044's structural target was \(0^\omega\), and Theorem 8 remains structural for the same reason.

The construction controls the local tables precisely because it may hard-code behavior correct on a computable target.

To transfer the construction to the committed computably random \(Y\), one would need to alter off-target sibling behavior while preserving

\[
N^Y(n)=Y(n)
\]

for every input without using \(Y\) as a noncomputable program parameter.

The committed autoreduction \(M\) supplies target correctness, but its off-target A/B/C timing is not freely programmable.

No construction in this session simultaneously obtains:

- a computably random target;
- the exact P4-S011 style wtt-autoreducibility;
- and universal selector-evasive delayed A certificates.

Equally, no theorem shows computable randomness forbids such timing geometry.

The correct record is therefore:

\[
\text{compatibility with the committed CR source is unresolved}.
\]

## 13. Sharper necessary obstruction under a hypothetical X in OH

Combine Theorem 4 with the retained P4-S042/P4-S043/P4-S044 recurrence results.

### Theorem 13 — live-access selector thinness is necessary for OH survival

Assume

\[
X\in OH.
\]

Then for every computable faithful moving-reservation selector \(S\), its actual target run fails event-time selector thickness.

Equivalently, \(S\) must either:

1. be permanently captured by a selected Case-C block; or
2. complete infinitely many epochs but select Case A only finitely often.

Moreover, the failure cannot be justified merely by saying the ambient A set is sparse. P4-S043 allows ambient recurrent A witnesses, and Theorem 9 shows that on a computable target such visible A recurrence would be harvestable after construction.

Therefore a surviving \(X\in OH\) branch must exploit the noncomputable **live-access cost** of learning which future blocks carry A certificates, together with certificate-time selection or C capture.

This is stronger than the P4-S044 phrase certificate-time endogeneity: it identifies the obstruction as **certificate-time selector thickness under live source access**.

The theorem remains one-way. Failure of all tested selectors does not prove \(X\in OH\).

## 14. Session outcome

P4-S045 reaches one of the requested substantive outcomes:

> a **uniformly computable countable-family structural selector countermodel**, strictly strengthening P4-S044's prescribed finite-family model, together with an exact theorem explaining why the construction cannot be universal on a computable target while retaining infinitely many visible A witnesses.

It also:

- formalizes faithful moving-reservation selectors;
- separates ambient block sets, reservation streams and event-time-selected target subsequences;
- defines exact event-time selector thickness;
- proves two concrete sufficient thickness conditions;
- proves bounded gaps/density and bare lane recurrence are insufficient;
- shows why computable-subsequence recurrence is mismatched to a source-dependent selected sequence;
- proves certificate time is future-blind after P4-S044 value closure;
- finds no direct computable-randomness betting contradiction from systematic delay;
- isolates the C0 two-selector failure as role alternation + certificate delay + global one-hole fallback, not support consumption;
- proves the ACB/ABC B clock has no generic timing control over the A0 clock;
- identifies the computable-target versus live-source certification gap.

No actual raw one-hole destroyer for the committed \(X\) is constructed.

No proof of

\[
X\in OH
\]

is obtained.

No OH non-invariance witness is proved, and no strict inclusion

\[
R_2\subsetneq OH
\]

is claimed.

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

P4-S032 null-ambiguity preservation remains available but ambiguity mass is not reinstated as an invariant.

## 15. Next bounded target

P4-S045 shows that the structural computable-target problem is now qualitatively different from the committed source problem.

On a computable target, visible A certificates can be enumerated off-line and turned into a post-construction selector. On \(X\), the finite source values needed to certify a prospective A block must be acquired by the live one-hole scan.

The next bounded question should therefore be **future A-certificate access cost**.

For a prospective raw target block \(b\) and role \(i\), determine exactly which raw coordinates must be exposed before a finite Case-A certificate can be recognized, and whether the actual committed \(M\) ever supplies infinitely many A certificates whose evidence avoids the prospective sentinel/block strongly enough to permit pre-certification while the current sentinel remains open.

In particular test:

- support-only or below-target A certificates which can be recognized without opening the prospective target block;
- whether target correctness or self-avoidance forces such certificates on any recurrent pattern;
- whether the B arm in \(ACB/ABC\) can certify a future \(A_0\) block without reading its raw sentinel;
- whether one can build a computable certification graph whose edges preserve one-hole freshness;
- or whether every useful future A certificate necessarily consumes/protects a second raw coordinate and therefore recreates the one-hole obstruction.

Do not return to a generic certificate-time bound. The new issue is **where the evidence must be read**, not how long the already closed computation takes.

## Guards

All validated mathematics through P4-S044 is preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

DEF-0020 is unchanged.

Phase 4 remains OPEN. Phase 5 remains CLOSED.

No novelty, openness, prior-art, Gate-4, publication or outreach conclusion is made.
