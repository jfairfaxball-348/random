# P4-S112 — Exact transport classification, closed-chart conservation and robust tree switches

2026-10-12. One owner-invoked CAND-01 Phase4 mathematics session. Entry main `7a3c1e331ddd39889c2c882f1dcddfd7e53367c4`, sole parent `909d72b806a14421ddc2df54dfa94cd359f244d1`, tree `608394f0c26d04b6b155095405f490e571ea6407`; S111 PR #9 merged non-force at the entry commit. S112 unused at entry, Phase4 OPEN. This is internal proof development, not external refereeing, formal verification or a novelty finding.

**Results:** a necessary-and-sufficient classification of ALL keyed fair-homeomorphic deformations of a tree switch that remain everywhere exactly-two; a class-wide destruction obstruction even for coherent label mixing; CR preservation on computable-measure effectively closed double-inverse charts, beyond open charts; a fair exact-two counterexample to automatic computability of stratum measure; and preservation of **R2 itself** by every tree switch and every keyed fair-homeomorphic deformation. General DP2, CP2, EQ, SEP, R2 versus R_L1 and unrestricted F2(R2) subset R2 remain unresolved.

## 1. Definitions and mandatory S111 correction audit

CR uses ordinary total nonnegative rational computable martingales with unbounded capital as success. F2 consists of everywhere-total computable fair Cantor maps with at most two preimages of EVERY output; fairness forces onto. R2 consists of sources whose image is CR under EVERY such map (identity implies source CR). DP2 asserts CR preservation at every actual double source of any F2 map; CP2 restricts to everywhere exactly-two maps. EQ is R2=MLR; SEP requires ONE nonMLR source surviving ALL F2 maps and ALL ordinary total rational output martingales. No validity-decision algorithm is assumed.

Let T be a decidable prefix-closed binary tree containing the empty word, K=[T]. For v outside K, rho(v) is its shortest prefix outside T and c(v) is the immediately following bit. Put U_b={v outside K:c(v)=b}. These two effectively open sets partition the complement of K. The S108 map on x=a u is

    G_T(a u)=u                              if u in K;
    G_T(a rho b t)=rho a t                  otherwise.

Actual infinite inverses: over y in K there are 0y,1y; over y=rho c t outside K there are c rho 0 t,c rho 1 t. Conditional on the initial key a, its output law is the measure h_a lambda, where

    h_a = 1_K + 2 1_(U_a).

The law follows from the disjoint first-exit cylinders plus the residual K. Each output m-cylinder has two input (m+1)-cylinders, hence exact fair price. No statement identifies finite prefix candidates with actual inverses without this separate argument.

S111 uses P_0 equal to pair swap up to first forbidden block and P_1=id, with forbidden words sigma (00)^(2q+L) 11 for sigma of q complete blocks. First exits end at an even-length 11 block; swapping arbitrary complete blocks changes the arbitrary sigma but fixes every 00 and 11 in the constrained run. Therefore it preserves the first-bad depth and leaves c untouched after that depth. The geometric union bound is sum_q 4^(-2q-L-1)=(16/15)4^(-L-1), giving K mass at least 59/60 at L=2. A key-zero even row is permutive even if the next block is the first forbidden 11, because its two bits agree. Key-one rows are C0,C1. Thus true even-prefix rows are P,P,C0,C1 along K, while actual inverses remain just the two specified paths. The four-cell finite diagram is unsaturated.

The ordinary block martingale assigns d(P(s)) at even tail lengths and the average of the two grandchildren at odd lengths. Four-way bijection implies every binary martingale equation, including at the first bad 11; output odd capital is at most twice preceding even capital. This retains S111's symbolic and finite audit, including actual ramified CR sources and near-full ramification. Replaying its checker gives 84,903 finite assertions, not an infinity proof.

