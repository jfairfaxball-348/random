# P4-S087 — Dispersible ambiguity: one simultaneous survivor for all finite-difference width-two observers, and the E₀-breaking frontier of R₂ versus MLR

Date: 2026-10-10. Scope: Phase 4 Mathematics ONLY; selected CAND-01.
Incoming independently pinned live main: `7435c93ec127f4fc2527a883917fb90784db4464`, exactly the P4-S086 outgoing commit (parent `453439b56f4bcf44b8539974969f0bed1a59773f` = P4-S085 outgoing, as recorded in the P4-S086 close).

**Disposition: R₂ versus MLR is NOT decided. Neither Route A nor Route B closed.** The session proves a genuinely simultaneous survivor theorem that goes strictly beyond the P4-S086 rank-one obstruction, and isolates the exact remaining frontier.

* **Theorem 4 (dispersed survivor).** Some z ∈ CR∖MLR has G(z) ∈ CR for EVERY total computable fair map G with all fibres of size ≤ 2 whose double fibres have, almost surely, density-zero difference sets. In particular this holds for every G whose two-point fibres a.s. differ in only finitely many coordinates. The quantifier order is ∃z ∀G over the whole class: this is not the ∀G ∃x_G fact of P4-S086. The class contains non-scan maps, maps with phantoms, and every one-hole scan of every block recoding.
* **Corollary 6 (frames).** The same holds after any single computable fair homeomorphic change of coordinates J. Consequently no family of width-two observers that is dispersible in one common computable frame is universal for CR∖MLR. Such families can be genuinely multi-observer: for one explicit graded frame they include every one-hole scan of every K∘D′ʲ(z), for all j ∈ ℕ and all block recodings K. That includes every tail-coded observer T∘D′, the S083 T* among them.
* **Theorem 8 (E₀-breaking separation).** There is z ∈ CR∖MLR surviving every finite-difference width-two map, yet destroyed by the tail-coded map G = F_{T*}∘D′ ∈ F₂. So R₂ ⊊ R₂^{fd}. This strengthens S083 Theorem 3.8: there, survival was against one-hole scans of block recodings only.
* **The frontier.** Any proof of R₂ = MLR must use, in every computable coordinate frame, width-two maps whose ambiguity is not dispersible: positive-measure double fibres with non-density-zero (e.g. tail) difference sets. Any z ∈ R₂∖MLR must defeat exactly such maps, including every frame-transported T*.

## 0. Authority, uniqueness and frozen objects

* **Pinned main.** `git ls-remote origin refs/heads/main` returned `7435c93…`. Its commit metadata gives parent `453439b…`, the P4-S085 outgoing SHA. The P4-S086 close record states that its outgoing SHA is the hash of its own atomic commit, and that commit is `7435c93…`. Reconciled.
* **Uniqueness.** `phase4/` contained no P4-S087 file. Every repository mention of P4-S087 names it only as the next session.
* **Prompt.** The incoming prompt is identical in substance to `authoritative/NEXT_SESSION_PROMPT.md`.
* **Reviewed.** Cumulative P4-S001–S086 records, with detail on S003–S008, S011–S012, S032–S033 and S081–S086 (including the S086 validation and close). Also CAND-01, the Gate-3 PASS, both Phase-4 pivots, and SRC-0015, SRC-0019, SRC-0060, SRC-0069–SRC-0072 at their RECORDED access levels. No source was fetched and no access level changed.
* **Frozen.** MLR = R_tot ⊆ R_fin ⊆ R_k ⊆ R₂ ⊆ OH^iso ⊊ OH^blk ⊆ OH^lin3 ⊆ OH = OH_h = R_k^scan ⊊ CR (k ≥ 2); R₂ ⊊ OH; MLR ⊊ OH; KLR ⊆ TKLR ⊆ OH. R_tot = MLR remains a programme deduction from SRC-0071's inspected preprint (journal version METADATA_ONLY). The S084 predictable-error theorem, ML-null infinite-resolution locus and balanced a.e. two-sheet destroyer are frozen. S085's c(n) criterion is a representation only. S086 Theorems 1–3 are frozen. The original computably random Y, the unchanged globally use-clipped syntactically self-avoiding wtt autoreduction M, the repeated three-bit H with A = [101;110;111], and X = H⁻¹(Y) are untouched; nothing below uses them. S057 is not invoked. There are no escrow, hazard, residue, unit-column, record-only z₀ or multi-hole detours.

