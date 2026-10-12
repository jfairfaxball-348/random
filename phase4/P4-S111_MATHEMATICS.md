# P4-S111 — A genuinely ramified hybrid exact-two quotient (same-source coupling)

2026-10-12. ONE new owner-invoked CAND-01 Phase4 mathematics session. LIVE entry main `909d72b806a14421ddc2df54dfa94cd359f244d1` (S110 sole atomic commit, parent `6dc2d1381792b45d69a437ffb6dad9f5aac86369`, tree `e439690c0ca0ffe0cdc72f1c61c08fb12be2e605`); S110 PR #8 CLOSED/MERGED, merge SHA equals entry. Initial open PRs zero and no competing S111 branches. Internal proof dossier, not external review, formal certification or novelty finding.

**Main new result.** There exist total computable, fair, everywhere EXACTLY-TWO-to-one maps F with original-coordinate additive use TWO, a positive-measure set of actual computably random *ramified* double sources, and true 48-type four-row hybrid transitions at EVERY EVEN output prefix on those sources. Ramification can have measure arbitrarily close to 1. Yet EVERY such F in the constructed family preserves ordinary computable randomness, so the original DP2/CP2 and EQ/SEP conjectures are not decided.

## 1. Independent correction audit of S109–S110

S110 G_t has source x=a u and, at each 2-bit boundary, applies a swap or identity to the following tail pair based only on the *already emitted* output prefix and the initial source key a. For fixed a, inverse reconstruction proceeds block by block; each output has precisely one inverse per a, hence exactly two ACTUAL infinite inverses. The four length-(m+2) prefix candidates at depth m are not four actual inverses. At active even levels: two key-zero rows are permutive in the next input bit and two key-one rows are C0/C1. The fair conditional block permutation has exact dyadic prices and needs x_(m+2) to compute output bit m for active key-zero rows. Its ordinary rational source martingale samples output capital at even block boundaries, uses the *average of its two grandchildren* at odd input lengths and exploits the 4-to-4 bijection. Unbounded output capital implies unbounded even capital (one step multiplies by at most 2). This rechecks rather than assumes S110 A–C.

S110's tagged gluing is globally exact-two/fair, but hybrid and S108 ramification are deliberately on DISJOINT tag cones; it proves no same-source hybrid/ramification statement. S108 first-exit formula and ramification were reconstructed: over [T] source preimages are (0,y),(1,y), over its complement they are the two same-key first-exit sources. S109's additive-one normal form H–S–K is a finite transition classification with exactly two rows: 4 balanced transition configurations and 2 folding configurations. Saturated fibre conservation uses EXACTLY 2^c ACTUAL inverses; a four-prefix unsaturated fibre does NOT qualify. No fatal correction was found under the original stated restrictions. These audits do not constitute independent outside review.

## 2. General exit-label compatible twist — a new exact-fibre and fairness theorem

Let T be a decidable prefix-closed binary tree containing the empty word, and let K=[T]. For v outside K, let rho(v) be its shortest prefix outside T and let c(v) be the bit immediately AFTER rho(v). Define the S108 tree-switch G_T on x=a u by:
- if u in K, G_T(a u)=u;
- if u=rho b t at its first exit, G_T(a rho b t)=rho a t.

Let P_0,P_1 be total computable **measure-preserving homeomorphisms** of Cantor space satisfying (i) P_a(K)=K and (ii) c(P_a(v))=c(v) for ALL v outside K. Define
    F(a u)=P_a(G_T(a u)).

**Twist theorem (INTERNALLY PROVED).** F is total computable and fair, and has exactly two ACTUAL preimages of EVERY y. Moreover Ram(F)={a u : u is in boundary(K)}. If each P_a preserves CR, then F preserves CR at EVERY source, even a ramified actual double source.

Proof — full inverses, not finite counts. If y in K, invariance of K gives exactly the two preimages a P_a^{-1}(y) for a=0,1. For y outside K write v_a=P_a^{-1}(y). Property (ii), applying the equality to v_a, gives c(v_a)=c(y). S108 inversion of G_T at fixed key a says there are exactly two preimages of v_a on the a-cone if a=c(v_a), and NONE otherwise. Exactly one a=c(y) qualifies, giving TWO source points, regardless of their placement in the finite prefix chart. This exhausts all cases.

Proof — genuine fairness. Conditional on the initial key a, the law of V=G_T(a,U) for a uniform tail U has density h_a(v)=1 on K, density 2 on {v outside K : c(v)=a}, and 0 elsewhere. This follows by the explicit first-exit cylinder bijection: rho 0 t and rho 1 t both map to rho a t, whereas on K there is one tail preimage. It holds on the countable disjoint first-exit partition plus the closed residual K, with no effective stopping-mass premise. P_a preserves measure, K, and c, hence h_a∘P_a^{-1}=h_a almost everywhere; its pushforward fixes this *conditional* law. Averaging h_0 and h_1 with key weights 1/2 gives density identically 1. Thus lambda(F^{-1}([tau]))=2^{-|tau|} for EVERY output cylinder, not merely for selected depths.

