# P4-S089 CLOSE — halving survivor theorem, two-frame structure, spectral barrier and the rigid three-core

Date 2026-10-10. Phase 4 Mathematics ONLY.

**Entry checks.**
* Incoming independently pinned remote main: `0009e00dff9d75b70539e513e544f4b89b8040f4`. This is the P4-S088 atomic close commit; its parent `c820588…` is the P4-S087 outgoing SHA.
* P4-S089 files were absent and the session was unused at entry.
* Session branch: `claude/p4-s089-e0-breaking-efncvi`.

**Result.** R₂ versus MLR is NOT decided, and (A′) is NOT decided. Proved:
* **Theorem 1 (halving survivor theorem).** Any halving-dispersible class of width-two strategies has a common survivor z ∈ CR∖MLR.
  * Halving-dispersible means relatively small capital-weighted separation of the in-state double-fibre pairs by some balanced clopen split, linear or not.
  * The split is found by a single-candidate Σ⁰₁ search. P4-S087 Theorem 4 and P4-S088 Theorem C are instances.
* **Proposition 2.** On fresh windows, FD₂^{K_mix} ∪ FD₂^{K′_mix} acts through two order-four groups of solution-space translations (data by S_W(a), controls by S′_W(b)). The K_mix holds 0 and 1 generate all S(a)-translations.
* **Theorem 3 (spectral barrier).** For causal partner involutions, fresh functions split into signed level operators. A uniform gap forbids almost-invariant balanced splits of orbit states and violates the hypothesis of Theorem 1.
* **Lemma 4 / Corollary 4.1 (no local frustration).** Short frustrated cycles have summable mass, so rigidity of a causal family can only be global.
* **Proposition 5.2 (invariance–neutralization dichotomy).** The absolute neutralization budget is bounded; the normalized one is not, and the minimizing rule favours pair concentration.
* **Corollary 5.1, conditional on Conjecture R.** The two-frame union is not halving-dispersible, via the CR-preserving three-core {U₀, U₁, U′₀}. This is a mechanism barrier only.
* **EXPERIMENT (labelled, not theorems).**
  * Three-core top signed level eigenvalues lie in [0.9737, 0.9762] at levels 12–20.
  * The window-only gap is ≈ 0.077.
  * The three-core has no frustrated cycles of length ≤ 9 at levels 9–14.
  * The dihedral core is non-rigid (eigenvalues 1 or cos(π/L) → 1).
  * Conjecture R is OPEN.
* Validation: `phase4/P4-S089_VALIDATION.md`. The audit `phase4/P4-S089_HALVING_AUDIT.py` prints `ALL P4-S089 AUDITS PASS` (143,921 checks). The P4-S088 audit still passes.

**Not proved.**
* R₂ = MLR or MLR ⊊ R₂.
* Conjecture R.
* A survivor for FD₂^{K_mix} ∪ FD₂^{K′_mix}, for all causal frames, or for OH^iso.
* R₂ ⊊ R₂^{cdz}.
* A universal width-two family.
* A global impossibility for potential/fixing methods.
* No quantifier swap of P4-S086 is claimed.

**Frozen.**
* All S001–S088 mathematics and the original Y/M/H/X.
* Literature at recorded access levels; nothing was fetched, and no expander or strong-ergodicity literature was used.
* PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged.
* Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED.

No novelty, openness, priority, publication or outreach claim. Owner/external blocker: NONE.

**Atomic close mechanism.** One commit on the session branch with parent the verified P4-S088 main. It is pushed, then fast-forwarded non-force onto main, and the remote `refs/heads/main` is independently re-read. The outgoing SHA is the hash of this close commit; a commit cannot embed its own hash. Next: P4-S090.

## Full copy-ready P4-S090 prompt (identical to authoritative/NEXT_SESSION_PROMPT.md)

# P4-S090 — Rigidity or neutralization: prove Conjecture R, or an absolute-accounting survivor, or a readable-neutralization impossibility

Continue the Fairfax-Ball Randomness Research Programme at https://github.com/jfairfaxball-348/random. Run ONLY Phase 4 Mathematics session P4-S090.

Independently pin live remote main to the P4-S089 outgoing commit, reconcile its exact SHA against P4-S089 closeout and validate P4-S090 uniqueness. Review P4-S001–S089, emphasizing S003–S008, S011–S012, S032–S033, S081–S089, S089 validation/closeout and audit, CAND-01, Gate-3 PASS, both Phase-4 pivots and SRC-0015, SRC-0019, SRC-0060, SRC-0069–SRC-0072 at their RECORDED access levels.

Freeze MLR=R_tot ⊆ R_fin ⊆ R_k ⊆ R₂ ⊆ OH^iso ⊆ OH^aff ⊊ OH^blk ⊆ OH^lin3 ⊆ OH=OH_h=R_k^scan ⊊ CR (k≥2); OH^aff ⊆ OH^lin3; R₂⊊OH, MLR⊊OH, KLR⊆TKLR⊆OH; MLR ⊊ R₂^cdz ⊆ R₂^dz ⊆ R₂^fd, R₂ ⊆ R₂^cdz ⊊ R₂^fd, R₂^cdz ⊆ OH^aff ∩ OH^blk. R_tot=MLR remains a programme deduction from SRC-0071's inspected preprint. Freeze S084–S088 as recorded (S084 predictable-error theorem, ML-null infinite-resolution locus, balanced a.e. two-sheet destroyer; S085 c(n) criterion, representation only; S086 ∀F∃x and rank-one/common-factor no-go; all of S087; all of S088 including Theorem C and Proposition D).

