# P4-S094 — Counterexample to ASSCL and the uniform-totality boundary

2026-10-11; only Phase 4 mathematics, CAND-01. Incoming live main f6733e313642001eb39998efb7dfe331da92261f, S093 atomic close with sole parent 96b3a8a496de5994bb141f2cd0131b5db69a065c. No intervening changes or S094 files/branch; no PRs or hosted Actions runs at entry. Session branch phase4/P4-S094-asscl-partiality.

**OUTCOME: the S093 Amortized Specified-Side Cost Lemma (ASSCL) is FALSE AS STATED. R₂ versus MLR remains UNRESOLVED.** This refutes an explicitly UNPROVED S093 hypothesis, not S093 Theorem A, not GOL itself, and not either of the programme's central alternatives.

## Gate 1 — exact targets and plan

F₂ consists of total computable measure-preserving Cantor self-maps with global fibres of size at most two. Equality means ∀z∈CR∖MLR ∃G∈F₂ ∃computable martingale d succeeding on G(z). Separation means ∃z∉MLR ∀G∈F₂ ∀computable martingale d bounded on G(z), with a single common source. S093 Theorem A makes GOL equivalent to AR-cover: every CR∖MLR source is autoreducible in some computable fair frame; GOL implies equality, but its failure would NOT prove strict inclusion. The chosen lead attack tests S093 ASSCL, meant to produce first the weaker milestone z∈CR∖MLR∖AR^iso and then attempt full F₂ survival.

## Gate 2 — exact counterexample to ASSCL

Use S089 Definition 1.1: for map G, martingale d and nonempty clopen P, put c^P(w)=1 when G⁻¹[w]∩P≠∅ and Ψ(P,t)=λ(P)⁻¹ Σ_{|w|=t} 2^(−t)d(w)c^P(w). For a finite weighted family Φ_pot=Σ_e w_eΨ_e. Crucially at early times Ψ(P,t) is a *hit-cell* potential, not the conditional average of d on P.

**Theorem 1 (ASSCL refuted).** Let G=id, P=2^ω, K=id, h₀=2. Define d(∅)=1; d(0σ)=1/2 and d(1σ)=3/2 for any finite σ. This is a total nonnegative rational computable martingale, constant after the first bit, in savings form A=d<2 and B≡0, with integrable B_∞=0. Give d any positive rational weight w. Because P is the full space, Ψ(P,t)=1 for ALL t, hence Φ_pot(P,t)=w.

Define the self-avoiding partial Turing functional T: on input h≥1, query only oracle bit 0, output 0 if it is 1, otherwise diverge. On input h=0 diverge without querying. T never queries its input coordinate. For each h≥2, T is wrong exactly when x₀=x_h=1. Thus any nonempty clopen P′⊆P on which T is wrong at some h≥2 lies in [1], indeed in A_h=[1]∩{x_h=1}; A_h itself is a nonempty clopen state with arbitrarily many free extension coordinates.

For EVERY time t′≥1, S089 Lemma 1.2(ii) in the identity frame yields Ψ(P′,t′)≥λ(P′)⁻¹∫_{P′}d(x↾t′)dλ=3/2. At t′=0, Ψ(P′,0)=1/λ(P′)≥4 since λ(P′)≤λ(A_h)=1/4. Therefore for all times and all possible wrong substates, Φ_pot(P′,t′)≥3w/2. Taking ε=w/4 makes the ASSCL first alternative Φ_pot(P′,t′)≤w+ε impossible, even if no restriction on t′ is imposed. Its second alternative also fails: T converges on EVERY x∈[1] at EVERY h≥2, hence does not diverge throughout P at any large h. Both alternatives fail, proving the quantified lemma false. ∎

The failure is not an aligned adaptive self-reader: only a fixed first-bit capital bias and a convergence domain concentrated in its expensive region suffice. In this example the cheap divergence state [0] exists; the lemma excluded the option of moving to it because the alternative required divergence on *all* P. Thus the S093 conditional Proposition S is a formally conditional implication with a false antecedent and is not an operative method of refuting GOL.

## Gate 3 — repair search and positive boundary

A natural repair allows the construction to choose a cheap clopen D⊆P where the reader diverges at a chosen hold, rather than requiring divergence on all P. Here D=[0] works. But for a general partial functional the divergence locus is Π⁰₁ closed, may have empty interior, and may not contain a nonempty clopen D. Its nonemptiness and protected-capital capacity may be inaccessible to a Σ⁰₁ search. Guessing non-halting needs a genuine true-path proof; it cannot be silently converted to finite-stage information. No complete repaired lemma was obtained.