## 1. Definitions

**Maps and strategies.** F₂ is the class of everywhere-total computable λ-preserving G: 2^ω→2^ω with |G⁻¹(y)| ≤ 2 for every y. A *width-two strategy* is a pair (G,d) with G ∈ F₂ and d a rational-valued computable martingale on outputs. As in S082 §2, we always pass to the savings transform d = A + B (S082 Lemma 2.4): 0 ≤ A < 2, B is non-decreasing along every output sequence, and B_∞(y) := lim_t B(y↾t). Since E_λ[B(y↾t)] ≤ E_λ[d(y↾t)] = d(∅) = 1, monotone convergence gives **E_λ[B_∞] ≤ 1**.

**Difference sets.** For an output y with G⁻¹(y) = {x, x′}, x ≠ x′, put Δ_G(y) := {k : x_k ≠ x′_k}. Then:
* **FD₂** is the class of G ∈ F₂ such that λ-almost every output with two preimages has Δ_G(y) finite.
* **DZ₂** is the class of G ∈ F₂ such that λ-almost every output with two preimages has lim_{R→∞} |Δ_G(y)∩[0,R)|/R = 0.
* FD₂ ⊆ DZ₂.
* R₂^{fd} := {z ∈ CR : G(z) ∈ CR for all G ∈ FD₂}, and R₂^{dz} is defined likewise with DZ₂. Hence R₂ ⊆ R₂^{dz} ⊆ R₂^{fd}.

**Consistency potential.** Ψ(σ,t), the split weight γ(σ,k,t), the indicator s^{σ,k} and Lemmas 2.1–2.3 are exactly as in S082 §2. Lemmas 2.1–2.3 hold for every total λ-preserving G. Write X_t(y) := d(y↾t). Since G is fair, Σ_{w∈2^t}2^{−t}d(w)g(w) = E_λ[X_t(y)g(y↾t)] for any g on output strings.

**Frames.** For a computable fair homeomorphism J, put FD₂^J := {G ∈ F₂ : G∘J⁻¹ ∈ FD₂}, and similarly DZ₂^J.

**E₀.** E₀ is the relation "x and x′ differ in only finitely many coordinates".

## 2. The dispersed cost lemma

Fix (G,d), a partial assignment σ and a finite set K₀ disjoint from dom σ, |K₀| = N. For output strings w put

  f(w) := Σ_{k∈K₀} s^{σ,k}(w)  (number of candidates on which the σ-consistent part of the cell G⁻¹[w] splits).

**Lemma 1 (monotone limit identification).** For every output y and k ∉ dom σ:
(i) s^{σ,k}(y↾(t+1)) ≤ s^{σ,k}(y↾t), and likewise c^σ and f are non-increasing along y;
(ii) s^{σ,k}(y↾t) is eventually equal to s^{σ,k}_∞(y) := 1 if G⁻¹(y) ⊆ [σ], |G⁻¹(y)| = 2 and k ∈ Δ_G(y), and 0 otherwise;
(iii) f(y↾t) is eventually equal to f_∞(y) := |K₀∩Δ_G(y)|·1(G⁻¹(y) ⊆ [σ], |G⁻¹(y)| = 2).

*Proof.* (i) G⁻¹[wb] ⊆ G⁻¹[w]. (ii) For b ∈ {0,1}, the sets G⁻¹[y↾t]∩[σ]∩{z_k = b} are compact and decreasing in t, with intersection G⁻¹(y)∩[σ]∩{z_k = b}. A decreasing sequence of compact sets has nonempty intersection iff all its members are nonempty. So s^{σ,k}(y↾t) = 1 for all t iff G⁻¹(y)∩[σ] meets both {z_k=0} and {z_k=1}. As |G⁻¹(y)| ≤ 2, this happens iff both preimages lie in [σ] and differ at k. The indicator is {0,1}-valued and non-increasing, so it is eventually constant. (iii) Sum (ii) over the finitely many k ∈ K₀. ∎

