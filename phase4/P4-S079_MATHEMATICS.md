# P4-S079 — Global unit-column raw one-hole extraction on the committed full-shear chain

Date: 2026-10-09
Scope: Phase 4 Mathematics ONLY; CAND-01; pinned incoming main a1f942bc4de29b4c9ae52f41a9e5b44cb1946534.
Disposition: **PROVED actual OH NONMEMBERSHIP for the six fixed intermediates z1,z2,z3,z4,z5,z6 of S078's original X-to-Y word; the fixed S-preservation proposition, X in OH, R2=OH and R2=OH^iso are UNRESOLVED.**

## 0. Authority, frozen objects and exact target

The live main matched the pinned SHA exactly. The incoming recursive tree contained one mathematics/validation/close triplet for each S001–S078 and no S079 file. Reviewed S001–S078 through the phase-4 summaries and the selected detailed mathematics, S078 validation/close, CAND-01 selection, P3-S008 Gate-3 PASS, both pivots; emphasis S011–S012, S032–S044, S057, S069–S078 and S033/S037/S070/S071/S077/S078.

Preserve the ORIGINAL computably random Y, the unchanged syntactically self-avoiding globally use-clipped wtt autoreduction M with M^Y(q)=Y(q), and the repeated H matrix A=[101;110;111]. Write X=H^{-1}(Y). S001 gives X in CR, and S011/S033 give Y=H(X) not in OH, X not in R2, X not in OH^iso. X in OH remains unclassified. Retain MLR subset R2 subset OH^iso subset OH proper-subset CR. By S078 the all-block S(a,b,c)=(a,b xor c,c) preserves OH on every OH source if and only if H does, but that proposition is still open inside the programme.

## 1. Global bridge: restricted sentinels with a compulsory real sweep

**Theorem 1 (infinite computable sentinel-family extraction).**
Let z be a computably random binary sequence. Suppose J is an infinite decidable set of RAW coordinates and, uniformly for j in J, a partial oracle procedure P(j) has the following two properties:
(a) every finite halting computation P^w(j), on every oracle w, reads no raw coordinate j;
(b) P^z(j) halts with the correct bit z(j).
No wtt use bound or totality on siblings is required. Then z is not in OH. More precisely a SINGLE everywhere-total computable adaptive no-repeat fair-coin-preserving RAW scan T_J with globally at most one omitted raw coordinate, and one rational nonnegative computable martingale d_J, succeed on z.

**Construction.** Maintain the finite table R of read raw coordinates and observed bits, reconstructible from the output transcript. At the beginning of each epoch choose j=least(J minus R), which exists because J is infinite and R finite. Keep j unread. At each stage run a bounded finite simulation of P(j) on the finite partial raw oracle R; increase the simulation-time bound with the number of emitted filler steps in the epoch. If a binary halt avoiding j is now visibly verified, bet ALL current capital on that predicted bit, query the fresh j, close the epoch, and then perform one genuine ZERO-STAKE sweep query at the least still-unread raw coordinate. Otherwise query the least unread coordinate other than j as a genuine ZERO-STAKE filler and repeat. On a nonbinary halt or any unverified computation, continue filling; never use nonhalting as a finite certificate. The martingale is constant on fillers/sweeps and has two children 2C,0 at a predicting sentinel, arranged according to the visible predicted bit.

**Every-transcript proof.** Each next query is found by a finite bounded simulation and a least-fresh search; all three query types read a genuinely fresh index, and no stage waits for an oracle computation. There are infinitely many real emitted bits on every input. A fixed output prefix determines the unique fresh queried indices from earlier output bits, so each output cylinder has fair-coin measure 2^{-length}. If an epoch never closes, its fillers enumerate EVERY coordinate except j (finitely many smaller non-j sites precede any given site), yielding precisely one permanent hole. If infinitely many epochs close, the mandatory sweep after EACH successful sentinel consumes the then least unread raw position. For every fixed n, after at most n+1 sweeps all positions through n are consumed (possibly earlier by other query types), so there are ZERO holes. Finite successful epochs followed by a permanent epoch are covered by the first case. Thus the global one-hole property holds on every transcript, independently of sibling partiality or how thin J is. The emitted scan and rational d_J are total and fair at every finite node. On z, a halting P^z(j) uses finitely many coordinates other than j; the least-fresh fillers eventually expose them, and the increasing time simulation witnesses the correct binary halt. Therefore ALL target epochs close and all target sentinel bets win, with d_J capital 2^e after e epochs. QED.

**Why the sweep is necessary.** Merely selecting sentinels in a sparse J and filling only until each halt can leave infinitely many untouched non-J sites on an all-trigger branch, violating the global one-hole condition. The single real least-unread sweep after every successful epoch is the essential global repair. It never consumes the current protected sentinel (already consumed) and does not require any negative convergence oracle.

## 2. A unit-column lemma for repeated invertible linear recodings

**Theorem 2 (source-specific unit-column OH exclusion).**
Let K be a fixed computable, uniformly effective, blockwise invertible binary linear homeomorphism on finite blocks, and let z=K^{-1}(Y) be computably random. Suppose there is an infinite decidable family J of raw coordinates j and a computable choice q(j) of a virtual coordinate such that the column of K at j has coefficient 1 exactly in row q(j), and coefficient 0 in EVERY OTHER output row. Then z is not in OH.

