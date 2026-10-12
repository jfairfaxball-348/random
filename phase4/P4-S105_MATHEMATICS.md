# P4-S105 — Ticket allocation, effective all-F₂ protection, and failed extraction

2026-10-12. ONE owner-invoked Phase-4 Mathematics session, selected CAND-01.
Entry main `a26d4476901d67db9abda823547c52cfd52693e7`, sole parent
`350d2e39d738eab0b21e41b65784b8263881af1d`, whose sole parent is
`8e57d9994ba21c219e3d94ffe31024d1ce175bac`. The amendment, rather than
S104's historical review-first handoff, controls this execution. The complete
authoritative incoming prompt is archived verbatim in P4-S105_INCOMING_HANDOFF.md.

**Result: EQ and SEP remain UNRESOLVED after three developed architectures and
dependent repairs.** A finite ticket-allocation theorem is proved, including
its global fair injective extension and exact obstruction from occupied cells.
A certificate-stream construction supplies an EFFECTIVE integrable savings
bank protecting every F₂ observer without an oracle for validity. This repairs
one technical weakness of the analytic SEP route, but neither constructs a
nonMLR protected point nor covers every R₂ point by a finite bank sublevel.
Cost selection and the nonMLR certificate remain unresolved. Aggregate bank
divergence does not, on its own, extract one succeeding observer.

**Five-session decision: NO-GO for AUTOMATIC flagship refinements.** Neither
central alternative nor a strictly smaller proved central bridge with source
accounting closed has emerged. This is not a mathematical impossibility result
for future EQ/SEP work. No S106 is executed or automatically scheduled.

## 1. Finishing statements, proof inputs and quantifier discipline

F₂ comprises ALL everywhere-total computable maps G:2^ω→2^ω with
G_*λ=λ and |G⁻¹{y}|≤2 for EVERY y. d is a total computable nonnegative
rational binary martingale; success means sup_t d(G(z)↾t)=∞.

EQ: ∀z∈CR∖MLR ∃G∈F₂ ∃d succeeding on G(z).
SEP: ∃z∉MLR ∀G∈F₂ ∀d, sup_t d(G(z)↾t)<∞.
Identity belongs to F₂, so SEP entails CR of the SAME z. Finite source-dependent
algorithm indices are permitted in EQ; an oracle for z is not.

Inputs: S003/S007/S085 effective clopen cells and searchable global width;
S082/S101 savings and bounded-bank implications; S095 closed cheap selection
as an EXISTENCE theorem; S098 closed-null and S099 Schnorr/cost boundaries;
S104 the computable gain-deadline prohibition and representation padding.
S101–S103 A–C and their source distinctions are frozen. No new external theorem,
source access, novelty claim or formal proof certification is used below.

The three architectures are: I, non-orientation ticket rebalancing for EQ;
II, effective certified savings plus priced closed forcing for SEP;
III, extraction of one legal observer from an aggregate ML-detecting bank.
They are developed below, not treated as a list of possible projects.

## 2. Architecture I: recursively allocate test tickets to profitable cells

Fix an arbitrary ordinary ML test (U_n) and arbitrary z∈CR∩⋂U_n. At a
current output depth r suppose the already emitted observation is a computable
clopen partition (P_w:|w|=r), with λP_w=2⁻ʳ, and the already specified
martingale values d(w)=c_w. Try to place a newly certified clopen test ticket
A (for example a finite stage of U_n) inside future high-capital leaves.
Earlier output bits and stakes cannot be revised when A is discovered.

### Theorem I.1: exact conditional price, and a finite globally legal completion

Let H>max_w c_w be rational. If A is to be wholly covered by a future
capital crossing ≥H of a fair refinement of this partition and extension
of this martingale, NECESSARILY, for each w,

    λ(A∩P_w) ≤ (c_w/H) λ(P_w).                         (1)

Conversely, for a computable clopen A satisfying (1), there is an effective
finite refinement and a total computable fair HOMEOMORPHISM G extending all
already specified cells through r, with a total rational martingale D extending
all already specified values through r, such that D reaches H on G(A).
D is frozen after a finite depth. Hence the full-map every-fibre condition is
closed for this FINITE theorem (each fibre is actually a singleton).

Proof of necessity. Conditional on P_w, future output bits of ANY fair
refinement have fair distribution: λ(P_{wv}|P_w)=2⁻|v|. For each finite future
horizon, the nonnegative martingale maximal inequality gives a crossing mass
at most c_w/H. Taking the increasing union over horizons proves (1), without
a computable crossing deadline. The statement prices ALL of A in that cell,
not merely one chosen x. If c_w=0, the entire future martingale is zero there.

