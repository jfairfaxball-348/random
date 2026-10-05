# P4-S007 — k=2 delayed-coalescence inverse-tree boundary

Date: 2026-10-05
Session: P4-S007
Incoming checkpoint: b25136e24991cb988dc1186567a5639a3c41b38c
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 only
Result: **K2 FORCES A COHERENT COMPUTABLE WIDTH-TWO INVERSE SKELETON AND ONE-INJURY POST-COALESCENCE AT EACH FIXED PRECISION; THIS DOES NOT FORCE COMPUTABLE PERSISTENCE TIMES, CONDITIONAL WEIGHTS OR A COMPUTABLE-RANDOMNESS TRANSFER; THE DELAYED-COALESCENCE SRC-0061 ROUTE REMAINS BLOCKED**

## Authority, uniqueness and scope

Live `main` matched the incoming checkpoint exactly before substantive work, and repository search returned no committed P4-S007 record. P4-S007 was therefore unused.

Gate 3 is PASS and Phase 4 is OPEN for selected CAND-01. Phase 5 remains CLOSED. P4-S001 through P4-S006 are preserved exactly. This session stays strictly at k=2.

P4-S005 and P4-S006 are treated as settled boundaries. In particular, no attempt is made to recover computability of the P4-S004 low-weight crossing measures, and no computable mass, computable selector or computable stabilization modulus is assumed for the canonical lexicographic sheets. The P4-S006 effective-complexity conclusions and one-hole collapse lemma remain unchanged.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard remains historical. DEF-0020 and all catalogue/source convention guards are unchanged. No k>2, novelty/open-status, Gate-4, publication or outreach claim is made.

## Exact k=2 setting

Let lambda be fair-coin measure and let F:2^omega -> 2^omega be everywhere-total computable, lambda-preserving, and satisfy

|F^{-1}(y)| <= 2

for every output y.

For n,m in omega and y in 2^omega define the finite compatible-prefix set

C_{n,m}(y)
 = { sigma in 2^n : [sigma] intersects F^{-1}([y↾m]) }.

For fixed n and y these sets decrease with m. They are uniformly computable from y↾m because total computability of F makes every cylinder preimage computable clopen.

P4-S003 already proved that for every n there is a computable output precision after which every output cylinder has at most two compatible n-prefixes. P4-S007 uses that fact to impose coherence across n.

## Lemma 1 — a computable coherent width-two inverse skeleton is forced

There is a computable nondecreasing function c(n), with c(n)>=n, such that for every y,

P_n(y)=C_{n,c(n)}(y)

is nonempty and has at most two members, and every member of P_{n+1}(y) extends a member of P_n(y).

Moreover the infinite paths through the level sets P_n(y) are exactly F^{-1}(y).

### Proof

For each n, use the decidable finite search from P4-S003 to find some d(n) such that every output string tau of length d(n) has preimage meeting at most two n-cylinders. Replace d by the monotone closure

c(n)=max(n,d(0),...,d(n)).

The at-most-two property persists when the output cylinder is refined, so |P_n(y)|<=2. Surjectivity from P4-S002 gives nonemptiness.

If sigma in P_{n+1}(y), choose z in [sigma] with F(z) extending y↾c(n+1). Since c(n+1)>=c(n), the n-prefix sigma↾n meets F^{-1}([y↾c(n)]), hence belongs to P_n(y). Thus the selected levels form a coherent prefix tree of width at most two.

Every x in F^{-1}(y) has x↾n in P_n(y), so every fibre point is a path through the skeleton.

Conversely, let z have z↾n in P_n(y) for every n. Choose z_n in [z↾n] with F(z_n) extending y↾c(n). For any requested output precision r, take n large enough that n is at least a forward use for r and c(n)>=r. Then z_n and z agree through that use, so F(z)↾r=F(z_n)↾r=y↾r. Hence F(z)=y. Therefore the path set of the skeleton is exactly the fibre. ∎

### Consequence

The apparent possibility of arbitrarily many finite source-prefix candidates is real only before a computably chosen diagonal sampling. Bare k=2 already lets one resample the inverse approximation into a coherent tree with at most two nodes at every source level.

This is stronger than an unrelated collection of two-prefix lists, but it still does not label the nodes as persistent branches.

## Lemma 2 — exact shape of the width-two skeleton

Fix y.

### Double fibre

If F^{-1}(y)={x_0,x_1} with x_0 != x_1, let r be one more than their first differing coordinate. Then for every n>=r,

P_n(y)={x_0↾n,x_1↾n}.