Proof — ramification and CR. On an initial-key clopen cone, F is the postcomposition of G_T with a homeomorphism, so local injectivity is exactly that of G_T. The two key cones are disjoint clopen sets. S108 proves the nonlocally-injective locus is the two copies of boundary(K), including the boundary's actual partners, and no other source. If x is CR, S108 gives G_T(x) CR, and the specified CR-preserving P_a gives F(x) CR. This proof does not infer CR conservation merely from a general computable measure-preserving homeomorphism: that inference is unsafe without a martingale transfer. QED.

The exit-label condition (ii) is essential in this argument. Merely imposing P_a(K)=K can give 0 or 4 inverse points outside K when c(P_0^{-1}y)=c(P_1^{-1}y) fails. This is a quantified obstruction to naive partner twisting, not a universal impossibility theorem.

## 3. Explicit fat invariant T_L and safe block involution P

Represent the tail as 2-bit blocks. Fix integer L>=1. For EVERY string sigma consisting of q complete blocks (q>=0), forbid the prefix
   w_sigma = sigma (00)^(2q+L) 11.
Let T_L be all finite binary words with NO w_sigma as a prefix and K_L=[T_L]. Membership is decidable at each finite depth, and every *first* bad prefix is at an even depth and ends with the equal-bit block 11. Given any cylinder [s], extend s to a complete block prefix sigma then append (00)^(2q+L)11: the complement U_L is dense open; K_L is closed nowhere dense.

For each q, the union of all 4^q forbidden cylinders of the indicated length has measure at most
   4^q · 4^-(3q+L+1) = 4^-(2q+L+1).
Summing the geometric bound yields lambda(U_L)<= (16/15)·4^-(L+1); therefore
   lambda(K_L)>=1-(16/15)·4^-(L+1).
For L=2 the bound is >=59/60; it approaches 1 as L grows. Prefix membership of T_L is invariant under swapping either order of bits within any number of COMPLETE 2-bit blocks: the arbitrary sigma ranges over all block strings and each specified later block is 00 or 11, unchanged by swapping.

Define P=P_0 blockwise on v. Before the first forbidden block has completed, SWAP each completed block; on the first forbidden block and thereafter use IDENTITY. Set P_1=id. The forbidden block is 11 and is invariant under swapping, so the procedure is a total computable, self-inverse, measure-preserving two-bit block tree automorphism. Swapping cannot change the first-bad index, since T_L membership at every even depth is swap-invariant; after the exit all bits, and especially the bit c(v) after the first bad block, are unchanged. Hence P(K_L)=K_L and c(P(v))=c(v) off K_L. At every completed block prefix before exit the induced four-block permutation is exactly a permutation (00↦00, 01↦10, 10↦01, 11↦11 when still admissible; at the first forbidden 11 it is still 11); after exit it is the identity. Note the switch on 11 does NOT lose bijectivity because that block is fixed by swapping.

Thus F_L(a u)=P_a(G_(T_L)(a u)) satisfies the general twist theorem: globally total computable, fair, exact TWO points over every infinite output, and Ram(F_L)={0,1}×K_L with measure at least 1-(16/15)4^-(L+1). Each y∈K_L has two actual inverse sources 0P(y) and 1y, both genuinely ramified. Crucially, there are NO disjoint tag cones.

## 4. Infinitely many actual 48-type hybrids at the SAME ramified sources

Fix any EVEN output prefix tau∈T_L of length m=2j, including any prefix along any y∈K_L. The four source length-(m+2) cylinders over output [tau] are indexed by key a∈{0,1} and pending tail bit t∈{0,1}; the preceding m tail bits are uniquely P_a^{-1}(tau) (P is its own inverse). The new source bit is b.

For key 1, no swap occurs: at output position m, G_T emits the pending bit t (even if the next completed forbidden block is approaching). The two key-one rows are therefore C0 and C1.

For key 0, the next output position m is the SECOND bit b of the new source block (t,b), because the block is swapped while admissible. If it is the FIRST forbidden block, the block is 11 (equal bits), so P leaves it unchanged but its first output bit is still 1=b. Tree-switch G_T retains every bit through the first bad block; it only substitutes the key AFTER that block. Thus the next output bit on BOTH key-zero rows is b, i.e. the two rows are P,P (permutive). The exact local transition multiset is
   {P,P,C0,C1},
one of the 48 hybrid 4-row balanced cases, for EVERY even tau in T_L, including all even prefixes of every y∈K_L. Not just a finite-state visual resemblance: the output actually has the two globally distinct inverses stated in Section 3. At odd output levels no hybrid conclusion is needed.

Choose y in K_L such that both 0P(y) and 1y are CR. Such y exist in measure at least lambda(K_L)>0, since total computable two-bit block automorphisms P, the initial-bit operation, and their inverses preserve CR (see Section 5), and CR has fair-coin measure one. Both inverse sources lie in Ram(F_L), and F_L sends them to the SAME y. Every even output prefix of y is 48-hybrid. This explicitly **CLOSES the S110 same-source hybrid/ramification structural gap**. It does NOT construct a CR double source with nonCR image.

