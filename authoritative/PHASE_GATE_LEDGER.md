# Phase Gate Ledger

| Gate | Status | Meaning |
|---|---|---|
| Scaffold -> Phase 1 | AUTHORIZED | Owner explicitly authorized Phase 1 on 2026-10-03. This is an authorization transition, not a research-gate PASS. |
| Phase 1 -> Phase 2 | CLOSED | Phase 1 is OPEN and active; Gate 1 has not passed. |
| Phase 2 -> Phase 3 | CLOSED | Phase 2 is not authorized. |
| Phase 3 -> Phase 4 | CLOSED | Phase 3 is not authorized. |
| Phase 4 -> Phase 5 | CLOSED | Phase 4 is not authorized. |
| Phase 5 completion | CLOSED | No publication work is authorized. |

Research-gate statuses are `CLOSED`, `UNDER_REVIEW`, `PASS`, `FAIL`, `BACKTRACK`.

`AUTHORIZED` is reserved here for the non-research bootstrap-to-Phase-1 transition that depends on explicit owner authorization rather than a completed research gate review. It must not be interpreted as a PASS of Gate 1.

A research-gate PASS must link to a completed gate review using `templates/gate-review.md`. A gate review must state evidence, unresolved risks and exact next authorization.
