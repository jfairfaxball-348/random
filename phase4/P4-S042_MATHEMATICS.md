# P4-S042 — target-trace contact, support lassos and persistent local Case C

Date: 2026-10-07
Session: P4-S042
Incoming checkpoint: f14170a6275cafc23d672b3598ace83f0258cd78
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding
Result: **EVERY RADIUS-ONE REMOTE DIVERGENCE MUST CONTACT THE CHANGED BLOCK ON THE FINITE HALTING TARGET TRACE, BUT ITERATING ONLY SUCH FINITELY JUSTIFIED CONTACTS NEED NOT DESCEND TO A LOCAL DIVERGENCE. THE CHAIN CAN TERMINATE IN A FINITE LOCAL REFUTATION OR CLOSE INTO EXACTLY THE P4-S041 CORRECT LOCAL DEPENDENCY CYCLES. AN EXPLICIT COMPUTABLE SELF-AVOIDING FINITE-USE COUNTERMODEL HAS REMOTE DIVERGENCE IN ALL THREE RAW DIRECTIONS WHILE THE LOCAL STATUSES ARE A_0,B_1,B_2, SO REMOTE PARTIALITY IS COMPATIBLE WITH FULL P4-S040 LOCAL DECISIVENESS. MINIMAL WTT USE GIVES NO WELL-FOUNDED DESCENT. NEVERTHELESS ANY SURVIVING X IN OH MUST HAVE ARBITRARILY LATE LOCAL CASE-C BLOCKS; IN FACT SOME FIXED RAW DIRECTION IS CASE C ON INFINITELY MANY BLOCKS. THUS A SINGLE RADIUS-ONE OR REMOTE DIVERGENCE WITNESS IS FAR TOO WEAK: OH SURVIVAL REQUIRES RECURRENT LOCAL DIVERGENCE-ONLY OBSTRUCTION.**

## Authority, uniqueness and scope

Live main was pinned at

\[
\texttt{f14170a6275cafc23d672b3598ace83f0258cd78},
\]

the exact outgoing P4-S041 checkpoint. No P4-S042 mathematics, validation or close record existed at that checkpoint.

P4-S001 through P4-S041, the selected CAND-01 authority, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, and especially P4-S011, P4-S012, P4-S039, P4-S040 and P4-S041 were read as authority.

All validated mathematics through P4-S041 is frozen. The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence, P4-S037/P4-S038 backward-price route, ordinary raw-martingale compilation and ambiguity mass are not reopened.

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Let \(Y\) be the P4-S011 computably random source, \(M\) its committed syntactically self-avoiding wtt autoreduction, \(H\) the repeated three-bit recoding, and \(X=H^{-1}(Y)\). Retain

\[
X\in CR,\qquad H(X)=Y\notin OH.
\]

No statement \(X\in OH\) is assumed.

## 1. Remote versus local radius-one partiality

Fix a raw block \(B=\{q_0,q_1,q_2\}\) and raw direction \(i\). The corresponding virtual flip support is

\[
S_i=\operatorname{supp}(c_i),
\]

where

\[
S_0=\{q_0,q_1,q_2\},\qquad
S_1=\{q_1,q_2\},\qquad
S_2=\{q_0,q_2\}.
\]

Write

\[
Z_i=Y\oplus\chi_{S_i}.
\]

The following notions remain distinct.

- **local partiality:** \(M^{Z_i}(q_r)\uparrow\) for at least one \(q_r\in B\);
- **remote partiality:** \(M^{Z_i}(n)\uparrow\) for at least one \(n\notin B\);
- **local Case C:** at least one local block equation diverges and every local equation which halts is correct for \(Z_i\);
- **decisive despite partiality:** remote or other divergence may exist, but the local status is A or B in the P4-S040 sense.

In particular global partiality does not determine the local A/B/C status.

## 2. A divergent companion must be touched by the halting target trace

Suppose

\[
M^{Z_i}(n)\uparrow
\]

while, as always on the target,

\[
M^Y(n)\downarrow=Y(n).
\]

Let \(T_Y(n)\) be the finite oracle-query trace of the target computation \(M^Y(n)\).

### Theorem 1 — first changed-coordinate contact

The target trace \(T_Y(n)\) queries at least one coordinate in \(S_i\).

