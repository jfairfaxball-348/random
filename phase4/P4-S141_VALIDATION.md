# P4-S141 — hostile proof and engineering validation
Status: SAME-AGENT INTERNAL proof audit, not Lean, Palomar, independent review or hosted CI.

### A141 source correctness
- Rute arXiv:1203.5535v4 (22 April 2015) §§2,7: original Theorem 7.11 explicitly concerns computable probability spaces and computably random points, including measures having null basic cylinders (caveat at §2); Proposition 7.6 is the *effective exceptional domain* check, not an assertion that every fair morphism preserves CR. The conditional restriction becomes an a.e *isomorphism* only on its conull singleton μ_B inverse locus.
- Finite computable clopen B has λ(B)>0 rational; λ_B=λ(·∩B)/λ(B) and μ_B([τ]) are computable rational cylinder measures. Crucially B need NOT have measure 2⁻ℓ: there may be NO finite equal-cell fair-Cantor homeomorphism onto B. Instead, at an N-cylinder σ⊂B every descendant λ_B conditional split is exactly fair, so a λ_B-martingale winning on CR x∈[σ] would yield a total rational λ-martingale by zero outside σ and parent averaging. Thus x∈CR_λ implies x∈CR_{λ_B}. No computable membership test for an effectively closed or Borel chart is assumed.
- J is PARTIAL on an effective Π² singleton-fibre domain relative to B, not claimed total. Its inverse identities are between λ_B and μ_B (NOT λ and μ_B), with μ_B-null inaccessible outputs omitted. Rute applies to full-measure partial inverse identities, not an arbitrary many-to-one morphism.
- For ordinary fair λ witness d define ν[τ]=2⁻|τ|d(τ). At μ_B-positive parent the missing ν mass on μ_B-null child is δ≥0. The displayed reserve allocation makes a nonnegative TOTAL rational μ_B martingale, including μ_B-zero subtrees, and it dominates ν[τ]/μ_B[τ] along every μ_B-positive prefix. Domination μ_B≤λ/λ(B), rather than a lower bound on density, gives martingale success. No inference μ_B-random⇒λ-random without this explicit calculation.
- Theorem A141 applies for every total computable globally fair G, including arbitrary input use and unbounded fibres, but ONLY conditional almost-everywhere singleton G|B. This does not say all F₃ observers preserve CR and cannot encompass S011 F₂ destructive examples.

### A141.2 bi-local quantifiers
For **every** s≺x, τ≺G(x), set B=[s]∩G⁻¹[τ], which is nonempty *clopen*, and apply contrapositive A141.1. The ambiguity must occur among **two inputs inside B**, not simply a second inverse elsewhere. μ_B(ambiguity)>0 implies some finite pair incompatible u,v⊂B has positive μ_B overlap and hence positive λ overlap by global domination. Pure positive λ overlap would NOT conversely imply positive μ_B overlap. Existence of pair is not an effective price-lower-bound procedure.

### B141 pocket countermodel hostile audit
- Algorithm stage j checks exactly whether finite earlier pockets cover [σ_j], not whether σ_j meets the infinite future set K. If uncovered, a free *clopen* subcylinder exists and can be chosen at arbitrarily large desired depth. Stage length ≥j+4, all pockets prefix-free and budget Σ2⁻(j+4)=1/8; density from visiting every σ_j.
- At input x∈K, evaluating P(x) requires no Π¹ membership decision: prefixes of length n can only be affected by pocket of length <n, necessarily found among finitely many stages j<n. Use n+1 suffices. This establishes *total computability on K* and everywhere, not just a.e.
- Each pocket maps ONTO ITSELF under local conditional one-bit shift; K maps identically to K. Therefore no cross-pocket inverse, exactly two inside each pocket, exactly one on K, λ-preserving all cylinders and Borel sets. Not a local row-only fictional map.
- For every x∈K and its source/output prefixes, a pocket lies in their intersection, hence provides positive internal μ_B-mass of double fibres. K≥7/8 positive measure, nowhere dense, with actual MLR/R₂ points. P fixes those points; neighbourhood conditions are necessary but insufficient.
- Internal exact finite Fraction-independent integer audit for n=1..10 gives 2046 distinct output rows, each count=2 at depth n+1; 4092 source incidences. Finite checks do NOT establish infinite legality or anything about a noncomputable x; separate proofs do.
- Countermodel falsifies ONLY the converse that persistent positive source/output local ambiguity is SUFFICIENT for destruction. It does NOT refute E-08, R₂=R₃, or the necessity of self-folding; indeed P∈F₂ is safe on R₂.

### Failed routes and first wrong inference
1. “μ_B has potentially noncomputable conditional price” fails for computably CLOPEN B: exact rational cylinder preimages.
2. “μ_B measure is dominated, therefore every G preserves CR” omits required a.e inverse-isomorphism; S011 refutes it.
3. “Positive overlap in every source neighbourhood forces a nonCR image” fails on full legal B141 pocket P.
4. “Choose a positive overlap chart effectively” confuses existential positivity of a Π¹ overlap with computable positive lower mass.
5. “F₃ factorization⇒R₂ preservation” still missing F₂(R₂) closure.
6. “MLR points in fat K can witness strictness” fails because P fixes them and is F₂ itself.
7. “A conull R₂ set meets G⁻¹(success d)” fails because the latter is null by fairness.
8. “Finite n≤10 counts prove all-outputs cap” fails unless backed by the separate disjoint-pocket infinite proof.

ENTRY operational audit: S140 PR #40 merged with authored head/main 5dca4c42509a78d248d25a0c1a1f995e43e5d49c, sole parent d9c97fced6163eb24a09d911af436ec436b988ec, tree 7e3cd465b95b7673a1ff7d2c915cb6e4f7c1e764; no S141 branch or PR before this session; branch newly created isolated; Actions runs=0, check-runs=0, statuses=[], rulesets=[], protection GET 403 UNKNOWN, no evidence of hosted CI PASS; workflow listing endpoint not accessible (400), earlier repository inspections show no workflows. Phase4 OPEN, Gate3 PASS, Gate4 NOT REVIEWED, Phase5 CLOSED. Final post-integration metadata requires independent live verification.
