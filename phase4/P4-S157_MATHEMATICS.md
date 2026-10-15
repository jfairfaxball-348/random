# P4-S157 — variable-cutoff inverse kernel and savings theorem

15 October 2026. Exactly one owner-invoked Phase4 CAND-01 mathematics session. LIVE entry main 1becd4095f553d468c1253d6ee72dd953e872ec3, tree 43e2b2662428c88034f750404932ee31c7e4c7cb, actual S156 one-parent commit parent e7ccfef78f78ae2b1adef4e5f9a8a647ecd6c62d and merged PR #56. Open PRs/competing S157 none; workflow runs/check-runs/status contexts all [] = ABSENT_NOT_PASS; rulesets []; protection 403 UNKNOWN. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED. S101–S103 A–C, original Y/M/H/X, DEF-0020/PA-0001 and source grades frozen. No external mathematical verification.

X=2^ω, λ fair coin, CR ordinary total nonnegative rational computable-martingale randomness. F_k: ALL total computable λ-preserving G with at most k ACTUAL COMPLETE inverse points above EVERY infinite output; R_k={x:∀G∈F_k, G(x)∈CR}. Write q_s(τ)=2^|τ| λ([s]∩G⁻¹[τ]). G is total computable, globally fair with a GIVEN total computable common source-use bound u(m) for m output bits. q_s(τ) is EXACT computable rational from finite source depth max(|s|,u(|τ|)). For all τ, q_ε(τ)=1, q_s=q_s0+q_s1 and q_s(τ0)+q_s(τ1)=2q_s(τ). A total computable Cantor map has some effective common modulus by finite compactness under its promised totality; we do NOT assume it is additive.

## A157.1 — exact rational savings (INTERNALLY PROVED)

For EVERY total nonnegative rational computable output martingale d put p=d+1, a strictly positive rational martingale, and p0=p(ε). For k≥1 let p^[k](τ) be p evaluated at the EARLIEST prefix of τ where p≥2^k p0, or p(τ) if no such prefix exists. Each p^[k] is a total rational stopped martingale. Define
  D(τ)=p0⁻¹ Σ_{k≥1}2^{-k}p^[k](τ).
For any fixed τ compute K≥1 with 2^K>max_{ρ≼τ}p(ρ)/p0. Then
  D(τ)=p0⁻¹(Σ_{k=1}^K2^{-k}p^[k](τ)+2^{-K}p(τ)),
since the whole k>K tail is unstopped. This is a TERMINATING EXACT rational algorithm, D(ε)=1, and termwise nonnegative martingale fairness gives D(τ0)+D(τ1)=2D(τ). If limsup_m d(y↾m)=∞, EVERY threshold k is eventually hit, and its stopped contribution 2^{-k}p^[k]/p0 remains ≥1 forever. Thus D(y↾m)→∞ without knowing any growth rate, threshold hitting time or infinity-oracle.

## A157.2 — globally effective variable-cutoff projective kernel (INTERNALLY PROVED, CONDITIONAL)

**EVCS:** a GIVEN total computable function M on ALL finite source words s, M(s)≥|s|, satisfies for EVERY finite s, EVERY output word τ with |τ|≥M(s), and EVERY finite continuation v,
  q_s(τv)=q_s(τ).
Neither existence nor computability of this last-change cutoff is inferred from G or from the number of its true fibres. M(s)−|s| need not have a fixed uniform bound.

For each infinite output z set κ_z([s])=q_s(z↾M(s)). EVCS makes κ_z([s]) locally constant with a GIVEN effective modulus. It is projective for EVERY z: κ_z(ε)=1; at any common depth m≥max(M(s),M(s0),M(s1)), q_s(z↾m)=q_s0(z↾m)+q_s1(z↾m), and EVCS identifies each with its κ value. Nonnegative consistent cylinder masses define a source probability measure κ_z. If z∉G([s]), compactness separates z from compact G([s]) at a finite output depth; q_s there is zero and stays zero, so κ_z([s])=0. Thus κ_z is supported on the ACTUAL complete inverse fibre without selecting, numbering or computing its cardinality.

Let μ_D[τ]=2^{-|τ|}D(τ), a computable probability measure on outputs. Construct one SOURCE function for EVERY finite s:
  η([s])=∫κ_z([s])dμ_D(z)
       =Σ_{|τ|=M(s)}q_s(τ)2^{-M(s)}D(τ);
  e(s)=2^{|s|}η([s]).
The displayed finite sum is an EXACT total rational algorithm using G,u,M,d. Projectivity of κ gives η(ε)=1, η([s])=η([s0])+η([s1]), hence e(ε)=1 and e(s0)+e(s1)=2e(s). It is ONE globally total rational nonnegative martingale, not a list of output tests or noncomputable limiting martingale.

**Full path inequality:** Fix ANY x and n; let s=x↾n, m=M(s), y=G(x), L=max(n,u(m)). The source cylinder [x↾L] is contained in [s]∩G⁻¹[y↾m]. Consequently q_s(y↾m)≥2^{m-L}. EVCS makes κ_z([s])=q_s(y↾m) on EVERY z∈[y↾m], not merely at y. Therefore
  e(x↾n)≥2^n·2^{m-L}μ_D([y↾m])
           =2^{n-L}D(y↾m)
           =2^{-(u(M(x↾n))−n)_+}D(G(x)↾M(x↾n)).