**Correction / strengthening C112-0.** S111 says CR preservation of its total computable measure-preserving homeomorphisms P_a must be an additional assumption and warns against inferring it from those hypotheses. That caveat is redundant under the repository's already verified E-ISO theorem: S001 proves the inverse of EVERY total computable fair homeomorphism computable and fair; S102 verifies Rute's original Theorem 7.11, which preserves CR in both directions. Therefore ALL such P_a automatically preserve CR, with no finite-block restriction. S111's proved family and rational compiler remain valid; no claim is quarantined. Preserve the original S111 files as historical and record this strengthening here and in live ledgers. Mere noninvertible fair maps still need not preserve CR.

## 2. Front C — full keyed homeomorphic transport classification

Allow arbitrary total computable fair homeomorphisms P_0,P_1; do NOT require either to preserve K or c. Define

    F(a u)=P_a(G_T(a u)),
    K_a=P_a(K),       A_a=P_a(U_a).

**Theorem C112-1 (exact counts and density).** For EVERY infinite y,

    N_F(y)=|F^-1(y)|=1_(K_0)(y)+1_(K_1)(y)
                         +2 1_(A_0)(y)+2 1_(A_1)(y).        (2)

The pushforward F_*lambda has Radon-Nikodym density N_F/2. In particular F is fair iff N_F=2 lambda-almost everywhere, whereas F is everywhere exactly-two iff (2) equals 2 at EVERY y. These assertions have different quantifiers.

Proof. Fix a key a and decode the UNIQUE v_a=P_a^-1(y). If v_a in K there is one tail inverse; if v_a in U_a there are two tails; if v_a in U_(1-a) there are none. Different initial keys give disjoint source sets. This exhausts the infinite inverse paths, proving (2). Since P_a is measure preserving, its conditional density is h_a(P_a^-1(y)). Average these two densities with key prices 1/2; their sum is exactly (2). Density equality is an almost-everywhere fact; the cardinal formula is pointwise. QED.

**Theorem C112-2 (necessary AND sufficient exact-two condition).** F is everywhere exactly-two (and consequently fair) iff

    K_0=K_1=:K',    A_0 disjoint union A_1 = complement(K').  (3)

Equivalently, set Q=P_1^-1 composed with P_0. Then

    Q(K)=K and Q(U_0)=U_0, hence Q(U_1)=U_1.               (4)

Every such F has the exact factorization

    F = P_1 composed with F_Q,
    F_Q(0u)=Q(G_T(0u)),    F_Q(1u)=G_T(1u).               (5)

Here Q is an exit-label-compatible homeomorphism in the S111 sense; the common outer P_1 may move K and mix its exit labels freely.

Proof. If y lies in K_0 symmetric-difference K_1, exactly one term 1_Ka is 1 and its own 1_Aa is 0. The remaining contribution is 0 or 2, so N_F is odd (1 or 3), impossible under exact-two. Thus K_0=K_1. On their common set both A terms vanish and N_F=2. Outside it the formula is 2(1_A0+1_A1), which equals 2 exactly when the A sets partition. This proves (3). Apply P_1^-1: K_0=K_1 gives QK=K. The partition condition becomes Q(U_0) disjoint union U_1=complement(K); hence Q(U_0)=U_0. Conversely (4) implies (3). Formula (5) follows on both keys and at every source. QED.

If both P_a preserve K, outside K the only possible counts are 0,2,4. Define d_a=c(P_a^-1(y)); then N_F=2(1_{d_0=0}+1_{d_1=1}). Exactly-two is equivalent to d_0=d_1, not necessarily d_a=c(y). Thus S111's pointwise c preservation is sufficient, NOT necessary. Coherent label mixing is legal; disagreement creates holes or four-point fibres. If K_0 and K_1 differ, 1 and 3 additionally occur. A fair continuous F cannot have an actual missing output: compact range and positive cylinder measure force onto, so an arbitrary 0-fibre candidate is not a fair F2 map.

## 3. Front A — coherent mixing works, but this whole attack class cannot destroy CR

Define a total computable fair homeomorphism R_T:

    R_T(v)=v                           on K;
    R_T(rho c t)=rho (1-c) t            off K.

