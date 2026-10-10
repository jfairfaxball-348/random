# P4-S089 VALIDATION — halving survivor theorem, two-frame structure, spectral barrier, no local frustration

Date 2026-10-10. Scope: Phase 4 mathematics only.
* Incoming GitHub main SHA `0009e00dff9d75b70539e513e544f4b89b8040f4`, read with `git ls-remote origin refs/heads/main`.
* Its commit parent is `c820588…`, the P4-S087 outgoing SHA, and `0009e00…` is the P4-S088 atomic close commit. Reconciled with the P4-S088 close record.
* No P4-S089 file existed on entry; P4-S089 is unused.

**Lemma 1.2 — PASS.**
* (i) Monotonicity uses only shrinking cells and the martingale identity, for any clopen P and C.
* (ii) Domination is pointwise.
* (iii) The identity c^{P∩C} + c^{P∖C} = c^P + s^{P,C} is pure logic. The weights α and 1−α exactly cancel the normalizations λ(P∩C)⁻¹ and λ(P∖C)⁻¹. No freshness or independence of C is needed.
* (iv) Compactness of the decreasing cells gives the eventual value s_∞ with no width modulus. The limit bound is dominated convergence with majorant 2+B_∞ (E[B_∞] ≤ 1).

**Theorem 1 (halving survivor) — PASS.**
* *Definition 1.3.* The condition is stated relative to the capital-weighted pair mass inside P plus λ(P). The proof shows that the pair mass is < 3λ(P) along true runs:
  * λ(Pair) ≤ λ(P) by fairness;
  * E[B_∞1_{Pair}] ≤ λ(P)·lim_tΨ(P,t) by monotone convergence;
  * Σw_e ≤ ½ and Φ < 2.
* *Halting.* Halting follows from dispersibility with ε_i/8, Lemma 1.2(iv), and monotonicity of Γ in t. The search is over single clopen candidates with a decidable balance test.
* *Invariant.* Each repetition adds ≤ ε_i = 2^{−(i+4)}/ℓ_i. Over a stage: 2 − 2^{−(i−1)} + 2^{−(i+2)} + 2^{−(i+4)} = 2 − (27/16)2^{−i}.
* *ML test.* Each split keeps at most ¾ of λ(P). With ℓ_i = 5(i+1), λ(P^ε_i) ≤ (¾)^{5(i+1)} < 4^{−(i+1)}, because (¾)⁵ = 243/1024 < ¼. So λ(V_i) ≤ 2^{−(i+1)} ≤ 2^{−i}.
* *Compactness and conclusion.* Verbatim S082 Proposition 4.3 and Lemma 2.4(iii), with clopen P*_i as in P4-S088 Theorem C.
* *Quantifier audit.* ∃z ∀ strategies of 𝒱. Wrong-guess runs may diverge.
* *Instances.* The instance claim for P4-S087 Theorem 4 and P4-S088 Theorem C is checked: the candidate-tuple excess bounds give min_k γ_∞ ≤ (pair mass + small)/N, which is Definition 1.3.

**Proposition 2 — PASS.**
* (a) δ⁰ has initial pair (1, 1⊕a₁) and δ¹ has (0,1). Both satisfy the recursion from j = 2, so they lie in S(a), and they are independent. Translations by functions of unchanged controls commute and add.
* (b) The control-flip computation gives ε_p = b_{p−1} and then the unchanged recursion. Data flips give δ^q. Compositions stay inside S_W(a), because the window controls never change.
* (c) T_W is parametrised by the below-window incoming state, and T′_W by (δ′_{J−1}, δ′_J), a function of the coordinates below 2J. Both are linear in the parameter, hence groups of order four. Pointwise invariance reduces to fibrewise translation by S_W(a), resp. S′_W(b). The stationary law of the K_mix state chain is uniform on its three states.
* The audit (Part 2) checks (a)–(c) on all 2¹⁴ inputs.

