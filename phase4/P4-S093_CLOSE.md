# P4-S093 close — orientation is autoreducibility; GOL calibrated; left-c.e. window criterion; category and forcing obstructions

Date: 2026-10-11. Phase 4 Mathematics ONLY.

**Entry.** Independently pinned main `96b3a8a496de5994bb141f2cd0131b5db69a065c` (the S092 atomic close), sole parent `ec2c6ff1b5050b1b324d10b007843b1336bd7010`. No open or closed pull requests. The remote side branches are historical; `phase4/P4-S092-wip` holds superseded scratch. There was no S093 file or branch at entry. The incoming prompt is archived verbatim as `phase4/P4-S093_INCOMING_HANDOFF.md`, SHA256 `a7c8a6ed5ed8bb4f3be62bb2da35911d33159e6ff048912fe8ab4f1c497b6a6b`; it equals the committed prompt up to stripped markdown markers. Session branch: `claude/r2-mlr-global-orientation-wsout9`, the designated development branch for this session.

**Outcome: R₂ versus MLR NOT decided after a sustained attempt through all six internal gates.**

* **Lead route (equality).** Theorem A: S092's Global Orientation Lemma in a frame K (coverage or race form) holds for z exactly when K(z) is Turing autoreducible. So GOL ⟺ (AR-cover): every z∈CR∖MLR is Turing autoreducible after some computable fair homeomorphism. Every computably random source with an autoreducible frame image lies outside OH^iso, so R₂∩AR^iso=∅.
* **Calibration.** Corollary A3: GOL ⇒ OH^iso=MLR ⇒ Rute's automorphism randomness = endomorphism randomness = MLR. This is part of QST-0002, recorded SOURCE-STATED OPEN in 2016; no later status check was made. Any all-correct-orientation proof of equality must decide it; a non-orientation F₂ mechanism need not.
* **Left-c.e. instance.**
  * L1: larger-candidate bets are sound in every frame.
  * L2/L3: with any computable precision N(h)≥h+1, destruction ⟺ infinitely many reached upper holds skipping a 2^{−N(h)} partner window. This strictly weakens S092's whole-interval jump-over requirement, and MLR sources land at almost every reached upper hold at every precision.
  * A Solovay-measure exclusion of landing was found void for every non-computable source.
  * L4: frame transfer of monotone orientation reaches only Δ⁰₂ sources, and CR∖MLR has sources ≡_T∅″.
  * The Δ⁰₂ window-skip property remains open.
* **Counterexample search.** Lemma G: every AR(K,Φ) is meager and 2-generics avoid AR^iso. Lemma M: CR∖MLR is meager in itself, so category alone cannot refute GOL.
* **Opposite route (separation).** The first milestone is z∈CR∖MLR∖AR^iso, which refutes GOL. Proposition F (pairing forcing) reduces its cost to a specified-side bias, which can equal 1 in one step (all-in example in the tail-coded frame). Proposition S (conditional sketch): the Amortized Specified-Side Cost Lemma (ASSCL) would give such z. ASSCL is UNPROVED; its obstruction is protected self-readers aligning their bets with the construction's own forcing windows. Full survival additionally needs every S084/S087–S091 obligation.

**Smallest remaining global obligations.**
* *Equality:* (AR-cover), which also decides the automorphism-randomness part of QST-0002, or a non-orientation F₂ destroyer for every CR∖MLR source.
* *Separation:* ASSCL or any z∈CR∖MLR∖AR^iso robust against self-reading protected strategies, then full F₂ survival.

**Validation.** Written adversarial self-review (P4-S093_VALIDATION.md). `phase4/P4-S093_AUTOREDUCIBILITY_AUDIT.py`: 72,834 exact checks PASS. Frozen audits re-run PASS: S092 103,286; S091 79,893; S090 92,802; S089 143,911 (its numerical Part 6 skipped, numpy/scipy unavailable). No Lean, independent agent, external review or hosted CI success claimed. Finite audits supplement the written proofs.

**Literature.** Two bounded web searches. New catalogue records SRC-0073 (Hölzl–Janicki, arXiv:2303.11986) and SRC-0074 (Barmpalias–Fang–Merkle–Titov, arXiv:2603.26484) are ABSTRACT_INSPECTED calibration only; no proof depends on them. An autoreducibility search returned only metadata-level hits, which were not used and are logged.

