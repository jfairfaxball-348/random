# P4-S087 VALIDATION — dispersed survivor and E₀-breaking separation

Date 2026-10-10. Scope: Phase 4 mathematics only. Incoming GitHub main SHA `7435c93ec127f4fc2527a883917fb90784db4464`, read with `git ls-remote origin refs/heads/main`. Its commit parent is `453439b…`, the P4-S085 outgoing SHA, and `7435c93…` is the P4-S086 atomic close commit. Reconciled with the P4-S086 close record. No P4-S087 file existed on entry; P4-S087 is unused.

**Lemma 1 (monotone limit identification) — PASS.** Pure compactness: decreasing compact sets G⁻¹[y↾t]∩[σ]∩{z_k=b} have nonempty intersection iff all are nonempty. Uses only totality, continuity and fibres ≤ 2. No S085 width modulus and no computable phantom-death rate is assumed or needed.

**Lemma 2 (excess bound) — PASS.**
* Termwise, f ≤ c^σ + (f−1)^+.
* For the limit: the savings decomposition X_t ≤ 2 + B_∞, E[B_∞] ≤ d(∅) = 1 (monotone convergence), e_t ≤ N, and dominated convergence with integrable majorant N(2+B_∞).
* The capital factor is controlled only through the savings transform. An unrestricted martingale need not be uniformly integrable, and the proof does not claim otherwise.

**Lemma 3 (dispersibility) — PASS.**
* FD₂: continuity from above of the finite measures μ_e = (2+B^e_∞)λ ≪ λ on D_{a,b}, whose intersection lies in the λ-null set {Δ infinite}. Greedy spacing then works inside any infinite pool.
* DZ₂: random N-subsets of a long window, the collision bound C(N,2)(s/R)², and dominated convergence.
* The restriction of the DZ₂ case to positive-density pools is stated explicitly. This is why Theorem 8 is stated for FD₂.

**Theorem 4 — PASS.** The only change to S082 §4 is the dovetailed search over pairs (K₀,t) for a decidable rational inequality.
* Halting on true runs follows from Lemmas 2 and 3.
* The per-repetition increment is < 3/N_i, and N_i = 3·2^{i+3}ℓ_i reproduces the S082 bound 2^{−(i+3)} per stage.
* Wrong-guess runs may diverge; S082 already permits this.
* ℓ_i = 2i+2 fixings per stage, so the ML test bound is unchanged.
* Compactness (S082 Prop. 4.3) uses only Lemmas 2.1, 2.2 and 2.4 and the invariant.
* Quantifier audit: the result is ∃z ∀(G,d) ∈ 𝒱. It is genuinely simultaneous for the whole class, NOT the S086 ∀F∃x form, and NOT a claim about all of F₂.

**Corollary 5 — PASS.**
* id ∈ DZ₂.
* Validity is arithmetical: totality and martingale totality Π⁰₂; fairness Π⁰₁; the two-fibre bound via S085 Theorem 1.
* The difference-set predicates are arithmetical, because on the effectively closed set separating a fixed string pair, the two preimages are Π⁰₁(y)-singletons computable from y.
* Theorem 4 needs only arithmetical validity.

**Corollary 6 — PASS.**
* Transport by J: J⁻¹ is injective and fair, so it lies in DZ₂.
* MLR conservation (THM-0035, SRC-0011 STATEMENT_INSPECTED) gives z = J⁻¹(w) ∉ MLR.
* The (J⁻¹,d) strategies give z ∈ CR.

**Corollary 7(b) — PASS.** J_f is lower unitriangular over F₂, hence a fair computable homeomorphism. Over F₂, D′ is multiplication by (1+x), and J_f(u)_i = [x^i]((1+x)^{f(i)}U). This gives J_f D′^{−j}(e_p)_i = [x^{i−p}](1+x)^{f(i)−j}, which has finite support since f(i) ≤ √i. Block recodings contribute finite-support differences, and linearity finishes. The audit's Part 3 confirms the finite support numerically for j = 1, 2 on 40-bit truncations; the proof does not rely on it.

**Theorem 8 — PASS.**
* S083 §3 is reused verbatim except for the candidate search, which is restricted to the infinite decidable classes C_ε. FD₂ dispersibility holds in any infinite pool.
* Class separation, the ⅛ fooling bound, Lemma 3.6 and Proposition 3.7 depend only on facts preserved by the change. T* runs bounded simulations, so runs that search forever never qualify.
* F_{T*}∘D′ ∉ FD₂ by S084 Corollary 4 (a.e. tail-complement fibres).

**Proposition 9 and Lemma 10 — PASS.**
* Proposition 9: E₀-preservation by H⁻¹ transfers FD₂ membership from G to G∘H. CR preservation of H is THM-0038 (SRC-0015, STATEMENT_INSPECTED). The non-closure under D′ is Theorem 8.
* Lemma 10: a piecewise finite-flip partner map is a λ-preserving involution, so the fibre disintegration is symmetric.

**Route analyses — CORRECTLY LABELLED.**
* §6.1 (race symmetry) and §6.2 (overcount exploitation schema) are labelled analysis or heuristic, not theorems.
* The §6.2 identities Ψ̃ = A + E and A ≤ Ψ̃ ≤ 2A are stated in the t→∞ limit with symmetric weights.
* §6.3 is a standard-type argument (likelihood-ratio martingale plus Levin–Schnorr), with no novelty claimed.

**Finite audit — PASS.** `python3 phase4/P4-S087_DISPERSION_AUDIT.py` prints `ALL P4-S087 AUDITS PASS` (8,261 checks, < 1 s). Finite truncations only.

**Evidence and guard audit — PASS.**
* No source was fetched and no access level changed.
* SRC-0072 (ABSTRACT_INSPECTED) is mentioned only as calibration vocabulary.
* R_tot = MLR remains a programme deduction.
* Original Y/M/H/X and all S001–S086 results are frozen.
* R₂ versus MLR, R₂ versus OH^iso, U(H), X ∈ OH and fixed-S preservation are unresolved.
* PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged.
* Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED.
* No novelty, openness, priority, publication or outreach claim. No owner/external blocker.
