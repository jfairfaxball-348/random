# P4-S021 close

Date: 2026-10-06
Session: P4-S021
Incoming checkpoint: baf6f7be7dfe30f475465d43e677235abee66518
Scope: selected CAND-01; k=2 loss-scale / scale-tail effectivity boundary only
Status: **COMPLETED**

## Result

P4-S021 gives a positive local scale-tail effectivization theorem but separates it from P4-S020's stronger exact loss-level searchability.

For bad-capital histories \(B_K=\{v:W^*(v)<K\}\), fix a loss scale \(\delta_n=2^{-n}\). Suppose there is a computable local waiting bound for any reachable future realized loss at least \(\delta_n\), and a computable bound \(T(K,n)\) on the total contribution of all smaller realized losses while \(W^*<K\). Then coarse-scale accumulated-loss reachability is decidable: if \(q\) units of \(\delta_n\)-large loss are reachable, a first-crossing witness uses at most \(\lceil q2^n\rceil\) such events, each reached within the computable waiting bound. Under set-theoretic loss-properness, search for an unreachable coarse-scale q and add \(T(K,n)\). This computes a uniform bad-capital loss bound U(K), hence the P4-S018 coercivity modulus.

The scale-tail hypothesis does not restore absolute premium summability. The settled one-sided-trigger harmonic account has computable scale-tail bounds while its exact fair premium sum diverges on the all-trigger branch.

However scale-tail data do **not** force the P4-S020 witness modulus D(K,m) or decidability of exact Reach(K,m). An exact globally k=2, globally admissible construction uses a computable index ladder followed by a geometric machine tail. On a nonhalting machine, realized loss approaches the boundary \(2e+2\) from below through shrinking deterministic losses; on a halt, one finite correction block pays the remaining rational residual and attains the boundary exactly. With \(K_e=e+2\) and \(m_e=2e+2\),

\[
\operatorname{Reach}(K_e,m_e)\iff \Phi_e\downarrow.
\]

The same account has computable global deadlines for every fixed loss scale, an effectively vanishing bound on smaller-scale loss, and an explicit computable linear U(K). Thus the remaining obstruction is not effectivity of loss-properness itself: it is **anti-Zeno / boundary isolation**, distinguishing finite attainment of a loss level from arbitrarily close computable approach.

P4-S011 fails the P4-S021 scale-tail hypothesis strongly under global admissibility. Its ticket capital is bounded on the computably random sentinel-first completion while P4-S016 gives divergent realized skipped gain. The missed-epoch gains form a divergent subseries of \(1/(r+1)\), so for every n the contribution from gains below \(2^{-n}\) is unbounded inside one bad-capital tree. Bare admissibility remains unruled-out exactly as before.

P4-S005 through P4-S020 remain settled. P4-S011 and P4-S015 through P4-S020 are preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Phase 4 remains OPEN. Phase 5 remains CLOSED. Owner/external blocker: **NONE**.

Validation: phase4/P4-S021_VALIDATION.md.

## Next bounded task

P4-S022 should remain strictly at k=2 and test only an anti-Zeno / boundary-isolation hypothesis weaker than an explicit P4-S020 witness modulus: whether a computable certificate that the remaining subscale tail is either too small to reach a queried integer loss boundary or must cross it within finite searchable depth makes exact Reach(K,m) decidable. Otherwise isolate the next shrinking-scale obstruction and check P4-S011 explicitly.