More precisely, let \(q\) be the first coordinate of \(S_i\) queried along \(T_Y(n)\). Up to the query of \(q\), the computations with oracles \(Y\) and \(Z_i\) have identical machine states, identical queries and identical oracle answers. At \(q\) they first receive different oracle answers.

#### Proof

If \(T_Y(n)\) queried no coordinate in \(S_i\), then \(Y\) and \(Z_i\) would give identical answers at every oracle query made by the finite target computation. Determinism would force \(M^{Z_i}(n)\) to execute the same finite computation and halt with the same output. This contradicts \(M^{Z_i}(n)\uparrow\).

For the refined statement, before the first query into \(S_i\) every queried coordinate lies outside the difference support, so the two computations agree step for step. At the first queried \(q\in S_i\), the oracle answers differ. ∎

Thus every remote divergence is genuinely dependent on the changed block in a finite target-trace sense. This is positive finite information about the target computation. It is not a certificate that the companion computation diverges.

If \(n=q_r\in S_i\), syntactic self-avoidance excludes \(q_r\) itself from the input-\(q_r\) trace. Hence the first changed contact lies in

\[
S_i\setminus\{q_r\}.
\]

## 3. The support-lasso relation

For a fixed radius-one companion \(Z_i\), orient dependencies only by halting target traces.