In particular, after the genuine split the skeleton consists of two exact persistent tracks and admits no further phantom node.

**Reason.** Both true prefixes belong to P_n(y) and are distinct. Since P_n(y) has size at most two, there is no room for any third candidate.

### Singleton fibre

If F^{-1}(y)={x}, then every P_n(y) contains x↾n and may contain at most one additional phantom prefix q_n.

For every fixed r there is N such that, for all n>=N, every member of P_n(y) extends x↾r.

**Proof.** Otherwise some prefix rho of length r different from x↾r would have compatible extensions in P_n(y) for arbitrarily large n. By coherence and finite branching, those extensions would yield an infinite skeleton path extending rho. Lemma 1 would then give a second point of F^{-1}(y), contradiction. ∎

Thus a singleton fibre may exhibit repeated temporary side branches, but their first disagreement with the true point is forced to drift arbitrarily far to the right.

## Lemma 3 — fixed-precision coalescence has an explicit finite-injury bound

For fixed n and y, the raw candidate sets C_{n,m}(y) form a decreasing sequence of nonempty subsets of 2^n.

Therefore:

1. before the computable coalescence stage c(n), at most 2^n-1 candidate deletions can occur;
2. from stage c(n) onward there are at most two candidates;
3. after c(n), at most one further candidate deletion can occur.

Equivalently, the lexicographically least compatible n-prefix can change at most 2^n-1 times in total, and after c(n) at most once; the same holds for the lexicographically greatest compatible n-prefix.

This sharpens the P4-S006 effective Baire-1 statement at each fixed precision: the canonical extremal prefixes have a computable mind-change bound. What is not forced is a computable time at which the last allowed change has happened.

A uniform computable persistence/stabilization test would in particular turn the P4-S006 extremal limits into computable selectors. P4-S002's collision map already rules out such a general selector. Hence the bounded number of injuries cannot be promoted to a uniformly computable last-injury stage.

## Corollary 4 — bounded finite information is forced, but it is not coherent enough for the known transfer arguments

At source precision n, y↾c(n) computes a list P_n(y) of at most two possible strings containing x↾n for every x in F^{-1}(y). Thus one additional choice bit is enough to select x↾n from that finite list.

This is only a per-precision information bound.

- On a double fibre, once n is beyond the true split, the lexicographic lower/upper choice is coherent forever.
- On a singleton fibre, a temporary phantom may occur on either side of x and may disappear only after an unbounded output delay. The list-index bit can therefore fail to provide a uniform persistent branch label.
- No conditional source mass is determined by the cardinality-two list. P4-S004 permits an actual persistent sheet of weight tending to zero, and P4-S005 shows that the associated hitting probabilities need not be computable.

There is also a useful partial inverse consequence. There is one oracle procedure which, given y, computes the unique point of F^{-1}(y) whenever that fibre is a singleton: to determine r source bits, search deeper skeleton levels until all current candidates share one r-prefix. Lemma 2 guarantees termination on singleton fibres. On a double fibre the procedure may stop only before the genuine split and then cease producing further bits.

This partial singleton inverse does not provide an a.e. inverse pair or a computable component measure.

## Lemma 5 — post-coalescence collapse is architecture-independent

Fix n and an output prefix tau of length at least c(n). The compatible n-prefixes form a set of size one or two.

If there are two, say sigma_0 and sigma_1, then every source coordinate j<n that is not already determined by tau varies only through the single binary choice between sigma_0 and sigma_1.

Consequently, any later information that selects one of sigma_0,sigma_1 simultaneously determines every first-n coordinate on which the two strings differ.

In particular, suppose a scan-style construction intends later to expose a genuine betting coordinate j<n and sigma_0(j) != sigma_1(j). Once that later output information determines the value of x_j, it identifies which of the two n-prefixes is actual and therefore pre-reveals every other coordinate k<n on which sigma_0 and sigma_1 differ.

This is the P4-S006 one-hole collapse phenomenon without any XOR, mask or coding assumption. After the computable coalescence point c(n), every exact k=2 inverse state below source precision n is intrinsically a single binary cohort.

## Consequence for delayed-coalescence SRC-0061 completions

A delayed-coalescence construction can evade Lemma 5 only by maintaining a freshness condition: before the output reaches c(n), all but at most one future genuine betting coordinate below n must already have been safely dealt with, or else the surviving two n-prefixes must agree on every such coordinate except possibly one.

The important point is that c(n) is a finite computable map-dependent bound which works simultaneously for every output. Delaying raw coalescence along one transcript does not remove this global bound.

