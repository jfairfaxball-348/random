# P4-S088 VALIDATION — asymmetric loci, translation pairs, countable-coset survivor

Date 2026-10-10. Scope: Phase 4 mathematics only. Incoming GitHub main SHA `c820588d2936d1a6fe28cee84fca86699e65610a`, read with `git ls-remote origin refs/heads/main`. Its commit parent is `7435c93…`, the P4-S086 outgoing SHA, and `c820588…` is the P4-S087 atomic close commit. Reconciled with the P4-S087 close record. No P4-S088 file existed on entry; P4-S088 is unused.

**Theorem A (G_asym) — PASS.**
* *Measure.* A is a closed product set with λ(A) = ∏_{k≥2}(1−2^{−k}) > 0.
* *Side 0.* This is the identity on 00A and an exact cylinder shift [00v] → [v00] on the complement.
* *Side 1 packing.* Units have length a_{j+1}+2, and slots, which are sibling pairs of units, have length a_{j+1}+1. B_w holds N slots and S_w holds N/2.
  * For N ≡ 1 (mod 3), t = (2N−2)/3 is even and s = (N−1)/3 is odd. The leftovers are exactly one slot of B_w and one unit of S_w.
  * For N ≡ 2 (mod 3), t is odd and s is even. The leftovers are one unit of B_w and one slot of S_w.
  * The parity of t and s follows from N = 2^{ℓ_j} being even, and is forced by the arithmetic.
* *Collapse.* Collapsing children lie in one parent cylinder, so diameters → 0 along every y ∈ A. That gives single-valued h₁ and totality.
* *Fibres.* Side 0 never outputs v1 or v01, side 1 never outputs v00, and inputs mapping into A never meet a straddler. So the double locus is exactly A.
* *Fairness.* G⁻¹[w] = [00w] ⊔ B_w ⊔ S_w has measure 2^{−a_j} at A-prefixes, and the straddler cylinders have the exact measures of [v1] and [v01].
* *Weights.* ¼ and ¾ are exact on every Borel V ⊆ A.

**Corollaries A1–A3 — PASS.**
* A1 is the contrapositive of P4-S087 Lemma 10.
* A2 is P4-S003 Theorem 3, applied to the computable clopen split [00] / complement on which G_asym is injective.
* A3: the dilution is a product of the identity and G_asym on complementary decidable coordinate sets. It is fair, its fibres are those of G_asym, and its differences are supported in a density-zero set.

**Lemma B0 and Theorem B — PASS.**
* *Lemma B0.* K_c is an involution because (c⊕e₀)₀ = 0. The fibres of G_c are {x, x⊕c}, and G_c(x) is a computable translate of a shift of x.
* *Theorem B(i), entropy step.* The low/high split uses that x⊕c is uniform on [k,m(n)) and independent of x given L, because r is uniform. Conditional independence then gives the affine-min bound. The two Jensen steps use the convexity of h⁻¹, which is the inverse of a concave increasing function. The fairness of J gives H(J(x)↾n | L) ≥ n − k, and m(n) ≥ n.
* *Theorem B(i), construction.* The search is effective because E_x D_n(x,ρr) is an exact rational computable from J. Markov's inequality gives λ{D ≥ ⅛} ≥ 1/7, and the limsup set is ⊕c-invariant. Hence the output set where differences have positive upper density has positive measure.
* *Theorem B(ii).* The reduced-echelon transvections T_j are causal linear involutions. T_j fixes b^l and e_{p_l} for l ≠ j because the echelon form is reduced. The finite linear algebra is decidable on long enough prefixes.
* *Scope.* The statement is per J (∀J ∃c). No single c defeats all J, and none is claimed. Single-map DZ₂-straightening is left open.

**Lemma C1 — PASS.** For independent functionals, λ(P_b) = λ(P)/2 exactly, because (⟨c_j,x⟩, ⟨c,x⟩) is uniform on F₂^{n+1}. The set identity c^{P₀} + c^{P₁} = c^P + s^{P,c} is pure logic. Monotonicity and domination are verbatim S082.

**Lemma C2 — PASS.** Pure compactness with clopen constraints. The excess bound uses only the savings decomposition and dominated convergence with majorant N(2+B_∞). No width modulus is used.

