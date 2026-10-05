# P4-S011 close

Date: 2026-10-05
Incoming checkpoint: 31cff4e4c442520b19054f19fac75bd8b5c7cc26

Status: COMPLETED

P4-S011 resolves the P4-S010 adaptive c.e.-trigger singleton-spine source-randomness question strictly at k=2.

SRC-0067 / SRC-0068 / THM-0076 supply a computably random weak-truth-table-autoreducible sequence Y. Its partial autoreduction is embedded into the least-fresh-sentinel comb: while the prediction is unresolved, the total scan emits fresh non-sentinel fillers; after a visible prediction it queries the sentinel and turns over.

The resulting map is everywhere total, computable, fair-coin preserving and globally k=2. A permanently nontriggering epoch queries every coordinate except one sentinel and therefore has a two-point fibre. If every epoch triggers, every coordinate is eventually queried and the fibre is a singleton.

On Y every prediction halts and is correct. One computable output martingale holds capital on filler bits and doubles on every sentinel, so it succeeds. Thus Y is computably random while F(Y) is not.

Therefore general forward computable-randomness preservation at k=2 fails by an exact witness. The repeated graph-like trigger structure does not force a computable source martingale in general.

SRC-0061 is not reused. P4-S005 through P4-S010 remain settled. PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE. DEF-0020 is unchanged. No k>2, novelty, Gate-4 or publication claim is made.

Owner/external blocker: NONE.

Recommended next bounded session: P4-S012, still at k=2, abstracting the weakest partial-predictor/autoreduction condition sufficient for the P4-S011 conversion and testing the converse inside the global-k=2 adaptive no-repeat scan subclass.