Proof of sufficiency. Put p_w=λ(A∩P_w)/λP_w. These are exact computable dyadic
rationals. Choose s with p_w=k_w/2ˢ for all w. Since H>c_w and (1) holds,
p_w<1. Assign H to k_w of the depth-s descendants of w, and assign

    R_w=(c_w-H p_w)/(1-p_w) ≥0

to the remaining descendants. Average backwards to define all intermediate
values; their average at w is exactly c_w. Label the chosen descendants so
their source cells partition A∩P_w; the remaining cells partition P_w∖A.
Such equal-mass clopen partitions are computable. Explicitly choose raw depth
L≥r+s at which every P_w and A is a union of raw L-cylinders. Each output
leaf must contain exactly 2^(L-r-s) raw cylinders, and the prescribed counts
are integers. Group them lexicographically, separately inside A and outside.
Assign distinct L-bit output names extending that leaf to its raw cylinders;
there are exactly enough names. This makes a permutation of ALL length-L
raw strings onto ALL length-L output strings. Append the unchanged raw tail.
The resulting map and inverse are computable, fair, onto and injective on
EVERY point. Freeze D after r+s. The earlier parent equations are preserved.
If A is empty all k_w are zero; the construction still works. ∎

This is a genuine finite all-source allocation theorem, not a theorem about
ML-test membership implying eventual infinite gain. The algorithm uses the
finite clopen ticket as ordinary data, not z. Infinite width-two construction
and source-to-output unbounded gain remain separate obligations.

### First attempted finish and exact counterexample

The tempting assertion was: sufficiently small GLOBAL λA always permits a
profitable reassignment, regardless of previous output. It is false even for
one ticket. Let d≡1 through depth r, choose a current cell A=P_w, and take
H=2. For arbitrarily large r this ticket has arbitrarily small absolute mass
2⁻ʳ, but its conditional mass in P_w is one, violating (1) by a factor two.
No future fair continuation can make EVERY point of A reach H. This is not
an EQ counterexample: a point of A might instead be caught by another observer.
It disproves only the claimed automatic full-ticket allocation step.

### Repair I.a: deeper test levels before committing cells

At a FIXED depth r and target H, sufficiently deep U_n has absolute measure
small enough to make every conditional ticket mass small, provided c_w has
a strictly positive known floor. One can also start with a positive floor by
adding constant capital. This observation is finite and useful, but it does
not give a completing algorithm along arbitrary z. To wait for evidence that
z enters the chosen level while withholding output would make the map partial
on inputs outside that open set. To keep emitting output while waiting lets
r and the cell concentration change before the ticket arrives. No fair
continuation can alter already emitted cells. S104 excludes imposing a
computable source-entry or high-gain deadline; padding excludes triggers that
depend on a cylinder's syntactic length instead of its actual set.

The missing recursive theorem would need to pay all successive tickets,
give global searchable width≤2 at EVERY precision, AND make one D unbounded
on the same arbitrary z. The finite theorem has not proved that statement.

### Repair I.b: leave one binary reserve and use several transverse channels

Replacing each injective finite completion by an endlessly renewed binary
reserve could in principle evade isomorphism preservation. But independently
retaining two unresolved raw binary choices gives four possible preimages on
a continuation where both survive. For literal no-repeat scans this follows
exactly from the fibre assignment formula in S101 §2.3. For general partitions
the relevant global condition is S085's all-cell width test, not a count of
named reserve variables. At raw precision n an infinite path through cells
meeting three distinct n-prefixes already gives three actual inverse points.

Thus a purported reserve controller must discharge the preceding ambiguity
on ALL affected sibling continuations before accumulating another independent
one, or prove the choices correlated. Merely target-only resolution does not
close legality. Discharging it by outputting its determining source data can
pre-reveal the wager which was to provide gain, the S003/S007 freshness issue.
No new controller with both full legality and repeatable all-source gain was
obtained. An injective infinite completion would preserve CR by E-ISO and
cannot supply EQ. These are precise failures of the attempted compiler, not
a theorem that all non-orientation observers are impossible.

Several channels do not inherit the one-channel price as a sufficiency
theorem. S104's F and F∘K have incompatible kernels and no prohibited common
CR-preserving output factor, but this alone says nothing about profitable
placement of a given source's tickets in at least one channel. The two inverse
partners can both be nonMLR. A favourable test-entry race is not available
from these hypotheses. Fractional betting, savings and restarts cannot replace
the missing actual gain; on a surviving infinitely resolving scan, S084
controls the ENTIRE predictable error stream. No finite channel family with
proved coverage of every CR∖MLR z emerged.

