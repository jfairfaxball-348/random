# P4-S082 — Consistency potentials: a computably random non-Martin-Löf-random sequence in OH

Date: 2026-10-10
Scope: Phase 4 Mathematics ONLY; selected CAND-01; pinned incoming live main `a6557f24867e48f5ac018f9865896993e74cc443` (the P4-S081 outgoing SHA).
Disposition: **The OH-certification gate is PASSED: OH∖MLR ≠ ∅ is PROVED (Theorem 4.4). A computably random z that is not Martin-Löf random lies in OH. The construction bypasses both halves of the P4-S081 §7 obstruction. It uses no random background, so obstruction (i) disappears. Blind bets on fixed content are controlled by a consistency potential, which resolves obstruction (ii). The same construction gives z∉MLR with K(z)∈OH for EVERY computable finite-block recoding K (Theorem 5.1). In particular H(z)∈OH and z∈OH^{lin3}, so a potential-built witness of this kind cannot separate OH from its H-image. A general cheap-coordinate criterion (Theorem 6.1) isolates exactly where bounded postponement width is used. Its precise boundary for globally ≤2-to-1 maps is recorded (§6.3). NOT decided: R₂=OH, R₂=OH^iso, U(H), X∈OH, fixed-S preservation, R₂ vs MLR, and anything about KLR/TKLR or QST-0001.**

## 0. Authority, uniqueness and frozen objects

Live remote `main` was verified with `git ls-remote origin refs/heads/main` to equal `a6557f24867e48f5ac018f9865896993e74cc443`, the P4-S081 commit whose close record embeds the P4-S082 prompt. The `phase4/` tree contained the P4-S001–S081 records and no P4-S082 file; the session ledger names P4-S082 only as the next session. P4-S082 is therefore unused. The incoming prompt is byte-identical to `authoritative/NEXT_SESSION_PROMPT.md`; no discrepancy was found.

Reviewed: the phase summaries for P4-S001–S081; in detail S008, S011, S012, S032, S033, S079, S080 and S081 (Lemma 2, Theorem A, Corollaries A1–A6, Theorem B, §7), the S081 validation and close records, selected CAND-01, the P3-S008 Gate-3 PASS and both Phase-4 pivots.

Retained: MLR ⊆ R₂ ⊆ OH^iso ⊆ OH ⊊ CR and KLR ⊆ TKLR ⊆ OH. The ORIGINAL computably random Y, the clipped syntactically self-avoiding wtt autoreduction M, the repeated H with A=[101;110;111] and X=H⁻¹(Y) are untouched; nothing below uses or alters them. Conventions follow S081 §0. A *scan* is a total computable adaptive no-repeat scan (S008). It is *one-hole* if every infinite transcript leaves at most one source coordinate unread, and every such scan preserves the fair coin λ. Martingales are nonnegative and rational-valued (S012, S081). OH = {z∈CR : F_T(z)∈CR for every one-hole scan T}.

## 1. Decision-relevant literature calibration (recorded access levels)

S081 step (0) found no catalogue statement separating total-strategy non-monotonic randomness from MLR. Because the certification construction is decision-relevant, a bounded external check was made. Two new catalogue sources are recorded:

| Record | Content used | Access |
|---|---|---|
| SRC-0069 Kastermans–Lempp, *Comparing notions of randomness* (author preprint) | Definitions of permutation and injective randomness (non-adaptive orders, partial computable stake functions). Theorems 6–7: injective and permutation randomness are each strictly weaker than MLR. The expected-martingale Lemma 8, the slow-but-sure (savings) Lemma 9, the average operator, and the construction of the real together with an effective martingale, verified by a compactness argument. The introduction states that total permutation randomness equals computable randomness. | full preprint text; STATEMENT_INSPECTED, with the §2 proof and parts of the §3 proof read (THM-0077, THM-0078) |
| SRC-0070 Bienvenu–Hölzl–Kräling–Merkle, *Separations of non-monotonic randomness notions*, CCA 2009, OASIcs 11, 71–82, doi:10.4230/OASIcs.CCA.2009.2260 | The abstract reports the Kastermans–Lempp separations for the Miller–Nies non-adaptive notions and announces a complete classification of those notions by strength | ABSTRACT_INSPECTED |

**What is and is not taken from these sources.** None of them concerns *adaptive* strategies of bounded postponement width, so none yields OH∖MLR ≠ ∅ directly. Their strategy classes (partial, non-adaptive, unbounded width) and OH's (total, adaptive, bounded width) are incomparable. The method of §§2–4 is **modelled on** the Kastermans–Lempp expected-martingale / average-operator / compactness technique. The adaptation is programme mathematics: an adaptive replacement for their expected martingale (the consistency potential of §2) and a frontier-based cost bound (§3) in place of their type and partiality analysis. No novelty, priority or openness inference is drawn, in either direction, from what these sources contain or omit. QST-0001 (KLR=MLR?) is recorded in the catalogue as SOURCE-STATED OPEN, and Kastermans–Lempp restate it as open. Nothing here bears on it (§7.3).

