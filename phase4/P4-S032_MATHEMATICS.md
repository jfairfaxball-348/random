# P4-S032 — finite-ambiguity reconnaissance and one-hole theorem selection

Date: 2026-10-06
Session: P4-S032
Incoming checkpoint: 26c86b254410806dac04ddb57584d97b0da7da1c
Scope: Phase 4 — Mathematics; sustained finite-ambiguity pivot after P4-S031
Result: **NULL OUTPUT-AMBIGUITY FORCES COMPUTABLE-RANDOMNESS PRESERVATION; ARBITRARILY SMALL POSITIVE AMBIGUITY CAN STILL DESTROY; STATIC FIBRE CARDINALITY AND AMBIGUITY MASS ARE NOT THE RESOURCE; SELECT THE ONE-HOLE NORMALIZATION / SOURCE-CHARACTERIZATION THEOREM TARGET**

## Authority, uniqueness and scope

Live main matched the requested incoming checkpoint exactly before substantive work and again immediately before the write. Repository search returned no committed P4-S032 record, so the session identifier was unused.

P4-S001 through P4-S031, the selected CAND-01 authority, and phase4/P4_RESEARCH_PIVOT_AFTER_S031.md were read. All validated mathematics through P4-S031 is frozen. In particular P4-S011 and P4-S015 through P4-S031 are preserved and the ticket/reserve/frontier/recycling sequence is not reopened.

This session is reconnaissance under the sustained pivot. It develops four exact probes: robustness/cross-randomness, a structural null-ambiguity threshold, composition/factorisation, and the scan ambiguity budget/source-side mechanism. It then selects one theorem programme for follow-up.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## 1. Robustness classes

For each integer k>=1 let F_k be the class of everywhere-total computable fair-coin-preserving maps F:2^omega->2^omega with

|F^{-1}(y)| <= k

for every y. Define

R_k = {x in CR : F(x) is in CR for every F in F_k}

and

R_fin = intersection_{1<=k<infinity} R_k.

The immediate consequences required by the pivot are:

1. P4-S001 gives R_1=CR.
2. Since F_k is contained in F_{k+1}, R_{k+1} is contained in R_k.
3. P4-S011 supplies x in CR and D in F_2 with D(x) not in CR. Hence R_2 is a proper subclass of CR. The same D belongs to every F_k for k>=2, so R_k is a proper subclass of CR for every k>=2 and R_fin is a proper subclass of CR.

These are internal consequences of settled programme mathematics, not novelty claims.

### Proposition 1 — Martin-Löf randoms lie in every finite-ambiguity robustness class

MLR is contained in R_fin.

Proof. Every total computable fair-coin-preserving map is a computable-probability-space morphism. THM-0035 conserves Martin-Löf randomness under such morphisms. Since Martin-Löf randomness implies computable randomness, every Martin-Löf-random x survives every F in every F_k. ∎

Thus

MLR subseteq R_fin subseteq R_k subseteq R_2 proper-subset CR

for k>=2, with no claim here that either inclusion involving MLR is strict or an equality.

### Proposition 2 — computable-randomness destruction here never destroys Schnorr randomness

If x is computably random and F is any total computable fair-coin-preserving map, with no fibre bound required, then F(x) is Schnorr random.

Proof. THM-0002 gives CR=>Schnorr. THM-0036 conserves Schnorr randomness under computable-probability-space morphisms. ∎

Consequently the P4-S011 output is Schnorr random but not computably random; by THM-0016 it is also Kurtz random. This gives a sharp comparative fact: the one-bit mechanism separates computable randomness from weaker Schnorr/Kurtz randomness, whereas Martin-Löf randomness is conserved even without a finite-fibre restriction.

## 2. Structural threshold: null output ambiguity is safe

For a total computable fair-coin-preserving map F define its output ambiguity locus

A_F = {y : |F^{-1}(y)| >= 2}.

No effective presentation of A_F is assumed.

### Theorem 3 — null-ambiguity preservation

