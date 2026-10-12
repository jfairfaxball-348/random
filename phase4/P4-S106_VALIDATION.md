# P4-S106 — Adversarial proof and counterexample validation

2026-10-12. Separate same-agent internal audit; not independent referee or formal verification.

| Challenge | Result / repair |
| --- | --- |
| Does two compatible r-prefixes at every m really give two inverse points? | YES: nested compact preimages in each fixed r-cylinder; finite descending candidate list stabilizes. Surjectivity follows from fairness. |
| Can a phantom survive A1 on a double fibre beyond c(n)? | NO once n≥r: two actual n-prefixes occupy BOTH allowed places. For n<r there may be a phantom, so charts compute at max(n,r) and truncate, not at arbitrary n. |
| Is lex order coherent as n increases? | YES after the true r split; order of two distinct r-prefixes persists under extensions. |
| Is D_r computable/clopen? | NO. Uniform Π1 only; every finite approximation is clopen. The proof does NOT decide y∈D_r or enumerate Int(D_r). |
| Is the local source slice B_i clopen? | YES only with a fixed finite U=[tau] contained entirely in D_r. A rank is then decided by G(x)|c(r) and x|r. This is the essential LOCAL hypothesis, not a global selector. |
| Does CR on a clopen source B imply conditional CR? | YES: B is clopen of dyadic positive measure, and the conditional measure ratio is a fixed dyadic multiplier after a contained prefix. No arbitrary Π1 conditioning is used. |
| Does mu_B≤lambda/lambda(B) establish CR against all output rational martingales? | YES with existing DEF-0036 computable-measure ratio characterization and the S003/SRC-0015 measure-isomorphism theorem, not by composing a martingale naively. |
| Is Baire's category theorem enough for CP2? | NO: dense open need not have measure one, effectively null complement, or avoid CR. CP2 remains unresolved. |
| Is boundary(D_r) closed nowhere dense even if D_r has positive measure? | YES for a closed subset of Cantor space, boundary is closed with empty interior. It may have positive measure. |
| Does meagreness of union boundaries exclude CR outputs? | NO. CR is a measure notion, not genericity. |
| Does S004 force positive weights on actual two branches? | NO: S004 provides double-fibre zero limiting conditional weight. Never use A1 Turing charts as probability weights. |
| Does S005 stop this proof? | NO: A3 conditions on a clopen source slice with computable dyadic mass, not on a Π1 inverse-stratum or computability of a stopping event's measure. |
| Can adding π before or after G* preserve F2 globally? | NO in general: four regular inverse points appear; complete all-output bound fails. |
| Can a changed continuous map equal G* on dense complement but change the singleton witness? | NO by continuity. A nonlocal construction is not excluded. |
| Does C1 secretly assume closure F2 under composition? | NO: output is in R4, not R2, for two F2 operations. Reverse implication is explicitly absent. |
| Historical comparison | S003 clopen TWO-SHEET theorem and S007 coherent skeleton are retained. The new point is the Π1 double-output strata, their local chart source decomposition, and exact topological residual confinement, not a rediscovery presented as conservation for ALL double points. |

### Executable finite check

Script phase4/P4-S106_CHART_AUDIT.py (Python 3 standard library only) was run locally: 16,406 assertions PASS for marker-deletion finite prefix tables for m=1,...,9, checking 2:1 preimage count, the expected true split at every r≤m, lex separation, and the 4:1 count on composition with first-bit deletion. This is a limited finite sanity test. At y=0^m one may see an apparent split at r=m+1 even though the infinite output 0^omega has a singleton fibre: the audit deliberately stops at r≤m, exposing exactly why a finite-prefix model cannot decide eventual double status. No computation proves A1–A4 for all Cantor inputs.

### Entry/reconciliation

Live main and original owner-amendment commit/parent/tree verified by GitHub refs and commits; PR #1 and #2 merged; PR list has no open PR at entry and no numbered S106 record; only the old docs/P4-S106-owner-research-pivot branch existed. Incoming authoritative prompt archived byte-identically. The committed tree has no .github/workflows files. GitHub Actions runs=0, check-runs=0, status contexts=0 (combined pending); no jobs from runs; rulesets empty; branch-protection GET 403 (unavailable); workflows collection rejected by connector allowlist. **Hosted CI ABSENT_NOT_PASS**, not green. No external proof certification, new primary-source access, prior-art/novelty claim or Gate4 review.
