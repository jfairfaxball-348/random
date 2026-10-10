# P4-S083 VALIDATION — tail-coded holes; north star decided negatively (R₂ ⊊ OH)

Date: 2026-10-10.

* **Pin.** Incoming live main was independently verified with `git ls-remote origin refs/heads/main` as exactly `d789bf0e0b743f9c49c6419d6fffe2639d74c060`, the P4-S082 outgoing SHA. The session branch `ccr-dd3e14c4-j9pfu2` was at the same commit.
* **Uniqueness.** `phase4/` had complete P4-S001–S082 records and zero P4-S083 files, and every repository mention of P4-S083 named it as the next session. P4-S083 is therefore unique.
* **Authority.** Selected CAND-01, the Gate-3 authority and both Phase-4 pivots are unchanged. The incoming prompt is `authoritative/NEXT_SESSION_PROMPT.md`.

**PASS:**
* §1 calibration: SRC-0060 (§10), SRC-0071, SRC-0019 and SRC-0072 at their recorded access levels, and Proposition 1.1 (programme deduction, R_tot = MLR).
* Lemma 2.1 (tail-coded hole).
* Lemmas 3.1–3.6, Proposition 3.7, **Theorem 3.8**.
* Corollaries 4.1–4.3 and Remarks 4.4–4.5.
* The §5 landscape and the §7.1 analysis.

**DECIDED:** the north star R₂ = OH is false, and R₂ ⊊ OH.
**NOT decided:** R₂ versus MLR (the primary target of the incoming prompt), R₂ versus OH^iso, OH^iso versus MLR, R_fin versus R₂, U(H), X∈OH, fixed-S preservation, block-H invariance of OH, TKLR∖MLR, QST-0001.

1. **Calibration.**
   * *SRC-0060.* Section 10 of the arXiv v4 text was read in full, including the proof of Theorem 10.4.
   * *SRC-0071.* The full v9 text was read, with the proofs of Lemmas 3.1–3.3. The journal version is METADATA_ONLY: its existence and coordinates come from the reference list of SRC-0019, and its identity with the preprint was not verified.
   * *SRC-0019.* Already catalogued (TCS 2025), so it was upgraded rather than duplicated. A first draft of the record had assigned it a new ID; this was corrected before commit.
   * *SRC-0072.* Abstract only.
   * *Proposition 1.1.* The conversion from a sequence-set strategy to a total computable fair map plus a computable martingale was checked: cells of level i have measure 2⁻ⁱ, each cell splits into exactly two children, μ is additive and d_S = μ/λ. The deduction inherits the source's correctness, and this is stated.
   * *No borrowing and no inference.* No proof in §§2–4 depends on any of these sources. No novelty, priority or openness inference is drawn.