**Synchronization.** The following agree on S093 completed and S094 next: STATE, START_HERE, AGENTS, README, ROADMAP, STATUS, phase4/README, gate ledger, decision log, session ledger, failure ledger and catalogue/search log. The full S094 prompt below is byte-identical to authoritative/NEXT_SESSION_PROMPT.md. Candidate and prior-art records and all previous numbered mathematics are unchanged.

**Frozen.**
* The incoming landscape; no class relation is added beyond recording the already-catalogued automorphism randomness ⊆ OH^iso.
* The S084–S092 results and their theorem/experiment distinctions; the exact frames, including K′_mix's preceding-control offset.
* The original Y/M/H/X; source access levels of existing records.
* PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged.
* Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED.
* No novelty, external openness, priority, publication or outreach claim. Owner/external blocker NONE.

**Delivery.** One atomic session commit with `96b3a8a496de5994bb141f2cd0131b5db69a065c` as sole parent, published on the session branch; main fast-forwarded non-force. The outgoing SHA is verified by independent remote reads and reported in the final report (a commit cannot contain its own hash).

## Full copy-ready P4-S094 prompt (identical to authoritative/NEXT_SESSION_PROMPT.md)

# P4-S094 — Resolve R₂ versus MLR: autoreducibility cover or a source outside every autoreducible frame image

Continue the Fairfax-Ball Randomness Research Programme at https://github.com/jfairfaxball-348/random. Execute ONLY Phase 4 Mathematics session P4-S094, upon a fresh owner invocation of this prompt. Do not execute S095.

## Mandate and scope

Genuinely attempt to resolve the central target:

  R₂=MLR, OR construct z∈R₂∖MLR.

The intended deliverable is a complete proof of one alternative. A partial lemma, restricted class, obstruction to one construction or reformulation is an intermediate result to apply immediately, not a preselected endpoint. The owner's sustained-attempt authorization continues: multiple internal proof gates, successive lemmas, constructions, repairs and changes of route are authorized within S094. Continue through dependent obligations while a concrete route remains; do not defer a reachable next step to S095 merely because an intermediate result is recordable.

These are internal mathematical gates, not programme phase gates. Phase 4 remains OPEN; Phase 5 remains CLOSED. No publication or outreach. Never declare a missing lemma true, hide an assumption or manufacture a resolution.

## Entry and authority

Independently pin live remote main. Reconcile the S093 atomic close (its outgoing SHA is in the S093 final report; it is the commit whose message begins "P4-S093") and its sole parent `96b3a8a496de5994bb141f2cd0131b5db69a065c` (the S092 close). Inspect any later changes and live branch/PR/check evidence; confirm S094 has not been executed.

Read repository authority, docs/SESSION_PROTOCOL.md, CAND-01, Gate-3 PASS, both Phase-4 pivots and cumulative S001–S093 outcomes. Emphasize S011–S012, S081–S093, S082 §§2–6, S083 §3, S084, S087 §6, S089 §5, S092 §§2–5, and S093 mathematics, validation, audit and close. Archive this exact incoming prompt before replacing NEXT_SESSION_PROMPT.md.

Use SRC-0015, SRC-0019, SRC-0028, SRC-0060, SRC-0069–SRC-0074 only at their RECORDED access levels; do not upgrade by recollection. SRC-0071's journal version remains METADATA_ONLY; SRC-0073 and SRC-0074 are ABSTRACT_INSPECTED calibration only. R_tot=MLR remains the programme deduction from SRC-0071's inspected preprint. Any new literature retrieval must be recorded with its access level and must not be used for priority or openness claims.

## Frozen starting mathematics

MLR=R_tot ⊆ R_fin ⊆ R_k ⊆ R₂ ⊆ OH^iso ⊊ OH^aff ⊊ OH^blk ⊆ OH^lin3 ⊆ OH=OH_h=R_k^scan ⊊ CR (k≥2, h≥1);
MLR ⊊ R₂^{cdz} ⊆ R₂^{dz} ⊆ R₂^{fd}; R₂ ⊊ R₂^{cdz} ⊊ R₂^{fd}; R₂^{cdz} ⊆ OH^aff∩OH^blk;
R₂⊊OH, MLR⊊OH, KLR⊆TKLR⊆OH, OH^aff⊆OH^lin3, and Rute's automorphism randomness ⊆ OH^iso.

