# P4-S099 — adversarial mathematical and repository validation

Date 2026-10-11. Incoming live main 7f4246c274fc24fd5ca0ec50cd6859609fa24e86, sole parent 633a096fbaeba72a77fbcaf475639a63c820a6dd. Open/recent PRs none, S099 branches/files none; Actions workflow directory missing, workflow runs 0, check-runs 0, statuses 0, rulesets [], branch protection 403. No hosted CI PASS or independent referee.

1. Theorem A is only the standard CR⇒Schnorr fact under *uniformly computable* λ(U_n), not a claim that every ML test excludes CR. Its hypothesis fails for genuinely noncomputable level-measure tests.
2. Theorem B uniformly approximates Π⁰₁ P_e by descending clopens [0]→∅ if e halts. λ(P_e)>0 iff e diverges; nonhalting is not c.e. Lower-mass certification requires extra finite witnesses not furnished by S095.
3. Toy A: nested Q1⊆Q0, λU=q. Toy B: disjoint Q1 and Q0, λU=q or 3q/2; a q/8-accurate measure approximation detects the difference and solves halting. U_n membership on 0-path across all n forces 0^ω; the 1-path requires every indexed program to halt, false. Both have N=2 and 2Nq=2^{-n-1}≤2^{-n}. They show conditions necessary but not sufficient, do not construct CR z.
4. D: every τ of length m imposes m linear independent adjacent XOR constraints on m+1 input bits, leaving exactly two choices, cylinder measure 2^{-m}. K(x)=(x0,D(x)) is computable measure-preserving homeomorphism, inverse x_{i+1}=x_i⊕y_i. π∘K harmless to CR. No unwarranted F₂ classification.
5. EQ error-stream inference uses S084 whole computable randomness, not mere frequency. The S096 f covers all VALID observers non-effectively and may choose MLR. Ψ computed over saturated G⁻¹G(P), with Ψ(P,0)=1/λP; factor 2Nq audited.
6. No finite code audit, Lean, hosted workflow run, external review or original infinite proof checking was run in this session. These results are written logical reductions checked adversarially here, not machine-verified theorems.

DISPOSITION: route-level Theorems A/B and explicit finite-branch countermodels PROVED as written; conditional finishing implication NOT executed; EQ and SEP UNRESOLVED, GOL unresolved. Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. Next S100 full audit is future only.
