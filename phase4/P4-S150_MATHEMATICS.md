# P4-S150 — All-output conditional balance and limits of two-bank compensation

**ONE owner-invoked internal Phase4 CAND-01 mathematics session, 2026-10-14.** Entry main `249c81e5264ad2d96f134c3607991680c7a543f4`, S149 sole parent `1fb31030ee5efb95f92b27e4f68ae2a4e22f95f0`, tree `f0c9eacadc5650b11c65628e40f379f224813008`, 19 changed paths, PR #49 merged by expected-head direct non-force FF (2026-10-14T19:43:45Z). No competing S150 branch, records or open PR. Actions runs=0, check runs=0, individual status contexts=0: ABSENT_NOT_PASS. Rulesets []; workflow listing UNKNOWN_URL_ALLOWLIST; protection 403 UNKNOWN_403. Same-agent proof, not external verification.

Use 2^omega with fair Bernoulli λ. F_k: total computable globally fair maps with <=k ACTUAL COMPLETE inverse sources for EVERY infinite output. R_k: those x whose image under every F_k observer is CR. S149's rational positive output martingale p=d+1 and arbitrary computable strictly increasing output-use u are assumed. R₃⊆R₂ is immediate; reverse E-00 and strictness S-00 remain OPEN.

## A150.1 — ALL-OUTPUT output-conditioned cancellation, unrestricted computable use (INTERNALLY PROVED)

**Theorem.** For EVERY total computable λ-preserving map G, EVERY total computable strictly increasing u with u(0)=0 whose u(n) input bits fix the first n output bits, EVERY n≥0 and output word τ∈2^n, let S_τ={s∈2^{u(n)}:G([s])⊆[τ]}, Δ=u(n+1)−u(n), and ρ_s=2^(−Δ) #{t∈2^Δ : G([st])⊆[τ1]}. Then
N=|S_τ|=2^(u(n)−n) and Σ_{s∈S_τ}ρ_s=N/2.

**Proof.** The disjoint u(n)-cylinder cover of G⁻¹[τ] is precisely S_τ, hence fairness yields N*2^(−u(n))=2^(−n). At depth u(n+1), the number of source words mapping into [τ1] is exactly 2^(u(n+1)−n−1) by fairness. Partition those words according to their unique earlier s∈S_τ and divide by 2^Δ. This gives Σρ=2^(u(n)−n−1)=N/2 for EVERY τ, including n=0. These finite counts are effectively computable dyadic rationals with no inverse selector or fibre-cap hypothesis. QED.

For p>0 a total rational martingale, set r_b=p(τb)/p(τ)∈(0,2), with r0+r1=2, and A_s=(1−ρ_s)r0+ρ_s r1 =1+(ρ_s−1/2)(r1−r0). The preceding theorem gives exactly
(1/N)ΣA_s=1,
(1/N)Σ(A_s−1)^2=(r1−r0)^2*(1/N)Σ(ρ_s−1/2)^2.
By AM–GM, ∏_{s∈S_τ} A_s≤1. More quantitatively, on 0<t<2 we have log t ≤ (t−1)−(t−1)^2/8: the function log t−(t−1)+(t−1)^2/8 has second derivative −t^(−2)+1/4≤0 and derivative/value zero at t=1. Averaging gives
(1/N)Σ log A_s ≤ −(r1−r0)^2/(8N) Σ(ρ_s−1/2)^2. (A150)
Strict inequality relative to zero is forced by any nonconstant ρ across these cells and a nontrivial r1−r0, but ONE individual cell can still have A_s>1. The inequality is over an output-conditioned POPULATION, not the unknown actual source x. This is stronger arithmetic information than S149's pathwise decomposition but DOES NOT supply a pathwise F₂ observer, and cannot establish R₂=R₃.

## B150 — q=1→2→t two-step local normalizer and multiple-bank no-free-lunch

At a c2 true-two-inverse cone transition q_A=1→2, both children of the sole A source cell take the selected first output bit. The next true output bit selects exactly t∈{1,2,3} of its FOUR source grandchildren. If the next-output rational martingale ratios are r_target,r_sibling (sum 2), the local two-source-bit normalizer is [t*r_target+(4−t)*r_sibling]/4 =1+(t/4−1/2)(r_target−r_sibling). This is **not** the global S_τ average: it conditions additionally on a named local A cone.

For a nonnegative source martingale with parent capital 1, guaranteed capital ≥a on each of the t future target grandchildren and ≥b on the remaining 4−t grandchildren is possible iff t*a+(4−t)*b≤4: necessity follows by summing the four grandchild capitals, sufficiency by allocation and dyadic backward averages. The sum of any finite family of self-financing banks is itself a martingale, so FINITE multiple-bank splitting cannot guarantee both a>1 and b>1. The target-only optimum 4/t has zero fallback. A time-adaptive future strategy might still work; the theorem rejects guaranteed-both-branches financing, NOT all possible globally computable compilers.

