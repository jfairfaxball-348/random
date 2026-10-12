# P4-S108 — Exact-two tree-switch quotients with arbitrarily large computably random ramification

Date 2026-10-12. One owner-invoked CAND-01 Phase4 MATHEMATICS session. Entry live main c15e98bdd188f78479d4b2d2170a031ce8c3591e, parent 87191694a6fa58c8f088abfc7f80e55f10dd9e14, tree 30460b23fccea2e0d1f42c0f15e3d07cacba4710; S107 PR #4 merged by non-force fast-forward. DP2 and CP2, separately quantified in incoming prompt, both UNRESOLVED. Claims below are INTERNALLY PROVED, not independently refereed or externally priority-checked.

## A. Complete legal construction, no limit-point exceptions

Fix ANY decidable prefix-closed tree T subset 2^{<omega} containing the empty word; write [T] for its closed infinite path set. Let the source be x=a u, initial bit a and tail u. If u belongs to [T], set G_T(a u)=u. Otherwise there is a LEAST n>=1 such that rho=u|n is not in T. Write u=rho b t, with b a single next bit and t the remaining infinite sequence, and define

                 G_T(a rho b t) = rho a t.                 (1)

The occurrence of rho itself is retained. The bit a moves after the first exit and the bit b is deleted. No branch test for infinite membership is needed to compute finite output: for an output prefix of length m, inspect a and u|m, decide whether the first non-T prefix rho has length n<m, and either print u|m if no such exit occurs, or print rho a (u from position n+1 to m-1). Thus the output m-prefix has uniform input use m+1 (including a). This finite prefix rule agrees with (1), even when u is a noncomputable infinite T-path or when n=m. G_T is everywhere total, uniformly computable and continuous.

**Theorem A1 (exact TWO points over EVERY y).** If y is in [T], then G_T^-1(y)={0y,1y}. If y is outside [T], let rho=y|n be its shortest prefix outside T and write y=rho c t; then G_T^-1(y)={c rho 0 t,c rho 1 t}. Both descriptions contain two distinct paths. To check completeness, when a source exits T, its output retains rho, so cannot be in [T]; conversely the first exit prefix of source and output coincide. No hidden preimages occur at finite or infinite boundary outputs. In particular y in [T] has EXACTLY two, not one, even when it is an accumulation of exit cylinders. QED.

**Theorem A2 (exact fairness, stronger finite-level identity).** For EVERY output word tau of length m>=1, its full preimage is exactly TWO disjoint source cylinders of length m+1:
(i) If tau is in T, the source cylinders are [0 tau] and [1 tau].
(ii) If tau is not in T and its shortest bad prefix rho has length n=m, again [0 tau] and [1 tau].
(iii) If its shortest bad prefix rho has length n<m and tau=rho c s, its source cylinders are [c rho 0 s] and [c rho 1 s].
Each has measure 2^-(m+1). Therefore lambda(G_T^-1([tau]))=2^-m for every tau. Length-zero follows from totality. By cylinder uniqueness, G_T pushes fair coin to fair coin. The two level-m source cylinders must NOT be mistaken for global inverse sheets: the pairing changes at the first exit. QED.

**Theorem A3 (ramification and discontinuous partner).** A source x=a u has a locally injective clopen source neighbourhood iff u lies outside the BOUNDARY of [T]. Equivalently

                 Ram(G_T) = {a u: a in {0,1}, u in boundary([T])}.     (2)

If u is outside [T], restrict to the clopen prefix [a rho b] at its first exit; (1) is injective there. If u is interior to [T], restrict to [a sigma] with [sigma] subset [T]; G_T is the tail identity there. Conversely if u lies on the boundary of [T], every prefix of u extends some shortest exit rho; for any fixed a and any t, the distinct nearby sources a rho 0 t, a rho 1 t have identical image rho a t. Thus no clopen neighbourhood of a u is injective. At u in [T], J_G(a u)=(1-a)u; as exit prefixes rho approach u, both partners of a rho b t lie on the SAME a-side and approach a u, not (1-a)u. Hence J_G is discontinuous there. All sources outside (2) have locally continuous J by S107 A2. In particular for nowhere-dense [T], Ram(G_T)={0,1} x [T] and K_G=G_T(Ram)=[T]. QED.