No ACTUAL-fibre-cap assumption appears in this inequality. If some finite B bounds the positive price (u(M(x↾n))−n)_+ at INFINITELY MANY n, and d succeeds on y, then M(x↾n)≥n→∞ on these n and D(y↾m)→∞ by savings. Thus e succeeds on the SAME x. Identity is a globally fair exactly-ONE-inverse observer, so a legal F₂/e compiler in this CONDITIONAL case.

**Necessary condition for a hypothetical bad CR x:** Under any GIVEN valid EVCS schedule M for G, if x∈CR and G(x)∉CR, then (u(M(x↾n))−n)_+→∞; otherwise infinitely many bounded-price n and e would contradict CR. This says neither that an arbitrary F₃ has such M nor that an expensive valid M causes bad images. Adding computable slack can arbitrarily inflate M even for a benign identity.

For additive use c choose u(m)=m+c. The price becomes M(s)−|s|+c. S156's CLS(c,h) takes M(s)=|s|+h (fixed globally); EVCS instead allows arbitrarily large prefix-dependent lag, provided some B bounds it infinitely often on the source under consideration. A saving transformation is ESSENTIAL: an unsaved output martingale could have all its unbounded spikes between the cheap levels. Strong savings does not pay a diverging predetermined price.

## A157.3 — infinite counterexample to NEED for fixed CLS lag (INTERNALLY PROVED)

Partition N into successive computable blocks B_j of lengths ℓ_j=j+2, endpoints a_0=0 and a_{j+1}=a_j+ℓ_j. In each block rotate source coordinates LEFT once: output[a_j,...,a_{j+1}−1]=(input[a_j+1],...,input[a_{j+1}−1],input[a_j]). This is a computable permutation of all independent bits, hence a total fair degree-ONE computable HOMEOMORPHISM with effective inverse on every output. First m output bits depend on fewer than m+1 source bits, so u(m)=m+1 is a valid additive-one bound.

Let M(s)=the least block endpoint ≥|s|, and M(ε)=0. Given any τ of depth ≥M(s), inverting completed output blocks determines ALL input bits before |s|. Thus q_s(τ) equals 0 or 1 according to that recovered prefix and stays identical under ALL continuations: EVCS holds. Yet sup_s(M(s)−|s|)=∞: for s length a_j+1, the just-read input bit x(a_j) is not exposed in output until a_{j+1}−1. At shorter output depths compatible with the preceding blocks its conditional q is 1/2 and subsequently splits into 0/1; so NO fixed h satisfies S156 CLS(1,h) for all s. At every infinite sequence's infinitely many block endpoints n=a_j, M(x↾n)=n and the use price is 1. Therefore A157.2 applies to ALL CR x. This example is degree ONE and NOT a three-fibre separator, but proves the new sufficient condition strictly extends S156.

## B. Full-space hostile audits

* q=1→2→t and 3→2→t are finite FOUR-aligned-cell budgets, not true inverse cardinalities or globally computable last-change data. The sharp simultaneous target/sibling payoff constraint remains t*a+(4−t)*b≤4. No repeated unlimited target-only bet.
* S135's 3:1↔2:2 tagged source cone has q_s(y↾m) oscillating 3/4↔1/2 at arbitrarily late m along exceptional infinite output y in the effective-null T. Thus NO all-output EVCS M(s) exists for this s. Both full inverse source paths into T already fail CR; it is not an R₂ separator.
* S117 paired reservoirs / S129 eventual balanced or one-surplus geometry cannot supply a COMPUTABLE all-output last-change cutoff. S141 harmless positive folds falsify naive inference from local ambiguity to destruction. S155 P_A has M(s)=|s| despite noncomputable measure of multiplicity-two locus; no such locus is queried by the compiler. S005/S006 noncomputable infinite stopping prices remain relevant to other methods.
* S011's adaptive F₂ destroys CR on Y, so Y∉R₂, and it is not additive use. A157.2 applies to arbitrary computable use ONLY with a global given EVCS cutoff and cheap-price recurrence; S011 supplies no such certificate at the destroyed source. No implication about whether it possesses any expensive global cutoff.
* Only on-y eventual stabilization does NOT provide the whole-output projectivity or rational source-martingale algorithm. No uniform exact cutoff follows merely from all fibers having ≤3 actual points. A computable unbounded h(n) cannot be financed against arbitrary slow winnings by savings alone.

## C. Central equality and strictness: direct ATTEMPTS FAILED

For a hypothetical globally fair additive-two F₃ G, one x∈R₂, y=G(x) nonCR and exactly two ACTUAL inverses, the theorem would contradict x∈CR IF G had a computable all-output M with recurring bounded price on this x. Neither premise is forced by G's fibre cap: S135 already refutes universal effective cutoff, and S157 does not construct an F₂ output-observer compiler from q oscillations. The exact finite-cell transitions provide no indefinite complete-sheet selector with all-output F₂ legality. Arbitrary-use E-00 is only covered CONDITIONALLY by an explicitly supplied u and M, not reduced to E-08. For strictness we still have NO SINGLE x surviving ALL legal F₂ maps together with a legal fair F₃ and rational winner. Partial map programs are not an enumeration of globally total fair capped maps; ∀F₂∃x_F ≠ ∃x∀F₂. The S011 Y is CR but NOT R₂.

**Outcome:** Two infinite scoped internal results A157.1–A157.3; no full E-08, E-00, S-00, R₂=R₃, strictness, R₂=MLR, formal proof, novelty upgrade or publication. Gate3 PASS; Gate4 NOT REVIEWED; Phase4 OPEN; Phase5 CLOSED. Local finite script SANITY ONLY, hosted CI ABSENT_NOT_PASS and protection UNKNOWN_403.
