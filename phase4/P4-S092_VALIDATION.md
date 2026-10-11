# P4-S092 validation — orientation reader, global entanglement, one-sided left-c.e. orientation

Date: 2026-10-11. Phase 4 only. Review mode: written adversarial self-review and exact finite audits. No independent agent, Lean or external review is claimed.

## Entry and authority

PASS: independent `git ls-remote` of `refs/heads/main` gave `ec2c6ff1b5050b1b324d10b007843b1336bd7010`; commit metadata gave sole parent `6633f88ba8a0826442618f5062cb2d74b83c9e86` (S091 close) and its sole parent `971b3ccef56fc5654c857a32e882342c80e325c2`, matching the prompt. The amendment's diff is documentation only (prompt, close handoff, STATE `next_transition` and `next_session_owner_direction`, AGENTS/START_HERE notes, decision and session ledgers). REST pull-request listing (all states) empty; zero check runs and zero commit statuses at the incoming SHA. No S092 file or branch at entry. Incoming prompt byte-identical to `authoritative/NEXT_SESSION_PROMPT.md` except a final newline; archived with SHA256 `d892903904fe352ba9a40d9118be61ea9dd2f57a46a1e70205b0381cf24cdaa0`.

Work was interrupted once by an owner-reported usage limit; scratch work was committed to the side branch `phase4/P4-S092-wip` at the owner's instruction ("You can commit scratch work") and is superseded by the single atomic session commit. Main was not touched before the close.

Source access unchanged; no external retrieval. THM-0014 is cited only at its recorded statement level and is not used in any proof.

## Proof review

**Lemma 1.1 (legality) — PASS.** Every step is a finite computation: the stage-t list W_{n(h),t}, the computable modulus of K⁻¹ and string prefix tests. Queries are the current unread hold or the current unread frontier only. Permanent-hold transcripts leave exactly that hold unread; infinitely resolving or tying transcripts read everything. Ties and timeouts are zero-stake reads. The S084 restart martingale is reused with its exact tail term. G=F_T∘K∈F₂ by the S008 scan fibre formula and the fair homeomorphism K.

**Theorem 1 — PASS.** Checked adversarially:
* separate coverage is tested only with strings no longer than the determined raw window ℓ(M); a string longer than the window could otherwise be misjudged as separating;
* the partner's raw window is computed from the flipped virtual window through K⁻¹, so the partner is ψ_h(x) exactly, in every frame;
* (O1) forces every reached hold to be left; (O2) at a hold forbids the wrong exclusive coverage AND forbids ties; only finitely many holds can tie or be wrong;
* the conclusion needs infinitely many selected correct bets, which (O3) supplies; with Sel≡true it follows from (O1)+(O2);
* infinite resolution gives a singleton virtual fibre and hence a singleton G-fibre.
The timing form (O2′) is valid because the proof uses (O2) only at the first coverage check. No measure bound on W is used; W need not be a test.

**Proposition 1.2 — PASS** (conditional statement only; GOL is not proved).

**Corollary 2 — PASS.** Contrapositive of Theorem 1 through z∈OH^iso⇒K(z)∈OH. The error-stream addendum uses S084 Theorem 1 with resolution flag and proposed bit computable from the preceding transcript; ties are separate partner coverages by definition. No claim is made about readers outside Theorem 1.

**Proposition 3 — PASS.** The onset bound is an explicit hypothesis; it holds with onset exactly h in the raw, D′, K_mix and K′_mix frames (for K′_mix the virtual hold 2q starts the a-difference at index q, raw position 2q; the preceding-control offset concerns later propagation, not the onset). Cylinders of an ML-test level m have length ≥m. Partners of non-MLR points are non-MLR by THM-0035 in both directions.

**Lemma 4 — PASS.** The summands are exact measure martingales of uniformly computable clopen sets; the 2^{m/2} weighting gives a computable convergence modulus uniform in σ and a finite initial capital; success follows if the source lies in infinitely many truncations. Uses only x∈CR. Applies to partners by THM-0038.

**Failed repairs (§3.3) — recorded as analysis, not theorems.**

**Lemmas 5.1–5.3, Proposition 5 — PASS.** Conventions made explicit: terminating expansions, half-open dyadic intervals, non-eventual-constancy (automatic for CR sources). Lemma 5.2's inequality r(z)<z↾h10^∞ when z_h=0 is strict exactly because the tail is not all ones. Lemma 5.3's monotonicity step uses that [z↾h0]_ℝ lies entirely below [z↾h1]_ℝ and that g is increasing and the approximation nondecreasing. The window condition |σ|≤M is harmless because length h+1 strings already decide coverage. With Sel₁ all selected bets on z are correct, so no restart accounting is needed.

**Lemma 5a — PASS.** A monotone computable martingale; its bets are correct by the same inequality as Lemma 5.2; contradiction with z∈CR if infinitely many. The statement is about index h+1 only; it does not bound later approximations.

**Corollary 5b — PASS.** Uses MLR⊆R₂⊆OH only.

**Status claims — PASS.** GOL, late-skip jump-overs for left-c.e. CR∖MLR sources, any survivor, Conjecture R and R₂ versus MLR are reported UNRESOLVED. No class inclusion is added to the frozen landscape. The separation-side designs of §5 are analysis only; the "recognizable center" statement for non-commuting involutions is not claimed as a theorem.

## Executed checks

`python3 phase4/P4-S092_ORIENTATION_AUDIT.py`: **103,286 exact checks PASS** (about 13 s; integer and Fraction arithmetic; fixed seed):

1. reader legality on random inputs in the raw and D′ frames (read set exactly [0,M)∖{h} at every step, no repeated query) and an exhaustive fibre check on all virtual inputs of length 9 (at most two compatible prefixes per output transcript);
2. Theorem 1 logic with a source-pinned family and injected partner cylinders: every uninjected hold resolves correctly; every error and every tie occurs at an injected (separately covered) partner;
3. left-c.e. sources with random nondecreasing dyadic approximations, slow and fast steps, two subsequences g: every proposal 1 has z_h=1 (Lemma 5.2); 0-bit holds resolve to 0, jump-overs resolve to 1, non-jump-overs never propose 1 (Lemma 5.3); the Lemma 5a betting rule never loses;
4. exact measure-martingale identity for the Lemma 4 summands on random clopen sets;
5. the octave skip-ratio inequality.

Finite checks supplement the written proofs; they do not establish GOL, infinite jump-overs, computable randomness of any witness, or any decision of R₂ versus MLR.

## Closeout checks

JSON parse of STATE.json; new cross-links resolve; current pointers (last completed P4-S092, next P4-S093) agree across STATE, START_HERE, AGENTS, README, ROADMAP, STATUS and phase4/README; the S093 prompt in the close record is byte-identical to `authoritative/NEXT_SESSION_PROMPT.md`; `git diff --check` clean. No changes to source, candidate or prior-art records, gate decisions, original witness data or earlier numbered mathematics.

Delivery: one session commit on `phase4/P4-S092-mathematics` with the incoming main as sole parent, pushed, then main fast-forwarded non-force and independently re-read. A commit cannot contain its own SHA; the final report supplies the verified outgoing hash. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED; owner/external blocker NONE.
