# P4-S049 Close

Date: 2026-10-07
Session: P4-S049
Status: **COMPLETED / VALIDATED**
Incoming checkpoint: ab8136c67eb772821b1fcc40a17e3b877ad32119

Scope: two-raw-bit square / partial-fixed-point star at an unresolved P4-S047 old-hole epoch.

## Results

- formalized finite square refutation as positive elimination of one raw pair hypothesis;
- proved the generic row/column elimination laws:
  - two refuted future values in one old row predict the old bit;
  - two refuted old values in one future column predict the future bit;
- proved **actual-column shielding** at an unresolved old-hole epoch:
  - the actual-old / actual-future corner is \(Y\), a total fixed point;
  - the false-old / actual-future corner is \(Z\), a global partial fixed point;
  - therefore neither corner in the actual future-bit column can have a finite wrong/nonbinary equation;
- deduced the central P4-S049 theorem:
  \[
  \boxed{\text{one finite square refutation already predicts the future raw bit}}
  \]
  at a genuinely trapped old epoch, independently of the old row;
- proved that an actual future \(A_j\) rejection is already such a one-refutation certificate, so a fourth-corner \(Z_j\) rejection is not needed for one-shot future prediction;
- retained the fourth-corner trichotomy—finite-refuted, locally self-consistent, divergence-only—but separated it from the one-refutation prediction theorem;
- proved that a square with no global finite refutation has all four corners as global partial fixed points;
- proved the exact paired-partial-fixed first-contact lasso:
  - a changed coordinate with two halting corner computations points to another changed coordinate;
  - the walk either stops at a divergence or enters the P4-S041 finite-difference cycle;
  - the \(011\) and \(101\) supports force two-cycles under full two-corner halting;
  - the \(111\) support gives a two-cycle-with-tail or oriented three-cycle;
- used the P4-S041 pairwise status law to show that a genuinely local Case-B fourth corner forces finite role-switch refutations in the false old row, which become alternate future-bit predictions by actual-column shielding;
- isolated the effectivity gap: the premise that the old epoch is truly unresolved is semantic and cannot be positively recognized at finite time;
- defined globally legal **finite-tenure square reservation policies**:
  - the old sentinel may remain the sole permanent hole;
  - each prospective future sentinel is reserved only transiently;
  - timeouts consume it at zero stake;
  - caught square refutations give correct future-bit wagers;
- proved that infinitely many caught square refutations at one trapped old sentinel yield a total computable one-hole destroyer and hence
  \[
  X\notin OH;
  \]
- sharpened the necessary obstruction under hypothetical
  \[
  X\in OH:
  \]
  at the first trapped P4-S047 epoch, every total computable finite-tenure square reservation policy catches only finitely many finite square refutations;
- kept that obstruction algorithm-relative and did not infer semantic infinitude of no-refutation squares or any computable bound;
- built a sharper recurrent structural full-star model on \(0^\omega\) in which:
  - the two unperturbed old rows are total fixed points;
  - for all three future raw directions, both actual-row and false-row raw-adjacent neighbours are global partial fixed points;
  - no future neighbour has a finite wrong/nonbinary equation;
- explicitly recorded that this structural model is non-random and deliberately lacks the actual-\(A_j\) premise, so it does not contradict the source-specific one-refutation theorem;
- obtained no infinite effective square escape on the committed source;
- did not prove \(X\in OH\) or \(X\notin OH\).

## New boundary

P4-S048 treated the fourth corner \(Z_j\) as the missing second kernel for a two-row CHU certificate.

P4-S049 shows that at a **semantically trapped old epoch** the finite square logic is stronger:

\[
\boxed{
\text{actual future column}=\{Y,Z\}
\text{ is refutation-free}
}
\]

and therefore

\[
\boxed{
\text{any finite square refutation}
\Longrightarrow
\text{wrong future column}
\Longrightarrow
\text{future-bit prediction}.
}
\]

Thus the fourth corner is not the missing logical condition for one-shot prediction.

The remaining problem is operational:

\[
\boxed{
\text{activate/capture the one-refutation rule effectively without a trap oracle and without two permanent holes.}
}
\]

Finite source-value use does not give a finite certificate-time modulus, so transient reservations may expire before existing refutations appear.

## Records

- phase4/P4-S049_MATHEMATICS.md
- phase4/P4-S049_VALIDATION.md
- phase4/P4-S049_CLOSE.md

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 unchanged. Phase 4 OPEN; Phase 5 CLOSED.

Owner/external blocker: **NONE**.

Recommended next session: **P4-S050**, attack effective activation of the one-refutation square theorem without semantic knowledge of the trapped epoch, using only positive finite square events and globally legal one-hole fallback.
