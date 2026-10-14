# P4-S131 — Nonstationary three-sheet realization, homeomorphic-sheet firewall, and the two-cone transition obstruction

14 October 2026. One owner-invoked Phase4/CAND-01 mathematics session. Incoming **live** main `ea116e7671b95ce7f0e40238cc5e59a0eceb4d10`, S130 authored commit (sole parent `85498fa557b9223e737c3d92a64432b85c8b50f3`, tree `a1777d67d21afcdd634e2f2724d676ccbe783735`), PR #29 closed/merged by non-force fast-forward as the authored commit. No intervening main commits/open PRs/competing S131 branch or records at entry. Internal mathematical investigation only. See ENTRY_EVIDENCE and VALIDATION for check/status/protection scope.

Definitions remain those of S129–S130. X=2^omega, lambda fair coin law, F_k total computable globally fair maps with at most k **ACTUAL full infinite** inverses per output, R_k universal CR preservation, R_fin intersection over all finite k. CR uses ordinary total nonnegative rational martingales; MLR subset all R_k. Additive use c means m output bits fixed by m+c input bits. Finite aligned compatible-cell counts and actual inverse counts are never conflated.

## A131 — the two-actual-inverse additive-two occupancy graph (rigorous scoped obstruction)

Let G be any total fair additive-two map. At a fixed y with exactly TWO actual inverse paths, choose disjoint equal-length cylinders B0,B1 isolating them, and take levels m sufficiently high that all four compatible length-(m+2) source cells lie in B0 union B1. This eventual coverage follows from compactness of the inverse sets, without an effective onset. Let a_m be the number in B0, so 1<=a_m<=3 and B1 has 4-a_m. Of the 2a_m source children in B0, exactly a_(m+1) continue toward y; the sibling receives 2a_m-a_(m+1). Both y-child and sibling have exactly FOUR total cells. Existence of a true path in each B-cone gives 1<=a_(m+1)<=3, and binary branching gives
 max(1,2a_m-4) <= a_(m+1) <= min(3,2a_m).
Consequently the ONLY permitted directed transitions are 1->{1,2}, 2->{1,2,3}, 3->{2,3}. A direct 1<->3 majority reversal is impossible; every reversal crosses a 2:2 state. The row obstruction applies at every sufficiently late level on the target, with all sibling populations 4, NOT a globally specified F2 completion.

If a_m=1 eventually for the cone containing x, the S117 gated source compiler defeats any ordinary rational output winner, making x nonCR. If a_m=2 eventually for that cone, the S129 B exact two-cell normalized legal F2 completion (with ALL balanced sibling and permanent chronological fallback) defeats any nonCR image of an R2 x. Thus an R2-to-nonCR counterexample at a degree-two y cannot put x in a cone with eventually-one or eventually-two occupancy. It must exhibit eventually-three occupancy or genuine non-stabilization of that cone (or evade additive-two altogether). The 3:1/2:2 oscillations, arbitrarily late switches, lower-occupancy recurrences and rational source-capital compilation remain OPEN; no assertion that visiting a one-cell level infinitely often suffices.

Hostile counterexample to overselling: the allowed row 3->2 forces a sibling with 6-2=4 cells from the old triple cone, and 2->3 likewise permits mixed rows. A direct permanent 2:2 fallback will generally modify the target; any new F2 reduction needs a proved balanced target run. At degree ONE, all four aligned cells may lie in one inverse cone, and the preceding two-cone graph is inapplicable.

## B131 — actual complete fair minimal-c3 three-sheet realization violating stationarity

Define eight root source tags of length 3, grouped into three disjoint clopen B_A,B_B,B_C, and give each tag an output prefix p:
| sheet | source tag s -> output leaf p |
|---|---|
| A | 000->0 ; 001->10 ; 010->11 |
| B | 011->1 ; 100->00 ; 101->01 |
| C | 110->0 ; 111->1 |

