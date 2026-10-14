# P4-S135 — Perfect branching, two-real-inverse boundary, and a rational source no-go

14 October 2026. One INTERNAL Phase4/CAND-01 mathematics session, not formal/external validation. Live ENTRY main be7655c2d7120a7649a65cdc6dfe44cb8ce92099; S134 authored atomic sole-parent commit (parent bb901e53261a8d4809b85ebaef506fcd85f9d5c2, tree 3235d70bc6e326eb9fd25593648e2e0525f1d287), PR #33 merged as non-force fast-forward, 18 changes. No S135 competing session on entry. Frozen Y/M/H/X, DEF-0020, PA-0001, source grades and S101–S103 A–C retained.

Notation: Cantor space X=2^omega, fair product lambda. F_k = total computable globally fair maps with at most k ACTUAL infinite preimages above EVERY output; R_k quantifies over every such map and all ordinary total nonnegative rational computable output martingales. CR is computable randomness. Additive-two observer has first m output bits computable from first m+2 source bits. There are four aligned input cells per output m-cylinder; this finite count is NOT an actual fibre count.

## A. Complete computably branching F3 oscillator — proved internally

Define effectively closed computably perfect
 T={y∈X : y_(3j+1)=y_(3j+2)=0 for all j≥0}.
The positions 3j are FREE; the next two are forced zero. The decidable tree T_m has 2^{ceil(m/3)} length-m strings, and lambda[T_(3j)]=4^{-j}. Hence T is uncountable, perfect, nowhere dense, effectively NULL with computable rate. All y∈T are non-Schnorr (and nonCR), but some are noncomputable.

Construct ordered rows R(tau) of exactly four distinct length-(|tau|+2) input words for EVERY finite output tau. Root R(empty)=[(A,00),(A,01),(A,10),(B,11)]. A node is ACTIVE iff tau follows T's forced digits, otherwise SAFE. An ACTIVE row at m≡0 or 1 (mod3) has (A,a0),(A,a1),(A,a2),(B,b0); at m≡2 it has (A,a0),(A,a1),(B,b0),(B,b1). Its two child rows are:

FREE m≡0: each input parent (tag,s) sends (tag,s0) to output tau0, (tag,s1) to tau1; BOTH rows stay ACTIVE A3/B1.

FORCED m≡1:
 R(tau0)=[(A,a0 0),(A,a0 1),(B,b0 0),(B,b0 1)] (ACTIVE A2/B2);
 R(tau1)=[(P,a1 0),(P,a1 1),(S,a2 0),(S,a2 1)] (SAFE P2/S2).

FORCED m≡2:
 R(tau0)=[(A,a0 0),(A,a0 1),(A,a1 0),(B,b0 0)] (ACTIVE A3/B1);
 R(tau1)=[(P,a1 1),(P,b0 1),(S,b1 0),(S,b1 1)] (SAFE P2/S2).

At EVERY SAFE row [(P,p),(P,q),(S,r),(S,s)], set
 R(tau0)=[(P,p0),(P,p1),(S,r0),(S,s0)];
 R(tau1)=[(P,q0),(P,q1),(S,r1),(S,s1)].
