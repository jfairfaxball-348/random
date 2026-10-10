# P4-S087 CLOSE — dispersed survivor and the E₀-breaking frontier

Date 2026-10-10. Phase 4 Mathematics ONLY.

**Entry checks.**
* Incoming independently pinned remote main: `7435c93ec127f4fc2527a883917fb90784db4464`. This is the P4-S086 atomic close commit; its parent `453439b…` is the P4-S085 outgoing SHA.
* P4-S087 files were absent and the session was unused at entry.
* Session branch: `claude/p4-s087-two-observer-dxy96o`.

**Result.** R₂ versus MLR is NOT decided; neither Route A nor Route B closed. Proved:
* **Theorem 4 (dispersed survivor).** One z ∈ CR∖MLR survives EVERY width-two fair map whose double fibres a.s. have density-zero (in particular, finite) difference sets. The quantifier order is ∃z∀G over an infinite, non-rank-one class.
* **Corollaries 6–7.** No family contained in a single computable frame's DZ₂^J is universal. One graded frame contains every one-hole scan of every K∘D′ʲ(z), so every T∘D′, together with all raw and block-recoded scans.
* **Theorem 8.** R₂ ⊊ R₂^{fd}, via the tail-coded F_{T*}∘D′ ∉ FD₂.
* **Proposition 9 and Lemma 10.** Homeomorphism closure of R₂^{fd}, and symmetric fibre weights for finite-difference maps.
* **Frontier.** R₂ versus MLR now lies exactly at E₀-breaking (non-dispersible) binary ambiguity, present in every computable frame.
* Written validation is in `phase4/P4-S087_VALIDATION.md`. The finite audit `phase4/P4-S087_DISPERSION_AUDIT.py` prints `ALL P4-S087 AUDITS PASS`.

**Not proved.**
* R₂ = MLR or MLR ⊊ R₂.
* A universal width-two pair or family.
* A survivor for all of F₂.
* The frame-straightening question.
* No quantifier swap of S086 is claimed.

**Frozen.**
* All S001–S086 mathematics and the original Y/M/H/X.
* Literature at recorded access levels; nothing was fetched.
* PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged.
* Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED.

No novelty, openness, priority, publication or outreach claim. Owner/external blocker: NONE.

**Atomic close mechanism.** One commit on the session branch with parent the verified P4-S086 main. It is pushed, then fast-forwarded non-force onto main, and the remote `refs/heads/main` is independently re-read. The outgoing SHA is the hash of this close commit; a commit cannot embed its own hash. Next: P4-S088.

## Full copy-ready P4-S088 prompt (identical to authoritative/NEXT_SESSION_PROMPT.md)

# P4-S088 — The E₀-breaking frontier: frame straightening or a homeomorphism-closed survivor

Continue the Fairfax-Ball Randomness Research Programme at https://github.com/jfairfaxball-348/random. Run ONLY Phase 4 Mathematics session P4-S088.

Independently pin live remote main to the P4-S087 outgoing commit, reconcile its exact SHA against P4-S087 closeout and validate P4-S088 uniqueness. Review P4-S001–S087, emphasizing S003–S008, S011–S012, S032–S033, S081–S087, S087 validation/closeout and audit, CAND-01, Gate-3 PASS, both Phase-4 pivots and SRC-0015, SRC-0019, SRC-0060, SRC-0069–SRC-0072 at their RECORDED access levels.

Freeze MLR=R_tot ⊆ R_fin ⊆ R_k ⊆ R₂ ⊆ OH^iso ⊊ OH^blk ⊆ OH^lin3 ⊆ OH=OH_h=R_k^scan ⊊ CR (k≥2); R₂⊊OH, MLR⊊OH, KLR⊆TKLR⊆OH. R_tot=MLR remains a programme deduction from SRC-0071's inspected preprint. Freeze S084's predictable-error theorem, ML-null infinite-resolution locus and balanced a.e. two-sheet destroyer; S085's c(n) criterion (representation only); S086's ∀F∃x pullback survivor and rank-one/common-factor no-go.

Freeze P4-S087. Its Lemma 2 is an excess bound: limsup_t(Σγ−Ψ) ≤ 2^|σ|E[(2+B_∞)(f_∞−1)^+], with no width modulus and with the time searched. Its Theorem 4 (dispersed survivor) gives ONE z∈CR\MLR with G(z)∈CR for EVERY width-two G whose double fibres a.s. have density-zero difference sets (DZ₂ ⊇ FD₂). Corollaries 6–7 say that no family contained in a single computable frame's DZ₂^J is universal. That covers, in the graded frame J_f (f(i)=⌊√i⌋), every one-hole scan of every K∘D′ʲ(z), so every T∘D′ including S083's T*. Theorem 8 gives R₂⊊R₂^fd via a tail-coded destroyer F_T*∘D′∉FD₂. Proposition 9: R₂^fd is closed under homeomorphisms whose inverse preserves E₀, but not under D′. Lemma 10: FD₂^J maps have symmetric fibre weights. R₂ versus MLR remains OPEN and is now located exactly at E₀-breaking (non-dispersible) binary ambiguity, present in every frame. Do not repeat S085, S086 or S087 as the next result.

OVERRIDING TARGET: prove R₂=MLR or construct z∈R₂\MLR. Work at the E₀-breaking frontier with one of the following, or a stronger alternative:

(A) Settle frame straightening for finite families. Is every finite family in F₂ contained in one computable frame's FD₂^J or DZ₂^J? If yes, NO finite family of width-two observers is universal for CR\MLR. If no, give an explicit pair (or finite family) not co-dispersible in any computable frame, and test whether such a pair can be universal. Lemma 10 (asymmetric positive-measure weights) is one possible obstruction; first decide whether F₂ admits positive-measure asymmetric double loci at all.

(B) Construct a survivor against a family that is closed under, or at least not co-dispersible in any frame for, enough computable fair homeomorphisms to contain every frame-transported tail code T∘D′∘J. Minimal cases are OH^iso\MLR, or the two-generator core {raw scans}∪{scans after D′ and after D′⁻¹ in incompatible frames}. Meet S084's whole-error-stream requirement for every infinitely resolving T*.

(C) Otherwise, prove a non-tautological GLOBAL impossibility theorem showing that the S087 dispersed-survivor method, or any potential/fixing method with guessable choices, cannot defeat some explicit E₀-breaking family, and identify that family. Do not substitute a filtration equivalence, a finite toy audit, an a.e. entropy estimate, the ∀F∃x fact, or a re-proof of S087 in a new frame.

Preserve the original computably random Y, unchanged globally use-clipped self-avoiding wtt autoreduction M, repeated three-bit H with A=[101;110;111], X=H⁻¹(Y), and all S001–S087 results. Keep R₂=OH^iso, U(H), X∈OH and fixed-S preservation separate. No escrow, hazards, residues, unit columns, record-only z0 or multi-hole detours. No novelty, openness, priority, publication or outreach claims. PA-0001 and DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED.

Close per docs/SESSION_PROTOCOL.md: validate and synchronize STATE.json, gate ledger, decisions, blockers and failure ledger. Make one atomic session-branch commit, push it, and non-force fast-forward/merge into main; independently verify the outgoing remote main SHA. Unless an owner/external blocker exists, embed the FULL copy-ready P4-S089 prompt verbatim in both the close record and the final report, identical to authoritative/NEXT_SESSION_PROMPT.md.