Set G0(su)=p_s u on ALL inputs. Within each sheet the p_s form a **complete prefix-free output code**; therefore every output y has precisely ONE full inverse in EACH sheet, namely s times the suffix after its unique leaf p_s. Thus G0 has EXACT THREE ACTUAL inverses at EVERY y, never four. All root inputs and all siblings are specified, with no uncomputable spine.

Global fair law: on target [0], the contributions from sheets A,B,C to the target density are (1/4,1/2,1/4); on target [1] they are (1/2,1/4,1/4). These are obtained from source sector mass 1/8 divided by output leaf cylinder mass 2^{-|p_s|}. Their sums are EXACTLY 1 on both target halves and on every finer Borel cylinder, so G0 pushes lambda to lambda. For first m output bits, max(3,m+2) input bits suffice.

Let K swap just the FIRST TWO output bits and fix the entire remaining infinite tail; K is an everywhere computable fair involutive homeomorphism. Define G=K circ G0. Then G remains total, globally fair, EXACT-three-fibred over EVERY output, and has additive use at most c=3. Its **minimal** additive c is 3: G's first output bit requires the fourth source bit in the tag 000 cone, so three source bits cannot determine it. At levels m+3 the sheet-count vector is (3,3,2) for m=0,1; for m>=2 it equals (2,4,2) or (4,2,2), according to the SECOND output bit. These vectors have five excess finite cells over the three actual paths at every level. This explicitly evades B130's all-output **constant** 3,3,2 hypothesis, without refuting its dyadic theorem. No output-dependent noncomputable hardwiring occurs; all branches are total.

On any source su the output K(p_s u) differs from the tail u only by a finite prefix and the finite two-coordinate interchange. By finite-prefix CR invariance, G preserves CR for EVERY source, so this real triple observer does NOT furnish R2\R3 or a nonCR output of any CR source. The occupancy change here is finite, not an indefinitely cycling surplus, and a five-surplus nonstationary destroyer is NOT constructed.

## B131' — saturated full-sheet firewall beyond stationary dyadic counting

**Scoped theorem.** Let G be fair, total computable, additive-c, and B a nonempty union of a source length-c cylinders. Suppose G restricted to B is one-to-one **ONTO ALL X** (one actual inverse inside B for EACH output). Then EVERY CR input in B has a CR image, WITHOUT assuming the B aligned-cell population is constant across output prefixes.

Proof: compactness makes G|B a homeomorphism onto X, and its inverse computable by effective compact search. For every output tau of length m the number q_B(tau) of length-(m+c) source cells in B compatible with tau is computable, is >=1 by onto and <=N=2^c. Let mu be the normalized pushforward of lambda restricted to B. With lambda(B)=a/N,
 mu[tau] = q_B(tau)/(a*2^m).
Thus mu is a computable positive rational cylinder measure with 1/a <= mu[tau]/lambda[tau] <= N/a. If an ordinary rational lambda-martingale d wins on y, then
 D_mu(tau) = a*d(tau)/q_B(tau)
is a TOTAL computable nonnegative rational mu-martingale and wins on y, since D_mu>=a*d/N. The effective measure isomorphism (B,lambda_B) -> (X,mu) transports CR in both directions, so a CR x in B cannot map to such y. CR of x under the computable conditional law lambda_B follows by gating a source martingale to the finitely many B cylinders. This uses the standard effective-isomorphism preservation principle (also stated in the existing programme background); it is NOT the false assertion that arbitrary fair noninvertible morphisms preserve CR.

In particular a triple-fibred fair map whose three inverse paths are globally split into three clopen ONTO singleton sheets preserves CR on all its inputs, even with changing occupancy and without B130's constant-price condition. The B131 example is a direct elementary finite-tail witness. This firewall does NOT cover fibres whose isolating cone fails to map onto an output neighbourhood, whose restriction retains two actual paths, or where the source has no computably certified clopen singleton sheet. It does not prove an F3 factorization, R2=R3, or general safe images.