## B. A dense-open exceptional complement of arbitrarily small measure

For integer L>=1 enumerate words
             w_(sigma) = sigma 0^(2|sigma|+L) 1
for EVERY finite binary sigma. Let U_L = union_sigma [w_(sigma)] and let [T_L]=2^omega\U_L. T_L is the decidable prefix tree of words having no w_(sigma) as a prefix. Checking a finite word of length m only requires the finitely many lengths n with 3n+L+1<=m and inspecting its substring. No noncomputable membership oracle is used.

Every nonempty basic cylinder [sigma] contains [w_(sigma)], so U_L is dense open and [T_L] is effectively closed NOWHERE DENSE. By the union bound,

    lambda(U_L) <= sum_(n>=0) 2^n * 2^-(3n+L+1)
                = (4/3)*2^-(L+1).

Therefore lambda([T_L]) >= 1-(4/3)*2^-(L+1). With L=5 this is at least 47/48. No independence or pairwise-disjointness of the enumerated holes was assumed; overlaps only strengthen the lower bound. For any positive rational epsilon choose L large enough that (4/3)2^-(L+1)<epsilon.

**Theorem B1 (large ramification).** Each G_(T_L) is a total computable fair EXACT-two quotient with
  lambda(Ram(G_(T_L))) = lambda([T_L]) >= 1-(4/3)*2^-(L+1);
  K_(G_(T_L)) = [T_L], the same positive-measure nowhere-dense output set.
This follows from (2) and the fact that the two input copies each have measure one half. In particular its ramification is not null, not effectively Schnorr-null, and can have measure arbitrarily close to ONE. Both K_G and Ram may contain computably random sequences: CR has measure one, so lambda(CR intersect Ram)=lambda(Ram)>0. The actual double-fibre partner of a u in [T_L] is the distinct (1-a)u. This explicitly REBUTS the candidate universal assertion that every exact-two fair quotient has effectively Schnorr-null Ram (and its weaker plain-null variant). It also shows the S106 nowhere-dense exceptional set K_G need not have measure zero. QED.

## C. Yet every tree-switch quotient preserves ordinary computable randomness

**Theorem C1 (global CR conservation in this family).** For EVERY decidable prefix-closed T as above, G_T(CR) subset CR, including CR sources in Ram(G_T).

Proof. For every fixed finite word p, a sequence p t is CR iff its tail t is CR. The fact is valid for ordinary total nonnegative rational computable martingales, via the finite cylinder restriction and extension with zero or constant capital off the cylinder; no ML-test substitution is involved. If a u is CR then u is CR. When u belongs to [T], G_T(a u)=u, hence CR. Otherwise u=rho b t at the first exit; since a rho b t is CR, t is CR, so rho a t is CR. There is NO excluded exceptional source, no computable last-injury rate, and no source martingale construction needed beyond this standard fixed-prefix equivalence. QED.

Consequently this example meets the exact fair/cap/partner/ramified-CR conditions but NOT the nonCR output and winning total rational output martingale required to refute DP2 or CP2. The positive-measure exceptional locus is fully CR-SAFE for this family. This distinguishes a geometric obstruction to null-cover conservation from a real CR-destroyer.

## D. Independent effective-conservation attack, failures and repairs

D1 (attempt, REFUTED): prove every EXACT-two fair quotient's Ram is Lebesgue null, then upgrade to effective Schnorr-null and derive CP2. B1 defeats even the first universal assertion with explicit uniformly priced examples and actual ramified CR points. Its failure is not an artefact of category: Ram has arbitrarily large measured mass. S004's zero-weight genuine branch and S005's noncomputable crossing measures give further independent reasons not to invent a uniform conditional-mass compiler.