However, this does **not** prove that a scan-style k=2 witness is impossible. A construction might arrange its coalescence schedule so that the required genuine bets occur before the relevant c(n), or move the protected betting positions to larger source coordinates quickly enough.

The committed SRC-0061 / THM-0072 mechanism supplies no such global freshness or bounded-query-time property. Its successful nonmonotonic strategy may choose an unqueried position arbitrarily late, and P4-S003 already records that decisive gains may be concentrated on sparse future positions. Therefore SRC-0061 cannot be reused here without a new theorem proving the freshness condition.

## Why the coherent skeleton still does not yield a computable martingale transfer

The new skeleton removes one possible topological obstruction but leaves the established measure/effectivity obstruction intact.

1. **No persistent candidate decision.** At a two-node level there is no uniform computable procedure deciding whether both nodes persist or which one eventually dies. Such a procedure would give the forbidden computable selector/stabilization information.
2. **No weight lower bound.** Even when the two nodes are already the two true branches of a double fibre, one branch can carry conditional weight tending to zero by P4-S004.
3. **No computable normalization.** P4-S005 shows that natural stopping probabilities and symmetric fibre-count masses can be noncomputable.
4. **Fixed-stage pullbacks remain incoherent.** P4-S004's exact martingales e_m still reproduce each individual output capital stage, but the width-two skeleton does not choose computable stopping times or branch weights with which to combine them into one succeeding source martingale.
5. **Bounded mind changes are not bounded delay.** A computable bound on how many times a candidate can change gives no computable bound on when the final change occurs; ordinary computable martingales cannot wait on a noncomputable persistence decision.

Accordingly, P4-S007 does not prove general forward computable-randomness preservation.

## Exact non-conservation route pursued and not completed

The negative target would require a total computable fair-coin-preserving k=2 map F and a computably random x such that F(x) is not computably random.

The delayed-coalescence idea was tested at the structural level needed by any SRC-0061-style completion. Lemma 1 shows that, after computable diagonal resampling, the many-candidate inverse state always compresses to at most two coherent source prefixes. Lemma 5 then shows that once such compression has occurred below precision n, revealing one distinguishing future betting coordinate collapses all remaining first-n ambiguity.

Thus a successful moving-sheet scan construction must do more than retain many raw candidates for a long time. It must prove the global freshness condition relative to the computable coalescence function c(n), while also proving totality, fair-coin preservation and fibres of size at most two on **every** transcript.

No such freshness theorem is available for SRC-0061, and no alternative exact k=2 destroyer is completed in this bounded session. SRC-0061 is therefore not reused as a finite-fibre witness.

## Successful and failed mechanisms

Successful:

1. A computable monotone coalescence schedule c(n) producing a coherent inverse skeleton of width at most two at every source level.
2. Exact identification of the double-fibre tail: after the first true split, the two skeleton nodes are exactly the two true branch prefixes.
3. Exact singleton behaviour: any phantom branch must move its first disagreement arbitrarily far to the right.
4. A computable fixed-precision mind-change bound, with at most one post-c(n) injury.
5. A uniform partial inverse procedure on singleton fibres.
6. An architecture-independent post-coalescence collapse lemma generalizing P4-S006's one-hole mask obstruction.
7. A precise necessary freshness condition for any future SRC-0061-style k=2 completion.

Failed or incomplete:

1. Computing the last injury/persistence time of a skeleton branch.
2. Turning the one-bit-per-precision list bound into a coherent computable inverse branch or computable component measure.
3. Converting the finite-injury skeleton into one computable martingale transferring arbitrary output-martingale success.
4. Proving that every possible delayed-coalescence scan completion violates the freshness condition.
5. Constructing an exact total computable fair-coin-preserving k=2 computable-randomness destroyer.

## Proof dependencies and guards

The new mathematics uses the P4-S002 computable-clopen inverse approximants, the P4-S003 two-prefix theorem, elementary compactness/finitely-branching tree arguments, and the settled P4-S004 through P4-S006 boundary results. No new literature theorem is imported.

SRC-0061 / THM-0072 is used only as the previously recorded unrestricted scan mechanism. It is not claimed to satisfy the new freshness condition and is not promoted to a finite-fibre counterexample.

- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- The pre-Phase-4 Gate-3 guard is preserved historically.
- P4-S001 through P4-S006 are unchanged exactly.
- General k=2 forward computable-randomness preservation/failure remains unresolved.
- No result is claimed for k>2.
- DEF-0020 and all catalogue/source convention records are unchanged.
- No novelty/open-status claim is made.
- Gate 4 is not reviewed. Phase 5 remains CLOSED.