Finite output m is computed by inspecting first exits before m; no infinite K-membership test occurs. The first exit rho stays unchanged. Flip exactly its following bit, an action whose location is decided by the earlier prefix. This is a computable binary tree automorphism and involution. Every level is permuted, so it is fair, fixes K and exchanges U_0,U_1.

Take P_0=P_1=R_T. Then F=R_T composed with G_T is globally fair and everywhere exactly-two, yet BOTH keyed postmaps change c everywhere off K. Over y=rho c t its inverses are

    (1-c) rho 0 t, (1-c) rho 1 t.

Over K they remain 0y,1y. This explicitly refutes the overbroad claim that legal mixing must preserve the old c pointwise. It is not a tagged disjoint-union construction. More generally choose S111's compatible Q (including its genuine ramified hybrid family), let P_1=R_T and P_0=R_T composed with Q. Formula (5) makes the resulting non-compatible keyed maps legal. On K, R_T is identity, so the same ramified double CR paths and infinitely recurring even hybrids remain. Off K the key sectors have exchanged. Ramification is unchanged by a common output homeomorphism.

By contrast P_0=R_T,P_1=id has count 0 on U_0 and 4 on U_1, density 0 and 2 respectively. When K is proper, its nonempty exit cones have positive mass, so this candidate is neither fair nor in F2. This is the earliest-exit counterexample to one-sided mixing; no numerical prefix count substitutes for its explicit infinite inverse proof.

Equal-depth output cone exchanges give additional legal mixing: transpose [rho 0 s] and [rho 1 s] for a first-exit rho by prefix replacement, fixing their complement. Both cones have equal fair mass, their transposition is a computable fair homeomorphism, and applying it COMMONLY to both keys preserves exact-two. More general common equal-measure clopen exchanges can move several exit cones. For arbitrary keyed proposed repairs, (3) is the exact constraint. Such repairs may correct counts but still stay in the conserving class.

**Theorem A112-1 (class-wide impossibility).** For EVERY T and EVERY total computable fair homeomorphisms P_0,P_1, EVERY CR source x has F(x) CR, regardless of whether F is fair or meets the fibre cap. In particular NO everywhere-exact-two member of this ENTIRE keyed deformation class can be a DP2/CP2 destroyer.

Proof. S108 proves G_T(CR) subset CR at every source by finite-tail equivalence. For the actual initial key a of x, E-ISO makes P_a preserve CR. The key a is a finite constant, not an oracle. Thus P_a(G_T(x)) is CR. This is stronger than conservation for S111's compatible finite-block family and includes all coherent label mixing in (3). It does NOT assert that arbitrary noninvertible fair P_a preserve CR. QED.

**Nonhomeomorphic transport attempt A2 (first unclosed lemma).** If P_a are instead arbitrary finite-fibre total computable maps, the exact cardinal equation becomes

    N_F(y)=sum_(a=0,1) sum_(v in P_a^-1(y))
                      (1_K(v)+2 1_(U_a)(v)).             (6)

Fairness separately requires

    (1/2) sum_a (P_a)_*(h_a lambda)=lambda.               (7)

There is no justification for density N_F/2 once P_a cease being measure-preserving bijections; (6) and (7) are independent obligations. This is where a genuine destruction route could escape A112-1.

Target cases examined: a two-point F-fibre can arise from one U_a tail image with multiplicity two, two K preimages on one key, or one K preimage on each key. The last could in principle place a known CR SINGLETON-destroying P_a path beside another key's K path. Globally, however, regular P_a double fibres must not hit supported sectors so as to create 3 or 4 F inverses, and (7) must still hold. Taking both P_a equal to the known destroyer fails exactly: sum_a h_a(v)=2 pointwise, hence N_F(y)=2|P^-1(y)|, giving four on every regular double output. Taking computable K wholly inside its ML-null singleton locus cannot retain a CR witness, since such effectively closed null K has no CR member. Different noninjective P_a and a positive-measure K with a compatible global partition remain possible, but no such all-output construction or ordinary rational winning output martingale was produced. This is a genuine unclosed design obligation, not a no-go theorem for all F2.

