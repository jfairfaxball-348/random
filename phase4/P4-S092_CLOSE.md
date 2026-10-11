# P4-S092 close — orientation reader, global entanglement, one-sided left-c.e. orientation

Date: 2026-10-11. Phase 4 Mathematics ONLY.

**Entry.** Independently pinned main `ec2c6ff1b5050b1b324d10b007843b1336bd7010` (owner handoff amendment, documentation only); sole parent `6633f88ba8a0826442618f5062cb2d74b83c9e86` (S091 atomic close), whose sole parent is `971b3ccef56fc5654c857a32e882342c80e325c2`. No open or closed PRs; zero check runs and commit statuses at the incoming SHA; no S092 file or branch at entry. Incoming prompt archived as `phase4/P4-S092_INCOMING_HANDOFF.md`, SHA256 `d892903904fe352ba9a40d9118be61ea9dd2f57a46a1e70205b0381cf24cdaa0` (identical to the committed prompt apart from a final newline). Session branch: `phase4/P4-S092-mathematics`. During the session an owner-reported usage limit led to scratch commits on `phase4/P4-S092-wip`, made at the owner's instruction; they are superseded by this single atomic close and were never merged.

**Outcome: R₂ versus MLR NOT decided after a sustained attempt through all six internal gates.**

* Lead route (equality): Theorem 1 gives a legal F₂ orientation reader for every computable frame, every uniformly c.e. cylinder family, computable levels and computable bet selection; it destroys a source on a singleton fibre whenever the source is separately covered at every hold while its hold partners are separately covered only finitely often (or the source wins the first-coverage race). Equality therefore follows from the Global Orientation Lemma (GOL), which was neither proved nor refuted.
* Proposition 3: universal ML tests separately cover every partner of every non-MLR source in frames with computable partner onset (raw, D′, K_mix, K′_mix), so GOL needs structurally non-universal families. Lemma 4: entry stages of a CR source into any ML test dominate every computable function, so time-truncated orientation is void.
* One-sided repair: for left-c.e. sources, monotone approximation evidence can certify only the larger completion of a raw hold (Lemma 5.2). The reader destroys such a source iff infinitely many reached 1-bit holds are jump-overs (Proposition 5). Computable randomness excludes early agreement (Lemma 5a), so jump-overs must be late error-halving skips. For left-c.e. MLR sources jump-overs are finite for every computable subsequence (Corollary 5b). Whether left-c.e. CR∖MLR sources have infinitely many jump-overs is OPEN.
* Opposite route (separation): Corollary 2 proves that every z∈OH^iso, hence every z∈R₂, is globally entangled: in every frame, for every c.e. family separately covering it at all levels, its partners are separately covered infinitely often with computably random race outcomes. Applied to guessed-run constructions this forces designed fooling against every frame. Mirror decoys, recognizable centers for non-commuting involutions, and linearization by conditioning were analysed (§5); no survivor construction was completed.

**Smallest remaining global obligations.** Equality: GOL, or any other theorem assigning an F₂ destroyer to every CR∖MLR source; its left-c.e. instance is the late jump-over property. Separation: a globally entangled CR∖MLR source that defeats every F₂ strategy, handling non-commuting partner families by designed fooling or invariance with controlled potential.

**Validation.** Written adversarial self-review (P4-S092_VALIDATION.md). `phase4/P4-S092_ORIENTATION_AUDIT.py`: 103,286 exact checks PASS. No Lean, independent agent, external review or hosted CI success claimed. Finite audits supplement the written proofs.

**Synchronization.** STATE, current pointers, START_HERE, AGENTS, README, ROADMAP, STATUS, phase4/README, gate ledger, decision log, session ledger and failure ledger agree on S092 completed and S093 next. The full S093 prompt below is byte-identical to authoritative/NEXT_SESSION_PROMPT.md. Source, candidate and prior-art records and all previous numbered mathematics are unchanged.

**Frozen.** Incoming landscape (no class relation added), S084–S091 results and theorem/experiment distinctions, exact frames including K′_mix's preceding-control offset, original Y/M/H/X, source access levels, PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE and DEF-0020 unchanged. Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, external openness, priority, publication or outreach claim. Owner/external blocker NONE.

**Delivery.** One atomic session commit with `ec2c6ff1b5050b1b324d10b007843b1336bd7010` as sole parent, published on `phase4/P4-S092-mathematics`; main fast-forwarded non-force; outgoing SHA verified by independent remote reads and reported in the final report (a commit cannot contain its own hash).

## Full copy-ready P4-S093 prompt (identical to authoritative/NEXT_SESSION_PROMPT.md)

# P4-S093 — Resolve R₂ versus MLR: global orientation or a globally entangled survivor

Continue the Fairfax-Ball Randomness Research Programme at https://github.com/jfairfaxball-348/random. Execute ONLY Phase 4 Mathematics session P4-S093, upon a fresh owner invocation of this prompt. Do not execute S094.

## Mandate and scope

Genuinely attempt to resolve the central target:

  R₂=MLR, OR construct z∈R₂∖MLR.

