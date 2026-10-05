# P4-S004 — k=2 conditional-weight stopping boundary

Date: 2026-10-05
Session: P4-S004
Incoming checkpoint: 08b2d04dba6adb57435857369cd2b5317c508940
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 only
Result: **LOW CONDITIONAL SHEET WEIGHT GIVES AN ML-LEVEL PULLBACK TEST AND FIXED-STAGE MARTINGALES LIFT EXACTLY, BUT COMPUTABLE-RANDOMNESS-LEVEL STOPPING/COHERENCE IS NOT FORCED BY THE ESTABLISHED DATA; BARE k=2 ALLOWS VANISHING SHEET WEIGHT; GENERAL k=2 PRESERVATION/FAILURE REMAINS UNRESOLVED**

## Authority, uniqueness and scope

Live `main` matched the incoming checkpoint exactly before substantive work and again before closeout. Repository search returned no committed P4-S004 record, so the session identifier was unused.

Gate 3 is PASS and Phase 4 is OPEN for selected CAND-01. Phase 5 remains CLOSED. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The Gate-3 guard remains historical: before Phase 4 no computable-randomness consequence of the bare global finite-cardinality fibre bound had been established.

P4-S001 through P4-S003 are preserved exactly. This session stays at k=2. It makes no claim for k>2, novelty, openness, Gate 4, publication or outreach. DEF-0020 is unchanged.

## Exact k=2 hypotheses and retained data

Let lambda be fair-coin measure and let F:2^omega -> 2^omega be everywhere-total computable, lambda-preserving, with |F^{-1}(y)|<=2 for every y.

P4-S003 supplies two retained facts:

1. for every input precision n, sufficiently much output gives a computable list of at most two candidate n-prefixes for the fibre;
2. for every finite source string sigma,
   [
   w_\sigma(\tau)=2^{|\tau|}\lambda([\sigma]\cap F^{-1}([\tau]))
   ]
   is a uniformly computable rational-valued martingale on output strings, bounded between 0 and 1.

No coherent branches or sheet colouring are assumed.

## Lemma 1 — low persistent-sheet weight produces only an ML-level pullback test

Fix a finite source string sigma of length s and condition fair coin on [sigma]:
[
\lambda_\sigma(B)=2^s\lambda(B\cap[\sigma]).
]
Let `mu_sigma=F_*lambda_sigma`. It is a computable probability measure because F is total computable and cylinder preimages are computable clopen. For every output string tau,
[
\mu_\sigma([\tau])=2^{s-|\tau|}w_\sigma(\tau).
]

On strings with positive `mu_sigma`-mass define
[
q_\sigma(\tau)=\frac{\lambda([\tau])}{\mu_\sigma([\tau])}
               =\frac{2^{-s}}{w_\sigma(\tau)}.
]
Then `q_sigma` is a nonnegative `mu_sigma`-martingale with initial value 1.

For rational epsilon>0 let
[
V_{\sigma,\epsilon}
 =\{x\in[\sigma]:\exists m\; w_\sigma(F(x){\upharpoonright}m)<\epsilon\}.
]
This set is uniformly effectively open. Ville's inequality applied to `q_sigma` gives
[
\lambda(V_{\sigma,\epsilon})\le\epsilon.
]

**Proof.** The condition `w_sigma(tau)<epsilon` is decidable because the weight is a computable rational, and `[sigma]∩F^{-1}([tau])` is computable clopen, so the union is effectively open. Under `lambda_sigma`, the output has law `mu_sigma`. Crossing `w_sigma<epsilon` is the same as crossing `q_sigma>2^{-s}/epsilon`. Hence `mu_sigma(crossing)<=epsilon*2^s`. Multiplying by `lambda([sigma])=2^{-s}` yields the displayed bound. ∎

Consequently, if x is Martin-Löf random and sigma is a prefix of x, then `inf_m w_sigma(F(x)↾m)>0`. Otherwise x would lie in every member of the Martin-Löf test `V_{sigma,2^{-j}}`.

This does **not** settle the requested computably-random source case. The catalogue records the strict implication Martin-Löf randomness -> computable randomness in REL-0001. Thus an ML-test bound cannot by itself be discharged from the weaker hypothesis that x is computably random. Computable randomness does imply Schnorr randomness (REL-0002), so one exact positive route would be to prove that the measures of the crossing sets above are uniformly computable, or otherwise upgrade them to a computable-randomness test. P4-S004 does not obtain that effectivization from the two-prefix lists.

The crossing measure is a hitting probability for a computable likelihood-ratio martingale. The set is c.e. open and its measure is lower semicomputable, but the established k=2 data provide no computable stopping probability or convergence modulus.

