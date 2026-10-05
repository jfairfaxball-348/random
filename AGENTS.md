# Instructions for every agent

## Authority

Read `authoritative/START_HERE.md` first. The committed repository is authoritative. Conversation history, model memory and pasted prompts are not research authority. If they conflict with live committed authority, stop and reconcile the mismatch before substantive work.

## Current phase restriction

Gate 1 — Research/Catalogue -> Discovery — **PASSED** in P1-S014 on 2026-10-04. Gate 2 — Discovery -> Novelty/Prior Art — **PASSED** in P2-S006 on 2026-10-04. Gate 3 — Novelty/Prior Art -> Mathematics — **PASSED** in P3-S008 on 2026-10-05.

Phases 1–3 are complete for gate purposes. Phase 4 — **Mathematics** — is OPEN for selected CAND-01. Phase 5 remains CLOSED.

Phase-4 work may perform original mathematical investigation on CAND-01: proofs/disproofs, counterexamples, exact boundary analysis, characterizations, examples, justified computation, and Lean/Palomar work where useful. It must preserve the exact committed CAND-01 formulation unless a documented mathematical finding requires an explicit revision/backtrack.

Gate-3 PASS does not establish novelty, openness, truth or publishability. PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE. The Gate-3 controlling guard was that finite multiplicity was provisionally substantive but had no established computable-randomness consequence before Phase 4. P4-S001 establishes the exact k=1 injective consequence. P4-S002 establishes that k=2 gives descending computable-clopen fibre names but not total computable selectors/branch enumerations. P4-S003 strengthens the forced k=2 information to uniform two-prefix inverse lists, proves preservation under an explicitly supplied computable clopen two-sheet split, and shows that no global continuous/clopen sheet colouring is forced. P4-S004 sharpens the conditional-weight boundary: low sheet-weight crossings give only an ML-level pullback test, every fixed output betting stage lifts exactly to a source martingale, and an explicit asymmetric k=2 collision map shows that an actual sheet may have weight tending to zero. P4-S005 then shows that the forced two-prefix structure does not make those crossing measures computable: an exact k=2 map with a computable clopen injective-sheet split has noncomputable low-weight hitting measure, and a natural symmetric fibre-count lift can have noncomputable mass. The example is in the positive split regime and is not a destroyer. General k=2 preservation/failure remains unresolved; the live obstruction is effective non-clopen branch coherence versus a genuinely moving-sheet counterexample. No conclusion is established for k>2 or general finite multiplicity. Publication work remains unauthorized until a separate Gate-4 PASS.

## Programme objective

The long-term objective is to determine whether a mathematically natural, useful, novel and publishable notion can legitimately be introduced as **Fairfax-Ball Randomness**.

The name is not an assumption. An agent must be willing to conclude that:
- a proposed definition is already known under another name;
- it collapses to an existing randomness notion;
- it is weaker/stronger only for trivial reasons;
- it lacks a natural motivation or characterization;
- it has no worthwhile theorem package;
- it is too close to prior art;
- or the programme should terminate without introducing a new named notion.

## Five hard phase gates

Phases are sequential unless a committed backtrack decision says otherwise:

1. Research / Catalogue
2. Discovery
3. Novelty / Prior Art
4. Mathematics
5. Publication

Never cross a phase boundary merely because the next task looks useful. The current phase must have a committed gate review marked PASS, and `authoritative/STATE.json` must explicitly open the next phase.

## Research integrity

- Prefer primary literature for exact theorem statements, priority and novelty.
- Record source-access level: metadata only, abstract inspected, statement inspected, proof inspected, or secondary-only.
- Never infer that a problem is open because searches found no solution.
- Separate source facts, programme deductions, conjectures, experiments, formal proofs and external opinions.
- Preserve exact definitions, quantifiers, oracle/measure/effectivity conventions and equivalence hypotheses.
- Record negative results and failed approaches in the failure ledger.
- Recheck current journal/arXiv/policy facts when they become decision-relevant.
- Never fabricate citations, theorem names, priority claims, reviewer views or publication status.

## Catalogue discipline

Phase 1 is intended to become a durable AI-searchable knowledge base. Use stable IDs, machine-readable metadata, explicit cross-links, normalized terminology and concise derived notes. Do not store copyrighted papers in the repository unless permission clearly allows it; store bibliographic metadata, stable links, source-status records and original notes instead.

## Mathematics and formalisation

Phase 4 alone authorizes new mathematical investigation. Lean formalisation and Palomar registration may be used where they add value. Formalisation verifies the encoded mathematics under its trust boundary; it does not establish novelty, significance, correct interpretation of the literature or journal acceptance.

## Sessions and blockers

Follow `docs/SESSION_PROTOCOL.md`. Work only within the bounded authorized phase/session. Before closeout, synchronize state, decisions, claims, blockers and lessons and verify the remote checkpoint.

If a blocker requires John's decision, communication, account action or other external input, state the exact blocker and required action and output **no next-session prompt**. A next-session prompt means the next task is immediately runnable.

Do not contact mathematicians, editors, journals, arXiv or other third parties without explicit authorization.

## Publication integrity

Publication is an aspiration, not a promised outcome. Do not represent an arXiv preprint as peer reviewed. Do not represent a private reviewer as a journal referee. Preserve an accurate disclosure trail for substantive AI assistance and follow the policies of the eventual venue.

## Mathematics checkpoint — P4-S005 (not a gate review)

P4-S005 completed one bounded k=2 crossing-measure/stopped-pullback investigation for selected CAND-01.

Result: the forced two-prefix inverse lists do not make the P4-S004 low-weight crossing measures computable. A total computable fair-coin-preserving k=2 prefix-code map, even with a computable clopen partition into two injective sheets, has a crossing set V_{0,1/3} whose fair-coin measure is a noncomputable base-4 encoding of a c.e. noncomputable set. A natural symmetric inverse-point-count lift can likewise have noncomputable total mass.

These are stopping-effectivity obstructions, not non-conservation results. The example preserves computable randomness by the P4-S003 clopen-sheet theorem. No exact k=2 destroyer is obtained, and the SRC-0061 pre-revealed-bet obstruction remains unresolved.

This is not a Gate-4 decision and not a novelty finding. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; the pre-Phase-4 Gate-3 guard, P4-S001 through P4-S004 and DEF-0020 are preserved; no claim is made for k>2. Phase 4 remains OPEN and Phase 5 CLOSED.

Record: phase4/P4-S005_MATHEMATICS.md.