**Proof.** On input j in J, simulate the ORIGINAL M on virtual input q(j), answering each virtual query k other than q(j) by computing (K(w))(k) from the finite raw support of that output. Because the j-column vanishes at all k different from q(j), none of those answers ever requires raw w(j). M syntactically avoids its input q(j), hence the derived oracle procedure does not query raw j on ANY oracle. For its final predicted virtual bit b, compute the parity g_j of the OTHER raw coordinates contributing to output q(j), and output b xor g_j. The unit column gives K(w)(q(j))=w(j) xor g_j. Along z, M^Y(q(j)) halts correctly, all finitely many required raw answers away from j are accessible and the derived prediction is z(j). Theorem 1 now constructs an actual globally legal winning raw one-hole scan on z. No conclusion from the failure of a restricted compiler is used. QED.

The lemma is source-SPECIFIC and depends on the original target-total-on-Y self-avoiding M; it does not assert a theorem for arbitrary z in OH, nor invariance under K. Finite block effectiveness (three-bit blocks below) gives the required uniformly decidable dependency tables; globally clipped M is left unchanged.

## 3. Apply to every concrete S078 intermediate, with NO substitutions for X

Retain exactly the chronological S078 chain
z0=R(X), z1=S(z0), z2=Q(z1), z3=R(z2),
z4=S(z3), z5=Q(z4), z6=R(z5), z7=S(z6)=Y,
where R globally swaps a/b and Q globally swaps b/c. Every z_i is computably random by the original computable fair homeomorphism theorem. For each i define B_i by Y=B_i(z_i), with B_i the product of the REMAINING global three-bit factors (NOT the initial prefix). Exact F2 multiplication gives:

| i | B_i rows in block | column weights | one usable unit column j->q |
|---|---|---|---|
| 0 | 011/110/111 | 2,3,2 | NONE |
| 1 | 010/111/110 | 2,3,1 | 3k+2 -> 3k+1 |
| 2 | 001/111/101 | 2,1,3 | 3k+1 -> 3k+1 |
| 3 | 001/111/011 | 1,2,3 | 3k -> 3k+1 |
| 4 | 001/110/010 | 1,2,1 | 3k -> 3k+1 |
| 5 | 010/101/001 | 1,1,2 | 3k -> 3k+1 |
| 6 | 100/011/001 | 1,1,2 | 3k -> 3k |

For each i=1,...,6 select the displayed residue class J_i={3k+t_i : k>=0}, and use the ORIGINAL M to predict these raw bits through B_i as in Theorem 2. Every J_i is infinite decidable; the virtual row q is computable; the derived predictor is uniformly syntactically self-avoiding in raw coordinate j and total/correct on precisely the fixed z_i. Applying Theorem 1 separately yields SIX concrete (algorithmically specified by M and B_i) total global one-hole scans and rational martingales winning on z1,...,z6. Therefore

    z1,z2,z3,z4,z5,z6 are in CR minus OH.            (*)

In particular z6=S(Y) is now UNCONDITIONALLY classified as outside OH, and so are z3 and z4. This is not merely an algebraic reduction or restricted-compiler failure: each nonmembership has an explicit legal raw scan and winning martingale. The construction does not alter Y,M,H,X and makes no oracle-specific choice of a halting time.

**Corollary 3 (only the first of S078's three transitions can be an OH exit).**
The sources z3 and z6 of the SECOND and THIRD S transitions already lie outside OH by (*). The destination z1 of the FIRST S transition is outside OH by (*), and z0=R(X) satisfies z0 in OH iff X in OH by S033. Consequently:

- IF X in OH, the explicitly fixed pair (z0,z1) is an ACTUAL counterexample to full-support S preservation, and R2 is a PROPER subclass of OH.
- IF S preserves OH universally, z0 and hence X must be outside OH.
- Without either premise, X in OH and R2=OH are NOT decided. Nonmembership of z1 gives no proof that z0 is in OH. Lack of a unit column for B_0 gives no proof that z0 is in OH.

This is a strict refinement of the earlier three conditional witness candidates: the last two cannot qualify because their sources are known NOT to be in OH.

## 4. Scope and failed routes

The missing bridge is now *membership of the single specific* z0=R(X) in OH, equivalently X in OH. The fixed full S may preserve OH universally or not; S079 proves only that the committed first output S(z0) is demonstrably bad while the input has not been classified. Neither R2=OH nor the logically separate R2=OH^iso follows.

Do NOT infer (i) z0 in OH from absence of a unit column, (ii) universal nonpreservation from z1 notin OH alone, (iii) global S-preservation from the five other exclusions, or (iv) success of an arbitrary future-wager price compiler. The earlier S071 spoiled-wager exposure and S037 effective renewal boundary remain untouched. This route needed no price, deadline, inventory, S057 controller, future wager, sibling nonhalting certificate or infinite-limit compactness.

## 5. Validation and disposition

The finite GF2 audit in P4-S079_UNIT_COLUMN_AUDIT.py verifies the exact eight-factor H word, all seven B_i, B_i times the chronological prefix equals A, all eight assignments per block, every asserted unit-column independence under flips of its raw input bit, and the absence of any unit column in B_0. These finite checks support the matrix portion only; the all-infinite-transcript legality, target-trigger convergence, and fair martingale are proved in Theorem 1.

Freeze S001–S078 including S011/S012, S033, S037, S057 (exact four clipped paired traces, prospective deadlines, genuine fillers, t/u zero-stake timeout release, mandatory non-s sweep without old reset, seven 8/7 vs one ZERO), S070–S078, S073 joint-price accounting, S074 sharp 3/16, S075 savings, S076 multistage, S077 finite support, S078 identities. S057 NOT invoked. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach conclusion. No owner/external blocker. Next P4-S080 must attack z0 membership or all-source fixed-S preservation, not continue residue tables.
