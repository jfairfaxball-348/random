# P4-S042 Validation

Date: 2026-10-07
Session: P4-S042
Incoming checkpoint: f14170a6275cafc23d672b3598ace83f0258cd78
Mathematics record: phase4/P4-S042_MATHEMATICS.md
Disposition: **PASS**

## Scope and authority

- Live main was pinned to the exact P4-S041 outgoing checkpoint before substantive work.
- P4-S042 was unused at that checkpoint.
- P4-S001 through P4-S041, the CAND-01 structured authority and the post-P4-S031 pivot were read.
- P4-S011, P4-S012 and P4-S039 through P4-S041 were checked directly for the exact self-avoidance, use-bound, local-code and status hypotheses used here.
- Phase 4 is OPEN and Phase 5 is CLOSED.
- The frozen P4-S015–P4-S031 bankroll line, P4-S037/P4-S038 backward-price route, ordinary raw-martingale compilation and ambiguity mass were not reopened.

## Mathematical validation

### 1. First-contact theorem

For a companion \(Z=Y\oplus\chi_S\), if \(M^Y(n)\) halts and \(M^Z(n)\) diverges, the finite target trace must query \(S\).

This is exact: if it did not, every target query would receive the same oracle answer from \(Y\) and \(Z\), so determinism would reproduce the same finite halt on \(Z\).

For local changed input \(q\in S\), syntactic self-avoidance excludes \(q\) itself, so any first changed contact lies in \(S\setminus\{q\}\).

**Status: VALID.**

### 2. Support-lasso classification

After a remote divergent trace first enters the changed support, each reached changed-coordinate companion computation has exactly three relevant semantic possibilities:

- wrong/nonbinary halt: finite Case-A refutation;
- divergence: local partiality, giving Case C iff no other local refutation exists;
- correct halt: target and companion outputs are opposite, so self-avoidance plus finite target halting forces a first contact with another changed coordinate.

Finite support then forces a directed cycle if the third arm continues.

No reverse-dependency finiteness or divergence certificate is assumed.

**Status: VALID.**

### 3. Minimal-use test

The first contacted coordinate \(q\) lies below the use \(u(n)\) of the original input under the ordinary initial-segment convention, but no inequality \(u(q)<u(n)\) follows.

Choosing a divergent input of minimal use therefore gives only: if a reached \(q\) is itself divergent, then \(u(q)\ge u(n)\). Correct-halting local computations can still cycle.

No well-founded descent follows from minimal use, minimal input or first-contact position.

**Status: VALID.**

### 4. Explicit remote-divergence countermodel

The target is \(0^\omega\).

Local truth tables were checked on all relevant companions:

\[
000,\quad 111,\quad 011,\quad 101.
\]

For \(011\):

\[
f_0(11)=0,\qquad f_1(01)=1,\qquad f_2(01)=1,
\]

so every local equation is correct and direction 1 is Case B.

For \(101\):

\[
f_0(01)=1,\qquad f_1(11)=0,\qquad f_2(10)=1,
\]

so every local equation is correct and direction 2 is Case B.

For \(111\):

\[
f_0(11)=0\ne1,\qquad f_1(11)=0\ne1,
\]

so direction 0 is Case A.

The remote input \(3\) queries only \(q_2\), returns \(0\) on the target and diverges when \(q_2=1\). All three raw columns \(111,011,101\) flip \(q_2\), so all three companions are remotely partial.

The functional is computable, finite-use and syntactically self-avoiding. The status vector

\[
(A_0,B_1,B_2)
\]

respects the P4-S041 pairwise law.

The target is computable and therefore this is explicitly only a structural countermodel, not a randomness witness.

**Status: VALID.**

### 5. Persistent Case-C necessity

If only finitely many block-direction pairs are Case C, choose a block cutoff above all of them, query the finite prefix at zero stake, and start the P4-S040 three-scan construction afterward.

Every reached later block is then decisive in all three directions, so P4-S040 yields a total computable one-hole destroyer of \(X\).

Hence

\[
X\in OH
\Longrightarrow
\text{infinitely many local Case-C block-direction pairs}.
\]

Since there are only three directions, one fixed direction occurs infinitely often.

The theorem is a necessary condition only. Infinite recurrent Case C is not claimed sufficient for \(X\in OH\).

**Status: VALID.**

## Guard checks

No step proves or assumes \(X\in OH\).

No step proves an unconditional \(X\notin OH\) result for the committed P4-S011 presentation.

No OH non-invariance theorem is claimed.

No strict \(R_2\subsetneq OH\) theorem is claimed.

The retained comparison chain remains

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.

DEF-0020 is unchanged.

No novelty, openness, prior-art, Gate-4, publication or outreach conclusion is made.

## Validation disposition

**PASS.**

P4-S042 sharpens the P4-S041 boundary in two ways:

1. remote divergence has a finite target-trace attachment to the changed support, but per-witness localization to local Case C is false in general;
2. if the actual recoded source were in \(OH\), local Case C would have to recur arbitrarily late, with one fixed raw direction recurring infinitely often.

The next bounded task should attack this recurrent fixed-direction Case-C regime rather than continue trying to localize one remote divergent equation.
