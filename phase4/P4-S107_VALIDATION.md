# P4-S107 — Adversarial validation (separate same-agent pass)

2026-10-12. Independent hostile reading within one agent; NOT a referee, formal verification or hosted CI. Challenged S107 A1–A4, B1 against original S003/S007 inverse-prefix cap, S106 A2–A4, S004/S005, S083.

| Proposed inference / attack | Verdict |
| --- | --- |
| Could L_n exceed two or exclude actual x prefix? | NO: S003 all-output cap and actual path inclusion. |
| Is L_n computable from finite source prefix? | YES: computable continuous G, computable clopen cylinder preimages. |
| Does singleton phantom persist at fixed earlier discrepancy? | NO: compact witnesses converge to forbidden second inverse as c(n) grows. |
| Does P_n(x) converging to J(x) make J total computable? | NO: lacks computable convergence modulus. |
| Is a Baire-one discontinuity set Schnorr null? | NOT established: meagre F-sigma is only topological. |
| Could S083's CR singleton destroyer have continuous J? | YES, all singleton points have J continuous; preservation does not follow. |
| Is A2 valid for mixed singleton/double maps? | NO: local injectivity need not imply J continuity at a double source approached by singleton points; exact-two everywhere is required. |
| Why does local injectivity force J continuous under exact-two? | Other partners cannot enter source chart; any converging subsequence approaches the unique other inverse. |
| In A4 why can inverse points not escape W0 union W1 nearby? | Compact image of closed complement avoids target, giving an output neighbourhood where all inverse points lie in union. |
| Can two inverses of nearby output both occupy one Wi? | NO: Wi restriction injective; exact-two total forces one in each. |
| Is J everywhere continuous known for ALL exact-two G? | NO; the global splitting conclusion has a conditional hypothesis only. |
| Is actual DP2 failure necessarily source-ramified? | YES by contrapositive of S106 local clopen source-preservation lemma. |
| Can small same-side collision outputs still be in D_r? | NO, two colliding source points exhaust all inverses and have same r-prefix. |
| Does pre/post composition obstruction hold for arbitrary exact-two H? | YES, disjoint cardinal sums, global onto; not just first-bit deletion. |
| Does B1 exclude a wholly new nonlinear fair exact-two quotient? | NO. |
| Is null-point graft while fixing a dense complement continuous? | NO, two continuous functions agreeing on a dense set coincide. |
| Was a fair exact-two ramified CR destroyer constructed? | NO, cell pricing/fibre bounds/source CR/output rational winner all remain absent. |
| Does a conditional Schnorr-cover theorem assert such covers exist? | NO, clearly conditional only. |
| Are finite checks proof for Cantor infinite fibres or randomness? | NO. |

Finite audit: Python3 standard library script phase4/P4-S107_PARTNER_AUDIT.py executed, PASS 6096 assertions over n=2,...,10 on marker-deletion prefixes, at-most-two compatible source n-prefixes, and flipping the genuine marker partner. Infinite marker assertion is separately justified in S107 mathematics; finite script cannot prove any CR statement.

Entry reconciled: main 87191694a6fa58c8f088abfc7f80e55f10dd9e14, sole parent f0b4e71b0d32b47aa44b620a9ff35d473fc12f3e, tree e9f03f8ee945928a5f654119498d5c688d7a9953. PR #3 merged with one S106 commit; no open PR or competing S107 record at entry. S107 branch newly created. Workflow files absent from entry tree, Actions runs 0 (hence no jobs), hosted check-runs/status contexts historically zero (not CI PASS), rulesets empty. Branch metadata unprotected; branch-protection endpoint inaccessible 403, workflows collection connector-disallowed. No gate or source access promotion, no publication action.
