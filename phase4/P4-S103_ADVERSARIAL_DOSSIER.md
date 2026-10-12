# P4-S103 — Fresh adversarial audit of the selected A–C package

2026-10-12. Exactly one owner-invoked Phase 4 Mathematics session. Entry main
`dbcf3f754deeb7bd06d2400b36a67eaff194e1cc`, sole parent
`4b6e9a0e85aab3fe293e80d18847c0ba6b8d3277`, tree
`64195c47f24d2c27869b597a21852716df42e220`. Incoming prompt archived verbatim.

**Disposition: A, B and C survive this fresh written adversarial check. No
fatal gap, theorem-changing repair or quarantined descendant was identified.**
This is a new same-agent derivation from the definitions and original proofs,
not independent peer review, formal verification, novelty assessment or Gate 4.
R₂ versus MLR is unresolved. Source-specific access remains unchanged: the
original JSL proof was not obtained and was not compared with the thesis.

The audit read the original S081–S083 mathematics and the S101 dossier, minimal
matrix, obligations, validation and close; S102 source dossier/access/validation/
close; entry authority, CAND-01, Gate-3 review, both pivots and S100 allocation.
Sections below state each hostile alternative and the actual argument that
excludes it. The evidence is the written argument; finite replays are auxiliary.

## 1. Frontier: semantic holes versus a computable finite bound

Fix a total no-repeat scan T which omits at most h coordinates on every infinite
transcript. For fixed n, form the transcript tree of states with more than h
unread coordinates in [0,n). It is prefix closed: extending a transcript only
removes unread coordinates. If states of arbitrary length existed, König's
lemma would give an infinite path. Along it the unread subsets of [0,n) are
decreasing finite sets; they stabilize with size greater than h. Those stabilized
coordinates are permanent omissions. This contradicts the hypothesis. Therefore
some finite depth has no bad state. Simulating all histories at each trial
depth is a terminating finite computation, conditional on T's totality. Search
for that depth, and replace the results by their running maximum to obtain c(n).

This proves uniformity over transcripts BEFORE choosing a source. It does not
extract a computable enumeration of valid scan indices. Checking a candidate
frontier requires only finitely many computations; finding one halts only for
valid indices. This distinction is essential in the guessed-run construction.

At time t at most t distinct coordinates have been queried; hence c(n)≥n−h.
Thus n_t=max{n:c(n)≤t} is finite and computable (search n≤t+h), is nondecreasing,
and tends to infinity. Take c(0)=0, so the maximum exists also at t=0. This is
an explicit harmless convention, not an added hypothesis. Set U_t to the unread
coordinates below n_t, BEFORE processing query t. Its size is at most h.

Hostile case: many coordinates enter at one frontier jump while another is
about to be read. The about-to-be-read coordinate still occupies its colour.
The simultaneous active set is U_t, of size ≤h. Colour newcomers in increasing
order, retaining every old active colour; only release a colour AFTER its query
is processed. This uses at most h colours and gives disjoint held intervals of
each colour, including their read endpoints. No target-specific frontier is used.

## 2. Own-transcript simulation and factor copying

For colour i, the compiled scan keeps simulated T-time/history, the colouring,
and a finite cache of values read by the compiled scan. Before processing the
next T-query, it pulls the least uncached active hold of another colour with
zero stake. Once no such hold remains, it processes the T-query: if already
cached, append the cached answer to T-history and advance T-time silently;
otherwise query it freshly and append the actual answer. Copy the original
stake only for held queries of colour i. The fill account pulls all holds and
copies only fill-query stakes.

Hostile case: silent skips run forever and the next-query program is partial.
At a fixed finite compiled transcript its cache is finite. Every silent skip
processes a different original query already in that cache, since T never
repeats. Consequently only finitely many silent skips can occur before a fresh
output. A pull is itself a fresh output, not silent waiting. Conversely simulated
T-time cannot stay bounded along infinitely many compiled outputs: at bounded
T-time there are finitely many original queries and finitely many frontier
holds to pull. Both arguments hold on EVERY compiled transcript, regardless of
the bit answers or success of the original martingale. Stored answers supply
all simulated history bits; no future source bit is consulted.

