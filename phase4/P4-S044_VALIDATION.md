# P4-S044 Validation

Date: 2026-10-07
Session: P4-S044
Incoming checkpoint: dfd593bd3d0e2bc68d9b2e2097b31c5dbc443c17
Mathematics record: phase4/P4-S044_MATHEMATICS.md
Disposition: **PASS**

## Scope and authority

- Live main was checked immediately before the first P4-S044 write and was exactly the final P4-S043 tip:
  \[
  \texttt{dfd593bd3d0e2bc68d9b2e2097b31c5dbc443c17}.
  \]
- P4-S044 was unused at that checkpoint.
- P4-S001 through P4-S043 were read from the pinned committed state.
- The selected CAND-01 authority was checked in phase2/candidates.json and phase2/P2-S001_DISCOVERY.md.
- phase4/P4_RESEARCH_PIVOT_AFTER_S031.md and P4-S032 through P4-S043 were checked.
- P4-S011, P4-S012, P4-S027 and P4-S039 through P4-S043 received direct attention.
- The frozen bankroll, backward-price, ordinary raw-martingale, ambiguity-mass, general radius-one-totalization and one-off remote-divergence routes were not reopened.

## Mathematical validation

### 1. Uniform value horizon

Let \(U(n)\) be the strict computable use cap supplied by the retained P4-S027 normal form.

For block \(B_b=\{3b,3b+1,3b+2\}\), define

\[
V(b)=\max_{r<3}U(3b+r)
\]

and

\[
h(b)=\max\left\{b+1,\left\lceil V(b)/3\right\rceil\right\}.
\]

Every local endpoint computation has input one of \(3b,3b+1,3b+2\), so every oracle query is below \(V(b)\), independently of the candidate oracle and independently of whether the computation eventually halts.

Every virtual coordinate below \(V(b)\) belongs to a raw three-bit block below \(\lceil V(b)/3\rceil\). Current-block virtual values are supplied by the finite endpoint hypothesis rather than by reading the sentinel.

Therefore all outside source values that can affect the six raw-adjacent endpoint computations lie in raw blocks below \(h(b)\).

Divergence is compatible with the finite query cap, because a computation can perform infinitely many internal steps after making only finitely many bounded oracle queries.

**Status: VALID.**

### 2. Source-value closure versus certificate time

After all possible oracle answers inside the use window are known, no later filler value can change the simulated computation.

However finite simulation may still reveal a halt only after arbitrarily many machine steps, and no computable halting-time modulus follows from wtt use.

This matches the already validated P4-S027 distinction between exhaustion of the value frontier and possible arbitrarily delayed trigger visibility.

**Status: VALID.**

### 3. Fixed future reservation dichotomy

Suppose a no-event continuation keeps the current sentinel \(s\) unread.

If a different fixed prospective sentinel \(t\) is also never queried, the complete transcript omits at least two source coordinates.

That contradicts the global one-hole requirement.

Hence on the no-event continuation at least one of \(s,t\) is consumed at finite time.

The conclusion is deliberately a dichotomy:

- consuming \(s\) abandons the unresolved current role and can miss a late A/B certificate;
- consuming \(t\) abandons the fixed future target.

The theorem does not claim that every form of moving handoff is impossible.

**Status: VALID.**

### 4. Moving reservations

A transient prospective block may be replaced by farther prospective blocks while the current sentinel stays open.

On a genuine C continuation, consuming each transient reservation prevents the appearance of a second permanent hole.

If a positive event occurs at a finite stage, the currently active reservation can be frozen and used after the current sentinel closes.

Thus the possible next targets can be constrained to a computable increasing reservation sequence, but the chosen member depends on the event time.

No claim is made that this sequence must meet an arbitrary infinite recurrent set infinitely often.

**Status: VALID.**

### 5. Exact finite-lane criterion

The intervals

\[
I_b=[b,h(b))
\]

form a computable interval graph.

A horizon lane is exactly a set of pairwise nonoverlapping intervals in increasing order.

For interval graphs, the minimum number of colours equals the maximum overlap depth. The proof in the mathematics record gives the required special case directly by greedy colouring in increasing left-endpoint order.

Thus finitely many computable lanes exist exactly when

\[
\sup_t |\{b\le t:t<h(b)\}|<\infty.
\]

The example \(h(b)=2b+2\) has unbounded overlap depth, so finiteness of every individual horizon does not imply a finite cover.