Let F:2^omega->2^omega be everywhere total, computable and fair-coin preserving. If lambda(A_F)=0, then F has an a.e.-computable fair-coin-preserving inverse and therefore preserves computable randomness.

This theorem does not require a finite global fibre bound.

#### Proof

First, as in P4-S001, total continuity makes ran(F) compact and hence closed. Fair-coin preservation forces ran(F)=2^omega, since a missed output point would lie in a positive-measure cylinder with empty preimage.

For every finite output word tau, the set F^{-1}([tau]) is effectively clopen. Indeed P4-S001's effective forward-use search computes a finite input use u(|tau|), after which the length-u input cylinders can be checked finitely for the output prefix tau.

Construct a partial inverse G. Given oracle y and requested input precision n, search m=0,1,2,... until the effectively clopen set

C_m(y)=F^{-1}([y restricted to m])

is contained in a single length-n input cylinder [sigma]. This is decidable from the finite clopen representation. When found, output sigma.

If F^{-1}(y)={x}, the nested compact sets C_m(y) have intersection {x}. For every n some C_m(y) must be contained in [x restricted to n]; otherwise the nested compact sets C_m(y) intersected with the complement of [x restricted to n] would all be nonempty and compactness would produce a second point in F^{-1}(y). Hence G(y) is total and equals x.

If y has two distinct preimages, choose n separating them. Every C_m(y) contains both, so the search at precision n never succeeds. Thus the domain of G is exactly the singleton-fibre locus S_F=2^omega\A_F. As the domain of this partial Type-2 computation it is a constructive G_delta, and by hypothesis it has measure one.

Let X_0=F^{-1}(S_F). Since F preserves lambda, lambda(X_0)=1. On X_0 and S_F the maps are inverse.

It remains to check that G preserves fair coin on its full-measure domain. For a cylinder [sigma], let C={y in S_F:G(y) in [sigma]}. Then

F^{-1}(C) = [sigma] intersect X_0.

Therefore, by measure preservation of F,

lambda(C)=lambda(F^{-1}(C))=lambda([sigma] intersect X_0)=2^{-|sigma|}.

Cylinder extension gives the a.e. measure-preserving property. Hence F and G satisfy THM-0038 and computable randomness is invariant on their full-measure inverse domains. In particular F preserves computable randomness. ∎

### Corollary 4 — several proposed in-between subclasses collapse to the safe side

Any total computable fair-coin-preserving map with only finitely many double outputs preserves computable randomness. More generally, any such map whose non-singleton output fibres are confined to an arbitrary lambda-null set preserves computable randomness. Effective nullness is not required.

This is a genuine threshold between k=1 and bare k=2, but it is not a complete k=2 characterization: the exactly-two-to-one left shift from P4-S002 has ambiguity locus of measure one and nevertheless preserves computable randomness.

### Theorem 5 — arbitrarily small positive ambiguity can still destroy computable randomness

For every epsilon>0 there is a total computable fair-coin-preserving global-k=2 map F with

0 < lambda(A_F) < epsilon

and a computably random x such that F(x) is not computably random.

Proof. Let D and x_0 be the settled P4-S011 destroyer and vulnerable computably random source. Theorem 3 implies lambda(A_D)>0, since otherwise D would preserve computable randomness.

Choose a finite word a of length r with 2^{-r}<epsilon. Define F_a blockwise:

- on [a], F_a(a concatenated u)=a concatenated D(u);
- outside [a], F_a is the identity.

The cylinder [a] is clopen, so F_a is total computable. It preserves fair coin separately on [a] and its complement, and there are no cross-block collisions; hence every fibre has size at most two.

Finite prefixing preserves computable randomness and non-computable-randomness by the elementary martingale shift argument. Thus a concatenated x_0 is computably random while

F_a(a concatenated x_0)=a concatenated D(x_0)

is not.

Moreover A_{F_a}=a concatenated A_D, so

lambda(A_{F_a})=2^{-r} lambda(A_D),

which is positive and below epsilon. ∎