## 2. The consistency potential

**Strategies.** A *strategy* is a pair (G, d). Here G: 2^ω→2^ω is total computable and λ-preserving, given by a computable monotone prefix map with computable modulus. d is a rational-valued computable martingale on the outputs. Its capital at output time m is X_m(z) := d(G(z)↾m). For a scan T, G = F_T. For a scan T of a recoding K(z), G = F_T∘K. Since G is λ-preserving, λ(G⁻¹[w]) = 2^{−|w|} for every output string w, and G⁻¹[w] is clopen and decidable from w.

**Partial assignments.** A *partial assignment* σ is a function from a finite set dom σ ⊆ ℕ to {0,1}. Put [σ] := {z : z(q)=σ(q) for q∈dom σ}, so λ[σ] = 2^{−|σ|}. For k∉dom σ write σ_b := σ∪{k↦b}.

**Definition 2.0.** For a strategy (G,d), a partial assignment σ, m∈ℕ and k∉dom σ, put, for w∈2^m,

  c^σ(w) := 1 if G⁻¹[w]∩[σ] ≠ ∅, else 0;
  s^{σ,k}(w) := 1 if G⁻¹[w]∩[σ] meets both {z_k=0} and {z_k=1}, else 0;

  Ψ(σ,m) := 2^{|σ|} Σ_{w∈2^m} 2^{−m} d(w) c^σ(w)  (**consistency potential**),
  γ(σ,k,m) := 2^{|σ|} Σ_{w∈2^m} 2^{−m} d(w) s^{σ,k}(w)  (**split weight** of k).

Equivalently Ψ(σ,m) = 2^{|σ|}∫X_m C^σ_m dλ with C^σ_m(z) := c^σ(G(z)↾m). Both quantities are computable rationals, uniformly in (an index of) the strategy, σ, m and k.

**Lemma 2.1 (monotonicity).** Ψ(σ,m+1) ≤ Ψ(σ,m) for every strategy, σ and m.

*Proof.* G⁻¹[wb] ⊆ G⁻¹[w], so c^σ(wb) ≤ c^σ(w). As d ≥ 0, d(w0)c^σ(w0)+d(w1)c^σ(w1) ≤ (d(w0)+d(w1))c^σ(w) = 2d(w)c^σ(w). Multiply by 2^{|σ|}2^{−m−1} and sum over w∈2^m. ∎

**Lemma 2.2 (domination).** 2^{|σ|}∫_{[σ]} X_m dλ ≤ Ψ(σ,m). That is, the expected capital at time m under the fair coin conditioned on [σ] is at most Ψ(σ,m).

*Proof.* If z∈[σ] then z∈G⁻¹[G(z)↾m]∩[σ], so 1_{[σ]} ≤ C^σ_m pointwise. ∎

**Lemma 2.3 (exact refinement identity).** For k∉dom σ and every m,

  ½(Ψ(σ_0,m) + Ψ(σ_1,m)) = Ψ(σ,m) + γ(σ,k,m).

Consequently min_b Ψ(σ_b,m) ≤ Ψ(σ,m) + γ(σ,k,m).

*Proof.* G⁻¹[w]∩[σ] = (G⁻¹[w]∩[σ_0]) ∪ (G⁻¹[w]∩[σ_1]), so c^{σ_0}(w)+c^{σ_1}(w) = c^σ(w)+s^{σ,k}(w). Also 2^{|σ_b|} = 2·2^{|σ|}. ∎

Lemmas 2.1–2.3 use only totality and λ-preservation of G. They hold for every scan (any number of holes), for every recoded scan, and for every finite-fibre map. Bounded postponement width enters only through the size of the split weights (§3).

**Lemma 2.4 (savings transform).** Let d₀ be a rational-valued computable martingale on outputs with d₀(∅)=1. Define A, B on output strings by A(∅)=1, B(∅)=0, and for v and b∈{0,1}:

  A′ := A(v)·d₀(vb)/d₀(v) (A′ := A(v) if d₀(v)=0); B′ := B(v); while A′ ≥ 2 do A′ := A′−1, B′ := B′+1; A(vb) := A′, B(vb) := B′,

and d := A+B. Then:
(i) d is a rational-valued computable martingale with d(∅)=1, uniformly in d₀, and 0 ≤ A < 2 everywhere;
(ii) along every output sequence y and all m ≤ m′, d(y↾m′) > d(y↾m) − 2;
(iii) if d is bounded along y, so is d₀.

*Proof.* (i) d₀(v0)+d₀(v1) = 2d₀(v), so before the bank transfers the active parts of the two children average to A(v). Each transfer moves one unit from A to B and leaves A+B unchanged. Hence d(v0)+d(v1) = 2A(v)+2B(v) = 2d(v). (ii) B is non-decreasing along y, so d(y↾m′) ≥ B(y↾m′) ≥ B(y↾m) = d(y↾m) − A(y↾m) > d(y↾m) − 2. (iii) If d is bounded along y, then B is bounded and only finitely many transfers occur. Between transfers A(vb)/A(v) = d₀(vb)/d₀(v), so after the last transfer A = c·d₀ along y for a constant c > 0. Hence d₀ < 2/c along y. If d₀ vanishes at some point of y it stays 0, and the claim is trivial. ∎

