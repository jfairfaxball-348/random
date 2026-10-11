# P4-S091 — Mixed constraints: a bounded-concentration obstruction and its sharp limit

Date: 2026-10-10. Phase 4 Mathematics ONLY; selected CAND-01.
Incoming remote main: `971b3ccef56fc5654c857a32e882342c80e325c2`.
Parent: `560f8a1e16a69aaf98a6b8328bfc893b09398d30`.

**Disposition: Route (I), PARTIAL. R₂ versus MLR is NOT decided.**

The global attack was to remove S090's free-control assumption from a readable-neutralization obstruction, then use the resulting observer against a proposed full-R₂ potential construction. Theorem 4 does this for precisely specified mixed affine guessed runs whose control marginals have uniformly bounded density. It constructs a single observer from the run program, independently of the true guess branch or its density bound, and forces unbounded conditional expected capital on every qualifying branch. Corollary 5 applies to the EXACT K_mix and K′_mix frames. It excludes a full-R₂ bounded-potential construction of this type whenever either projection defect remains bounded.

The decisive unrestricted obligation is NOT closed: unbounded projection concentration can absorb the exponentially small stall events. Section 6 realizes this amplification in the actual recurrences, with mixed equations and in both frames. These finite countermodels are not CR witnesses. No universal destruction of CR∖MLR, no R₂ survivor, and no general impossibility for arbitrary clopen guessed runs follows.

This session's result is a quantified obstruction to a class of global construction programs, not another fixed-frame randomness-class separation. It adds no inclusion to the frozen landscape.

## 0. Entry, review and S090 challenge

Independent GitHub reads of `git/ref/heads/main` and `branches/main` agree on the incoming SHA. Git commit and REST commit metadata agree on its sole parent. S090's close identifies its outgoing checkpoint as its own atomic close commit; the observed message, changed-file list, tree and parent identify that commit exactly. No intervening main commit. The recursive tree is complete, contains no S091 file or tracked workflow, and the session-branch search finds no S091 branch. Open PRs: none. Hosted runs for the pinned SHA: zero. Branch metadata reports no enforced required checks. The workflow-collection endpoint rejects the query; no conclusion is drawn from that rejection. No hosted CI success is claimed.

Reviewed repository authority, SESSION_PROTOCOL, CAND-01, Gate-3 PASS, both pivots, cumulative S001–S090 outcomes and emphasized theorem statements. Detailed dependencies are S082's potential/savings/compactness and §6.3, S083's class separation, S084's predictable errors, S087 §6.2, S088's affine states and exact two frames, and S089/S090 mathematics, validation, close and audit. This is not a claim to re-prove all historical mathematics.

S090 was checked adversarially before use: positive-density stage pools; Σ⁰₁ finite searches; separated data supports; the conditional quarter bound and tower estimate without independent trials; a stall cover relative to validity, unavailable to the observer; relative false-reading bounds at every later true state; 27/8 compactness margin; and singleton destruction only at the selected witness. Its exact audit passes 92,802 checks again. S088 passes 92,724. S089 exact Parts 1–5 pass 143,911, with `--no-numeric`; no spectral experiment was run. No flaw requiring a change to S090 was found.

Source access is unchanged: SRC-0015, SRC-0019, SRC-0060, SRC-0069, SRC-0071 STATEMENT_INSPECTED with previously recorded particular proof inspections; SRC-0070 and SRC-0072 ABSTRACT_INSPECTED. SRC-0071's journal version remains METADATA_ONLY. No external literature retrieval or access promotion. R_tot=MLR is still the S083 programme deduction from the inspected preprint.

## 1. Projection concentration of a mixed affine state

Write a_j=x_{2j}, b_j=x_{2j+1}. In a finite window let a,b each have n coordinates. A nonempty affine state has the form

  P={ (a,b): A a ⊕ B b = c },

where the combined matrix [A B] has row rank r. Redundant equations can first be removed. Define

  d_a(P)=r−rank(B),   d_b(P)=r−rank(A).

These are the codimensions of the projections onto a and b, respectively, rather than the total codimension r of P.

