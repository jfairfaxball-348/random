# P4-S080 VALIDATION — admissible-model underspecification, GL(3,2) classification, certification gate

Date: 2026-10-09. Incoming live main exactly `670bfaed2351827f8a1f6c57c42574c60f094dd0`; 79 complete earlier triplets and zero P4-S080 files. Selected CAND-01, Gate-3 authority and both Phase-4 pivots unchanged. Reviewed P4-S079 mathematics/validation/close and the controlling S011/S012, S027 §2, S032/S033, S037, S039–S049, S070–S079.

**PASS** for Lemma 1 (chained-substitution spreading), Theorem 2 (admissible model with every block recoding outside OH), Corollary 3 (record-level status of the primary target), Theorem 4 (U(K) on GL(3,F₂)), Proposition 5 and Corollary 5′ (target-only role refutation, universal over autoreductions), Proposition 6 (KLR⊆OH) and Corollary 7 (certification gate and calibration). **NOT a decision of U(H), X∈OH, fixed-S preservation, R₂=OH, R₂=OH^iso or OH=MLR.**

1. *Record scope.* P4-S011 fixes Y and M existentially from SRC-0067/SRC-0068/THM-0076 (abstract/statement access only). P4-S027 §2 describes clipping as a normal form inside that existential witness. No later record adds a hypothesis on Y. The admissibility definition matches exactly what the record uses.
2. *Lemma 1.* τ is a computable bijection: injective by construction, and each stage consumes the current least unused number, so every number is used. The cap gives j>U(i) and k>U(j)≥U(i) (U taken nondecreasing; a larger cap is a valid clip). Hence N(i) never reads j or k, and N(j) never reads k, on every oracle. Substituted values equal the true W-values on V by induction, so M_V is correct on V. M_V reads only coordinates outside its own block on every oracle, and its use is computable. V is a computable coordinate permutation of W, so V∈CR by S001.
3. *Theorem 2.* For any computable blockwise bijection family K, the derived predictor reconstructs the V-blocks of the other blocks and runs the block-avoiding M_V, so it never reads its own block of K(V). S011 then gives a total, computable, no-repeat, fair-coin-preserving, globally one-hole winning scan. In particular H⁻¹(V)∉OH, and every S078 intermediate built from H⁻¹(V) is outside OH. No property of the committed Y is altered.
4. *Corollary 3.* (a) follows because (Y1,M1) satisfies every record hypothesis. (b) is the definition of being established for every admissible choice. (c) uses S011 (WAR∩OH=∅), S033 Corollary 4 and S078 Theorem 2. (d) uses S078 and WAR⊆CR∖OH. The converse of (d) is not claimed.
5. *Theorem 4.* (1) S079 Theorem 2 uses only self-avoidance and target correctness of the autoreduction, so it applies to every admissible pair. (2) WAR is closed under computable coordinate permutations, and OH and its complement in CR are closed under signed permutations (S033 Theorem 5). (3) Exhaustive audit: |GL(3,F₂)|=168; the no-unit-column set equals S₃AS₃, has 18 elements and is closed under inversion; every other matrix has a unit column.
6. *Proposition 5.* The candidate pair is computed without the hidden raw bit. The true candidate is never refuted. Under r-goodness the false oracle agrees with Y' on every coordinate read by the witnessing target computation, which therefore halts with the true bit against the false candidate's complement. Cofinite r-goodness gives an infinite decidable J for S079 Theorem 1. The 1408-case finite audit confirms the in-block bookkeeping. Corollary 5′ is the contrapositive applied to every admissible M2.
7. *Proposition 6 / Corollary 7.* One-hole scan plus martingale is a total computable non-monotonic strategy (DEF-0012). MLR⊆R₂ (S032) puts every element of OH∖R₂ outside MLR. MLR⊆KLR is proved inline via Ville's inequality rather than cited. QST-0001's status is quoted from the catalogue (SOURCE-STATED OPEN, SRC-0018/SRC-0019); P4-S080 makes no openness claim of its own.
8. *Audit.* `python3 phase4/P4-S080_ADMISSIBILITY_AUDIT.py` prints PASS for all four parts. The toy model covers substitution logic and block avoidance on finite truncations only. Infinite-sequence randomness, autoreducibility and one-hole legality rest on the written proofs.
9. *Adversarial re-read.* The toy model's first run failed with a KeyError: synthetic queries reached coordinates outside the finite τ-truncation. That was a truncation artefact, fixed by restricting the queries to covered coordinates. A second run with a quadratic cap built an oversized universe and was stopped. Neither affects the infinite proof, in which τ is a bijection of ℕ. No theorem was revised.