All 178 labelled legal rows survive from S146–S147 with counts (q,t) (1,1):40,(1,2):15,(2,1):16,(2,2):36,(2,3):16,(3,2):15,(3,3):40. Symmetric q_B=1 corresponds to q_A=3. This finite row test is NOT all-cylinder global fairness of a new observer and is NOT a <=2 ACTUAL INFINITE fibre cap.

## C150 — Extensive central proof/counterexample attempts and exact failures

**(i) Globally balanced two-bank coupling:** Since Σ_{s∈S_τ}(A_s−1)=0, attaching the same positive gain to EVERY hidden source state violates global funding. One may profit on selected states at the expense of others; selecting the SAME R₂ source's positive debt sequence without knowing its input/output future, actual inverse degree, or effective cone is the FIRST missing E-08 obligation. This population budget does not bar a new global F₂ map exploiting source bits differently.

**(ii) Delayed sentinel and sheet gluing:** Tried to use finite rational ρ to route high-debt states into an F₂ output tree while compensating low-debt states via alternate sentinels. Exact global legalities λ(F⁻¹[σ])=2^(−|σ|) for EVERY σ and |F⁻¹{z}|≤2 for EVERY infinite z do not follow from balanced rows. Recycling a state can create additional infinite inverse paths; discarding it can misprice sibling cylinders. No total computable F satisfying both was produced. S135 globally fair degree3/degree2 oscillator refutes static sheet-state inference; S141 benign fat folds refute folding⇒destruction.

**(iii) Stopped-excursion reserve and charts:** Every finite ρ is computable, but an infinite hitting price λ(B∩G⁻¹{d reaches 2^(4k) eventually}) is only left-c.e. generally. S145–S147 show a CR bad-image source cannot admit uniformly computable local exact stopped prices along any computable unbounded threshold subsequence. S011 F₂ CR destroyer already has this obstruction. Thus finite rational ρ does NOT pay a global stopping event; FIRST missing algorithm is a computably priced clopen/open subevent scheme capturing the SAME x, or a proof avoiding stopping prices entirely.

**(iv) Arbitrary-use E-00 and one-source S-00:** A150 holds for unrestricted u, but no additive-use reduction or F₂(R₂) closure is proved. The E-08 universal SAME-SOURCE observer construction is not supplied, hence E-00 OPEN. S-00 requires a single total fair complete-cap-three G, total rational output d and ONE x∈R₂ with d(G(x)) unbounded. No R₂ survivor was constructed; conull R₂ cannot be intersected with the null d-success preimage as proof of existence. The latter is a quantifier error, not merely a missing estimate.

## D150 — All-output hostile controls, distinctions and audit

- **Identity** H(x)=x is a total computable fair degree-one homeomorphism, exactly one complete inverse over EVERY output, CR conserving. Choose the valid OVERREAD schedule u(0)=0, u(n)=n+1 for n≥1. For n≥1, x|u(n) already determines the next output bit, so ρ∈{0,1} and Σ|ρ−1/2| diverges on EVERY x, including all CR x. Thus 'divergent local bias ⇒ bad image' is FALSE by a fully legal all-output map, not merely a finite-row counterexample. Its conditional output-population balance A150 still holds.
- **Adjacent swap** is a globally fair degree-one computable homeomorphism preserving CR, with infinitely many source-forced output rows on its natural additive clock.
- **S011** is a globally fair F₂ destroying a genuine CR source Y, but Y is NOT known to be in R₂. Thus A150 cannot imply blanket F₂ preservation.
- **S135** globally fair 3:1↔2:2 oscillator conserves CR; **S141** dense positive folded pockets can coexist with R₂ sources and CR conservation. Pure sheet counts/variance are not enough.
- **Finite sanity**: EXACT Python Fraction checks of the six named example maps, output-prefix mass and factor balance, squared deviations, products, all 178 row-count/bank-floor configurations: 8,532 assertions PASS FINITE SANITY ONLY. No independent proof, CI, formalisation or all-output fibre verification of newly proposed maps.

**Result:** A150.1 exact per-output-prefix hidden-population balance, second moment and negative log drift INTERNALLY PROVED; B150 exact multiple-bank finite capacity, with four failed/blocked global strategies isolated. NO globally legal new F₂ detector, R₂ survivor, E-08/E-00 or S-00. R₂=R₃ and strictness UNRESOLVED. Historical S101–S103 A–C, Y/M/H/X, DEF-0020, PA-0001, source grades and gates remain frozen.