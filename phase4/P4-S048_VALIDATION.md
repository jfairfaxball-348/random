# P4-S048 Validation

Date: 2026-10-07
Session: P4-S048
Incoming checkpoint: caba6f96b665e067661750e40e08164fb959968c
Mathematics record: phase4/P4-S048_MATHEMATICS.md
Disposition: **PASS**

## Authority and scope

Live `main` matched the exact P4-S047 outgoing checkpoint; P4-S048 was unused. Required P4-S001 through P4-S047, CAND-01, pivot and special-focus authority was read at the pinned state. Frozen routes were not reopened.

**Status: VALID.**

## 1. Partial-neighbour trichotomy and lasso

At an unresolved P4-S047 global-refutation epoch the false completion \(Z\) satisfies

\[
M^Z(n)\downarrow\Longrightarrow M^Z(n)=Z(n)\in\{0,1\}.
\]

For \(n\notin B_b\), \(Y(n)=Z(n)\). If the finite target trace avoids the old changed support \(S_i\), the \(Z\)-trace is identical. If it contacts \(S_i\), partial fixedness leaves only a correct halt with the same value or divergence. A finite wrong/nonbinary halt would already refute the completion.

For a divergence-sensitive future equation, P4-S042 gives finite target-trace contact with \(S_i\). At a reached \(q\in S_i\), either \(M^Z(q)\uparrow\), or both \(Y\)- and \(Z\)-computations halt correctly with opposite values. Self-avoidance then forces contact with another member of \(S_i\). Iteration on finite \(S_i\) yields old-support divergence or a correct-halting cycle. The P4-S042 finite-refutation arm is genuinely absent.

**Status: VALID.**

## 2. Canonical role lists

Retain

\[
d_0=110,\qquad d_1=101,\qquad d_2=111,
\]

with virtual effects \(e_0,e_1,e_2\).

The canonical P4-S046 low-cost wrong slices are

\[
A_0:\ e_0,d_0,d_1,d_2,
\]

\[
A_1\text{ after future }x_2:\ e_1,d_0,
\]

\[
A_2\text{ after future }x_1:\ e_2,d_1.
\]

In the false old-hole branch, candidate \(d_r\) differs from \(Z\) only at future input \(q_r\). Syntactic self-avoidance makes its canonical input-\(q_r\) computation exactly \(M^Z(q_r)\). A halt is correct by partial fixedness and therefore rejects the unit-flipped candidate.

Hence the exact canonical target-equation lists are

\[
F_0=\{q_0,q_1,q_2\},\qquad
F_1=\{q_0\},\qquad
F_2=\{q_1\}.
\]

The separate false-branch raw-adjacent rejection \(R_j^Z(c)\) concerns a doubly perturbed oracle and is not controlled by partial fixedness of \(Z\).

**Status: VALID.**

## 3. Structural Family F

On target \(Y_*=0^\omega\), close the old changed support by mutual copying for size two or a directed copy cycle for size three. Then both \(Y_*\) and \(Z_*=Y_*\oplus\chi_{S_i}\) are correct on the old block and self-avoidance holds.

On future blocks, query fixed \(p\in S_i\) first. If \(p=0\), run the validated \(ACB,CAC,CCA\) target gadgets for roles \(0,1,2\).

If \(p=1\), make exactly

\[
r_0=0,\qquad r_1=0,\qquad r_2=1
\]

diverge and all other future target inputs output \(0\). These \(r_j\) lie in \(F_j\), so \(Z_*\) is a global partial fixed point with one recurrent listed divergence.

Choose

\[
a_0=1,\qquad a_1=1,\qquad a_2=0.
\]

Each \(a_j\) lies in \(\operatorname{supp}(c_j)\) and differs from \(r_j\). The false raw-adjacent candidate expects \(1\) at \(q_{c,a_j}\), while that computation outputs \(0\), so \(R_j^{Z_*}(c)\) remains finite and positive.

Thus listed fixedness divergence can recur while raw-adjacent rejection survives.

**Status: VALID.**

## 4. Structural Family R

Keep the same old-support cycles. When \(p=1\), each future input queries only the other two coordinates of its future virtual block and outputs \(0\) exactly when both are \(0\); otherwise it diverges.

On false target block \(000\), every future equation halts correctly, so \(Z_*\) is a total global fixed point.

A unit flip at input \(q_r\) is invisible to that input, which still sees the other two bits \(00\); its output \(0\) gives the canonical automatic rejection.

For

\[
c_0=111,\qquad c_1=011,\qquad c_2=101,
\]

each support has size at least two. Therefore every local input on the false raw-adjacent candidate sees at least one \(1\) among its other two block coordinates and diverges. The raw-adjacent rejection can thus fail by divergence even when all false-neighbour target equations are total.

**Status: VALID.**

## 5. Effectivity and guards

Divergence supplies no positive finite elimination. Observing one branch halt does not show that the other will never halt.

The canonical escape theorem explicitly requires a total computable one-hole-safe operator returning all finite role-kernel evidence plus legal fallback/handoff. Under that hypothesis, iteration gives an infinite computable CHU path and \(X\notin OH\).

Under hypothetical \(X\in OH\), only the algorithm-relative contrapositive is asserted. No semantic infinitude of all bad future blocks is inferred, and finiteness without a computable escape bound is not treated as effective.

**Status: VALID.**

## 6. Separation status

No CHU path is constructed for the committed source. P4-S048 proves neither \(X\in OH\) nor \(X\notin OH\), no OH non-invariance theorem, and no strict \(R_2\subsetneq OH\) separation.

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 unchanged. Phase 4 OPEN; Phase 5 CLOSED.

**Status: VALID.**

## Final disposition

**PASS.**

P4-S048 reduces the canonical false-neighbour fixedness burden to exact finite role lists and proves that this burden and false-branch raw-adjacent rejection are structurally independent, even under global partial fixedness.