At entry the two P cells need not be siblings (S134's correction); after one SAFE step they are siblings. Every case assigns EACH of eight source children exactly ONCE across its two four-cell output rows.

Induction from root gives a partition of ALL length-(m+2) source words by the output length-m rows, so every input determines one coherent computable output and G is total with additive use two. Each output tau has four aligned source cylinders, exactly measure 4·2^{-(m+2)}=2^{-m}. This is fairness on EVERY cylinder, including EVERY sibling, not only on T.

TRUE infinite fibres: if y∉T it enters SAFE at its first forbidden 1. Its P pair contributes ONE infinite path (the selected parent alone survives at every stage, while the pair of children continues) and the two S singleton branches contribute ONE each: degree exactly THREE. If y∈T, the tagged A and B candidate sets are nonempty at every level, yielding at least one inverse each by compactness. At cofinal ACTIVE stages m≡1 only the FIRST A parent can extend into the active child; at cofinal m≡2 only the FIRST B parent can extend. Two distinct A (or B) full inverse paths would eventually differ at one of these arbitrarily late stages, contradicting that unique surviving parent. Hence exactly ONE A and ONE B full inverse, degree exactly TWO. Both initial sectors are disjoint. The 3:1→2:2→3:1 boundary cycle repeats on EVERY y∈T. The case of uncountably many recurrent exceptional outputs was achieved with ALL siblings complete.

Choose any noncomputable alpha and put alpha(j) at output coordinate 3j with the next two digits zero. The resulting y∈T and both preimages are noncomputable (computable source would produce computable y). But this gives NO random source.

## A'. One TOTAL rational SOURCE martingale defeats every inverse of T — proved internally

An OUTPUT martingale d doubles capital on 0 at positions m≡1 or 2 mod3, loses on 1, and holds at FREE positions. It is ordinary rational, total, nonnegative, and succeeds on EVERY y∈T. Crucially, an output winner alone does NOT refute source CR. We give an independent SAME-SOURCE compiler.

For each integer j≥1 let V_j be the clopen union of length-6j output cylinders compatible with T, and U_j=G^-1(V_j). Then U_j is computable clopen SOURCE data decided from 6j+2 input bits. Global fairness implies lambda(U_j)=lambda(V_j)=2^{-4j}. For finite source s put q_j(s)=lambda(U_j∩[s])/lambda[s]; it is TOTAL EXACT computable rational and satisfies q_j(s0)+q_j(s1)=2q_j(s). For every source word a of length j:
       0≤q_j(a)≤2^j lambda(U_j)=2^{-3j}.
Define M_j(s)=1 when |s|≤j; for |s|>j set a=s|j and M_j(s)=q_j(s)/q_j(a) if q_j(a)>0, otherwise HOLD at 1. This is a genuine unit nonnegative total rational SOURCE martingale: on each j-cone the conditional quotient averages correctly, including the activation edge; a zero-price cone is held flat and contains no point of U_j.

If G(x)∈T then x∈U_j for ALL j, so q_j(x|j)>0. Since U_j is decided by input precision 6j+2, q_j(x|(6j+2))=1. Thus M_j(x|(6j+2))≥2^{3j}. Now combine by ONE ordinary finite-expression rational martingale
       W(s)= Σ_(1≤j≤|s|) 2^{-j} M_j(s) + 2^{-|s|}.
The tail is EXACTLY Σ_(j>|s|)2^{-j}=2^{-|s|}, because these components have not started and equal 1 at length |s|. So W(empty)=1 and W(s0)+W(s1)=2W(s) EXACTLY, not by an infinite computable-real approximation. For every such x, at n≥6j+2 we have W(x|n)≥2^{-j}2^{3j}=2^{2j}. Hence W wins on ALL sources over T, including noncomputable ones. No x∈CR, hence no x∈R2, can map into T.

General mechanism: under any total computable globally fair observer, preimages of a computable effectively closed NULL output class are effectively closed NULL source classes. Conditional-clopen martingale construction with a computable search for small probabilities on each finite set of depth-j source cylinders gives a rational source winner; our explicit U_j avoids a search. Therefore making the active T tree sparser while retaining an effectively closed null class CANNOT rescue this architecture.

## B. Arbitrary-outer F2 factorization: necessary degree identity, NOT resolved

There is NO clopen C with lambda(C∩G^-1[tau])=lambda[tau]/2 for ALL tau. Fix y∈T with distinct true x_A,x_B. For any clopen C, sufficiently late aligned cells above y lie inside small disjoint neighborhoods of these points where C is constant. The number of compatible cells in C is then 0,4,q_A(m),or q_B(m). Along T, q_A oscillates 3,3,2 and q_B oscillates 1,1,2; none gives the required 2 at EVERY late m. Thus no globally fair F can give G=shift∘F through a continuous first-bit half-tag. This is a LIMITED result; it does not rule out arbitrary H.

For ANY possible G=H∘F with H,F∈F2, both factors are onto (compact images and fair full-support measure). At EVERY y∉T, genuine degree 3 implies H has EXACTLY two true preimages and the corresponding F-fibre sizes are 1 and 2. At EVERY y∈T, genuine degree 2 implies EITHER H has one true preimage with F-degree 2 OR H has two with F-degrees (1,1). This is a necessary arbitrary-H invariant; a drop can occur in the outer fibre or in the inner double selector on T. Neither type has been universally excluded or realized. No assertion of genuine nonfactorability.

## C. Headline hierarchy: explicit opposing tests, no positive separation

The tempting claim “a noncomputable inverse over a bad output witnesses R2\R3” FAILS at the first membership test: W wins on every such inverse. In fact this G preserves ALL CR: CR sources cannot map into T by W, and outside T each source is on a SAFE P or S branch after a finite entry. The remaining source/output tails differ only by finite-prefix changes (at most one delayed bit for P); finite-prefix invariance of CR yields CR image. So G creates no R2\R3 witness despite the perfect degree-two boundary.

More attempted routes, all unresolved: sparse computable forced stages still define an effectively closed NULL set and admit source compilers; an arbitrary F2∘F2 factorization cannot be denied using the shift half-tag obstruction; composition of two F2 observers may have FOUR actual inverse streams and R2 of x guarantees only CR of F(x), not R2 of F(x). The old S129 one-surplus theorem has r=2^c−1 and CANNOT apply to c2 degree two. S131 two-cone 3→2→3 transitions permit our rows; S131 globally-onto sheets fail on a forbidden sibling. S132/S133 restricted factorization is not arbitrary-H.

UNRESOLVED: R2=R3, R2=MLR, R3=MLR, R2/R4, F2(R2)⊆R2, one x∈R2\R3, one x∈R2\MLR, one x∈R_fin\MLR. Neither CR nor noncomputability substitutes for R2's ALL-observer universal quantifier. ∀k∃x_k is NOT ∃x∀k.

## D. Genuine finite but unbounded fibres, still no destroyer

Using S130/S131's computably closed fat nowhere-dense C_t and decidable disjoint removed-prefix patches [rho_n] whose lengths grow with stage, set Q(x)=x on C_t and Q(rho_n u)=rho_n (T_(n+1)∘G)(u) on each patch. Here T_(n+1) is S127's complete-prefix-code fair finite-tail-conserving map of exactly n+1 inverse streams. Piecewise conditional fairness and identity on C_t imply GLOBAL fairness; prefix growth proves total effective continuity at C_t; targets in C_t have their own sole inverse, targets in patch n have ≤3(n+1) actual inverses there, no cross-patch inverses. Nonhomeomorphic, pointwise finite, not uniformly bounded; however G preserves CR, T_(n+1) and finite-prefix operations preserve CR and C_t is fixed. Therefore Q preserves ALL CR, hence cannot destroy any x∈R_fin. Moving a boundary via a computable fair homeomorphism (S133) would remain safe; a genuinely destructive interaction is missing.

## E. Hostile replay, correction sheet and status

S134's isolated zero-spine inverses were exactly {0^omega,110^omega}, BOTH computable; its SAFE initial P pair need not be siblings; its no-half-tag result ONLY applies to shift outer. S129 one-surplus has degree THREE at additive two, not our degree TWO. S131 two-cone counts allow transitions (3,1)↔(2,2). S132 K's selector uses SECOND output bit, S133 relabel uses FIRST; neither extends automatically. In our construction the NEW null perfect set does not produce CR preimages: the explicit W stops that inference at the exact first false step.

Exact Python Fraction finite sanity (not proof) at m=0..12: 8191 target cylinders, 32764 source-cell occurrences, 16384 final input words, 91 ACTIVE rows and 8100 SAFE; independent-in-method but SAME-AGENT checking. Infinite claims proved by row induction, compactness/pruning and rational-capital argument, NOT finite enumeration. Zero hosted workflows/runs/checks/statuses observed: ABSENT_NOT_PASS, protection inaccessible UNKNOWN. No external referee, novelty grade increase, formal validation, Gate4, or publication. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN and Phase5 CLOSED. Open central targets preserved.

