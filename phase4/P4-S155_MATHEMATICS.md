# P4-S155 — computable inverse kernels with noncomputable two-fibre mass

15 October 2026. One owner-invoked Phase4 CAND-01 mathematics session, INTERNAL SAME-AGENT mathematical validation ONLY. Entry LIVE main `a3118c22412b131c7db04c2bf78942dc73813c93` tree `efea2267f11d4f97b584dc51f3d1459b278021d7`. S154 PR #54 was merged as the actual authored atomic SHA with sole parent `24e9eda1de8ff2b5842c47d264ec410e6bacaaf0`, non-force direct fast-forward. No open PR or competing S155 record/branch at entry. Zero Actions runs/check-runs/statuses = ABSENT_NOT_PASS, rulesets [], protection 403 = UNKNOWN. All original Y/M/H/X, DEF-0020, PA-0001, frozen S101–S103 A–C and evidence grades unchanged.

Let X=2^ω, λ fair measure. F_k = TOTAL computable λ-preserving maps with at most k ACTUAL COMPLETE inverse points above EVERY infinite output. R_k is survival of all F_k against ordinary total nonnegative rational computable output martingales; CR is computable randomness. Additive use one means the first n output bits depend only on the first n+1 source bits.

## Theorem A155.1 (INTERNALLY PROVED, constructive scoped effectivity separation)

For EVERY c.e. A⊆N, uniformly from its enumeration construct P_A∈F₂, total, globally fair and additive-use-one, such that:
(a) D_A={y:|P_A⁻¹(y)|=2}=⋃_{e∈A}[1^e0^{e+2}]; all other fibres are singletons;
(b) P_A(CR)⊆CR;
(c) for EVERY input cylinder [s] of length k, q_s(τ):=2^{|τ|}λ([s]∩P_A⁻¹[τ]) is an EXACT computable rational with q_s(τv)=q_s(τ) for EVERY |τ|≥k and EVERY finite v; consequently a uniformly computable, projectively coherent inverse-probability kernel κ_y exists on ALL y;
(d) λ(D_A)=Σ_{e∈A}4^{-(e+1)}, a noncomputable real whenever A is c.e. noncomputable;
(e) for infinite A the source local-collision core K_{P_A}={1^ω}, a singleton containing NO CR points (for finite A the core is empty).

This refutes specifically the inference "uniform computable disintegration even with exact finite-depth stabilisation ⇒ computable measure of output multiplicity-two locus". It does NOT refute an alternative effective betting compiler, imply R₂≠R₃, or create an S-00 witness. S005/S006 already exhibit related noncomputable inverse-weight phenomena, so NO literature novelty/priority is asserted.

### Complete construction and use proof
Set t_e=1^e 0^{e+2}, T_e=[t_e]. These form pairwise prefix-free cylinders of lengths 2e+2, masses q_e=4^{-(e+1)}, summing to 1/3. If e first enters enumeration A at stage h_e, set L_e=max(2e+2,h_e)+2; otherwise L_e is undefined. On x∈T_e with L_e defined, delete input bit at zero-indexed coordinate L_e:
`P_A(x)=x↾L_e concatenated with x|[L_e+1,∞)`.
On inactive T_e and X\⋃_e T_e set P_A(x)=x. Deletion is *inside* T_e, and every T_e is invariant.

To compute P_A(x)↾n inspect only x↾(n+1), simulate the enumeration for n stages, and inspect finitely many tags with |t_e|≤n. A deletion influences the first n bits only if L_e<n, which implies h_e<n, hence its activation has been detected. Every later activation has L_e≥n and copies these n bits unchanged. Compute the fixed deletion on any detected block; otherwise copy x↾n. This terminates globally, without deciding e∉A or guessing future halts. All outputs depend on at most n+1 source bits, giving the promised additive-use-one bound.

### Global fairness and complete fibres
Each invariant T_e, conditional on its own tag, is a fair product tail. Deleting one fixed fair tail bit pushes conditional λ to the same conditional λ. Identity pieces also conserve λ. The countable invariant measurable partition into active tags, inactive tags and the complement therefore yields λ(P_A⁻¹V)=λ(V) for EVERY Borel V, hence exact measure 2^{-|τ|} for EVERY output cylinder, all siblings included. For EVERY y∈active T_e the COMPLETE inverse set is exactly
`{(y↾L_e)0(y|[L_e,∞)), (y↾L_e)1(y|[L_e,∞))}`.
For every other y it is {y}. Because different T_e are invariant, no cross-tag inverse or third preimage exists, including over 1^ω. This is a whole-Cantor-space legality proof, not just finite row counting.

### Uniform COMPUTABLE conditional kernel and stabilisation
For each output y set κ_y=δ_y outside active T_e, and on active T_e let κ_y be the equal-weight pair of its two displayed inverse atoms. Elementary conditional integration of the independent deleted bit shows κ_y is a disintegration of λ along P_A, and ∫κ_y([s])dλ(y)=2^{-|s|}.

