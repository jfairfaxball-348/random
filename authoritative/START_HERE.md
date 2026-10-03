# Authoritative Entry Point

Repository: https://github.com/jfairfaxball-348/random

## Read in this order

1. `AGENTS.md`
2. `authoritative/STATE.json`
3. `PROJECT_CHARTER.md`
4. `ROADMAP.md`
5. `docs/GATE_POLICY.md`
6. `docs/SESSION_PROTOCOL.md`
7. `docs/SOURCE_AND_CITATION_POLICY.md`
8. `docs/AGENT_SEARCH_GUIDE.md`
9. `authoritative/PHASE_GATE_LEDGER.md`
10. `authoritative/DECISION_LOG.md`
11. `docs/FAILURE_AND_LESSON_LEDGER.md`

Then read only the records required by the currently open phase.

## Current authority

**Phase 1 — Research / Catalogue — is OPEN.**

Explicit owner authorization was received on 2026-10-03 for P1-S001 and Phase-1 research/catalogue work. Phases 2–5 remain CLOSED. Mathematical investigation and publication work remain unauthorized.

Opening Phase 1 is an authorization transition only. The Phase 1 -> Phase 2 gate has **not** passed and remains CLOSED until the full Gate-1 evidence in `docs/GATE_POLICY.md` is satisfied and audited.

Incoming Phase-1 predecessor checkpoint:
`51ee5da396325eb3c898dcb475ad14e628ba4af4`

Verify live `main` before each session.

## Conflict rule

If a prompt, conversation recollection or older record conflicts with live committed authority, the repository wins unless the owner gives a new explicit instruction. Record that instruction before relying on it in later sessions.

## Phase transition rule

A phase may open only when:
1. the preceding phase gate has a committed PASS (except Phase 1, which requires owner authorization from scaffold state);
2. any gate-blocking contradictions are reconciled;
3. `STATE.json` is updated to the new phase;
4. the gate ledger records the transition.

No agent may self-declare a gate passed merely to continue working.