For a scan the stake of d at a read is A·θ/(A+B) ∈ [−1,1], where θ is the original stake fraction, so d is again a stake function on transcripts, computable from them.

## 3. Split weights of bounded-width strategies

For a scan T and an output (transcript) string w of length t, let Q(w) = {q_0,…,q_{t−1}} be the coordinates read along w. Then F_T⁻¹[w] = {z : z(q_s) = w_s for s<t}. Hence, for G = F_T:
* c^σ(w) = 1 iff w agrees with σ on Q(w)∩dom σ;
* for k∉dom σ, s^{σ,k}(w) = c^σ(w)·1(k∉Q(w)).

So γ(σ,k,t) is the capital-weighted mass of σ-consistent transcripts of length t that have **not read k**.

**Lemma 3.1 (one-hole cost bound).** Let T be an h-hole scan with the computable frontier c of S081 Lemma 2, and let c(n) ≤ t. Then for every σ and every set K ⊆ [0,n)∖dom σ,

  Σ_{k∈K} γ(σ,k,t) ≤ h·Ψ(σ,t).

In particular the bound is Ψ(σ,t) for a one-hole scan.

*Proof.* Every transcript of length t ≥ c(n) leaves at most h coordinates below n unread. So for each w∈2^t at most h elements k∈K have s^{σ,k}(w)=1, and each such term is at most c^σ(w). Sum over w. ∎

**Recoded scans.** A *computable finite-block recoding* K is given by a computable partition of ℕ into finite blocks B_0, B_1, …, and computable bijections κ_j of {0,1}^{B_j}. The partition is presented by a total computable block-index function β and a total computable map j ↦ canonical index of B_j. The recoding acts by K(z)↾B_j = κ_j(z↾B_j). K is a computable fair-coin homeomorphism with computable inverse, since K⁻¹ is the recoding by the κ_j⁻¹. Examples are the repeated H with A, any computable sequence of blockwise GL(3,F₂) matrices (S070), and the finite-coordinate recodings of S034. For a scan T of K(z), put G = F_T∘K. Then G⁻¹[w] = {z : K(z)(q_s)=w_s for s<t} is a product of blockwise constraints.

**Lemma 3.2 (block-recoded cost bound).** Let T be a one-hole scan with frontier c, K a computable finite-block recoding, G = F_T∘K, and c(n) ≤ t. Let K₀ ⊆ ℕ∖dom σ be a set whose elements lie in pairwise distinct blocks, each block contained in [0,n). Then Σ_{k∈K₀} γ(σ,k,t) ≤ Ψ(σ,t).

*Proof.* If every virtual coordinate of a block B_j has been read along w, then z↾B_j = κ_j⁻¹(w↾B_j) is the same for every z∈G⁻¹[w], so s^{σ,k}(w)=0 for k∈B_j. Every block meeting K₀ lies below n. Along w at most one virtual coordinate below n is unread, so at most one such block is not fully read, and it contains at most one element of K₀. ∎

Lemmas 3.1 and 3.2 are the only places where bounded postponement width is used.

## 4. The certification construction

**Enumeration and validity.** Fix an acceptable enumeration (T_e, θ_e)_{e∈ℕ} of pairs of partial computable functions on finite transcripts. T_e gives the next query and θ_e gives a rational stake in [−1,1]. Call e **valid** if T_e is total and no-repeat on every transcript, every infinite transcript leaves at most one coordinate unread, and θ_e is total. For valid e let d_e be the stake martingale of θ_e on outputs, d̄_e its savings transform (Lemma 2.4), and

  X^e_t(z) := d̄_e(F_{T_e}(z)↾t),  Ψ^e(σ,t), γ^e(σ,k,t) as in §2 for (F_{T_e}, d̄_e),

with c_e the frontier of S081 Lemma 2. For valid e, c_e is computable uniformly in e by searching all transcripts.

**Fact 4.0.** z∈OH iff for every valid e, d_e does not succeed on F_{T_e}(z).

*Proof.* (⇐) The identity scan is a valid one-hole scan, so z∈CR. Any computable martingale succeeding on F_T(z) can be replaced by a rational-valued computable martingale succeeding on the same sequence (S012/S081 convention), whose stake fractions give a valid pair. (⇒) This is the definition of OH. ∎

By Lemma 2.4(iii), it suffices that each X^e be bounded along z.

**Guessed runs.** For ε∈{0,1}^{<ω} the run R(ε) has stages i = 0,1,…,|ε|−1. Its state is a partial assignment σ, a time τ, and positive rational weights w_e for e in A := {e<|ε| : ε(e)=1, e already processed}. Put

  Φ(σ,t) := Σ_{e∈A} w_e Ψ^e(σ,t),  Γ(σ,k,t) := Σ_{e∈A} w_e γ^e(σ,k,t),