No width modulus c(n) is used: phantoms (S007) disappear along each y by compactness alone, with no computable rate.

**Lemma 2 (excess bound).** For every t,

  Σ_{k∈K₀} γ(σ,k,t) ≤ Ψ(σ,t) + 2^{|σ|} E_λ[X_t·(f(y↾t)−1)^+],

and

  limsup_{t→∞} 2^{|σ|} E_λ[X_t·(f(y↾t)−1)^+] ≤ 2^{|σ|} E_λ[(2 + B_∞)·(f_∞−1)^+].

*Proof.* Termwise, f ≤ c^σ + (f−1)^+, because f ≥ 1 forces c^σ = 1. Multiply by 2^{|σ|}2^{−t}d(w) and sum over w ∈ 2^t; this gives the first line.

For the second line, write e_t := (f(y↾t)−1)^+ ≤ N and e_∞ := (f_∞−1)^+. Then X_t = A_t + B_t ≤ 2 + B_∞, so E[X_t e_t] ≤ 2E[e_t] + E[B_∞ e_t]. By Lemma 1, e_t → e_∞ pointwise and is eventually constant. Also e_t ≤ N and B_∞ e_t ≤ N B_∞, which is integrable. Dominated convergence gives 2E[e_t] → 2E[e_∞] and E[B_∞ e_t] → E[B_∞ e_∞]. ∎

**Definition 3 (dispersible class).** A class 𝒱 of width-two strategies is *dispersible* if the following holds for every finite set F ⊆ 𝒱 of valid strategies (with savings banks B^e), every partial assignment σ, every a, N ∈ ℕ and every ε > 0. There is K₀ ⊆ [a,∞)∖dom σ with |K₀| = N and

  Σ_{e∈F} E_λ[(2 + B^e_∞)·(f^e_∞ − 1)^+] < ε.

Since (f_∞−1)^+ ≤ N·1(|G⁻¹(y)| = 2, |K₀∩Δ_G(y)| ≥ 2), a sufficient σ-free condition is

  Σ_{e∈F} μ_e{y : |G_e⁻¹(y)| = 2, |K₀∩Δ_{G_e}(y)| ≥ 2} < ε/N,  where μ_e := (2+B^e_∞)·λ.

Each μ_e is a finite measure (total mass ≤ 3) absolutely continuous with respect to λ.

**Lemma 3 (FD₂ and DZ₂ are dispersible).** Every class of width-two strategies whose maps lie in DZ₂ is dispersible. In particular every class with maps in FD₂ is dispersible. For FD₂ the set K₀ may moreover be taken inside any prescribed infinite set P ⊆ ℕ.

*Proof (FD₂).* For a < b let D^e_{a,b} := {y : |G_e⁻¹(y)| = 2, Δ_{G_e}(y)∩[0,a] ≠ ∅, Δ_{G_e}(y)∩[b,∞) ≠ ∅}. For fixed a, the sets D^e_{a,b} decrease in b. Their intersection lies in {Δ infinite}, which is λ-null and hence μ_e-null. Since μ_e is finite, μ_e(D^e_{a,b}) → 0 as b → ∞.

Choose K₀ = {k₁ < … < k_N} ⊆ P∩[a,∞)∖dom σ greedily, with Σ_{e∈F} μ_e(D^e_{k_r,k_{r+1}}) < ε/N² at each step. If |K₀∩Δ(y)| ≥ 2, say k_r, k_{r′} ∈ Δ(y) with r < r′, then y ∈ D_{k_r,k_{r+1}}. Summing over r < N gives the σ-free condition.

*Proof (DZ₂).* Let a′ > max(a, max dom σ). Choose K₀ uniformly at random among the N-subsets of [a′, a′+R). For a fixed double output y, put s := |Δ(y)∩[a′,a′+R)|. Then

  P(|K₀∩Δ(y)| ≥ 2) ≤ C(N,2)·(s/R)·((s−1)/(R−1)) ≤ C(N,2)·(|Δ(y)∩[0,a′+R)|/R)²,

