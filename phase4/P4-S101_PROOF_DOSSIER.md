# P4-S101 — Internal proof dossier: bounded holes, block survival and tail separation

2026-10-12. Phase 4 Mathematics, CAND-01. Incoming main is
`1a5be73a7f54731d9be6dcb8db00b06a30217394`, whose sole parent is
`a6324a26434d1b73bacd9708495e8b44a318bbee`. This dossier reconstructs
S001/S011 and the selected S081–S083 package. It is not a manuscript,
external review, novelty audit, formal verification or Gate-4 review.

**Outcome: the selected package closes under the explicitly declared literature
assumptions below. No unresolved programme-mathematical premise remains in A–C.**

* A: for each fixed finite h≥1 and k≥2, OH_h=OH=R_k^scan.
* B: there exists z∉MLR with K(z)∈OH for every computable finite-block recoding K.
* C: there exists ONE such z and a total computable fair map G with
  |G⁻¹(y)|≤2 for EVERY y, such that G(z)∉CR. Thus R₂⊊OH.

The proof of C below also proves B; it does not identify this z with the original
Y or X. EQ R₂=MLR and SEP ∃z∈R₂∖MLR remain unresolved. The complete minimal
claim matrix is `P4-S101_CLAIM_DEPENDENCIES.md`; external checking obligations
are `P4-S101_REVIEW_OBLIGATIONS.md`.

## 1. Definitions and trust boundary

Cantor space is 2^ω, with fair product measure λ. For a finite assignment
σ:D→{0,1}, D⊂ℕ finite, [σ] is its cylinder and λ[σ]=2^{−|D|}.
Ordinary prefix cylinders are a special case. A rational martingale d is total
computable, nonnegative, and satisfies d(u0)+d(u1)=2d(u). Success means
sup_t d(y↾t)=∞, not a computable rate or convergence to infinity. CR means no
such martingale succeeds. MLR means avoidance of every ordinary uniformly
c.e.-open test (V_i) with λ(V_i)≤2^{−i}.

Rational martingales suffice also if CR is defined with computable real-valued
martingales. Here is the needed reduction. Replace a real martingale d by d+1
and normalize its root. Its child factors f_b are strictly positive computable
reals with average 1. At a node of length t choose a rational stake in [−1,1]
approximating its real stake closely enough that each rational child factor
is at least (1−2^{−t−2})f_b. Positive computable lower bounds for min_b f_b
are searchable, so the choice is computable at every node. The product of
these lower retention factors is positive. The resulting rational martingale
therefore succeeds wherever d does. Zero initial capital can never succeed.

A total computable map means an oracle machine producing every finite output
prefix on EVERY source; no a.e.-total replacement is allowed. Fair means
λ(G⁻¹[u])=2^{−|u|}. F_k consists of these maps with cardinal fibre bound
|G⁻¹(y)|≤k on EVERY output y. Define R_k={z∈CR:∀G∈F_k, G(z)∈CR}.
Cardinality, conditional sheet weight and a.e. fibre conditions are different.

A scan T is a total computable next-query function on finite transcripts u,
whose successive source queries q_s=T(u↾s) never repeat along ANY transcript.
F_T(z)_s=z(q_s), with q_s determined by its previous output bits. An h-hole
scan leaves at most h coordinates unread on EVERY infinite transcript.
OH_h={z∈CR:∀h-hole T, F_T(z)∈CR}; OH=OH_1. R_k^scan uses only scans in F_k.
These are semantic universal hypotheses; their valid indices are not assumed
computably enumerable.

A computable finite-block recoding K is presented by total programs for a
partition (B_j) of ℕ into nonempty finite blocks, a block-index function β,
finite block lists, and bijection tables κ_j on {0,1}^{B_j}. They must agree:
β(n)=j iff n∈B_j. Blocks need not be consecutive or uniformly bounded in size.
K(z)↾B_j=κ_j(z↾B_j). Table inversion gives a computable inverse. Independence
of disjoint blocks and bijectivity give fairness. Write
OH^blk={z:∀such K, K(z)∈OH}. The identity is included.

A computable fair homeomorphism is a total computable fair bijection of
Cantor space with continuous inverse; §2 makes its inverse computable.
OH^iso uses all these recodings. For reference, R₂⊆OH^iso⊆OH^blk⊆OH:
precomposition of an F₂ map by such a bijection preserves its cardinal bound,
and identity recoding gives the last inclusion. No equality of these classes
is assumed.

Uniform oracle conventions, if used, mean totality and scan/martingale legality
on EVERY oracle and EVERY transcript, with one uniform program. Target-only
halting is not that convention. The A–C construction is unrelativized: the true
validity sequence is used only in the existence proof, never as an oracle for
T*, an emitted ML test, or a computable map. The S081 uniform relativized
van-Lambalgen theorem is outside this dossier's dependency chain.

