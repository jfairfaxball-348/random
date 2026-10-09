# P4-S081 VALIDATION — bounded-hole collapse, van Lambalgen for OH, sharpened certification gate

Date: 2026-10-09. Incoming live main independently verified with `git ls-remote origin refs/heads/main` as exactly `b8017ed6f3090bcdd5bcbd5f4ceba8058cc7bacf`, the P4-S080 outgoing SHA. The `phase4/` tree had 80 complete mathematics/validation/close triplets and zero P4-S081 files; P4-S081 is unique. Selected CAND-01, Gate-3 authority and both Phase-4 pivots are unchanged. The incoming prompt matches `authoritative/NEXT_SESSION_PROMPT.md`.

**PASS:**
* Step (0) catalogue check: no separation statement found; no openness inference.
* Lemma 2 (computable frontier).
* Theorem A (OH_h = OH for all finite h).
* Corollaries A1–A6.
* Theorem B (x⊕y ∈ OH ⟺ x ∈ OH^[y] ∧ y ∈ OH^[x], uniform relativization) and Corollary B1.

**NOT** a decision of the certification gate (OH∖MLR ≠ ∅), OH=MLR, U(H), X∈OH, fixed-S preservation, R₂=OH or R₂=OH^iso.

1. **Step (0).** Catalogue records inspected at their recorded access levels only; no new retrieval.
   * KL material: DEF-0012, THM-0011 and QST-0001 (SRC-0018, SRC-0019; ABSTRACT_INSPECTED).
   * Endomorphism randomness: DEF-0064 / THM-0071 (SRC-0060; STATEMENT_INSPECTED).
   * CR/MLR records: THM-0014, THM-0002, THM-0015, THM-0020.
   * No record separates total-strategy non-monotonic randomness (or KLR) from MLR. The finding is recorded as an absence in the catalogue, not as evidence of openness.
2. **Lemma 2.** "More than h unread below n" is prefix-closed. König's lemma converts unbounded depth into an infinite transcript with more than h permanently unread coordinates, contradicting the h-hole hypothesis. Search over all 2^N transcripts is effective because T is total computable. Monotonicity is immediate.
3. **Theorem A.**
   * Held intervals are [e_q, r_q] inclusive. This was corrected during review: U_t counts reads before step t.
   * At most h held coordinates are active at once, so first-fit gives a valid h-colouring, and the permanently unread coordinates pairwise overlap and get distinct colours.
   * Each colour scan S_i pulls the other colours at entry. It is total, because only finitely many pulled coordinates are skipped between outputs, and no-repeat. Its unread set is T's colour-i permanent holes, so it is one-hole.
   * F pulls everything held and reads each q by output index 2c(q+1)+h+1, using c(n) ≥ n−h. It is an effective isomorphism (S008 Lemma 2 pattern; S001 / THM-0038), so D_F is bounded on a computably random source.
   * Each positive factor f_s of d along F_T(z) is placed exactly once, in F for fill coordinates or in S_c for colour c. So log d = log D_F + Σ_i log D_i, and an unbounded left side forces some D_i to be unbounded.
   * The proof uses no fact about T's behaviour on z beyond totality and the global hole bound.
4. **Corollaries A1–A3.**
   * A1 combines Theorem A with S032 Lemma 8.
   * A2 is the h=1 case (S_1=T). Its least-unread / increasing / sequential structure follows from |U_t| ≤ 1 and inclusive intervals.
   * A3: width-0 scans are effective isomorphisms, so "no width-0 strategy succeeds" ⟺ z ∈ CR; the rest is Theorem A.
5. **Corollaries A4–A6.**
   * A4 is S079 Theorem 1 with a bounded window in place of the sentinel. The conditional fair bets give factor at least 1+1/(2^h−1) on correct predictions. Never-triggering epochs leave at most h holes; infinitely many triggers plus sweeps leave none.
   * A5 transports a block-avoiding predictor through any computable blockwise bijection family; g_k∘κ_k is nonconstant.
   * A6 is the contrapositive, combined with S080 Corollary 5′.
6. **Theorem B.**
   * ⇐: each one-hole scan of x⊕y induces y-uniform and x-uniform one-hole scans of the halves. They are total on every oracle because every T-transcript reads infinitely many coordinates of each parity. The log-capital splits into even and odd parts.
   * ⇒: a uniformly total y-scan is simulated on x⊕y by reading the needed oracle bits as fresh zero-stake odd coordinates, followed by one odd sweep per x-read. It is one-hole and its capital is unchanged.
   * The non-uniform failure mode is noted in the record's Remark.
   * The theorem is consistent with, and modelled on, THM-0024 (uniformly relative CR) and THM-0021 (MLR), and does not contradict THM-0025.
   * Corollary B1 uses THM-0021.
7. **Audit.** `python3 phase4/P4-S081_COLOURING_AUDIT.py` prints:
   * Theorem A bookkeeping: PASS (60 buffer scans with h ∈ {1,2,3}, 9660 exact factor identities d_T = D_F·Π D_i);
   * Corollary A4 window scan: PASS (20 correct parity windows, capital exactly 2^20);
   * Theorem B even/odd factor split: PASS (40 one-hole scans on joins);
   * ALL P4-S081 AUDITS PASS.

   *Adversarial note.* The first run failed an assertion in the audit itself. The "unread below the frontier" invariant was checked immediately after advancing the simulated T-time, before the scan performed the pulls for coordinates that had just entered. The check was moved to after the pulls, matching the construction's order, and the re-run passes. No mathematical claim changed. The audit covers truncations only. Infinite-transcript hole counts, totality, computable randomness and OH membership rest on the written proofs.
8. **Adversarial self-review (no multi-agent review was run this session).** Each claim was re-read against attempts to break it:
   * whether the colour scans can be stuck forever (no: skips are bounded by pulls);
   * whether a fill coordinate can be pulled (no: pulls are held coordinates only);
   * whether an other-colour held coordinate can reach clause (b) unpulled (no: it is pulled at entry ≤ τ);
   * whether D_F needs z to be read exhaustively by T (no);
   * whether Theorem A secretly needs a non-uniform hole bound (it needs the uniform one; recorded in Remark (3));
   * whether Theorem B's ⇒ survives non-uniform relativization (no; recorded).

   Wording fixes applied: inclusive held intervals; precise width definition in A3; the zero window factor on wrong predictions in A4; an explicit computable sequence (g_k) and a cleaner H-independence statement in A6; THM-0021/THM-0024/DEF-0025 citations in §6.
9. **Failed and deferred routes** are recorded in §§7 and 9 of the mathematics record:
   * the sparse late-window certification, with exact obstruction (i) independence and (ii) blind fill bets on revealed content;
   * left-c.e. one-sided certificates;
   * single-flip-closed local tests (excluded by Theorem A);
   * partial-martingale simulation;
   * filler-order normalization;
   * the unbounded-width extension.

No earlier result is revised. The original Y/M/H/X are frozen; S037, S057 (not invoked) and S070–S080 are unchanged. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. Owner/external blocker NONE. No novelty, openness, prior-art, publication or outreach claim.
