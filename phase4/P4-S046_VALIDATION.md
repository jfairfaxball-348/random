# P4-S046 Validation

Date: 2026-10-07
Session: P4-S046
Incoming checkpoint: 99b628d62895fb3c98e7c31545b818580b0b884d
Mathematics record: phase4/P4-S046_MATHEMATICS.md
Disposition: **PASS**

## Authority and scope

- P4-S045's exact outgoing prompt-setting checkpoint was 99b628d62895fb3c98e7c31545b818580b0b884d.
- Live main matched it immediately before substantive P4-S046 work.
- P4-S046 was unused at that checkpoint.
- P4-S001 through P4-S045, CAND-01 authority, the post-S031 pivot and P4-S032 through P4-S045 were checked at the pinned state.
- P4-S011, P4-S012, P4-S027 and P4-S039 through P4-S045 received direct attention.
- Frozen routes listed in the session prompt were not reopened.

**Status: VALID.**

## 1. Certificate-support definition

A candidate local block is supplied as a finite raw hypothesis. Same-block virtual oracle answers can therefore be answered from the hypothesis rather than by reading the live target block.

Outside-block oracle answers are actual target values and require raw support under the fixed recoding. P4-S027/P4-S044 put every such query below the retained finite horizon \(h(b)\).

The freshness cost \(\kappa\) counts only actual raw coordinates of the prospective target block that must be exposed; outside support is tracked separately. This is necessary because a cost-zero future certificate can still query a currently protected old sentinel through outside support.

**Status: VALID.**

## 2. Inverse-matrix calculation

\[
A=\begin{pmatrix}1&0&1\\1&1&0\\1&1&1\end{pmatrix},
\qquad
A^{-1}=\begin{pmatrix}1&1&1\\1&0&1\\0&1&1\end{pmatrix}.
\]

Thus
\[
A^{-1}e_0=110,\qquad
A^{-1}e_1=101,\qquad
A^{-1}e_2=111,
\]
and direct multiplication gives \(A(A^{-1}e_r)=e_r\).

**Status: VALID.**

## 3. Automatic-rejection theorem

For \(d_r=A^{-1}e_r\), replacing \(x\) by \(x+d_r\) changes the virtual oracle at exactly \(q_r\).

The committed autoreduction is syntactically self-avoiding on input \(q_r\), so changing only oracle coordinate \(q_r\) cannot alter that computation. It follows the target trace and halts with \(Y(q_r)\), while the candidate expects the opposite bit. Hence this finite trace rejects the candidate.

No target value is inserted as a program parameter; all eight local raw hypotheses may be dovetailed.

**Status: VALID.**

## 4. One-bit freshness theorem

For role 0 the opposite-\(x_0\) slice has differences
\[
100,110,101,111=e_0,d_0,d_1,d_2.
\]
Case \(A_0\) rejects \(e_0\); the automatic theorem rejects the others.

For role 1, after observing \(x_2\), the wrong-\(x_1\) pair is
\[
010,110=e_1,d_0.
\]

For role 2, after observing \(x_1\), the wrong-\(x_2\) pair is
\[
001,101=e_2,d_1.
\]

Therefore every actual A witness has local cost at most one. Target correctness is used only to guarantee that the true slice is never fully rejected; no runtime bound is used.

**Status: VALID.**

## 5. Common \(011/110\) diagonal

The fourth difference in each full wrong slice for roles 1 and 2 is
\[
\delta=011=e_1+e_2,
\qquad
A\delta=c_1+c_2=110.
\]

All other candidates are already rejected. Therefore a block-free slice certificate exists exactly when this diagonal candidate is finitely rejected.

If the diagonal is accepted or divergence-only, no finite rejection exists for it. The “if and only if” is correctly scoped to P4-S046's finite positive slice-certificate system.

**Status: VALID.**

## 6. Structural sharpness gadgets

For the \(CAC\) table:

- \(111\) has only correct halts where defined plus divergence, so \(C_0\);
- \(011\) has \(f_0(11)=1\) against expected \(0\), so \(A_1\);
- \(101\) has only correct halts where defined plus divergence, so \(C_2\);
- diagonal \(110\) has trace \((1,1,\uparrow)\), so no finite rejection.

Thus the unique visible A is \(A_1\) and has exact cost one.

For the \(CCA\) table:

- \(111\) is \(C_0\);
- \(011\) is \(C_1\);
- \(101\) is finitely refuted at \(q_1\), so \(A_2\);
- \(110\) again has \((1,1,\uparrow)\).

Thus the unique visible A is \(A_2\) and has exact cost one.

The tables are block-local and syntactically self-avoiding. The target is \(0^\omega\), so the result is correctly labelled structural only.

**Status: VALID.**

## 7. Recurrent-C, B-arm and randomness guards

The cost-one gadgets show an access obstruction independent of P4-S045's delay-only obstruction: the local table may be fixed immediately and still require one cross-role target bit for positive slice certification.

For \(ACB/ABC\), \(A_0\) already has local cost zero, so B cannot lower that local cost. No universal claim about every alternative B compiler is made.

The session does not turn “must read a bit” into a prediction of that bit. No computable-randomness contradiction is inferred from access cost alone.

**Status: VALID.**

## 8. Certification graph and separation guard

A usable graph edge includes outside-support avoidance and a total one-hole fallback, not merely semantic A status.

An infinite computably generated path of such edges would concatenate to a total one-hole scan with infinitely many correct certified sentinel wagers.

P4-S046 does not establish such a path and does not infer one from finite branching. It proves neither
\[
X\in OH
\]
nor
\[
X\notin OH.
\]

The retained separation status
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR
\]
is unchanged.

**Status: VALID.**

## Final disposition

**PASS.**

P4-S046 establishes a source-specific same-block access theorem and a sharp structural exact-cost-one obstruction while preserving all source-side and novelty guards.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 unchanged. Phase 4 OPEN; Phase 5 CLOSED.
