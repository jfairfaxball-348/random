# P4-S046 Close

Date: 2026-10-07
Session: P4-S046
Status: **COMPLETED / VALIDATED**
Incoming checkpoint: 99b628d62895fb3c98e7c31545b818580b0b884d

Scope: future Case-A certificate support and raw freshness cost for the committed recoded P4-S011 source.

## Results

- formalized finite rejection support, same-block slice certificates and local freshness cost \(\kappa\);
- separated same-block live access from finite outside raw support below the retained horizon \(h(b)\);
- computed
  \[
  A^{-1}e_0=110,\qquad A^{-1}e_1=101,\qquad A^{-1}e_2=111;
  \]
- proved each \(A^{-1}e_r\) candidate is automatically finitely rejected because it changes only virtual input \(q_r\), which the input-\(q_r\) computation syntactically avoids;
- proved the source-specific access bound
  \[
  A_0\Rightarrow\kappa=0,\qquad
  A_1\Rightarrow\kappa\le1,\qquad
  A_2\Rightarrow\kappa\le1;
  \]
- therefore eliminated local cost two for every actual Case-A witness under the displayed recoding;
- isolated the exact common obstruction to block-free \(A_1/A_2\): raw difference \(011\), virtual difference \(110\);
- built block-local finite-use self-avoiding \(CAC\) and \(CCA\) structural gadgets on \(0^\omega\) whose unique visible A has exact local cost one;
- showed same-block access is an obstruction independent of P4-S045's certificate-time delay;
- showed the B arm in \(ACB/ABC\) cannot reduce \(A_0\)'s already-zero same-block cost;
- defined open-hole-safe pre-certification and showed block-free does not imply it, because outside support may still hit the currently protected sentinel;
- defined the usable certification graph and proved an infinite computable usable path would yield a raw one-hole destroyer and hence \(X\notin OH\);
- did not obtain such a path for the committed source;
- did not obtain a direct computable-randomness contradiction from one-bit access;
- did not prove \(X\in OH\) or \(X\notin OH\).

## New boundary

The future target block itself is no longer the main local-information bottleneck:

\[
A_0:\kappa=0,\qquad A_1:\kappa\le1,\qquad A_2:\kappa\le1.
\]

The remaining source-side resource is

\[
\textbf{current-hole-uniform future A certification}.
\]

A useful future certificate must survive branching over the unknown current sentinel, avoid reading it through outside support, preserve the future sentinel, and retain a total one-hole fallback.

## Records

- phase4/P4-S046_MATHEMATICS.md
- phase4/P4-S046_VALIDATION.md
- phase4/P4-S046_CLOSE.md

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 unchanged. Phase 4 OPEN; Phase 5 CLOSED.

Owner/external blocker: **NONE**.

Recommended next session: **P4-S047**, on current-hole-uniform future A certification and outside-support collision.