Hostile case: a compiled colour scan acquires multiple permanent holes. It reads
every coordinate read by T. A coordinate omitted by T eventually enters U_t
because n_t→∞. It is then pulled by every colour scan other than its own, and
permanent holds have distinct colours. Hence each colour scan has at most one
permanent omission. The fill scan pulls every omitted coordinate and is
exhaustive. By simulated time c(q+1), q has been read or pulled; the number of
compiled outputs is at most c(q+1)+n_{c(q+1)}+1≤2c(q+1)+h+1, allowing the
inclusive endpoint. Thus the fill scan has a computable inverse obtained by
waiting for the requested coordinates, is fair, and is an effective isomorphism.
E-ISO makes its output CR on a CR source.

Hostile case: a stake is computed only after seeing its betting bit. When a
fresh output is a copied bet, the original T-history ends BEFORE that bit is
appended. It is already reconstructed from earlier compiled outputs. The copied
rational stake is therefore a function of the compiled past alone. At pulls
the stake is zero; at zero original capital the fractional stake is defined
as zero. The resulting accounts are total nonnegative rational martingales.

On a winning original path all original capital factors are positive. At each
completed T-time each factor has been assigned once, either to the fill account
or to exactly one held-colour account; every inserted pull has factor one.
Therefore d_T=D_fill∏_{i≤h}D_i at those respective output prefixes. If all
accounts were bounded above their finite product would be bounded above.
D_fill is bounded by CR and E-ISO; so some D_i succeeds. No positive lower
bound on any account, synchronized output length, or monotone log growth is
needed. This proves OH⊆OH_h; the reverse inclusion follows from scan-family
containment. Every scan transcript is realizable by freely assigning its fresh
query coordinates. Its fibre has exactly 2^r members for r finite omissions,
and infinitely many if infinitely many are omitted. Thus for fixed k≥2 the
allowed omissions are ≤floor(log₂k), giving A: OH_h=OH=R_k^scan.

## 3. Potential coefficients and savings: independent algebra

For output cell w at time t put a_w=2^{|σ|−t}d(w)≥0. Let c_w be its
nonempty-intersection indicator with [σ], and s_w its indicator of meeting
BOTH child assignments at a fresh raw coordinate k. Then Ψ=Σa_wc_w and
γ=Σa_ws_w. The two child indicators are respectively (0,0), (1,0), (0,1)
or (1,1); in each case their sum is c_w+s_w. Child normalization multiplies
by two, so (Ψ_0+Ψ_1)/2=Ψ+γ exactly. This coefficient check rules out the
plausible but wrong cost γ/2.

Refined cells are subsets of their parents. Multiplying their indicators by
nonnegative child capital and using d(w0)+d(w1)=2d(w) gives time decrease.
Also [σ]∩G⁻¹[w] has measure at most λ(G⁻¹[w])=2^{-t}, with equality NOT
assumed. Consequently E[d(G(x)↾t)|[σ]]≤Ψ. Domination is a conditional
average inequality, not a pointwise capital bound.

Savings is necessary because finite cover witnesses may occur at different
times. In the wrapper, active capital A is multiplied by the original child
factor and unit amounts are then transferred to a nondecreasing bank B until
0≤A<2. Transfers preserve total capital; averaging the pre-transfer children
gives the martingale equation. At a node of original capital zero, A is already
zero (zero is absorbing), so the specified zero-denominator branch is legal.
For any later time, total capital is greater than its earlier value minus 2.
If total savings stays bounded, only finitely many integer bank transfers
occur. If the original path ever hits zero it is bounded already. Otherwise
active capital stays positive and, after the last transfer, equals a positive
constant times the original capital. Since it stays <2, the original is bounded.
This handles unbounded limsup, not only endpoint/liminf success.

## 4. Block candidates and the finite-stage headroom