which tends to 0 as R → ∞ for μ_e-a.e. double y. The probability is at most 1 and μ_e is finite, so dominated convergence gives E_{μ_e}[P(|K₀∩Δ| ≥ 2)] → 0. Sum over the finitely many e ∈ F. For large R the average over K₀ is < ε/N, so some K₀ attains it. ∎

*Remark.* For DZ₂ the candidate pool must have positive density. The class-restricted pools C_ε of S083 have density zero, which is why Theorem 8 below is stated for FD₂.

## 3. The simultaneous survivor theorem

**Theorem 4 (dispersed survivor).** Let 𝒱 be a class of width-two strategies (G_e,d_e), uniformly partial computable in e, with an arithmetically defined set of valid indices. Suppose 𝒱 contains every strategy (id, d) with d a rational computable martingale, and 𝒱 is dispersible. Then there is z ∉ MLR such that no strategy of 𝒱 succeeds on z. In particular z ∈ CR. If 𝒱 contains (G,d) for every rational computable d whenever it contains G, then G(z) ∈ CR for every such G. The witness z is computable from a finite iterate of the jump.

*Proof.* Run the S082 §4 construction (guessed runs R(ε), weights w_e, potentials Φ and Γ) with exactly one change, in stage (b). Put ℓ_i := 2i+2, N_i := 3·2^{i+3}ℓ_i and ε_i := 2^{−(i+4)}/ℓ_i.

**Stage (b), one repetition.**
* Let a := 1 + max dom σ.
* Dovetail over pairs (K₀, t) with K₀ ⊆ [a,∞), |K₀| = N_i and t ≥ τ. Halt at the first pair satisfying the decidable inequality

  Σ_{k∈K₀} Γ(σ,k,t) ≤ Φ(σ,t) + ε_i.

* Put τ″ := t. Let k be the least element of K₀ minimizing Γ(σ,k,τ″), and b the least value minimizing Φ(σ_b,τ″).
* Set σ := σ_b and τ := τ″.

Steps (a) and (c) and the weights are as in S082.

**Halting on true runs.** Let F be the active valid strategies, with weights w_e. Apply Definition 3, with ε := ε_i/(2·2^{|σ|}·max_e w_e·|F|), to get K₀. By Lemma 2, weighted and summed over e ∈ F, limsup_t (Σ_{k∈K₀}Γ(σ,k,t) − Φ(σ,t)) < ε_i/2. So some t ≥ τ satisfies the inequality, and the dovetailed search halts. A run on a wrong guess may search forever; S082 already allows such runs to diverge.

**Invariant (S082 Proposition 4.1).** The chosen k has Γ(σ,k,τ″) ≤ (Φ(σ,τ″) + ε_i)/N_i < 3/N_i while Φ < 2. By Lemma 2.3, min_b Φ(σ_b,τ″) ≤ Φ(σ,τ″) + Γ(σ,k,τ″). By Lemma 2.1, Φ(σ,τ″) ≤ Φ(σ,τ). So the ℓ_i repetitions raise the carried bound by less than ℓ_i·3/N_i = 2^{−(i+3)}. This is the S082 bookkeeping verbatim, so Φ(σ^ε_i, τ^ε_i) < 2 − 2^{−i} on true runs.

**Remaining steps.**
* Each stage still fixes exactly ℓ_i new coordinates. So S082 Proposition 4.2 gives the ML test (V_i), and every z ∈ S := ⋂_i[σ*_i] is non-ML-random.
* S082 Proposition 4.3 (compactness, using only Lemmas 2.1, 2.2 and 2.4(ii) and the invariant) gives z ∈ S with X^e_t(z) ≤ 2 + 2/w_e for every valid e and every t.
* By S082 Lemma 2.4(iii), each d_e is bounded on G_e(z).
* Validity is arithmetical, so the guessed sequence ε* and the true runs are computable from a finite iterate of the jump; so is the leftmost point of the nonempty class S∖O. ∎