Preserve S084's entire computably random predictable-error-stream requirement, ML-null infinite-resolution locus and balanced a.e. double-fibre destroyer; S085's representation-only c(n); S086's ∀F∃x and common-factor obstruction; all S087–S092 results with their theorem/experiment distinctions; the exact frames K_mix and K′_mix, including K′_mix's PRECEDING-control offset. Conjecture R remains UNRESOLVED; its numerics are EXPERIMENT only.

Challenge these S093 results before relying on them, without spending the session re-proving them:

* **Theorem A (orientation is autoreducibility).** For every source z and computable fair homeomorphism K, the S092 GOL hypotheses in frame K (coverage or race form) hold iff K(z) is Turing autoreducible. Hence GOL ⟺ (AR-cover): every z∈CR∖MLR is Turing autoreducible after some computable fair homeomorphism. Every computably random z with an autoreducible frame image lies outside OH^iso, so R₂∩AR^iso=∅.
* **Corollary A3.** GOL ⇒ OH^iso=MLR ⇒ Rute's automorphism randomness = endomorphism randomness = MLR (part of QST-0002, recorded SOURCE-STATED OPEN in 2016; no later status check). An equality proof through all-correct orientation must decide this; a non-orientation F₂ mechanism need not.
* **Propositions L1, L2, L4; Corollary L3.** For left-c.e. sources, bets on the lexicographically larger hold completion are always correct in EVERY frame. In the raw frame with any computable level N(h)≥h+1, destruction ⟺ infinitely many reached holds with α_h=1 at which no approximation lands in the 2^{−N(h)}-window of the partner. MLR sources land at almost every reached upper hold at every computable precision. Measure (Solovay) exclusion of landing is void for non-computable sources. Frame transfer of monotone orientation reaches only Δ⁰₂ sources, while CR∖MLR has sources ≡_T∅″.
* **Lemmas G and M.** Every AR(K,Φ) is meager and 2-generics avoid AR^iso; but CR∖MLR is meager in itself, so category alone cannot produce a GOL counterexample.
* **Proposition F and the conditional Proposition S.** Pairing forcing makes any self-avoiding Φ wrong inside any hold-invariant clopen state; its cost is split weight plus a specified-side bias, which can equal 1 in one step (all-in example in the tail-coded frame). If the Amortized Specified-Side Cost Lemma (ASSCL, identity-frame protection) holds, some z∈CR∖MLR lies outside AR^iso and GOL fails. ASSCL is UNPROVED; its obstruction is protected self-readers aligning their bets with the construction's own forcing windows.

These are established starting results subject to a documented correction if an actual proof error is found.

## Proof gate 1 — State the exact theorem that would finish the problem

For equality, prove ∀z∈CR∖MLR ∃G∈F₂ ∃computable martingale d: d succeeds on G(z), preserving the quantifier order. Two admissible routes:

* (AR-cover), i.e. GOL, which by Corollary A3 also decides the automorphism-randomness part of QST-0002; or
* a non-orientation destroyer: fractional rather than all-correct orientation, or non-scan F₂ maps with genuinely E₀-breaking or asymmetric double fibres.

For separation, prove ∃z∉MLR ∀G∈F₂: G(z)∈CR for the SAME z, exposing effectivity and oracle use; its first necessary milestone is z∈CR∖MLR∖AR^iso (equivalently: GOL is false).

Write a short dependency plan for the chosen direction and identify the genuinely missing global implication. Choose on mathematical grounds.

## Proof gate 2 — Build a candidate all the way to its decisive obstruction

If pursuing equality:

* Attack (AR-cover) directly: from an arbitrary ML test failed by z, construct a computable fair homeomorphism and a self-avoiding reduction, or prove that for some z every derived Solovay test (ψ_h(V_{n(h)}))_h is failed by z for every V, K, n.
* Alternatively build a fractional-orientation or non-scan destroyer, proving totality, fairness and the fibre bound on EVERY transcript and actual unbounded capital, with repeated false readings handled by restart or selection accounting.
* For the left-c.e. Δ⁰₂ instance, prove or refute the window-skip property using only computability facts you prove or that are catalogued at adequate access.

