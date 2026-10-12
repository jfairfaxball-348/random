# P4-S113 — Noninjective tag transport rigidity and all-k finite erasures

Date 2026-10-12. One newly owner-invoked CAND-01 Phase4 mathematics session. Entry LIVE main 3092dd2abe916b961d7357addf93e8c67e877c8b, with sole parent 7a3c1e331ddd39889c2c882f1dcddfd7e53367c4 and tree 0237df759e0af4b00970f4accf67ab9d61e43592. S112 PR #10 was closed/merged at this atomic SHA; no open PR or S113 branch or record was present. Phase4 OPEN. Internal proofs only, no outside novelty or refereeing.

## 1. S112 correction and dependency audit

For decidable prefix-closed T, K=[T], a point v outside K has a FIRST forbidden prefix rho and post-exit bit c(v) immediately AFTER rho. The original S108 map is G_T(a u)=u for u in K, and G_T(a rho b t)=rho a t off K. For EVERY output y in K the complete actual inverse set is {0y,1y}; for EVERY y=rho c t outside K it is {c rho 0 t,c rho 1 t}. This dichotomy exhausts infinite paths. Conditioned on source initial key a, the output has density

    h_a(v) = 1_K(v) + 2*1_Ua(v),       h_0+h_1=2,       (1)

where U_a is the effectively open off-K set with post-exit bit a. Boundary points are in K and counted, not guessed from finite candidate rows.

S112's homeomorphic keyed theorem remains valid under its REAL hypotheses: when P_a are total computable FAIR HOMEOMORPHISMS, N(y)=1_(P0K)+1_(P1K)+2*1_(P0U0)+2*1_(P1U1), and exact-two everywhere iff the residual K images coincide and the two moved U sectors partition the complement. The relative Q=P1^-1 P0 must preserve K and U0. Verified E-ISO makes every such P_a preserve CR, correcting S111's unnecessary additional assumption. S112's computable-measure closed C subset D_r yields computable masses on BOTH effectively closed rank sheets by subtraction from computable total lambda(G^-1C)=lambda(C); zero sheets contain no CR inputs. Its halting-coded G_T has D1=K of NONCOMPUTABLE measure, so this sufficient chart criterion is not automatic. The S112 R2 prefix deletion test RETAINS its finite output tag; composing arbitrary two-fibre tests directly could raise capacity to four. The reconstructive audit found no fatal gap in these restricted S112 claims. No new primary source inspection or historical access-grade upgrade is claimed.

## 2. Front A — genuine nonhomeomorphic key transport, all-output count and price

Use a different keyed postmap, deliberately not a homeomorphism:

    P_a(v)=a shift(v),    P_a(0w)=P_a(1w)=a w.

It is total computable, NONINJECTIVE, maps onto the proper tagged cone [a], and is not individually fair. Define

    F_T(a u)=P_a(G_T(a u))=a shift(G_T(a u)).            (2)

This is an original-source additive-lookahead-one map. Unlike S112's homeomorphic class, the key is now visible in the first OUTPUT bit.

**Theorem A113-1 (all-output fibre count and exact density).** For EVERY infinite output a w, even on K-boundary paths,

    N_T(a w) = h_a(0w)+h_a(1w).                          (3)

The image measure of F_T has density N_T/2. Thus F_T is fair iff N_T=2 almost everywhere, while it is everywhere exact-two iff N_T=2 at EVERY output.

Proof: the first output bit forces the input key a. The unique intermediate v=G_T(a u) must be 0w or1w, and its number of ACTUAL tail inverses on key a is exactly h_a(v), by the explicit first-exit inverse formula. This exhausts all infinite inverse paths. On key a, v has conditional law h_a lambda; applying shift gives density [h_a(0w)+h_a(1w)]/2 on tail w. The key itself has exactly fair input mass one half and reappears as the output tag, leaving the identical full-output density N_T/2. This calculation is SPECIAL to this shift: equation (6) of S112 does NOT generally imply the fair-price equation (7) for arbitrary noninjective transports. QED.

Define a bounded signed stopping-bit function

    f(v)=h_0(v)-1 = 0 on K, +1 on U0, -1 on U1.
    N_T(0w)=2+f(0w)+f(1w);
    N_T(1w)=2-f(0w)-f(1w).                              (4)

**Theorem A113-2 (all-tree rigidity, PROVED INTERNALLY).** For EVERY decidable prefix-closed T with the root, these are equivalent: (i) F_T fair; (ii) F_T has exactly two ACTUAL inverses for EVERY output; (iii) K is the entire Cantor space. For EVERY proper K, an explicit nonempty finite output cylinder has a NONFAIR price. This remains true for unpruned T with dead ends, fat noncomputable K, zero sheets and infinite boundary paths.

Proof: if K is all space, G_T(a u)=u and F_T(a b t)=a t. This deletes the second input coordinate: exactly two inverse sources a0t,a1t and exact fair cylinder prices, proving (iii) implies (i),(ii). Theorem A113-1 proves (ii) implies (i).