**Lemma C3 (coset dispersal) — PASS.**
* Continuity from below of the finite measures μ_e gives a finite dominant set Q.
* Any m+1 vectors in F₂^m are dependent, so every group of m+1 coordinates carries a nonzero functional annihilating Q.
* For Δ = v⊕s, the functional sees only s. The collision bound C(N,2)(h/H)² goes to 0 by density zero of s, and dominated convergence applies.
* Supports lie in [a,∞), so independence from the current constraints is automatic.

**Theorem C — PASS.** The only change from P4-S087 Theorem 4 is the candidate space, which is now N-tuples of disjoint-support parities above all current supports instead of coordinates.
* *Halting.* Halting on true runs follows from Lemmas C2 and C3, with ε converted through (f−1)^+ ≤ N_i·1(f≥2) and the weights.
* *Invariant and test.* The invariant Γ < 3/N_i per repetition, the ℓ_i constraints per stage, λ(P^ε_i) = 2^{−(i+1)(i+2)}, the ML test, nestedness, nonemptiness of S and compactness all transfer, with clopen P*_i in place of cylinders.
* *Validity.* Validity need not be arithmetical. The existence proof needs only that the runs are uniformly partial computable from finite guesses, and the complexity bound is stated relative to the validity set (z ≤_T (ε*)′).
* *Quantifier audit.* The result is ∃z ∀G ∈ CDZ₂. It is not ∀G ∃x, and not a claim about all of F₂.

**Corollary C4 — PASS.** As P4-S087 Corollary 6, with J⁻¹ ∈ CDZ₂ as an injective map and THM-0035 (SRC-0011, STATEMENT_INSPECTED) for z ∉ MLR.

**Corollaries 5.1–5.3 — PASS.**
* *Inclusions.* FD₂^K ⊆ CDZ₂ for affine K, because Δ = M⁻¹(finite vector) and the finite vectors are countable. Block recodings give FD₂ directly. Linear homeomorphisms are fair by uniqueness of Haar measure.
* *Strictness.* R₂^{cdz} ⊊ R₂^{fd} uses the P4-S087 Theorem 8 witness and F_{T*}∘D′ ∈ CDZ₂ (tail difference vectors). OH^{aff} ⊊ OH^{blk} uses the P4-S083 Theorem 3.8 witness and the linearity of D′.
* *Universality exclusion.* The exclusion for families inside one CDZ₂^J is Corollary C4. Non-co-dispersibility in one DZ₂^J is Theorem B(i).
* *S084.* The error-stream statement is S084 Theorem 1 applied to the CR outputs.

**Proposition D — PASS.**
* *(i) Uncountable cosets.* The transition matrix of the difference recursion is invertible, so (0,0) never occurs and every second step at least is a fresh fair coin. The martingale strong law gives lower density ≥ ⅛ of Δ⊕v for every fixed v.
* *(ii) No common annihilating parity.* For the last support index p, δ_p is conditionally fair unless the state is (1,0), which has probability ≤ ½. The averaging step bounds P(X ≥ 2) ≥ 1/16 for N ≥ 16, using X ≤ N.
* *(iii) Frames.* Controls are fixed by each frame, so the other map's data difference survives in that frame's coordinates.
* *Scope.* The scope note is correct: the fixed-hold U_q and U′_q are themselves CR-preserving, so D is a statement about mechanisms only.

**Analyses — CORRECTLY LABELLED.**
* §6's "conceptual reformulation" (almost-invariance, amenability, spectral gap) is labelled a research direction, with no literature claim.
* §7.1–7.3 are analyses. R₂ ⊊ R₂^{cdz} is explicitly not proved.

**Finite audit — PASS.**
* `python3 phase4/P4-S088_COSET_AUDIT.py` prints `ALL P4-S088 AUDITS PASS` (92,724 checks, ≈1.3 s).
* `python3 phase4/P4-S087_DISPERSION_AUDIT.py` still prints `ALL P4-S087 AUDITS PASS` (8,261 checks).
* These cover finite truncations only.

**Evidence and guard audit — PASS.**
* No source was fetched and no access level changed.
* Only already-catalogued THM-0035 and THM-0038 (via P4-S003) are used.
* R_tot = MLR remains a programme deduction.
* The original Y/M/H/X and all S001–S087 results are frozen, and S057 is not invoked.
* R₂ versus MLR, R₂ versus OH^iso, U(H), X ∈ OH and fixed-S preservation are unresolved and kept separate.
* PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged.
* Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED.
* No novelty, openness, priority, publication or outreach claim. No owner/external blocker.
