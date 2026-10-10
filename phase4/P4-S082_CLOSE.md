# P4-S082 CLOSE — consistency potentials; OH-certification gate passed

Date: 2026-10-10. Incoming remote main `a6557f24867e48f5ac018f9865896993e74cc443` (the P4-S081 outgoing SHA) pinned; P4-S082 unique; incoming prompt identical to `authoritative/NEXT_SESSION_PROMPT.md`. **VALIDATED. The certification gate is PASSED: OH∖MLR ≠ ∅. The north star (R₂=OH) and U(H) are unresolved.**

**Calibration.** SRC-0069 (Kastermans–Lempp preprint; STATEMENT_INSPECTED, with the §2 proof read) and SRC-0070 (Bienvenu–Hölzl–Kräling–Merkle, CCA 2009; ABSTRACT_INSPECTED) are recorded, with THM-0077 and THM-0078. Their notions are non-adaptive with partial stakes, so they are incomparable with OH. Only their expected-martingale and compactness method is adapted. No novelty, priority or openness inference is drawn.

**Consistency potential (§2).** For any total computable fair map G, martingale d and partial assignment σ, Ψ(σ,m) = 2^{|σ|}E_λ[X_m·1(G⁻¹[G(z)↾m] meets [σ])]. It is non-increasing in m, it dominates the [σ]-conditional expected capital, and averaging over the value of a new coordinate k gives exactly Ψ(σ) + γ(σ,k). Here γ is the capital-weighted split weight of k.

**Cost bounds (§3).** For one-hole scans, the split weights of coordinates below the frontier sum to at most Ψ (h·Ψ for h-hole scans). The same holds for one-hole scans of computable finite-block recodings, with candidates in distinct blocks.

**Theorem 4.4 (certification gate PASSED).** OH∖MLR ≠ ∅.
* Guessed runs (Π⁰₂ validity) add weighted strategies and fix 2i+2 bits at stage i. Each fixed bit is a minimal-split-weight coordinate, set to the potential-minimizing value, and Φ < 2 is kept throughout.
* The 2^{i+1} runs form a Martin-Löf test.
* Compactness yields z in the null closed set S with every savings capital bounded.
* The witness is ≤_T ∅‴.
* Both S081 §7 obstruction halves are bypassed, not repaired: there is no random background, and blind bets are controlled by the potential.

**Theorem 5.1.** There is z∉MLR with K(z)∈OH for every computable finite-block recoding K, so H(z)∈OH and z∈OH^{lin3}. Potential-built witnesses cannot separate OH from its blockwise images.

**Theorem 6.1, Proposition 6.2, Examples E1–E3.**
* Theorem 6.1 is a general cheap-coordinate criterion.
* Example E1 shows that unbounded width breaks the accounting, so nothing follows about TKLR, KLR or QST-0001.
* For globally ≤2-to-1 maps, the counting potential makes fixing free and moves all cost to tracking (fresh-split weight).
* The exact gap for R₂: (a) transient fresh splits converge to the persistent part without a computable modulus; (b) potential-minimizing fixings can concentrate untracked double-fibre mass.

**Landscape (§7.2).** MLR ⊊ OH. Moreover R₂=MLR ⇒ R₂⊊OH, and R₂=OH ⇒ R₂∖MLR≠∅. So deciding R₂ versus MLR is now a sharp sub-question of the north star. S080 Corollary 7(b)'s route via OH=MLR is closed.

**Validation.** The exact finite audit passes. Structured adversarial self-review corrected the base case of the invariant (made non-strict) and simplified one proof step. No multi-agent review was run.

**Frozen.** P4-S001–S081; original Y/M/H/X; S037; S057 (not invoked); S070–S081. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claim. Owner/external blocker NONE.

Files: phase4/P4-S082_MATHEMATICS.md, phase4/P4-S082_VALIDATION.md, phase4/P4-S082_POTENTIAL_AUDIT.py, this close record; catalog/sources.json, theorems.json, authors.json, search-log.md.

Next session: **P4-S083**.

## Next-session prompt (copy-ready; identical to authoritative/NEXT_SESSION_PROMPT.md)

# P4-S083 — R₂ versus MLR: the consistency potential against all globally ≤2-to-1 maps, or R₂ = MLR

Continue the Fairfax-Ball Randomness Research Programme, ONLY Phase 4 Mathematics, in https://github.com/jfairfaxball-348/random. Pin independently verified live remote main to the exact P4-S082 outgoing SHA; reconcile discrepancies and confirm P4-S083 uniqueness. Review P4-S001–S082 mathematics, especially S007 (width-two skeleton c(n)), S008, S011/S012, S032/S033, S070, S078, S080, S081 (Theorem A, Corollaries A1–A6, Theorem B) and S082 (Lemmas 2.1–2.4, 3.1–3.2, Theorems 4.4, 5.1, 6.1, Proposition 6.2, Examples E1–E3, §7 trichotomy), together with S082 validation and close, CAND-01, the Gate-3 PASS, both Phase-4 pivots, and SRC-0069/SRC-0070 at their recorded access levels.