using the current A. Start with σ=∅, τ=0, A=∅. Let ℓ_i := 2i+2 and N_i := 2^{i+4}ℓ_i.

*Stage i.*
(a) If ε(i)=1: compute P := Ψ^i(σ,τ), set w_i := 2^{−(i+2)}/(1+P), and add i to A.
(b) Repeat ℓ_i times:
 * let a := 1+max dom σ (a := 0 if σ=∅) and K₀ := [a, a+N_i);
 * let τ″ := max(τ, max_{e∈A} c_e(a+N_i));
 * let k be the least element of K₀ minimizing Γ(σ,k,τ″);
 * let b be the least element of {0,1} minimizing Φ(σ_b,τ″), where σ_b = σ∪{k↦b};
 * set σ := σ∪{k↦b} and τ := τ″.
(c) Output σ^ε_i := σ and τ^ε_i := τ.

Each stage depends only on ε↾(i+1). The run on a longer guess repeats the earlier stages verbatim, so the outputs for ε↾(i+1) and ε↾(i+2) are nested. If some e with ε(e)=1 is not valid, the run may diverge; nothing below needs runs on wrong guesses to halt. Exactly ℓ_i new coordinates are fixed at stage i, all at least a > max dom σ. Hence |dom σ^ε_i| = Σ_{j≤i}(2j+2) = (i+1)(i+2).

**Proposition 4.1 (invariant).** If every e≤i with ε(e)=1 is valid, then R(ε) completes stage i and

  Φ(σ^ε_i, τ^ε_i) < 2 − 2^{−i}.

*Proof.* We show Φ ≤ 2−2^{−(i−1)} before stage i, by induction. Before stage 0, Φ = 0 = 2−2^{1}. Assume Φ(σ,τ) ≤ 2−2^{−(i−1)} before stage i.

(a) All computations are finite for valid indices. The new term is w_i P = 2^{−(i+2)}P/(1+P) < 2^{−(i+2)}.

(b) Consider one repetition. The search for c_e(a+N_i) halts for valid e (S081 Lemma 2). Every k∈K₀ is below every active frontier at τ″. By Lemma 3.1 applied to each e∈A and weighted, Σ_{k∈K₀} Γ(σ,k,τ″) ≤ Φ(σ,τ″), so the chosen k has Γ(σ,k,τ″) ≤ Φ(σ,τ″)/N_i < 2/N_i. Lemma 2.3, weighted, gives Φ(σ_b,τ″) ≤ Φ(σ,τ″) + Γ(σ,k,τ″) for the chosen b. Lemma 2.1 gives Φ(σ,τ″) ≤ Φ(σ,τ). So each repetition raises the carried bound by less than 2/N_i, and the ℓ_i repetitions together by less than ℓ_i·2/N_i = 2^{−(i+3)}. (While the bound stays below 2, the estimate Γ < 2/N_i persists.)

Hence Φ(σ^ε_i,τ^ε_i) < 2 − 2^{−(i−1)} + 2^{−(i+2)} + 2^{−(i+3)} = 2 − (13/8)2^{−i} < 2 − 2^{−i}, which also carries the induction. ∎

**Proposition 4.2 (Martin-Löf test).** Let V_i := ⋃{[σ^ε_i] : ε∈{0,1}^{i+1} and R(ε) completes stage i}. Then (V_i) is a uniformly c.e. sequence of open (indeed clopen-union) sets with λ(V_i) ≤ 2^{i+1}·2^{−(i+1)(i+2)} = 2^{−(i+1)²} ≤ 2^{−i}.

*Proof.* Dovetail the 2^{i+1} runs. Each completed run contributes one set [σ^ε_i] of measure 2^{−(i+1)(i+2)}. ∎

Let ε* be the characteristic sequence of validity, σ*_i := σ^{ε*↾(i+1)}_i, τ*_i := τ^{ε*↾(i+1)}_i, and let w_e (e valid) be the weights assigned in these runs. By Proposition 4.1 every true run completes, and the σ*_i are nested. Put

  S := ⋂_i [σ*_i].

S is a nonempty compact set, being an intersection of nested nonempty compact sets. Every z∈S lies in ⋂_i V_i and so is **not Martin-Löf random**.

**Proposition 4.3 (compactness).** There is z∈S such that X^e_t(z) ≤ L_e := 2 + 2/w_e for every valid e and every t.

*Proof.* Suppose not. Let O := ⋃_{e valid} {z : ∃t X^e_t(z) > L_e}. Since X^e_t(z) depends on finitely many coordinates of z, O is open and S ⊆ O. The sets [σ*_i] are compact and decreasing with intersection S, so [σ*_{i₀}] ⊆ O for some i₀. Compactness of [σ*_{i₀}] yields finitely many witnesses (e_r, t_r) such that every z∈[σ*_{i₀}] has X^{e_r}_{t_r}(z) > L_{e_r} for some r. Let b := max_r e_r, t̂ := max_r t_r, j := max(i₀, b), and t ≥ max(t̂, τ*_j). Every e_r is valid and ≤ j, so it is active in the true run at stage j.

