# P4-S096 — Closed saturation and the effective true-path obstruction

2026-10-11; ONE Phase 4 CAND-01 mathematical session. Incoming live main 56082da9a1b805e47b2161bf46bac77df889c739 (S095 outgoing); sole parent 4703cdf3c6cb88721771d49c05bcd32aef531985. No intervening commits, existing S096 files/branches or open/recent repository PRs. Hosted Actions runs 0, jobs 0, check-runs 0, status contexts 0; NONE is not CI PASS. Session branch phase4/P4-S096-closed-saturation-effectivity.

**DISPOSITION: neither R₂=MLR nor one z∈R₂∖MLR PROVED.** Six central proof gates genuinely attempted. Exact new results identify the missing effective-index/branch-budget implication and give a NON-EFFECTIVE analytic construction protecting ALL F₂ strategies, but the constructed survivor may be ML-random. No new class inclusion.

## Gate 1 — exact finished quantifiers

F₂ is EVERY total computable λ-preserving map G:2^ω→2^ω with |G⁻¹(y)|≤2 for EVERY y. R₂={z∈CR:∀G∈F₂ G(z)∈CR}. Equality EQ demands ∀z∈CR∖MLR ∃G∈F₂ ∃total computable rational nonnegative output martingale d succeeding on G(z). Separation SEP demands ∃z∉MLR ∀G∈F₂ ∀such d, sup_t d(G(z)↾t)<∞. GOL is S093's AR-cover; it would imply EQ, but may not be necessary. ¬GOL alone is NOT SEP. All inherited class inclusions and S093/S094/S095 corrections remain frozen.

## Gate 2 — extend S089 hit accounting to closed states, exactly

Let P be nonempty compact of positive λ measure, G any total computable fair map, and (d_t) a saved output martingale in S082 Lemma 2.4 with active part <2 and final nondecreasing savings bank B∞. Put X_t(x)=d(G(x)↾t). For each t define C_t(G,P)={x: G(x)↾t extends some length-t prefix of a point of G(P)}. The sets C_t are clopen, decreasing, and their intersection is Sat_G(P):=G⁻¹(G(P)), since G(P) is compact.

Extend the *numerical*, not necessarily computable, S089 hit potential to P:
 Ψ_G(P,t)=λ(P)⁻¹ Σ_{|w|=t}2⁻ᵗd(w)1[G⁻¹[w]∩P≠∅]
          =λ(P)⁻¹∫_{C_t(G,P)}X_t dλ.
Its monotonicity Ψ(P,t+1)≤Ψ(P,t) uses child hit indicators and fair martingales, also for compact P. With d(∅)=1, Ψ_G(P,0)=1/λ(P), NOT 1 in general.

**Theorem A — closed-hit saturation limit (PROVED).**
 lim_{t→∞} Ψ_G(P,t)=λ(P)⁻¹∫_{Sat_G(P)}d∞(G(x))dλ(x).
This applies to EVERY total fair G, not only F₂. PROOF: G preserves λ. The output bank has E B∞≤1 because B_t increases and B_t≤d_t, E d_t=1. For all t, 0≤X_t(x)≤2+B∞(G(x)), an integrable dominating function. Almost-sure output martingale convergence and the decreasing clopen indicators 1_{C_t}→1_{Sat_G(P)} permit dominated convergence. No computable rate, closed-hit decision or λ(P) algorithm follows. For a homeomorphism, saturation equals P; for two-fibre maps it can be strictly larger.

**Corollary A1 — existential homeomorphic closed-hit repair (PROVED).** For any finite list of fair computable homeomorphisms G_e, savings martingales d_e and positive weights w_e, let f=Σ_e w_e d^e∞∘G_e, integrable. Fix positive effectively closed P, time t₀, partial syntactically self-avoiding Φ in any computable fair frame K, and ε>0. The S095 Theorem A selector gives arbitrarily high holds and a positive Π⁰₁ wrong-or-diverge Q⊆P with avg_Q f≤avg_P f+ε/2. Since homeomorphisms have Sat_{G_e}(Q)=Q, Theorem A gives Σw_eΨ_{G_e}(Q,t)→avg_Q f. Savings UI, S089 domination and monotonicity yield avg_P f≤Σw_eΨ_{G_e}(P,t₀). Thus for SOME late t≥t₀, Σw_eΨ_{G_e}(Q,t)≤Σw_eΨ_{G_e}(P,t₀)+ε. This is an EXISTENCE theorem, NOT effective h, s, t selection and NOT a general F₂ bound.