No earlier results revised. Original Y/M/H/X frozen; S037, S057 (not invoked) and S070–S079 unchanged. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. Owner/external blocker NONE. No novelty, openness, prior-art, publication or outreach claim.

## 10. Independent adversarial review before merge (2026-10-09)

Before the merge into `main`, six independent skeptics (workflow run `wf_e0fad3b4-c24`) each tried to refute one claim cluster: Lemma 1/Theorem 2; §1 and Corollary 3; Theorem 4; Proposition 5/Corollary 5′; Proposition 6/Corollary 7; plus a records-integrity critic. **Verdict for every cluster: holds_with_minor_fixes. No refutation, no fatal issue and no mathematical major issue.** One skeptic independently recomputed the GL(3,F₂) facts (168; 18-element no-unit-column coset; inversion and transpose closure; 150 with a unit column). Another independently re-derived the generalized unit-column argument. The records critic re-ran the audit (PASS).

Fixes applied in response:
- **Lemma 1 cap normalization.** A running-maximum cap U'(i)=max(i+1, max_{i'≤i}U(i')) is now stated in the mathematics record. The use bound is corrected to 1+max{τ⁻¹(m): m≤U(k_n)}. The redundant re-clipping is removed.
- **Theorem 2.** Each S078 intermediate is K_i(V) for a blockwise matrix, so the theorem applies directly.
- **§1 and Corollary 3 (precision).**
  - "Established by the record" is replaced by "follows from the record". Deriving X∉OH is exactly proving U(H), and X∉OH is explicitly NOT established.
  - Corollary 3(c) now says what failure of U(H) gives: R₂⊊OH and OH^iso⊊OH, with R₂=OH^iso left open. It no longer says failure "decides the north star".
  - §7: a proof of X∈OH would need a new commitment pinning down Y, and such a commitment can make X∈OH true only if U(H) fails.
- **Theorem 4 proofs.**
  - (1) is restated as a generalized unit-column lemma. S079 Theorem 2's proof uses only self-avoidance on every oracle and target correctness.
  - (2) gives the recomputed computable cap under the permutation π.
  - (3) gives a hand proof: 3·3! = 18, the explicit A⁻¹, and inversion and transpose closure.
- **§4.** Removed the claim that quantification over all autoreductions is new. r-good ⇒ local Case A_r is credited to the contrapositive of S041 Theorem 4 plus S042 Theorem 1, and the cofinite-A_r destruction to S043 Theorem 2 / S042 Theorem 5. Corollary 5′ is strengthened to "infinitely many non-A_r blocks for each r", with the target two-cycles as its observable consequence. "Target two-cycle" is defined, and remote divergence at decisive blocks is distinguished.
- **§5.**
  - Robustness to the partial/total reading of DEF-0012 is stated.
  - Ville's argument now spells out its conventions (frozen capital, nonnegativity, unit initial capital).
  - "Certify" is replaced by "establish that OH contains".
  - The text now notes that KLR⊆OH yields no known non-MLR member, says "affirmative answer to QST-0001", and calls OH=MLR? a one-sided gate (sufficient, not necessary, for R₂=OH).
- **Audit script.** The docstring reference is corrected to Proposition 5. The toy predictor is now genuinely adaptive: the later query list depends on the first answer. Re-run: PASS on all four parts.
- **Records.**
  - The STATUS.md header is updated (it was stale since P4-S079).
  - STATE.json `current_research_target` is updated.
  - The ledger summaries now say "follows from the record … NOT established".
  - NEXT_SESSION_PROMPT.md is corrected and adds a catalogue-only check for total-strategy non-monotonic randomness results; P4-S080_CLOSE.md now embeds it verbatim.
- **Procedural (the two items the critic rated major).** Merge into `main` and embedding the full next prompt in the close record were outstanding. Both are now carried out under the owner's standing closeout direction.

No conclusion changed. U(H), X∈OH, fixed-S preservation, R₂=OH, R₂=OH^iso and OH=MLR remain UNRESOLVED.