Hostile case: arbitrary nonlinear or unbounded-size finite recodings cause
several raw splits despite just one virtual hole. A fully read virtual block
determines its entire raw block by the finite inverse table. A raw candidate
can split a cell only if its virtual block is incomplete. If all candidate
blocks lie below n and time is at least the scan frontier c(n), at most ONE
virtual coordinate below n is unread; hence at most ONE candidate block is
incomplete. With one raw candidate per block, Σ_k s_w(k)≤c_w cell by cell,
and summation gives Σ_kγ≤Ψ even after arbitrary previous raw fixes.

One candidate per block is indispensable. A bijection (a,b)↦(a xor b,b),
with its first virtual coordinate known and second unread, leaves BOTH raw
coordinates split. The bound for two candidates in this same block would fail.
No fixed block-size or contiguity hypothesis is allowed. For finitely many
active recodings, previously chosen candidates exclude finitely many finite
blocks. Their union is finite, so an infinite candidate class still supplies
N_i distinct increasing candidates. Choose n greater than EVERY coordinate
of every active candidate block, rather than just the candidates themselves.

At stage i a newly activated term contributes
2^{-i-2}P/(1+P)<2^{-i-2}. While Φ<2, a minimizing candidate costs <2/N_i.
Here N_i=2^{i+4}(2i+2), so all 2i+2 fixes together cost <2^{-i-3}.
The total new budget is <(3/8)2^{-i}. Starting headroom is 2^{1-i}; it is
strictly larger, so induction on the repetitions licenses Φ<2 throughout.
At the end Φ<2−(13/8)2^{-i}<2−2^{-i}. There is no circular assumption
that a completed stage alone implies the intermediate bound. For no active
indices, use maximum frontier 0 and zero empty sums. Stage 0 is covered.

## 5. Invalid guesses, true completion and the ordinary ML test

Hostile case: semantic validity is Π⁰₂ and cannot be decided by the test or
observer. Fix one deterministic partial interpreter for every finite guess.
Finite queries/stakes, finite block membership/lists and bijection tables are
requested as needed. Malformed types, repeated inspected query coordinates,
out-of-range stakes, invalid tables or contradictory inspected membership
are rejected. Nonhalting requested computations leave that run pending.
Finite cell intersection is a finite constraint problem on the fetched raw
blocks; it does not ask whether the full tuple is semantically valid.

The savings transform and rational finite potentials are computed from these
inspected values. For valid indices all requested data agree with the true
maps and all frontier/candidate searches halt. For invalid indices no potential
invariant is promised. Nevertheless EVERY emitted assignment is checked to
have binary values and exactly (i+1)(i+2) DISTINCT strictly increasing raw
coordinates. Reject before emission if this syntactic condition fails. This
final check is redundant for faithful execution but makes the access boundary
explicit. It does not reject or alter any true run.

There are exactly 2^{i+1} possible length-(i+1) guesses. Dovetail them and
enumerate the final assignment only when all its stages finish, at most once
per guess. Each assignment fixes (i+1)(i+2) independent source coordinates,
so has measure 2^{-(i+1)(i+2)} even for a semantically invalid completed run.
Its arbitrary-coordinate cylinder is effectively expanded into the finite
set of ordinary prefixes through its maximum coordinate. The resulting
ordinary uniformly c.e.-open source test satisfies

    λ(V_i)≤2^{i+1-(i+1)(i+2)}=2^{-(i+1)^2}≤2^{-i}.

Neither an exact measure algorithm, a completion deadline, a validity oracle,
nor an infinite union over unpriced holds is inserted into this test. The
true validity guess activates only valid programs, so each finite true run
finishes and extends its predecessor. The nested finite cylinders are nonempty
compact with positive finite measure; their intersection S is nonempty, may
be null, and lies in every V_i. Every element of S is nonMLR for this EFFECTIVE
reason. Validity's noncomputability does not certify nonMLR by itself.

## 6. B: compactness really protects one point against every pair