Conversely let K be proper. Choose w and a key b such that b w is off K. For b=0,1 define j_b(w) to be the index in the COMMON suffix w of the bit immediately AFTER the earliest forbidden prefix of b w, or infinity if b w stays in K. Some j_b is finite. Put j=min(j_0,j_1) and sigma=w restricted to j+1 bits. Condition a fresh fair suffix W to lie in [sigma]. Every branch b whose j_b=j has its first forbidden prefix AND following bit already fixed by sigma, hence f(bW) is the constant epsilon=+1 if w_j=0, otherwise -1. If BOTH j_b=j, the two fixed signs are the SAME, because the post-exit bits refer to the same w coordinate. On every other branch the following bit at its first exit has NOT YET BEEN READ after conditioning on sigma. The conditional mean of f(bW) on this branch is exactly ZERO: decompose the later-first-exit set into countably many disjoint finite forbidden-prefix cylinders; each has the two equally probable post-exit children with signs +1 and -1; the never-exit residual paths have f=0. This is valid without a computable stopping time, stopping-price oracle, or exclusion of infinite paths.

Hence conditional on [sigma] the mean of f(0W)+f(1W) is epsilon or 2epsilon, never zero. Formula (4) says the average density of F_T on positive output cylinder [0sigma] is 1+epsilon/2 or 1+epsilon, NOT one. Thus fair-price conservation fails. K must be full. QED.

**Independent pointwise check.** Suppose N=2 at ALL outputs. If one of 0w,1w belongs to K and the other not, (3) has odd cardinal 1 or3: impossible. Thus K must be invariant under flipping the FIRST intermediate bit. On any common double-exit suffix, two c bits must oppose to make cardinal two. Take the earlier c bit and continue the suffix indefinitely with that same bit; the other branch remains off K by symmetry, must eventually exit and read precisely that same later bit, giving 0 or4 inverses. Contradiction. This checks EVERY-output exactness by another method, while the preceding conditional-measure argument also gives a positive mispriced CYLINDER.

**Corollary A113-3.** The sole fair map in this tagged nonhomeomorphic family is F_T(a b t)=a t, a fixed single-coordinate deletion; it is in F2 and cannot destroy CR or R2 (proof in Section 3). Proper-tree F_T is not a legal F2 witness, even if its proposed target has two actual sources. No arbitrary nonhomeomorphic cardinal/density equivalence is claimed.

## 3. Front E/D — FINITE COORDINATE ERASURE theorem for every R_k

Let R_k mean survival as CR under EVERY fair total computable map with fibre cardinal at most k, for any fixed positive integer k. For a total computable fair homeomorphism H, H(R_k)=R_k: composition G composed H remains fair, total, with precisely the same fibre bound; apply H^-1 for equality.

**Theorem D113-1 (PROVED INTERNALLY).** If x is in R_k and S is ANY finite set of input-coordinate indices, the subsequence x with EXACTLY coordinates S deleted, retaining the order of all remaining bits, is again in R_k. Fixed finite permutations and fixed finite flips of coordinates preserve R_k bijectively. No uniform computation of S from x is needed for the pointwise conclusion.

Proof. Choose N larger than every coordinate in S. Permute the FIRST N coordinates so the indices in S come first and the remaining indices in their original order; leave every index at least N fixed. This is a TOTAL COMPUTABLE FAIR HOMEOMORPHISM H with computable fair inverse, so H(x) belongs to R_k. Write H(x)=p u, |p|=|S|. Then u is EXACTLY the requested subsequence. For arbitrary G in F_k define the TAG-RETAINING map

    L_G(sv)=s G(v),     with |s|=|p|.

Every output prefix shorter than the tag has its fair price; longer prefixes factor into an unchanged fair finite tag and the fair G price. Over output s y the input fibre consists exactly of {s v:G(v)=y}, hence cardinal <=k, NOT 2^|s|k. Thus L_G belongs to F_k. Robustness of H(x)=p u gives p G(u) CR for EVERY G. Ordinary total rational martingale restriction after fixed prefix p shows G(u) CR, hence u∈R_k. Fixed finite coordinate flips/permutations are fair computable homeomorphisms, proving the remaining statement. QED.

**Corollary D113-2 (pointwise finite-edit conservation).** Suppose ANY map V has the property that, for each individual x in R_k, V(x) results from x by deleting finitely many coordinates, permuting finitely many remaining coordinates and flipping finitely many remaining bits. The finite recipe may depend noncomputably on x. Then V(R_k) subset R_k. This is pointwise closure under a FINITE composition of the preceding membership-preserving operations, not a claim that V is computable, fair, injective or globally k-fibre. In particular maps pointwise built this way cannot break R2 or CR (R1=CR). It does NOT cover INSERTING a bit/prefix into an R2 source, infinite reordering, or an arbitrary F2 output.

For K full the tag-shift F_T deletes precisely coordinate one, and so preserves R2. S108's tree switch is another instance of pointwise finite deletion plus a finite flip: remove its initial key and, on off-K sources, flip the one finite post-exit coordinate to the old key. This generalises restricted S112 D112-2/D112-3 without claiming F2(R2) subset R2 for arbitrary G.

## 4. Front B — full DP2/CP2 versus computable closed chart coverage