## 4. Front B — computable-measure closed double charts preserve CR

Recall S106's uniformly effectively closed strata

    D_r={y: two actual G-inverses have distinct length-r prefixes}.

For every G in F2 the computable inverse-precision c(r) gives at most two source r-prefixes over each output c(r)-cylinder. On D_r both are actual; their lex ranks are computable from this finite list. The charts h_(r,i) on D_r are partial computable and continuous with the recorded uniform precision c(max(n,r)). This is inverse information, not a conditional-mass oracle.

**Lemma B112-1 (closed injective source restriction).** Let G be total computable fair, and B an effectively closed source set with computable fair measure, such that G restricted to B is injective. Then every CR source x in B has CR output G(x).

Proof. If B has measure zero it has no CR member (CR implies Kurtz); the implication is vacuous. Otherwise Rute arXiv:1508.05082v2 Lemma15, whose statement and complete proof were inspected in this session, makes the submeasure beta(E)=lambda(B intersect E) computable and transfers a lambda-CR x in B to beta-CR. For cylinder measures, computability follows already from upper semicomputability of B intersect [sigma] and of B outside [sigma], whose sum is the computable total lambda(B).

Normalize beta by its positive computable total if desired. G restricted to the effective compact set B is a computable bijection onto the effectively compact image G(B). Its inverse is partial computable on that image by finite image separation of the disjoint compact pieces B intersect [sigma]. The computable pushforward nu=G_*beta and beta, with these inverse maps, satisfy E-ISO on their full-measure supports. Hence G(x) is nu-CR. Finally nu(E)<=lambda(G^-1(E))=lambda(E); Rute Lemma16, also proof-inspected here, transfers nu-CR to lambda-CR. Equivalently a computable measure ratio witness against lambda is also one against nu. The ordinary total rational convention follows from S101's explicit positive-factor rationalization; no ML-only conclusion is substituted. QED.

**Theorem B112-2 (closed double-chart criterion).** For every G in F2, every r, every effectively closed output C subset D_r with computable lambda(C), and every CR x with G(x) in C, G(x) is CR.

Full source-measure proof. B=G^-1(C) is effectively closed and lambda(B)=lambda(C) is computable by fairness. Define a TOTAL computable clopen source predicate Q_0 by: form the finite list of source r-prefixes meeting G^-1([G(x)|c(r)]); declare rank zero when x|r is its lexicographically least member. The list is nonempty and includes x|r on EVERY source. Set Q_1=complement(Q_0); put B_i=B intersect Q_i. On B the list has exactly two genuine prefixes, so G restricted to each B_i is injective and these sets partition B. Both B_i are effectively closed and their measures are upper semicomputable. Their sum is the computable lambda(B), so each has computable measure: an upper approximation for one and for the other supplies lower bounds via subtraction from the computable total. The same argument computes all cylinder intersections. Apply B112-1 to the sheet containing x. Zero-measure sheets contain no CR input and cause no problem. QED.

This criterion works on a nowhere-dense C and does NOT require local clopen injectivity at x, positive limiting sheet weights, or computable stopping prices. It thus goes beyond S106's interior(D_r) theorem. A certificate consists of C, its containment in D_r, and a computable name for its measure. The theorem is conditional on those data, not an algorithm deciding their existence for arbitrary G.

Corollaries: if EVERY double output is contained in some such certified C, then DP2 holds for that G; if each D_r itself has computable measure, then DP2 holds for that G and CP2 holds when it is everywhere exactly-two. Uniformity of the measure names in r is sufficient but not required for the pointwise mathematical implication. A purported universal solution still has to supply these certificates or some different compiler for ALL maps and ALL actual double sources.