The following positive result isolates the only case in which the direct wrong-side argument becomes uniformly inexpensive.

**Theorem 2 (uniform-totality boundary, identity strategies only).** Let K be a computable fair homeomorphism, P nonempty clopen, T self-avoiding, and Φ_pot a finite positive rational weighted sum of identity-map S089 potentials for total rational computable savings martingales satisfying the S087 integrable domination d_e(x↾s)≤2+B^e_∞(x). Suppose T^{K(x)}(h) converges on ALL x∈P for arbitrarily large h. Then, for every initial time t and ε>0, some such h has a nonempty clopen wrong substate A_h⊆P and s≥t with Φ_pot(A_h,s)≤Φ_pot(P,t)+ε.

*Proof.* Uniform convergence use on compact P makes A_h clopen. For sufficiently high h, the partner involution ψ_h=K⁻¹ flip_h K preserves P, fixes any prescribed raw initial segment and preserves λ. By self-avoidance, ψ_h exchanges the wrong and right halves of P, hence λ(A_h)=λ(P)/2 and A_h is nonempty with free coordinates. Each d_e(x↾s) converges almost surely, and the integrable savings bound gives dominated L¹ convergence to f_e∈L¹. Put f=Σw_e f_e. Because ψ_h preserves λ and eventually fixes each finite cylinder, approximating f in L¹ by cylinder-simple functions shows ∫|f−f∘ψ_h|→0. As ψ_h maps A_h to P∖A_h,
|λ(A_h)⁻¹∫_{A_h} f−λ(P)⁻¹∫_P f|≤λ(P)⁻¹∫_P|f−f∘ψ_h|→0.
The fixed-time hit-cell definition and martingale conservation show λ(P)⁻¹∫_P f≤Φ_pot(P,t), including when P is not a union of length-t cylinders. Because A_h is clopen, its hit cells at all sufficiently late s are exactly its contained cylinders, and Φ_pot(A_h,s)→λ(A_h)⁻¹∫_{A_h}f by dominated convergence. Choose eligible h and then s large to obtain the ε bound. ∎

**Caveats:** This is existential, with NO asserted computable modulus or search for h/s. It assumes T total on the WHOLE current P for arbitrarily large holds, not convergence somewhere, almost everywhere or on a high-capital subregion. It protects only identity martingales. It is not an AR-cover or ¬AR-cover theorem. Theorems 1 and 2 together show that the missing difficulty includes *selective partiality*, beyond S093's anticipated aligned forcing-window bias.

## Gate 4 — full-family quantifier

No z is constructed. Even a future z outside AR^iso would need to satisfy S084's entire computably random predictable-error streams, all fractional one-hole readers in all frames including K_mix/K′_mix (with PRECEDING-control offset) and all non-scan F₂ maps. This session does NOT cross ∃z∀G∀d, nor does it prove EQ's ∀z∃G∃d.

## Gate 5 — independent equality attack

Trying to orient all failing ML-test points with a universal test fails: flipped-h partners are also covered (S092 Proposition 3). Restricting to time-bounded first entry fails on CR points (S092 Lemma 4). Source-dependent asymmetric coverage is precisely the still-unproved AR-cover / S093 Theorem A. A proposed fractional restart destroyer would need demonstrably positive cumulative edge despite S084's computably random prediction-error stream on every infinitely resolving R₂ source; no such uniform edge or global non-scan F₂ construction is established. Failure of the ASSCL route gives no evidence that EQ is true.

## Gate 6 — adversarial validation and status

Theorem 1 checks *all* weights w>0, t′≥0, nonempty clopen wrong substates, the convergence branch, self-avoidance, savings domination, and available future coordinate fixings. Python exact fractions audited 441 finite cylinder-time instances (phase4/P4-S094_ASSCL_AUDIT.py), PASS; the symbolic argument proves universality. Theorem 2 checks use-modulus partner invariance, clopen compactness, martingale uniform integrability, the precise S089 potential, and clearly distinguishes mathematical existence from effective selection. Full review in P4-S094_VALIDATION.md.

PROVED: ASSCL FALSE AS STATED; conditional uniform-totality boundary.
FAILED/UNPROVED: effective cheap wrong-or-diverge substate repair; AR-cover/GOL; its negation; full F₂ equality or survivor.
UNRESOLVED: R₂ vs MLR; Conjecture R; R₂ vs OH^iso; U(H); original X∈OH and fixed-S preservation.

No new sources or source-access upgrades. Keep PA-0001, DEF-0020, original Y/M/H/X, all previous class inclusions unchanged. Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, priority, external openness, publication or outreach claim.