**Architecture I disposition:** finite feasibility and exact prices PROVED;
absolute-smallness repair REFUTED; rate-free recursive full coverage UNPROVED.
Neither EQ nor a narrowed central bridge is supplied.

## 3. Architecture II: effective protection without a valid-index oracle

S096's selected bank was an abstract sum over valid indices. A different bank
can be constructed effectively by checking finite certificates and suspending
bad programs. This does not change S096's historical function or evidence.

### Theorem II.1: an effective integrable all-F₂ protection bank

There exists an effectively lower-semicomputable nonnegative function b with
∫b dλ≤1 such that

    b(x)<∞ ⇒ ∀G∈F₂ ∀d⁰, sup_t d⁰(G(x)↾t)<∞.          (2)

More explicitly: for each valid normalized pair (G,d⁰), some positive rational
weight a_e is assigned to a certificate program e, and its S082 saved bank B
satisfies a_e B(G(x)↾t)≤b(x) for EVERY x,t. This includes all non-scan maps,
all frames, every fractional output strategy and exceptional fibres. No
semantic membership test for F₂ or total martingales is used.

Construction. Enumerate all ordinary programs purporting to emit successive
finite transactions. A transaction supplies a complete clopen dyadic source
partition through output depth m_j, a normalized nonnegative rational
martingale table through m_j, and the width certificate

    every depth-m_j cell meets at most two raw j-prefixes.

Require m_j≥j and strictly growing depths (apart from initial empty depth).
Check exact partition, disjoint children, masses 2⁻|w|, rational martingale
child equations and agreement with ALL previously accepted data. Finite
prefix codes allow every check to be decided. Reject malformed or incompatible
transactions permanently; an unfinished transaction merely waits. Accept
one transaction at a time in the program's order. Rejecting may not erase
earlier savings. The initial table is root capital one and bank zero.

On acceptance at depth m_j compute the S082 savings wrapper over the entire
accepted finite tree. Define b_{e,j}(x)=B_e(w) for the unique accepted leaf
w whose source cell contains x. This is a nonnegative rational clopen simple
function. Successive functions increase pointwise because bank transfers
never decrease, and consistent partition refinements retain the actual past.
Exact fairness gives ∫b_{e,j}=2⁻m_j Σ_w B_e(w)≤1. Let b_e be their supremum,
including zero before any acceptance. Then b_e is effectively lsc and
∫b_e≤1 by monotone convergence, whether the program is valid, stalls or rejects.
Choose a_e=2⁻e⁻¹ for all e≥0 and put b=Σ_e a_e b_e. Increasing finite
stage sums give an effective lsc presentation. Tonelli gives ∫b≤1.

Coverage and global legality. Given actual (G,d⁰), effective compactness
computes its clopen partitions; S003/S085 searches the width certificate at
each raw j; totality computes the complete finite martingale tables. A
certificate program doing these searches exists and passes EVERY transaction.
Its depths tend to infinity, so its b_e is exactly the pulled-back bank of
this pair. Conversely, any program accepting unboundedly many transactions
defines a total computable map: wait for the next accepted table containing
the requested output depth, then decide its finite clopen cell. Fairness
holds at every finite depth. The certified width at each j gives the global
cardinality cap via compactness, exactly as S085. Its infinite table defines
a total rational martingale. No index deciding WHICH programs progress is
needed. A stalled/rejected program has only finitely many accepted tables,
so its b_e is a globally bounded finite clopen function; it does not become
an illegal winning observer. All of these are ordinary algorithmic searches.

If b(x)=C<∞, the saved total capital of each covered pair is <2+C/a_e
at every time, since its active part is <2. S082's savings implication then
bounds its ORIGINAL d⁰ on G(x). Normalize any positive initial capital by
its computable rational root; zero-root martingales are identically zero.
This proves (2), including CR via the identity. ∎

Important limitations: (2) is ONE-WAY. Even when each b_e(x) is finite, their
weighted sum can be infinite. No claim b(x)<∞ ⇔ x∈R₂ is made. b is an
effective lsc source function, not one computable source martingale. It need
not have computable integral, pointwise convergence rate or computable finite
bank cutoff. Its construction does not put a gain deadline on any CR source.

### Corollary II.2: certified closed protected states, and the proposed SEP finish

For rational C>1, P_C={x:b(x)≤C} is effectively closed, lies inside R₂,
and has λP_C≥1-1/C by Markov's inequality. The known lower mass at this
INITIAL state is real information; it is not a positivity oracle for arbitrary
subconditions. The set {b=∞} is ML-null: the open sets {b>2^(n+1)} have
measure ≤2⁻n⁻¹. Thus every MLR point has finite b.

