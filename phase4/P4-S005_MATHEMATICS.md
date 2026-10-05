# P4-S005 — k=2 crossing-measure non-effectivity boundary

Date: 2026-10-05
Session: P4-S005
Incoming checkpoint: beaa3c41f886176cde1b51d74e6e812b8f30974a
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 only
Result: **THE FORCED TWO-PREFIX LISTS DO NOT MAKE LOW-WEIGHT CROSSING MEASURES COMPUTABLE; A NATURAL SYMMETRIC FIBRE-COUNT LIFT CAN ALSO HAVE NONCOMPUTABLE MASS; NO EXACT k=2 RANDOMNESS-DESTROYING WITNESS IS OBTAINED**

## Authority, uniqueness and scope

Live `main` matched the incoming checkpoint exactly before substantive work and P4-S005 was unused. Gate 3 is PASS and Phase 4 is OPEN for selected CAND-01. Phase 5 remains CLOSED.

P4-S001 through P4-S004 are preserved exactly. This session stays strictly at k=2. It does not make a claim for k>2, novelty, openness, Gate 4, publication or outreach. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard remains historical. DEF-0020 is unchanged.

## Retained P4-S004 problem

For a finite source string sigma and output string tau,
[
w_\sigma(\tau)=2^{|\tau|}\lambda([\sigma]\cap F^{-1}([\tau]))
]
is a uniformly computable rational martingale bounded by 1. P4-S004 defined
[
V_{\sigma,\epsilon}
 =\{x\in[\sigma]:\exists m;w_\sigma(F(x){\upharpoonright}m)<\epsilon\}
]
and proved that it is uniformly effectively open with
[
\lambda(V_{\sigma,\epsilon})\le\epsilon.
]

The open question for this session is whether the k=2 two-prefix structure forces the hitting measure itself to be computable, or otherwise supplies a computable stopped/pullback construction strong enough for computable randomness.

## Theorem 1 — k=2 does not force computable low-weight crossing measures

There is an everywhere-total computable fair-coin-preserving Cantor self-map F with fibres of size at most two, and in fact with a computable clopen split into two injective sheets, such that
[
\lambda(V_{0,1/3})
]
is noncomputable.

### Step 1 — a prefix-free family of output blocks

Fix a c.e. noncomputable set K. For e>=0 let
[
t_e=1^e0^{e+2},\qquad T_e=[t_e].
]
The words t_e are prefix-free and
[
q_e=\lambda(T_e)=2^{-(2e+2)}=4^{-(e+1)}.
]
Let
[
R=2^\omega\setminus\bigcup_e T_e.
]

Write an input as rz with r in {0,1}. The first bit r will be the global sheet label.

### Step 2 — the finite local codes

Define injective prefix-code maps C_0,C_1 on Cantor space by
[
C_0(00u)=00u,\quad C_0(01u)=10u,\quad C_0(1u)=11u,
]
and
[
C_1(00u)=00u,\quad C_1(01u)=10u,\quad C_1(1u)=01u.
]

Thus the two images overlap on [00] and [10]; [01] is reached only from sheet 1 and [11] only from sheet 0.

If e enters K for the first time at stage s, define
[
G_{e,r}(u)=u{\upharpoonright}s;C_r(u_{\ge s}).
]
If e never enters K, put G_{e,r}(u)=u.

This definition is computable despite the negative case. To compute the first n output bits of G_{e,r}(u), simulate the enumeration of K for n steps. If e has not entered by then, any later activation occurs after the requested output prefix, so those n bits are just u↾n. If e entered at a stage s<n, the finite code above determines the requested prefix.

### Step 3 — define F

For the unique e with z=t_eu, set
[
F(rz)=t_eG_{e,r}(u).
]
For z in R, set
[
F(rz)=z.
]

To compute an n-bit output prefix, inspect only enough input to determine whether a block T_e has already been entered; if no such block is determined within the requested prefix, copying z is correct because every later block keeps its marker t_e unchanged. Hence F is everywhere total computable and continuous.

### Step 4 — exact fair-coin and fibre checks

On R and on every nonactivated block T_e, F is just the ordinary two-sheet one-bit deletion map, so every output has one preimage in each sheet.

