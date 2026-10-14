# P4-S132 — additive-two global two-sheet rigidity, an explicit triple factorization, and the finite-fibre boundary

14 October 2026; ONE owner-invoked Phase4 CAND-01 mathematics session. Live ENTRY main 917337721afcdd9c10c5e85d89dad0a04668ea39, actual S131 one-parent authored commit with parent ea116e7671b95ce7f0e40238cc5e59a0eceb4d10 and tree b5330652ad4815ded3a5284be435879256469a7a; PR #30 merged by direct non-force fast-forward. Incoming S132 archived exactly. No competing S132 records/open PRs at entry. All proofs here INTERNAL and the hostile review is SAME AGENT.

Throughout X=2^omega with fair coin measure lambda. F_k are ALL total computable globally fair maps with <=k ACTUAL infinite inverses at EVERY output (not merely <=k compatible finite words), and R_k universal CR-image preservation; R_fin=intersection_k R_k. Additive use c means the first m output bits are determined by m+c input bits. CR uses ordinary nonnegative total rational martingales.

## A132 — a new special-case global two-sheet 2:2 rigidity theorem

**Theorem A132-1 (INTERNALLY PROVED).** Suppose G:X->X is total computable, fair, additive use c=2. Suppose B0,B1 are disjoint clopen sets PARTITIONING X, and each restriction G|B_i is an injective map ONTO ALL X. Thus every y has precisely TWO ACTUAL inverses, one in each sheet. Then for every sufficiently large m, and EVERY output word tau of length m, EXACTLY TWO of the four source (m+2)-words above tau lie inside each sheet. Consequently lambda(B0)=lambda(B1)=1/2 and each restricted sheet sends its unnormalised source measure to (1/2)lambda. In particular an observer in this class can have NO infinitely recurrent 3:1/2:2 two-cone excursions.

**Proof.** Choose m0 so m+2 is at least the clopen resolution of B0 and B1 for m>=m0. For every tau of such length define q_i(tau) by counting all compatible length-(m+2) source cells within B_i. Exact global fairness gives q0+q1=4. Onto each sheet ensures q_i>=1, so q0 is in {1,2,3}. Binary child-count conservation gives q0(tau0)+q0(tau1)=2q0(tau). If q0(tau)=1 then BOTH children have 1 and inductively all descendants have 1. If q0(tau)=3 then BOTH children have 3 and inductively all descendants have 3. Each extreme forces one of the two sheets (call it B) to have constant q_B=3 throughout the subtree of tau.

Here is the decisive obstruction, without assuming global stationarity. The three compatible length-(m+2) cylinders [s1],[s2],[s3] inside B map (by the homeomorphism G|B onto X) to disjoint CLOPEN subsets A_i of [tau], whose union is [tau]. Since the subtree count is CONSTANT 3, for any Borel A subset [tau] we have lambda(B intersect G^-1(A))=(3/4)lambda(A), initially for output cylinders and then by measure extension. Hence for each i,

    2^(-(m+2)) = lambda([si]) = (3/4)lambda(A_i),

so lambda(A_i)=2^(-m)/3. Every clopen subset of Cantor fair measure has DYADIC rational measure; 2^(-m)/3 is NOT dyadic. Contradiction. Thus q0 cannot be 1 or 3 at ANY sufficiently deep output word, and must equal 2 throughout. Summing over target words gives lambda(B_i)=1/2, and the cylinder identity lambda(B_i intersect G^-1[tau])=(1/2)lambda[tau] extends to all Borel sets. QED.

**Scope check.** This is a global clopen-sheet rigidity theorem, NOT a universal additive-two F2 theorem. It does not apply to degree-two fibres without global ONTO clopen splitting, nor to degree-one fibres, nor to c>=3; S131's c3 triple example is unaffected. S131's local 3->2 row has sibling (4,0), precisely violating global two-sheet onto. The local transition graph itself is unchanged.