A sufficient finish would be an ordinary uniformly c.e. ML test (V_n),
and one C with P_C∩⋂V_n nonempty. Any point of this intersection would be
ONE nonMLR all-F₂ protected source. This is a sufficient target only; it is
not an exact reformulation of SEP, since R₂ may contain points with infinite
b. No strict reduction credit is assigned merely for renaming that existence
problem as an intersection.

### Repair II.a: finite-stage cost certificates still fail

Try S095's positive Π⁰₁ wrong-or-diverge choices with f=1+b. It is now
effectively lsc and integrable, so the analytic selection theorem applies
without a validity oracle for f. Its arbitrarily high good h,s STILL have
no computably supplied lower-mass or upper-conditional-cost certificate.
Effective lsc makes finite-stage underestimates available; it does not verify
an upper bound on the eventual average in a selected closed state.

This cost problem persists even on a KNOWN positive clopen state, and with
identity as the only map. Let D be the finite identity martingale which bets
all capital on zero at each of the first two bits and then stops. Its S082
bank B has B(00)=2, B(01)=1 and B(1)=0, constant afterwards, with ∫B=3/4.
For ordinary program e put b^(e)(x)=B(x) if e eventually halts, and zero
otherwise. This is uniformly effectively lsc with integral≤3/4. On fixed
P=[00], avg_P b^(e) is 2 or 0 respectively. A sound AND complete c.e.
certifier of avg_P b^(e)<1 would enumerate precisely the nonhalting indices.
Impossible. The bank is implementable by a certificate program waiting for
e's halt before accepting the fixed finite table; no invalid map or positivity
uncertainty is involved. This refutes a general effective upper-cost test,
not a specially designed construction with additional certificates.

### Repair II.b: search inside the protected sublevel instead

The initial positive lower bound for P_C bypasses one arbitrary-positivity
problem. It does not show that this closed class contains a nonMLR point.
If one chooses a uniformly effective nested closed null chain inside it, its
intersection is Π⁰₁ null and cannot contain a CR point (S098). If one searches
all high holds, even the constant reader's wrong states union to measure one
(S096). If one emits a finite delayed guessed family, EVERY emitted source
state needs its numerical upper mass, the number of completions needs a paid
bound, and a continuing true run needs proof; S097–S099 supply none for this
new b. Positive P_C and noncomputably delayed emissions do not close these.

There is also an exact countermodel to the stronger blanket assertion
“any effective integrable protection bank has a nonMLR finite point.”
Fix a universal ordinary ML test (W_n) with λW_n≤2⁻n⁻², and define

    g(x)=Σ_{n≥0} 1_{W_n}(x).

It is effectively lsc, has ∫g≤1/2, and is infinite on EVERY nonMLR point.
All MLR points have finite g by the same integral-test/Markov argument.
Then b'=b+g remains effectively lsc and integrable (∫b'≤3/2), and still
dominates EVERY bank protected in II.1 with the same weights. Nevertheless
EVERY finite sublevel of b' contains ONLY MLR points. For C>3/2 such a
sublevel even has the certified positive measure ≥1-3/(2C).

This is a countermodel to inference from effectivity, integrability,
all-map domination and positive mass ALONE. It does NOT show that the
SPECIFIC b of II.1 lacks a nonMLR finite point. That is unresolved. It explains
why II.1 is a technical repair, not a completed SEP bridge satisfying S100.

**Architecture II disposition:** effective all-map domination, correct invalid
program handling and positive closed protected states PROVED. NonMLR membership
of the same protected point UNPROVED; a general upper-cost certification rule
REFUTED. No SEP and no coverage theorem for all R₂ sources.

## 4. Architecture III: can an ML-detecting aggregate extract one F₂ destroyer?

Attempt to connect the two fronts: arrange that an effective bank dominates
a universal ML integral test, then use its divergence to select one F₂
component, or compile its infinitely many profitable finite components into
one legal observer. This would avoid orienting a test partner directly.

The exact problem is the distinction between

    Σ_e a_e b_e(z)=∞

and

    ∃e [b_e(z)=∞ and e accepts unboundedly many transactions].

Only the second furnishes one actual observer and succeeding original
martingale. Even if every progressing component is globally F₂, the first
does not imply the second.

### Counterexample III.1: aggregate divergence from wholly finite legal accounts