**Lemma 3.1, Lemma 3.2, Theorem 3 — PASS.**
* *Causal maps.* Causal maps are closed under composition and inversion. Partner involutions of fixed-hold scans after causal frames are causal. For involutions, c_i(ψ_iv) = c_i(v), so M_n is self-adjoint.
* *Decomposition.* The level decomposition is the martingale-difference decomposition of the coordinate filtration, and each W_{n+1} is invariant.
* *Theorem 3(i).* Fresh exact halvings lie in ⨁_{n≥a}W_{n+1}.
* *Theorem 3(ii).* The orbit state P is invariant. The low part (functions on O ⊥ 1_O) and the fresh part are M-invariant and orthogonal. η₀ > 0 because a finite connected orbit graph has a simple eigenvalue 1. The bound ⟨g,Mg⟩ ≤ (1−η′)‖g‖² with ‖g‖² ≥ ¾λ(P) gives (3/8)η′λ(P).
* *Theorem 3(iii).* With d ≡ 1, μ = 2λ. Fairness converts output separation into input separation inside the invariant P, giving (9/4)η′λ(P) on the left against 7ελ(P) on the right.
* *Scope.* Theorem 3 is unconditional, but its hypothesis (a uniform signed-level gap) is verified for no explicit family. That is Conjecture R for the three-core.

**Lemma 4 and Corollary 4.1 — PASS.**
* The exact recursion m_{n+1} = m_n − 2^{−n}|F_{{w}}(n)| gives Σ ≤ 1 per automorphism. A frustrated closed walk is a word fixing v with odd section product at level n.
* The conclusion is correctly limited: local certificates fail. Nothing is claimed about whether a global gap exists.

**Corollary 5.1 and Proposition 5.2 — PASS, correctly conditional.**
* Corollary 5.1 is stated only under Conjecture R. U₀, U₁ and U′₀ are in FD₂^{K_mix} or FD₂^{K′_mix} (P4-S088). Each preserves CR (THM-0038 after a computable fair homeomorphism, then deletion of one coordinate). The text states that the barrier concerns the mechanism, not survival.
* Proposition 5.2(i) is set monotonicity.
* (ii) uses the limit t → ∞ of Ψ for d ≡ 1 and an all-double map with fixed partner: Ψ_∞ = λ(P∪ψP)/λ(P) = 2 − π(P).
* (iii) is Theorem 3(ii).

**Experiment record — CORRECTLY LABELLED.**
* E1–E5 are floating-point computations on finite truncations. They are labelled EXPERIMENT and support only Conjecture R, which is explicitly OPEN.
* The recorded values were checked against the raw outputs. One transcription range was corrected before commit: levels 12–20 lie in [0.9737, 0.9762].
* Audit Part 6 reproduces E3 at levels 7–12 and E4 at levels 5, 6, 8 and 11 to within 10⁻⁴.

**Routes — CORRECTLY LABELLED.**
* §6.1–6.3 are analyses. (A′), (B′) and (C′) are explicitly not closed.
* The §6.3 obstruction is stated as an obstruction to one design, not as an impossibility theorem.

**Finite audit — PASS.**
* `python3 phase4/P4-S089_HALVING_AUDIT.py` prints `ALL P4-S089 AUDITS PASS` (143,921 checks, ≈2 s). Parts 1–5 are exact.
* `python3 phase4/P4-S088_COSET_AUDIT.py` still prints `ALL P4-S088 AUDITS PASS`.
* These cover finite truncations only.

**Evidence and guard audit — PASS.**
* No source was fetched and no access level changed. No expander or strong-ergodicity literature was used. The almost-invariance vocabulary is programme mathematics, proved or labelled.
* Only already-catalogued THM-0038 (via P4-S003/S088) is used.
* R_tot = MLR remains a programme deduction.
* The original Y/M/H/X and all S001–S088 results are frozen, and S057 is not invoked.
* R₂ versus MLR, R₂ versus OH^iso, R₂ versus R₂^{cdz}, U(H), X ∈ OH and fixed-S preservation are unresolved and kept separate.
* PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged.
* Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED.
* No novelty, openness, priority, publication or outreach claim. No owner/external blocker.