Take z∈[σ*_j] ⊆ [σ*_{i₀}] and its witness r. Lemma 2.4(ii) gives X^{e_r}_t(z) > L_{e_r} − 2 = 2/w_{e_r}, so Σ_{e active} w_e X^e_t(z) > 2. This sum depends only on finitely many coordinates of z, so its minimum over [σ*_j] exceeds 2. Lemma 2.2, weighted, gives Φ(σ*_j,t) > 2.

But Lemma 2.1 and Proposition 4.1 give Φ(σ*_j,t) ≤ Φ(σ*_j,τ*_j) < 2, a contradiction. ∎

**Theorem 4.4 (certification gate).** There is a sequence z that is computably random, lies in OH, and is not Martin-Löf random. Equivalently, there is a non-ML-random sequence on which no total computable non-monotonic betting strategy of bounded postponement width succeeds (S081 Corollary A3). Hence

  MLR ⊊ OH = OH_h (every finite h) = R_k^scan (every k≥2).

The witness can be chosen computable from ∅‴.

*Proof.* Take z from Proposition 4.3. Every valid X^e is bounded along z, so by Lemma 2.4(iii) every d_e is bounded on F_{T_e}(z), and z∈OH by Fact 4.0. z∈S, so z∉MLR (Proposition 4.2). The equalities are S081 Theorem A and Corollary A1. For the complexity bound: validity is Π⁰₂, so ε*, the true runs, the weights and the bounds L_e are ∅″-computable. S is a Π⁰₁(∅″) class and O is Σ⁰₁(∅″), so S∖O is a nonempty Π⁰₁(∅″) class, and its leftmost path is ∅‴-computable. ∎

**How the S081 §7 obstruction is bypassed.** (i) *Independence.* There is no random background x and no placement of windows relative to x. The fixed coordinates are chosen by the potential, and z is selected afterwards, by compactness, from the null closed set S. (ii) *Blind fill bets on fixed content.* The value of each fixed bit is chosen so as not to increase the weighted expected capital over all completions of the unfixed coordinates, at a time when every active strategy has already read that coordinate except on a set of small capital-weighted mass (Lemma 3.1). This is precisely a content-selection rule compatible with a small c.e. family: the family is the 2^{i+1} guessed runs of Proposition 4.2. Late revelation is replaced by finite Π⁰₂ guessing. S081's single-sentinel normal form (A2) appears here as the one-coordinate split bound of Lemma 3.1.

## 5. Robustness under all computable finite-block recodings

Let OH^{blk} := {z : K(z)∈OH for every computable finite-block recoding K}. The identity is such a recoding, so OH^{blk} ⊆ OH. S070's OH^{lin3} requires robustness only under computable blockwise GL(3,F₂) sequences, so OH^{blk} ⊆ OH^{lin3}. Every computable fair-coin homeomorphism preserves R₂ (S033), so R₂ ⊆ OH^iso ⊆ OH^{blk}.

**Theorem 5.1.** OH^{blk}∖MLR ≠ ∅. More precisely, there is z∉MLR such that K(z) is computably random and lies in OH for every computable finite-block recoding K. In particular H(z), H⁻¹(z) and every intermediate of the S078 chain built from z lie in OH, and z∈OH^{lin3}.

*Proof.* Repeat §4 with an enumeration of triples (K_e, T_e, θ_e). Validity now also requires a total computable block presentation of K_e, a partition of ℕ into finite blocks, and total canonical indices of bijections κ_j. This is still an arithmetical condition (Π⁰₂ for totality, Π⁰₁ for the partition and bijection conditions given totality), and the guessing in Proposition 4.2 needs only that it is a property of indices. The strategy is G_e := F_{T_e}∘K_e. Lemmas 2.1–2.4 hold verbatim.

Stage (b) changes only in the choice of candidates. Let A be the active set. Choose K₀ = {k_1<…<k_{N_i}} greedily: k_1 := a, and k_{r+1} := the least number > k_r lying outside every block, of every partition K_e with e∈A, that contains one of k_1,…,k_r. Each block is finite and computable, so K₀ is computable. Let n be 1 + the maximum of all these blocks, and τ″ := max(τ, max_{e∈A} c_e(n)). For each e∈A the elements of K₀ lie in pairwise distinct K_e-blocks contained in [0,n), so Lemma 3.2 gives Σ_{k∈K₀} γ^e(σ,k,τ″) ≤ Ψ^e(σ,τ″). Propositions 4.1–4.3 then go through unchanged.

The result is z∉MLR such that, for every valid triple, the savings capital along F_{T_e}(K_e(z)) is bounded. This covers every one-hole scan of K(z) (including the identity scan, so K(z)∈CR) for every computable finite-block recoding K. The named recodings are of this form: H and H⁻¹ (blocks of size 3, matrices A and A⁻¹), S078's R, Q, S and their products, and blockwise GL(3,F₂) sequences. ∎

