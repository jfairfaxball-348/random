# P4-S003 close

Date: 2026-10-05
Session: P4-S003
Incoming checkpoint: 4ccf7a1f9993a38ed15d8ba59207bde2ee1ecdee
Scope: selected CAND-01; k=2 weighted-sheet / martingale-transfer boundary only
Status: **COMPLETED**

## Result

P4-S003 strengthens the forced k=2 inverse information: for every requested input precision n one can computably find an output precision m_F(n) at which each output cylinder has preimage meeting at most two length-n input cylinders. Thus every fibre has a uniform finite two-prefix list at every precision, even though P4-S002 showed that those candidates need not admit total computable persistent branch labels.

The session also proves a positive transfer theorem. If the source has a computable clopen partition into two sheets on each of which F is injective, then conditional source measures and their pushforwards give effective measure-isomorphism components; SRC-0015 / THM-0038 plus DEF-0036's computable-measure ratio characterization yields forward fair-coin computable-randomness preservation.

That sufficient sheet structure is not forced. The explicit marker-and-delete map H is total computable, fair-coin preserving and exactly two-to-one off one singleton, but its double pairs converge to the singleton from both colours, so no continuous/clopen two-colouring can separate every pair. H nevertheless has an a.e. sheet description and preserves computable randomness.

P4-S003 further isolates computable conditional-weight martingales
w_sigma(tau)=2^{|tau|}lambda([sigma]∩F^{-1}([tau])).
Their effective behaviour on a true double-fibre split is the remaining weighted inverse issue.

The exact counterexample route through SRC-0061 / THM-0072 was tested but not completed. Completing the known nonmonotonic scan with filler queries would force all but at most one input coordinate to be read, hence k=2 fibres, but a filler may reveal a position before the original strategy later bets on it. No argument preserving the winning capital while maintaining the global k=2 condition was obtained.

Accordingly, the general k=2 forward computable-randomness preservation/failure question remains unresolved in P4-S003. No exact k=2 randomness-destruction witness is claimed.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard, P4-S001, P4-S002 and DEF-0020 are preserved exactly. No conclusion is made for k>2. Gate 4 is NOT REVIEWED. Phase 5 remains CLOSED. No owner/external blocker exists.

Validation: phase4/P4-S003_VALIDATION.md.

Next: P4-S004, still bounded to k=2, focused on the conditional-weight obstruction: determine whether source computable randomness forces enough effective stabilization/positive sheet weight to transfer an arbitrary losing output martingale, or build an exact k=2 witness where that mechanism fails and computable randomness is destroyed.
