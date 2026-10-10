# P4-S088 — Asymmetric double loci, frame-free coset dispersal, and a survivor for all countable-coset width-two observers

Date: 2026-10-10. Scope: Phase 4 Mathematics ONLY; selected CAND-01.
Incoming independently pinned live main: `c820588d2936d1a6fe28cee84fca86699e65610a`, exactly the P4-S087 atomic close commit (parent `7435c93ec127f4fc2527a883917fb90784db4464` = P4-S086 outgoing, as recorded in the P4-S087 close).

**Disposition: R₂ versus MLR is NOT decided.** The session settles the first sub-question of (A), shows that frame straightening is the wrong invariant, and proves a (B)-type survivor theorem for a family that is not co-dispersible in any single computable frame and contains every affinely frame-transported tail code.

* **Theorem A (asymmetric double loci).** F₂ admits positive-measure asymmetric double loci. An explicit total computable fair map G_asym with all fibres of size ≤ 2 has, on a closed output set A with λ(A) = ∏_{k≥2}(1 − 2^{−k}) ≈ 0.5776, exactly two preimages over every y ∈ A, with conditional weights exactly ¼ and ¾.
  * Hence G_asym ∉ FD₂^J for every computable fair homeomorphism J (P4-S087 Lemma 10), so **frame straightening for FD₂ fails already for a single map**.
  * G_asym is nevertheless harmless: it has a computable clopen two-sheet split, so it preserves CR on every input (P4-S003 Theorem 3).
  * A diluted copy lies in DZ₂ with the same asymmetric weights, so Lemma 10 is specific to finite differences, and asymmetry is no obstruction to the P4-S087 survivor.
* **Theorem B (translation pairs).** For every computable fair homeomorphism J there is a computable c such that the translation-pair map G_c (fibres {x, x⊕c}) lies outside DZ₂^J. Every G_c is a one-hole scan after a linear frame, and every G_c preserves CR. Every finite set of translation pairs is straightened by one linear frame.
  * So co-dispersibility in one frame is neither necessary for survival nor the right invariant.
