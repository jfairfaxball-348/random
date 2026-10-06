# P4-S032 close

Date: 2026-10-06
Session: P4-S032
Incoming checkpoint: 26c86b254410806dac04ddb57584d97b0da7da1c
Scope: sustained Phase-4 finite-ambiguity pivot; reconnaissance and theorem selection
Status: **COMPLETED**

## Result

P4-S032 completes the required reconnaissance and selects the next theorem programme.

The robustness classes are now explicit:

R_k = {x in CR : every total computable fair-coin-preserving map with fibres <=k sends x to CR},

R_fin = intersection over finite k of R_k.

Settled mathematics gives R_1=CR, R_{k+1} subseteq R_k, and P4-S011 gives R_k proper-subset CR for every k>=2. THM-0035 additionally gives MLR subseteq R_fin. THM-0036 shows that every total computable fair-coin-preserving image of a computably random source is at least Schnorr random, so the P4-S011 failure lives exactly above the Schnorr level rather than destroying all weaker randomness.

The main new structural theorem is **null-ambiguity preservation**: if a total computable fair-coin-preserving map is injective on almost every output, then the singleton-fibre locus supports an a.e.-computable fair-coin-preserving inverse, so THM-0038 forces computable-randomness preservation. This requires no finite global fibre bound and no effective-null presentation of the ambiguity set.

The boundary is sharp in measure but not characterizing. Localizing the P4-S011 destroyer inside an arbitrarily small cylinder gives global-k=2 destroyers with positive output ambiguity measure below any prescribed epsilon. Conversely P4-S002's exactly-two-to-one left shift has ambiguity measure one and preserves computable randomness. Hence ambiguity mass is not the invariant.

Composition gives F_j after F_k multiplicity at most jk and the transport rule F_j(R_jk) subseteq R_k. This also shows why binary factorisation alone would not imply R_2=R_4: the intermediate image would need to retain R_2 robustness, not merely computable randomness.

For adaptive no-repeat scans, the exact fibre size is 2^h where h is the number of never-queried source coordinates. Thus k=2 is exactly a one-hole budget in that subclass. The P4-S011 vulnerable source nevertheless ends on a singleton fibre: its resource is not a permanently hidden bit but a renewable, migratory counterfactual hole used to place self-avoiding wagers.

The selected target is therefore **one-hole normalization**. Let OH be the computably random sources robust under every total computable adaptive no-repeat scan with at most one omitted coordinate on each transcript. Then R_2 subseteq OH, MLR subseteq R_2, and P4-S011 shows OH proper-subset CR. The next programme asks whether R_2=OH. A positive answer normalizes arbitrary k=2 destruction to the P4-S012 self-avoiding stake mechanism; a negative answer must expose a genuinely non-scan resource.

## Selection rationale

One-hole normalization outranks the other routes because it is source-side, explains the k=1/k=2 jump dynamically rather than by final fibre size, already has the P4-S012 converse machinery, and has informative outcomes in both directions.

The ambiguity-mass route has already reached a sharp zero-versus-positive boundary but is not a full invariant. Direct hierarchy questions are too coarse without a mechanism for arbitrary k=2 failure. Factorisation alone is insufficient without hereditary robustness.

## Guards

All mathematics through P4-S031 remains frozen and preserved. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made. Phase 4 remains OPEN and Phase 5 CLOSED.

Owner/external blocker: **NONE**.

## Next bounded task

P4-S033: begin the one-hole normalization programme. Formalize OH and test whether an arbitrary global-k=2 destruction witness can be converted to a one-hole adaptive no-repeat scan/stake witness, starting from the P4-S002/P4-S007 effective width-two inverse skeleton and using the P4-S032 null-ambiguity theorem to remove the a.e.-injective case.
