# P4-S074 Validation — rolling two-claim joint-price escrow

Date: 2026-10-09
Incoming exact remote main: 71ad3437aa4a0c9f22b0567a9c12da8b07812409
Disposition: **PASS — conditional infinite-chain financing theorem; global source-scan legality; quantitative all-stage bound. Universal preservation unresolved.**

## Authority and uniqueness — PASS

Independent live remote main ref equalled incoming S073 outgoing SHA; its commit parent was 9394fc898b1f152666524d27c1e60d037f658e4a. Recursive pinned tree had S001–S073 records, no P4-S074 mathematics/validation/close; P4-S074 appeared only as forward direction. P4-S001–S073 mathematics inspected, including emphasized S008/S011/S012/S027/S032–S044/S052–S057/S065–S073; S073 mathematics/validation/close, S034–S037, S070–S072, CAND-01 P3-S007 selection, P3-S008 Gate 3 and both pivots reviewed. No original Y/M/H/X, S057 controller, theorem or gate altered.

## Global scan and stake legality — PASS

The virtual T is the explicit recursive permutation from the mathematics: startup v0,v2, followed by each group's next v, next u, next v, current two w, and finite cleanup. Check inductively that v_{4i},v_{4i+2},u_{4i} were queried in the preceding group, with the special u0 cleanup; every virtual u,v,w appears once and at finite time on EVERY path. The S071 raw P on E=all or E=even is EVERYWHERE total, fair-coin preserving, no-repeat and exhaustive; for selected v a REAL fresh c is queried before b and the later w is silent. None of the new bets changes raw queries.

At w_{4i}, the stake q R_{i-1} R_i depends on previously read virtual u_j and u_{j+4}, with constant R_-1=1 for i=0; at w_{4i+2}, q R_i is already known. No stake sees its own virtual w value. At the real c_{4i+2} funding bit, C_{i,0} and R_{i-1} are already known, so its Q child factors 1+-q^2 average one BEFORE that bit. At the real a_{4i+4} pivot, C_{i,0}, C_{i,2}, R_{i-1} are already known, so its F child factors G_i(+)/pi_i,G_i(-)/pi_i average one BEFORE that pivot. All prices/factors are strictly positive for fixed rational 0<q<1; algorithms are uniform total on every finite raw history and use no future stake or negative halting certificate.

## Exact escrow algebra — PASS

Price pi_i=1+q^2 C_{i,0}C_{i,2}R_{i-1} is credited to Q at real c_{4i+2}, then charged to Pi at real a_{4i+4}; \(\Pi\) includes retired prices, while A includes only credited unsettled w multipliers. F Pi=d A at every completed virtual stage because d has no live bets. Q and F bet at DISJOINT raw coordinates, so e=Q F (unlike a generic product of martingales) is one fair raw martingale. Exact e/d=A Q/Pi. At most one price is prefunded and not yet charged, and at most two claims are simultaneously credited and unsettled. Therefore Q/Pi >=1-q^2 and A>=(1-q)^2 at EVERY stage. At q=1/2 the bound is 3/16, sharp via G_i=1/4 and next pi=3/4. No packet-boundary equality is asserted: after group i closes, e/d=pi_{i+1}, generally not one.

The next group is started before old claims settle; its second price finance is transacted between the old pivot and old w settlement. The next group's first claim's stake uses R_i, an essential dependency on the old group's shared pivot. The graph on block groups is an infinite linked chain; no empty pending-w frontier occurs after v0, no disjoint block-aligned finite closed packetization exists. This does NOT negate S037 effective fresh-frontier renewal or classify every alternative packet formalism.

## Exact rational finite audit — PASS

Finite enumeration: 3 groups settled, fourth group prefunded, two c signs per 4 group pairs plus 3 fresh a pivot signs = 11 relevant signs. For each E=all and E=even, enumerate all 2048 sign assignments (4096 cases total). At each of **159744 completed virtual checkpoints** check:
- raw and virtual coordinate no-repeat;
- selected-v real c filler before b; selected-w silent handling;
- Q and F child averages exactly one, without new-bit access;
- F*Pi=d*A, e=Q*F=d*A*(Q/Pi) in exact rational arithmetic;
- Q/Pi>=3/4 and A>=1/4;
- e/d>=3/16.

**Result: zero discrepancies; actual minimum e/d=3/16, reached at 1536 audited checkpoints.** Unused raw b/odd-c/other-a values are arbitrary because all bets hold there; the all-branch proof is structural, not inferred from exhaustive finite outcomes. The infinite mathematical proof is the explicit schedule, total wagers and product identity, not the finite check.

## Failed methods and explicit exclusions — PASS

Multiplying same-pivot g_i factors without joint normalization is unfair when correlation price differs from one. Betting the already-known pi_i on both children at its own a pivot is unfair. Counting only two open claims or claiming Pi bounded ignores premiums of settled groups. Finite conditional prices are not automatic computable infinite escrow prices. No universal total registrar, negative divergence certificate, X-specific success, R2 equality or H-preservation result is asserted.

Freeze original Y/M/H/X and all S001–S073. Exact S057 four paired globally clipped traces, prospective deadlines, REAL fillers, zero-stake t/u release, compulsory non-s sweep WITHOUT old-sentinel reset and seven 8/7 vs one ZERO preserved but not invoked. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE, DEF-0020 unchanged, Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty/openness/prior-art/publication/outreach claim. Owner/external blocker NONE.

Outgoing remote SHA will be independently verified after an atomic authoritative-files commit; never guessed inside this pinned validation record.