**Corollary 5.2 (what potential-built witnesses cannot do).** A sequence built by the §4 method can be made robust, simultaneously, under every computable finite-block recoding. So no witness of H-nonpreservation, and in particular no witness of R₂⊊OH obtained through blockwise recodings (S033 Corollary 4, S070, S078), arises from sparse potential-controlled fixing alone. A separation witness z∈OH∖R₂ must exploit structure that one-hole raw scans cannot reach. Two candidates are recodings without bounded-block structure (unbounded coded holes, §6.2 Example E3) and genuinely non-scan globally ≤2-to-1 maps (§6.3). Theorem 5.1 does **not** show that OH is H-invariant, and it decides neither U(H) nor the committed X.

## 6. The general criterion and its boundary

### 6.1 A cheap-coordinate criterion

**Theorem 6.1.** Let 𝒱 be a class of strategies (G_e, d_e) indexed by an arithmetically defined set V of indices. The G_e are total computable λ-preserving maps and the d_e rational computable martingales, uniformly partial computable in e. Suppose there are a constant M and a uniform procedure with the following property. Given finitely many e∈V, positive rational weights, a partial assignment σ, numbers a, t₀ and N, the procedure halts with a time t ≥ t₀ and a set K₀ ⊆ [a,∞)∖dom σ of size N such that

  Σ_{k∈K₀} Σ_e w_e γ^e(σ,k,t) ≤ M·Σ_e w_e Ψ^e(σ,t).

Then there is z∉MLR on which no strategy in 𝒱 succeeds. If 𝒱 contains the identity scans with all rational computable martingales, then z is moreover computably random.

*Proof.* As in §4, with N_i := 2^{i+4}ℓ_iM and with the procedure in place of the frontier search. Only the existence of the true runs, the invariant, the counting bound on V_i and the compactness argument are used. ∎

Instances: one-hole scans (M=1, Lemma 3.1), h-hole scans (M=h), and one-hole scans of computable finite-block recodings (M=1, Lemma 3.2), together or separately. Theorems 4.4 and 5.1 are the corresponding cases.

### 6.2 Three boundary examples

**E1 (unbounded width; the bound fails).** Let T read z_0, then all odd coordinates if z_0=0, and all even coordinates ≥ 2 if z_0=1. T is a total computable no-repeat scan with infinitely many holes on every transcript. For σ=∅ and every k≥1, k stays unread forever on one of the two branches. So γ(∅,k,t) ≥ (capital-weighted mass of that branch) for all t, and Σ_{k∈K₀} γ grows linearly in |K₀|. No constant M exists. This does not show that such strategies defeat the construction. It shows only that the potential accounting, as it stands, uses bounded width essentially. It is consistent with QST-0001 being open (§7.3).

**E2 (a 2-to-1 map; one-time neutralization).** Let D(z)_i := z_i⊕z_{i+1}. D is total computable, λ-preserving and exactly 2-to-1, with fibres {z, z̄}. Every output prefix of length m has exactly two compatible source prefixes of length m+1, and they differ in every coordinate. With σ=∅, every coordinate splits on every output, so γ(∅,k,m) = Ψ(∅,m) for every k. Once a single coordinate is fixed, at most one fibre point is σ-consistent, and γ(σ,k,m) = 0 for all k. The criterion fails at σ=∅, but the cost is paid once and is then neutralized.

**E3 (an unbounded coded hole).** Let D′ be the computable fair homeomorphism D′(z)_0 = z_0, D′(z)_i = z_i⊕z_{i−1}. Its inverse is the prefix parity. A one-hole scan of D′(z) holding virtual coordinate q knows z_k for k<q, and knows z_{≥q} only up to complementing the whole tail. So s^{σ,k}=1 exactly when q ≤ k and no fixed coordinate lies in [q, ·) within the determined range. Every candidate above a long-held q is split. The one-coordinate bound of Lemma 3.2 fails for D′, but a split is neutralized as soon as any fixed coordinate lies at or above q. The cost of fixing k is then the capital-weighted mass of holds strictly between the last fixed coordinate and k, so it depends on the order of fixing. Whether this order-dependent accounting can be closed for all computable fair homeomorphisms, which would give OH^iso∖MLR ≠ ∅, is not settled.

### 6.3 Globally ≤2-to-1 maps: the counting potential and the exact gap

Let G be total computable and λ-preserving with all fibres of size ≤ 2. Let c_G be the computable monotone function of P4-S007: for m ≥ c_G(n), every output prefix of length m has at most two compatible n-prefixes. For a finite *tracked set* P ⊆ [0,n), a partial assignment σ with dom σ ⊆ P, and an output string w, let

  κ^σ_P(w) := #{u∈{0,1}^P : u extends σ↾P and u = z↾P for some z∈G⁻¹[w]},
  Ψ̃_P(σ,m) := 2^{|σ|} Σ_{w∈2^m} 2^{−m} d(w) κ^σ_P(w).