**Counterexample A2 — full-F₂ saturation gap (PROVED).** Let G(x)=x₁x₂… delete raw bit zero: total computable fair and exactly two preimages for every output. Take P=[0] fixing raw bit zero and d≡1. Then G(P)=2^ω, Sat_G(P)=2^ω, and Ψ_G(P,t)=2 at EVERY t≥0, although avg_P X_t=1. Even the identity savings bank cannot turn a mere conditional L¹ estimate into the S089 all-map Ψ budget. The example is an accounting obstruction, NOT a randomness destroyer: fixed-bit deletion preserves CR.

## Gate 2 continued — the exact effective coding frontier

**Lemma B1 — effectively closed outer-cover lemma (PROVED).** For a uniformly supplied Π⁰₁ class P with decreasing computable clopen approximants P_s and a rational q>0 KNOWN to satisfy λ(P)≤q, search for s with λ(P_s)<2q. It halts by continuity of measure from above, and P_s is a computed clopen outer cover of measure <2q. If finitely many effectively emitted true/wrong guessed runs at level n give at most N_n indexed Π⁰₁ classes with certified bound q_n and 2N_nq_n≤2⁻ⁿ, their outer covers form a uniformly c.e. ML test. Invalid/nonhalting runs may produce nothing, but the true run must be proved to complete. This lemma does NOT generate the necessary index, lower positive-measure certificate or branch count.

**Lemma B2 — every closed selector has an exact upper half bound (PROVED).** S095 uses P_h=P∩ψ_h(P), whose measurable wrong-or-diverge selector S_h contains exactly one representative of each ψ_h pair; λ(S_h)=λ(P_h)/2. Every finite convergence-stage closed approximation Q_{h,s}⊆S_h therefore satisfies λ(Q_{h,s})≤λ(P)/2. S095 provides SOME h,s with λ(Q)≥(1/2−ε)λ(P), but the lower bound, acceptable s and conditional f-cost are not computably searchable. The geometric upper mass of an individually selected TRUE branch does NOT constrain the measure of the union over candidate h,s.

**Counterexample B3 — arbitrary unpriced holds consume all measure (PROVED).** Let P=2^ω, K=id, and the totally defined syntactically self-avoiding reader Φ^x(h)=0 without any query. Its bad (wrong) set for hold h is clopen Q_h={x:x_h=1}, with λ(Q_h)=1/2. For distinct h=H,…,H+m−1, λ(∪ Q_h)=1−2⁻ᵐ. Consequently the union over ALL h≥H has measure ONE, despite each candidate being a half-measure state. Enumerating every existentially available h as a guessed run is NOT an effective test; a finite-branch coding must explicitly price its index bits. A Σ⁰₁ search for positivity/cost is not supplied by S095 (a Π⁰₁ class only has upper-semicomputable measure in general). Arbitrary oracle-selected cylinders [z↾n] shrink geometrically yet can contain a Martin-Löf random z. Relative true-path availability ≠ an ordinary effective null cover.

**S082 comparison.** Its guessed runs enumerate 2^{i+1} validity prefixes, each of computably chosen clopen state measure at most 2^{−(i+1)(i+2)}, yielding a genuinely c.e. bounded union. With Π⁰₁ states, B1 can recover the cover ONLY AFTER uniformly enumerated state indices, a numerical per-run upper bound, an explicit bound on number of completed runs and a true-run completion proof. Neither S095 Theorem A nor Corollary A1 solves the unbounded h/s choice entropy. The S095 dense reader has Π⁰₁ divergence with no clopen interior; the S094 expensive-region example still defeats wrong-only forcing.

## Gate 3 — substantial ALL-F₂ analytic forcing attempt