For each valid tuple e the activation weight w_e is positive and fixed once
and for all on the true run. Let X_t^e denote its savings capital on the raw
source after its block recoding and scan. Suppose no point of S bounds all
these capitals by L_e=2+2/w_e. The clopen sets {X_t^e>L_e}, over all valid
e and times t, form an open cover O of S. Compactness of the decreasing finite
cylinders implies some finite true cylinder is already contained in O: if
not, nested nonempty compact sets [σ_i] outside O would intersect S outside O.
A finite subcover of that cylinder uses finitely many e,t. Go to a later true
stage containing EVERY one of those valid e, and a time beyond EVERY witness
time and the stage time. Savings then gives weighted capital >2 at every
point of the later cylinder. The finite sum is clopen/finite-coordinate, so
its conditional mean is >2. Domination gives Φ>2, contradicting Φ<2.

Thus one point survives all valid pairs at once. The tuple family includes
every computable finite-block K, every legal one-hole T and every rational
martingale stake, including identity recoding and identity scan. It follows
that the SAME point is CR and every K-image belongs to OH. This is B. It is
not a family of separate witnesses z_e, and it protects only the indexed block-
recoded scan family, not all F₂. E-WTT and SRC-0071 are not used.

## 7. C: class separation and all-source tail-observer legality

Replace stage-i candidate pools by the computable disjoint infinite class
C_{ε↾(i+1)}. The preceding candidate proof still applies. For two guesses,
stages before the first disagreement execute identical deterministic
instructions, including all ties. After the disagreement, equal stage
lengths have unequal class names, and unequal lengths also have unequal
names. Therefore a completed false run and ANY finite true state assign the
same value to every coordinate they share. The statement covers true states
both shorter and longer than the false run; it is not just a same-level fact.

For v=D′(x), v_0=x_0 and v_i=x_i xor x_{i-1}. If [0,M) except q has been
read, put π_F=x_{q-1} xor XOR_{q<s≤F}v_s (x_{-1}=0). Telescoping gives
x_F=π_F xor v_q for every q≤F<M. The boundary F=q uses an empty XOR and
works too. This determines x below q and leaves the raw tail complementary.
D′ is a total fair computable bijection with computable prefix-XOR inverse.

T* tests only finitely many guessed runs, each for finitely many machine steps
at each output time. It uses only completed finite assignments, past virtual
bits and its read-set invariant [0,M) except q. A qualifying guess of length
m≥1 supplies r=q+2m+4 distinct fixes below M, consistent with the known raw
prefix, whose implied hold values agree. Resolving queries the UNREAD q and
then makes M the new hold; filling queries the UNREAD M. Either move increases
M by one. No program is awaited unboundedly, so each query and stake is total
on every transcript. On infinitely resolving transcripts q→∞ and every
coordinate is read. On finitely resolving transcripts every coordinate
except the final q is read. Freshness gives fairness, and the free omitted
coordinate gives exactly one or two preimages for EVERY transcript. Composition
with D′ preserves the cardinal count. Thus G=F_T*∘D′ is in F₂ globally.

Potential self-reference is harmless here: the standard tuple enumeration
may contain T* or computations mentioning it, but the observer's simulation
is bounded. Its totality/fibre proof does not assume those runs finish. Their
true finite termination is established only subsequently, using their already
proved validity. There is no validity oracle or circular waiting instruction.

## 8. The EVERY-state 1/8 bound and the common destroyed survivor

At a resolution the raw value at every selected F equals π_F xor v_q, while
the predicted value equals π_F xor ν. Hence a wrong ν forces ALL r selected
fixes opposite to the completed guess; if one agrees, all agree. For fixed
(q,ε), this adverse event is an r-coordinate cylinder B(q,ε).

Condition on ANY finite true cylinder. If any selected coordinate is already
fixed there, shared-fix agreement makes the adverse event impossible. If none
is fixed, all r are free under that cylinder and the relative measure is
2^{-r}. These two cases exhaust the possibilities. At length m there are at
most 2^m guesses, independent of semantic validity or completion. The union
bound therefore gives, at EVERY finite true state,

    relative λ(W) ≤ Σ_{q≥0,m≥1} 2^m 2^{-q-2m-4}
                  = (1/16)·2·1 = 1/8.

