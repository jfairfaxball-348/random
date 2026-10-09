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
3. create a concise session close record; unless an owner/external blocker exists, it must contain the full copy-ready next-session prompt, identical to `authoritative/NEXT_SESSION_PROMPT.md`;
4. commit atomically, push the session branch, merge it into `main` (fast-forward when possible, otherwise a merge commit; never rewrite `main` history) and push `main`;
5. independently verify the remote checkpoint (e.g. `git ls-remote origin refs/heads/main`) equals the outgoing SHA;
6. identify the next bounded task.

Steps 4–5 are mandatory (owner direction recorded after P4-S080): a session is not closed while its work exists only on a side branch. If the merge or push cannot be completed, report that as the blocker, with the exact failing step.

If an active blocker requires owner/external action, report the concrete request and give **no next-session prompt**. Otherwise the final report must state the verified outgoing `main` SHA and reproduce the copy-ready next-session prompt consistent with live authority.
