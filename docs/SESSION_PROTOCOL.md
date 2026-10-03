# Session Protocol

## Session identifiers

Use:
- `B###` for bootstrap/scaffold sessions;
- `P1-S###` through `P5-S###` for phase sessions.

Session IDs are unique and monotone within their phase.

## Start

1. Pin live `main`.
2. Read `authoritative/START_HERE.md` and required authority.
3. Reconcile the incoming prompt with live state.
4. Confirm the proposed session ID is unused.
5. Confirm its phase is OPEN.
6. State the bounded objective.

If the phase is not open, do not perform the substantive task.

## Work

- Keep scope bounded.
- Write durable results to the repository as they are established.
- Distinguish evidence levels.
- Link source IDs rather than relying on prose recollection.
- Preserve failures and corrections.
- Do not start another numbered session in the same turn.

## Closeout

Before ending:
1. validate changed records;
2. synchronize `STATE.json`, gate ledger, decisions, blockers and failure ledger;
3. create a concise session close record;
4. commit and verify the remote checkpoint;
5. identify the next bounded task.

If an active blocker requires owner/external action, report the concrete request and give **no next-session prompt**. Otherwise provide a copy-ready next-session prompt consistent with live authority.