For each i≥0 set L_i=2^(i+1). In the IDENTITY observation, let D_i bet all
capital on zero for the first L_i bits, then stop forever. D_i is total rational,
globally bounded by 2^L_i, and succeeds on NO sequence. The S082 savings bank
B_i has B_i(0^ω)=L_i: each correct zero doubles active 1 to 2 and transfers
exactly one unit, restoring active 1. It is globally bounded by L_i and
∫B_i≤1. With a_i=2⁻i⁻¹, the effective bank

    h(x)=Σ_i a_i B_i(x)

has ∫h≤1 but h(0^ω)=Σ_i 1=∞. Every component is a legitimate finite account
on a globally fair injective map, yet none succeeds. ∎

The example source is computable and is NOT a CR∖MLR counterexample to EQ.
Its precise role is to refute the proposed purely analytic component-extraction
lemma, even when all components are legal and all widths are one. A stronger
extraction lemma restricted to CR∖MLR would need extra source information;
none has been proved here. Domination by a universal ML function alone gives
no such extraction. Adding g in II.b would actually insert non-component
divergence, so is an especially invalid EQ shortcut.

### Repair III.a: select the component on the source as it becomes large

One can effectively observe finite bank values on a source using the accepted
clopen tables. Choosing a new observer after detecting a large source bank
does not retrospectively make that gain output-visible to a martingale in
an already committed observer. Concatenating independent observations can
reveal repeated source bits and lose conditional fairness; multiplying fibre
bounds through composition can exceed two. Inserting fair fillers reintroduces
the source-presentation and pre-revelation problem of Architecture I. A late
selected program index is not an output capital transfer. No valid compiler
preserving all finite-source prices, global width and unbounded gain was found.

### Repair III.b: finite advice and inverse tracks

S007's two true tracks on a DOUBLE fibre are useful after a genuinely separating
finite prefix is specified. They do not supply a uniform computable branch
selector on arbitrary outputs, conditional masses or a source-dependent
success compiler. On SINGLETON fibres there can still be outward-moving
phantoms without a computable last-injury time. S083's destructive witness
already has singleton fibre, with balanced double fibres almost everywhere
by S084. Thus neither discarding singleton outputs as null nor assuming
a.e. balanced inverse weights can prove CR preservation or EQ. The new
certificate enumeration verifies whole width trees, not individual sheets.

S086 also prohibits selecting ONE universal observation with arbitrary
rebetting or harmless output recodings. III.a would need genuinely different
source partitions and an actual same-source capital argument; it is not
licensed by that known representation. Architecture III closes no extraction
or common-survivor implication and proves neither flagship alternative.

## 5. Adversarial finishing audit and decision

Every claimed map in I.1 is globally legal by a finite prefix permutation,
but its gain is finite. Every progressing observer in II.1 is globally legal
by complete exact finite tables plus ALL-precision width certificates, and
all valid pairs have such presentations; however b-finite points might all
be MLR. Invalid prefixes are charged by root-one fair expectation, not by
semantic guesses. All-finite banks are not silently promoted to one winning
martingale. No output/source clock or source oracle is introduced.

What is still missing for EQ: a recursive source-sensitive legal family with
actual unbounded capital on every arbitrary CR∖MLR source, or an extraction
compiler with those exact quantifiers. What is still missing for SEP: an
ordinary ML test containing ONE point with all-map protection, with priced
emissions, positive continuing true states and honest eventual cost bounds.
Neither is narrowed to a proved falsifiable bridge satisfying all source-price
obligations. The finite allocation result, effective bank and countermodels
each improve diagnosis, but no claimed GO follows from diagnosis.

The S101–S105 decision is therefore **NO-GO for automatic flagship search**.
Recommend a separately owner-chosen independent check of the established
A–C theorem dossier, with II.1 independently checked as a secondary technical
result if desired. Preserve EQ/SEP as unresolved questions. Do not issue a
sixth automatic local refinement, novelty audit, manuscript or Gate4 review.
The exact five-session ledger is P4-S105_DEPENDENCIES_AND_DECISION.md.

Original Y/M/H/X, CAND-01, DEF-0020 and PA-0001 unchanged. SRC-0067 remains
ABSTRACT_INSPECTED; SRC-0068 primary thesis PROOF_INSPECTED, without original
journal/thesis proof correspondence. No claim on U(H), original X∈OH,
fixed-S, R₂ versus OH^iso or Conjecture R. Gate3 PASS; Gate4 NOT REVIEWED;
Phase4 OPEN; Phase5 CLOSED. This is internal written mathematics plus limited
finite sanity checks, not independent/referee, Lean, Palomar or hosted CI.
