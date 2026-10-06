# P4-S024 close

Date: 2026-10-06
Session: P4-S024
Incoming checkpoint: 4f0eef36aa6c2223528c1e48a8e300f0e9d29ec0
Scope: selected CAND-01; k=2 pointwise/branchwise tail sharpness only
Status: **COMPLETED**

## Result

P4-S024 resolves the sharpness question after P4-S023 in two layers.

A single oracle-uniform branchwise convergence functional is not a genuine weakening of P4-S023. Because the globally admissible bad-capital tree \(B_K\) is computable, finitely branching and pruned, the cylinders on which the functional halts form a c.e. open cover of \([B_K]\). Effective compactness finds a finite subcover, and the maximum of the finitely many returned branch moduli gives a computable global tail modulus. Semantic anti-Zeno then yields the same searchable strict-frontier conclusion as P4-S023.

Genuinely nonuniform pointwise/branchwise effective convergence is insufficient. The exact incompatible-branch comb in phase4/P4-S024_MATHEMATICS.md stays globally k=2 and globally admissible, has a computable fixed-scale exhaustion depth \(G(K,n)\), and has an explicit computable bad-capital loss bound \(U(K)\). Every individual bad-capital branch has only finitely many positive losses, hence is eventually loss-constant, semantically non-Zeno at every integer boundary, and has some ordinary computable convergence modulus.

Nevertheless for \(K_e=e+2\) and \(m_e=2e+2\),

\[
\operatorname{Reach}(K_e,m_e)\iff\Phi_e\downarrow.
\]

On divergence, later incompatible teeth have final losses \(m_e-2^{-(t+1)}\) tending to \(m_e\), while their Cantor-limit all-continue spine stays at \(m_e-2\). The branch-limit loss is therefore discontinuous. Near-boundary mass can move to later branches and disappear at the compact limit, so semantic anti-Zeno alone gives no uniform strict gap.

Thus P4-S023's compactness step needs more than branchwise convergence; it needs enough uniform/effective topological control to prevent this discontinuity. The natural next boundary is effective upper-semicontinuity or an equivalent local tail-cap basis for the branch-limit loss.

P4-S011 remains outside even the weak pointwise-tail regime under global admissibility: its computably random sentinel-first completion lies in one bad-capital tree with cumulative realized skipped gain diverging to infinity. Bare admissibility remains unruled-out.

P4-S005 through P4-S023 remain settled. P4-S011 and P4-S015 through P4-S023 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Phase 4 remains OPEN. Phase 5 remains CLOSED. Owner/external blocker: **NONE**.

Validation: phase4/P4-S024_VALIDATION.md.

## Next bounded task

P4-S025 should remain strictly at k=2 and test only whether an effectively upper-semicontinuous branch-limit loss, or an equivalent computable local tail-cap basis strictly weaker as primitive data than a global uniform tail modulus, combines with semantic anti-Zeno to force searchable strict frontier separation. Otherwise isolate the sharpest effective-topological obstruction. Check P4-S011 explicitly.