Theorems 3 and 5 show that zero ambiguity mass is a real preservation boundary, but there is no positive ambiguity-mass threshold. Together with the P4-S002 left shift, even ambiguity mass one can be safe. Therefore ambiguity mass is not the sought invariant.

## 3. Composition and factorisation probe

### Lemma 6 — multiplicities multiply

If F is in F_j and G is in F_k, then G composed with F is in F_{jk}.

Proof. Total computability and measure preservation compose. For an output z, G^{-1}(z) has at most k elements and each of those has at most j preimages under F. ∎

### Corollary 7 — robustness transports down a stage

For every j,k,

F_j(R_{jk}) subseteq R_k.

That is, if x is robust against multiplicity jk and F is a j-to-one-or-less stage, then F(x) is robust against every k-to-one-or-less second stage.

Proof. F(x) is computably random because F itself belongs to F_{jk}. For G in F_k, Lemma 6 puts G composed with F in F_{jk}. ∎

This identifies an important obstruction to a naive hierarchy-collapse argument. Even if every global-k=4 map admitted an effective factorisation into two k=2 maps, R_2 robustness alone would only say that the first-stage image is computably random. It would not say that the first-stage image is itself in R_2. A factorisation route therefore needs an additional hereditary/invariance principle for R_2, not merely binary decomposition.

Factorisation remains potentially useful, but it does not by itself outrank the source-characterization route.

## 4. Scan ambiguity budget: fibre size is a static hole count

Return to the settled P4-S008 adaptive no-repeat scan model. For a transcript y let Q(y) be the queried source coordinates and put

h(y)=|omega\Q(y)|.

P4-S008 already identifies the fibre over y with arbitrary assignments to the omitted coordinates.

### Lemma 8 — exact scan multiplicity

If h(y)<infinity then

|F_T^{-1}(y)| = 2^{h(y)}.

If h(y)=infinity the fibre is uncountable. Consequently an adaptive no-repeat scan has global fibre bound at most k exactly when

h(y) <= floor(log_2 k)

for every transcript y.

Thus, inside the scan subclass, the multiplicity hierarchy has power-of-two plateaux:

- k=1 means zero holes on every transcript;
- k=2 and k=3 both mean at most one hole;
- k=4,5,6,7 mean at most two holes;
- and so on.

This is an exact ambiguity-budget calculation, not a claim about arbitrary finite-to-one maps.

### Consequence — final hidden information is not the P4-S011 resource

On the vulnerable P4-S011 source x_0, every epoch triggers, every source coordinate is eventually queried, and the final fibre is a singleton. Hence h(F_T(x_0))=0.

Nevertheless the output is not computably random.

So the destroyer is not powered by a bit that remains hidden in the final inverse. What k=2 permits is a renewable *counterfactual* hole: during an epoch one fresh coordinate can be withheld as a sentinel while other fresh coordinates are inspected; once a wager becomes visible the sentinel is consumed and a new least-fresh coordinate can become the next withheld coordinate. On avoiding siblings the current hole may persist forever, keeping the global fibre bound at two. On the vulnerable target the hole migrates and is eventually consumed each time.

This temporal renewable ambiguity is compatible with a singleton final fibre and is therefore deeper than raw final inverse information.

## 5. Source-side scan robustness

Define the one-hole scan robustness class OH by

OH = {x in CR : F_T(x) is in CR for every total computable adaptive no-repeat scan T such that every transcript omits at most one source coordinate}.

Every such scan map is in F_2, so

R_2 subseteq OH.

P4-S011 gives a computably random source outside OH, hence OH is also a proper subclass of CR. Proposition 1 gives MLR subseteq R_2 subseteq OH.

P4-S012 supplies the central source-side meaning of failure in this class. If a computably random x is destroyed by a one-hole scan and a computable output martingale d, the winning target must be on a singleton scan fibre and P4-S012 constructs a total-on-x self-avoiding signed fractional stake functional which, in the scan's query order, exactly reproduces d's capital. Conversely, P4-S012 shows that a target-winning self-avoiding partial stake spine in the least-fresh architecture yields an exact global-k=2 destroyer.