Suppose e enters K at stage s. After the copied s-bit local prefix, inspect the four two-bit output cylinders. Relative to the current output parent P, the source preimage masses are:

| target child | sheet 0 | sheet 1 | total |
| --- | ---: | ---: | ---: |
| P00 | 1/8 lambda(P) | 1/8 lambda(P) | 1/4 lambda(P) |
| P01 | 0 | 1/4 lambda(P) | 1/4 lambda(P) |
| P10 | 1/8 lambda(P) | 1/8 lambda(P) | 1/4 lambda(P) |
| P11 | 1/4 lambda(P) | 0 | 1/4 lambda(P) |

The remaining tail is copied. Therefore every target cylinder receives exactly its fair-coin mass. Hence F_*lambda=lambda.

Fibres have size at most two: P00 and P10 have one preimage in each sheet, while P01 and P11 have one preimage. Different blocks and R have disjoint images. Moreover each restriction F|[0] and F|[1] is injective, because each local C_r is injective. Thus [0],[1] form a computable clopen two-sheet split.

### Step 5 — compute the low-weight event

Take sigma=0. Before an activation, and on all block ancestors, the two sheets contribute equally, so w_0=1/2.

At the first output bit of the activated local code,
[
w_0(P0)=1/4,\qquad w_0(P1)=3/4.
]
At the next bit the four values are respectively
[
1/2, 0, 1/2, 1.
]

A sheet-0 source point can enter the low parent P0 only through local source codeword 00. It therefore crosses below 1/3 exactly on a subset of source block [0t_e] of relative sheet probability 1/4. Since
[
\lambda([0t_e])=q_e/2,
]
the contribution of an activated block is q_e/8. Nonactivated blocks contribute nothing. Hence
[
\lambda(V_{0,1/3})
 =\frac18\sum_{e\in K}4^{-(e+1)}.
]

### Step 6 — noncomputability

Let
[
\alpha=8\lambda(V_{0,1/3})
      =\sum_{e\in K}4^{-(e+1)}.
]
Its base-4 digits are exactly chi_K(e), each in {0,1}. This coding has a uniform gap: after the first e digits have been removed and the remainder is scaled by 4^{e+1}, the value is at most 1/3 if e is not in K, and at least 1 if e is in K. Thus a computable alpha would compute K digit by digit. Since K is noncomputable, alpha and therefore lambda(V_{0,1/3}) are noncomputable. ∎

## Consequence for the P4-S004 stopping route

The P4-S003 two-prefix inverse lists do **not** force the P4-S004 low-weight hitting measures to be computable. The counterexample is stronger than needed: it already has the explicit computable clopen two-sheet split that P4-S003 showed sufficient for forward computable-randomness preservation.

Therefore the direct proposed upgrade
[
V_{\sigma,\epsilon}: c.e. open with computable measure
]
fails in general at k=2. In particular, V_{0,1/3} in the example cannot itself be used as a Schnorr-test component through the standard computable-level-measure requirement.

This does **not** prove that no alternative Schnorr cover exists, and it does not refute a different general k=2 preservation theorem. It refutes the specific inference from bounded inverse lists to computable crossing probability.

## Lemma 2 — a natural symmetric fibre-count lift is not uniformly computable either

A second branch-label-free idea is to lift an output probability measure nu by counting inverse points. For a source cylinder [rho] put
[
\widehat\nu([\rho])
 =\int \#(F^{-1}(y)\cap[\rho])\,d\nu(y).
]
The cylinder values are finitely additive because inverse-point counts split over rho0 and rho1, and the total mass is at most 2.

If this finite measure were uniformly computable, it would provide a natural symmetric starting point for a martingale pullback without choosing a persistent branch.

For the map in Theorem 1 and nu=lambda, however,
[
\widehat\lambda(2^\omega)
 =\int |F^{-1}(y)|\,d\lambda(y).
]
Outside activated blocks every fibre has size two. Inside an activated block exactly half of its output mass has two preimages and half has one. Therefore
[
\widehat\lambda(2^\omega)
 =2-\frac12\sum_{e\in K}q_e.
]
The same base-4 coding shows that this total mass is noncomputable. Hence the symmetric fibre-count lift is not a uniformly computable finite measure even for the computable output measure lambda.