Two literature assumptions are declared, not newly proof-certified here:

| Input | Exact statement used | Recorded access |
|---|---|---|
| E-ISO: SRC-0015 / THM-0038, Rute Lemma 8 | Computable randomness is invariant under a.e.-computable measure-preserving inverse pairs for computable Cantor measures, with inverse identities on their full-measure domains | STATEMENT_INSPECTED |
| E-WTT: SRC-0067 / SRC-0068 / THM-0076 | There exists a CR Y with a target-total wtt autoreduction; input j is computed without querying j; siblings may diverge | SRC-0067 ABSTRACT_INSPECTED; SRC-0068 STATEMENT_INSPECTED, thesis Theorem 6.9 and reduction definitions |

E-ISO is the only literature premise of A–C. E-WTT is used only for the exact
k=2 nonconservation foundation and OH⊊CR. Elementary finite-product measure,
Cantor compactness/König's lemma and the martingale equation are proved or used
explicitly below. MLR conservation here follows by pulling back a c.e. test
through a total fair computable map, so it requires no new source assertion.
SRC-0069 is method provenance (STATEMENT_INSPECTED with recorded partial proof
reading), not an unproved lemma imported into this construction. SRC-0071's
preprint/journal distinction, R_tot=MLR and sources SRC-0019/0070/0072 are
outside A–C. No access level changes in S101.

## 2. Effective geometry and the exact foundations

### 2.1 Clopen preimages, surjectivity and bounded inverse lists

For a total computable F and requested output length m, search a finite
input-use u and computation stage s at which EVERY length-u answer string
produces m output bits without querying ≥u. Compactness of Cantor space and
totality make this search halt. Checking a proposed (u,s) is finite. Thus
F⁻¹[w] is an effectively computable finite union of length-u cylinders.
Its intersection with any finite assignment is decidably empty or nonempty,
and its fair measure is an exact rational. Uniformity is conditional on a
valid total index; the search may hang on an invalid index.

Fairness forces onto-ness: a continuous map has compact closed range, and an
omitted point would have a positive-measure output cylinder with empty
preimage. For a fixed source precision n, let C_{n,m}(y) be the n-prefixes
meeting F⁻¹[y↾m]. If all fibres have cardinality ≤k, some m works uniformly
over ALL output m-prefixes with |C_{n,m}|≤k. Otherwise the prefix-closed tree
of output prefixes meeting at least k+1 n-cylinders has an infinite path y.
The decreasing finite candidate sets on that path retain k+1 n-prefixes;
for each, nested nonempty compact preimages yield a point mapping to y.
This contradicts the ALL-output bound. The finite clopen test searches m.
For k=2, monotone resampling c(n)≥n gives a coherent width-two prefix tree
with path set exactly F⁻¹(y): true preimages are paths, and a path x is
verified by approximating x with compatible inputs at each larger precision
and using continuity. No selector, sheet probability or final injury time
follows from this list bound (S003/S007).

### 2.2 k=1 preservation

At k=1, F is injective and onto. The finitely many compact sets F([σ]),
|σ|=n, are disjoint. Using forward uses, compute their attained output
m-prefixes and search m at which the finite lists are disjoint. Compact
separation guarantees termination. The unique list containing y↾m determines
F⁻¹(y)↾n. Thus the inverse is total computable. For Borel A,
λ(F(A))=λ(A), by applying fairness to F(A). Hence the inverse is fair too.
E-ISO now applies with inverse identities EVERYWHERE. Therefore R₁=CR.
The inverse modulus depends on F; coordinate permutations preclude a single
class-wide use bound (S001).

### 2.3 Exact scan cylinder and fibre geometry

For a finite transcript w of length t, simulate T along w. Its t queries
are distinct and
F_T⁻¹[w]={z:z(q_s)=w_s for s<t}. This is a cylinder fixing t independent
bits, of measure 2^{−t}; T is fair. For an infinite transcript y this
assignment extends on its queried set Q(y), with arbitrary choices elsewhere.
Every choice induces the same transcript, by induction on output time.
The fibre therefore has size 2^{h(y)} if h(y)=|ℕ\Q(y)| is finite, and is
uncountable otherwise. Consequently T∈F_k iff h(y)≤⌊log₂k⌋ for EVERY y.
Every infinite transcript is realizable; there is no hidden reachable-only
weakening here (S008/S032 Lemma 8).

For later comparison, if a one-hole T permanently omits a fixed j, prequery j,
ignore its value, and simulate T. If T asks for j, switch to increasing fresh
fillers; otherwise it reads every coordinate except j. This completion is
exhaustive on EVERY transcript, induces a fair computable bijection, and has
computable inverse by waiting for each requested coordinate. Copy d's bets
while T avoids j and freeze at consumption. E-ISO implies that a CR source
destroyed by T must have singleton fibre and query every coordinate (S008).
This is not a theorem that all singleton inverses preserve CR.