2. **Lemma 2.1.** The telescoping zⱼ = zⱼ₋₁⊕vⱼ gives (i)–(iii) directly. Audit Part 1 checks the identities exhaustively over all hold positions on 400 random 24-bit prefixes (120000 checks).
3. **Lemma 3.1.** S082 Lemma 3.2 needs three properties of K₀: its elements lie outside dom σ, they lie in pairwise distinct blocks of each active partition, and all of those blocks lie below n ≤ every active frontier at τ″. The class restriction preserves all three, because classes are infinite and blocks are finite. Propositions 4.1–4.2 then go through unchanged, and |dom σ^ε_i| = (i+1)(i+2) still holds because each repetition fixes a new coordinate.
4. **Lemma 3.2.**
   * Stage s of a run depends only on the guess prefix of length s+1 and the previous state, so stages below the first disagreement e coincide.
   * Each class C_{ε'↾(s+1)} with s ≥ e is disjoint from every true class: same length forces a difference at e, and different lengths give different indices.
   * Audit Part 2 checks nesting and separation on a toy family (866 checks).
5. **Lemma 3.3.**
   * Totality: each step is a bounded simulation.
   * No repeats: each query is the current q or M, both fresh.
   * One hole: holds increase strictly at each resolution, and fillers are read in order.
   * Fairness: S008.
   * The composite with the homeomorphism D′ keeps fibres ≤ 2.
   * Audit Parts 3–4 check no-repeat, at most one unread coordinate below the filler frontier, and, exactly on all 2¹⁴ raw prefixes, at most two raw preimages per T*-transcript.
6. **Lemma 3.4.**
   * By (Q3), every implied value equals ν, and by Lemma 2.1(ii), x_{F_l}⊕π_{F_l} = v_q for every l. So a wrong prediction forces x_{F_l} ≠ σ'(F_l) for all l, and agreement at one fix forces correctness.
   * Audit Part 3 verifies "wrong ⟺ anti-consistent on all selected fixes" at every one of 3127 toy resolutions.
7. **Lemma 3.5.**
   * Positions inside dom σ*_j carry the true value (Lemma 3.2), which empties the cylinder.
   * Otherwise the r positions are free and the relative measure is 2^{−r}.
   * The sum Σ_{q≥0}Σ_{m≥1}2^m·2^{−(q+2m+4)} = ⅛ is checked exactly in audit Part 5.
   * *Review point.* The true-run prefixes ε' ⊑ ε* are included in the sum. For j below the stage of their fixes they may contribute 2^{−r}, and the bound covers this.
8. **Lemma 3.6.**
   * |dom σ*_{m−1}| = m(m+1), so at most q of these coordinates lie below q, and r(q,m) = q+2m+4 ≤ m(m+1) − q once m² − m ≥ 2q + 4.
   * Consistency is immediate from z∈S.
   * M and the simulation budget both tend to ∞ while q is held.
9. **Proposition 3.7.**
   * The compactness pattern is S082 Proposition 4.3 with an extra open set W, which is open because a wrong resolution is witnessed by a finite virtual transcript, hence by a clopen raw set.
   * With L_e = 2+4/w_e the savings drop gives weighted capital > 4 off W.
   * Domination and Lemma 3.5 give Φ > 4·(7/8) = 7/2, which contradicts Φ < 2. The constants are checked in audit Part 5.
   * *Review point.* Only openness of W is used, not effectivity.
10. **Theorem 3.8.**
    * (ii) uses the triple form of S082 Fact 4.0, as in S082 Theorem 5.1, and the identity scan gives CR.
    * (iii): infinitely many resolutions (Lemma 3.6), all correct (z∉W), so d* is unbounded.
    * (iv): S is Π⁰₁(∅″), O is Σ⁰₁(∅″) and W is Σ⁰₁.
    * *Review point.* On z the fibre of G is a singleton, because T* reads every coordinate of D′(z). This is consistent with S008, which says a CR source destroyed by a scan lies on a singleton fibre.
11. **Corollaries.**
    * 4.1 uses R₂ ⊆ OH (S032) and the explicit map G. It does not need homeomorphism invariance of R₂.
    * 4.2: z∈OH^{blk} and D′(z)∉OH ⊇ OH^{blk}.
    * Consistency with the frozen record: S034 and S077 (finite-support invariance) do not apply, because D′ has infinite support. S070, S078 and S080 concern block H, which D′ is not. S082 Corollary 5.2 predicted that non-block recodings are needed. No frozen result is contradicted.
12. **Audit.** `python3 phase4/P4-S083_SEPARATION_AUDIT.py` prints, in about 7 s:
    * Part 1: 120000 checks PASS;
    * Part 2: 866 checks PASS;
    * Part 3: 3127 resolutions, 2804 correct and 323 fooled. The equivalence holds at all 3127, all 2414 selections of true-run prefixes are correct, and the adversarial completion fooled T* twice, which shows that the exclusion of W is necessary;
    * Part 4: 8192 transcripts, at most 2 preimages;
    * Part 5: series and constants;
    * ALL P4-S083 AUDITS PASS.

    The frozen `phase4/P4-S082_POTENTIAL_AUDIT.py` was re-run and prints ALL P4-S082 AUDITS PASS (about 51 s). The audits cover finite truncations only.
13. **Adversarial self-review (structured; no multi-agent review was run).** Each item below was an attempt to break a claim.
    * *Could a raw one-hole scan replicate T*?* No. A raw hole z_q is separated only by z_q itself, and the S082 candidate rule never fixes a held coordinate. The tail-coded hole is separated by every fix at or above q.
    * *Could T* need the true run?* No. Any qualifying run whose fixes agree with z gives the correct prediction, and a wrong prediction requires full anti-consistency.
    * *Could the true run later fix a fooling position with the anti value?* No: the class separation of Lemma 3.2. The first draft lacked classes, and this case is exactly why classes were added.
    * *Is "q ≤ max dom σ" a problem?* No. T* may hold any q, and every true fix at or above q orients the tail.
    * *Does S082's invariant need candidates in [a, a+N)?* No, only the three properties listed in item 3.
    * *Is the conclusion too strong?* It is stated only for the class-separated construction and does not claim OH^iso∖MLR = ∅ (Remark 4.5(a)).
    * *Does any step use multi-hole scans?* No. *Is the k=2 map's totality global?* Yes, on every input.
    * *Document consistency.* One editorial correction was made: the source IDs for Petrović 2024 were reconciled with the existing SRC-0019.

    No fatal issue was found.
14. **Records synchronized.**
    * `authoritative/STATE.json`, including a new `phase4_s083_tail_coded_separation` entry, catalogue counts, next transition and research target.
    * `authoritative/NEXT_SESSION_PROMPT.md` (P4-S084).
    * SESSION_LEDGER, DECISION_LOG, PHASE_GATE_LEDGER and START_HERE.
    * AGENTS.md checkpoint; README, STATUS and ROADMAP; phase4/README.
    * docs/FAILURE_AND_LESSON_LEDGER.md.
    * catalog/sources.json, theorems.json, definitions.json, questions.json, authors.json and search-log.md.

**Frozen.** P4-S001–S082; original Y/M/H/X; S037; S057 (not invoked); S070–S082. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claim. Owner/external blocker NONE.