## Lemma 2 — every fixed output betting stage lifts exactly

Let d be a nonnegative computable fair martingale on output strings with d(empty)=1. For each fixed output length m define a source martingale
[
e_m(\sigma)=2^{|\sigma|}\int_{[\sigma]} d(F(z){\upharpoonright}m)\,d\lambda(z).
]
Equivalently,
[
e_m(\sigma)=2^{|\sigma|-m}\sum_{|\tau|=m}d(\tau)w_\sigma(\tau).
]

Then `e_m` is a uniformly computable nonnegative source martingale with `e_m(empty)=1`.

**Proof.** At fixed m the function `z -> d(F(z)↾m)` is a computable clopen step function, so the displayed integrals are computable rationals. Splitting [sigma] into its two children gives the fair-martingale equation. Finally `e_m(empty)=1` because F preserves fair coin and d has expectation 1 at level m. ∎

If y=F(x), total continuity gives some source prefix rho_m of x on which the first m output bits are fixed to `y↾m`. At that prefix,
[
e_m(\rho_m)=d(y{\upharpoonright}m).
]

Therefore every individual capital peak of a martingale succeeding on y can be reproduced exactly by a computable martingale on the source — but generally by a **different** martingale `e_m` for each stage m.

This is the precise coherence obstruction. Computable randomness forbids one computable martingale from succeeding on x; it does not forbid a uniformly computable sequence of normalized martingales from attaining larger and larger one-off peaks at different source prefixes. A fixed computable convex mixture of the `e_m` cannot be justified from unboundedness of d alone: output success may be arbitrarily slow, so no prescribed summable coefficient schedule is guaranteed to retain unbounded capital. An adaptive threshold/stopping construction would be the natural repair, but its computability again depends on effective hitting probabilities of the kind isolated in Lemma 1.

Thus the conditional-weight issue and the direct-martingale issue are the same effective stopping problem in two forms.

## Lemma 3 — bare k=2 does not force positive persistent sheet weight

There is an exact k=2 map with a genuine double fibre for which one actual sheet has conditional weight tending to zero.

Let `a=0^omega`, `b=1^omega`, and `c=0^omega`. Put `A_0=2^omega`. For m>=1 define
[
P_m=[0^{2m}],\qquad Q_m=[1^m]\setminus[1^m0^m],\qquad A_m=P_m\cup Q_m.
]
Then the `A_m` are nested computable clopen sets,
[
\lambda(A_m)=2^{-2m}+(2^{-m}-2^{-2m})=2^{-m},
]
and their intersection is exactly `{a,b}`.

Let `C_m=A_m\setminus A_{m+1}` and `D_m=[0^m1]`. For every m>=0, `C_m` and `D_m` are clopen and both have measure `2^{-(m+1)}`.

For each m choose uniformly a computable measure-preserving homeomorphism `phi_m:C_m -> D_m`: refine `C_m` to a common cylinder length L_m; because its measure is `2^{-(m+1)}`, it consists of exactly as many length-L_m cylinders as `D_m`; map them lexicographically by same-length prefix replacement and copy the tail.

Define
[
F_{thin}(a)=F_{thin}(b)=c,\qquad F_{thin}(z)=\phi_m(z)\quad(z\in C_m).
]

### Hypothesis checks