### 2.4 k=2 nonconservation under E-WTT

Keep the originally fixed CR Y and its syntactically self-avoiding, globally
use-clipped M: on input j abort attempts to query j or exceed its strict
computable use cap; on Y the clipping changes nothing (S027). At each epoch
hold the least fresh j. With an increasing finite simulation budget, test
whether M(j) has a binary halt using only already read coordinates. If yes,
query j and bet all capital on its visible value. If not, read the least
fresh coordinate other than j with zero stake. Abort/nonbinary siblings keep
filling forever. The finite bounded test makes the scan total on EVERY
transcript, regardless of M's partiality. Queries are always fresh, so §2.3
gives fairness. A final nontrigger epoch reads all but j (two preimages);
infinitely many completed epochs consume increasing least-fresh sentinels
and exhaust ℕ (one preimage). The fibre bound holds at EVERY output.

On Y every M^Y(j) halts correctly using finitely many non-j coordinates.
Fillers eventually expose them and the simulation budget eventually suffices,
so every epoch resolves correctly. The total rational output martingale
has capital 2^r after r resolutions. Thus R₂⊊CR and OH⊊CR under E-WTT.
The wtt use cap is not needed for the conversion; target-visible
self-avoiding partial computations suffice (S012). It is not sibling totality.
An all-continuation unavoidable sentinel has a searchable finite avoidance
bar by compactness (S009), but target-only halting supplies no such bar.
S010's capped optional projection does not provide a computable substitute.
Those two boundaries are not additional premises of A–C.

### 2.5 Null ambiguity: domain check, not an A–C premise

This records explicitly S100's completion of S032 Theorem 3. If a total fair
F has λ{y:|F⁻¹(y)|≥2}=0, search at precision n for m such that F⁻¹[y↾m]
lies inside one n-cylinder. It halts for all n exactly on singleton outputs.
For fixed n, the success locus D_n is effectively open; all D_n have measure
one under the null-ambiguity hypothesis. The inverse domain is ⋂D_n.
Its complement is a countable union of effectively closed null classes.
CR points avoid each such class P: approximate P by decreasing computable
clopen supersets and search U_i⊃P with λ(U_i)≤2^{−2i−2}. If a U_i is empty,
P is empty. Otherwise ν=∑_{i≥0}2^{−i−1}λ(·|U_i) is a computable probability
measure: its finite rational sums have uniform tail bound 2^{−i−1}.
The computable real martingale ν[u]/λ[u] has value at least
2^{−i−1}/λ(U_i)≥2^{i+1} once a prefix of x∈P is contained in U_i.
It succeeds on every x∈P; §1 turns it into a rational martingale.
This is the elementary CR⇒Kurtz implication, with the domain consequence
now justified without an additional source premise.
The source domain ⋂F⁻¹(D_n) has the same property and contains EVERY CR input.
On these domains F and its partial inverse are inverse and fair: for a
source cylinder [σ], pull back its inverse image and remove only a null set.
E-ISO thus proves forward preservation on all CR inputs, without assuming
the output is already CR. This avoids circular use of an unspecified generic
domain. Null ambiguity and a.e. balanced double ambiguity are different.

## 3. Reconstruction of A: bounded-hole collapse

Fix a finite h≥1 and an h-hole scan T. For each n, the tree of transcripts
leaving more than h coordinates below n unread is prefix closed. If it has
arbitrary height, an infinite path leaves a decreasing finite family of
unread-below-n sets all of size >h; its limit has >h permanent omissions.
Contradiction. Search the least c(n) at which every transcript has ≤h such
unread coordinates. Total T allows finite simulation of every transcript at
each trial, so c is computable and nondecreasing. Also c(n)≥n−h.

Set n_t=max{n:c(n)≤t}. This maximum is computable and finite because
c(n)≥n−h; n_t≤t+h and n_t→∞. Let U_t be the unqueried coordinates below
n_t before T's step t. Every transcript satisfies |U_t|≤h. A coordinate read
before entering U is fill; otherwise it enters U at e_q and stays until its
read step r_q (possibly forever). Its held interval includes its read step,
so no new colour is freed until that read has actually been processed.

Colour entrants at each step in increasing order, taking the least unused
colour among 1,…,h. At most h intervals are active, so this always succeeds.
Colours are permanent. Same-coloured held intervals do not overlap, and
permanent omissions of one transcript have distinct colours.

For colour i define a new scan S_i. From its own transcript reconstruct the
simulated T-time τ, T-history, colours and its finite read set R with values.
Before processing T's next query, pull the least unread member of U_τ of
colour ≠i with stake zero. Once none remains, process q_τ: if it was pulled
earlier, append its stored value to T's simulated history and advance τ
without another output; otherwise read q_τ and advance. On an in-step held
query of colour i copy d's fractional stake computed from T-history; on a
fill query stake zero. Other-coloured held queries have already been pulled.
The fill scan F pulls ALL members of U_τ and copies d's stakes only on fill
queries. Each simulation updates U and colours at the relevant T-time.

