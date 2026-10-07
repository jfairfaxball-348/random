# P4-S047 Close

Date: 2026-10-07
Session: P4-S047
Status: **COMPLETED / VALIDATED**
Incoming checkpoint: 751ce6dbf35c2ea4e34e02280e31ddeaab8871d1

Scope: current-hole-uniform future Case-A certification and old-hole outside-support collision.

## Results

- formalized the two finite counterfactual source completions \(X^{[0]},X^{[1]}\) at the current raw sentinel without using the actual hole value as a program parameter;
- computed the exact safe-row sets
  \[
  \operatorname{Safe}(0)=\varnothing,\qquad
  \operatorname{Safe}(1)=\{u_0\},\qquad
  \operatorname{Safe}(2)=\{u_1\};
  \]
- defined current-hole-uniform finite slice certificates and separated semantic existence, positive discovery and computable indefinite selection;
- proved a safe-trace theorem: rejection traces avoiding old hole-dependent rows are automatically valid under both old-hole hypotheses;
- defined two-branch future fixedness and proved it restores all three P4-S046 automatic \(A^{-1}e_r\) rejections in both branches;
- obtained the conditional low-cost CHU bounds:
  \[
  A_0:\kappa=0,\qquad
  A_1:\kappa\le1,\qquad
  A_2:\kappa\le1
  \]
  when the raw-adjacent rejection also survives both old-hole hypotheses;
- showed the future \(A_1\) read of \(x_2\) and future \(A_2\) read of \(x_1\) do not themselves interact with the older hole;
- defined syntactic collision, avoidable collision, unavoidable witness collision, branch-harmless collision and genuine current-hole nonuniformity;
- built a sharp computable finite-use syntactically self-avoiding structural \(0^\omega\) old-row-gated family;
- showed for every current raw role and every future A role that the true branch can retain the visible A and P4-S046 local cost while the alternate old-hole branch makes every relevant future local computation diverge;
- used \(CAC/CCA\) for exact cost-one recurrent nontriple \(C_0\) and an explicit \(ACB\) table for block-free \(A_0\);
- therefore proved no nonempty role-only CHU transition matrix is forced by the retained abstract hypotheses;
- showed finite use does not force infinitely many future visible A candidates outside the old-hole collision set;
- proved failure of CHU does not itself reveal the current unread bit, because both old-hole branches are counterfactual simulations;
- proved any finite wrong/nonbinary autoreduction equation under one old-hole completion eliminates that completion and predicts the current sentinel;
- built a canonical global-refutation one-hole scan which dovetails all equations under both hole hypotheses;
- proved hypothetical \(X\in OH\) forces that scan eventually to reach a false raw-radius-one completion which is a partial fixed point of \(M\), so every defined equation is correct and only divergence can hide the false branch;
- refined the usable certification graph to CHU edges and proved an infinite computable CHU usable path would imply
  \[
  X\notin OH;
  \]
- obtained no such path for the committed source;
- did not prove \(X\in OH\) or \(X\notin OH\).

## New boundary

The future target-block cost is no longer the main issue.

The exact positive resources are:

\[
\text{safe old-row traces}
\]

or, more generally,

\[
\text{two-branch future fixedness plus compatible two-branch A rejection}.
\]

The sharp structural obstruction is:

\[
\text{one old hole-dependent virtual row can gate every later low-cost A witness}.
\]

The next source-side problem is therefore **persistent partial-fixed-point old-hole sensitivity**: determine whether the actual committed computably random wtt-autoreducible source lets one old raw perturbation remain semantically essential for infinitely many later A certificates, or whether that sensitivity can be effectively escaped and converted into CHU usable edges.

## Records

- phase4/P4-S047_MATHEMATICS.md
- phase4/P4-S047_VALIDATION.md
- phase4/P4-S047_CLOSE.md

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 unchanged. Phase 4 OPEN; Phase 5 CLOSED.

Owner/external blocker: **NONE**.

Recommended next session: **P4-S048**, persistent old-hole sensitivity of future A-certificate computations on the actual committed source.