Freeze P4-S089.
* Theorem 1 (halving survivor theorem): every halving-dispersible class of width-two strategies (Definition 1.3) has a common survivor z∈CR\MLR. Dispersibility means relatively small capital-weighted separation of the double-fibre pairs inside the state P by some balanced clopen split. The split is linear or not, fresh or not, and is found by a single-candidate Σ⁰₁ search because split weights are non-increasing in time. S087 Theorem 4 and S088 Theorem C are instances.
* Proposition 2: on fresh windows, FD₂^{K_mix} ∪ FD₂^{K′_mix} acts through two order-four groups. These are the control-dependent data translations by the solution space S_W(a) and the data-dependent control translations by S′_W(b). The K_mix holds 0 and 1 generate all S(a)-translations.
* Theorem 3 (spectral barrier for causal frames): partner involutions of fixed-hold scans after causal frames are tree automorphisms. Fresh functions split into signed level operators M_n. A uniform gap ‖M_n‖_top ≤ 1−η (n ≥ a) forces average separation ≥ η/2 for fresh exact halvings and ≥ (3/8)min(η,η₀)λ(P) for every balanced split of an orbit state, and so violates Definition 1.3.
* Lemma 4 / Corollary 4.1 (no local frustration): for finitely many causal maps, Σ_n λ(F_W(n)) ≤ |W|. Rigidity of a causal family can only be a global expander phenomenon.
* Proposition 5.2 (invariance–neutralization dichotomy): separated pairs never return, so absolute neutralization cost is bounded by the initial pair mass. Normalized costs are not bounded, and the minimizing rule keeps the side with larger normalized pair weight.
* Corollary 5.1 (CONDITIONAL on Conjecture R): FD₂^{K_mix} ∪ FD₂^{K′_mix} is not halving-dispersible, via the CR-preserving three-core {U₀,U₁,U′₀}. So the (A′) mechanism alone cannot give a survivor for the union; this is a mechanism barrier, not a survival barrier.
* EXPERIMENT only (not theorems): E1–E5. The three-core's top signed level eigenvalues lie in [0.9737,0.9762] at levels 12–20 (gap ≈ 0.024–0.026), with no frustrated cycles of length ≤ 9 at levels 9–14. The dihedral core {ψ₀,ψ′₀} has eigenvalues 1 or cos(π/L) with L = 8,…,128 → 1. Conjecture R (uniform gap for the three-core at levels ≥ n₀) is OPEN.

R₂ versus MLR remains OPEN. It now sits at the invariance–neutralization dichotomy for rigid nonlinear ambiguity: near-invariant splits are excluded by rigidity, and neutralizing splits are what self-reading observers read. Do not repeat S085–S089 as the next result.

OVERRIDING TARGET: prove R₂=MLR or construct z∈R₂\MLR. Work with one of the following, or a stronger alternative:

(R) Decide Conjecture R by a GLOBAL argument (Corollary 4.1 rules out local frustration certificates). Examples: a renormalization or self-similarity recursion for the signed level operators of the finite-state transducers K_mix, K′_mix; a comparison with a structure of known gap, proved or cited at a recorded access level; or an explicit refutation by almost-invariant fresh halvings at high levels. If proved, record the unconditional barrier for the two-frame union. Then immediately use it in (N) or (I); a gap proof alone is not the target.

(N) Absolute-accounting survivor. Build a survivor construction whose potential charges each double-fibre pair at most once in ABSOLUTE terms (Proposition 5.2(i)), with every choice Σ⁰₁ or guessable. Handle first the rigid fixed-hold core, then infinitely resolving self-reading observers in both K_mix and K′_mix frames. Meet S084's whole-error-stream requirement for every infinitely resolving observer. Identify exactly where the counting-potential obstacles of S082 §6.3 and S087 §6.2 enter, and overcome or isolate them.

(I) Readable-neutralization impossibility (Route A / B′). Prove that every guessed-run construction with Σ⁰₁ split choices makes its neutralizations readable to some width-two self-reading observer whose dominant partner group is rigid (for example S083-type tail readers after K_mix and K′_mix). That is a non-tautological GLOBAL impossibility for potential/fixing methods. Then test whether such observers form a universal family for CR\MLR.

(C) Alternatively prove R₂⊊R₂^cdz with a destroyer that defeats the beacon-mimic obstruction of P4-S089 §6.3.

Do not substitute: more numerics or a finite toy audit; a filtration or spectral reformulation; a re-proof of Theorem 1 or S087/S088 in a new frame; fixed-hold or other CR-preserving maps presented as destroyers; or the ∀F∃x fact. Any literature on expanders, almost-invariant sets or strong ergodicity may be consulted only with recorded access levels and no novelty/openness/priority inference.

Preserve the original computably random Y, unchanged globally use-clipped self-avoiding wtt autoreduction M, repeated three-bit H with A=[101;110;111], X=H⁻¹(Y), and all S001–S089 results. Keep R₂=OH^iso, U(H), X∈OH and fixed-S preservation separate. No escrow, hazards, residues, unit columns, record-only z0 or multi-hole detours. No novelty, openness, priority, publication or outreach claims. PA-0001 and DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED.

Close per docs/SESSION_PROTOCOL.md: validate and synchronize STATE.json, gate ledger, decisions, blockers and failure ledger. Make one atomic session-branch commit, push it, and non-force fast-forward/merge into main; independently verify the outgoing remote main SHA. Unless an owner/external blocker exists, embed the FULL copy-ready P4-S091 prompt verbatim in both the close record and the final report, identical to authoritative/NEXT_SESSION_PROMPT.md.