Enumerate as an abstract countable mathematical family every VALID (G_e,d^0_e) with G_e∈F₂ and d^0_e a total rational normalized computable output martingale. Validity is NOT computably enumerable. Let d_e be the S082 savings transform of d^0_e, with bank B^e∞. Fix weights w_e>0 with Σ w_e≤1 on this family and define
 f(x)=Σ_e w_e(2+B^e∞(G_e(x))).
Each term is LOWER SEMICONTINUOUS as an abstract function: B∞=sup_t B_t, each B_t is continuous on output cylinders, G_e continuous. The positive sum is lsc and integrable, with ∫ f≤3 by Tonelli, fairness and E B∞≤1. For every e and t:
 w_e d_e(G_e(x)↾t) ≤ f(x).
No effective index for f and no computable listing of valid maps are asserted.

Mathematically enumerate every computable fair homeomorphism K and every syntactically self-avoiding partial reader Φ, repeating each with every arbitrarily large lower hold threshold H. Begin P₀=2^ω. At requirement n apply S095 Theorem A to the SAME f and P_n, choosing some high hold h≥H and a positive effectively closed P_{n+1}⊆P_n where Φ^{K(x)}(h) is wrong-or-divergent throughout, and avg_{P_{n+1}}f≤avg_{P_n}f+ε_n, with ε_n=2⁻ⁿ⁻². All conditions are individually Π⁰₁, nested, positive, with avg_{P_n}f<4 and λ(P_n)≤2⁻ⁿ (B2).

**Theorem C — NON-EFFECTIVE common all-F₂ survivor with no-frame-autoreduction (PROVED WITH THESE QUALIFIERS).** The nested intersection contains a single z∈R₂ where every such partial self-avoiding reader in every computable fair homeomorphic frame fails at arbitrarily high holds. The intersection has measure zero. This does NOT show z∉MLR.

PROOF: The set {x:f(x)≤4} is closed because f is lsc. Each P_n meets it: otherwise avg_{P_n} f>4. Compactness yields z∈∩_n(P_n∩{f≤4}). All requirements persist. For each valid strategy e, sup_t d_e(G_e(z)↾t)≤4/w_e<∞, so S082 savings Lemma 2.4(iii) bounds the ORIGINAL martingale d^0_e on G_e(z). The enumeration covers every rational observer of every G∈F₂, including identity, proving z∈R₂. Half-volume iterations force λ(∩P_n)=0. But the sequence of Π⁰₁ indices was selected using noncomputable choices; an abstract null intersection need NOT exclude MLR points. Indeed all MLR sources lie in R₂ and are nonautoreducible, so this is compatible with an ML-random z.

**Exact conditional finish.** If the above choices can be organized into a computably enumerable, finitely bounded guessed-run family of Π⁰₁ states with true-run completion and the B1 effective ML test (uniform level measure ≤2⁻ⁿ) WHILE preserving the f-integral invariant, compactness gives ONE z∈R₂∖MLR. The all-F₂ capital bound then follows from f directly; the S089 arbitrary-F₂ hit potential is not required for this CONDITIONAL route. The missing decisive implication is effective priced choice (h,s,positivity,budget,validity), not an unproved assertion that Π⁰₁ sets cannot be open-covered.

The attempt to implement this condition failed: unbounded candidate holds cannot all be included (B3), no uniform computable large-h threshold exists from the proved S095 hypotheses, and choosing h/s with ∅″-style true-path arithmetic does not enumerate an unrelativized ML test. A limit z selected this way may be MLR. There is therefore NO constructed z∈CR∖MLR∖AR^iso and NO SEP.

## Gate 4 — checking FULL F₂, not just a scan subclass

Theorem C's analytic envelope formally contains EVERY everywhere-total fair globally ≤2-to-1 non-scan map, every fractional one-hole scan strategy, S084's ENTIRE computably random error-stream adversaries, both K_mix and K′_mix with the PRECEDING-control offset, and all phantom-fibre programs, because each valid (G,d) appears in the countable family. Its explicit bound for each saved output strategy is 4/w_e; the original d^0_e is bounded by savings. It is a common-source all-map result, but can be TRIVIALLY satisfied by an MLR point. It does not supply an effective non-MLR certificate, and may not be advertised as R₂∖MLR. It does not weaken S084's constraints or change any inclusion.