**Corollary 5.** R₂^{dz}∖MLR ≠ ∅, hence R₂^{fd}∖MLR ≠ ∅. Explicitly, some z ∈ CR∖MLR has G(z) ∈ CR for every G ∈ DZ₂, and so for every G ∈ FD₂.

*Proof.* Let 𝒱 be all strategies (G,d) with G ∈ DZ₂. The identity is in DZ₂: it has no double fibres. 𝒱 is dispersible by Lemma 3.

Validity is arithmetical. Totality and martingale totality are Π⁰₂. Fairness is Π⁰₁ given totality. The global two-fibre bound is "∀n ∃m W(n,m) ≤ 2" (S085 Theorem 1). For the density condition, fix a pair of distinct strings (u,u′). On the effectively closed set of outputs whose fibre meets both [u] and [u′], the two preimages are computable from y, being the unique elements of Π⁰₁(y) singletons. So the predicates "k ∈ Δ(y)", the density statement and the λ-null statement are arithmetical. Apply Theorem 4. ∎

**Corollary 6 (one computable frame).** For every computable fair homeomorphism J, some z ∈ CR∖MLR has G(z) ∈ CR for every G ∈ DZ₂^J.

*Proof.* Apply Theorem 4 to 𝒱_J := {(G∘J⁻¹, d) : G ∈ DZ₂^J} ∪ {(J⁻¹, d)} ∪ {(id, d)}, over all rational computable d. J⁻¹ is injective and fair, so it lies in DZ₂, and 𝒱_J is dispersible by Lemma 3. Theorem 4 gives w ∉ MLR. Put z := J⁻¹(w).
* z ∉ MLR, because J is a computable fair map and conserves MLR (THM-0035).
* z = J⁻¹(w) ∈ CR, since no (J⁻¹, d) succeeds on w.
* G(z) = (G∘J⁻¹)(w) ∈ CR for every G ∈ DZ₂^J. ∎

**Corollary 7 (excluded universality hypotheses; genuinely multi-observer).** Let 𝒢 ⊆ F₂ be any family, finite, countable or arbitrary. If 𝒢 ⊆ DZ₂^J for one computable fair homeomorphism J, then 𝒢 is not universal for CR∖MLR: a single z ∈ CR∖MLR survives every member of 𝒢. Instances:

(a) **J = id.** This covers every G ∈ FD₂, including non-scan maps, maps with S007 phantoms, and every one-hole scan F_T∘K of every computable finite-block recoding K (a fibre pair differs inside one block). It recovers S082 Theorem 5.1 and extends it from scans to arbitrary finite-difference ≤2-to-1 maps.

(b) **The graded frame.** Let f(i) := ⌊√i⌋ and J_f(z)_i := Σ_{l=0}^{min(f(i),i)} C(f(i),l)·z_{i−l} mod 2. J_f is lower unitriangular over F₂ on every prefix, so it is a computable fair homeomorphism with computable inverse. Then every one-hole scan of every K∘D′ʲ(z), for j ∈ ℕ and K a computable finite-block recoding, lies in FD₂^{J_f}.

*Proof of (b).* Let G = F_T∘K∘D′ʲ and fix an output with two preimages under G∘J_f⁻¹. In virtual coordinates the two preimages are v and v⊕e_q, where q is the final hold. Put s := K⁻¹(v)⊕K⁻¹(v⊕e_q); s is supported in the block of q. D′ and J_f are F₂-linear, so the raw difference is J_f D′^{−j}(s) = ⊕_{p∈s} J_f D′^{−j}(e_p).

D′ multiplies generating functions by (1+x), so D′^{−j}(e_p) has generating function x^p(1+x)^{−j}. J_f(u)_i = [x^i]((1+x)^{f(i)}U(x)), so J_f D′^{−j}(e_p)_i = [x^{i−p}](1+x)^{f(i)−j}.
* If f(i) ≥ j, this is a polynomial of degree f(i) − j. Its coefficient vanishes unless p ≤ i ≤ p + √i, which bounds i.
* If f(i) < j, then i < j².
So each J_f D′^{−j}(e_p) has finite support, and so does the difference. ∎

