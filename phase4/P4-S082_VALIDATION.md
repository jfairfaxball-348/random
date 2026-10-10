# P4-S082 VALIDATION — consistency potentials; certification gate passed

Date: 2026-10-10. Incoming live main was independently verified with `git ls-remote origin refs/heads/main` as exactly `a6557f24867e48f5ac018f9865896993e74cc443`, the P4-S081 outgoing SHA. The `phase4/` tree had 81 complete mathematics/validation/close triplets and zero P4-S082 files, so P4-S082 is unique. Selected CAND-01, Gate-3 authority and both Phase-4 pivots are unchanged. The incoming prompt is byte-identical to `authoritative/NEXT_SESSION_PROMPT.md`.

**PASS:**
* §1 calibration: SRC-0069 and SRC-0070, recorded at their access levels; THM-0077 and THM-0078.
* Lemmas 2.1–2.4: monotonicity, domination, the exact refinement identity, and the savings transform.
* Lemmas 3.1–3.2: the one-hole cost bound and the block-recoded cost bound.
* Propositions 4.1–4.3 and **Theorem 4.4: OH∖MLR ≠ ∅**.
* Theorem 5.1: OH^{blk}∖MLR ≠ ∅, with H(z)∈OH and z∈OH^{lin3}.
* Theorem 6.1 (cheap-coordinate criterion) and Proposition 6.2 (counting potential).
* Examples E1–E3.
* The §7.2 trichotomy.

**NOT** decided: R₂=OH, R₂=OH^iso, R₂ versus MLR, OH^iso versus MLR, U(H), X∈OH, fixed-S preservation, H-invariance of OH, TKLR∖MLR, QST-0001.

1. **Calibration (§1).**
   * SRC-0069: the full author preprint was read. Definitions, Theorems 6–7 and the Section 2 proof were read in full; the Section 3 proof was read in part. The final published venue was not verified and is not recorded.
   * SRC-0070: the DROPS landing-page metadata and abstract were read.
   * Both sources concern non-adaptive strategies with partial stakes. Their classes are incomparable with OH, and Theorem 4.4 is not derived from them.
   * The method debt (expected martingale, average operator, compactness) is stated explicitly, and the adaptation is labelled programme mathematics.
   * No novelty, priority or openness inference is drawn.
2. **Lemma 2.1.**
   * G⁻¹[wb] ⊆ G⁻¹[w] gives c^σ(wb) ≤ c^σ(w).
   * Nonnegativity of d gives d(w0)c(w0)+d(w1)c(w1) ≤ 2d(w)c(w).
   * The proof uses only totality and λ-preservation (λ(G⁻¹[w]) = 2^{−|w|}). No frontier or hole bound is used.
3. **Lemma 2.2.** z∈[σ] witnesses G⁻¹[G(z)↾m]∩[σ] ≠ ∅.
4. **Lemma 2.3.** The union G⁻¹[w]∩[σ] = (·∩[σ_0])∪(·∩[σ_1]) gives c^{σ_0}+c^{σ_1} = c^σ+s^{σ,k} exactly, and the normalization doubles.
5. **Lemma 2.4.**
   * Bank transfers preserve A+B, and before transfers the children's active parts average to A(v). The case d₀(v)=0 is handled.
   * The drop bound comes from B being non-decreasing and A < 2.
   * Boundedness of d forces finitely many transfers, hence A = c·d₀ with c > 0 eventually.
6. **Lemma 3.1.** For a scan, F_T⁻¹[w] is the cylinder of the read coordinates, so a split at k∉dom σ means "k unread". At t ≥ c(n) at most one coordinate below n is unread (h for h-hole scans), by S081 Lemma 2.
7. **Lemma 3.2.** A fully read block determines the raw block through κ_j⁻¹. At most one block below the frontier is not fully read, and candidates lie in pairwise distinct blocks.
8. **Proposition 4.1.**
   * The invariant is stated with ≤ before each stage and < after it. The base case Φ = 0 = 2−2^{1} was corrected from a strict inequality during review.
   * Per repetition: averaging over N_i candidates gives Γ ≤ Φ/N_i < 2/N_i (Lemma 3.1, weighted). The minimizing b increases Φ by at most Γ (Lemma 2.3), and moving time forward never increases Φ (Lemma 2.1).
   * Arithmetic: −2^{−(i−1)} + 2^{−(i+2)} + 2^{−(i+3)} = −(13/8)2^{−i}.
9. **Proposition 4.2.**
   * There are 2^{i+1} guesses of length i+1, each completed run contributing measure 2^{−(i+1)(i+2)}, so λ(V_i) ≤ 2^{−(i+1)²}.
   * Uniform c.e. by dovetailing. Runs on wrong guesses may diverge or halt; neither affects the bound.
   * True runs are nested because stage i depends only on ε↾(i+1).