For an arbitrary G in F2, S106's actual double locus D is a union of effective closed D_r with partial computable inverse charts h_(r,i). S112's closed C subset D_r theorem preserves CR when lambda(C) has an ACTUAL computable name, even if C nowhere dense; the two sheet masses are obtained by subtracting upper-semicomputable measures from computable total. Neither actual two inverses nor fair global measure automatically computes lambda(D_r): S112 gives a globally fair EXACT-two G_T with D1=K of NONCOMPUTABLE mass. That K even has positive measure and can contain CR points. This forbids the naive C=D_r uniform application but does NOT refute DP2.

An attempted total rational ghost compiler based just on finite four-cell balance fails at the precise inference from finite candidates to TWO persistent source paths: the other candidates can die at unbounded noncomputable stages. S004's vanishing conditional sheet weight and S005's noncomputable hitting-price example prevent blindly rationalizing a positive sheet price. No constructive price compiler for arbitrary genuine CR double sources was obtained, and no CP2/DP2 theorem or counterexample is claimed.

## 5. Front C — unsaturated four-state/nonhomeomorphic architecture

The tag-collapse F_T is a useful 2-to-1 keyed candidate but its extra noninjectivity cannot coexist with fairness unless K is full. It has additive lookahead ONE, so independently S109's SATURATED finite-candidate rational compiler would conserve CR at any hypothetical fair actual double source; invoking that restricted theorem on a proper-tree F_T would be illegal because it is UNFAIR.

More general tagged sector gluing F(a u)=a Q_a(u) is fair and exactly-two iff BOTH Q_a individually are fair exactly-two, as follows by conditioning on the visible tag and counting fixed-key inverse sets. The tagged map has a CR double destroyer precisely when an appropriate Q_a already has a CR double destroyer, because finite prefix addition/deletion preserves ordinary CR. Hence this construction does not upgrade a known S083 SINGLETON destroyer to a paired one. In contrast, general NONDISJOINT sector transports might still permit coupled source mass transfer; they must satisfy BOTH S112 eq(6) on EVERY y and eq(7) on EVERY output cylinder. An actual CR double source, total rational winner and all-boundary-path verification remain missing.

S110/S111 already exhibit recurrent 48-type hybrid rows and actual ramified CR double paths yet conserve ALL CR. Repetition or ramification alone is not a winning capital strategy. S112 excludes all homeomorphic keyed deformations; D113-2 excludes pointwise finite erasures. Neither exclusion covers all unsaturated 4-state F2 maps. This is the remaining unclosed construction class.

## 6. Front D — EQ/SEP, SAME-source hierarchy and iteration

EQ requires for EACH CR nonMLR z a SOME legal global F2 destroyer and ordinary TOTAL RATIONAL computable output martingale. SEP requires ONE nonMLR z surviving EVERY legal F2 map and EVERY ordinary total rational martingale. The new tag maps either fail fairness on a positive cylinder or finitely delete source bits, hence cannot provide either central result. The protected-source bank still has no certified nonMLR member; no global coverage over all nonMLR sources was established. The original Y/M/H/X, DEF-0020/PA-0001 and frozen S101–S103 A-C remain unchanged.

R2 versus R_L1 needs a SAME z in R_L1\R2. A map outside L1 which conserves all CR, or S083's C\R_L1 source, is NOT such a witness. General F2(R2) subset R2 is not a consequence of the new restricted erasure theorem: H composed G can have four preimages. S106 gives only F2(R4) subset R2 without extra reasoning. No general hierarchy/iteration conclusion.

## 7. Evidence grades and next frontier

INTERNALLY PROVED: A113-1 count/density of this concrete noninjective transport, A113-2 proper-tree finite-cylinder unfairness iff/full-K classification, A113-3 fair deletion case, D113-1 arbitrary finite coordinate deletion for all k, D113-2 pointwise finite-erasure conservation, and the conditional tagged-sector reduction. These are original internal reconstructions, not assertions of literature novelty.

FAILED: arbitrary noninjective count implies fair price; legal proper-tree visible-tag pairing; computable canonical D_r masses; extension of finite-erasure R2 closure to finite INSERTION; reuse of a singleton destroyer by disjoint tags; universal martingale price compiler from finite candidates. GENERAL DP2, CP2, EQ R2=MLR, SEP R2\MLR, R2 versus R_L1 and unrestricted F2(R2) subset R2 remain UNRESOLVED.

Exact FINITE sanity script exhausts 65,812 clopen-tree cases at depths 1–4 with 8,471,380 assertions, plus 676 rooted possibly nonpruned height-three trees with 22,308 assertions: 8,493,688 assertions PASS. It does NOT prove infinity cases, fairness with noncomputable K, CR/R2 or central targets. Same-agent independent-in-method hostile proof audit only, not outside/formal certification.

Frozen source access levels (SRC-0067 ABSTRACT_INSPECTED, SRC-0068 PROOF_INSPECTED, old E-ISO and only scoped S112 Lemma15/16 proof use), Y/M/H/X, PA-0001/DEF-0020, A-C. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. No Gate4, Phase5, Lean, Palomar, manuscript, outreach or publication.