Fix source word s of length k. If an activation has L_e≥k, both inverse points share source k-prefix y↾k; κ_y([s]) is its indicator. If L_e<k, then h_e<k and |t_e|<k, so an enumeration simulation through k stages detects this activation, and y↾k gives each inverse's k-prefix after inserting 0 or 1 at coordinate L_e. Their average is exact 0,1/2 or 1. All undecided future tags with length≥k and all future activations with L_e≥k are invisible to source k-prefix membership. Thus κ_y([s]) depends ONLY on y↾k and is uniformly exact rational. On every output cylinder [τ] of depth m≥k κ_y([s]) is constant, whence
`λ([s]∩P_A⁻¹[τ])=∫_[τ]κ_y([s])dλ(y)=2^{-m}κ_y([s])`.
Therefore q_s(τv)=q_s(τ) for ALL τ of length m≥k, ALL v; the conditional probability kernel is computable and projectively consistent for ALL output paths, not merely λ-a.e. Its values do not supply a computable test of whether y belongs to D_A.

### Noncomputability of degree-two locus
Disjointness gives α_A:=λ(D_A)=Σ_{e∈A}4^{-(e+1)}. It is left-c.e. from the enumeration A. Its base-four digits are 0/1. If α_A were a computable real, decide e∈A recursively: subtract all earlier decoded digit contributions, divide by 4^{-(e+1)}, then approximate to distinguish [0,1/3] (digit 0, worst possible later tail) from [1,4/3] (digit 1). Thus α_A computes A, impossible when A is a chosen noncomputable c.e. set (e.g. the halting set). This argument does NOT say no computable positive lower bounds exist, and does NOT prove all stopped-event probabilities noncomputable.

### CR conservation and collision core
Inside any activated T_e, P_A is a *single fixed finite-coordinate deletion*: finite prefix insertion/deletion preserves ordinary fair-coin CR, so each CR source maps to CR. On other pieces it is identity. Independently S154's local injectivity corollary applies everywhere except 1^ω. Inside active T_e, [x↾(L_e+1)] fixes the deleted bit and is injective; inactive T_e is an identity chart; any x outside ⋃T_e other than 1^ω has a cylinder disjoint from ⋃T_e (the sole accumulation point of the tags is 1^ω). If A is infinite, every cone [1^n] includes an activated T_e with e≥n, hence two colliding sources, so K_{P_A}={1^ω}. If A is finite the core is empty. Since 1^ω is computable, K_{P_A}∩CR=∅. No S141 positive joint-fold necessity at a bad CR source is met.

## Main central E-08 and strictness attacks (FAILED, exactly scoped)
Assume the actual-hard configuration: fair additive-two G∈F₃; output rational d succeeds on y=G(x); x is the SAME member of R₂; and y has exactly two ACTUAL inverses. S141 forces positive ambiguity inside every B=[s]∩G⁻¹[τ] for s≺x, τ≺y; S154 requires x∈K_G. The attempted deduction "finite rational q_B arrays ⇒ computable price of the two-fibre stratum ⇒ one indefinitely financed F₂ test" fails already at its middle implication by A155.1, even where ALL finite posteriors have a known exact stabilisation bound. This is a no-go for that SPECIFIC inference only, not for arbitrary compilers. For a genuine hard G, the kernel itself may fail to be effectively computable, and even a given kernel need not identify or finance an actual sheet in time.

The q=1→2→t, 3→2→t and S135 3:1↔2:2 transitions still lack a global, on-the-same-source infinite two-sheet F₂/e strategy. A targeted 4-cell bet of multiplier a on t cells and sibling floor b obeys t*a+(4−t)*b≤4; target-only 4/t spends all sibling protection, so finite profitable rows cannot be iterated for free. S117 paired reservoirs, S129 eventual 2:2 chart, S141 benign folds and S011's singleton-fibre F₂ CR destroyer remain hostile controls. We did NOT produce all-output F₂, output test e, future-sheet-independent finance or E-08.

An S-00 proof additionally requires a SINGLE x∈R₂ surviving ALL globally legal F₂ maps and bad G(x), with a total rational d. S011 has Y∈CR but Y∉R₂. The constructed P_A preserves all CR and cannot separate R₂/R₃; S135's output null trap has a total source martingale. Enumerating partial algorithms is not an effective enumerator of *legal* F₂ programs. ∀F₂∃x_F is not ∃x∀F₂. No coupled witness, E-00 or arbitrary-use reduction was produced.

**Result:** A155.1 is new-to-this-session scoped internal mathematics relative to a precisely specified effective-use regime, NOT a novelty/publication claim. E-08/E-00/S-00 and R₂=R₃ versus strictness remain OPEN. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.