- If \(M^{Z_i}(n)\uparrow\), draw \(n\leadsto q\) where \(q\in S_i\) is the first changed coordinate queried by the finite target trace \(M^Y(n)\).
- If \(q\in S_i\) and \(M^{Z_i}(q)\downarrow=Z_i(q)\), then the target and companion computations at input \(q\) halt with opposite outputs. Since input \(q\) is never queried, their first changed contact is some
  \[
  q'\in S_i\setminus\{q\}.
  \]
  Draw \(q\to q'\).

The second edge is exactly the finite first-difference edge used in P4-S041, but here it is entered from a remote divergent computation.

### Theorem 2 — support-lasso classification

Starting from any remote divergent input \(n\notin B\), first-contact tracing reaches \(S_i\) in one finite target-trace step. Thereafter exactly one of the following semantic outcomes occurs.

1. **Finite local refutation.** A reached local input \(q\in S_i\) halts on \(Z_i\) with a wrong binary or nonbinary output. Then direction \(i\) is Case A.
2. **Local divergence.** A reached local input \(q\in S_i\) diverges on \(Z_i\). This is genuine local partiality. The direction is Case C exactly when no other local equation gives a finite refutation; otherwise the direction is still Case A.
3. **Correct-halting lasso.** Every reached changed-coordinate computation halts correctly for \(Z_i\). Since \(S_i\) is finite and every such vertex points to another vertex of \(S_i\), the trace enters a directed cycle of correct local halts. If all remaining local block equations also halt correctly, the direction is Case B even though the original outside equation diverges.

#### Proof

Theorem 1 supplies the first edge into \(S_i\). At a reached changed coordinate \(q\), a wrong/nonbinary halt gives arm 1, divergence gives arm 2, and a correct halt gives a first-difference edge to another member of \(S_i\). Continuing only in the third case produces an infinite walk on finite \(S_i\), hence a repeated vertex and a directed cycle. ∎

The important point is that the cycle arm is not pathological bookkeeping. It is exactly the positive P4-S041 Case-B geometry. Remote divergence can feed into a locally closed fixed-point cycle.

## 4. Minimal use does not provide a descent

Let \(u(n)\) be a computable wtt use bound.

A first-contact edge

\[
n\leadsto q
\]

shows only that \(q<u(n)\) under the usual initial-segment use convention. It gives no inequality between \(u(q)\) and \(u(n)\).

Choose, semantically, a divergent input \(n\) of minimal \(u(n)\) for a fixed companion. If a reached local input \(q\) also diverges, minimality only implies

\[
u(q)\ge u(n).
\]

If \(q\) halts correctly, no comparison of uses follows at all, and the support-lasso can close into a local cycle.

### Proposition 3 — no well-founded use measure is forced

Neither minimal input number, minimal wtt use, nor minimal position of first changed contact forces the dependency relation of Theorem 2 to descend.

The wtt use map is forward information. A queried coordinate can have a larger, equal or smaller use on its own input, and correct local computations may cycle inside \(S_i\).

Therefore minimal-use selection does not reduce remote divergence to local Case C.

## 5. Exact support geometry

For

\[
S_1=\{q_1,q_2\},
\]

the correct-halting lasso has no choice:

\[
q_1\leftrightarrow q_2.
\]

For

\[
S_2=\{q_0,q_2\},
\]

it is

\[
q_0\leftrightarrow q_2.
\]

For

\[
S_0=\{q_0,q_1,q_2\},
\]

the correct-halting lasso is a two-cycle with a tail or an oriented three-cycle, exactly as in P4-S041.

Thus the rigidity of the two-coordinate supports does **not** make remote divergence impossible. It merely says that if the changed local equations all halt correctly, the remote divergent computation is attached to an already closed two-cycle.

## 6. Exact computable countermodel: remote partiality with full local decisiveness

The support-lasso obstruction is realizable without any noncomputable parameter.

Take the computable target

\[
Y=0^\omega
\]

and one block

\[
(q_0,q_1,q_2)=(0,1,2).
\]

Define a syntactically self-avoiding finite-use functional \(N\) on the three local inputs by the following Boolean tables.

For input \(q_0\), query only \((q_1,q_2)\) and set

\[
f_0(00)=0,\qquad f_0(11)=0,\qquad f_0(01)=1,\qquad f_0(10)=0.
\]

For input \(q_1\), query only \((q_0,q_2)\) and set

\[
f_1(00)=0,\qquad f_1(01)=1,\qquad f_1(11)=0,\qquad f_1(10)=0.
\]

For input \(q_2\), query only \((q_0,q_1)\) and set

\[
f_2(00)=0,\qquad f_2(01)=1,\qquad f_2(10)=1,\qquad f_2(11)=1.
\]

Let \(n=3\). On input \(n\), query \(q_2\); output \(0\) if the answer is \(0\), and diverge forever if the answer is \(1\). On every other input output \(0\) without oracle queries.

Then \(N^Y(m)=Y(m)\) for every \(m\), and \(N\) is syntactically self-avoiding with a computable finite use bound.

The three raw-adjacent block companions of \(000\) are

\[
111,\qquad 011,\qquad 101.
\]

Direct table inspection gives:

- \(011\) is locally accepted: direction \(1\) is Case \(B_1\);
- \(101\) is locally accepted: direction \(2\) is Case \(B_2\);
- \(111\) is finitely refuted at \(q_0\) and \(q_1\): direction \(0\) is Case \(A_0\).

Yet every one of the three companions flips \(q_2\), so

\[
N^{111}(3)\uparrow,\qquad
N^{011}(3)\uparrow,\qquad
N^{101}(3)\uparrow.
\]

### Theorem 4 — genuinely remote radius-one partiality is possible

A computable syntactically self-avoiding finite-use autoreduction can have radius-one remote divergence in all three raw directions while every raw direction is locally P4-S040-decisive.

In the explicit example the local status vector is

\[
(A_0,B_1,B_2).
\]

For directions \(1\) and \(2\), the divergent outside equation is attached respectively to the forced correct local two-cycles. It does not localize to Case C.

This countermodel is a structural machine-theoretic obstruction only. Its target \(0^\omega\) is not computably random, so it says nothing directly about whether the committed P4-S011 source has the same pattern.

It nevertheless proves that self-avoidance, finite use, the three supports and the P4-S041 cycle theorem alone cannot imply

\[
\text{remote radius-one divergence}\Longrightarrow\text{local Case C}.
\]

## 7. Pairwise status law: exact limit of strengthening

The P4-S041 law remains

\[
B_0\Rightarrow A_1,A_2,\qquad
B_1\Rightarrow A_0,\qquad
B_2\Rightarrow A_0.
\]

The explicit countermodel realizes the second and third implications simultaneously:

\[
B_1\wedge B_2\wedge\text{remote partiality in all directions}
\]

coexists with \(A_0\).

Hence remote partiality in a direction can coexist with local Case B. A remote target trace in one direction supplies no finite wrong-halt witness in another direction.

The one sharp no-A consequence from P4-S041 is unchanged:

\[
\neg A_0\wedge\neg A_1\wedge\neg A_2
\Longrightarrow
C_0\wedge C_1\wedge C_2.
\]

Remote traces do not strengthen this implication by finite evidence.

## 8. Why the obvious localization compiler is not obtained

Theorem 1 explains a basic syntactic tension.

A remote divergence depends on a changed coordinate \(q\) because the target input-\(n\) trace queries \(q\). But an autoreduction equation whose input is \(q\) is forbidden from querying \(q\). Directly duplicating the outside computation into the contacted local equation therefore violates the very self-avoidance condition required at \(q\).

Routing through another changed coordinate gives the support-lasso of Theorem 2 and can close into a correct cycle. Choosing a divergent outside equation canonically would itself require negative divergence information. Minimal use does not repair that.

Thus P4-S042 obtains no permitted uniform target-equivalent localization normal form \(M'\). In particular no construction uses \(Y\) as a noncomputable program parameter.

This is weaker than an impossibility theorem for every conceivable special compiler for the committed \(M\). The exact conclusion is that the finite target-trace and wtt-use resources tested here do not force such a compiler.

## 9. Remote partiality is harmless whenever local decisiveness is eventually available

P4-S040 uses only local A/B decisiveness. It never requires global totality of the companion.

Therefore the existence of remote divergence, even in all three raw directions, is irrelevant once local decisiveness is established on the blocks used by the raw scans.

This can be sharpened to a tail theorem.

### Theorem 5 — persistent local Case C is necessary for \(X\in OH\)

Suppose there is a raw block cutoff \(N\) such that every block \(B\) above \(N\) and every raw direction \(i\in\{0,1,2\}\) is locally decisive, i.e. is Case A or Case B.

Then

\[
X\notin OH.
\]

Consequently,

\[
X\in OH
\Longrightarrow
\text{there are infinitely many block-direction pairs }(B,i)\text{ of local Case C}.
\]

By the finite pigeonhole principle, if \(X\in OH\) then some fixed direction \(i\) is Case C on infinitely many raw blocks.

#### Proof

Query the finitely many raw coordinates through the cutoff at zero stake, and then start the P4-S040 synchronized three-scan construction on fresh blocks above the cutoff. By hypothesis every reached block is decisive in all three directions. P4-S040 therefore supplies one total computable raw one-hole scan whose output martingale succeeds on \(X\). Thus \(X\notin OH\).

Taking the contrapositive shows that \(X\in OH\) forbids every such tail cutoff, so Case-C pairs occur arbitrarily far out. Since there are only three directions, one direction occurs infinitely often. ∎

A slightly more operational formulation is also useful: for every delayed-start version of the P4-S040 synchronized construction, if \(X\in OH\) then that run must eventually encounter a reached block with at least one Case-C direction. Otherwise that delayed-start run itself destroys \(X\).

This is the strongest source-side consequence of P4-S042.

It strictly separates:

- one radius-one divergent perturbation;
- one remote divergent equation;
- one local Case-C direction;
- arbitrarily late local Case-C blocks;
- a fixed direction with infinitely many Case-C blocks.

Only the latter recurrence is forced by the assumption \(X\in OH\).

## 10. Separation status

P4-S042 does **not** determine the actual local status pattern of the committed \(M\) on infinitely many blocks.

Therefore it does not prove

\[
X\notin OH
\]

and does not prove

\[
X\in OH.
\]

No OH non-invariance witness is obtained, and no strict

\[
R_2\subsetneq OH
\]

conclusion follows.

The sustained inclusions remain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

The P4-S032 null-ambiguity theorem remains available but is not used as an invariant here.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## 11. New exact boundary

The P4-S041 radius-one boundary is now sharpened in two opposite directions.

First, **per-witness localization fails**: a remote radius-one divergence can attach to a closed correct local dependency cycle while the companion is locally Case B.

Second, **OH survival forces recurrence**: if the recoded source really lies in \(OH\), divergence-only local obstruction cannot be a one-off accident. Some fixed raw direction must exhibit local Case C infinitely often.

The next bounded problem is therefore no longer to localize one remote divergent equation. It is to exploit or obstruct **recurrent fixed-direction local Case C** across arbitrarily late fresh blocks, using the exact pairwise raw-adjacent laws without returning to general totalization or the frozen pricing machinery.