This is a relative bound, not merely the unconditional measure of W. No
independence between adverse events is needed. Infinite sums are sums of
nonnegative numbers; pending runs contribute nothing.

For x∈S at a held q, a true guess of length m supplies m(m+1) fixes, at
most q below q. Choose m²−m≥2q+4; then it has at least q+2m+4 fixes at
or above q. They agree with x. If the hold never resolved, filler frontier,
number of considered indices and simulation step budget all tend to infinity.
Eventually this completed finite true run and all its selected positions are
visible and qualify, contradiction. An earlier false qualifying run is allowed
and only resolves sooner. Thus EVERY point of S resolves every reached hold.

Now use L_e=2+4/w_e and let O be the union of valid capital exceedances. If
S⊂O∪W, nested compactness gives a finite true cylinder covered by finitely
many clopen capital witnesses and finitely many clopen pieces of W. Activate
all capital witnesses at a later stage and move beyond all their times.
Off the finite W-pieces the weighted savings capital is >4. The relative
measure of that region is at least 7/8. It is clopen and its finite-coordinate
capital has a minimum >4, so its conditional integral is strictly >7/2.
Domination forces Φ>7/2>2, contradicting the stage invariant. If there are
no capital witnesses, the 1/8 bound already rules out the purported cover.

Therefore ONE z lies in S outside both O and W. Its block-recoded capitals
are bounded, so z∈OH^blk⊆OH and z∈CR. It is nonMLR by the SAME test above.
Every T* hold resolves on D′(z), and none resolves incorrectly, so the total
rational output martingale doubles infinitely: G(z) is not CR. This is C and
R₂⊊OH. E-ISO additionally makes D′(z) CR and hence proves the stated
OH^iso⊊OH^blk consequence. Neither direct B nor the strictness construction
of C uses E-WTT or SRC-0071; E-ISO supports A and the CR recoding consequence.

## 9. Corrections, retained obligations and allocation

No mathematical erratum or quarantine is warranted. Explicit c(0)=0,
maximum-of-empty-frontiers 0, exclusion of empty observer guesses, canonical
deterministic runs and final syntactic emission checks clarify executable
boundary cases without changing any true run or theorem. Old records remain
historical and unmodified; this audit does not upgrade them to external review.

The remaining source task is original SRC-0067 journal proof access and actual
comparison with SRC-0068. The Cambridge original article/abstract route showed
abstract, metadata and an access link; Project Euclid full/PDF routes did not
return the paper; a Cambridge PDF route was inaccessible. Both search engines
were used to seek the original, without obtaining its full text. A search
snippet suggesting a PDF is not proof access. No source access was upgraded,
no contact made, and no theorem falsified by this access failure. See the
source-access dossier for exact URLs and journal-versus-thesis limitations.

Independent external/formal checking, S084 optional balanced-fibre boundary,
and any later novelty/significance/Gate-4 assessment remain separate review
obligations. S084 is not needed in A–C and has not been newly certified here.
The original Y/M/H/X, CAND-01, DEF-0020 and PA-0001 are unchanged. No EQ/SEP,
R₂ versus OH^iso, U(H), original X∈OH, fixed-S preservation or Conjecture R
result follows. Gate3 PASS; Gate4 NOT REVIEWED; Phase4 OPEN; Phase5 CLOSED.

S100's dossier-by-S103 condition is met and survives this audit. ZERO
speculative flagship sessions have been used through S103. With no fatal
repair pending, select its rank-2 fallback for the FUTURE S104: one bounded
source-dependent non-orientation dyadic-partition coverage gate, with explicit
all-source geometry and actual martingale-success obligation. Selection is
allocation, not evidence that such a bridge exists. S105 must apply the
five-session GO/NO-GO policy; no automatic sixth local refinement is warranted.
No S104 mathematics is executed here.