In particular, by (b) the S083 tail-coded observer T*∘D′, for every one-hole scan T*, and all its higher-order analogues T∘D′ʲ lie in one co-dispersible family together with all raw and block-recoded one-hole scans. That family has a common CR∖MLR survivor. S086 handled only families Q_i∘F factoring through one observation via CR-preserving output maps. The families of Corollary 7 have genuinely different source partitions: for example, raw one-hole scans T₁ and T₂ need not be factor-equivalent. So Corollary 7 is strictly beyond the S086 rank-one obstruction.

## 4. The E₀-breaking separation

**Theorem 8 (R₂ ⊊ R₂^{fd}).** There is z with:
(i) z ∉ MLR;
(ii) G(z) ∈ CR for every G ∈ FD₂, so z ∈ R₂^{fd} and z ∈ CR;
(iii) F_{T*}(D′(z)) ∉ CR, where T* is the S083 §3.2 tail-coded scan defined from the runs of this construction, and F_{T*}∘D′ ∈ F₂∖FD₂.
Hence z ∉ R₂, D′(z) ∉ OH, and R₂ ⊊ R₂^{fd}.

*Proof.* Run S083 §3 verbatim with the candidate step replaced by the Theorem 4 search, restricted to K₀ ⊆ C_{ε↾(i+1)}∩[a,∞). Each class C_ε is infinite and decidable, so Lemma 3 (FD₂, any infinite pool) gives halting on true runs. The invariant is that of Theorem 4.

S083 Lemma 3.1 holds: the new proof of the bound uses only that the chosen coordinates lie outside dom σ. S083 Lemma 3.2 (class separation) holds, because every coordinate fixed at stage s of R(ε′) still lies in C_{ε′↾(s+1)}, and stage s still depends only on ε′↾(s+1). T* simulates each run for a bounded number of steps, so runs that search forever never qualify. Lemma 3.3 (validity of T*) is unchanged.

Lemmas 3.4–3.6 and Proposition 3.7 then go through verbatim. They depend only on the r(q,m) = q+2m+4 qualification rule, the ⅛ fooling bound, |dom σ*_{m−1}| = m(m+1), and Φ < 2.

This yields z ∈ S∖W with bounded savings capital for every valid FD₂ strategy, which gives (i) and (ii). By S083 Theorem 3.8(iii), T* resolves infinitely often on D′(z), always correctly, which gives (iii).

F_{T*}∘D′ ∉ FD₂, because by S084 Corollary 4 almost every output has two preimages related by the tail complement J_q, so Δ = [q,∞). Finally R₂ ⊆ OH, and z ∉ R₂ since G(z) ∉ CR for this G ∈ F₂. ∎

**Proposition 9 (which homeomorphisms preserve R₂^{fd}).** Let H be a computable fair homeomorphism such that H⁻¹ maps E₀-related pairs to E₀-related pairs. Then H(R₂^{fd}) ⊆ R₂^{fd}. Examples are computable finite-block recodings and the prefix parity D′⁻¹ (whose inverse D′ preserves E₀, since D′(x⊕e_q) = D′(x)⊕e_q⊕e_{q+1}). By Theorem 8, R₂^{fd} is NOT closed under D′, whose inverse breaks E₀ (D′⁻¹(v⊕e_q) = D′⁻¹(v)⊕1_{[q,∞)}).

*Proof.* For G ∈ FD₂, G∘H ∈ F₂, and its fibres are the H⁻¹-images of the fibres of G. These are E₀-related over the same co-null set of outputs, so G∘H ∈ FD₂. If z ∈ R₂^{fd} then G(H(z)) = (G∘H)(z) ∈ CR. Also H(z) ∈ CR, because computable fair homeomorphisms preserve CR (THM-0038). ∎

**Lemma 10 (finite differences force symmetric sheet weights).** If G ∈ FD₂^J for some computable fair homeomorphism J, then almost every double fibre of G carries conditional weights ½, ½.

