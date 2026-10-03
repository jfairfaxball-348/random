# Failure and Lesson Ledger

Every phase must preserve material dead ends, including candidate collapses, false conjectures, counterexamples, novelty failures, search strategies that miss terminology, formalisation/specification mismatches, publication-policy dead ends and corrected programme claims.

Use IDs `FL-###`. Do not delete an old failure because a later route succeeds.

## FL-001 — Foundational original-source retrieval gaps in P1-S001

Session: `P1-S001`  
Status: OPEN RESEARCH GAP / NOT A PROGRAMME BLOCKER

The first foundational pass did not obtain statement-level primary/original coverage for the foundational Schnorr formulation, Kurtz randomness, or Demuth's original randomness papers. Later primary papers, surveys and monographs were located, but P1-S001 deliberately did not promote uninspected originals into exact definition records.

Lesson: when an original is not available at statement level, record the gap and use the strongest actually inspected later source with its evidence level. Do not manufacture priority or theorem detail from citation trails.

Follow-up: prioritize these sources in P1-S002.

## FL-002 — Chaitin near-title metadata collision

Session: `P1-S001`  
Status: RESOLVED

Searches for *On the Length of Programs for Computing Finite Binary Sequences* surfaced both the 1966 JACM article and a distinct 1969 continuation with “Statistical considerations” and a different DOI.

Resolution: SRC-0004 was anchored to the 1966 record only after cross-checking year, volume, pages and DOI (`10.1145/321356.321363`).

Lesson: exact-title searching is insufficient when an author publishes near-identically titled sequels; verify DOI plus journal coordinates before assigning a stable source ID.

## FL-003 — Provisional stable-ID format defect

Session: `P1-S001`  
Status: RESOLVED BEFORE CLOSEOUT

The first KL-randomness definition draft used `DEF-0006A`, which violated the required `DEF-####` stable-ID convention. Referential validation also caught one lingering question-record link to that provisional ID.

Resolution: the permanent record is `DEF-0012`; source/theorem/question references were repaired and final cross-file validation passed with zero unresolved reference errors.

Lesson: run ID-pattern and referential-integrity validation before authoritative closeout, including status-question links.