**Lemma 1 (exact marginal density).** There is an affine a-subspace Q_a of codimension d_a such that

  dλ(a | P)/dλ_a = 2^{d_a}·1_{Q_a}.

The analogous formula holds for b with d_b. In particular, for every control-only Borel event E,

  λ(E | P) ≤ 2^{d_a(P)} λ_a(E).                         (1)

Both defects are nondecreasing when independent affine constraints are added to a nested state.

*Proof.* For fixed a, solvability is equivalent to Aa⊕c∈im B. The induced map a↦Aa modulo im B has rank r−rank B because [A B] has rank r. This gives Q_a. For each admissible a there are exactly 2^{n−rank B} data solutions. Normalize by λ(P)=2^{−r}. Adding one independent row increases r by one and rank B by zero or one, and similarly for A. ∎

Thus mixed equations need not destroy the free-control marginal: independent equations a_j⊕b_j=c_j have d_a=d_b=0. Auxiliary equations can make either defect positive. The theorem below allows positive defects; it does not assume either marginal is fair.

## 2. Precisely quantified class of programs under attack

Fix a partial computable, prefix-coherent binary-guess run program R. A completed run of length m≥1 emits a nonempty clopen affine state P^ε_m and exactly m(m+1) labelled **readout equations**

  ℓ_l(a,b):=α_l·a ⊕ β_l·b = c_l.                       (2)

It may impose additional affine equations. A finite output provides the entire finite support and all equation values. Impose these explicit syntactic requirements:

* Each β_l is nonzero. Its support J_l is disjoint from all other data readout supports on that run, with min J_{l+1}≥max J_l+2. For the two-frame corollary, impose the same requirement on the nonzero α_l supports as well.
* Every equation imposed at stage i, INCLUDING auxiliary equations, uses only raw coordinate pairs indexed by the disjoint computable stage pool D_{ε↾(i+1)} of S090 §1. Its full support is above every earlier stage's full support. Readout spacing within a stage is also enforced. The pools' positive density is not needed for the obstruction; it is relevant only if a proposed survivor search uses S088 dispersal inside them.
* Runs agree through each common guess prefix. Every state retains its earlier constraints and entails all its labelled readouts. Malformed finite outputs are rejected before they are used by an observer.

These requirements are effective finite checks. No totality, validity-oracle computability, or successful search on wrong guesses is assumed. A **true branch** ξ is any infinite guess sequence on which every stage completes; write P_i for its state after i stages, i≥1, and S=⋂_i P_i.

**Lemma 2 (class compatibility under arbitrary marginal bias).** Fix a true state P_i and an entire control assignment a admissible for it. For a completed run, each readout is either an identical equation entailed by P_i or has its entire support disjoint from all constraints of P_i. The data parities of any collection of the latter readouts are independent fair bits conditional on a and P_i.

*Proof.* Before the first guess disagreement, shared stages have identical output. Afterwards their pools are disjoint. Readouts from future shared-branch stages lie beyond all supports in P_i. If the selected readouts are unshared, their nonzero, disjoint data supports are unconstrained by P_i. Conditional on a, the other data coordinates remain independent fair bits. Auxiliary equations in P_i cause no exception because their supports obey the same pool and stage restrictions. ∎

Every P^ε_m has measure at most 2^{−m(m+1)}: the readouts are independent equations because their data supports are disjoint. Their completed-run unions form a uniformly c.e. ML test of measure at most 2^{−m²}. Consequently S∩MLR=∅. This nullity is an assumption-compatible consequence, not a survivor certificate.

## 3. Two exact self-reading observers and repeated false readings

For the first frame use precisely

  (K_mix x)_{2j}=a_j,
  (K_mix x)_{2j+1}=b_j⊕b_{j−2}⊕(1⊕a_j)b_{j−1}.

At a held virtual data bit 2q+1, the two raw data candidates differ by δ_j=0 for j<q, δ_q=1 and

  δ_j=δ_{j−2}⊕(1⊕a_j)δ_{j−1}  (j>q).                 (3)