**Status: VALID.**

### 6. Countable lanes

Greedy colouring with natural-number colours is computable because a new interval has only finitely many earlier active intervals.

An infinite set may meet each countable colour class only finitely often, so countable pigeonhole is unavailable.

The displayed finite-concentration condition is sufficient but is not asserted for the committed recurrent status sets.

**Status: VALID.**

### 7. Conditional lane success

P4-S043 already supplies the martingale once one computable scan completes infinitely many epochs and selects A infinitely often without becoming C-trapped.

P4-S044 correctly keeps the hypothesis on the scan's event-time-selected targets.

It does not replace that hypothesis by ambient A recurrence on the whole lane.

**Status: VALID.**

### 8. Support-consumption obstruction

For the repeated recoding,

\[
u_2=x_0\oplus x_1\oplus x_2.
\]

On a fresh raw block, an exact raw evaluation of this virtual row requires all three raw bits unless other determining data have already been exposed.

The wtt use bound constrains query location but does not forbid a local computation from making such a future \(u_2\) query.

Thus there is no theorem from the use bound alone that every support block can preserve a fresh raw sentinel.

The mathematics record leaves open opportunistic partial reuse.

**Status: VALID.**

### 9. Finite transient-race obstruction

On an all-C continuation of a race among finitely many prospective sentinels, global one-hole admissibility forces all but at most one to be consumed.

Each such consumption occurs after finite interaction.

A structural partial computation can make exactly the same bounded oracle queries but delay a wrong halt by additional internal computation until after that finite consumption time.

For a prescribed finite family the finitely many delays can be chosen effectively.

This proves failure of a rate-free guarantee for the tested finite transient-race architecture. It is not stated as an impossibility theorem for every possible compiler or for the actual committed source.

**Status: VALID.**

### 10. Structural horizon countermodel

The P4-S043 recurrent-\(C_0\) local gadgets \(CCA\) and \(CAC\) are already validated finite-use self-avoiding tables on \(0^\omega\).

Prepending an ignored query to virtual row \(u_2\) in block

\[
d(b)=2b+1
\]

does not change the local status because that far block is unchanged by the raw-adjacent candidate in \(B_b\), and the answer is ignored.

The far query is not the current input, so syntactic self-avoidance remains true.

Its raw support occupies all three bits of block \(d(b)\), and the query location forces a genuine computable horizon of order

\[
h(b)=2b+2.
\]

Those intervals have unbounded overlap.

The inherited finite-family elimination still uses only nontriple recurrent \(C_0\) patterns and visible A directions.

The target is explicitly computable, so the model is correctly labelled structural only.

**Status: VALID.**

### 11. Recurrent C0 and asymmetric patterns

The retained pattern facts are used exactly:

\[
C_0:\ CAA,CAC,CCA,CCC,
\]

\[
C_1\wedge B_2\Rightarrow(A,C,B),
\qquad
C_2\wedge B_1\Rightarrow(A,B,C).
\]

P4-S044 does not infer scan-reachable recurrence from these ambient patterns. The horizon changes the source-value footprint but not the no-rate certificate-time selection problem.

**Status: VALID.**

### 12. Source-side guard

The final necessary selector statement is a direct consequence of P4-S043:

if \(X\in OH\), no computable selector scan can complete infinitely many epochs, avoid C eventually and select A infinitely often, because such a scan would carry a succeeding computable martingale.

The mathematics record does not reverse this implication.

Failure to construct such a selector is therefore not promoted to \(X\in OH\).

**Status: VALID.**

## Separation and programme guards

No actual raw one-hole destroyer for the committed \(X\) is constructed.

No proof of

\[
X\in OH
\]

is claimed.

No OH non-invariance theorem is claimed.

No strict

\[
R_2\subsetneq OH
\]

is claimed.

The retained comparison remains

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

DEF-0020 is unchanged.

No novelty, openness, prior-art, Gate-4, publication or outreach conclusion is made.

## Validation disposition

**PASS.**

P4-S044 gives a substantive sharpening of the P4-S043 reachability obstruction.

The wtt use bound does compute a finite source-value horizon, but the missing resource is now isolated as **certificate-time selector thickness**: a globally one-hole scan must continually decide which prospective future coordinates to consume while an unresolved current role may remain open forever, and no rate information forces the ambient recurrent A witnesses onto the event-time-selected subsequence.