10. **Proposition 4.3.**
    * O is open. [σ*_i] is a decreasing sequence of compact sets with intersection S, so S ⊆ O gives [σ*_{i₀}] ⊆ O, and compactness gives finitely many witnesses.
    * The savings drop bound (Lemma 2.4(ii)) transfers each witness to every later time.
    * The weighted capital then exceeds 2 everywhere on [σ*_j], so Φ > 2 by Lemma 2.2. This contradicts Lemma 2.1 together with Proposition 4.1.
11. **Theorem 4.4.**
    * Fact 4.0: identity scans give CR, and rational martingales suffice (S012/S081 convention).
    * Lemma 2.4(iii) transfers boundedness from the savings version to the original martingale.
    * Complexity: validity is Π⁰₂ (totality; one-hole ⟺ ∀n∃N by S081 Lemma 2). S∖O is a nonempty Π⁰₁(∅″) class, so its leftmost path is computable from ∅‴.
12. **Theorem 5.1.**
    * Validity of block recodings is arithmetical: Π⁰₂ totality, plus a Π⁰₁ partition check given totality, plus decidable bijection checks per block.
    * The greedy candidate selection is computable and places candidates in pairwise distinct blocks of every active partition.
    * Lemma 3.2 replaces Lemma 3.1, and the rest is unchanged. The identity scan of K(z) gives K(z)∈CR.
    * H, H⁻¹, R, Q, S and products, and blockwise GL(3,F₂) sequences are all computable finite-block recodings.
13. **Theorem 6.1 and Proposition 6.2.**
    * 6.1 only abstracts the cost bound.
    * 6.2(i)–(iii) are the counting analogues of Lemmas 2.1–2.3. Note (iii) needs m ≥ c_G(n) from P4-S007.
    * 6.2(iv): the difference κ_{P∪{k}}−κ_P ∈ {0,1}.
    * 6.2(v) was checked against the scan case: the fresh split at k means k is the held coordinate.
14. **Examples.**
    * E1: each k≥1 is unread forever on one parity branch.
    * E2: fibres {z, z̄} differ everywhere; after one fixed coordinate at most one fibre point is consistent.
    * E3: the prefix-parity inverse makes a virtual hole at q flip every z_k with k≥q.
    * The audit confirms E1 and E2 numerically.
15. **Audit.** `python3 phase4/P4-S082_POTENTIAL_AUDIT.py` prints:
    * Lemmas 2.1, 2.2, 2.3, 3.1 (raw one-hole, two-hole and identity scans): (360, 400, 109, 40) checks PASS;
    * Lemma 2.4 (savings transform): 300 paths PASS;
    * Lemmas 2.1, 2.3, 3.2 (virtual scans through blockwise GL(3,2) recodings incl. A): (216, 24, 24) checks PASS;
    * Finite construction: 4 coordinates fixed; Φ after each stage = 1/16, 3/64, 73/1920, 667413109/17539806080, all < 2; a good completion was found;
    * Example E1: Ψ = 1 and summed split weight 25/8 > Ψ;
    * Example E2: split weight equal to Ψ at σ=∅, and zero after one fixing;
    * ALL P4-S082 AUDITS PASS (about 50 s).

    The audit covers finite truncations only. Its lemma labels were aligned with the record's numbering before the final run.
16. **Adversarial self-review (structured; no multi-agent review was run this session).** Each claim was re-read against attempts to break it:
    * whether Lemma 2.1 needs one-holeness (no);
    * whether a held coordinate can lie above the frontier when Lemma 3.1 is applied (no: candidates are below every active frontier at τ″);
    * whether a wrong guess could corrupt the true run (no: stages depend only on the guess prefix, and wrong runs only add measure inside the 2^{i+1} count);
    * whether the compactness step needs O to be effectively open (no: only openness is used; effectivity is used only for the complexity bound);
    * whether the bounded-width hypothesis is used anywhere besides Lemmas 3.1–3.2 (no; Example E1 shows it is needed there);
    * whether Theorem 5.1 silently claims H-invariance of OH (no; Corollary 5.2 and §7 state the limits).

    Corrections applied: the base case of Proposition 4.1 was made non-strict; the Lemma 2.4(iii) argument was simplified; topic tags were aligned with catalogue vocabulary.
17. **Catalogue.**
    * sources.json gains SRC-0069 and SRC-0070; theorems.json gains THM-0077 and THM-0078; authors.json gains AUT-0076 to AUT-0079, and AUT-0019 and AUT-0039 are linked to SRC-0070.
    * The search-log entry was added.
    * All JSON parses, and formatting round-trips identically.

No earlier result is revised. P4-S081's §7 obstruction is superseded by a different construction, not refuted as stated. The original Y/M/H/X are frozen; S037, S057 (not invoked) and S070–S081 are unchanged. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. Owner/external blocker NONE. No novelty, openness, prior-art, publication or outreach claim.