A readout (2) separates them exactly when s_l=β_l·δ=1. Its control term cancels. With the held virtual bit set to zero, compute the inverse candidate b^(0). A separating equation predicts

  ν_l=c_l⊕α_l·a⊕β_l·b^(0).                            (4)

The observer R↦T_R^a is S090 §4 with (4) replacing its data-only prediction: bounded simulations of all finite guesses; require the WHOLE completed run's full support below the read frontier; select the first r(q,m)=q+2m+4 separating readouts whose data supports lie above q; resolve the held bit only when all their predictions agree. Otherwise read the next filler at zero stake. After a resolution, advance to the next unread odd data coordinate, genuinely reading an intervening even control at zero stake. A resolution bets all-in on ν; d_R^a starts at 1.

For the second frame retain the offset in the committed definition:

  (K′_mix x)_{2j+1}=b_j,
  (K′_mix x)_{2j}=a_j⊕a_{j−2}⊕(1⊕b_{j−1})a_{j−1},

with b_{−1}=a_{−1}=a_{−2}=0. This is NOT the same-index control swap. Hold virtual coordinate 2q; the raw a-difference satisfies

  δ′_j=δ′_{j−2}⊕(1⊕b_{j−1})δ′_{j−1}.                 (5)

Use α_l·δ′ for separation and predict c_l⊕β_l·b⊕α_l·a^(0). T_R^b initially holds virtual coordinate 0 and fills from 1; after a resolution it holds the next even coordinate, genuinely reading an intervening odd control if needed.

**Lemma 3 (legality, stalls and false readings).**

(a) Each T_R^f is total computable, no-repeat, and leaves at most one coordinate unread on EVERY infinite transcript. Each d_R^f is total rational computable and fair. Hence

  G_R^a=F_{T_R^a}∘K_mix∈F₂,   G_R^b=F_{T_R^b}∘K′_mix∈F₂.

The second statement uses the α support requirement of §2. The maps are determined by R alone, not ξ or a marginal-density bound. Self-reference does not change totality because all run simulations are bounded.

(b) Under the unconditioned fair control measure, L readout supports above a hold, ordered and spaced as in §2, satisfy

  Pr(fewer than r separate) ≤ 2^r(7/8)^L.               (6)

For K_mix use the S090 conditional quarter proof with the control filtration through the previous maximum data support. For K′_mix use the filtration through the previous maximum a support MINUS ONE. The fresh controls in its final two transitions are b_{p−2},b_{p−1}. With that offset, the same quarter bound and tower calculation apply. No independent separation indicators are assumed.

(c) Let W_f be the set where T_R^f ever predicts incorrectly, including errors after any earlier false reading. It is unrelativized effectively open and, for EVERY true state, regardless of its marginal bias,

  λ(W_f | P_i) ≤ 1/8.                                 (7)

*Proof of (a).* All next-query operations are bounded simulations and finite calculations. On a permanent last hold, fillers exhaust all other coordinates. Infinitely many increasing holds exhaust all coordinates. No query repeats. Before each read the wager is known, with fair children d,d on fillers and 0,2d at predictions. S008's scan-fibre formula gives ≤2 globally; composition with the exact fair homeomorphisms preserves it. This is an infinitely resolving potential destroyer, not a fixed-hold CR-preserving core.

*Proof of (c).* Condition on the ENTIRE unchanged control sequence. The list of separating readouts of a fixed completed run is now fixed. On each selected equation, (4) is correct iff that equation holds at the actual input; thus an incorrect agreed prediction makes all r equations false. A shared equation makes this event impossible. Otherwise Lemma 2 makes its probability 2^{−r} under the conditional data measure. Integrate against the actual, possibly biased control law, then union-bound over EVERY q,m and all 2^m guesses:

  Σ_{q≥0,m≥1}2^m2^{−q−2m−4}=1/8.

This does not condition on which guessed run wins an entry race. The event includes ANY wrong prediction over the entire scan, so repeated false readings are handled together. An earlier error does not invalidate later scan legality. ∎

## 4. The global obstruction with bounded projection concentration