**Counterexample B112-3: exact-two fairness does NOT force computable stratum measure.** Fix any undecidable c.e. set A. Let p_e=1^(2e+3)0. These words are prefix-free with weight 4^(-e-2). Enumerate [p_e] iff e enters A. Define the decidable tree T by placing s in T iff no e with p_e prefix s has appeared in A by stage |s|. This is prefix-closed: any excluded prefix remains excluded at later stages and lengths. Its paths are exactly

    K = complement(union_(e in A) [p_e]),
    lambda(K)=1-sum_(e in A)4^(-e-2) >= 11/12.            (8)

The real in (8) is not computable. If its complementary sum were computable, recover A(e) inductively: subtract earlier recovered terms; if e is absent the remaining tail is at most w_e/3, while if present it is at least w_e, w_e=4^(-e-2). Approximation error below w_e/12 distinguishes these cases. This would decide A.

S108's G_T is nevertheless total computable, fair, everywhere exactly-two and CR-conserving. Its D_1 is EXACTLY K: on K its two inverses have distinct initial keys, and off K its two inverses have the SAME initial key c(y). Therefore lambda(D_1) is noncomputable in an explicit valid F2 map. Late enumeration merely delays the first-bad prefix; it does not require a halting oracle to compute finite output. This falsifies the automatic-measure lemma, not DP2/CP2 or B112-2. This counterexample does not assert that every possible alternative closed-chart certificate around each point fails.

For S111's special K_L the measure IS computable: after enumerating all q<=Q forbidden patterns compute their finite clopen union exactly; the unexamined tail is at most (16/15)4^(-2(Q+1)-L-1). This is a computable error bound despite overlaps. B112-2 therefore supplies an independent-in-method closed-chart explanation of conservation at those ramified points (use its two separated key charts over K_L). The general noncomputable K example shows why that explanation cannot be silently extended to every tree, although S108's pointwise proof conserves all trees.

## 5. Front D — R2 itself survives this entire deformation class

The following source-wise argument addresses iterated robustness without assuming F2 closed under composition.

**Lemma D112-1 (homeomorphic invariance).** For every total computable fair homeomorphism H, H(R2)=R2. If x in R2, for arbitrary G in F2 the map G composed with H is total fair and has exactly the same fibre cap as G because H is bijective. Thus G(H(x)) is CR. Apply the same argument to H^-1 for equality. This is a definition-level transport fact, not a new EQ/SEP bridge.

**Lemma D112-2 (finite-prefix deletion).** If x=p u in R2 for ANY finite word p, then u in R2. For an arbitrary H in F2 and l=|p|, form the total map

    L_H(s v)=s H(v),             |s|=l.

It preserves fair measure: output prefix probabilities factor into the unchanged uniform finite tag and the fair H tail, including prefixes shorter than l. Above output s y, inverses are exactly {s v:H(v)=y}, of cardinality at most two. Thus L_H is in F2. For x=p u, R2 gives p H(u) CR; fixed-prefix martingale restriction gives H(u) CR. Since H was arbitrary, u in R2. This retains the key as an OUTPUT tag inside the witnessing map, avoiding the cap-four mistake in H composed with ordinary deletion. The lemma proves deletion; it does NOT claim arbitrary prefix insertion preserves R2.

Every finite modification of a point in R2 remains in R2 by D112-1 applied to the tree automorphism flipping the finitely many changed coordinates (hard-code that finite set).

**Theorem D112-3 (tree-switch R2 conservation).** For EVERY decidable T, G_T(R2) subset R2. Write the actual x=a u in R2. Lemma D112-2 gives u in R2. If u in K its image is u. Otherwise u=rho b t and its image rho a t differs from u at JUST ONE coordinate. That fixed finite-coordinate flip preserves R2. The exit coordinate need not be computable uniformly from every source to make this pointwise argument: at each actual off-tree source it is a finite integer. QED.

**Theorem D112-4 (keyed deformation R2 conservation).** For EVERY P_0,P_1 in Section 2, F(R2) subset R2. First D112-3 gives G_T(x) in R2; then D112-1 applied to the actual key's P_a proves the image in R2. No premise that F itself is F2 is needed. In particular every globally exact-two label-mixing map classified in C112-2 satisfies the requested iterated robustness inclusion. Finite compositions of these maps also preserve R2 even when their global fibre bound multiplies beyond two.