**Totality and own-history reconstruction.** Pulls and in-step reads supply
every answer later appended to T-history, so no unobserved source bit is
needed. For a fixed finite S_i transcript, only finitely many coordinates
are in R. Each no-output skip consumes one distinct member of R in T-order.
There cannot be infinitely many skips before the next fresh output. Pulls
themselves are outputs; thus each next-query computation terminates. Queries
are fresh on every transcript. On an infinite transcript τ cannot stay
bounded, since only finitely many pulls and T-queries occur at bounded τ.
Thus τ→∞. This argument applies equally to F, and does not assume a favourable
source or that the original betting succeeds.

**Global holes.** S_i reads everything T reads, plus every held coordinate
of another colour. Any permanently omitted coordinate of T eventually
enters U because n_t→∞ and is pulled unless coloured i. Hence S_i has at
most one permanent omission on EVERY source/transcript. F reads all held
and fill coordinates and is exhaustive. By T-time c(q+1), it has read q.
At this time at most c(q+1) in-step reads and at most n_{c(q+1)} pulls have
occurred. The harmless inclusive bound 2c(q+1)+h+1 on output length works
uniformly on every transcript. Consequently F is a fair effective
isomorphism, with inverse obtained by finite simulation until each coordinate
is queried. E-ISO makes F(z) CR whenever z is CR.

Normalize d(∅)=1. Its rational stake at T-history u is
θ(u)=(d(u1)−d(u0))/(2d(u)), or zero at d(u)=0. All copied/pulled stakes
are computable from the new scan's own history and lie in [−1,1], giving
total rational martingales D_i,D_F. Along a winning y=F_T(z), d never
vanishes. Its factors f_s=1+θ(y↾s)(2y_s−1) are positive. At each completed
T-time τ every original factor occurs exactly once, in the fill account or
one held-colour account, while pulls contribute 1. Hence

    d(y↾τ)=D_F(τ)∏_{i=1}^h D_i(τ).

Each account value is taken on a real output prefix of its own scan.
D_F is bounded above on CR F(z). If all finitely many D_i were bounded above,
their product would bound d, contradiction. Equivalently split logarithms;
no lower bound on individual accounts is needed. Thus some D_i succeeds on
the one-hole scan S_i(z), and z∉OH. This proves OH⊆OH_h; the reverse inclusion
is immediate. By §2.3, R_k^scan=OH_{⌊log₂k⌋}=OH for each fixed k≥2.
There is no inference for unbounded budgets or arbitrary non-scan F_k maps.

## 4. Consistency potentials and savings

For a total fair G and rational output martingale d, put X_t(z)=d(G(z)↾t).
For each w∈2^t, let c^σ(w) indicate that G⁻¹[w] meets [σ], and let
s^{σ,k}(w) indicate that it meets both [σ∪{k↦0}] and [σ∪{k↦1}], for
k∉dom σ. Define the computable rationals

    Ψ(σ,t)=2^{|σ|}∑_{w∈2^t}2^{−t}d(w)c^σ(w),
    γ(σ,k,t)=2^{|σ|}∑_{w∈2^t}2^{−t}d(w)s^{σ,k}(w).

Clopen intersection decisions come from §2.1. Four exact properties suffice:

1. **Time monotonicity.** c^σ(wb)≤c^σ(w). Nonnegativity and the martingale
   equation give Ψ(σ,t+1)≤Ψ(σ,t), term by term on parents.
2. **Domination.** Since 1_[σ](z)≤c^σ(G(z)↾t), fairness gives
   E[X_t|[σ]]≤Ψ(σ,t). This is a bound on all completions, not only true fixes.
3. **Refinement.** Write σ_b=σ∪{k↦b}. At each cell,
   c^{σ_0}+c^{σ_1}=c^σ+s^{σ,k}. The factor 2^{|σ_b|}=2·2^{|σ|} gives
   (Ψ(σ_0,t)+Ψ(σ_1,t))/2=Ψ(σ,t)+γ(σ,k,t).
   Thus the cheaper fixed value costs at most γ.
