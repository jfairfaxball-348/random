# P4-S050 Close

Date: 2026-10-08
Session: P4-S050
Incoming checkpoint: 9d03117f2674bd0a942634520ff4bed0890f5e1b
Status: **COMPLETED / VALIDATED**
Scope: finite positive square-refutation activation without a trapped-epoch oracle.

## New mathematics

1. A positively refuted two-bit atom can be excluded on every old epoch; no semantic trap knowledge is needed.
2. Exact terminal hedge: 0 on forbidden (a,beta), 4/3 on each of the other three; implement by fair first-s capitals 2/3 and 4/3, then fair t-query (0,4/3) or zero-stake (4/3,4/3). Guaranteed terminal 4/3 gain on X; temporary first-stage drawdown allowed.
3. A legal finite-tenure active-pair protocol executes every timely square event, consumes both s,t, and starts a new epoch. Timeout consumes t at zero stake and retains s. Exhaustive zero-stake sweep makes every complete transcript at most one-hole; output is computable and fair-coin preserving.
4. Combined old-branch/square exits have guaranteed gains 2 or 4/3. Infinitely many executed positive exits yield one succeeding computable output martingale and prove X not in OH.
5. Under hypothetical X in OH, each computable combined policy has finitely many positive exits, hence an algorithm-dependent final persistent sentinel with no finite old-branch refutation and no timely square captures thereafter.
6. A single excluded pair cannot give a guaranteed strict gain by querying only s or only t. The unconditional two-bit hedge **resets the old sentinel**. This reset cost is distinct from the P4-S049 trapped-epoch future-bit theorem, which can retain s but has an unrecognizable semantic premise.
7. Source-specific infinite cross-epoch square capture remains unproved. Infinite semantic A blocks and wtt value horizons do not supply certificate-time capture bounds.

## Records
- phase4/P4-S050_MATHEMATICS.md
- phase4/P4-S050_VALIDATION.md
- phase4/P4-S050_CLOSE.md

## Disposition
No proof X in OH or X not in OH. No strict R_2 subsetneq OH or OH non-invariance. Retain MLR subseteq R_2 subseteq OH^iso subseteq OH proper-subset CR.

PA-0001 **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**; DEF-0020 unchanged; Phase 4 OPEN, Phase 5 CLOSED.

Owner/external blocker: **NONE**.

Next bounded session: **P4-S051**, investigate square-refutation capture across reset and whether positive multi-square information permits legally reusable gain without assuming a trapped epoch.