This blocks another natural attempt to turn “at most two inverse candidates” into one computable branch-free martingale.

## Fixed-stage pullbacks remain exact but incoherent

P4-S004's martingales
[
e_m(\sigma)=2^{|\sigma|}\int_{[\sigma]}d(F(z){\upharpoonright}m)\,d\lambda(z)
]
remain valid and unchanged. The present theorem does not damage them. It shows instead that one obvious way to choose or normalize stopping stages—by computing the relevant low-weight hitting probability—cannot be forced from k=2.

Likewise, at a synchronization precision supplied by the two-prefix theorem one can form finite-stage densities by dividing among the at most two current candidates. Those finite objects need not be projectively coherent as candidates merge, split or disappear. Lemma 2 shows that the most symmetric count-each-preimage projectivization can already hide noncomputable mass.

No single computable stopped/pullback martingale transferring every output computable-martingale success is obtained in this session.

## Why Theorem 1 is not a randomness-destruction witness

The domain partition [0],[1] is computable clopen and F is injective on each half. Therefore P4-S003's positive two-sheet theorem applies: F preserves computable randomness forward.

This is important. Noncomputable crossing probability is a real obstruction to the proposed stopping proof, but by itself it does not imply non-conservation.

## Exact destruction-witness route pursued and not completed

The requested negative target would require an everywhere-total computable fair-coin-preserving k=2 map, a computably random x on a genuinely thin/non-effectively controlled sheet, and a non-computably-random F(x).

Three mechanisms were tested.

1. **Use the halting-gadget map above.** This fails as a destroyer because its persistent first-bit sheet label is computable and the P4-S003 positive theorem applies.
2. **Symmetric fibre counting instead of sheet labels.** Lemma 2 shows that the associated finite measure can have noncomputable total mass, so this does not furnish the needed computable pullback.
3. **Return to SRC-0061 with one hidden/masked filler bit.** The P4-S004 pre-revealed-bet obstruction remains. A masked filler can postpone disclosure, but if that coordinate is later exposed as a genuine betting position then the mask, or an equivalent accumulated relation, can reveal other previously masked coordinates that may themselves be future betting positions. Rotating a single hidden bit transfers rather than removes this problem. No construction was found that simultaneously preserves the winning output simulation and leaves at most one source bit globally unresolved on every path.

Accordingly, no exact k=2 computable-randomness-destroying witness is established in P4-S005.

## Successful and failed mechanisms

Successful:

1. An exact k=2 map with a computable clopen injective-sheet split and a noncomputable low-weight crossing measure.
2. A proof that the forced two-prefix inverse lists do not imply computable hitting probabilities, even under strictly stronger sheet information.
3. A noncomputability obstruction for the canonical symmetric fibre-count lift.
4. A clean separation between stopping-effectivity failure and actual randomness non-conservation.

Failed or incomplete:

1. Upgrading the P4-S004 crossing sets themselves to Schnorr-test components by computing their measures.
2. Obtaining a projectively coherent branch-free martingale from equal candidate/fibre counting.
3. Resolving the SRC-0061 filler/pre-revealed-bet problem with one hidden or rotating mask bit.
4. Constructing a computably random source on a genuinely thin sheet with a non-computably-random image.

## Proof dependencies and guards

The new construction uses only elementary prefix coding, fair-coin cylinder measure, computable enumeration of a fixed c.e. noncomputable set, P4-S003's already-proved positive clopen-sheet theorem, and the P4-S004 definitions of w_sigma and V_{sigma,epsilon}. No new literature theorem is imported.

SRC-0061 / THM-0072 is mentioned only as the previously recorded unrestricted scan route; no finite-fibre conclusion is imported.

- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- The pre-Phase-4 Gate-3 guard is preserved historically.
- P4-S001 through P4-S004 are unchanged exactly.
- General k=2 forward computable-randomness preservation/failure remains unresolved.
- No result is claimed for k>2.
- DEF-0020 and all catalogue/source convention guards are unchanged.
- No novelty/open-status claim is made.
- Gate 4 is not reviewed. Phase 5 remains CLOSED.