**Serious failed A attempt.** Start from the S131 3:1->2:2->3:1 local rows and try to complete every sibling while maintaining a global two-sheet homeomorphic cover. The 3->2 step forces a sibling entirely inside the triple cone, so that second sheet has no inverse there. With full global onto imposed, q=3 instead propagates 3:3 to both target children and triggers the local dyadic obstruction above. Removing global clopen onto sheets remains the unfixed hard problem; no SAME-SOURCE R2-destroyer, universal normalized F2 detector or valid cap-three output winner is produced. At degree one the two-cone argument does not apply: eventually all four finite aligned candidates remain in a single cone, and the appropriate source capital compiler is still missing.

## B132 — nonstationary c3 five-surplus destroyer attempt, and the precise obstruction encountered

Revisited S131's eight root tags A:{000->0,001->10,010->11}; B:{011->1,100->00,101->01}; C:{110->0,111->1}, followed by the first-two-output-bit involution K. All infinite fibres are exactly three, output law globally fair, and the aligned sheet vector varies (3,3,2) at root then (2,4,2)/(4,2,2). The three globally ONTO injective clopen sheets already certify all-CR preservation by S131. Permuting sheet labels on finitely many CLopen output sectors is not an escape: for a finite clopen partition (U_j) and label permutations pi_j, the proposed sheets union_j [B_(pi_j(i)) intersect G^-1(U_j)] remain clopen and each has exactly one actual inverse over every output. Source conjugation by any computable fair homeomorphism likewise transports the clopen cover.

To escape this firewall one needs a genuinely non-clopen, infinite-accumulation loss of globally selectable onto singleton sheets; merely raising additive overhead, swapping finitely many coordinates or changing a finite-prefix row cannot suffice by itself. Tried to couple an infinite noncomputable ACTIVE path to the c3 five surplus cells. The first failed proof line is that a finite consistent row table along ONE path would imply global fair completion and <=3 FULL inverses on every sibling: it does not. A fully specified all-output c3 branching observer with a Schnorr-random nonCR target and three genuinely CR inverses has NOT been constructed. No hardcoded noncomputable target or false R2 assertion is introduced.

## C132 — explicit F2 o F2 FACTORIZATION of B131's fair EXACT-three map

**Theorem C132-1 (INTERNALLY PROVED).** The actual nonstationary fair minimal-additive-three G=K o G0 from B131 DOES factor as H o F, where H,F are each total computable globally fair with <=2 ACTUAL inverses per output.

For the three source sheets A,B,C of G0, their output-density contributions relative to lambda are, on ORIGINAL output first bit 0: A=1/4, B=1/2, C=1/4; on first bit 1: A=1/2, B=1/4, C=1/4. These identities hold on ALL finer cylinders, not merely first-bit prices, because each tag is a complete finite-prefix homeomorphic chart. K swaps the first two output bits and is fair, so for actual y=G(x) the relevant ORIGINAL first bit is (K^-1(y))_0=y_1.

Define the computable selector J(y) = B if y_1=0, and A if y_1=1. For every output y EXACTLY ONE of its three inverses belongs to J(y); the selected-sheet pushforward unnormalised source measure has density EXACTLY 1/2 relative to lambda on ALL output cylinders (the complementary two inverses together give the other half). Let b(x)=1 iff the original root sheet of x is J(G(x)), else 0. Define

    F(x) = b(x) concatenated with G(x),       H(b y)=y.

Both are total computable. H is the ordinary fair delete-first-bit map, with two ACTUAL inverses. For EVERY output cylinder [tau], including those crossing the first two bits, exact half-density gives

    lambda(F^-1([1 tau])) = lambda(F^-1([0 tau])) = (1/2)lambda[tau].

Thus F is globally fair; for every infinite y the fibre of F above 1y contains EXACTLY ONE actual inverse, and above 0y EXACTLY TWO; no hidden inverse or missing sibling exists. Hence F∈F2, H∈F2 and H o F=G identically. QED.

