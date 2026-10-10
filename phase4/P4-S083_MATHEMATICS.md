# P4-S083 — Tail-coded holes: OH is not homeomorphism-invariant, and R₂ ⊊ OH

Date: 2026-10-10
Scope: Phase 4 Mathematics ONLY; selected CAND-01; pinned incoming live main `d789bf0e0b743f9c49c6419d6fffe2639d74c060` (the P4-S082 outgoing SHA).
Disposition: **The north star is DECIDED NEGATIVELY: R₂ ⊊ OH (Corollary 4.1).**

* **Theorem 3.8.** There is a computably random, non-Martin-Löf-random z with K(z)∈OH for every computable finite-block recoding K, such that D′(z)∉OH. Here D′ is the computable fair homeomorphism D′(z)₀ = z₀, D′(z)ᵢ = zᵢ⊕zᵢ₋₁.
* **The destroyer.** The composite G = F_{T*}∘D′ is a total computable fair-coin-preserving map with all fibres of size ≤ 2, and G(z) is not computably random. Here T* is an explicit one-hole scan of the virtual sequence.
* **Consequences.**
  * z ∈ OH^{blk}∖R₂, so R₂ ⊊ OH, R_k ⊊ OH for all k ≥ 2, and R_fin ⊊ OH.
  * OH^iso ⊊ OH^{blk}: OH is not invariant under computable fair homeomorphisms.
  * The one-hole normalization target selected in P4-S032 fails. The binary-ambiguity resource of k=2 maps strictly exceeds raw one-hole postponement. The extra power comes from **tail-coded holes**: a held virtual bit whose two completions differ on an entire raw tail.
* **Calibration (§1).** Petrović's universal pair of sequence-set (half-betting) strategies gives R_tot = MLR, where R_tot is robustness under ALL total computable fair maps. This is a programme deduction from an unrefereed preprint whose journal version is recorded at metadata level only.
* **NOT decided:** R₂ versus MLR (the primary target of the incoming prompt; still open), R₂ versus OH^iso, OH^iso versus MLR, R_fin versus R₂, U(H), X∈OH, fixed-S preservation, block-H invariance of OH, TKLR∖MLR and QST-0001.

## 0. Authority, uniqueness and frozen objects

* **Pinned main.** `git ls-remote origin refs/heads/main` returned `d789bf0e0b743f9c49c6419d6fffe2639d74c060`. This is the P4-S082 commit whose close record embeds the P4-S083 prompt, and the local branch `ccr-dd3e14c4-j9pfu2` was at the same SHA.
* **Uniqueness.** `phase4/` contained the P4-S001–S082 records and no P4-S083 file. Every repository mention of P4-S083 names it only as the next session, so P4-S083 is unused.
* **Prompt.** The incoming prompt is `authoritative/NEXT_SESSION_PROMPT.md`; no discrepancy was found.

**Reviewed.** S082 in full (Lemmas 2.1–2.4, 3.1–3.2, Propositions 4.1–4.3, Theorems 4.4, 5.1 and 6.1, Proposition 6.2, Examples E1–E3, §7) together with its validation and close records. S081 (Theorem A, Corollaries A1–A6, Theorem B). The phase summaries of S007, S008, S011/S012, S032/S033, S070, S078 and S080. CAND-01, the Gate-3 PASS, both Phase-4 pivots, and SRC-0069/SRC-0070 at their recorded access levels.

**Conventions.** These follow S082 §0.
* A *scan* is a total computable adaptive no-repeat scan (S008). It is *one-hole* if every infinite transcript leaves at most one coordinate unread.
* OH = {z∈CR : F_T(z)∈CR for every one-hole scan T}.
* OH^{blk} = {z : K(z)∈OH for every computable finite-block recoding K} (S082 §5).
* OH^iso = {z : H(z)∈OH for every computable fair homeomorphism H} (S033).
* R_k = the CR sources preserved by every total computable fair-coin-preserving map with all fibres of size ≤ k, and R_fin = ⋂_k R_k (S032).

**Frozen.** The ORIGINAL Y, the clipped syntactically self-avoiding wtt autoreduction M, the repeated H (A=[101;110;111]) and X = H⁻¹(Y) are untouched; nothing below uses them. All P4-S001–S082 results are frozen. In particular, S082's consistency-potential lemmas are used verbatim, and S057 is not invoked.

## 1. Decision-relevant literature calibration (recorded access levels)

