# P4-S025 close

Date: 2026-10-06
Session: P4-S025
Incoming checkpoint: 2b6c46b63029c454cc5536cfc11d51786d0590a1
Scope: selected CAND-01; k=2 effective upper-semicontinuity / local tail-cap boundary only
Status: **COMPLETED**

## Result

P4-S025 resolves the effective upper-semicontinuity question in two layers.

A natural complete effective upper-cap basis for the branch-limit loss is sufficient with semantic anti-Zeno, but it is not genuinely weaker than P4-S023's uniform-tail hypothesis. Because the globally admissible bad-capital tree is computable, finitely branching and pruned, one can enumerate local cylinders on which an upper cap lies within \(2^{-n}\) of the current finite-prefix loss. Pointwise convergence guarantees that those tight cylinders cover every branch. Effective compactness finds a finite subcover, and the maximum prefix length gives a computable global uniform tail modulus.

Conversely, a computable global tail modulus immediately enumerates a complete effective upper-cap basis by assigning the cap \(E(\sigma)+2^{-n}\) after the corresponding uniform frontier. Thus full effective upper-semicontinuity and global effective tail convergence are equivalent for this monotone prefix-loss process, up to harmless rational margins.

Semantic anti-Zeno then gives searchable strict frontier separation exactly as in P4-S023. If false Reach(K,m) had no strict frontier, near-m frontier nodes would compactify to a bad-capital branch with limit loss m but no finite attainment. Hence exact Reach is decidable and P4-S020's witness modulus is recoverable.

The sharp obstruction is effectivity, not ordinary semicontinuity. P4-S025 gives an exact delayed-activation globally k=2, globally admissible comb with computable fixed-scale exhaustion and effective loss-properness in which every bad-capital branch is eventually loss-constant and semantically anti-Zeno, and the branch-limit loss is continuous. Nevertheless

\[
\operatorname{Reach}(e+2,2e+2)\iff\Phi_e\downarrow.
\]

A selected-e branch first accumulates loss \(2e+1\). At comb stage t, a nonhalting tooth adds only \(2^{-(t+1)}\), so tooth limits converge continuously to the all-continue spine at \(2e+1\). If a halt is detected, the still-surviving comb component receives a finite deterministic correction of total 1, split into tiny \(2^{-(t+3)}\)-sized tickets, and reaches \(2e+2\). Late activation therefore hides halting in the **effective modulus of continuity / upper caps**, not in discontinuity.

A boundary-specific cap mechanism can be weaker as syntax, but if it uniformly supplies sound covers for all false integer Reach instances then it is exactly the missing positive semidecision of Bar(K,m), hence has the settled P4-S020/P4-S022 final computability strength.

P4-S011 remains outside even the semantic finite-limit regime under global admissibility: its computably random sentinel-first completion lies in one bad-capital tree with cumulative realized skipped gain diverging to infinity. Bare admissibility remains unruled-out.

P4-S005 through P4-S024 remain settled. P4-S011 and P4-S015 through P4-S024 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Phase 4 remains OPEN. Phase 5 remains CLOSED. Owner/external blocker: **NONE**.

Validation: phase4/P4-S025_VALIDATION.md.

## Next bounded task

P4-S026 should remain strictly at k=2 and test only the narrow intermediate effectivity gap: whether a one-sided effective boundary-modulus weaker than a complete upper-semicontinuity basis can arise from a natural structural hypothesis and force searchable Bar(K,m) without already restating P4-S020 searchability. Otherwise prove that every boundary-complete effective cap mechanism collapses to decidable Reach. Recheck P4-S011.