D2 (repaired, PROVED in class C1): for this large-ramification family do NOT discard ram sources; instead preserve CR via a source-dependent, FINITELY DELIMITED tail-equivalence chart. If G_T(a u) has its source u in [T], it merely removes first input bit. If u exits, it exchanges two fixed finite prefixes of a common tail t. Each source has a finite witness for the branch, except members of [T], where the direct deletion argument applies pointwise without deciding membership. Thus no purported effective nullness is necessary. This is a genuine full-source theorem but depends on the special form (1), and cannot be generalized to arbitrary F2 without a new argument.

D3 (failed broad lift): the two preimage source cylinders at each finite output precision have exact price, but the first-exit pairing may switch at arbitrarily large depth along an actual CR ramified source. These uniformly priced finite charts do NOT yield a global continuous partner involution; A3 gives a direct counterexample. To lift an arbitrary successful output martingale for general F2 one still needs a single ordinary rational source martingale whose capital succeeds on the chosen source, without a computable stabilization modulus or noncomputable conditional stopping prices. C1 avoids that obligation only because finite-tail invariance applies to its special formula. Any claim that these finite prices universally imply CP2 is unjustified.

## E. Separate destruction/surgery avenue

E1. Attempt to replace the trivial output u on the fat ramified set with S083's nonCR destroyer, preserving the exceptional partnered fibre. On U_L the images and source prefixes must still have exact dyadic price and global exactly-two fibres. Replacing only the closed nowhere-dense [T_L] fails: two continuous maps agreeing on dense open input complement agree everywhere (S107's no-graft lesson). Introducing a noninjective fair S083 map by pre/post composition creates fibres of cardinal >2 at some outputs by S107 B1. No legal redesigned all-source tree, winning output martingale, and actual CR partnered destroyed source were obtained. UNRESOLVED.

E2. A potential non-compositional repair would modify infinitely many exit cones AND the fat base coherently, with computable finite-stage prices and a true paired witness, while allowing non-tail-trivial coding of later source bits. Its remaining exact lemma is a compatible globally fair width-two inverse tree whose ramified CR source maps to a nonCR output; neither finite cone puzzles nor the above CR-safe tree switch prove its existence.

## F. Claims and limits

INTERNALLY PROVED: A1 all-output exact two; A2 exact dyadic cylinder prices with two source (m+1)-cylinders per m-cylinder and uniform finite use; A3 exact ramification/partner discontinuity; B1 nowhere-dense positive-measure (arbitrarily close to full-measure) exceptional source and output loci containing CR sources; C1 CR conservation for ALL sources in the tree-switch family. No novel external priority, formalisation or independent review claim.

REFUTED: "every fair exact-two ramification set is null" and therefore "every such set is effectively Schnorr-null"; "finite-level two-cell covering forces continuous partner" (the latter is false here). NOT refuted: CP2, DP2, EQ, SEP, S107 A1-A4, or the possibility of a different effective all-source martingale argument.

UNRESOLVED: DP2 for every F2 map at ACTUAL double CR sources; CP2 for EVERY globally exactly-two map; EQ R2=MLR; SEP a z in R2 outside MLR; F2(R2) subset R2. The examples are CR-conserving and therefore cannot furnish an output total rational winning martingale. Original Y/M/H/X, S101-S103 A-C, recorded primary-source access, historical S105 NO-GO and the owner post-S105 research pivot unchanged. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. No publication work.

Finite check: phase4/P4-S108_TREE_SWITCH_AUDIT.py verified 36,840 finite source-prefix assignments, including 16,380 at one fixed parameter up to depth 12, and tree-parameter sweeps L=1,2,3,5,8 to depth 10. These checks are sanity only; infinite quantifiers follow the symbolic arguments above.