* **Theorem C (countable-coset survivor).** Let CDZ₂ be the class of G ∈ F₂ whose double-fibre difference vectors x⊕x′ fall, almost surely, into countably many cosets of the density-zero subgroup 𝒵. Then ONE z ∈ CR∖MLR has G(z) ∈ CR for EVERY G ∈ CDZ₂.
  * CDZ₂ contains DZ₂ ⊇ FD₂, every map in FD₂^K for every computable affine fair homeomorphism K, every one-hole scan of every K(z) for affine K, and every tail-coded F_T∘D′∘J for affine J. In particular it contains every such T∘D′ (S083's T* among them) and the S087 Theorem 8 destroyer.
  * By Theorem B, CDZ₂ is not contained in any single computable frame's DZ₂^J.
  * The mechanism is **frame-free**. The construction fixes fresh linear parity constraints that annihilate the dominant difference cosets of all active observers simultaneously, chosen anew at every step. It never fixes coordinates of a single frame.
* **Corollaries.**
  * R₂^{cdz}∖MLR ≠ ∅ and R₂^{cdz} ⊊ R₂^{fd}.
  * OH^{aff}∖MLR ≠ ∅, where OH^{aff} is robustness of OH under all computable affine fair homeomorphisms, and OH^{aff} ⊊ OH^{blk}.
  * No family contained in CDZ₂, or in CDZ₂^J for a single J, is universal for CR∖MLR.
* **Frontier (§6).** R₂ versus MLR now sits at width-two ambiguity whose difference vectors are **uncountable modulo 𝒵 in every frame**: nonlinear E₀-breaking ambiguity. An explicit pair of one-hole scans after two nonlinear causal frames shows the precise limit of the linear mechanism. Each member is dispersible in its own frame. No fresh parity is simultaneously invariant for both, and neither natural frame co-disperses the pair. Whether some frame or some nonlinear halving family co-disperses it is the sharpened open form of (A).

## 0. Authority, uniqueness and frozen objects

* **Pinned main.** `git ls-remote origin refs/heads/main` returned `c820588…`. Its commit metadata gives parent `7435c93…`, the P4-S086 outgoing SHA. The P4-S087 close record states that its outgoing SHA is the hash of its own atomic commit, which is `c820588…`. Reconciled.
* **Uniqueness.** `phase4/` contained no P4-S088 file. Every repository mention of P4-S088 names it only as the next session.
* **Prompt.** The incoming prompt is identical in substance to `authoritative/NEXT_SESSION_PROMPT.md`.
* **Reviewed.**
  * Cumulative P4-S001–S087 records. In detail: S003 (Theorem 3, the clopen two-sheet split), S004 (Lemma 3, F_thin), S007, S008, S011–S012 and S032–S033.
  * S081–S087: S082 §§2–6, S083 §§2–4, S084, S085 Theorem 1, S086 Theorems 1–3, and the S087 mathematics, validation, close and audit.
  * CAND-01, the Gate-3 PASS and both Phase-4 pivots.
  * SRC-0015, SRC-0019, SRC-0060 and SRC-0069–SRC-0072, at their RECORDED access levels. No source was fetched and no access level changed.
* **Frozen.**
  * MLR = R_tot ⊆ R_fin ⊆ R_k ⊆ R₂ ⊆ OH^iso ⊊ OH^blk ⊆ OH^lin3 ⊆ OH = OH_h = R_k^scan ⊊ CR (k ≥ 2); R₂ ⊊ OH; MLR ⊊ OH; KLR ⊆ TKLR ⊆ OH.
  * R_tot = MLR remains a programme deduction from SRC-0071's inspected preprint.
  * S084's predictable-error theorem, ML-null infinite-resolution locus and balanced a.e. two-sheet destroyer.
  * S085's c(n) criterion (a representation only). S086's ∀F∃x pullback survivor and rank-one/common-factor no-go.
  * All of P4-S087, including Lemma 2 (an excess bound with no width modulus and with the time searched), Theorem 4, Corollaries 5–7, Theorem 8, Proposition 9 and Lemma 10.
  * The original computably random Y, the unchanged globally use-clipped syntactically self-avoiding wtt autoreduction M, the repeated three-bit H with A = [101;110;111], and X = H⁻¹(Y). Nothing below uses or alters them. S057 is not invoked.
  * There are no escrow, hazard, residue, unit-column, record-only z₀ or multi-hole detours.
  * R₂ = OH^iso, U(H), X ∈ OH and fixed-S preservation are kept separate and untouched.

## 1. Conventions and new definitions

* F₂, FD₂, DZ₂, FD₂^J, DZ₂^J, R₂^{fd}, R₂^{dz}, strategies (G,d), the savings transform d = A + B (S082 Lemma 2.4, with 0 ≤ A < 2, B non-decreasing and E_λ[B_∞] ≤ 1), and E₀ are as in P4-S087 §1.
* For G ∈ F₂ and an output y with G⁻¹(y) = {x, x′}, x ≠ x′, the **difference vector** is Δ_G(y) := x ⊕ x′ ∈ 2^ω. It is symmetric in the pair, and Δ_G(y) is the indicator of the P4-S087 difference set.
* 𝒵 := {s ∈ 2^ω : lim_R |{i < R : s_i = 1}|/R = 0} is the **density-zero subgroup** of (2^ω, ⊕). The finitely supported vectors form a subgroup of 𝒵.
* **CDZ₂** is the class of G ∈ F₂ for which there is a countable set Q ⊆ 2^ω with Δ_G(y) ∈ Q ⊕ 𝒵 for λ-almost every output y having two preimages. That is, the difference vectors occupy essentially countably many 𝒵-cosets. **CD₂** is the subclass in which Δ_G(y) ∈ Q almost surely.
* For a computable fair homeomorphism J, CDZ₂^J := {G ∈ F₂ : G∘J⁻¹ ∈ CDZ₂}. Then R₂^{cdz} := {z ∈ CR : G(z) ∈ CR for every G ∈ CDZ₂}.
* A **computable affine fair homeomorphism** is K(x) = Mx ⊕ c. Here c is a computable vector. M is an F₂-linear bijection of 2^ω given by a computable matrix whose rows are finitely supported, with inverse of the same kind. Such a K is a computable homeomorphism, since each output coordinate is a finite parity, and it is fair by the remark below. OH^{aff} := {z : K(z) ∈ OH for every computable affine fair homeomorphism K}.
* **Linear functionals.** Let Φ be the F₂-space of finitely supported vectors. For c ∈ Φ and x ∈ 2^ω, ⟨c,x⟩ := ⊕_{i∈supp c} x_i. If c₁,…,c_n ∈ Φ are linearly independent, the vector (⟨c_j,x⟩)_{j≤n} is uniform on F₂ⁿ under λ. So an **affine constraint set** P := {x : ⟨c_j,x⟩ = b_j, j ≤ n} is clopen with λ(P) = 2^{−n}.

*Remark (fairness of linear homeomorphisms).* If M and M⁻¹ are continuous and F₂-linear, M is a group automorphism of the compact group 2^ω. Haar measure is unique, and λ is Haar measure, so M preserves λ. Translation by c preserves λ as well.

*Inclusions.*
* FD₂ ⊆ DZ₂ ⊆ CDZ₂, since 𝒵 is one coset.
* FD₂^K ⊆ CDZ₂ for every computable affine fair homeomorphism K(x) = Mx ⊕ c. The preimages of G are K⁻¹ of the preimages of G∘K⁻¹, so Δ_G = M⁻¹(u ⊕ u′), where u ⊕ u′ is finitely supported almost surely, and there are countably many finitely supported vectors.
* Every one-hole scan F_T∘K, for K affine, lies in FD₂^K and hence in CDZ₂.
* Every F_T∘K for K a computable finite-block recoding lies in FD₂, since a pair differs inside one block.
* Hence R₂ ⊆ R₂^{cdz} ⊆ R₂^{dz} ⊆ R₂^{fd}. Moreover R₂^{cdz} ⊆ OH^{aff} ∩ OH^{blk}: K(z) ∈ CR because the injective map K lies in CDZ₂, and F_T(K(z)) ∈ CR because F_T∘K ∈ CDZ₂.

## 2. Theorem A: positive-measure asymmetric double loci exist in F₂

**Blocks and the locus.** Put ℓ_j := j + 2, a₀ := 0 and a_{j+1} := a_j + ℓ_j for j ≥ 0, and let W_j := [a_j, a_{j+1}) be the j-th output block.

* A *block value* at j is a string in {0,1}^{ℓ_j}. The value 1^{ℓ_j} is **forbidden**; the other 2^{ℓ_j} − 1 values are **allowed**.
* A := {y : y↾W_j ≠ 1^{ℓ_j} for every j}. This is a closed product set with λ(A) = ∏_{j≥0}(1 − 2^{−(j+2)}) = ∏_{k≥2}(1 − 2^{−k}) ≈ 0.57758.
* An *A-prefix of level j* is a string w of length a_j all of whose j blocks are allowed.
* For such w, put v := w1^{ℓ_j} and D_v := [v]. The complement of A is the disjoint union of the cylinders D_v, indexed by the first forbidden block.

**Side 0 (the cylinder [00]).** Define G(00z) := z if z ∈ A. If z ∈ D_v, write z = vx and define G(00z) := v00x.

**Side 1 (the clopen set [1] ∪ [01]): containers.** Each A-prefix w of level j receives a **container** Π_w = (B_w, S_w): two disjoint cylinders with |B_w| = a_j + 1 and |S_w| = a_j + 2. Put Π_∅ := ([1], [01]).

*Splitting Π_w at block j.* Put N := 2^{ℓ_j}. A **unit** is a subcylinder of length a_{j+1} + 2, and a **slot** is a subcylinder of length a_{j+1} + 1, which is a sibling pair of units. B_w contains N slots (2N units), and S_w contains N/2 slots (N units). A *child* is a pair (slot, unit).

* **Case N ≡ 1 (mod 3).** Put t := (2N−2)/3 and s := (N−1)/3.
  * Pack t children inside B_w, using t whole slots and t units cut from t/2 further slots (t is even). This leaves exactly one slot of B_w unused.
  * Pack s children inside S_w (s is odd), using s whole slots and (s+1)/2 cut slots. This leaves exactly one unit of S_w unused.
  * The remaining **straddling** child is (that slot of B_w, that unit of S_w).
* **Case N ≡ 2 (mod 3).** Put t := (2N−1)/3 (odd) and s := (N−2)/3 (even). The same packing leaves one unit of B_w and one slot of S_w. The straddling child is (that slot of S_w, that unit of B_w).

In both cases t + s + 1 = N, and the N children partition B_w ∪ S_w. The N − 1 **collapsing** children (the ones inside B_w or inside S_w) are assigned, in a fixed computable order, to the allowed block values u, giving containers Π_{wu}. The straddling child (P_v, Q_v), with P_v the slot and Q_v the unit, is assigned to the forbidden value; let v := w1^{ℓ_j}.

**Side 1: the map.**
* For x in the slot P_v, written x = P_v x′, put G(x) := v1x′.
* For x in the unit Q_v, written x = Q_v x′, put G(x) := v01x′.
* If x lies in collapsing children at every level, let w₀ ⊏ w₁ ⊏ … be the A-prefixes so obtained, and put G(x) := ⋃_j w_j ∈ A.

Write h₁(y) for the unique point of ⋂_j (B_{y↾a_j} ∪ S_{y↾a_j}), for y ∈ A.

**Theorem A.** G_asym := G is a total computable λ-preserving map with all fibres of size ≤ 2. Every y ∈ A has exactly the two preimages 00y and h₁(y), and every y ∉ A has exactly one. For every Borel V ⊆ A,

  λ(G⁻¹(V) ∩ [00]) = ¼λ(V)  and  λ(G⁻¹(V) ∖ [00]) = ¾λ(V).

So on the positive-measure double locus A the conditional sheet weights are exactly ¼ and ¾.

*Proof.*
* **Totality, computability, continuity.**
  * On side 0, each output bit needs only finitely many input bits: G copies z until the first forbidden block is complete, and then outputs v00 followed by the rest.
  * On side 1, membership of x in the finitely many children at level j is decidable from a finite prefix. The straddling case outputs v then 1 or 01 and copies the rest. The collapsing case outputs the next block value.
* **The collapsing containers shrink.** A collapsing child of Π_w lies inside B_w or inside S_w, so both of its cylinders extend a common prefix of length ≥ |B_w| = a_j + 1.
  * Along y ∈ A the containers are nested, nonempty and compact, with diameters ≤ 2^{−(a_j+1)} → 0. So ⋂_j(B_{y↾a_j} ∪ S_{y↾a_j}) is a single point h₁(y).
  * Every side-1 input either lies in a straddling child at some level or lies in collapsing children at every level, so G is defined everywhere.
* **Fibres.**
  * *y ∈ A.* Side 0 contributes exactly 00y: if G(00z) ∈ A then z ∈ A, because z ∈ D_v gives an output in D_v. Side 1 contributes exactly h₁(y), since an input mapping into A never lies in a straddling child.
  * *y ∈ [v00x].* The only preimage is 00vx. Side 1 never outputs v00.
  * *y ∈ [v1x] ∪ [v01x].* The only preimage is P_v x or Q_v x respectively. Side 0 maps [00v] onto [v00] only.
  * So all fibres have size ≤ 2, and the double locus is exactly A.
* **Fairness.** It suffices to check λ(G⁻¹[w]) = 2^{−|w|} for every output string w.
  * For an A-prefix w of level j, G⁻¹[w] = [00w] ⊔ B_w ⊔ S_w. Its measure is 2^{−a_j}(¼ + ½ + ¼) = 2^{−a_j}.
  * A string strictly inside a block is a finite disjoint union of block completions, and the measures add.
  * Inside D_v: G⁻¹[v00x′] = [00vx′], G⁻¹[v1x′] = [P_v x′] and G⁻¹[v01x′] = [Q_v x′]. These have the right measures because |P_v| = a_{j+1} + 1 = |v| + 1 and |Q_v| = |v| + 2.
  * Cylinders generate the Borel σ-algebra, so G_*λ = λ.
* **Weights.** For Borel V ⊆ A, G⁻¹(V) ∩ [00] = 00V has measure ¼λ(V). By fairness λ(G⁻¹(V)) = λ(V), so the rest has measure ¾λ(V). ∎

**Corollary A1 (FD frame straightening fails for one map).** G_asym ∉ FD₂^J for every computable fair homeomorphism J.

*Proof.* P4-S087 Lemma 10 says FD₂^J maps have conditional weights ½, ½ on almost every double fibre. G_asym has weights ¼, ¾ on A, and λ(A) > 0. ∎

**Corollary A2 (asymmetry is harmless).** G_asym(x) ∈ CR for every x ∈ CR.

*Proof.* [00] and its complement form a computable clopen partition, and G_asym is injective on each piece by the fibre analysis. Apply P4-S003 Theorem 3. ∎

**Corollary A3 (dilution: DZ₂ admits asymmetric weights).** Let P ⊆ ℕ be decidable, infinite, co-infinite and of density zero (for example the squares). Define

  G_dil(x) := the sequence carrying x↾(ℕ∖P) on the positions ℕ∖P and G_asym(x↾P) on the positions P,

with all restrictions read through increasing enumerations. Then:
* G_dil ∈ F₂, because it is a product of the identity and G_asym on independent coordinate sets;
* its double locus has measure λ(A) > 0, with weights ¼, ¾;
* every difference vector is supported in P, so G_dil ∈ DZ₂.

So Lemma 10 is specific to finite differences. Asymmetric sheets do not obstruct the P4-S087 survivor, which survives G_dil by P4-S087 Corollary 5. ∎

*Remarks.*
* The construction works with clopen containers only because ¼ and ¾ are dyadic and the container measures (¾)·2^{−a_j} are dyadic. Non-dyadic constant weights such as ⅓ need non-clopen bookkeeping and are not claimed.
* Whether G_asym ∈ DZ₂^J for some J is not decided. It is not needed below.

## 3. Theorem B: translation pairs and the limits of frame straightening

For c ∈ 2^ω with c₀ = 1, put:
* K_c(x) := x ⊕ x₀·(c ⊕ e₀), so that (K_c x)₀ = x₀ and (K_c x)_i = x_i ⊕ x₀c_i for i ≥ 1;
* T₀ := the one-hole scan that holds coordinate 0 forever and reads 1, 2, 3, … in order, so F_{T₀}(u) = u₁u₂…;
* G_c := F_{T₀}∘K_c, so G_c(x) = (x_i ⊕ x₀c_i)_{i≥1}.

**Lemma B0.** If c is computable with c₀ = 1, then:
* K_c is a computable linear involution and a fair homeomorphism;
* every fibre of G_c is exactly {x, x⊕c}, so Δ_{G_c} ≡ c, G_c ∈ FD₂^{K_c} and G_c ∈ CD₂ ⊆ CDZ₂;
* G_c(x) ∈ CR for every x ∈ CR, since G_c(x) is x₁x₂… or its translate by the computable vector c₁c₂….

*Proof.* (c ⊕ e₀)₀ = 0, so K_c∘K_c = id, and K_c is linear and continuous. The preimages of y are (0,y) and (1, y ⊕ c_{≥1}), whose sum is c. Then G_c∘K_c⁻¹ = F_{T₀}, whose fibres differ only at coordinate 0. Computable translations and the shift preserve CR. ∎

**Theorem B.**
(i) For every computable fair homeomorphism J there is a computable c with c₀ = 1 and G_c ∉ DZ₂^J. More precisely, there is a ⊕c-invariant set X_c with λ(X_c) ≥ 1/7 such that every x ∈ X_c has upper density ≥ ⅛ of {i : J(x)_i ≠ J(x⊕c)_i}.
(ii) For every finite set c¹, …, c^r of computable vectors there is one computable linear fair homeomorphism J that maps each c^j to a finitely supported vector. In particular G_{c¹}, …, G_{c^r} ∈ FD₂^J.
(iii) Hence the countable family 𝒯 := {G_c : c computable, c₀ = 1} ⊆ CDZ₂ is not contained in DZ₂^J for any single computable fair homeomorphism J. Every finite subfamily of 𝒯 is contained in a single FD₂^J. And every member of 𝒯 preserves CR.

*Proof of (i).* Let m(n) be a computable modulus with J(x)↾n determined by x↾m(n). Then m(n) ≥ n, because J(x)↾n is uniform on 2ⁿ. Put D_n(x,c) := |{i < n : J(x)_i ≠ J(x⊕c)_i}|/n. Write h for the binary entropy and h⁻¹ : [0,1] → [0,½] for its inverse on [0,½]; h is concave and increasing on [0,½], so h⁻¹ is convex and increasing.

*Claim.* Let ρ be a string of length k with ρ₀ = 1, let n ≥ k with m(n) ≥ k, and let r be uniform on {0,1}^{m(n)−k}, independent of x. Then

  E_r E_x D_n(x, ρr) ≥ h⁻¹(1 − k/n).

Here c ⊒ ρr is arbitrary beyond m(n), which does not affect D_n.

*Proof of the claim.*
* Put L := x↾k. The pair (x, x⊕c) has low parts L and L⊕ρ. On [k, m(n)) the high parts are x and x⊕r, which are independent and uniform given L.
* For i < n let p_{i,ℓ} := P(J(x)_i = 1 | L = ℓ). Given L, the bits J(x)_i and J(x⊕c)_i are independent, with parameters p_{i,L} and p_{i,L⊕ρ}.
* So P(J(x)_i ≠ J(x⊕c)_i) = E_L[p_{i,L}(1−p_{i,L⊕ρ}) + (1−p_{i,L})p_{i,L⊕ρ}] ≥ E_L[min(p_{i,L}, 1−p_{i,L})]. For fixed p the expression is affine in p′ and lies between p and 1 − p.
* min(p, 1−p) = h⁻¹(h(p)), so by Jensen, E_L[min(p_{i,L}, 1−p_{i,L})] ≥ h⁻¹(H(J(x)_i | L)).
* J is fair, so J(x)↾n is uniform. Hence Σ_{i<n} H(J(x)_i | L) ≥ H(J(x)↾n | L) ≥ n − k.
* A second application of Jensen gives (1/n)Σ_i h⁻¹(H(J(x)_i | L)) ≥ h⁻¹(1 − k/n). ∎

*Construction of c.* Start with ρ₀ := "1". Given ρ_s of length k_s:
* choose n_s > n_{s−1} with h⁻¹(1 − k_s/n_s) ≥ ¼ (it suffices that k_s/n_s ≤ 0.18);
* by the claim, some r ∈ {0,1}^{m(n_s)−k_s} has E_x D_{n_s}(x, ρ_s r) ≥ ¼, and this exact rational is computable, so search for such an r;
* put ρ_{s+1} := ρ_s r.

Then c := ⋃_s ρ_s is computable, and E_x D_{n_s}(x,c) ≥ ¼ for every s.
* Since D ≤ 1, λ{x : D_{n_s}(x,c) ≥ ⅛} ≥ 1/7 for every s.
* So X_c := limsup_s {D_{n_s} ≥ ⅛} has λ(X_c) ≥ 1/7, and each x ∈ X_c has upper density ≥ ⅛ of differences.
* D_n(x⊕c, c) = D_n(x, c), so X_c is ⊕c-invariant. Hence X_c = G_c⁻¹(G_c(X_c)), and λ(G_c(X_c)) = λ(X_c) > 0.
* The fibres of G_c∘J⁻¹ are {J(x), J(x⊕c)}. On a positive-measure set of outputs their difference sets do not have density zero, so G_c ∉ DZ₂^J. ∎

*Proof of (ii).*
* Let V := span{c^j}. Choose a reduced echelon basis b¹, …, b^s of V with pivots p₁ < … < p_s, where p_j is the least index of b^j. The vectors are computable, and the finite linear algebra is decidable on long enough prefixes. "Reduced" means (b^j)_{p_l} = 0 for l ≠ j.
* Let T_j(x) := x ⊕ x_{p_j}·(b^j ⊕ e_{p_j}). The vector b^j ⊕ e_{p_j} is supported in (p_j, ∞), so T_j is a computable causal linear involution, hence a fair homeomorphism.
* T_j b^j = e_{p_j}. For l ≠ j, T_j fixes b^l and e_{p_l}, because (b^l)_{p_j} = 0.
* So J := T_s∘…∘T₁ maps each b^j to e_{p_j}, and maps V into span{e_{p_j}}.
* For G_{c^j} the J-frame fibres are {Jx, Jx ⊕ Jc^j}, which differ on a finite set. ∎

(iii) combines (i), (ii) and Lemma B0. ∎

**Consequence for (A).**
* For FD₂, frame straightening fails already for the single map G_asym (Corollary A1).
* For DZ₂, it fails for the countable linear family 𝒯, although every finite subfamily straightens linearly.
* Neither failure matters for survival: G_asym and every G_c preserve CR, and Theorem C below handles all of CDZ₂ ⊇ 𝒯 at once.
* **Co-dispersibility in one frame is therefore not the right invariant for the R₂-versus-MLR question.** It is not necessary for a common survivor (Theorems B and C), and P4-S087 already showed it is not sufficient to cover E₀-breaking maps.
* Single-map DZ₂-straightening in general, and finite-family straightening outside CDZ₂, are not decided. They are superseded by the sharper invariant of §6.

## 4. Theorem C: one survivor for all countable-coset width-two observers

**Affine-state potentials.** Fix a strategy (G,d) with d savings-transformed, and an affine constraint set P = {⟨c_j,x⟩ = b_j, j ≤ n} with independent c_j ∈ Φ. For output strings w of length t, put:
* c^P(w) := 1 if G⁻¹[w] ∩ P ≠ ∅;
* for a functional c ∈ Φ independent of the c_j, s^{P,c}(w) := 1 if G⁻¹[w] ∩ P meets both {⟨c,x⟩ = 0} and {⟨c,x⟩ = 1};
* Ψ(P,t) := λ(P)⁻¹ Σ_{w∈2^t} 2^{−t} d(w) c^P(w) and γ(P,c,t) := λ(P)⁻¹ Σ_w 2^{−t} d(w) s^{P,c}(w);
* P_b := P ∩ {⟨c,x⟩ = b}.

These are computable rationals, uniformly in all the data. When the c_j are distinct coordinates, they reduce to the S082 quantities.

**Lemma C1 (S082 Lemmas 2.1–2.3 for affine states).**
(i) Ψ(P,t+1) ≤ Ψ(P,t).
(ii) λ(P)⁻¹∫_P X_t dλ ≤ Ψ(P,t), where X_t(x) := d(G(x)↾t).
(iii) ½(Ψ(P₀,t) + Ψ(P₁,t)) = Ψ(P,t) + γ(P,c,t). Hence min_b Ψ(P_b,t) ≤ Ψ(P,t) + γ(P,c,t).

*Proof.*
* (i) and (ii) are verbatim the S082 proofs, with [σ] replaced by P.
* (iii) G⁻¹[w]∩P = (G⁻¹[w]∩P₀) ⊔ (G⁻¹[w]∩P₁), so c^{P₀} + c^{P₁} = c^P + s^{P,c}.
* c is independent of the c_j, so λ(P_b) = λ(P)/2, and the normalisations λ(P_b)⁻¹ = 2λ(P)⁻¹ give the identity. ∎

**Lemma C2 (limit identification and excess bound; P4-S087 Lemmas 1–2 for functionals).** Let c′₁, …, c′_N ∈ Φ be such that {c_j} ∪ {c′_k} is linearly independent. Put f(w) := Σ_k s^{P,c′_k}(w). Then:
(i) along every output y, f(y↾t) is non-increasing and eventually equals f_∞(y) := |{k : ⟨c′_k, Δ_G(y)⟩ = 1}|·1(|G⁻¹(y)| = 2, G⁻¹(y) ⊆ P);
(ii) Σ_k γ(P,c′_k,t) ≤ Ψ(P,t) + λ(P)⁻¹E_λ[X_t(f−1)^+];
(iii) limsup_t λ(P)⁻¹E_λ[X_t(f−1)^+] ≤ λ(P)⁻¹E_λ[(2+B_∞)(f_∞−1)^+].

*Proof.*
* (i) The sets G⁻¹[y↾t] ∩ P ∩ {⟨c′,x⟩ = b} are compact and decreasing in t, with intersection G⁻¹(y) ∩ P ∩ {⟨c′,x⟩ = b}. So s^{P,c′} is eventually 1 iff G⁻¹(y) ∩ P contains two points with different ⟨c′,·⟩. With at most two preimages, this means both lie in P and ⟨c′, x⊕x′⟩ = 1.
* (ii) Termwise f ≤ c^P + (f−1)^+, because f ≥ 1 forces c^P = 1.
* (iii) This is the dominated-convergence argument of P4-S087 Lemma 2, with f ≤ N and X_t ≤ 2 + B_∞. ∎

No width modulus is used. Phantoms disappear along each y by compactness alone.

**Lemma C3 (coset dispersal).** Let F be a finite set of valid strategies (G_e, d_e) with every G_e ∈ CDZ₂, and put μ_e := (2+B^e_∞)λ, a finite measure with μ_e ≪ λ. For every a, N ∈ ℕ and ε > 0 there are c′₁, …, c′_N ∈ Φ, nonzero, with pairwise disjoint supports contained in [a,∞), such that

  Σ_{e∈F} μ_e{y : |G_e⁻¹(y)| = 2, |{k : ⟨c′_k, Δ_{G_e}(y)⟩ = 1}| ≥ 2} < ε.

*Proof.*
* **A finite set of dominant cosets.** For each e choose a countable Q_e with Δ_{G_e} ∈ Q_e ⊕ 𝒵 almost surely on the double locus. Since μ_e is finite and ≪ λ, there is a finite Q ⊆ ⋃_e Q_e with Σ_e μ_e{double, Δ_{G_e} ∉ Q ⊕ 𝒵} < ε/2. Put m := |Q|.
* **Annihilating group functionals.** Fix a′ ≥ a and a window [a′, a′+R) with (m+1) | R, and split it into H := R/(m+1) consecutive groups of m+1 coordinates.
  * For each group g, the m+1 vectors (⟨e_i, v⟩)_{v∈Q} ∈ F₂^Q, for i ∈ g, are linearly dependent. So some nonempty S_g ⊆ g has ⊕_{i∈S_g}⟨e_i, v⟩ = 0 for every v ∈ Q.
  * Put c_g := 1_{S_g}. Then c_g ≠ 0, supp c_g ⊆ g, and ⟨c_g, v⟩ = 0 for every v ∈ Q.
* **Random choice of groups.** Choose N distinct groups uniformly at random (H ≥ N), and take the c_g of those groups.
  * For a double output y with Δ = v ⊕ s, where v ∈ Q and s ∈ 𝒵, we have ⟨c_g, Δ⟩ = ⟨c_g, s⟩. This can be 1 only if s meets g.
  * If h groups meet s, then P(two or more chosen groups meet s) ≤ C(N,2)(h/H)². Here h ≤ |s ∩ [0, a′+R)| and H = R/(m+1), so h/H ≤ (m+1)|s∩[0,a′+R)|/R → 0 as R → ∞, because s has density zero.
  * The probability is ≤ 1 and each μ_e is finite, so by dominated convergence the μ_e-average of this probability tends to 0 as R → ∞.
  * For large R the average over the random choice is < ε/2, so some choice achieves it.
* Adding the two parts gives < ε. ∎

**Theorem C (countable-coset survivor).** There is z ∉ MLR such that G(z) ∈ CR for every G ∈ CDZ₂. In particular z ∈ CR (the identity lies in CDZ₂), and

  R₂^{cdz} ∖ MLR ≠ ∅.

The witness z is computable from the Turing jump of the validity set defined below.

*Proof.*
* **Enumeration and validity.** Fix an acceptable enumeration of pairs (G_e, d_e). Here G_e is a partial computable monotone prefix map and d_e a partial computable rational-valued function on output strings. Call e **valid** if G_e is total and λ-preserving with all fibres of size ≤ 2, G_e ∈ CDZ₂, and d_e is a total martingale. Let ε* be the characteristic sequence of validity, and let d̄_e be the savings transform of d_e (S082 Lemma 2.4).
* **The runs.** Run the S082 §4 / P4-S087 §3 construction, with guessed runs R(ε), weights w_e, and Φ := Σ_{e∈A} w_e Ψ^e and Γ := Σ_{e∈A} w_e γ^e on affine states. Put ℓ_i := 2i+2, N_i := 3·2^{i+3}ℓ_i and ε_i := 2^{−(i+4)}/ℓ_i. The state is (P, τ): P is an affine constraint set, initially P = 2^ω, and τ is a time.
  * *Stage (a).* Exactly as S082: on ε(i) = 1, compute P̂ := Ψ^i(P,τ), set w_i := 2^{−(i+2)}/(1+P̂), and add i to A.
  * *Stage (b), repeated ℓ_i times.*
    * Let a := 1 + the maximum index occurring in the supports of the constraints of P (a := 0 if there are none).
    * Dovetail over pairs (C, t), where t ≥ τ and C = (c′₁,…,c′_{N_i}) is a tuple of nonzero finitely supported vectors with pairwise disjoint supports in [a, ∞). Halt at the first pair satisfying the decidable inequality Σ_k Γ(P, c′_k, t) ≤ Φ(P,t) + ε_i.
    * Let k be the least index minimising Γ(P, c′_k, t), and b the least value minimising Φ(P ∩ {⟨c′_k,x⟩ = b}, t).
    * Set P := P ∩ {⟨c′_k,x⟩ = b} and τ := t.
  * *Stage (c).* Output P^ε_i and τ^ε_i.

  The new functional's support lies above every earlier support, so the constraints stay linearly independent.
* **Halting on true runs.** Let F be the active valid strategies.
  * Apply Lemma C3 with ε := ε_i·λ(P)/(2N_i·max_e w_e·|F|). The Lemma C3 bound is a measure; the factor N_i converts it into the excess bound, using (f−1)^+ ≤ N_i·1(f ≥ 2).
  * Lemma C2(iii), weighted and summed over F, then gives limsup_t(Σ_k Γ(P,c′_k,t) − Φ(P,t)) < ε_i/2. So the dovetailed search halts.
  * Runs on wrong guesses may diverge; S082 allows this.
* **Invariant.** The chosen functional has Γ ≤ (Φ + ε_i)/N_i < 3/N_i while Φ < 2. Lemma C1(iii) and (i) then give the S082 Proposition 4.1 bookkeeping verbatim, so Φ(P^{ε*}_i, τ^{ε*}_i) < 2 − 2^{−i} on true runs.
* **Martin-Löf test.**
  * Stage i adds exactly ℓ_i independent constraints, so λ(P^ε_i) = 2^{−(i+1)(i+2)}.
  * V_i := ⋃{P^ε_i : |ε| = i+1 and R(ε) completes stage i} is uniformly c.e., being a union of clopen sets given by finite data, and λ(V_i) ≤ 2^{i+1}·2^{−(i+1)(i+2)} ≤ 2^{−i}.
  * True runs complete and are nested, so S := ⋂_i P*_i is nonempty and compact, and S ⊆ ⋂_i V_i. Hence S ∩ MLR = ∅.
* **Compactness.** This is S082 Proposition 4.3 verbatim, with [σ*_i] replaced by the clopen sets P*_i and domination given by Lemma C1(ii). It yields z ∈ S with d̄_e(G_e(z)↾t) ≤ 2 + 2/w_e for every valid e and every t.
* **Conclusion.**
  * By S082 Lemma 2.4(iii) every valid d_e is bounded along G_e(z).
  * If some computable martingale succeeded on G(z) for some G ∈ CDZ₂, then some rational-valued computable martingale would succeed on G(z), and its index would be a valid e. Contradiction.
* **Complexity.** The runs are computable, so S is Π⁰₁(ε*). The bad set O := ⋃_{e valid}{x : ∃t d̄_e(G_e(x)↾t) > 2 + 2/w_e} is Σ⁰₁(ε*). The leftmost point of the nonempty Π⁰₁(ε*) class S∖O is computable from (ε*)′. ∎

**Corollary C4 (frame transport).** For every computable fair homeomorphism J, some z ∈ CR∖MLR has G(z) ∈ CR for every G ∈ CDZ₂^J.

*Proof.* As P4-S087 Corollary 6. Run Theorem C on the class {G∘J⁻¹ : G ∈ CDZ₂^J} ∪ {J⁻¹} ∪ {id}, where J⁻¹ is injective and so lies in CDZ₂. Then take z := J⁻¹(w), and use THM-0035 for z ∉ MLR. ∎

## 5. Consequences

**Corollary 5.1 (classes).**
(a) R₂ ⊆ R₂^{cdz} ⊆ R₂^{dz} ⊆ R₂^{fd}, and R₂^{cdz}∖MLR ≠ ∅.
(b) R₂^{cdz} ⊊ R₂^{fd}. The P4-S087 Theorem 8 witness lies in R₂^{fd} but is destroyed by F_{T*}∘D′, which lies in CDZ₂ because its difference vectors are the tails 1_{[q,∞)}, a countable set.
(c) R₂^{cdz} ⊆ OH^{aff} ∩ OH^{blk} (§1), so OH^{aff}∖MLR ≠ ∅. The P4-S083 Theorem 3.8 witness lies in OH^{blk} but D′(z) ∉ OH, and D′ is linear, so OH^{aff} ⊊ OH^{blk}.
(d) The chain is

  MLR ⊊ R₂^{cdz} ⊆ OH^{aff} ⊆ OH^{lin3},  OH^iso ⊆ OH^{aff} ⊊ OH^{blk},  R₂ ⊆ R₂^{cdz} ⊊ R₂^{fd},

and all frozen relations stand. Whether R₂^{cdz} ⊊ R₂^{dz}, and whether R₂ ⊊ R₂^{cdz}, are not decided.

**Corollary 5.2 (universality exclusions).** Let 𝒢 ⊆ F₂ be any family, finite, countable or arbitrary. If 𝒢 ⊆ CDZ₂^J for a single computable fair homeomorphism J, then 𝒢 is not universal for CR∖MLR (Corollary C4). With J = id this covers, all at once:
* every map in FD₂^K and every one-hole scan of K(z), for every computable affine fair homeomorphism K;
* every tail-coded F_T∘D′∘K for affine K, in particular S083's T*∘D′ and every T∘D′ʲ;
* the graded-frame family of P4-S087 Corollary 7(b) and the translation family 𝒯;
* every DZ₂ map, including G_dil.

By Theorem B(i) this family is not contained in any single DZ₂^J. **Corollary 5.2 therefore strictly extends P4-S087 Corollaries 6–7: it is a universality exclusion for a family that is not co-dispersible in any one computable frame.**

**Corollary 5.3 (the S084 error-stream requirement is met on affine frames).** For the Theorem C witness z, every one-hole scan T* and every computable affine fair homeomorphism K satisfy F_{T*}(K(z)) ∈ CR. So whenever T* resolves infinitely often on K(z), its prediction-error stream is computably random with limiting frequency ½ (P4-S084 Theorem 1). For linear and affine frames, the prompt's whole-error-stream requirement is thus met by construction rather than checked separately.

**Remark 5.4 (why the S083/S087 self-reading attack does not apply here).** A tail-coded observer that reads the construction's choices must hold a bit whose two completions are separated by many of the constraints the construction fixes.
* For an observer in an affine frame, the two completions differ by a vector from a countable set of cosets.
* Lemma C3 chooses every constraint to annihilate the dominant cosets of every active observer. So in the potential accounting an affine-frame reader contributes only the small Lemma C3 excess, and Theorem C bounds its capital on z. This is an explanation of the proof, not an extra claim.
* A reader therefore needs a frame whose difference vectors are essentially uncountable modulo 𝒵. That is exactly the frontier of §6.

## 6. The sharpened frontier: nonlinear (uncountable-coset) E₀-breaking ambiguity

After Theorem C and Corollary C4:
* **Route A (R₂ = MLR).** A universal family must contain, for every computable frame J, a member outside CDZ₂^J. In every frame, it needs width-two ambiguity whose difference vectors are essentially uncountable modulo 𝒵. Since 𝒵 ⊇ finitely supported vectors, such ambiguity is E₀-breaking in every frame.
* **Route B (MLR ⊊ R₂).** A survivor must in addition defeat every such map. The linear mechanism of Theorem C cannot supply this in general, as the explicit two-frame instance below shows.

**Two nonlinear causal frames.** Split coordinates into even and odd.
* **K_mix.** Even coordinates are controls a_j := x_{2j}, and are left unchanged. Odd coordinates carry data b_j := x_{2j+1}, and are recoded as

  b′_j := b_j ⊕ b_{j−2} ⊕ (1 ⊕ a_j)·b_{j−1}  (with b_{−1} = b_{−2} := 0).

* **K′_mix.** Odd coordinates are controls and are left unchanged. Even coordinates carry data b̃_j := x_{2j}, and are recoded as

  b̃′_j := b̃_j ⊕ b̃_{j−2} ⊕ (1 ⊕ x_{2j−1})·b̃_{j−1}  (with x_{−1} := 0).

Both maps are causal: every output bit is the corresponding input bit XOR a function of strictly earlier input bits. So both are computable fair homeomorphisms with causal computable inverses. Neither is affine: the data recursion depends on the controls multiplicatively.

For q ∈ ℕ:
* U_q := F_{T_q}∘K_mix, where T_q holds K_mix-coordinate 2q+1 forever and reads every other coordinate in increasing order;
* U′_q := F_{T′_q}∘K′_mix, where T′_q holds K′_mix-coordinate 2q forever and reads every other coordinate in increasing order.

Both are in F₂, and every fibre has exactly two points. U_q ∈ FD₂^{K_mix} and U′_q ∈ FD₂^{K′_mix}.

**Proposition D.**
(i) **Uncountable cosets.** Under λ, the difference vector Δ_{U_q} has no atoms modulo 𝒵: P(Δ_{U_q} ⊕ v ∈ 𝒵) = 0 for every v ∈ 2^ω. So U_q ∉ CDZ₂, and likewise U′_q ∉ CDZ₂.
(ii) **No common annihilating parity.** Let c ∈ Φ have support inside [2q+3, ∞). Then c separates the pairs of U_q with λ-probability ≥ ¼ if c has an odd support point, and the pairs of U′_q with λ-probability ≥ ¼ if c has an even support point. Hence:
  * for every N ≥ 16 and every N nonzero c′₁, …, c′_N ∈ Φ with disjoint supports inside [2q+3, ∞), one of U_q, U′_q has λ{two or more of the c′_k separate} ≥ 1/16;
  * so the conclusion of Lemma C3 fails for the two-element family {U_q, U′_q}, equipped with any martingales (μ_e ≥ 2λ).
(iii) **Neither natural frame co-disperses the pair.** In the raw frame neither map lies in DZ₂. U′_q ∉ DZ₂^{K_mix}, and U_q ∉ DZ₂^{K′_mix}.
(iv) **Each class alone has a survivor.** By Corollary C4 with J = K_mix (respectively K′_mix), some z ∈ CR∖MLR survives all of CDZ₂^{K_mix} ⊇ FD₂^{K_mix}, and likewise for K′_mix.

*Proof.*
(i) *The difference process.*
* Two preimages of one U_q-output share the controls a and all K_mix-coordinates except 2q+1. Their data difference δ therefore satisfies δ_j = 0 for j < q, δ_q = 1, and

  δ_j = δ_{j−2} ⊕ (1 ⊕ a_j)δ_{j−1}  for j > q.

* Let s_j := (δ_{j−1}, δ_j), so s_q = (0,1). The transition matrix is invertible, so (0,0) never occurs. The transitions are:
  * (0,1) → (1, 1⊕a_{j+1});
  * (1,1) → (1, a_{j+1});
  * (1,0) → (0,1), deterministically.
* Whenever δ_j = 1, the next value δ_{j+1} is a fresh fair bit, because a_{j+1} is independent of the past. Among any two consecutive steps after q, at least one is such a random step.
* Fix v. At each random step the mismatch indicator [δ_{j+1} ≠ v_{j+1}] is conditionally fair given the past. The martingale strong law then gives liminf_n |{q < j ≤ n : δ_j ≠ v_{2j+1}}|/n ≥ ¼ almost surely. So Δ_{U_q} ⊕ v has lower density ≥ ⅛ on ℕ almost surely, and in particular Δ_{U_q} ⊕ v ∉ 𝒵.
* Every output of U_q is double. So for any countable Q, μ(Δ ∈ Q ⊕ 𝒵) = 0, and U_q ∉ CDZ₂.
* U′_q is symmetric, with even and odd exchanged.

(ii) *A single functional.*
* Controls are unchanged across a U_q-pair, so ⟨c, Δ_{U_q}⟩ = ⊕_{j∈J_c} δ_j, where J_c is the set of data indices j with 2j+1 ∈ supp c.
* Let p := max J_c > q. Given a_{<p}, the bits δ_j for j < p are fixed. If δ_{p−1} = 1, then δ_p is a fresh fair bit, so ⟨c,Δ⟩ is conditionally fair.
* δ_{p−1} = 0 with δ_{p−2} = 1 requires a random step at p−1 with outcome 0, which has probability ≤ ½. (p−1 = q is impossible, since s_q = (0,1).) Hence P(⟨c,Δ⟩ = 1) ≥ ½·½.
* The even case for U′_q is symmetric.

*A tuple of functionals.* Each nonzero c with support ⊆ [2q+3, ∞) has an odd or an even support point. So Σ_k [P(c′_k separates U_q) + P(c′_k separates U′_q)] ≥ N/4, and one of the two maps has expected separation count X with E X ≥ N/8. Since X ≤ N, E X ≤ 1 + N·P(X ≥ 2), so P(X ≥ 2) ≥ (N/8 − 1)/N ≥ 1/16 for N ≥ 16.

(iii)
* In the raw frame, Δ has positive lower density on the data positions, by (i).
* K_mix fixes the even coordinates, and a U′_q-pair differs on the even coordinates by its own data difference δ′, which has positive lower density by (i). So in K_mix-coordinates the U′_q-pairs differ on a set of positive lower density.
* The case of U_q in K′_mix-coordinates is symmetric.

(iv) is Corollary C4. ∎

*Honest scope of Proposition D.*
* The fixed-hold maps U_q and U′_q are themselves CR-preserving. Each deletes one fixed coordinate after a computable fair homeomorphism, and THM-0038 applies.
* Proposition D is therefore a statement about **mechanisms**, not a destruction result. It shows that the Theorem C parity mechanism and the P4-S087 single-frame mechanism, in either natural frame, do not extend to the union FD₂^{K_mix} ∪ FD₂^{K′_mix}.
* **Open (the sharpened form of (A)/(B)).** Is there one z ∈ CR∖MLR surviving every map in FD₂^{K_mix} ∪ FD₂^{K′_mix}? Is this union contained in a single CDZ₂^J? These classes contain infinitely resolving, self-reading observers in each frame.

**Conceptual reformulation (recorded as a research direction, not a theorem).**
* Both survivor mechanisms need fresh clopen halvings that are, up to small capital-weighted mass, invariant under the dominant partner involutions of all active observers.
* For an affine frame, the partner involutions are translations x ↦ x ⊕ v with v in countably many 𝒵-cosets. Finitely many of them generate a finite elementary abelian group, whose invariant parities have finite codimension (Lemma C3).
* For a nonlinear frame K, the partner involutions K⁻¹∘flip_q∘K are data-dependent, and finitely many of them can generate an infinite group acting on 2^ω.
* The next mechanism to test is therefore **approximate invariance** of fresh clopen halvings under finitely many such involutions. These are Følner-type almost-invariant sets, whose existence for ergodic actions is tied to amenability and the absence of strong ergodicity. Two involutions always generate a (finite or infinite) dihedral group.
* Whether such almost-invariant halvings exist effectively, freshly and in the required number, and whether failure of this (spectral-gap-type rigidity) is the resource a Route-A family needs, is not decided. No literature claim is made about it.

## 7. Routes attempted on the overriding target (not closed)

**7.1 Route B beyond affine frames (analysis).** Theorem C's construction can use arbitrary fresh clopen halvings in place of parities. Lemma C1 and Lemma C2 hold verbatim for any clopen state P and any clopen C with λ(P∩C) = λ(P)/2. For approximate halvings the weighted form of Lemma C1(iii) still gives min_b Ψ(P_b) ≤ Ψ(P) + γ.
* What fails is Lemma C3: the joint supply of fresh halvings that the dominant partner involutions of several nonlinear frames almost never split.
* For a single nonlinear frame K such halvings exist: K-coordinates far beyond the dominant holds are fresh. x↾m is a function of K(x)↾n(m), and the coordinates of a fair sequence are independent, so these K-coordinates are independent of every constraint already fixed. That is P4-S087 Corollary 6.
* For the K_mix / K′_mix pair, Proposition D shows that parities do not suffice. Nonlinear almost-invariant halvings were not constructed.

**7.2 Route B: an S083-type separation R₂ ⊊ R₂^{cdz} (analysis).** A self-reading observer in a K_mix-like frame would hold a data bit and wait until the true run's parity constraints separate its two candidates. By Proposition D(ii) each fresh constraint separates with probability ≥ ¼, not with certainty.
* The S083 Lemma 3.6 step (every hold is resolved on the witness class) then depends on the witness's control bits, which the compactness selection does not control.
* The fooling bound would need a per-constraint separation analysis.
* Neither was completed, so R₂ ⊊ R₂^{cdz} is **not** proved.

**7.3 Route A with nonlinear tail codes (analysis).** The Theorem C witnesses must be destroyed, if at all, by maps outside every CDZ₂^J for their construction frame, that is by uncountable-coset ambiguity. The race analysis of P4-S087 §6.1 carries over unchanged: partners of a non-MLR point under computable fair involutions are again non-MLR. No universal family was obtained.

**7.4 Frame straightening in the strict sense of (A).**
* Settled negatively for FD₂ (a single map, Corollary A1).
* Settled negatively for DZ₂ for the countable family 𝒯 (Theorem B(i)), with every finite subfamily straightened (Theorem B(ii)).
* Single-map DZ₂-straightening (for example of G_asym), and finite-family straightening outside CDZ₂, are not decided. Theorems B and C show they are not the decision-relevant invariant.

**7.5 Not attempted, as instructed.** Escrow, hazards, residues, unit columns, record-only z₀, multi-hole variants, and any change to Y/M/H/X.

## 8. Finite audit

`phase4/P4-S088_COSET_AUDIT.py` runs in exact arithmetic in under 2 s and makes 92,724 checks.
* **Part 1 (G_asym).** Three blocks, a₃ = 9, all 2¹¹ inputs of length 11.
  * Container packing: lengths, nesting, disjointness and total mass, both residue cases N ≡ 1, 2 (mod 3), and the collapse of every non-straddling child into one parent cylinder.
  * Fairness at every output precision ≤ 9.
  * Exact weights ¼, ¾ over all 315 A-prefixes of level 3.
  * λ(A₃) = ∏(1 − 2^{−ℓ_j}), and λ(A) ≈ 0.5775761902.
* **Part 2.** K_c involution and fibre {x, x⊕c} on 24-bit truncations. Reduced echelon frames J with J bʲ = e_{p_j}, J(span) ⊆ span{e_{p_j}}, and causal involutive transvections.
* **Part 3.** The pointwise affine-min bound, convexity of h⁻¹, and the inequality E_rE_x D_n ≥ h⁻¹(1 − k/n) by exact enumeration for random causal fair maps on 8 bits (k = 1, 2, 3).
* **Part 4.** Group functionals annihilating random finite Q with support inside m+1 coordinates, and ⟨c_g, v⊕s⟩ = ⟨c_g, s⟩.
* **Part 5.** For random fair maps with random rational martingales and random independent affine constraints on 7-bit inputs: the refinement identity of Lemma C1(iii), monotonicity in t, domination, and λ(P_b) = λ(P)/2.

The script prints `ALL P4-S088 AUDITS PASS`. The frozen P4-S087 audit was re-run and still passes. The audits cover finite truncations only. Totality, fairness and the weights of the infinite G_asym, Theorem B(i), the Martin-Löf test, compactness, computable randomness and every class inclusion rest on the written proofs.

## 9. Disposition

**Proved.**
* **Theorem A:** positive-measure asymmetric double loci exist in F₂, via the explicit G_asym with weights ¼, ¾.
* Corollaries A1–A3: FD frame straightening fails for a single map; asymmetry is harmless (P4-S003); DZ₂ admits asymmetric weights.
* **Theorem B:** the translation family 𝒯 ⊆ CDZ₂ lies in no single DZ₂^J, every finite subfamily lies in a single FD₂^J, and all members preserve CR.
* Lemmas C1–C3.
* **Theorem C:** one z ∈ CR∖MLR survives every countable-coset width-two observer. The quantifier order is ∃z∀G, and the class is not co-dispersible in any single frame.
* Corollary C4: the frame-transported version.
* Corollaries 5.1–5.3: R₂^{cdz}∖MLR ≠ ∅; R₂^{cdz} ⊊ R₂^{fd}; OH^{aff}∖MLR ≠ ∅; OH^{aff} ⊊ OH^{blk}; universality exclusion for every family inside one CDZ₂^J; the S084 requirement met on affine frames.
* **Proposition D:** an explicit nonlinear two-frame instance at which both existing mechanisms stop.

**Not proved.**
* R₂ = MLR or MLR ⊊ R₂.
* R₂ ⊊ R₂^{cdz}, or R₂^{cdz} ⊊ R₂^{dz}.
* A survivor for FD₂^{K_mix} ∪ FD₂^{K′_mix}, or for OH^iso.
* A universal width-two family.
* Single-map DZ₂-straightening.
* No quantifier swap of P4-S086 is claimed.

**Unresolved and kept separate.** R₂ versus MLR (decisive), R₂ versus OH^iso, OH^iso versus MLR, R_fin versus R₂, U(H), X ∈ OH, fixed-S preservation, block-H invariance of OH, TKLR∖MLR and QST-0001.

**Frozen.**
* All P4-S001–S087 results and the original Y/M/H/X.
* Literature at recorded access levels; no source was fetched or upgraded.
* PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged.
* Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED.

No novelty, openness, priority, publication or outreach claim is made. Owner/external blocker: NONE.

**Next: P4-S089.** Attack nonlinear (uncountable-coset) E₀-breaking ambiguity directly:
* either construct one CR∖MLR survivor for FD₂^{K_mix} ∪ FD₂^{K′_mix}, and then for all one-hole scans after all causal computable fair homeomorphisms, by effective almost-invariant halvings;
* or prove that the partner-involution groups of an explicit nonlinear family have a rigidity (spectral-gap-type) property that defeats every potential/fixing method, and test it as a Route-A universal family.

R₂ versus MLR remains the decisive target.