This is stronger than ordinary CR conservation for this family. It closes a restricted piece of the iteration question left explicit in S111, while the statement for EVERY F2 map remains unresolved. A conservative map outside L1 does not supply a SAME-source separation R2 strictly below R_L1: ALL CR, hence all R_L1 sources, survive every map of this deformation class. The SAME S083 witness remains in C and outside R_L1; it is not a witness for the unresolved first inclusion R2 subset R_L1.

## 6. Sustained EQ/SEP attempts and finishing gaps

EQ attempt E1: enlarge S111 to arbitrary coherent cone exchanges, common recodings and relative-compatible twists, hoping to turn nonMLR test entries into label bets. The complete classification (3)-(5) and A112-1 prove the resulting ENTIRE class CR-conserving. Even an infinite computable schedule of such changes, when it yields total fair homeomorphisms P_a, stays in that theorem. It cannot destroy ANY CR nonMLR source. If the limiting P_a is noninjective or not a computable homeomorphism, the theorem no longer applies; totality, (6), (7), and an ordinary rational winner must then be proved anew.

EQ attempt E2: choose nonhomeomorphic P_0,P_1 independently, make the nonMLR target a K singleton of one P_a and provide its partner via the other key. The target-level count two alone is insufficient: (6) must hold globally and (7) must price every cylinder. A shared known destroyer gives four points on regular outputs; a computable null K loses the CR source. No globally balanced pair covering EVERY CR minus MLR point was obtained. Universal ML-test membership still does not orient the two candidate source histories or supply a total rational betting strategy. No equality result.

SEP attempt S1: use closed-chart certificates to select one protected nonMLR point against all observers. B112-2 protects CR only at sources whose images lie in its certified closed sets. G and r vary, and B112-3 refutes automatic computable measure of the canonical strata. Even if all certified charts were listed, their intersection need not contain a nonMLR point and does not cover uncertified F2 maps. The effective bank from S105 still lacks the required nonMLR protected-source certificate. No SEP result.

Iteration attempt I1: argue F2(R2) subset R2 just because an F2 map preserves CR. This inference is invalid: testing H(F(x)) needs H composed with F, which may be cap four. D112-3/4 instead prove the restricted inclusion through explicit source deletion and finite-change/homeomorphic invariance, with an actual tag-retaining F2 test. A general F2 output has no such pointwise recoding proved. A failure outside this family would need ONE x in R2 and legal F,H in F2 with a total rational winner on H(F(x)); none was built.

## 7. Scope and proof grades

INTERNALLY PROVED: C112-0 correction; C112-1/2 exact counts, density and relative-compatible normal form; legal common label mixing and its one-sided 0/4 countermodel; A112-1 full keyed-homeomorphism CR conservation; B112-1/2 computable-measure closed-chart preservation; B112-3 noncomputable D_1 in a fair exact-two map; D112-1/2 invariance and deletion; D112-3/4 R2 preservation for the entire tree-switch deformation class.

UNRESOLVED: general DP2, CP2, EQ, SEP, R2 versus R_L1, unrestricted F2(R2) subset R2; nonhomeomorphic paired transport meeting (6)-(7) and providing an actual CR double source with a successful total rational output martingale. Finite checks corroborate projections and exact algebra only. Same-agent independent-in-method adversarial validation is not external or formal proof.

Frozen: original Y/M/H/X, DEF-0020, PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE, S101-S103 A-C, SRC-0067 ABSTRACT_INSPECTED and SRC-0068 PROOF_INSPECTED, original E-ISO source distinctions. The new use of SRC-0015 Lemmas15-16 has its proof-inspected scope recorded separately in S112_DEPENDENCIES; it does not retroactively change the historical Lemma8 grade or any source catalogue count. Gate3 PASS; Gate4 NOT REVIEWED; Phase4 OPEN; Phase5 CLOSED. No S113 execution, Lean, Palomar, manuscript, novelty campaign, outside contact or publication.