4. **Savings.** For normalized d₀, start active A=1, bank B=0. At child ub
   let A'=A(u)d₀(ub)/d₀(u), using A'=A(u) if d₀(u)=0. Repeatedly move
   one unit from A' to B while A'≥2. Let d=A+B. Before transfers the two
   totals average to A+B; transfers leave totals unchanged. Thus d is a
   total rational martingale with 0≤A<2 and nondecreasing B. For t'≥t,
   d(y↾t')>d(y↾t)−2. If d₀ stays positive and d is bounded, only finitely
   many bank transfers occur. Active A stays positive (a transfer leaves
   A≥1), and after the last transfer A=c d₀ with c>0; hence d₀ is bounded.
   If d₀ hits zero, it stays zero and is already bounded on that path.

For raw scans, a transcript cell fixes its queried coordinates, so
s^{σ,k}=c^σ·1_{k unread}. At t≥c(n), for a candidate set J⊂[0,n)\dom σ,
∑_{k∈J}γ(σ,k,t)≤hΨ(σ,t); at one hole the coefficient is 1.
For G=F_T∘K with one-hole T, choose candidates in pairwise distinct K-blocks,
all those entire blocks below n. A fully read virtual block determines the
whole raw block via κ_j⁻¹, so no raw candidate in it can split. At most one
candidate block is incomplete because there is at most one unread virtual
coordinate below n. Therefore ∑_{k∈J}γ≤Ψ again. This remains true after
arbitrary σ fixes; they can remove splits but cannot create a second
incomplete candidate block. For finitely many active recodings, candidates
can be chosen simultaneously in distinct blocks of every recoding: each
previous choice excludes only a finite union of finite blocks.

## 5. Partial enumeration, actual test price and common-source B

Fix a standard enumeration of tuples of partial programs for the block
presentation K, query function T, and rational stake θ. A tuple e is valid
iff K is a genuine total presentation as in §1, T is total/no-repeat/one-hole
on every transcript, and θ is total with outputs in [−1,1]. Raw scans are
included by the identity K. Every rational output martingale with positive
initial capital gives such a stake program after normalization. An identity
T is also included, so survival covers CR of every K(z).

**Concrete syntax for wrong guesses.** Decode natural-number queries, finite
lists of distinct natural coordinates, canonical finite bijection tables,
and rational numerator/positive-denominator pairs. Reject malformed returned
values, repeated scan queries on inspected histories, stakes outside [−1,1],
and inconsistent block membership on inspected finite data. A rejected run
has no output at that stage. A required computation that fails to halt simply
keeps that run pending; all runs are dovetailed. To compute a finite G-cell,
simulate every required transcript query/stake and fetch the finite blocks
and tables of its finitely many virtual coordinates. Intersect those finite
block constraints and σ. For valid indices this is exactly the clopen set;
no semantic validity oracle is consulted. Finitely inspected malformed data
cannot be assigned arbitrary successful mass. Even an invalid tuple that
passes the finite checks and finishes a guessed run emits only a finite
assignment with the required number of distinct coordinates and binary values.
Its capital need not obey the valid-index estimates; the ML-test count needs
only that cylinder size. This specifies a partial computable implementation
of the historical guessed-run instructions, rather than a computable
enumeration of valid strategies.

All validity clauses can be put in Π⁰₂ form. Totality, correct tables and
partition agreement use ∀finite input ∃finite halting/check witnesses.
The one-hole clause is equivalently ∀n∃c such that all 2^c transcripts read
all but at most one coordinate below n; finite computation witnesses make
this Π⁰₂ together with totality. Its equivalence is §3's frontier proof.
Thus the true characteristic sequence ε* is ∅″-computable, but the ML test
and T* below do not compute ε*.

A guessed run on a finite binary string ε has stages i<|ε|, finite assignment
σ, output time τ, active set A and positive rational weights w_e. Initially
σ=∅, τ=0, A=∅. Write Φ=∑_{e∈A}w_eΨ^e and Γ=∑_{e∈A}w_eγ^e using SAVINGS
martingales. Let ℓ_i=2i+2 and N_i=2^{i+4}ℓ_i. At stage i:

* If ε(i)=1, compute P=Ψ^i(σ,τ), add i with w_i=2^{−i−2}/(1+P).
* Repeat ℓ_i times: let a=1+max dom σ (zero if empty); choose N_i fresh
  strictly increasing candidates ≥a, in distinct blocks of EVERY active recoding. Let n exceed
  every coordinate in their entire active blocks (and the candidates).
  Search all active frontiers and set τ''=max(τ,max_e c_e(n)). Minimize
  Γ(σ,k,τ'') over candidates, ties by least k; then minimize
  Φ(σ∪{k↦b},τ'') over b, ties by 0. Fix this bit and set τ=τ''.
* Emit σ_i^ε and τ_i^ε only after all repetitions have finished.

The raw construction uses the interval [a,a+N_i). The block construction uses
greedy distinct-block candidates instead. True finite guesses halt: each
needed program is total, frontier searches terminate, and finite blocks
exclude only finitely many members of an infinite candidate pool. Wrong
guesses may hang, be rejected, or finish. Exactly ℓ_i new coordinates larger
than all earlier fixes are added by ANY completed run, so after stage i
|σ_i^ε|=(i+1)(i+2). Identical guess prefixes execute identical instructions
and share identical weights, times and fixes.

**Invariant.** For true guesses, before stage i the carried Φ is at most
2−2^{−(i−1)} (zero for i=0). A new active term adds <2^{−i−2}. Time advance
cannot raise Φ. The cost bound gives ∑_k Γ≤Φ<2, so its minimizing candidate
costs <2/N_i; refinement then raises Φ by at most that amount. All ℓ_i
costs total <ℓ_i·2/N_i=2^{−i−3}. There is no circular assumption Φ<2:
induct on the repetitions with these partial costs; their maximum, including
the new term, is (3/8)2^{−i}, smaller than the starting headroom 2·2^{−i}.
At stage end

    Φ(σ_i^*,τ_i^*) < 2−(13/8)2^{−i} < 2−2^{−i}.

**Ordinary ML test.** Dovetail all 2^{i+1} guessed prefixes of length i+1
and enumerate [σ_i^ε] whenever that run completes. A finite assignment
enumerates a finite union of standard prefix cylinders, so this is uniformly
c.e.-open in the ordinary sense. At most 2^{i+1} assignments are emitted,
each of measure 2^{−(i+1)(i+2)}. Thus

    λ(V_i)≤2^{i+1−(i+1)(i+2)}=2^{−(i+1)^2}≤2^{−i}.

This is the number of POSSIBLE completed guesses; no claim that all complete,
no computable completion deadline and no computation of exact union measure
are needed. True assignments σ_i^* are nested, nonempty, and have positive
finite measure 2^{−(i+1)(i+2)}. S=⋂_i[σ_i^*] is nonempty compact and every
point of S lies in every V_i. NonMLR is certified by this computably emitted
test, not by non-effective selection of ε* or geometric nullness alone.

**Common-source survival.** For each valid e let L_e=2+2/w_e. Suppose every
point of S exceeds some X_t^e>L_e. Their union O is open since each X_t^e
is a finite-coordinate function. Nested compactness gives [σ_{i₀}^*]⊂O:
otherwise pick outside-O points at arbitrarily late stages and take a
cluster point in S\O. A finite subcover then gives finitely many witnesses
(e_r,t_r). Choose j≥i₀ and every e_r, and t≥τ_j^* and every t_r.
Savings gives, for every z∈[σ_j^*], at least one
X_t^{e_r}(z)>L_{e_r}−2=2/w_{e_r}. Therefore the weighted sum >2 on
[σ_j^*]. It is finite-coordinate and has a minimum >2 there. Domination
forces Φ(σ_j^*,t)>2, whereas monotonicity and the invariant give Φ<2.
Contradiction. Thus ONE z∈S bounds EVERY valid savings capital, and savings
then bounds each original martingale. Identity scans give CR and all other
scans give K(z)∈OH for every K. This proves B independently of tail coding.

## 6. Class-separated strengthening and the tail observer

To prove C use the same construction with one change in candidate pools.
Fix a computable bijection ι from finite binary strings to ℕ and Cantor
pairing ⟨·,·⟩. Put C_ε={⟨ι(ε),j⟩:j∈ℕ}. These classes are disjoint,
infinite, uniformly decidable and have computable increasing enumerations.
At stage i select candidates ≥a from C_{ε↾(i+1)}, greedily avoiding the
finitely many active blocks used by earlier candidates. True searches still
halt, and every cost estimate, invariant, cylinder size and ML-test count
in §5 survives unchanged. Write S for this strengthened true limit.

**Shared fixes agree.** A completed false run and the true run have identical
stages before their first guess disagreement. Thereafter their stage classes
are disjoint: equal stage lengths give different prefixes, and unequal
lengths name different classes. Hence every coordinate shared with ANY
finite true assignment has the SAME value, whether the false guess is a
true prefix or incomparable. This includes true assignments shorter or
longer than the completed false run. Semantic validity of the false run is
unnecessary.

Define D′(z)_0=z_0 and D′(z)_i=z_i⊕z_{i−1} for i≥1. The inverse is
z_i=⊕_{s≤i}v_s. Each finite prefix transform is a bijection, so D′ and
its inverse are total computable fair homeomorphisms. D′ is not a finite-block
recoding: changing raw bit j changes virtual bits j and j+1, so any block
presentation must put j and j+1 in the same block for EVERY j, forcing an
infinite block. This explicit dependence argument does not confuse an
unbounded inverse use with a proof of non-blockness.

If the virtual read set is [0,M)\{q}, M>q, the raw prefix below q is known,
and for q≤F<M put π_F=z_{q−1}⊕⊕_{q<s≤F}v_s, using z_{−1}=0.
Then z_F=π_F⊕v_q. Flipping the held v_q alone complements the entire raw
tail [q,∞). An absolute fix at ANY F≥q therefore determines the hold once
the intervening virtual bits are read.

**T* and d*.** Start q=0,M=1, with no virtual coordinates read. At a transcript
of length t, simulate each nonempty guessed run ε with ι(ε)<t for t steps.
Use only completed runs; m=|ε|≥1 and σ' is its final assignment. It qualifies if:

1. σ' agrees with the known raw values on dom σ'∩[0,q);
2. the r(q,m)=q+2m+4 least fixed positions F_l≥q exist and are all <M;
3. all σ'(F_l)⊕π_{F_l} have the same value ν.

If a run qualifies choose least ι(ε), query v_q, wager all on ν, then set
q=M and increment M. Otherwise query filler v_M with zero stake and
increment M. Replay these bounded simulations from the preceding transcript
to compute the next query and wager. They neither decide validity nor wait
for any particular run to halt. d* starts at 1, is constant at fillers, and
has children 2d*,0 at a resolution, ordered by ν.

**Every-transcript legality.** The invariant read set is [0,M)\{q} before
each query, with M>q. Either move reads a fresh coordinate and preserves that
invariant; resetting q=M after a resolution leaves exactly the new unqueried
hold. Bounded simulations make each next query total. Infinitely many
resolutions send q→∞ and read EVERY coordinate; finitely many leave only
the final q unread because fillers continue forever. Thus T* is a total
computable no-repeat one-hole scan on EVERY transcript, d* is a total rational
martingale, and §2.3 makes F_{T*} fair with all fibres ≤2. Composing with
D′ preserves fairness and EXACT cardinal counts. G=F_{T*}∘D′∈F₂ on all
outputs, not merely almost surely or on the eventual witness.

## 7. Relative fooling exclusion and ONE protected destroyed source

At a qualifying resolution on raw source x, for every selected F_l,
x_{F_l}⊕π_{F_l}=v_q and σ'(F_l)⊕π_{F_l}=ν. Thus ν≠v_q forces
x_{F_l}=1−σ'(F_l) for ALL r selected fixes. If even one matches σ', every
one matches and the resolution is correct. This is an exact implication
at each actual resolution, independent of the guess's validity.

Let W be the sources producing any wrong resolution of T* on D′(x).
It is effectively open: a wrong resolution is witnessed by finitely many
virtual bits, themselves computed from a finite raw prefix. For each q
and nonempty completed guess ε of length m, let B(q,ε) be the cylinder
setting the r(q,m) least fixed positions ≥q opposite to σ'; it is empty
if too few positions exist or the run never completes. Then W⊂⋃B(q,ε).
Fix ANY finite true state [σ_j^*]. If a selected position is already fixed
there, shared-fix agreement makes B(q,ε)∩[σ_j^*] empty. Otherwise its r
distinct positions are all free and its relative measure is exactly 2^{−r}.
Therefore, uniformly for EVERY j,

    λ(W∩[σ_j^*])/λ[σ_j^*]
       ≤∑_{q≥0,m≥1}2^m 2^{−q−2m−4}
       =2^{−4}(∑_{q≥0}2^{−q})(∑_{m≥1}2^{−m})=1/8.

This is conditional relative control; a bound at σ=∅ alone would not suffice.
Class separation is essential. No independence between different events is
assumed in the union bound.

**Every true-limit hold resolves.** Fix x∈S and a hold q. A true prefix of
length m finishes and has m(m+1) fixed positions, at most q below q. Choose
m with m²−m≥2q+4, so it has at least q+2m+4 fixes ≥q. Known-prefix
agreement holds because x extends that true assignment; the implied hold
values are all v_q. If the hold stayed unresolved, fillers would give
M→∞ and the computation budget t→∞, eventually covering these finitely
many positions, the run's index and its finite runtime. This run would
qualify, contradiction. An earlier qualifying run might resolve first;
that only strengthens termination. Since a resolved hold is replaced by
a new fresh one, EVERY x∈S resolves infinitely often.

**Simultaneous compactness.** Set L_e=2+4/w_e for valid e, and
O=⋃_{e valid,t}{X_t^e>L_e}. Suppose S⊂O∪W. As in §5, some finite true
cylinder [σ_{i₀}^*] is covered; take finitely many clopen capital witnesses
and finitely many clopen subsets W_l⊂W covering it together. Choose later
j containing all witness indices and t beyond all witness times and τ_j^*.
Outside ⋃W_l, savings forces the active weighted capital >4 pointwise.
That region is clopen and has relative measure ≥7/8 in [σ_j^*]. It is
nonempty and the finite-coordinate capital has minimum >4 on it.
Domination then gives

    Φ(σ_j^*,t) > 4(1−1/8)=7/2>2,

contradicting time monotonicity and Φ(σ_j^*,τ_j^*)<2. This also covers an
empty collection of capital witnesses: W alone cannot cover a positive
true cylinder by its relative bound. Hence there exists ONE

    z∈S\(O∪W).

It is nonMLR by the SAME class-separated guessed-run ML test. All valid
block-recoded savings capitals, hence all original martingales, are bounded
on it, so z∈OH^blk⊆OH and z∈CR. Every T* hold resolves on this z and none
is wrong, so d*(G(z)) doubles infinitely and G(z)∉CR. D′(z)∈CR by E-ISO,
but D′(z)∉OH. This proves C, R₂⊊OH, and OH^iso⊊OH^blk on ONE common
source. It proves neither z∈R₂ nor destruction of all nonMLR sources.

For the optional historical complexity bound, validity is Π⁰₂ as specified
in §5. True states, weights and bounds are ∅″-computable; S\(O∪W) is a
nonempty Π⁰₁(∅″) class. A leftmost path is computable in ∅‴ by asking
which finite prefixes have infinite extensions. This is an existence bound,
not effective advice inserted into G. A–C do not require the bound.

## 8. S084 reconciliation: balanced double fibres and exceptional destruction

For completeness reconstruct only the boundary needed here. For Q≥0 the
union E_Q of opposite-fix cylinders B(q,ε), q≥Q, is uniformly c.e.-open,
with λ(E_Q)≤2^{−Q−3}; the same bound holds relatively on every true state.
There is a total rational output martingale d_restart which puts weight
2^{−j−1} into an account beginning at output time j, each account betting
all-in on T* resolutions and zero on fillers. At a prefix u include only
accounts j≤|u| plus the exact rational tail 2^{−|u|−1}. This is an exact
martingale of initial capital 1. If resolutions are infinite but errors
finite, a post-last-error account succeeds. If errors are infinite, the
strictly increasing hold coordinates put the source in every E_Q.
Thus the infinite-resolution locus I is covered by the ordinary ML test

    E_n ∪ G⁻¹{y:∃t d_restart(y↾t)≥2^{n+1}}.

The second component has measure ≤2^{−n−1} by the finite martingale maximal
inequality and its monotone limit; fairness pulls this bound to source
space. The total bound is (1/8+1/2)2^{−n}<2^{−n}, so λ(I)=0.

The number of resolutions is determined by the output transcript, making
I=G⁻¹(I_out), with I_out Borel (in fact effective G_delta). Fairness gives
λ(I_out)=0. A finite-resolution output omits precisely its final virtual
q; its two preimages differ only at v_q, hence in raw coordinates by the
tail-complement J_q. On the measurable piece with final hold q, the query
process never sees v_q. Flipping it preserves the whole output and fair
measure. Disintegration symmetry therefore gives equal weights 1/2,1/2
on that pair almost everywhere. One may equivalently take conditional limits
of finite transcript probabilities: on each fixed-q final-hold piece, the
unqueried bit is unbiased. This is an a.e. statement, not a computable
all-source inverse or a preservation theorem. The z in §7 is in I, has a
singleton fibre, is CR nonMLR, and is destroyed. There is no contradiction.

## 9. Proof challenge, clarifications and exact exclusions

No fatal proof error was found in A–C. The following formerly compressed
points are now proved explicitly, without upgrading historical evidence:

* The n_t maximum is finite, and simulations skip only a finite existing
  read set before the next output. All-source history reconstruction and
  exhaustion replace any target-only simulation assumption.
* Completed wrong guesses emit cylinders of the correct size even though
  their potentials need not satisfy the true invariant. Partial syntax is
  specified; neither validity selection nor exact union measure is computable.
* Φ<2 is maintained by a prefix-of-stage budget, not assumed circularly.
  Finite true states have positive mass; the limit need not.
* Savings needs positive active capital after the last transfer on a positive
  d₀ path. The zero-capital case is handled separately.
* W is bounded relative to EVERY true finite state. Shared fixes have equal
  values; a false resolution requires all opposite fixes. Compactness selects
  one source satisfying both capital exclusion and no-fooling.
* S032's partial inverse contains every CR input in its full-measure domain.
  S084's balanced double fibres are a.e., whereas the F₂ bound is everywhere.
* The forward-dependence proof makes D′ non-blockness precise. Infinite
  inverse use alone would not justify that conclusion.

These are implementation/proof elaborations, not errata changing any theorem
or hierarchy. Selected original finite exact audits are replayed separately.
They do not prove infinitary compactness, CR, MLR failure, or universal legality.

S087–S090 later protect broader restricted difference families and give
stronger separations. None is needed here, none upgrades B to all F₂, and
none identifies the original X as this constructed source. The S084 entire
error-stream restriction for a hypothetical R₂ source is separate from the
no-error witness here. EQ/SEP, R₂ versus OH^iso, U(H), original X∈OH,
fixed-S preservation and Conjecture R remain unresolved.

CAND-01, DEF-0020, PA-0001 and original Y/M/H/X (H rows 101/110/111) are
unchanged. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED.
Source proof verification remains an external-use obligation under the
declared assumptions, not an unresolved internal bridge disguised as proved.
S101 closes the dossier target ahead of S100's S103 deadline; speculative
flagship sessions used in the S101–S105 window: ZERO. S102 remains future.