## Gate 5 — attack equality independently

AR-cover/GOL remains precisely S093's assertion that each z∈CR∖MLR has some fair computable frame K making K(z) autoreducible. S092 Proposition 3 refutes universal-test partner orientation: both hold completions fail a universal ML test. S093's left-c.e. landing criterion needs infinitely many reached high-precision NON-LANDINGS; monotone evidence does not cover high Turing degrees (S093 L4). No arbitrary-source AR-cover derivation is available.

For an explicit non-orientation F₂ attempt, fixed deletion G(x)=x₁x₂… is globally legal but CR-preserving; transport by a fair computable homeomorphism remains CR-preserving, so this cannot be a universal destroyer. Any infinitely resolving fair scan variant must retain global fibre≤2 and satisfy S084's full predictable-error constraint on every proposed survivor. On N resolved predictions with c correct and e wrong, a fixed stake 0<a<1 multiplies capital by (1+a)^c(1−a)^e. If e/N→1/2 (S084), (log capital gain)/N→½log(1−a²)<0; all-in a=1 loses permanently on one wrong bit. Restarts do not erase lost accounts. Variable predictable stake strategies cannot be dismissed by frequency alone, but are covered by S084's stronger assertion that the ENTIRE selected error sequence is computably random. No output martingale with positive general gain, global total F₂ extension or universal source coverage was proved. Neither equality nor separation follows from failure of the other attempt.

## Gate 6 — adversarial validation and classification

Check: t=0 Ψ(P,0)=1/λP; deletion saturation yields Ψ=2 for ALL t; savings UI is crucial for Theorem A; no all-F₂ L¹→hit implication; Π⁰₁ empty-interior divergence not treated as clopen; B1 requires a UNIFORMLY EMITTED index and KNOWN upper mass; unbounded h union is full measure; oracle-selected null cylinders may contain ML-random points; f is NON-EFFECTIVE yet integrable lsc; compactness uses closed {f≤4} and the same z for ALL maps; the full S084 error streams and K′_mix preceding-control offset are not silently simplified. Auxiliary exact finite check: 120 instances PASS (m=1..12 for union formula and deletion Ψ t=0..8); this is NOT an infinite proof or hosted CI. No Lean or independent verification.

PROVED: Theorem A (closed saturation), Corollary A1 (homeomorphic existential hit repair), A2 (general-F₂ saturation gap), B1 (conditional-index outer cover), B2 (half-measure upper bound), B3 (unpriced hold entropy), Theorem C (NON-EFFECTIVE all-F₂ protected compactness survivor). CONDITIONAL: true-path effective priced-choice + ML test would imply SEP. REFUTED: automatic all-F₂ Ψ control from conditional L¹, all-h cheap enumerable guessed paths, and the claim that merely geometric oracle-chosen closed states show non-MLR. UNRESOLVED: EQ, SEP, AR-cover/GOL and its negation, R₂ vs OH^iso, U(H), X∈OH, fixed-S preservation and Conjecture R.

Preserve original CR Y, globally use-clipped syntactically self-avoiding wtt M, repeated 3-bit H with rows 101/110/111 and X=H⁻¹Y; frozen MLR=R_tot⊆R_fin⊆R_k⊆R₂⊆OH^iso⊊OH^aff⊊OH^blk⊆OH^lin3⊆OH=OH_h=R_k^scan⊊CR (k≥2), MLR⊊R₂^cdz⊆R₂^dz⊆R₂^fd, R₂⊊R₂^cdz⊊R₂^fd, R₂⊊OH. SRC-0015, 0019, 0028, 0060, 0069–0074 at RECORDED levels; SRC-0071 journal METADATA_ONLY, SRC-0073/74 ABSTRACT_INSPECTED. PA-0001/DEF-0020 unchanged. Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No new source retrieval, novelty, openness, priority, publication, outreach, Lean, spectral calculations or excluded detours.