This does not yet prove an intrinsic scan-free characterization. It does identify an exact mechanism in the largest presently understood destroying subclass.

## 6. Reconnaissance comparison

Four routes were tested seriously.

### Route A — ambiguity mass

Strong exact progress was possible immediately: null ambiguity is safe, while arbitrarily small positive ambiguity can destroy and full-measure ambiguity can also be safe. Therefore ambiguity *mass* is an informative boundary but not the invariant.

### Route B — robustness hierarchy / cross-randomness

We obtain MLR subseteq R_fin proper-subset CR and universal Schnorr preservation under the ambient map class. This is a useful placement, but deciding R_2 versus MLR or strictness of R_2,R_3,... directly is too coarse for the next bounded theorem without a mechanism for arbitrary k=2 failure.

### Route C — composition/factorisation

Multiplicities multiply and R_{jk} transports to R_k after an F_j stage. But binary factorisation alone does not collapse the robustness hierarchy: the missing statement is hereditary R_2 robustness of the intermediate image. This route is demoted until the source-side invariant is clearer.

### Route D — one-hole normalization / source characterization

The scan calculation exposes a concrete candidate resource: renewable one-hole access. It explains k=1 safety, contains the exact P4-S011 failure, has an exact P4-S012 stake converse, and remains meaningful even though the winning source ends on a singleton fibre. The unresolved question is whether this is merely one construction architecture or a normal form for arbitrary k=2 destruction.

This route has the best combination of depth, explanatory power and tractability.

## 7. Selected theorem target

### Selected target: one-hole normalization

Determine whether

R_2 = OH.

Equivalently: if F is an arbitrary total computable fair-coin-preserving global-k=2 map, x is computably random, and F(x) is not computably random, must there exist a total computable one-hole adaptive no-repeat scan T such that T(x) is not computably random?

A slightly more flexible normalization may allow pre/post composition by computable fair-coin-preserving homeomorphisms, which do not change computable randomness by P4-S001. Any such relaxation must be stated explicitly and proved equivalent at the robustness level.

A positive theorem would reduce arbitrary binary-ambiguity vulnerability to the P4-S012 source-side self-avoiding stake mechanism. A negative theorem would be equally informative if it constructs a genuinely non-scan k=2 destroyer and isolates the extra resource used by that map.

This target outranks the alternatives because it attacks the actual mechanism rather than the size of the final fibre, has a natural source-side interpretation already supported by P4-S012, and can organize several bounded sessions without reverting to the frozen bankroll sequence.

## 8. Bounded multi-session plan

P4-S033: formalize OH and attack the first normalization step. Use the P4-S002/P4-S007 width-two inverse skeleton and a succeeding output martingale to test whether arbitrary k=2 failure can be converted into a one-hole scan/stake witness. Prove the strongest coherent subclass theorem available or isolate an exact obstruction. Use Theorem 3 to discard a.e.-injective maps from the negative side.

P4-S034: if normalization remains live, analyze the obstruction from non-coordinate output mixing. Test whether computable fair-coin homeomorphism conjugacies can turn a general k=2 witness into a scan witness, or construct a candidate non-scan separation.

P4-S035: resolve the strongest surviving structured subclass, for example maps with a coherent effective width-two inverse coding, and determine whether failure forces renewable branch migration/self-avoiding stakes there.

P4-S036, only if warranted: compare the resulting OH/R_2 boundary with MLR and with the finite-hole scan hierarchy; if normalization fails, replace OH by the sharper invariant exposed by the separation.

This is a bounded research plan, not a prediction that the normalization theorem is true.

## Guards

- P4-S005 through P4-S031 remain settled.
- P4-S011 and P4-S015 through P4-S031 are preserved.
- The P4-S015–P4-S031 local ticket/reserve sequence remains frozen as default trajectory.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- DEF-0020 is unchanged.
- No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.
- Phase 4 remains OPEN; Phase 5 remains CLOSED.