Deciding R₂ versus MLR is decision-relevant, so a bounded external check was made of the nearest frameworks. New and updated catalogue records:

| Record | Content used | Access |
|---|---|---|
| SRC-0060 Rute, *Computable randomness and betting for computable probability spaces* (update) | §10 in full (arXiv:1203.5535v4 text). Definition 10.1 and Proposition 10.2 (endomorphism randomness, ER). Definition 10.3 (balanced and exhaustive betting strategies). Theorem 10.4 with proof (ER ⟺ no exhaustive/balanced computable betting strategy succeeds). Corollaries 10.5–10.7 (ER ⊆ KLR; CR not preserved by endomorphisms). The chain (10.1) MLR → ER → automorphism random (AR) → KLR. Question 10.8 (does any implication of (10.1) reverse?). Footnote 11 (Petrović's claimed pair of balanced strategies, which "would imply" ER = MLR). | STATEMENT_INSPECTED (proof of Thm 10.4 read) |
| SRC-0071 Petrović, *A pair of universal sequence-set betting strategies* (arXiv:1210.5968v9, 2015). Journal version recorded as *A universal pair of 1/2-betting strategies*, Inf. Comput. 281 (2021) 104703, from a reference list only. | Definitions 2.1–2.7 (mass placements, grids, mass-placement tests; sequence-set betting strategies, i.e. level-i cells of measure 2⁻ⁱ). Theorem 1 (for every ML test there are two computable sequence-set strategies, one of which succeeds on every sequence failing the test). Lemmas 3.1–3.3 with proofs. The remark that no single computable sequence-set strategy is universal. | preprint STATEMENT_INSPECTED with proof read; journal version METADATA_ONLY |
| SRC-0019 Petrović, *Kolmogorov–Loveland betting strategies lose the betting game on open sets* (update; TCS 1037 (2025) 115177; arXiv:2403.19817v2 text read) | Abstract and introduction: classes previously shown equivalent to MLR each contain finitely many strategies that win on small effective open sets, and Shen's van Lambalgen pair of atomless general strategies. Definitions 2.1–2.4, Theorem 1 (main theorem) and Definition 3.1 (the betting game on open sets). | STATEMENT_INSPECTED |
| SRC-0072 Petrović, *Betting strategies with bounded splits* (arXiv:2212.14279v1) | Abstract only: two conditions under which a pair of KL strategies cannot win on every non-MLR sequence | ABSTRACT_INSPECTED |

**Proposition 1.1 (programme deduction from SRC-0071).** Let R_tot := {x∈CR : Φ(x)∈CR for every total computable λ-preserving Φ: 2^ω→2^ω}. Then R_tot = MLR.

*Proof.*
* *A sequence-set strategy is a fair map with a martingale.* Let S be a computable sequence-set strategy: a computable sequence of finite clopen partitions 𝒜₀ ≼ 𝒜₁ ≼ … of 2^ω, with every cell of 𝒜ᵢ of measure 2⁻ⁱ, and a computable additive mass function μ. Each A∈𝒜ᵢ is the union of exactly two cells of 𝒜ᵢ₊₁; order them computably as A0, A1. Then Φ_S(x) := the unique y with x∈A_{y↾i} for all i is total computable, and λ(Φ_S⁻¹[w]) = λ(A_w) = 2^{−|w|}. The function d_S(w) := μ(A_w)/λ(A_w) is a computable martingale.
* *Success transfers.* By SRC-0071 Definition 2.5, x fails S iff sup_i d_S(Φ_S(x)↾i) = ∞.
* *Universality.* Apply SRC-0071 Theorem 1 to a universal ML test. Every x∉MLR has Φ_{S^j}(x)∉CR for some j∈{0,1}; computable real-valued martingale success implies rational-valued success, by the standard equivalence. Hence R_tot ⊆ MLR.
* *Converse.* MLR ⊆ R_tot because computable measure-preserving maps conserve MLR (the S032 citation), and MLR ⊆ CR. ∎

**What is and is not taken from these sources.**
* *Petrović's maps have unbounded fibres.* Their cells need not shrink to finite sets. Proposition 1.1 therefore says nothing about R_fin or R₂. It shows only that bounded fibre size is exactly the resource separating R₂ from MLR (§5).
* *Status of the inputs.* Proposition 1.1 inherits the correctness of an unrefereed preprint. The journal version was not inspected, and Rute's footnote describes the result as "claimed". No inference about ER, AR or Question 10.8 is drawn beyond what the sources state.
* *Rute's question is not used.* SRC-0060 Question 10.8 is recorded as QST-0002, SOURCE-STATED OPEN with 2016 evidence; no later status check was made.
* *SRC-0019's open-set game is framing only.* No result below depends on it. The single-goal game is too weak to capture the nested (Martin-Löf) setting of §3.
* *No proof depends on SRC-0019, SRC-0071 or SRC-0072.*
* *No novelty, priority or openness inference* is drawn from what these sources contain or omit.

## 2. Tail-coded holes

Let D′: 2^ω→2^ω be D′(z)₀ = z₀ and D′(z)ᵢ = zᵢ⊕zᵢ₋₁ for i ≥ 1. Its inverse is the prefix parity zᵢ = v₀⊕…⊕vᵢ. Both maps are computable, and D′ restricts to a bijection of {0,1}ⁿ for every n. So D′ is a computable fair-coin-preserving homeomorphism. It is not a finite-block recoding: every raw coordinate zᵢ depends on all of v₀,…,vᵢ (S082 Example E3).

**Lemma 2.1 (tail-coded hole).** Let v = D′(z), q ≥ 0 and M > q. Put z₋₁ := 0 and π_F := z_{q−1}⊕v_{q+1}⊕…⊕v_F for q ≤ F < M (so π_q = z_{q−1}). Then:
(i) z↾q is determined by v↾q;
(ii) for q ≤ F < M, z_F = π_F ⊕ v_q;
(iii) flipping v_q alone changes z↾M to z↾q ⌢ (complement of z↾[q,M)). So the two completions of a hole at v_q are the raw pair {z, z⊕1_{[q,∞)}} restricted to [0,M).
In particular, any single absolute raw value z_F with q ≤ F < M, together with the virtual bits other than v_q, determines v_q = z_F⊕π_F.

*Proof.* Telescoping zⱼ = zⱼ₋₁⊕vⱼ. ∎

**Why this differs from a raw hole.** A one-hole scan of D′(z) holding v_q knows z↾q exactly and z↾[q,M) up to one global complement.
* *Coded hole.* Every raw coordinate F ≥ q splits the two candidates. In S082 terms, s^{σ,k} = 1 for every candidate k ≥ q (Example E3), and this is a single bit of information, unlike S082 Example E1.
* *Raw hole.* A raw one-hole scan holding z_q has candidates {z, z⊕e_q}, which only z_q itself separates. The construction of S082 can always fix a coordinate outside a raw hole (Lemma 3.1), but it cannot fix a coordinate above max dom σ outside a tail-coded hole held at q ≤ max dom σ + 1.

§3 converts this asymmetry into a separation.

## 3. The separation construction

### 3.1 Class-separated runs

Fix a computable bijection ι: {0,1}^{<ω}→ℕ and Cantor pairing ⟨·,·⟩, and put C_ε := {⟨ι(ε), j⟩ : j∈ℕ}. The classes C_ε (ε∈{0,1}^{<ω}) are pairwise disjoint, infinite and uniformly decidable, with uniformly computable increasing enumerations.

**The runs.** Repeat S082 §5 (the version of §4 over triples (K_e, T_e, θ_e), with K_e ranging over computable finite-block recodings) verbatim, with ONE change in stage (b). At stage i of run R(ε) the candidates are taken from the class C_{ε↾(i+1)}:
* k₁ := the least element of C_{ε↾(i+1)} that is ≥ a, where a := 1 + max dom σ (a := 0 if σ = ∅);
* k_{r+1} := the least element of C_{ε↾(i+1)} greater than k_r that lies outside every block, of every partition K_e with e∈A, containing one of k₁,…,k_r;
* K₀ := {k₁,…,k_{N_i}}.

n, τ″, the choice of k minimizing Γ(σ,k,τ″) and the choice of b minimizing Φ(σ_b,τ″) are unchanged.

**Lemma 3.1 (S082 invariants survive).** Propositions 4.1 and 4.2 of S082, in their §5 form, hold verbatim for the class-separated runs. If every e ≤ i with ε(e) = 1 is valid, then R(ε) completes stage i with Φ(σ^ε_i, τ^ε_i) < 2 − 2^{−i}. Also |dom σ^ε_i| = (i+1)(i+2), so V_i := ⋃{[σ^ε_i] : |ε| = i+1, R(ε) completes stage i} is a Martin-Löf test with λ(V_i) ≤ 2^{−(i+1)²}.

*Proof.* The proofs use only these properties of K₀: its elements lie outside dom σ, below n ≤ every active frontier at τ″, and in pairwise distinct blocks of every active partition. Then S082 Lemma 3.2 gives Σ_{k∈K₀} γ^e(σ,k,τ″) ≤ Ψ^e(σ,τ″) for each active e. The class restriction preserves all three properties, since each class is infinite and blocks are finite. ∎

Let ε* be the characteristic sequence of validity, σ*_i := σ^{ε*↾(i+1)}_i, τ*_i := τ^{ε*↾(i+1)}_i, w_e the true weights, and S := ⋂_i [σ*_i]. By Lemma 3.1, S ⊆ ⋂_i V_i, so no element of S is Martin-Löf random.

**Lemma 3.2 (class separation).** Let ε'∈{0,1}^{<ω} with m := |ε'| ≥ 1 be such that R(ε') completes all m stages, and put σ' := σ^{ε'}_{m−1}. Then for every j and every k ∈ dom σ'∩dom σ*_j, σ*_j(k) = σ'(k).

*Proof.* Stage s of a run depends only on the guess prefix of length s+1 and on the state after stage s−1.
* *Prefix case.* If ε' ⊑ ε*, then σ' = σ*_{m−1}, which is compatible with σ*_j.
* *Incomparable case.* Otherwise let e be least with ε'(e) ≠ ε*(e). By induction on s < e, stages 0,…,e−1 of R(ε') and R(ε*) coincide. So the coordinates R(ε') fixes before stage e are fixed with the same values by R(ε*), and occur in σ*_{e−1}, which is compatible with every σ*_j. Any coordinate R(ε') fixes at a stage s ≥ e lies in C_{ε'↾(s+1)}. The string ε'↾(s+1) differs from ε*↾(s+1), at position e, and from every ε*↾(s'+1) with s' ≠ s, in length. Hence C_{ε'↾(s+1)} is disjoint from every class used by the true run, and in particular from dom σ*_j. ∎

### 3.2 The tail-coded scan T*

T* reads a virtual sequence v. Its state is a *hold* q and a *filler frontier* M > q; the read set is [0,M)∖{q}. Initially q = 0 and M = 1.
* *Known data.* From the read bits, T* computes z_k := v₀⊕…⊕v_k for k < q, and π_F for q ≤ F < M as in Lemma 2.1.
* *Qualification.* At a transcript of length t, T* runs every R(ε') with ι(ε') < t for t steps. A run that has completed all its stages, with m := |ε'| and σ' := σ^{ε'}_{m−1}, *qualifies at (q,M)* if:
  * (Q1) σ'(k) = z_k for every k∈dom σ'∩[0,q);
  * (Q2) dom σ'∩[q,∞) has at least r := r(q,m) := q + 2m + 4 elements, and its r least elements F₁<…<F_r are all < M;
  * (Q3) the implied values ν_l := σ'(F_l)⊕π_{F_l} (l = 1,…,r) are all equal; call the common value ν.
* *Moves.* If some run qualifies, take the qualifying ε' with least ι(ε') and **resolve**: query v_q with all capital wagered on v_q = ν, then set q := M and M := M+1. Otherwise query the filler v_M with zero stake and set M := M+1.
* *Martingale.* The output martingale d* starts at 1, doubles at a correct resolution, drops to 0 at a wrong one, and is unchanged at fillers.

**Lemma 3.3 (validity).**
(i) T* is a total computable adaptive no-repeat scan, and every infinite transcript leaves at most one coordinate unread.
(ii) d* is a rational-valued computable martingale on outputs.
(iii) F_{T*} is λ-preserving with all fibres of size ≤ 2, so G := F_{T*}∘D′ is a total computable λ-preserving map with all fibres of size ≤ 2.

*Proof.*
* *Totality.* Each step is a finite computation with a t-step simulation budget.
* *No repeats.* Each query is the current q or the current M, and neither has been read before.
* *One hole.* If a transcript resolves infinitely often, the holds increase strictly and every coordinate is eventually read, either as a filler or at its resolution. If it resolves only finitely often, the final hold is the only coordinate never read.
* *Fairness.* A total adaptive no-repeat scan preserves λ (S008), and a one-hole scan has fibres of size ≤ 2.
* *Composite.* D′ is a fair homeomorphism, so G inherits totality, λ-preservation and the fibre bound. ∎

### 3.3 Predictions and the fooling set

**Lemma 3.4 (prediction).** Let x∈2^ω and v = D′(x), and suppose T* resolves hold q on v using ε' and positions F₁,…,F_r. If x_{F₁} = σ'(F₁), the prediction is correct (ν = v_q). If the prediction is wrong, then x_{F_l} ≠ σ'(F_l) for every l ≤ r.

*Proof.* By Lemma 2.1(ii), x_{F_l}⊕π_{F_l} = v_q for every l. By (Q3), σ'(F_l)⊕π_{F_l} = ν for every l. Hence ν = v_q iff σ'(F_l) = x_{F_l} for one (equivalently every) l. ∎

For q∈ℕ and ε' with |ε'| = m ≥ 1, let B(q,ε') := {x : x_{F_l} ≠ σ'(F_l) for l = 1,…,r(q,m)}. Here F_l are the r(q,m) least elements of dom σ^{ε'}_{m−1}∩[q,∞), and B(q,ε') := ∅ if R(ε') does not complete or there are too few such elements. Let **W** := {x : T* makes a wrong resolution on D′(x)}. W is open (a wrong resolution is witnessed by a finite transcript), and W ⊆ ⋃_{q,ε'} B(q,ε') by Lemma 3.4.

**Lemma 3.5 (fooling bound).** For every j, λ(W∩[σ*_j]) ≤ ⅛·λ[σ*_j].

*Proof.* Fix (q,ε') and its positions F₁,…,F_r.
* *Some position is fixed.* If some F_l ∈ dom σ*_j, then σ*_j(F_l) = σ'(F_l) by Lemma 3.2, so B(q,ε')∩[σ*_j] = ∅.
* *No position is fixed.* Then the F_l are r distinct coordinates outside dom σ*_j, and λ(B(q,ε')∩[σ*_j]) = 2^{−r}λ[σ*_j].
* *Sum.* There are 2^m strings of length m, so
  Σ_{q≥0} Σ_{m≥1} 2^m·2^{−(q+2m+4)} = 2^{−4}·(Σ_{q≥0}2^{−q})·(Σ_{m≥1}2^{−m}) = 2^{−4}·2·1 = ⅛. ∎

**Lemma 3.6 (every hold is resolved on S).** If x∈S, then T* resolves every hold it reaches on D′(x).

*Proof.* Fix a hold q and let m be large.
* *Completion.* R(ε*↾m) completes, by Lemma 3.1.
* *(Q1).* It holds because x∈[σ*_{m−1}].
* *(Q2).* At most q of the m(m+1) coordinates of dom σ*_{m−1} lie below q. So once m² − m ≥ 2q + 4, at least r(q,m) of them lie in [q,∞).
* *(Q3).* x_F = σ*_{m−1}(F) for every F∈dom σ*_{m−1}, so ν_l = x_{F_l}⊕π_{F_l} = v_q for all l.
* *Timing.* While q is held, T* keeps reading fillers, so M→∞, and the simulation budget t→∞. Hence some run qualifies (ε*↾m, or an earlier one), and T* resolves q. ∎

### 3.4 Compactness with an excluded fooling set

**Proposition 3.7.** There is z∈S∖W such that X^e_t(z) ≤ L_e := 2 + 4/w_e for every valid e and every t. Here X^e_t is the savings capital of S082 §4, along F_{T_e}(K_e(z)).

*Proof.*
* *Setup.* Suppose not, and let O := ⋃_{e valid}{z : ∃t X^e_t(z) > L_e}. Then S ⊆ O∪W, which is open.
* *Finite witnesses.* The sets [σ*_i] are compact and decreasing with intersection S, so [σ*_{i₀}] ⊆ O∪W for some i₀. By compactness of [σ*_{i₀}], there are finitely many witnesses (e_r,t_r), each with a clopen set {X^{e_r}_{t_r} > L_{e_r}}, and finitely many clopen sets W₁,…,W_p ⊆ W, all together covering [σ*_{i₀}].
* *Large capital off the W-pieces.* Let j ≥ max(i₀, max_r e_r) and t ≥ max(max_r t_r, τ*_j). Each z∈[σ*_j]∖⋃W_l has some r with X^{e_r}_{t_r}(z) > L_{e_r}. By the savings drop bound (S082 Lemma 2.4(ii)), X^{e_r}_t(z) > L_{e_r} − 2 = 4/w_{e_r}, so Σ_{e active} w_e X^e_t(z) > 4.
* *Lower bound on Φ.* By weighted domination (S082 Lemma 2.2) and Lemma 3.5,
  Φ(σ*_j,t) ≥ 2^{|σ*_j|}∫_{[σ*_j]∖⋃W_l} Σ_e w_e X^e_t dλ > 4·(1 − ⅛) = 7/2.
* *Upper bound on Φ.* By S082 Lemma 2.1 and Lemma 3.1, Φ(σ*_j,t) ≤ Φ(σ*_j,τ*_j) < 2. Contradiction. ∎

### 3.5 The theorem

**Theorem 3.8 (tail-coded separation).** Let z be as in Proposition 3.7. Then:
(i) z is not Martin-Löf random;
(ii) for every computable finite-block recoding K (including the identity), K(z) is computably random and lies in OH. In particular z∈OH^{blk} ⊆ OH^{lin3} ⊆ OH and z∈CR;
(iii) on D′(z), T* resolves infinitely often and every resolution is correct. So d* is unbounded along F_{T*}(D′(z)), D′(z)∉OH, and the ≤2-to-1 map G = F_{T*}∘D′ has G(z)∉CR;
(iv) z can be chosen computable from ∅‴.

*Proof.*
(i) z∈S ⊆ ⋂V_i.
(ii) Every valid savings capital is bounded along z. By S082 Lemma 2.4(iii) and the triple form of Fact 4.0 (S082 Theorem 5.1), every one-hole scan of every K(z), the identity scan included, fails to succeed.
(iii) By Lemma 3.6 every hold reached is resolved, so there are infinitely many resolutions. Since z∉W, all of them are correct. So d* doubles infinitely often and never drops.
(iv) Validity is arithmetical (S082 §5). S is Π⁰₁(∅″), O is Σ⁰₁(∅″) and W is Σ⁰₁. So S∖(O∪W) is a nonempty Π⁰₁(∅″) class, and its leftmost path is ∅‴-computable. ∎

## 4. Consequences

**Corollary 4.1 (north star decided negatively).** R₂ ⊊ OH. More precisely, OH^{blk}∖R₂ ≠ ∅ and (OH^{blk}∖MLR)∖R₂ ≠ ∅. Since R_k ⊆ R₂ for k ≥ 2 and R_fin ⊆ R₂, also R_k ⊊ OH and R_fin ⊊ OH.

*Proof.* z of Theorem 3.8 lies in OH^{blk} ⊆ OH, and G of Lemma 3.3(iii) is a total computable fair-coin-preserving map with fibres of size ≤ 2 such that G(z)∉CR. Hence z∉R₂. R₂ ⊆ OH is S032. ∎

**Corollary 4.2 (OH is not homeomorphism-invariant).** z∈OH while D′(z)∉OH, so OH^iso ⊊ OH^{blk}. The landscape is

  MLR ⊆ R₂ ⊆ OH^iso ⊊ OH^{blk} ⊆ OH^{lin3} ⊆ OH,

and neither OH nor OH^{blk} is invariant under the computable fair homeomorphism D′. Dually, CR∖OH is not invariant under D′⁻¹: D′(z)∈CR∖OH, but D′⁻¹(D′(z)) = z∈OH.

**Corollary 4.3 (one-hole normalization fails).** The sustained target selected in P4-S032 asked whether every global-k=2 destruction normalizes to a raw one-hole scan. G destroys z, and no raw one-hole scan does. The binary ambiguity that G exploits is the tail-coded hole of Lemma 2.1. At a held virtual coordinate, the two completions differ on the whole raw tail [q,∞), and any later absolute fact about the tail resolves the hole. On z itself the fibre of G is a singleton, because T* resolves infinitely often. A double fibre of G arises only on transcripts with a final permanent hold, and it then has the infinite raw difference set [q,∞).

**Remark 4.4 (relation to S082).** The witness uses exactly the S082 Example E3 boundary. S082 Corollary 5.2 already predicted that a separation witness must use non-block recodings or non-scan maps; Theorem 3.8 realizes the first route.
* *Values do not matter.* The S082 potential still chooses every fixed value adversarially against all raw and block-recoded one-hole scans. T* does not care which value is chosen. It waits, holding a tail-coded bit, until a run has made its choice, and then reads the choice off.
* *Raw holes can be avoided, tail-coded holes cannot.* A raw scan that waited in the same way would have to hold the chosen coordinate itself, and the candidate selection of S082 avoids held coordinates. A tail-coded hole at q covers every candidate above q.
* *Classes bound the fooling.* The class separation of §3.1 is what makes the fooling set W small relative to [σ*_j].

**Remark 4.5 (what is not shown).**
(a) *Potential-built witnesses are not proved to lie outside OH^iso.* T* can be fooled; Part 3 of the audit exhibits an adversarial completion that fools it. A different construction could therefore try to select z∈S∩W, and Theorem 3.8 needs the exclusion of W. Whether OH^iso∖MLR is nonempty is open.
(b) *R₂ versus MLR, R₂ versus OH^iso and R_fin versus R₂ are open.*
(c) *Block recodings are untouched.* D′ is not a finite-block recoding. The block-H questions (S070 H-preservation, S078 fixed-S preservation, S080 U(H), X∈OH) are untouched, and Theorem 5.1 of S082 (OH^{blk}∖MLR ≠ ∅) is consistent with, and refined by, Theorem 3.8.

## 5. The new landscape and the remaining question

  MLR = R_tot ⊆ R_fin ⊆ R_k ⊆ R₂ ⊆ OH^iso ⊊ OH^{blk} ⊆ OH^{lin3} ⊆ OH = OH_h = R_k^scan ⊊ CR  (k ≥ 2, h ≥ 1),
  MLR ⊊ OH,  OH^{blk}∖R₂ ≠ ∅,  KLR ⊆ TKLR ⊆ OH,  Rute: MLR ⊆ ER ⊆ AR ⊆ KLR.

The first equality, MLR = R_tot, is Proposition 1.1, a programme deduction from SRC-0071.

The S082 §7.2 trichotomy loses case (γ): R₂ = OH is now refuted. Exactly one of the following holds, and both remain open:
* **(α) R₂ = MLR.** The bounded-fibre preservation notion of CAND-01 would then collapse to Martin-Löf randomness, which is equal to unbounded-fibre robustness R_tot.
* **(β) MLR ⊊ R₂ ⊊ OH.** R₂ would then be a genuinely intermediate notion.

So **R₂ versus MLR is the decisive remaining question for CAND-01**. This is a consequence for the programme's own objective, not a novelty or significance claim. Two necessary conditions follow from what is proved:
* any z∈R₂∖MLR lies in OH^iso, so it must defeat every tail-coded-hole scan, including self-referential ones that simulate the construction;
* any proof of R₂ = MLR must exploit bounded fibres in a way Petrović's unbounded-fibre strategies do not need.

## 6. Finite audit

`phase4/P4-S083_SEPARATION_AUDIT.py` checks finite components in exact arithmetic (about 7 s):
* **Part 1.** Lemma 2.1: 120000 identities on random 24-bit prefixes and all hold positions.
* **Part 2.** Lemma 3.2 on a toy family of class-separated runs (all guesses up to length 3, stage s fixing 2s+2 class coordinates): 866 nesting and separation checks.
* **Part 3.** The scan T* on D′(z) with a toy threshold r = 2, over 480 completions consistent with the eight true runs of length 3:
  * no repeats, and at most one unread coordinate below the filler frontier;
  * 3127 resolutions, with "wrong ⟺ anti-consistent on all selected fixes" verified at every one;
  * all 2414 selections of true-run prefixes were correct;
  * 323 random fooling events, and an adversarial completion that fools T*.
* **Part 4.** An exact fibre count on all 2¹⁴ raw prefixes: every T*-transcript of D′(x) has at most two raw preimage prefixes.
* **Part 5.** The exact series Σ_{q,m} 2^m 2^{−(q+2m+4)} = ⅛, and the compactness constant 4·(1−⅛) = 7/2 > 2.

The audit prints `ALL P4-S083 AUDITS PASS`. The frozen `phase4/P4-S082_POTENTIAL_AUDIT.py` was re-run and still prints `ALL P4-S082 AUDITS PASS`. The audits cover finite truncations only. Validity guessing, the Martin-Löf test, compactness, computable randomness and OH membership rest on the written proofs.

## 7. Analysis of the primary target, failed or deferred routes

**7.1 The exact fixing-martingale (analysis).** For any total computable λ-preserving G, any savings-transformed d = A+B (S082 Lemma 2.4) and any partial assignment σ, put β(σ,t) := 2^{|σ|}∫_{[σ]} B_t∘G dλ and β(σ) := sup_t β(σ,t).
* *Exactness.* ½(β(σ₀)+β(σ₁)) = β(σ) exactly. Each β(·,t) is additive over [σ] = [σ₀]⊔[σ₁], and B_t is non-decreasing in t.
* *Bracket.* The conditional capital 2^{|σ|}∫_{[σ]}X_t∘G lies in [β(σ,t), β(σ,t)+2).

So a construction that could compare β(σ₀) with β(σ₁) would pay no fixing cost at all, for any fibre size. All the difficulty lies in making such comparisons computably from finitely many guesses: β is only left-c.e., and guessing it to precision 2^{−ℓ} costs about ℓ guess bits, which cancels the compression of ℓ fixed bits. For the class of all total fair maps the obstruction is unavoidable, because R_tot = MLR (Proposition 1.1). This settles option (c) of the prompt for that class, in a weak sense only. For globally ≤2-to-1 maps, S082 Proposition 6.2's counting potential Π_∞ = Ψ_∞ + (unresolved persistent pair weight) is the corresponding exact fixing-martingale, with Π_∞ ≤ 2Ψ_∞. Again only the computability of choices is at issue.

**7.2 Attempted routes to R₂∖MLR ≠ ∅ (not completed).**
* *Ψ-accounting.* Pays the full capital-weighted mass of every thick pair at each split (Examples E2/E3). Tail-coded holes renew this cost at every advance of max dom σ.
* *Tracked counting potentials Ψ̃_{[0,n)}.* These make fixings below n free, but the weight of invisible pairs (difference sets beyond n) can concentrate on the chosen branches by a factor 2 per fixing. No computable modulus controls this.
* *Guessing a tracking precision or a settling time.* Costs self-delimiting description length, which non-computable moduli can make exceed the compression gained.

The separation of §3 shows that this obstacle is real for constructions of the S082 type: a self-aware tail-coded scan wins whenever the selected witness avoids its fooling set.

**7.3 Attempted route to R₂ = MLR (not completed).** Generalizing T* to an arbitrary non-MLR z requires orienting tail-coded holes from an arbitrary ML test. Both completions of a hole are computable images of each other, so both are non-MLR, and their enumeration races are not separated by any argument found. Petrović's universality uses unbounded fibres, through losing streaks that never resolve low coordinates. No bounded-fibre substitute was found.

**7.4 Not attempted, as instructed.** A record-only proof of z₀∈OH; finite price, escrow, hazard or renewal work; residue tables; unit-column enumeration; multi-hole variants. Every scan above is total, computable, no-repeat, fair and at most one-hole on every transcript, and G is total, computable and fair with all fibres of size ≤ 2.

## 8. Disposition

**Proved.**
* Lemma 2.1 (tail-coded holes).
* Lemmas 3.1–3.6.
* Proposition 3.7.
* **Theorem 3.8: z∈OH^{blk}∖MLR with D′(z)∉OH and G(z)∉CR for a ≤2-to-1 total computable fair G.**
* **Corollary 4.1: R₂ ⊊ OH, so the north star R₂ = OH is FALSE.** Also R_k ⊊ OH and R_fin ⊊ OH.
* Corollary 4.2: OH^iso ⊊ OH^{blk}, and OH is not invariant under computable fair homeomorphisms.
* Corollary 4.3: one-hole normalization fails.
* Proposition 1.1, a programme deduction from SRC-0071: R_tot = MLR.
* The §7.1 fixing-martingale analysis.

**Recorded.** SRC-0060 and SRC-0019 updates; new SRC-0071, SRC-0072; THM-0079, THM-0080, THM-0081; QST-0002 (Rute Question 10.8, SOURCE-STATED OPEN, 2016 evidence); DEF-0066 (automorphism randomness).

**Unresolved.**
* R₂ versus MLR, now the decisive CAND-01 question.
* R₂ versus OH^iso, OH^iso versus MLR, R_fin versus R₂.
* U(H), X∈OH, fixed-S preservation, block-H invariance of OH.
* TKLR∖MLR and QST-0001.

**Frozen.**
* All P4-S001–S082 results, including S008, S011/S012, S027 clipping, S033, S037, S070–S082, and S057 (exact four paired clipped traces, prospective deadlines, genuine fillers, t/u zero-stake timeout release, mandatory non-s sweep without old-sentinel reset, seven 8/7 versus one ZERO; NOT invoked).
* The original Y/M/H/X.
* PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged.
* Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED.

No novelty, openness, prior-art, publication or outreach claim is made. No owner or external blocker.

**Next: P4-S084.** Decide R₂ versus MLR, either by constructing z∈R₂∖MLR (which must first lie in OH^iso and defeat tail-coded holes) or by proving R₂ = MLR. R₂ versus OH^iso is the secondary target.
