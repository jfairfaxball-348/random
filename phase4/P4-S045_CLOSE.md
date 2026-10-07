# P4-S045 Close

Date: 2026-10-07
Session: P4-S045
Status: **COMPLETED / VALIDATED**
Incoming checkpoint: 55b203879c3c4ab6cfa88cc32f6dee6dc57d9259

Scope: source-specific certificate-time selector thickness after P4-S044 source-value closure, under the sustained \(R_2=OH\) one-hole normalization target.

## Results

- formalized a faithful moving-reservation selector as an everywhere-total computable no-repeat one-hole scan:
  - choose the raw role before local status is known;
  - keep the current sentinel until its own A/B certificate;
  - cycle through computable transient future block reservations;
  - freeze the reservation active at certificate time;
  - consume every transient reservation on a no-event continuation;
- separated the ambient A set, the reservation stream, and the event-time-selected target subsequence;
- defined exact event-time selector thickness: infinitely many completed epochs with infinitely many selected A blocks and no selected C trap;
- proved selector thickness produces an actual raw one-hole destroyer and hence \(X\notin OH\);
- proved a C-free A-cofinite computable reservation lane is sufficient for selector thickness;
- proved finite possible-index coverage plus certificate-time domination is another sufficient form;
- showed bounded gaps, positive density, bare finite-union lane concentration and recurrence along computable subsequences do not by themselves imply selector thickness;
- proved that after the P4-S044 value horizon is closed, finite certificate time is future-blind: it depends only on already exposed finite source data and internal computation, not on later reservation-block bits;
- found no direct computable-randomness betting contradiction from systematic delayed A certificates, because no coupling from delay to an unread future bit is forced;
- recorded the presentation guard that finite dummy delays preserve target correctness, self-avoidance, use and semantic A/B/C status, so those properties alone cannot yield a presentation-independent runtime modulus;
- strengthened the P4-S044 structural diagonalization from every prescribed finite selector family to **every member of any prescribed uniformly computable countable family of faithful moving-reservation selector schemes**;
- retained recurrent nontriple \(C_0\), visible A witnesses and the genuine unbounded-overlap horizon
  \[
  h(b)=2b+2
  \]
  in that structural model;
- proved the strengthening cannot become a universal computable-target countermodel: after the model is built, Case-A certificates on a computable target are c.e., so a new computable selector can enumerate certified A targets and schedule them in finite known certificate windows;
- identified the actual-source distinction as **live-source certification cost**: for the noncomputable \(X\), prospective A evidence requires querying finite source values and may consume or protect the very coordinates needed for a future one-hole target;
- sharpened recurrent \(C_0\): the two-selector obstruction already follows from role alternation \(CAC/CCA\), arbitrarily delayed A, and the global one-hole fallback; support consumption is not needed;
- proved the visible B arm in \(ACB/ABC\) gives no generic timing bound on the \(A_0\) certificate, because the two finite certificate clocks can be independently delayed without changing use, queries or status;
- did not prove computable-randomness compatibility or incompatibility of selector-evasive delayed certificates for the exact committed autoreduction;
- did not prove \(X\in OH\) or an unconditional \(X\notin OH\);
- did not prove OH non-invariance or \(R_2\subsetneq OH\).

## New boundary

The structural computable-target selector problem and the committed-source problem are now separated.

On a computable target, visible A certificates can be enumerated off-line after construction. Hence no computable-target model with infinitely many visible A blocks can defeat every computable selector.

For the committed noncomputable source, the A certificate is only available after the live scan acquires its finite source-value support. That acquisition may destroy future-target freshness or create a second protected coordinate while the current sentinel is still open.

Thus the remaining resource is:

\[
\textbf{future A-certificate access compatible with one-hole freshness}.
\]

Certificate time still matters, but P4-S045 shows that timing alone is not the whole obstruction.

## Records

- phase4/P4-S045_MATHEMATICS.md
- phase4/P4-S045_VALIDATION.md
- phase4/P4-S045_CLOSE.md

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 unchanged. Phase 4 OPEN; Phase 5 CLOSED.

Owner/external blocker: **NONE**.

Recommended next session: **P4-S046**, on future A-certificate access cost: determine whether the actual committed autoreduction supplies infinitely many prospective A certificates whose evidence can be acquired without consuming/protecting the future raw target, or prove a sharper one-hole certification-access obstruction.
