# P4-S088 CLOSE — asymmetric loci, translation pairs and the countable-coset survivor

Date 2026-10-10. Phase 4 Mathematics ONLY.

**Entry checks.**
* Incoming independently pinned remote main: `c820588d2936d1a6fe28cee84fca86699e65610a`. This is the P4-S087 atomic close commit; its parent `7435c93…` is the P4-S086 outgoing SHA.
* P4-S088 files were absent and the session was unused at entry.
* Session branch: `claude/p4-s088-e0-breaking-b8ccnj`.

**Result.** R₂ versus MLR is NOT decided. Proved:
* **Theorem A.** F₂ admits positive-measure asymmetric double loci: the explicit G_asym has exact weights ¼, ¾ on a closed set of measure ≈ 0.5776.
  * FD₂ frame straightening therefore fails for a single map (via P4-S087 Lemma 10).
  * G_asym is harmless (P4-S003 clopen split), and a diluted copy lies in DZ₂.
* **Theorem B.** For every computable frame J, some CR-preserving translation-pair map G_c (a one-hole scan after a linear frame) lies outside DZ₂^J. Every finite set of translation pairs straightens linearly. Co-dispersibility in one frame is not the right invariant.
* **Theorem C.** One z ∈ CR∖MLR survives EVERY width-two map whose difference vectors occupy countably many cosets of the density-zero subgroup (CDZ₂).
  * The class contains DZ₂, FD₂^K and all one-hole scans after every computable affine K, and every T∘D′∘J for affine J (S083's T*∘D′ included).
  * It is not co-dispersible in any single frame. The mechanism is frame-free: fresh parities annihilate all dominant difference cosets.
* **Corollaries.** R₂^{cdz}∖MLR ≠ ∅; R₂^{cdz} ⊊ R₂^{fd}; OH^{aff}∖MLR ≠ ∅; OH^{aff} ⊊ OH^{blk}; no family inside one CDZ₂^J is universal; the S084 error-stream requirement is met on all affine frames.
* **Proposition D.** An explicit nonlinear two-frame instance (K_mix, K′_mix) with atomless difference cosets, at which both survivor mechanisms stop. It is a mechanism result only: its fixed-hold witnesses preserve CR.
* **Frontier.** R₂ versus MLR is now located at nonlinear (uncountable-coset) E₀-breaking ambiguity in every frame.
* Written validation is in `phase4/P4-S088_VALIDATION.md`. The finite audit `phase4/P4-S088_COSET_AUDIT.py` prints `ALL P4-S088 AUDITS PASS` (92,724 checks). The P4-S087 audit still passes.

**Not proved.**
* R₂ = MLR or MLR ⊊ R₂.
* R₂ ⊊ R₂^{cdz}.
* A survivor for FD₂^{K_mix} ∪ FD₂^{K′_mix}, or for OH^iso.
* A universal width-two family.
* Single-map DZ₂-straightening.
* No quantifier swap of P4-S086 is claimed.

**Frozen.**
* All S001–S087 mathematics and the original Y/M/H/X.
* Literature at recorded access levels; nothing was fetched.
* PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged.
* Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED.

No novelty, openness, priority, publication or outreach claim. Owner/external blocker: NONE.

**Atomic close mechanism.** One commit on the session branch with parent the verified P4-S087 main. It is pushed, then fast-forwarded non-force onto main, and the remote `refs/heads/main` is independently re-read. The outgoing SHA is the hash of this close commit; a commit cannot embed its own hash. Next: P4-S089.

## Full copy-ready P4-S089 prompt (identical to authoritative/NEXT_SESSION_PROMPT.md)

# P4-S089 — Nonlinear E₀-breaking ambiguity: almost-invariant halvings or a rigid universal family

Continue the Fairfax-Ball Randomness Research Programme at https://github.com/jfairfaxball-348/random. Run ONLY Phase 4 Mathematics session P4-S089.

Independently pin live remote main to the P4-S088 outgoing commit, reconcile its exact SHA against P4-S088 closeout and validate P4-S089 uniqueness. Review P4-S001–S088, emphasizing S003–S008, S011–S012, S032–S033, S081–S088, S088 validation/closeout and audit, CAND-01, Gate-3 PASS, both Phase-4 pivots and SRC-0015, SRC-0019, SRC-0060, SRC-0069–SRC-0072 at their RECORDED access levels.

Freeze MLR=R_tot ⊆ R_fin ⊆ R_k ⊆ R₂ ⊆ OH^iso ⊆ OH^aff ⊊ OH^blk ⊆ OH^lin3 ⊆ OH=OH_h=R_k^scan ⊊ CR (k≥2); OH^aff ⊆ OH^lin3; R₂⊊OH, MLR⊊OH, KLR⊆TKLR⊆OH; MLR ⊊ R₂^cdz ⊆ R₂^dz ⊆ R₂^fd, R₂ ⊆ R₂^cdz ⊊ R₂^fd, R₂^cdz ⊆ OH^aff ∩ OH^blk. R_tot=MLR remains a programme deduction from SRC-0071's inspected preprint. Freeze S084's predictable-error theorem, ML-null infinite-resolution locus and balanced a.e. two-sheet destroyer; S085's c(n) criterion (representation only); S086's ∀F∃x pullback survivor and rank-one/common-factor no-go; all of P4-S087 (excess Lemma 2, dispersed survivor Theorem 4, Corollaries 5–7, R₂⊊R₂^fd, Proposition 9, Lemma 10).

Freeze P4-S088.
* Theorem A: an explicit G_asym ∈ F₂ has a positive-measure double locus with exact weights ¼, ¾. So FD₂ frame straightening fails for a single map, yet G_asym preserves CR via S003's clopen split, and a diluted copy lies in DZ₂.
* Theorem B: for every computable fair homeomorphism J some translation-pair map G_c (fibres {x, x⊕c}, a one-hole scan after a linear frame, CR-preserving) lies outside DZ₂^J. Every finite set of translation pairs straightens linearly.
* Theorem C: ONE z∈CR\MLR has G(z)∈CR for EVERY G∈CDZ₂, the maps whose double-fibre difference vectors occupy countably many cosets of the density-zero subgroup 𝒵. CDZ₂ contains DZ₂, FD₂^K and all one-hole scans after every computable affine K, and every T∘D′∘J for affine J, including S083's T*∘D′. It is not co-dispersible in any single frame. The mechanism fixes fresh parities annihilating all dominant difference cosets at once.
* Corollaries: R₂^cdz\MLR≠∅, R₂^cdz⊊R₂^fd, OH^aff\MLR≠∅, OH^aff⊊OH^blk, and no family inside one CDZ₂^J is universal.
* Proposition D: for the explicit nonlinear causal frames K_mix and K′_mix (controls on even/odd coordinates; data recoded by b′_j=b_j⊕b_{j−2}⊕(1⊕a_j)b_{j−1}), one-hole scans have atomless difference cosets mod 𝒵, so they lie outside CDZ₂. No fresh parity is jointly invariant for the pair, and neither natural frame co-disperses it. The fixed-hold witnesses are themselves CR-preserving, so D concerns mechanisms only.

R₂ versus MLR remains OPEN and is now located at NONLINEAR (uncountable-coset) E₀-breaking ambiguity in every frame. Do not repeat S085–S088 as the next result.

OVERRIDING TARGET: prove R₂=MLR or construct z∈R₂\MLR. Work with one of the following, or a stronger alternative:

(A′) Decide the explicit two-frame instance. Is there one z∈CR\MLR surviving every map in FD₂^{K_mix} ∪ FD₂^{K′_mix} (infinitely resolving, self-reading observers in both frames included)? A positive answer should come from a genuine mechanism: effective, fresh, approximately invariant clopen halvings under the finitely many dominant partner involutions K⁻¹∘flip_q∘K of all active observers. These are Følner-type almost-invariant sets; recall that two involutions generate a dihedral group. Then extend the mechanism to all one-hole scans after all causal computable fair homeomorphisms, and ultimately to OH^iso\MLR. Meet S084's whole-error-stream requirement for every infinitely resolving T* in every such frame.

(B′) Otherwise, construct an explicit nonlinear family whose partner-involution groups have a quantitative rigidity (spectral-gap / strong-ergodicity-type) property. Prove that it defeats every potential/fixing method with guessable choices: a non-tautological GLOBAL impossibility theorem for that family. Then test whether such a family is universal for CR\MLR (Route A), for instance by destroying the Theorem C witnesses.

(C′) Alternatively, prove R₂⊊R₂^cdz by an S083-type self-reading observer in a nonlinear frame against the Theorem C construction. Handle the probabilistic (≥¼) per-constraint separation and the S083 Lemma 3.6 resolution step on the witness class.

Do not substitute a filtration equivalence, a finite toy audit, an a.e. entropy estimate, the ∀F∃x fact, a re-proof of S087/S088 in a new frame, or frame-straightening of CR-preserving maps. Any literature on almost-invariant sets or strong ergodicity may be consulted only with recorded access levels and no novelty/openness/priority inference.

Preserve the original computably random Y, unchanged globally use-clipped self-avoiding wtt autoreduction M, repeated three-bit H with A=[101;110;111], X=H⁻¹(Y), and all S001–S088 results. Keep R₂=OH^iso, U(H), X∈OH and fixed-S preservation separate. No escrow, hazards, residues, unit columns, record-only z0 or multi-hole detours. No novelty, openness, priority, publication or outreach claims. PA-0001 and DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED.

Close per docs/SESSION_PROTOCOL.md: validate and synchronize STATE.json, gate ledger, decisions, blockers and failure ledger. Make one atomic session-branch commit, push it, and non-force fast-forward/merge into main; independently verify the outgoing remote main SHA. Unless an owner/external blocker exists, embed the FULL copy-ready P4-S090 prompt verbatim in both the close record and the final report, identical to authoritative/NEXT_SESSION_PROMPT.md.