**Proposition 6.2 (counting potential).**
(i) Ψ̃_P(σ,m+1) ≤ Ψ̃_P(σ,m).
(ii) For k∈P∖dom σ: ½(Ψ̃_P(σ_0,m)+Ψ̃_P(σ_1,m)) = Ψ̃_P(σ,m) exactly.
(iii) For m ≥ c_G(n): Ψ(σ,m) ≤ Ψ̃_P(σ,m) ≤ 2Ψ(σ,m).
(iv) For k∈[0,n)∖P and m ≥ c_G(n): Ψ̃_{P∪{k}}(σ,m) − Ψ̃_P(σ,m) = 2^{|σ|}Σ_w 2^{−m}d(w)·φ(w), where φ(w)=1 iff κ^σ_P(w)=1 and κ^σ_{P∪{k}}(w)=2 (a **fresh split** at k relative to P), and φ(w)=0 otherwise.
(v) For a one-hole scan G=F_T, with P ⊇ dom σ below the frontier, the fresh-split weight at k equals γ(σ,k,m).

*Proof.* (i) κ(wb) ≤ κ(w), and the argument of Lemma 2.1 applies. (ii) Each counted restriction u has a definite value at k, so κ^{σ_0}_P+κ^{σ_1}_P = κ^σ_P. (iii) For m ≥ c_G(n), κ^σ_P(w) ∈ {0,1,2}, and it is 0 exactly when c^σ(w)=0. (iv) Projection gives κ_P ≤ κ_{P∪{k}} ≤ 2, and κ_P=0 forces κ_{P∪{k}}=0. (v) A restriction to P∪{k} is ambiguous only through the single unread coordinate. ∎

So in counting form, fixing a tracked coordinate is free, and all cost moves to *tracking*. For ≤2-to-1 maps the cost of tracking k is the weight of current ambiguity cohorts whose difference set Δ (between the two compatible n-prefixes) avoids P and contains k. Persistent cohorts are double fibres. Transient cohorts are the P4-S007 phantoms, whose disagreement can recur further and further out. A cohort is neutralized once P meets Δ.

**The exact remaining gap for R₂.** A proof of R₂∖MLR ≠ ∅ by Theorem 6.1 in counting form needs a computable tracking schedule with summable fresh-split charges for every finite family of globally ≤2-to-1 strategies. Two obstacles were identified. (a) The transient fresh-split weight at a tracking time converges, without computable modulus (cf. S038), to the persistent double-fibre part. (b) The fixing values that minimize the potential can concentrate not-yet-tracked double-fibre mass: for any one fixing the untracked persistent weight is preserved only on average. So a bound on the total persistent charge needs an augmented potential that is itself computable. Neither obstacle was resolved. **R₂∖MLR ≠ ∅ is not established.**

## 7. Consequences for the north star

### 7.1 The certification gate

S080 Corollary 7(a) showed that any proof of R₂⊊OH, and any refutation of U(H), must exhibit a computably random non-MLR member of OH. Theorem 4.4 supplies one, so this necessary condition is now met. A separation witness must in addition lie outside R₂. Corollary 5.2 shows that the §4 method alone, run against blockwise recodings, cannot produce such a witness. S080 Corollary 7(b), the route "OH=MLR ⇒ R₂=OH and U(H)", is now closed: OH ≠ MLR. S081's remark that OH_h=MLR would answer QST-0001 is likewise moot.

### 7.2 The new landscape

  MLR ⊊ OH = OH_h = R_k^scan (all h≥1, k≥2),  OH^{blk}∖MLR ≠ ∅,  KLR ⊆ TKLR ⊆ OH,
  MLR ⊆ R₂ ⊆ OH^iso ⊆ OH^{blk} ⊆ OH^{lin3} ⊆ OH ⊊ CR.

Since MLR ⊊ OH, exactly one of the following holds:
* **(α) R₂ = MLR.** Then R₂ ⊊ OH, and the north star is decided negatively. The same holds for R_fin.
* **(β) MLR ⊊ R₂ ⊊ OH.**
* **(γ) R₂ = OH.** Then R₂∖MLR ≠ ∅.

So **deciding whether R₂∖MLR is empty is now a sharp sub-question of the north star**. Emptiness would settle it. Non-emptiness is necessary for R₂=OH but not sufficient. §6.3 isolates what the potential method still needs in order to show non-emptiness.

The S070 equivalence (H-preservation of OH ⟺ OH^{lin3}=OH) and the S078 single-shear criterion are unchanged. Theorem 5.1 shows only OH^{lin3}∖MLR ≠ ∅, which bears on neither side of that equivalence.

### 7.3 Kolmogorov–Loveland calibration

Theorem 4.4 says nothing about TKLR∖MLR or KLR∖MLR. Example E1 shows that the potential accounting fails for strategies of unbounded postponement width. That is exactly the freedom KL strategies, and the half-splitting technique, use. It is not claimed that the Theorem 4.4 witness lies in TKLR or outside it. QST-0001 is untouched, and no openness or difficulty inference is drawn.

### 7.4 Committed objects and U(H)

