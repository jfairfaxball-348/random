# P4-S005 validation

Date: 2026-10-05
Incoming baseline: beaa3c41f886176cde1b51d74e6e812b8f30974a
Result: **PASS** for uniqueness, k=2 scope discipline, prefix-code construction, noncomputable-crossing calculation, branch-free lift obstruction, authority synchronization and preserved novelty/convention guards.

Checks:
- live main matched the incoming baseline before substantive work;
- repository search found no committed P4-S005 record on the incoming checkpoint;
- Phase 4 was OPEN for selected CAND-01 and Phase 5 CLOSED;
- CAND-01's exact formulation is unchanged;
- P4-S001 through P4-S004 are not edited;
- the block words t_e=1^e0^{e+2} are prefix-free and have measure q_e=4^{-(e+1)};
- the local codes C_0 and C_1 are total computable and injective;
- finite output computation only needs to simulate whether e enters K before the requested post-block output depth, so the global map is everywhere total computable;
- on each activated local parent, the four target grandchildren receive total source masses 1/4,1/4,1/4,1/4 of the parent, so fair coin is preserved;
- fibres are at most two, with double fibres on local 00/10 regions and singleton fibres on 01/11 regions after activation;
- [0] and [1] are a computable clopen partition and each restriction of F is injective;
- before activation w_0=1/2; at the first activated output bit the two values are 1/4 and 3/4; a sheet-0 point crosses below 1/3 exactly through local source codeword 00;
- each activated block contributes q_e/8 to V_{0,1/3};
- lambda(V_{0,1/3})=(1/8) sum_{e in K}4^{-(e+1)};
- the base-4 digit-gap argument proves this real noncomputable when K is c.e. noncomputable;
- the conclusion is limited to failure of the direct computable-hitting-measure/Schnorr-component route; no claim excludes all alternate Schnorr covers or all other transfer proofs;
- the symmetric inverse-point-count lift has total mass 2-(1/2) sum_{e in K}q_e and is therefore not uniformly computable;
- the construction is explicitly not a randomness destroyer because the P4-S003 computable clopen two-sheet preservation theorem applies;
- no SRC-0061 finite-fibre witness is claimed; the filler/pre-revealed-bet obstruction remains unresolved;
- no exact k=2 computable-randomness destroyer is asserted;
- general k=2 preservation/failure remains unresolved;
- no result is asserted for k>2;
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- the pre-Phase-4 Gate-3 guard remains historical and unchanged in meaning;
- DEF-0020 and catalogue records are unchanged;
- Gate 4 is not reviewed and Phase 5 remains CLOSED;
- synchronized `authoritative/STATE.json`, `phase2/candidates.json` and `phase3/prior-art.json` parse successfully; PA-0001 remains `UNRESOLVED_UNDER_INSPECTED_EVIDENCE`;
- the final baseline comparison changes only P4-S005 records and programme authority/index files; P4-S001 through P4-S004 and catalogue files are absent from the changed-file set;
- P4-S006 is the next bounded task and no owner/external blocker exists.

This is bookkeeping/manual proof validation, not proof-assistant verification and not a novelty theorem.