*Proof.* In the J-frame, the partner map on the double locus is ψ(x) = x⊕1_{Δ(G(x))}. Up to a null set, ψ is a countable union of restrictions of finite coordinate flips, each λ-preserving, and ψ is injective. So ψ preserves λ, and G∘ψ = G. The disintegration of λ over G is therefore ψ-invariant, and each two-point fibre gets equal weights. J is λ-preserving, so it transports the conditional weights. ∎

So any G ∈ F₂ whose double locus has positive measure with asymmetric conditional weights (S004 exhibits zero-weight sheets only on a null double locus) lies outside every FD₂^J. The **frame-straightening question** is recorded, not settled: is every finite family in F₂ contained in a single FD₂^J or DZ₂^J? A positive answer would rule out every finite universal family. Lemma 10 is one possible obstruction. F₂ itself is not contained in any single DZ₂^J, because it is closed under precomposition with computable fair homeomorphisms. Let T₀ be the raw one-hole scan that holds coordinate 0 forever and reads 1, 2, … in order, and put G := F_{T₀}∘D′∘J ∈ F₂. Then G∘J⁻¹ = F_{T₀}∘D′, and every output of it has the fibre {z, z̄}, with difference set ℕ.

## 5. Updated landscape and the exact frontier

  MLR ⊊ R₂^{dz} ⊆ R₂^{fd} ⊆ OH^blk ⊆ OH^lin3 ⊆ OH,  R₂ ⊊ R₂^{fd},  R₂ ⊆ OH^iso ∩ ⋂_J R₂^{fd,J},

where R₂^{fd,J} := {z ∈ CR : G(z) ∈ CR for all G ∈ FD₂^J}. All earlier frozen relations stand.

* **Route A, R₂ = MLR.** A universal witness family must, in every computable frame J, contain a member outside DZ₂^J: a map with positive-measure double fibres whose difference sets have positive upper density. Tail codes are the basic example. Two such maps that become co-dispersible in one frame are still excluded, for example T*∘D′ together with raw scans. A finite universal pair remains sufficient but not known necessary.
* **Route B, MLR ⊊ R₂.** A survivor must defeat every non-dispersible ambiguity in every frame simultaneously. That includes every frame-transported T*∘D′∘J, with the whole S084 error stream computably random and of mistake frequency ½. Theorem 8 shows that the dispersed-survivor method alone does not do this.
* **Decisive question.** R₂ versus MLR is now located exactly at **E₀-breaking (non-dispersible) binary ambiguity**. It remains OPEN, as do R₂ versus OH^iso, OH^iso versus MLR, R_fin versus R₂, U(H), X ∈ OH, fixed-S preservation, block-H invariance, TKLR∖MLR and QST-0001.

## 6. Routes attempted on the overriding target (not closed)

**6.1 Route A: coded holes reading an ML test (analysis).** A tail-coded observer holding v_q sees the source only up to the involution φ_q(x) = x⊕1_{[q,∞)}. Reading a universal ML test U, it can bet on whichever candidate's separating cylinder is enumerated first.
* φ_q is a computable fair involution, so φ_q(x) is non-MLR whenever x is, and both candidates eventually enter every U_c.
* The bet is therefore a race of enumeration times. The events "x wins" and "x loses" are both effectively open.
* For involution families whose Cayley graph is bipartite, the enumeration order can make half of every orbit lose every race. Non-bipartite families, such as {φ_q, φ_{q′}, φ_qφ_{q′}}, cap the all-loss fraction of an orbit at ¼, but force no computably detectable bias.
* By S084, a survivor must lose a computably random half of the races. Nothing found forces this impossible.
* Changing the pairing adaptively does not help: every computable partner of x is again non-MLR.
No universal pair was obtained.

**6.2 Route B: the counting potential (analysis; obstruction recorded).** For G ∈ F₂ with tracked precision N, let Ψ̃_N be the S082 Proposition 6.2 counting potential. The facts below are verified directly from the definitions; items 2–3 rely on the same weight convention as Lemma 10.
1. Ψ̃_N is exact under fixings inside the tracked set. This is S082 Proposition 6.2(ii).
2. In the t→∞ limit, with symmetric sheet weights, A ≤ Ψ̃_N ≤ 2A, where A(σ) := 2^{|σ|}∫_{[σ]}X_∞ dλ is the exact fixing martingale.
3. Ψ̃_N = A + E, where the overcount E consists of tracked unsplit pairs and split pairs, and 0 ≤ E ≤ A.
4. Ψ̃_N(σ,t) is non-increasing in t. So "Ψ̃_{N,∞}(σ) < θ" is Σ⁰₁, and the choice of a good fixing can be **searched without any modulus**. This removes S082 §6.3 obstacle (a), and Theorem 4 uses exactly this search.