If pursuing separation:

* Prove ASSCL or replace it. Specify states, requirements, schedule and invariant; every effective choice must be Σ⁰₁ or explicitly guessed; separate validity information from what a computable observer can use.
* Defeat protected self-readers that simulate the guessed runs and align their bets with the forcing windows. Possible tools: hiding the forcing windows behind guess-dependent decoys of bounded measure cost, amortized taxation that the self-reader cannot anticipate, or a different forcing mechanism.
* Then extend from (¬AR-cover) towards full survival: S084 error streams, fractional one-hole strategies in every frame, non-commuting partner families (three-involution core, K_mix with K′_mix, tail-coded frames together) and non-scan F₂ maps.

## Proof gate 3 — Attack the obstruction, then repair the argument

Formulate the strongest plausible lemma the full theorem needs, try to prove it, and actively search for counterexamples to its quantified statement. If it fails, identify exactly which hypothesis failed and attempt a substantive repair that neither assumes the conclusion nor excludes the hard sources. Do not stop at another reformulation, bounded-defect theorem, frame calculation or restricted-class destroyer; apply it immediately to eliminate the route or to force a stronger construction.

## Proof gate 4 — Cross the full-family quantifier

For separation: survival for EVERY F₂ map and EVERY output martingale with all convergence, compactness, effectiveness and scheduling claims proved. Survival of selected frames, or non-autoreducibility alone, is a milestone, not membership in R₂.

For equality: coverage of EVERY CR∖MLR source with a precise coverage theorem. An obstruction to one construction is not evidence for a survivor. Keep the current gap explicit; a conditional equivalence earns a resolution only when its missing condition is proved.

## Proof gate 5 — Give the opposite alternative a serious attempt if the lead route stalls

If the lead route remains blocked after substantive repair, use the failure to attack the other direction and carry it to its own decisive global obligation. Do not trade ∃z∀F for ∀F∃z. Inability to prove one side is not evidence for the other. If a common obstruction blocks both mechanisms, state its precise scope and try to bypass it.

## Proof gate 6 — Adversarially validate the proposed resolution

If either target (or the GOL/¬GOL milestone) appears proved, assemble a self-contained proof from the exact definitions, auditing every quantifier, limit, source-selection dependence, effectivity claim and all-transcript obligation, including exceptional paths, repeated false predictions and conditioning on arbitrarily small states. Use exact computation or formalisation where it addresses a concrete proof risk; finite checks never establish universal coverage or randomness of an infinite witness. If no resolution is achieved, report honestly the strongest proved result, the failed attempts and repairs, and the smallest remaining GLOBAL obligation. No novelty, external openness or priority claim.

## Preserved boundaries and closeout

Keep R₂ versus OH^iso, U(H), original X∈OH and fixed-S preservation separate from the central target. Preserve original CR Y, unchanged globally use-clipped self-avoiding wtt M, repeated three-bit H with A=[101;110;111], and X=H⁻¹(Y). No escrow, hazard, residue, unit-column, record-only z₀ or multi-hole detours; no spectral numerics, local frustration certificates or stand-alone operator reformulations. Do not re-prove S085–S093 with changed constants, another frame, another bounded defect or another restricted reader class as the session result.

PA-0001 and DEF-0020 unchanged; Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No publication or outreach.

Close per docs/SESSION_PROTOCOL.md. Validate and synchronize state, current pointers, gate ledger, decisions, blockers and failure ledger. Distinguish proved, conditional, refuted and unresolved obligations, and identify whether the full target was actually decided.

Make one atomic S094 session-branch commit, push it, non-force fast-forward/merge into main, and independently verify outgoing remote main and its parent. Unless an owner/external blocker exists, embed the FULL copy-ready P4-S095 prompt verbatim in both the close record and final report, identical to authoritative/NEXT_SESSION_PROMPT.md. Its task must follow the actual outcome; if the target is resolved, do not pretend it remains open. STOP after S094; do not execute S095.