1. **Everywhere total computable.** To produce r output bits, decide membership in `A_r`. If z is in `A_r`, the first r output bits are 0. Otherwise some unique m<r has z in `C_m); finite search finds it and `phi_m` supplies the requested output.
2. **Continuous.** The same finite-use argument gives continuity, including at a and b, because points in deeper `A_r` map to longer all-zero output prefixes.
3. **Fair-coin preserving.** The `C_m` partition the source outside the null set `{a,b}`, the `D_m` partition the target outside `{c}`, and each `phi_m` preserves measure.
4. **Fibres.** The fibre over c is exactly `{a,b}`. Every other output lies in one unique `D_m` and has one preimage under `phi_m^{-1}`.
5. **Conditional weight.** For m>=1, `F_thin^{-1}([0^m])=A_m`. With sigma=0,
   [
   w_0(0^m)=2^m\lambda([0]\cap A_m)=2^m\lambda([0^{2m}])=2^{-m}\to0.
   ]
   The other branch has `w_1(0^m)=1-2^{-m}`.

Thus an actual point of a double fibre may have zero limiting conditional sheet mass; k=2 itself supplies no positive persistent-sheet lower bound.

This example is **not** a randomness-destruction witness. The thin point a is computable, hence not computably random. Moreover `F_thin` has an a.e.-computable inverse off c: find the first 1 in the output, identify the shell `D_m`, and apply `phi_m^{-1}`. SRC-0015 / THM-0038 therefore places this example in the positive invariance regime on random points.

The example isolates exactly what remains: source computable randomness would have to rule out membership in a non-effectively controlled zero-weight sheet, not merely rely on the cardinal fibre bound.

## Why the two-prefix lists do not close Lemma 1

At a canonical input precision n, P4-S003 lets one reduce every output cylinder to at most two candidate n-prefixes. Their conditional weights sum to one, but the list gives no computable lower bound for the candidate containing the actual source point. `F_thin` shows that a persistent candidate can carry weights tending to zero.

The missing positive datum is therefore not candidate count. It is an effective statement about **hitting probabilities / stabilization** for the likelihood-ratio process. If the low-weight crossing sets were uniformly Schnorr-effective, source computable randomness would eliminate the zero-weight alternative. No such uniform computation follows from the present list construction.

## Counterexample routes tested and not completed

### SRC-0061 filler completion

The P4-S003 pre-revealed-bet obstruction remains unresolved. No ordinary filler schedule was found that both makes every adaptive scan globally cofinite and preserves the future bets responsible for the known non-conservation witness. Therefore SRC-0061 / THM-0072 is not reused as a k=2 counterexample.

### One-time-pad / masked fillers

A natural repair was to output a relation such as `x_j xor x_r` instead of revealing filler coordinate j outright. This prevents immediate disclosure of either endpoint. The obstruction migrates rather than disappears: if one endpoint is later genuinely queried/revealed, the earlier relation reveals the other endpoint, which may itself be a future betting position. Protecting a single global mask coordinate forever gives a fixed two-sheet ambiguity separated by that coordinate; in the injective-per-sheet case this falls back into P4-S003's positive clopen-sheet theorem. No dynamic masking construction was completed that both preserves the winning simulation and keeps every fibre globally of size at most two.

### Exact randomness-destroying witness

No exact total computable fair-coin-preserving k=2 map with a computably random x and non-computably-random F(x) is established in P4-S004. The asymmetric `F_thin` witness is only a conditional-weight counterexample, not a randomness counterexample.

## Successful and failed mechanisms

Successful in P4-S004:

1. **Likelihood-ratio reduction.** Vanishing conditional sheet weight along a source cylinder yields a uniform effectively open test of measure at most the weight threshold.
2. **Randomness-level calibration.** That estimate is Martin-Löf-test strength; an upgrade to computable crossing measures would make the route Schnorr-effective, which would be enough for a computably random source.
3. **Exact finite-stage martingale lift.** Every fixed output martingale stage has a uniformly computable normalized source martingale attaining exactly the same capital once that output prefix is determined.
4. **Exact zero-weight k=2 example.** `F_thin` satisfies totality, fair-coin preservation and the global two-fibre bound while one actual double-fibre sheet has conditional weight tending to zero.

Failed or incomplete:

1. **Derive a positive persistent-sheet lower bound from source computable randomness.** The available Ville estimate produces an ML test, not a computable-randomness test.
2. **Coherently combine the fixed-stage lifts.** Static mixtures need a growth rate; adaptive stopping needs effective hitting probabilities not supplied by the current data.
3. **Use two-prefix lists to compute the low-weight hitting measure.** No such effectivization is proved.
4. **Repair SRC-0061 with ordinary or masked filler queries.** The pre-revealed-bet problem persists in migrated form.
5. **Construct an exact k=2 computable-randomness destroyer.** None is claimed.

## Proof dependencies and guards

New programme mathematics uses elementary computable clopen measure, conditional pushforward measures, nonnegative martingales/Ville's inequality, DEF-0002, DEF-0004, and the catalogue hierarchy relations REL-0001/REL-0002. The claim that `F_thin` preserves computable randomness uses already-catalogued SRC-0015 / THM-0038 after its a.e.-computable inverse is exhibited. SRC-0061 / THM-0072 is mentioned only as the already-tested unrestricted scan route; no finite-fibre conclusion is imported.

- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- The pre-Phase-4 Gate-3 guard is preserved historically.
- P4-S001, P4-S002 and P4-S003 are unchanged exactly.
- General k=2 forward computable-randomness preservation/failure remains unresolved.
- No result is claimed for k>2.
- DEF-0020 and all source/convention guards are unchanged.
- No novelty/open-status claim is made.
- Gate 4 is not reviewed. Phase 5 remains CLOSED.