The intended deliverable is a complete proof of one alternative. A partial lemma, restricted class, obstruction to one construction or reformulation is an intermediate result to apply immediately, not a preselected endpoint. The owner's sustained-attempt authorization continues: multiple internal proof gates, successive lemmas, constructions, repairs and changes of route are authorized within S093. Continue through dependent obligations while a concrete route remains; do not defer a reachable next step to S094 merely because an intermediate result is recordable.

These are internal mathematical gates, not programme phase gates. Phase 4 remains OPEN; Phase 5 remains CLOSED. No publication or outreach. Never declare a missing lemma true, hide an assumption or manufacture a resolution.

## Entry and authority

Independently pin live remote main. Reconcile the S092 atomic close (its outgoing SHA is in the S092 final report; it is the commit whose message begins "P4-S092") and its sole parent `ec2c6ff1b5050b1b324d10b007843b1336bd7010`. Inspect any later changes and live branch/PR/check evidence; confirm S093 has not been executed. The side branch `phase4/P4-S092-wip` holds superseded S092 scratch only.

Read repository authority, docs/SESSION_PROTOCOL.md, CAND-01, Gate-3 PASS, both Phase-4 pivots and cumulative S001–S092 outcomes. Emphasize S003–S008, S011–S012, S032–S033, S081–S092, S082 §6.3, S087 §6.1–6.2, S089 §5, S091 Proposition 6, and S092 mathematics, validation, audit and close. Archive this exact incoming prompt before replacing NEXT_SESSION_PROMPT.md.

Use SRC-0015, SRC-0019, SRC-0028, SRC-0060 and SRC-0069–SRC-0072 only at their RECORDED access levels; do not upgrade by recollection. SRC-0071's journal version remains METADATA_ONLY. R_tot=MLR remains the programme deduction from its inspected preprint. Any new literature retrieval must be recorded with its access level and must not be used for priority or openness claims.

## Frozen starting mathematics

MLR=R_tot ⊆ R_fin ⊆ R_k ⊆ R₂ ⊆ OH^iso ⊊ OH^aff ⊊ OH^blk ⊆ OH^lin3 ⊆ OH=OH_h=R_k^scan ⊊ CR (k≥2, h≥1);
MLR ⊊ R₂^{cdz} ⊆ R₂^{dz} ⊆ R₂^{fd}; R₂ ⊊ R₂^{cdz} ⊊ R₂^{fd}; R₂^{cdz} ⊆ OH^aff∩OH^blk;
R₂⊊OH, MLR⊊OH, KLR⊆TKLR⊆OH, and OH^aff⊆OH^lin3.

Preserve S084's entire computably random predictable-error-stream requirement, ML-null infinite-resolution locus and balanced a.e. double-fibre destroyer; S085's representation-only c(n); S086's ∀F∃x and common-factor obstruction; all S087–S091 results with their theorem/experiment distinctions; the exact frames K_mix and K′_mix, including K′_mix's PRECEDING-control offset. Conjecture R remains UNRESOLVED; its numerics are EXPERIMENT only.

Challenge these S092 results before relying on them, without spending the session re-proving them:

* **Theorem 1 (orientation reader).** For any computable fair homeomorphism K, uniformly c.e. cylinder family W, computable level n and computable bet selection, the hold/filler reader with exclusive separate-coverage resolution, ties at zero stake and the S084 restart martingale is a legal F₂ strategy on every transcript. If the source is separately covered at every reached hold and its hold partners ψ_h=K⁻¹∘flip_h∘K are separately covered at only finitely many (or the source wins the first-coverage race at almost every hold), the source is destroyed on a singleton fibre.
* **Corollary 2 (global partner entanglement).** Every z∈OH^iso (so every z∈R₂) satisfies, in EVERY computable frame and for EVERY uniformly c.e. family separately covering it at all levels: its partners are separately covered infinitely often, and the reader's bet-error stream is computably random.
* **Proposition 3 / Lemma 4.** Universal ML tests separately cover every partner of every non-MLR source in frames with computable partner onset; entry stages of a CR source into any ML test dominate every computable function, so time-truncated orientation is void.
* **Proposition 5 / Lemma 5a / Corollary 5b.** For a left-c.e. source and its own approximation family W^g in the raw frame, exclusive coverage of the 1-candidate is always correct. Destruction by this reader is equivalent to infinitely many jump-overs at reached 1-bit holds; computable randomness excludes early agreement, so jump-overs must be late error-halving skips; for left-c.e. MLR sources jump-overs are finite for every computable g.

These are established starting results subject to a documented correction if an actual proof error is found.

## Proof gate 1 — State the exact theorem that would finish the problem

For equality, prove ∀z∈CR∖MLR ∃G∈F₂ ∃computable martingale d: d succeeds on G(z), preserving the quantifier order (source-dependent choice among genuinely computable maps is allowed; noncomputable G is not). The S092 sufficient form is the **Global Orientation Lemma (GOL)**: every z∈CR∖MLR has a frame K, a uniformly c.e. family W and computable n with separate coverage of z at every level and of its partners only finitely often (or the race form). Any other universal destroyer theorem is equally acceptable.

