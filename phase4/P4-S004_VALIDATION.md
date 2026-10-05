# P4-S004 validation

Date: 2026-10-05
Incoming baseline: 08b2d04dba6adb57435857369cd2b5317c508940
Result: **PASS** for uniqueness, k=2 scope discipline, conditional-weight calculations, explicit-map checks, authority synchronization and preserved novelty/convention guards.

Checks:
- live main matched the incoming baseline before substantive work and again before closeout writes;
- repository search found no committed P4-S004 record on the incoming checkpoint;
- Phase 4 was OPEN for selected CAND-01 and Phase 5 CLOSED;
- CAND-01's exact formulation is unchanged;
- P4-S001 through P4-S003 are not edited;
- for conditioned source measure lambda_sigma, mu_sigma([tau])=2^{|sigma|-|tau|}w_sigma(tau), so q_sigma=2^{-|sigma|}/w_sigma is the fair-coin/mu_sigma likelihood-ratio martingale;
- Ville's inequality gives lambda(V_{sigma,epsilon})<=epsilon for the effectively open low-weight crossing set;
- the conclusion for Martin-Löf-random sources is explicitly not promoted to computably random sources; REL-0001/REL-0002 are used only to calibrate this effectivity gap;
- the fixed-stage pullback e_m(sigma)=2^{|sigma|} integral_[sigma] d(F(z)↾m) dlambda is computable, normalized and satisfies the source martingale equation;
- continuity guarantees that along x some source prefix makes e_m equal d(F(x)↾m);
- the family e_m is not misrepresented as one succeeding martingale; coherence/stopping remains unresolved;
- for F_thin, A_m=[0^{2m}] union ([1^m] minus [1^m0^m]) is nested, clopen, has measure 2^{-m}, and intersects to {0^omega,1^omega};
- C_m=A_m minus A_{m+1} and D_m=[0^m1] have equal measure 2^{-(m+1)}, allowing uniform same-level prefix-replacement measure isomorphisms;
- F_thin is everywhere computable, continuous, fair-coin preserving, has one double fibre and all other fibres singleton;
- F_thin^{-1}([0^m])=A_m and w_0(0^m)=2^{-m}, so positive persistent sheet weight is not a bare k=2 consequence;
- F_thin is explicitly not a randomness-destruction witness and has an a.e.-computable inverse off 0^omega;
- the SRC-0061 filler/pre-revealed-bet obstruction is not claimed resolved; masked fillers are recorded only as a failed mechanism;
- no exact k=2 computable-randomness destroyer is asserted;
- general k=2 preservation/failure remains unresolved;
- no result is asserted for k>2;
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- the pre-Phase-4 Gate-3 guard remains historical and unchanged in meaning;
- DEF-0020 and catalogue records are unchanged;
- Gate 4 is not reviewed and Phase 5 remains CLOSED;
- synchronized JSON records parse successfully;
- P4-S005 is the next bounded task and no owner/external blocker exists.

This is bookkeeping/manual proof validation, not proof-assistant verification and not a novelty theorem.