Obstacle (b) is genuine for minimisation rules. A self-referential observer can inflate every unsearched child with tracked overcount (free for it, since ambiguity costs no capital) and place un-overcounted capital (V := A − E) on the child the search will select. Along a minimum-Ψ̃ path one then gets V_c + 2E_c ≤ V + 2E with V_c as large as V + 2E. Tracking converts V into E, so A can grow by a factor (1+θ) per stage when a fraction θ is tracked. This is a heuristic adversary schema, not a realized observer. It explains why the counting route stalls exactly at non-dispersible ambiguity, and why Lemma 2 needs dispersibility.

**6.3 Diagnostic: survivors cannot be random for a computable measure.** If x ∈ CR is ν-MLR for some computable measure ν, then x ∈ MLR.
* L(σ) := 2^{|σ|}ν[σ] is a computable λ-martingale, so x ∈ CR bounds it along x: ν[x↾n] ≤ C·2^{−n}.
* Levin–Schnorr for ν then gives K(x↾n) ≥ n − log C − O(1), so x ∈ MLR.
This is a standard-type argument, recorded only to exclude "random point of a computable measure" constructions of z ∈ R₂∖MLR. No novelty is claimed.

**6.4 Not attempted, as instructed.** Escrow, hazards, residues, unit columns, record-only z₀, multi-hole variants, and any change to Y/M/H/X.

## 7. Finite audit

`phase4/P4-S087_DISPERSION_AUDIT.py` (exact rationals, < 1 s, 8,261 checks) covers four maps on 9-bit inputs: (a) a raw one-hole scan, (b) the same scan with a non-causal output pair-swap (non-scan cells), (c) a scan of the committed block matrix A, and (d) a scan of D′. It checks:
1. The termwise inequality Σγ ≤ Ψ + excess, for all four maps.
2. Zero excess and Σγ ≤ Ψ for (a)–(c), with block-separated candidates.
3. Explicit violations Σγ > Ψ for the tail code (d).
4. Monotonicity of the split count f along output branches.
5. That the graded frame J_f turns D′ʲ tail differences (j = 1, 2) into finitely supported ones.
It prints `ALL P4-S087 AUDITS PASS`. The audit covers finite truncations only; every infinitary claim rests on the written proofs.

## 8. Disposition

**Proved.**
* Lemmas 1–3.
* **Theorem 4**: dispersed survivor, a genuine ∃z∀G over an infinite non-rank-one class.
* Corollaries 5–7: R₂^{dz}∖MLR ≠ ∅; the frame version; the excluded co-dispersible universality hypotheses, including the graded frame containing every T∘K∘D′ʲ.
* **Theorem 8**: R₂ ⊊ R₂^{fd}, with a tail-coded destroyer.
* Proposition 9 and Lemma 10.

**Not proved.**
* R₂ = MLR or MLR ⊊ R₂.
* A universal width-two pair or family.
* A survivor for all of F₂.
* The frame-straightening question.
* No quantifier swap of S086 is claimed.

**Frozen.**
* All P4-S001–S086 results and the original Y/M/H/X.
* Literature at recorded access levels: no source fetched or upgraded; SRC-0072 is used for calibration vocabulary only.
* PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged.
* Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED.

No novelty, openness, priority, publication or outreach claim is made. Owner/external blocker: NONE.

**Next: P4-S088.** Attack the E₀-breaking frontier directly. Either settle frame straightening for finite families, which would exclude every finite universal family, or build a survivor against a family that is not co-dispersible in any frame, the minimal case being one closed under all computable fair homeomorphisms (OH^iso∖MLR, or its two-map core). R₂ versus MLR remains the decisive target.