**Theorem 4.** Fix any R satisfying §2's K_mix requirements. On EVERY true branch ξ for which

  sup_i d_a(P_i)≤D<∞,                                 (8)

the one computable strategy (G_R^a,d_R^a) of §3 has unbounded conditional expected capital along its states. More precisely, with d̄ its S082 savings transform, for EVERY K>2 and EVERY i₀ there are j≥i₀ and t such that

  E_λ[d̄(G_R^a(x)↾t) | P_j] > (27/32)(K−2).           (9)

The same holds for its original all-in martingale, with the lower bound (27/32)K. The analogous theorem for K′_mix assumes the α certificate layout and sup_i d_b(P_i)<∞.

*Proof.* Choose an integer D satisfying (8); it is used only here, not by T_R^a. For each q choose m_q by a rational search such that L₀=m_q(m_q+1)−q−1≥0 and

  2^D·2^{r(q,m_q)}(7/8)^{L₀}≤2^{−q−6}.               (10)

Quadratic L₀ and linear r ensure termination. From the true length-m_q run define H_q as the control-only clopen event that fewer than r(q,m_q) of its readouts above q separate. At most q+1 readouts have minimum data index ≤q. Thus (6), (1) and (10) give, uniformly over EVERY true state, λ(H_q | P_i)≤2^{−q−6}. For H=⋃_q H_q,

  λ(H | P_i)≤1/32,   λ(H∪W_a | P_i)≤5/32.             (11)

H is open and c.e. relative to ξ. It is not claimed unrelativized effective. The observer never uses H, ξ, D, or the true m_q run.

Every x∈S∖H has every hold resolved: if a hold persisted, its true m_q run would eventually finish, its full finite support would enter the filler frontier, and its correct separating predictions would qualify. Every x∈S∖(H∪W_a) therefore has infinitely many correct resolutions. On these points d_R^a doubles infinitely often; d̄ is unbounded too. Their destructive fibres are singleton. They are NOT automatically CR points.

For fixed K let O_K={x:∃t d̄(G_R^a(x)↾t)>K}, an effectively open set. Then S⊆H∪W_a∪O_K. Compactness of the nested nonempty P_i gives some P_j⊆H∪W_a∪O_K, j≥i₀, and a finite subcover. Take t beyond the finitely many capital-witness times. On P_j∖(H∪W_a), the savings drop bound gives d̄(G_R^a(x)↾t)>K−2. This region has relative measure at least 27/32 by (11). Nonnegativity gives (9). For the original all-in d, it is nondecreasing on the complement of W_a, so the same finite-subcover argument gives the stronger K bound. The proof for K′_mix uses d_b and (5). ∎

**Quantifiers.** The observer is uniform in R. The estimates hold on every qualifying true branch, even if its bound D is not known effectively and different branches have different bounds. They do not cover a branch with unbounded projection defects, a run without the certificate/pool layout, or all CR∖MLR inputs.

## 5. Immediate application to the full-R₂ survivor attempt

**Corollary 5 (mixed-run potential no-go).** A program satisfying §2 cannot have all true stages complete, bounded d_a, and a finite strategy-specific conditional-capital bound, uniform over all sufficiently late states and times, for EACH computable F₂ savings strategy along that true branch. The same holds with bounded d_b and the second certificate layout. In particular the standard invariant Φ(P_i,τ_i)<2, with every valid F₂ savings strategy eventually carrying a fixed positive weight, cannot hold under these hypotheses: domination and time monotonicity bound (9) by 2/w once its strategy is active, a contradiction.

For programs supplying certificates in BOTH exact frames, any such full-family bounded-potential proof must have

  d_a(P_i)→∞ AND d_b(P_i)→∞,                           (12)

or leave the stated layout. Lemma 1 gives monotonicity. CDZ₂ observers may be included in the intended family; including them does not remove this obstruction because G_R^a and G_R^b are F₂ strategies with global legal transcripts. We do not assert that a program with (12) exists or survives either reader, much less every F₂ map.