NORTH STAR: decide R2=OH, keeping R2=OH^iso separate. Retain MLR ⊊ OH = OH_h = R_k^scan, OH^blk∖MLR ≠ ∅, MLR ⊆ R2 ⊆ OH^iso ⊆ OH^blk ⊆ OH^lin3 ⊆ OH ⊊ CR, and KLR ⊆ TKLR ⊆ OH. Preserve the ORIGINAL CR Y, the clipped syntactically self-avoiding wtt autoreduction M, the repeated H (A=[101;110;111]) and X=H^{-1}(Y), all unaltered.

S082 SETTLED:
(1) Consistency potential. Let G be a total computable fair-coin-preserving map, d a rational martingale with capital X_m, and σ a finite partial assignment. Put Ψ(σ,m) = 2^{|σ|}·E_λ[X_m·1(G^{-1}[G(z)↾m] meets [σ])]. Then Ψ is non-increasing in m, it dominates the [σ]-conditional expected capital, and it satisfies the exact refinement identity: the average over b of Ψ(σ∪{k↦b}) equals Ψ(σ) + γ(σ,k), where γ is the capital-weighted split weight of k.
(2) Cost bounds. For one-hole scans, the split weights of coordinates below the frontier sum to at most Ψ. The same holds for one-hole scans of computable finite-block recodings, with candidates taken in distinct blocks.
(3) Theorem 4.4: OH∖MLR ≠ ∅, so the certification gate is PASSED. The witness is ≤_T ∅‴. The proof uses guessed computable runs, a Martin-Löf test built from the 2^{i+1} runs, and compactness.
(4) Theorem 5.1: there is z∉MLR with K(z)∈OH for every computable finite-block recoding K. In particular H(z)∈OH and z∈OH^lin3, so potential-built witnesses cannot separate OH from its blockwise images.
(5) §7.2 trichotomy: R2=MLR implies R2⊊OH, which decides the north star negatively; R2=OH implies R2∖MLR≠∅.
(6) §6.3 exact gap for globally ≤2-to-1 maps. The counting potential makes fixing free and moves all cost to tracking, where the cost is the fresh-split weight. Two obstacles remain. (a) The transient fresh-split weight converges to the persistent double-fibre part without a computable modulus. (b) Potential-minimizing fixings can concentrate untracked double-fibre mass.

PRIMARY TARGET: decide R2 versus MLR.
(a) Close the §6.3 gap. Construct a computably random non-MLR z with F(z)∈CR for every total computable fair-coin-preserving map F with all fibres of size ≤2, so that z∈R2∖MLR. One route: an augmented computable potential that bounds total tracking charges, using the P4-S007 width-two skeleton, neutralization of ambiguity cohorts, and guessed right-c.e. bounds for persistent fresh-split weights. Or
(b) prove R2 = MLR: every non-MLR CR source is destroyed by some such map. With Theorem 4.4 this gives R2⊊OH and decides the north star. Or
(c) prove the §6.3 gap unavoidable for a precisely defined natural class of potential constructions.
Secondary, only where it serves the primary target: OH^iso∖MLR via order-dependent neutralization (Example E3), or a separation z∈OH with a winning non-scan k=2 map or a winning non-block homeomorphism image.

Do NOT attempt a record-only proof of z0 ∈ OH (impossible by S080). Do NOT resume finite price/escrow/hazard/renewal work, residue tables, unit-column enumeration, or multi-hole variants of one-hole arguments. Every scan must be everywhere total, computable, no-repeat, fair-coin preserving and at most one-hole on EVERY transcript. Every k=2 map must be total computable, fair-coin preserving, with all fibres of size ≤2. Distinguish MLR, KLR, TKLR, OH, OH^blk, OH^lin3, OH^iso, R2 and R_fin carefully. No openness or priority inference may be drawn from missing searches; record access levels for any literature used.

Freeze all P4-S001–S082 results, especially S037, S057 (exact four paired clipped traces, prospective deadlines, genuine fillers, t/u zero-stake timeout release, mandatory non-s sweep without old-sentinel reset, seven 8/7 vs one ZERO) and S070–S082. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE, DEF-0020 unchanged, Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach assertions.

CLOSEOUT (mandatory, per docs/SESSION_PROTOCOL.md): validate; synchronize authoritative records; commit atomically; push the session branch; merge it into main (fast-forward when possible, never rewriting main history) and push main; independently verify with `git ls-remote origin refs/heads/main` that remote main equals the outgoing SHA. The P4-S083 close record and the final report must both contain the full copy-ready P4-S084 prompt, identical to authoritative/NEXT_SESSION_PROMPT.md, unless an owner/external blocker exists, in which case state the blocker and give no prompt.
