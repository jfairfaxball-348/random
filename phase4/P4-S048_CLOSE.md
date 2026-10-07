# P4-S048 Close

Date: 2026-10-07
Session: P4-S048
Status: **COMPLETED / VALIDATED**
Incoming checkpoint: caba6f96b665e067661750e40e08164fb959968c

Scope: persistent partial-fixed-point old-hole sensitivity of future A-certificate computations.

## Results

- fixed an unresolved P4-S047 global-refutation epoch and separated the actual total fixed branch \(Y\) from the false raw-radius-one partial fixed neighbour \(Z\);
- classified every future target equation into trace-safe, trace-sensitive but value-fixed, or divergence-sensitive;
- proved every divergence-sensitive future target equation has finite target-trace contact with the old changed support;
- sharpened the P4-S042 support lasso under partial fixedness: after old-support contact, only old-support divergence or a correct-halting dependency cycle can remain; the finite-refutation arm disappears;
- isolated the exact canonical false-neighbour target-equation lists
  \[
  F_0=\{q_0,q_1,q_2\},\qquad
  F_1=\{q_0\},\qquad
  F_2=\{q_1\};
  \]
- proved that, once the false-branch raw-adjacent rejection is positively available, halting of the corresponding finite list completes the false-branch P4-S046 low-cost rejection package;
- separated listed target-equation divergence from false-branch raw-adjacent rejection, because the latter lives on a doubly perturbed oracle rather than on \(Z\);
- defined the source-specific canonical future-A fixedness sensitivity set and kept syntactic fan-out, semantic sensitivity, divergence sensitivity, raw-adjacent sensitivity and canonical certificate-essential sensitivity distinct;
- built recurrent finite-use syntactically self-avoiding structural Family F in which:
  - the false neighbour is a global partial fixed point;
  - one fixed old row is the first-contact gate for infinitely many future listed equations;
  - one required role-list equation diverges on every designated future block;
  - the old changed support closes into a correct P4-S041 cycle;
  - the false-branch raw-adjacent rejection remains finite and positive;
- built recurrent structural Family R in which:
  - the false neighbour is a **total global fixed point**;
  - every canonical automatic unit-flip rejection survives;
  - every false-branch raw-adjacent future candidate nevertheless becomes divergence-only;
- therefore proved that global partial fixedness, and even total fixedness of the false neighbour, does not force a CHU escape;
- defined an exact canonical partial-neighbour escape operator and proved that one total computable such operator along all reached nodes yields an infinite computable CHU path and hence
  \[
  X\notin OH;
  \]
- sharpened the hypothetical-\(X\in OH\) obstruction only algorithm-relatively: every such total canonical escape constructor must fail on a reached node; if raw-adjacent rejection and fallback have already positively resolved, the remaining permanent capture is divergence of one equation in the relevant finite role list;
- explicitly did **not** infer semantic infinitude of all bad future blocks or effective escape from semantic finiteness alone;
- obtained no CHU path for the committed source;
- did not prove \(X\in OH\) or \(X\notin OH\).

## New boundary

The false old-hole partial neighbour supplies two independent finite kernels for a canonical future A edge:

\[
\boxed{\text{finite target-equation fixedness list}}
\]

and

\[
\boxed{\text{false-branch raw-adjacent rejection}}.
\]

The target-equation lists have exact sizes

\[
3,\ 1,\ 1
\]

for \(A_0,A_1,A_2\).

Partial fixedness removes finite wrong-output sensitivity from the first kernel, but does not make its divergence positively decidable. It also gives no control over the second, doubly perturbed kernel.

The next irreducible object is therefore the **two-raw-bit square** consisting of \(Y\), the false old partial neighbour \(Z\), the future raw-adjacent A candidate, and the same future perturbation applied to \(Z\).

## Records

- phase4/P4-S048_MATHEMATICS.md
- phase4/P4-S048_VALIDATION.md
- phase4/P4-S048_CLOSE.md

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 unchanged. Phase 4 OPEN; Phase 5 CLOSED.

Owner/external blocker: **NONE**.

Recommended next session: **P4-S049**, attack the two-raw-bit square and determine whether the actual committed source imposes a positive finite constraint on false-branch raw-adjacent rejection beyond P4-S048's independent structural countermodels.
