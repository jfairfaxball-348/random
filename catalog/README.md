# Phase-1 Catalogue

Phase 1 is **OPEN** and the catalogue is **IN PROGRESS**. This directory is a structured research library, not a claim of field completeness.

## Entry point

Start with `catalogue.json`. It gives record counts and paths. Then use:

- `coverage-plan.json` — 19 research strata with scope, aliases, dependencies, depth target, current coverage and access limitations.
- `sources.json` — stable `SRC-####` bibliographic/source-evidence records.
- `definitions.json` — stable `DEF-####` formal-notion records.
- `theorems.json` — stable `THM-####` characterization/relationship theorem records.
- `relations.json` — stable `REL-####` implication/equivalence/separation/property records.
- `questions.json` — stable `QST-####` status-sensitive questions with dated source provenance.
- `authors.json` — stable `AUT-####` navigation records.
- `taxonomy.md` — controlled retrieval vocabulary and aliases.
- `search-log.md` — databases/locations, query families, citation-following routes, failed/incomplete searches and access limits.
- `schema/source-entry.schema.json` — source metadata/evidence contract.

## Evidence discipline

The source `access_level` records what was actually inspected, not what might be obtainable. A theorem or definition can cite an abstract when the abstract itself states it, but must preserve that lower evidence level. No source in this catalogue establishes global novelty of any future Fairfax-Ball notion.

## P1-S001 checkpoint

P1-S001 established the architecture and populated a first foundational corpus. It intentionally did **not** complete Phase 1. Important incompleteness is recorded in `coverage-plan.json` and `search-log.md`.

No copyrighted papers are stored here merely for convenience; the repository stores metadata, stable links and original structured notes.