This is the direct application of the session's theorem to the overriding target. It rules out a definite mixed-constraint route to R₂∖MLR; it does not rule out a point of R₂ in the limit set merely from unbounded conditional expectations. A thin survivor may lie in H or W, and an alternative selection argument may use a different invariant. S084's full CR error-stream requirement still applies to that point; inserting one error is insufficient.

## 6. Decisive obligation that failed: unbounded concentration

The attempted extension of (11) without (8) fails. Formula (1) has factor 2^{d_a(P_i)}. An absolute estimate, even an exponentially small one, gives no uniform relative estimate when d_a grows. This is exactly where S082 §6.3/S087 §6.2 concentration reappears; neither absolute neutralization summability nor a Σ⁰₁ search bounds that factor.

**Proposition 6 (sharp actual-frame amplification).** Hold q=0 in K_mix, and take readout supports J_l={2l+1}, 0≤l<L. The control event

  E_L={a_1=a_3=⋯=a_{2L−1}=1}

has measure 2^{−L} and makes every δ_{2l+1} zero. Impose the mixed readouts a_{2l+1}⊕b_{2l+1}=0 and the auxiliary controls a_{2l+1}=1. The resulting affine P_L has r=2L, rank B=L, d_a=L, and λ(E_L | P_L)=1. Thus the factor 2^{d_a} in (1) is attained exactly, and all L mixed readouts fail to separate the hold.

For the EXACT K′_mix offset, E′_L={b_0=b_2=⋯=b_{2L−2}=1} makes every δ′_{2l+1} zero. Impose the same mixed readouts and these auxiliary b constraints. Then r=2L, rank A=L, d_b=L, and λ(E′_L | P′_L)=1. These are sharp one-frame examples. To stall both sets of readouts simultaneously, impose the readouts, all these odd a constraints, and all these even b constraints. Its ranks are r=3L, rank B=2L, rank A=L, hence d_a=L,d_b=2L. Both holds see no separating certificate.

*Proof.* With δ_0=1 and δ_{−1}=0, each coefficient at an odd j is zero on E_L. Induction gives δ_even=1 and δ_odd=0. The K′ recurrence has coefficient 1⊕b_{j−1}, so its odd steps vanish on E′_L. The equations and ranks are on distinct coordinates; the readouts force odd b=odd a. The displayed probabilities and ranks follow directly. ∎

These are finite conditioning countermodels. Their simple infinite extension forces computably identifiable bits and is not CR. They do NOT construct an R₂ survivor or refute universal readability on CR sources. They prove that the measure step needed by the proposed unrestricted obstruction does not follow from mixedness, spacing, or small absolute stalls alone. The class-pool geometry is not used to claim these examples are complete true branches of a survivor program.

No effective neutralization accounting useful after unrestricted conditioning was obtained. No theorem orienting arbitrary ML-test entry races was obtained. No inference from Conjecture R or its experiments was made. No spectral numerics, local frustration, operator-only reformulation or forbidden detour was used.

## 7. Disposition and guards

Proved: Lemmas 1–3; Theorem 4, a global conditional-capital obstruction for the precisely specified mixed programs with uniformly bounded projection defect; its two-frame potential application, Corollary 5; and the sharp finite amplification countermodels, Proposition 6. All infinitary statements rest on the written proof; finite checks are supplemental.

Not proved: R₂=MLR; z∈R₂∖MLR; survival of the two-frame union; an unrestricted readable-neutralization impossibility; coverage of every CR∖MLR source by any family; a useful absolute-accounting construction; Conjecture R. R₂ versus OH^iso and the original U(H), X∈OH and fixed-S questions remain separate.

The entire incoming strengthened landscape, S084–S090 results, original CR Y, unchanged globally use-clipped self-avoiding wtt M, repeated H with A=[101;110;111], X=H⁻¹(Y), PA-0001 and DEF-0020 are unchanged. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No novelty, external openness, priority, publication or outreach claim. Owner/external blocker: NONE.

Next: P4-S092 must attack the unbounded-concentration frontier or either full R₂ alternative, with actual control of both self-readers and entire error streams. No more bounded-defect variants as a substitute for that decisive obligation.
