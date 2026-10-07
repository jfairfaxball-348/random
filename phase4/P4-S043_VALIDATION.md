# P4-S043 Validation

Date: 2026-10-07
Session: P4-S043
Incoming checkpoint: 9027605cad65de83cca6ae23e7986cf41ceb9424
Mathematics record: phase4/P4-S043_MATHEMATICS.md
Disposition: **PASS**

## Scope and authority

- Live main was pinned to the exact final P4-S042 checkpoint before substantive work.
- P4-S043 was unused at that checkpoint.
- P4-S001 through P4-S042, the selected CAND-01 authority and the post-P4-S031 pivot were read.
- P4-S011, P4-S012 and P4-S039 through P4-S042 were checked directly for the self-avoidance, raw-adjacent status, one-hole and recurrence hypotheses used here.
- The frozen P4-S015–P4-S031 bankroll line, P4-S037/P4-S038 backward-price route, ordinary raw-martingale compilation, ambiguity mass and general radius-one totalization were not reopened.
- Phase 4 remains OPEN and Phase 5 CLOSED.

## Mathematical validation

### 1. Exact local status list

For target block \(000\), syntactic self-avoidance reduces the relevant local table to

\[
a=f_0(11),\ b=f_1(11),\ c=f_1(01),\ d=f_2(01),\
e=f_0(01),\ f=f_2(10),\ g=f_2(11).
\]

The three companions test

\[
(a,b,g)\text{ against }111,
\]
\[
(a,c,d)\text{ against }011,
\]
\[
(e,b,f)\text{ against }101.
\]

The displayed 14-row table was checked row by row using:

- A = at least one halting wrong value;
- B = every required value halts correctly;
- C = no wrong halt and at least one divergence.

It realizes exactly

\[
AAA,AAB,AAC,ABA,ABB,ABC,ACA,ACB,ACC,BAA,CAA,CAC,CCA,CCC.
\]

Every excluded pattern violates at least one retained implication

\[
B_0\Rightarrow A_1,A_2,\qquad
B_1\Rightarrow A_0,\qquad
B_2\Rightarrow A_0.
\]

Hence the pairwise law is complete for the local self-avoiding finite-table geometry.

**Status: VALID.**

### 2. Fixed-\(C_i\) pattern classification

Filtering the 14 patterns gives:

\[
C_0:\quad CAA,\ CAC,\ CCA,\ CCC,
\]

\[
C_1:\quad ACA,\ ACB,\ ACC,\ CCA,\ CCC,
\]

\[
C_2:\quad AAC,\ ABC,\ ACC,\ CAC,\ CCC.
\]

Thus every nontriple fixed-\(C_i\) block has at least one Case-A direction.

The requested asymmetric cases are exact:

\[
C_1\wedge B_2\Rightarrow (A,C,B),
\]

\[
C_2\wedge B_1\Rightarrow (A,B,C).
\]

Finite pigeonhole applies only after restricting to an infinite fixed-\(C_i\) block set; it does not by itself make that recurrent pattern computably selectable.

**Status: VALID.**

### 3. Asynchronous one-role scan

The construction selects one sentinel role before opening a fresh block.

Inside-block values for the two raw completions are supplied as finite hypotheses, so no raw query of the sentinel is required to simulate the local candidate equations. Outside-block virtual queries are answered by querying fresh raw supports.

On the actual source:

- the actual endpoint cannot be finitely refuted;
- a finite refutation of the other endpoint therefore gives a correct sentinel prediction;
- two accepted endpoints give Case B and a zero-stake closure;
- Case C supplies neither positive event.

The least-fresh background sweep means an unresolved target epoch still emits infinitely many scan bits and eventually queries every raw coordinate except the sentinel. Hence the scan is total and has one hole, rather than becoming a partial scan.

After a positive A/B resolution the sentinel is queried and finite prefix restoration produces another completely fresh block.

No status of an unselected direction is needed.

**Status: VALID.**

### 4. Martingale success criterion

The output martingale holds on fillers and selected Case-B sentinels and bets all capital only after a finite refutation certifies the selected Case-A sentinel.

Every target Case-A bet is correct.

Therefore infinitely many selected Case-A completed epochs imply unbounded doubling.

The theorem is conditional on the scan's own reached status sequence. It does not replace that condition by ambient raw-block recurrence.

**Status: VALID.**

### 5. Raw recurrence versus scan reachability

A local status computation may expose raw support in later blocks before its current sentinel closes.

Consequently the next completely fresh block is endogenous to that scan's finite evaluation footprint.

It is therefore invalid to infer

\[
A_j\text{ infinitely often on raw blocks}
\]

from

\[
A_j\text{ infinitely often on blocks reached by a fixed scan}.
\]

The mathematics record preserves this distinction and does not use the invalid inference.

**Status: VALID.**

### 6. Total-abandonment theorem

If every unresolved sentinel is eventually consumed on every transcript and prefix restoration follows, then every epoch completes and the completely queried prefix tends to infinity.

The scan therefore queries every coordinate exactly once.

An exhaustive computable adaptive no-repeat scan is an effective fair-coin isomorphism: to recover source bit \(n\), simulate the transcript until coordinate \(n\) is queried.

Thus it preserves computable randomness and cannot destroy the settled \(X\in CR\).

The theorem does not say every mixed waiting/abandonment architecture is exhaustive. It applies exactly when closure is guaranteed in every epoch on every branch.

**Status: VALID.**

### 7. Finite-family structural countermodel

For fixed recurrent \(C_0\), the two patterns

\[
CCA,\qquad CAC
\]

are both realizable, nontriple and contain a visible A role. They respectively trap role sets \(\{0,1\}\) and \(\{0,2\}\).

For fixed recurrent \(C_1\), use

\[
CCA,\qquad ACC.
\]

For fixed recurrent \(C_2\), use

\[
CAC,\qquad ACC.
\]

At a new block, each still-active policy chooses its role from the already fixed finite transcript before the new block gadget is selected. Hence the block pattern can be chosen computably to trap at least one still-active member. A finite family is exhausted after finitely many such blocks.

The three local gadget tuples in the mathematics record were checked against the Proposition-1 table.

Applying the chosen gadget independently blockwise yields a computable finite-use syntactically self-avoiding functional correct on target \(0^\omega\).

The target is computable, so this is explicitly a structural countermodel and is not used as a computable-randomness witness.

**Status: VALID.**

### 8. Triple-C guard

The finite-family countermodel proves only that recurrence plus the local status law and the tested wait-family geometry do not force triple-C recurrence.

It does not prove that the actual committed \(X\in OH\), nor that a surviving \(X\in OH\) cannot have recurrent triple C.

Accordingly the P4-S041 shared-divergence identities are retained but not used as a new cross-block resource.

**Status: VALID.**

## Guard checks

No step assumes \(X\in OH\).

No unconditional raw one-hole destroyer for the committed \(X\) is claimed.

No recurrent-triple-C necessity theorem is claimed.

No OH non-invariance theorem is claimed.

No strict

\[
R_2\subsetneq OH
\]

theorem is claimed.

The retained comparison remains

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

DEF-0020 is unchanged.

No novelty, openness, prior-art, Gate-4, publication or outreach conclusion is made.

## Validation disposition

**PASS.**

P4-S043 establishes a genuine positive extension of P4-S040—own-role A/B closure can be fully asynchronous—while locating the next obstruction more sharply.

The missing resource is not another local A/B/C law. It is a computable online role selector and fresh-block reachability theorem capable of converting ambient recurrent A witnesses into recurrent A witnesses on one scan's own reached blocks without giving up the branchwise permanent-hole resource.