**General exact criterion (C132-2).** Let any total computable globally fair G have exactly THREE ACTUAL inverses over every output. If a computable bit b(x) selects exactly ONE inverse over each y (b=1), and lambda(G^-1(A) intersect {b=1})=(1/2)lambda(A) for ALL Borel output A, then F(x)=b(x)G(x) is total, fair and in F2, and G=shift o F is an F2 o F2 factorization. Conversely a factorization specifically of this tagged-delete-bit form with one b=1 inverse per y requires that half-measure selector identity. This is a sufficient/class-specific equivalence, NOT an iff for arbitrary F2 factorizations. The half-density condition, not merely the existence of a pair of inverse paths, is essential.

The original S131 B131 map is therefore emphatically NOT a candidate nonfactorable F3 observer. It remains CR-preserving and does not establish F2(R2)⊆R2 or R2=R3: a composite has up to FOUR inverses in general, and x∈R2 gives only F(x)∈CR, not F(x)∈R2. Nonfactorable F3 remains open.

## D132 — exact dense-open continuity rigidity and a nontrivial safe boundary action

Take the S130/S131 total fair pointwise-finite fat-boundary map G_t, with closed nowhere dense C_t and dense open U_t=X\C_t. **Lemma D132-1.** If another continuous map Q:X->X agrees with G_t at EVERY point of U_t, then Q=G_t everywhere: choose u_n in U_t converging to any c in C_t and apply continuity of Q and G_t. Thus a boundary-only change while holding ALL existing open patch formulas fixed cannot alter any C_t value, regardless of computability or fairness. Changing the action coherently must alter patches arbitrarily close to C_t.

A positive but NONDESTRUCTIVE comparison: let T flip every output bit, a computable fair homeomorphism with no fixed point. Then F_t=T o G_t is total computable globally fair with exactly the same finite fibre cardinalities over transported outputs, and its local-unbounded-degree locus is T(C_t). Every c in source C_t maps to T(c) not c, including actual MLR/R_fin points. Nevertheless F_t preserves CR of EVERY source: G_t preserves CR by the S130 patch proof and T by fair computable homeomorphic isomorphism. This shows NONIDENTITY on the boundary is possible if the adjacent patches are changed too; it does not provide any R_fin destroyer. In particular high lambda(C_t) or moved boundary is not sufficient.

## E132 — independent central attempt, quantified failure and audit

Tried using the three-sheet construction as a hierarchy separator: invalid immediately because every CR source image is CR by the full-sheet firewall and because C132 supplies an explicit F2 factorization. Tried turning globally clopen two-sheet 3:1 oscillations into an R2 detector: A132 instead shows such oscillations impossible in that special class, not in general. Tried to infer F2(R2)⊆R2 by writing any candidate G as H o F: invalid because the definition supplies F(x)∈CR only. Tried deriving a nonMLR R2 survivor from S101's OH/block-safe witness: S101's claim C explicitly has ONE F2 observer destroying that SAME nonMLR witness, so it is NOT an R2 survivor.

Unresolved: general R2=R3 (and a SAME x∈R2\R3), R2=MLR or ONE R2\MLR source, R3=MLR, R2 vs R4 and F2(R2) closure, genuinely nonfactorable F3, global c3 three-CR-over-nonCR construction, and a pointwise-finite bad image of ONE x∈R_fin. Universal quantifiers are neither replaced by finite audits nor by separate x_k.

Hostile five-session audit S127–S131: S127 cap multiplicativity and normalized T_k fibre count remain distinct from class closure; S128 surplus rotation and selector are compatible with C132's special selector, not a general factorability theorem; S129 A odd-one-surplus source rotations are at c2/r3 not A132 c2/r2, and B129 F2 normalization needs permanently balanced target siblings; S130 dyadic proof requires stationary sectors and D130 patch map fixes C; S131 K swaps bits and half-sheet prices depend on the SECOND actual output bit. We found no definitive additional fatal historical line in these scoped spot checks; no exhaustive historical verification, external referee, Lean or Palomar is claimed.

Gate3 PASS; Gate4 NOT REVIEWED; Phase4 OPEN; Phase5 CLOSED. Frozen Y/M/H/X, DEF-0020, PA-0001, sources, S101–S103 A–C unchanged.