Y, M, H and X are untouched. WAR ⊆ CR∖OH (S011), so the Theorem 4.4 and 5.1 witnesses are not wtt-autoreducible. They say nothing about U(H), whose counterexamples, if any, must lie in WAR. U(H), X∈OH and fixed-S preservation remain UNRESOLVED.

## 8. Finite audit

`phase4/P4-S082_POTENTIAL_AUDIT.py` checks the finite components exactly, in rational arithmetic, by enumerating all transcripts up to length 9:
* Lemmas 2.1 and 2.2: 360 monotonicity and 400 domination checks on random one-hole, two-hole and identity scans with savings-transformed hash-seeded stakes and random partial assignments;
* Lemma 2.3: 109 exact refinement identities;
* Lemma 3.1: 40 summed-split-weight bounds, with factor h for two-hole scans;
* Lemma 2.4: 300 random paths satisfying X_{t′} > X_t − 2, plus a winning path checked to be unbounded;
* Lemma 3.2 and the recoded Lemmas 2.1–2.3: 216 monotonicity checks, 24 exact identities and 24 cost bounds for one-hole scans of blockwise GL(3,F₂) recodings, including the committed A; the audit also checks that |GL(3,F₂)| = 168;
* a finite run of the §4 stage loop with an identity scan and three one-hole buffer scans, recording Φ after each stage (all < 2) and finding a completion on which the weighted capital stays below 2 at every time up to the horizon;
* Example E1 (summed split weight 25/8 > Ψ = 1) and Example E2 (every coordinate split at σ=∅; zero split weight after one fixing).

The audit prints `ALL P4-S082 AUDITS PASS`. It supports only finite identities and inequalities on truncations. Validity guessing, Π⁰₂ correctness, the Martin-Löf test, compactness, computable randomness and OH membership rest on the written proofs.

## 9. Failed, superseded or deferred routes

* **S081 §7 sparse late-revealed windows over an independent random background.** Superseded, not repaired: both obstruction halves are artifacts of using an independent background (§4, last paragraph).
* **Direct use of Kastermans–Lempp.** Their notions are partial and non-adaptive. Neither inclusion with OH is available, so their theorems do not yield Theorem 4.4. Only their method is adapted.
* **Extension to all globally ≤2-to-1 maps (R₂∖MLR).** Not completed. The exact gap is recorded in §6.3.
* **Extension to all computable fair homeomorphisms (OH^iso∖MLR).** Not completed. Example E3 shows order-dependent neutralization accounting is needed.
* **Attacker–defender variant for a separation z∈OH with H(z)∉OH.** A heuristic attempt was made: fix bits in favour of one virtual one-hole scan while keeping raw potentials bounded. It met the counterfactual-simulation obstacle: a raw scan holding one raw coordinate of the virtual hole can evaluate the virtual strategy under both raw completions. Gains are free of raw cost only at self-confirming blocks (S047-style two-branch structure). Nothing is claimed.
* **Record-only proof of z₀∈OH; finite price/escrow/hazard/renewal work; residue tables; unit-column enumeration; multi-hole variants.** Not attempted, as instructed. Theorem 4.4 uses one-hole scans only; the h-hole remark in Lemma 3.1 is a by-product.

## 10. Disposition

**Proved.**
* The consistency-potential lemmas 2.1–2.4 for arbitrary total computable fair maps.
* The one-hole and block-recoded cost bounds (Lemmas 3.1, 3.2).
* **Theorem 4.4: OH∖MLR ≠ ∅ (certification gate PASSED)**, with a witness z ≤_T ∅‴.
* Theorem 5.1: OH^{blk}∖MLR ≠ ∅, with H(z)∈OH and z∈OH^{lin3}.
* Theorem 6.1: the cheap-coordinate criterion.
* Proposition 6.2: the counting potential for globally ≤2-to-1 maps.
* The trichotomy of §7.2.

**Recorded.** SRC-0069 and SRC-0070 with their access levels; THM-0077 and THM-0078 from SRC-0069.

**Unresolved.** R₂=OH (north star), R₂=OH^iso, R₂ vs MLR, OH^iso vs MLR, U(H), X∈OH, fixed-S preservation, H-invariance of OH, TKLR∖MLR, QST-0001.

**Frozen.**
* All P4-S001–S081 results, including S008, S011/S012, S027 clipping, S033, S037, S070–S081, and S057 (exact four paired clipped traces, prospective deadlines, genuine fillers, t/u zero-stake timeout release, mandatory non-s sweep without old-sentinel reset, seven 8/7 versus one ZERO; NOT invoked).
* The original Y/M/H/X.
* PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged.
* Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED.

No novelty, openness, prior-art, publication or outreach claim is made. No owner or external blocker.

**Next: P4-S083.** Decide R₂ versus MLR (§7.2). Either extend the potential method to all globally ≤2-to-1 total maps, closing the §6.3 gap and proving R₂∖MLR ≠ ∅, or prove R₂ = MLR, which would give R₂⊊OH. The separation route (z∈OH with a winning non-scan k=2 map or non-block homeomorphism) is the alternative target.