S130's stronger stationary count restriction remains VALID and distinct: if q_B(tau)=a everywhere, the conditional output measure is lambda and the clopen images of a root cells each need target measure 1/a, forcing a power of two. At c3, an all-output stationary three-sheet partition must be (4,2,2) up to permutation. The present varying example has (3,3,2) at root but is fully safe.

## C131 — composition, factorization and same-source cross-level audit

The example's cap3 and all-output exact-three are proved without implying it is nonfactorable. S128 selector necessity still stands: a hypothetical G=H circ F with F,H in F2 and everywhere degree3 forces H degree2 and exactly one F-double over each H-fibre. S130 preserves CR of H(F(x)) when H is saturated additive-one and x in R2, irrespective of F use. We have neither ruled out factorization of B131 nor built an F3 with proved nonfactorability. Likewise F2 circ F2 can have degree FOUR, and x in R2 only guarantees F(x) CR, not F(x) in R2. F2(R2) subset R2 and general R2 vs R4 remain OPEN. The direct B131 example cannot refute anything in the hierarchy because every CR image is CR.

## D131 — arbitrarily fat but harmless pointwise-finite exceptional loci

S130's closed C can be made as close to measure ONE as desired without making it destructive. For each integer t>=1 use successive block lengths d_n=n+t. Let C_t be sequences with NO all-zero d_n block; let G_t be identity on C_t and, on the cylinder of the FIRST zero block at stage n, delete the first n tail bits after that cylinder, keeping its prefix unchanged. The same total prefix algorithm, piecewise fairness, precise finite fibres (2^n on that removed patch and 1 on C_t), and L_(G_t)=C_t proofs from D130 hold verbatim. Since
 lambda(C_t)=product_n(1-2^{-(n+t)}) >=1-sum_n 2^{-(n+t)} =1-2^{-t},
we can choose t for any positive epsilon to obtain lambda(L_(G_t))>=1-epsilon. Each C_t is effectively closed nowhere dense, has positive measure, and meets MLR/R_fin, while G_t FIXES C_t and preserves every CR input by finite-tail equivalence off C_t. There is still NO R_fin bad output. Large, even near-full-measure, L_G does not imply failure of R_fin.

## E131 — central target status and first failed proof lines

R2=R3, a same-source x in R2\R3, R3=MLR, R2=MLR, an x in R2\MLR or R_fin\MLR, genuine c3 three-CR-over-bad-output, general cap3 c2 preservation, F2(R2) iteration, nonfactorable F3, and a destructive pointwise-finite G on ONE R_fin source all remain UNRESOLVED. No 'for all k exists x_k' -> 'exists x for all k' move.

Failed line 1: '3,3,2 root cells cannot extend to a fair exact-three c3 map' is FALSE: B131 gives a full nonstationary legal map. B130 only disallows constant counts at every prefix.
Failed line 2: 'Changing tagged sheet occupancy yields a bad output' is FALSE: globally effective onto homeomorphic sheets give a CR firewall.
Failed line 3: 'Every degree-two bad-image fibre can be normalized to balanced 2:2' is NOT PROVED: valid 3:1 states and oscillatory rows survive.
Failed line 4: 'Full sheet effective isomorphism settles arbitrary B with one inverse only at the target' is FALSE: the onto hypothesis is essential.
Failed line 5: 'A near-full-measure local-unbounded locus creates a bad image' is FALSE in the exhibited class, G_t|C_t=id.

Internal five-session S126–S130 correction audit: S126 exact recovery of BOTH distinct inverses is not selecting one; S127 code Kraft and actual vs aligned counts; S128 all-output SOLO/PAIR siblings; S129 one-surplus new-tag source betting only at r=2^c-1 and the exact delayed rational mixture; S129 B2 normalization ONLY after stable two-cell and proper fallback; S130 sheet theorem only stationary q_B=a; S130 patch use computable from blocks and finite-cylinder price. No identified fatal contradiction in these scoped statements. Finite Fraction checks are sanity, not infinity/proof/referee. Frozen S101–S103 A–C, Y/M/H/X, DEF-0020, PA-0001 and primary source grades untouched. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.