For separation, prove ∃z∉MLR ∀G∈F₂: G(z)∈CR for the SAME z, exposing effectivity and oracle use. By Corollary 2 such z must be globally entangled.

Write a short dependency plan for the chosen direction and identify the genuinely missing global implication. Choose on mathematical grounds; the S092 machinery is not mandatory.

## Proof gate 2 — Build a candidate all the way to its decisive obstruction

If pursuing equality:

* Attack GOL directly: find family SHAPES (not finite pinning) that separate an arbitrary CR∖MLR source from its partners, in a frame chosen from the source's failing test. Exploit asymmetries that universal evidence lacks, as monotone evidence does for left-c.e. sources.
* Carry the left-c.e. instance to its end: prove or refute that every left-c.e. z∈CR∖MLR admits a computable subsequence of some approximation with infinitely many late jump-overs at reached 1-bit holds, or find another F₂ destroyer for that class. Use only computability-theoretic facts you prove or that are catalogued at adequate access.
* Then generalize: transfer one-sided orientation from monotone approximations to arbitrary sources (for example through frames in which the source's failing test becomes monotone or order-respecting), or show why no such transfer exists.
* Prove total computability, fairness and the fibre bound on EVERY transcript; handle repeated false readings with the restart or selection accounting; establish actual unbounded capital.

If pursuing separation:

* Use Corollary 2 as a design constraint: the source must be globally entangled, with computably random race outcomes, in every frame for every separately covering family.
* Specify states, requirements, schedule and invariant; every effective choice must be Σ⁰₁ or explicitly guessed; separate validity information from what a computable observer can use; address non-effective validity.
* Handle non-commuting partner families (the three-involution core, K_mix with K′_mix, and tail-coded frames together): either designed fooling with group-closed decoy families of bounded measure cost, invariant splits, or a different mechanism. Meet S082 §6.3 / S087 §6.2 explicitly if absolute charges are used. Confront infinitely resolving self-readers in both exact nonlinear frames and S084's whole-error-stream requirement in the same construction.

## Proof gate 3 — Attack the obstruction, then repair the argument

Formulate the strongest plausible lemma the full theorem needs, try to prove it, and actively search for counterexamples to its quantified statement. If it fails, identify exactly which hypothesis failed and attempt a substantive repair that neither assumes the conclusion nor excludes the hard sources. Do not stop at another bounded-defect theorem, frame calculation or restricted-class destroyer; apply it immediately to eliminate the route or to force a stronger construction.

## Proof gate 4 — Cross the full-family quantifier

For separation: survival for EVERY F₂ map and EVERY output martingale with all convergence, compactness, effectiveness and scheduling claims proved. Survival of selected frames is a stress test, not membership in R₂.

For equality: coverage of EVERY CR∖MLR source with a precise coverage theorem. An obstruction to one construction is not evidence for a survivor. Keep the current gap explicit; a conditional equivalence earns a resolution only when its missing condition is proved.

## Proof gate 5 — Give the opposite alternative a serious attempt if the lead route stalls

If the lead route remains blocked after substantive repair, use the failure to attack the other direction and carry it to its own decisive global obligation. Do not trade ∃z∀F for ∀F∃z. Inability to prove one side is not evidence for the other. If a common obstruction blocks both mechanisms, state its precise scope and try to bypass it.

## Proof gate 6 — Adversarially validate the proposed resolution

If either target appears proved, assemble a self-contained proof from the exact definitions, auditing every quantifier, limit, source-selection dependence, effectivity claim and all-transcript obligation, including exceptional paths, repeated false predictions and conditioning on arbitrarily small states. Use exact computation or formalisation where it addresses a concrete proof risk; finite checks never establish universal coverage or randomness of an infinite witness. If no resolution is achieved, report honestly the strongest proved result, the failed attempts and repairs, and the smallest remaining GLOBAL obligation. No novelty, external openness or priority claim.

## Preserved boundaries and closeout

Keep R₂ versus OH^iso, U(H), original X∈OH and fixed-S preservation separate from the central target. Preserve original CR Y, unchanged globally use-clipped self-avoiding wtt M, repeated three-bit H with A=[101;110;111], and X=H⁻¹(Y). No escrow, hazard, residue, unit-column, record-only z₀ or multi-hole detours; no spectral numerics, local frustration certificates or stand-alone operator reformulations. Do not re-prove S085–S092 with changed constants, another frame, another bounded defect or another restricted reader class as the session result.

PA-0001 and DEF-0020 unchanged; Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No publication or outreach.

Close per docs/SESSION_PROTOCOL.md. Validate and synchronize state, current pointers, gate ledger, decisions, blockers and failure ledger. Distinguish proved, conditional, refuted and unresolved obligations, and identify whether the full target was actually decided.

Make one atomic S093 session-branch commit, push it, non-force fast-forward/merge into main, and independently verify outgoing remote main and its parent. Unless an owner/external blocker exists, embed the FULL copy-ready P4-S094 prompt verbatim in both the close record and final report, identical to authoritative/NEXT_SESSION_PROMPT.md. Its task must follow the actual outcome; if the target is resolved, do not pretend it remains open. STOP after S093; do not execute S094.