## 5. Ordinary rational martingale conservation, no conditional-price oracle

To verify CR preservation of P, take an arbitrary total nonnegative rational output martingale d; replace it by strictly positive p=(d+1)/2 if needed. At even input block boundaries s define E(s)=p(P(s)); at odd prefixes s define E(s)=(E(s0)+E(s1))/2. The mapping from the four 2-bit input extensions of any even s to the four output extensions of P(s) is a bijection, including at the first forbidden 11 block; the four values average to p(P(s)) by two steps of the ordinary martingale equation. Therefore E is a total nonnegative rational computable one-bit source martingale at even and odd lengths. At even lengths E(v|2j)=p(P(v)|2j). A nonnegative output martingale cannot have unbounded odd capital and bounded even capital, because its value at an odd child is at most twice its even parent. Thus any output martingale succeeding on P(v) produces an E succeeding on v. P is an involution, so both forward and inverse CR preservation follow.

The finite initial key is handled by clopen conditionalisation: if a tail betting strategy wins, hard-code the observed key a and put constant capital on the other initial-key cylinder. S108 directly proved that G_T maps EVERY CR source to CR (its output is either a tail deletion or a finite prefix modification of a common tail). Combining that theorem with the explicit rational P compiler proves F_L(CR)⊆CR, including every fat ramification source, without any source-partner stopping oracle or noncomputable stabilization bound.

Therefore the restricted robustness set for the family {F_L:L>=1}, even augmented by S110 G_t and the identity, remains exactly CR: all are CR-conserving, and the identity is present. This equality does not imply R2=MLR.

## 6. Four wider fronts: destruction, CP2, hierarchy and free discovery

**Front A — paired CR destruction (NOT SOLVED).** F_L has actual ramified partners and recurrent hybrids simultaneously, but the preceding ordinary rational compiler blocks EVERY attempted output winner on a CR source. Trying to replace P_a by an S083 destroyer reintroduces the singleton-fibre problem: its first-exit label may be changed, violating the twist lemma, and straightforward composition multiplies fibre sizes. No fair F2 paired CR destroyer has been constructed, and no universal impossibility shown.

**Front B — general DP2/CP2 conservation (NOT SOLVED).** The twist theorem proves conservation across a non-clopen partner-involution discontinuity and unsaturated four-prefix candidates—strictly beyond S109's saturated theorem and a globally computably clopen sheet split. However its conclusion depends on CR-preserving compatible P_a. General F2 may have ghost prefixes whose effective conditional mass and exit labels are not computable; our paired product density calculation is special to the explicit first-exit partition. An attempted universal sheet-weight compiler has no finite rational source-price guarantee (S004/S005). No DP2 or CP2 theorem is claimed.

**Front C — hybrid/ramification (SOLVED FOR CONSTRUCTION).** Sections 3–5 give a full infinity-level yes answer to the structural question in S111: 48-type recurrent even-level hybrids AND genuinely ramified CR two-point fibres on the SAME output path. The compatible-twist condition also identifies why easy key-dependent postcomposition usually destroys the exact-two bound.

**Front D — EQ/SEP/hierarchy (NOT SOLVED).** F_L∈F2\L1 for the same explicit key-zero permutive even rows; nevertheless F_L preserves ALL CR sources, so it cannot separate R2 from R_L1. The S109 exact inclusion R2⊆R_L1⊊C and established S083 single-source witness remain intact. A full EQ proof would require an all-source destroyer for every CR\MLR sequence. A SEP proof requires ONE nonMLR source safe against EVERY F2 map and EVERY ordinary total rational output martingale; building a conserving subclass cannot discharge that quantifier. F2(R2)⊆R2 remains unsettled because compositions can raise fibre bounds. A conditional result is safe: finite compositions of these concrete conserving maps preserve CR, but they need not remain in F2 and do not imply the target inclusion.

**Free structural discovery.** Conservation, actual ramification and infinite 48-type hybridity can coexist on a set of source measure arbitrarily near ONE, not merely in separate clopen cones. Thus the proposed sufficient 'hybrid+ramified' geometry for CR destruction is REFUTED by an explicit continuous globally exact-two map. This is a meaningful restriction on future destroyer designs, not a solution of the central randomness problem.

## 7. Proof grades and disposition

INTERNALLY PROVED: compatibility-twist exact fibres/fairness/ramification/conservation; computable fat block-invariant K_L with >=59/60 ramification for L=2 and measure arbitrarily near one; true 48-type transitions at every even prefix of every y∈K_L; actual CR ramified double sources; an explicit ordinary total rational 2-bit martingale compiler; robust restricted conserving class. NO central DP2, CP2, EQ, SEP, R2 vs R_L1, or F2(R2) theorem. No external peer review, formalization, novelty audit, Gate4, Phase5 or publication. Preserve Y/M/H/X, PA-0001/DEF-0020, S101–S103 A–C, original source-access grades and all earlier records. The separate finite checker passed 84,903 assertions, sanity only, not infinity proofs.
