# Instructions for every agent

## Authority

Read `authoritative/START_HERE.md` first. The committed repository is authoritative. Conversation history, model memory and pasted prompts are not research authority. If they conflict with live committed authority, stop and reconcile the mismatch before substantive work.

## Current phase restriction

Gate 1 — Research/Catalogue -> Discovery — **PASSED** in P1-S014 on 2026-10-04. Gate 2 — Discovery -> Novelty/Prior Art — **PASSED** in P2-S006 on 2026-10-04. Gate 3 — Novelty/Prior Art -> Mathematics — **PASSED** in P3-S008 on 2026-10-05.

Phases 1–3 are complete for gate purposes. Phase 4 — **Mathematics** — is OPEN for selected CAND-01. Phase 5 remains CLOSED.

Phase-4 work may perform original mathematical investigation on CAND-01: proofs/disproofs, counterexamples, exact boundary analysis, characterizations, examples, justified computation, and Lean/Palomar work where useful. It must preserve the exact committed CAND-01 formulation unless a documented mathematical finding requires an explicit revision/backtrack.

Gate-3 PASS does not establish novelty, openness, truth or publishability. PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE. The Gate-3 controlling guard was that finite multiplicity was provisionally substantive but had no established computable-randomness consequence before Phase 4. P4-S001 now establishes only the k=1 injective consequence: such maps force a computable measure-preserving inverse and preserve computable randomness. No conclusion is established there for k>=2 or general finite multiplicity. Publication work remains unauthorized until a separate Gate-4 PASS.

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
