# P4-S093 — Orientation is autoreducibility: the Global Orientation Lemma as a classical statement, its calibration, the left-c.e. window criterion, and the category/forcing obstructions

Date: 2026-10-11. Phase 4 Mathematics ONLY; selected CAND-01.
Incoming live main: `96b3a8a496de5994bb141f2cd0131b5db69a065c` (the S092 atomic close), sole parent `ec2c6ff1b5050b1b324d10b007843b1336bd7010`.

**Disposition: R₂ versus MLR is NOT decided.** A sustained attempt was made through all six internal proof gates. The lead route (equality through S092 orientation readers) was carried to an exact classical reformulation and then to its decisive obligation; the opposite route (a survivor, or at least a counterexample to the Global Orientation Lemma) was attempted and stopped at a precisely stated cost lemma.

Proved this session:

* **Theorem A (orientation is autoreducibility).** For every source z and computable fair homeomorphism K, S092's GOL hypotheses hold in frame K (in either the coverage form or the race form) if and only if K(z) is Turing autoreducible. Hence GOL is equivalent to: *every z∈CR∖MLR has a Turing-autoreducible image under some computable fair homeomorphism*. With S092 Theorem 1, every computably random z with an autoreducible image lies outside OH^iso, hence outside R₂ (Corollary A2).
* **Corollary A3 (calibration).** GOL implies OH^iso=MLR, and therefore that Rute's automorphism randomness and endomorphism randomness (SRC-0060, recorded STATEMENT_INSPECTED) both equal MLR. A proof of GOL would thus settle the second implication of Rute's chain (10.1), part of QST-0002 (recorded SOURCE-STATED OPEN in 2016; no later status check made; no openness inference drawn).
* **Proposition L1 (larger-candidate soundness in every frame).** For a left-c.e. source and its approximation-prefix family, in EVERY computable frame, separate coverage of the lexicographically larger of the two hold completions (equivalently, the larger real, for sequences that are not eventually constant) certifies that the source is that completion.
* **Proposition L2 (window criterion).** In the raw frame, with an arbitrary computable level N(h) ≥ h+1, the reader proposes 1 at a reached hold exactly when z_h=1 and no approximation (from index N(h) on) lands in the 2^{−N(h)}-window of the partner. This strictly weakens S092's whole-interval jump-over requirement to a window of any computable precision; Corollary L3 strengthens S092 Corollary 5b accordingly (left-c.e. MLR sources still land at almost every reached upper hold, at every computable precision).
* **Proposition L4 (no frame transfer of monotone orientation beyond Δ⁰₂).** If some computable fair homeomorphism makes z left-c.e., then z ≤_T ∅′; CR∖MLR contains sources that are not Δ⁰₂ (via THM-0014, recorded STATEMENT_INSPECTED). So one-sided monotone orientation cannot be transported by frames to all of CR∖MLR.
* **Lemma G (category).** Each autoreducibility class AR(K,Φ) is meager; every 2-generic sequence lies outside AR^iso := ⋃_K AR(K).
* **Lemma M (no Baire space).** CR∖MLR is meager in itself. Hence Lemma G cannot be relativized to CR∖MLR by a Baire-category argument; a counterexample to GOL cannot be obtained by category alone.
* **Proposition F (pairing forcing and its exact cost).** In any clopen condition invariant under a hold involution, convergence of a would-be autoreduction yields a clopen sub-condition on which it is wrong; the two sides have equal measure, and the only cost of forcing the wrong side is a *specified-side bias* of the protected strategies.

Not proved: R₂=MLR; z∈R₂∖MLR; GOL; its negation; the left-c.e. instance; the Specified-Side Cost Lemma (§6); Conjecture R. No new class inclusion is claimed.

## 0. Entry, review and challenge of the S092 starting results

**Pinning.** `git ls-remote origin refs/heads/main` gave `96b3a8a496de5994bb141f2cd0131b5db69a065c`, the commit whose message begins "P4-S092"; its sole parent is `ec2c6ff1b5050b1b324d10b007843b1336bd7010`, as the prompt states. The pull-request listing (all states) is empty. Remote side branches are historical work branches; `phase4/P4-S092-mathematics` equals main and `phase4/P4-S092-wip` holds superseded scratch. `phase4/` contained no P4-S093 file and every mention of P4-S093 names it as the next session, so S093 was unused. The incoming prompt is archived verbatim as `phase4/P4-S093_INCOMING_HANDOFF.md` (SHA256 `a7c8a6ed5ed8bb4f3be62bb2da35911d33159e6ff048912fe8ab4f1c497b6a6b`); it agrees with the committed `authoritative/NEXT_SESSION_PROMPT.md` up to markdown markers (headings, bullets, bold, code quotes) stripped in the pasted copy.

**Reviewed.** Repository authority, SESSION_PROTOCOL, gate and source policies, CAND-01 and the Gate-3 PASS, both Phase-4 pivots, the cumulative S001–S091 summaries, and in detail S082 §§2–6 (including §6.3), S083 §§1–3, S085, S086, S087 §§1, 4–6, S089 §§1, 5–6, S092 mathematics, validation and close. This is not a claim to have re-proved historical mathematics.

**Sources.** Used only at recorded access: SRC-0015 (THM-0007), SRC-0028 (THM-0014), SRC-0060 (THM-0080, QST-0002) STATEMENT_INSPECTED; SRC-0071 preprint STATEMENT_INSPECTED with recorded proof reading, journal version METADATA_ONLY; SRC-0019, SRC-0069, SRC-0070, SRC-0072 unused. New retrieval this session (two bounded web searches, §3.5 and catalogue) produced abstract-level calibration only; it is recorded in the catalogue with its access level, and no proof below depends on it.

**Challenge of S092.** Theorem 1 was re-checked against its proof: the reader's schedule at a hold h is history-independent (when h becomes the hold, exactly h coordinates have been read, so t=h and M=h+1, and thereafter M=t+1); legality, fairness and the fibre bound hold on every transcript; the restart martingale handles finitely many wrong bets. Corollary 2, Proposition 3 and Lemma 4 were re-checked. In Proposition 5 the level n(h)=h+1 is a choice, not a necessity; §3 shows that larger computable levels give strictly more destructive power. No proof error was found; no correction is needed.

## 1. Proof gate 1 — the finishing statements and the dependency plan

F₂, R₂, OH, OH^iso and frames are as in S092 §1–2.1. For a frame K and virtual coordinate h, ψ_h:=K⁻¹∘flip_h∘K is the partner involution.

* **Equality.** (EQ) ∀z∈CR∖MLR ∃G∈F₂ ∃ computable martingale d: d succeeds on G(z). The S092 sufficient form is GOL.
* **Separation.** (SEP) ∃z∉MLR ∀G∈F₂: G(z)∈CR.

**Plan.** Before attacking GOL by family shapes, determine exactly what GOL asserts about an individual source. If GOL is a known kind of statement, its strength can be calibrated and the right attack chosen. Theorem A shows that GOL is a statement about Turing autoreducibility. Corollary A3 then shows that GOL is at least as strong as the automorphism-randomness part of SRC-0060 Question 10.8. The genuinely missing global implication on the equality side is therefore:

> **(AR-cover)** every z∈CR∖MLR is Turing autoreducible after some computable fair homeomorphism,

or else a non-orientation F₂ mechanism. On the separation side, the minimal necessary step is a source in CR∖MLR outside AR^iso (which already refutes GOL), and then survival against all F₂.

## 2. Proof gate 2 (equality) — orientation is autoreducibility

### 2.1 Definitions

A Turing functional Φ is **self-avoiding** if on input h it never queries position h of its oracle. A sequence v is **Turing autoreducible** if some self-avoiding Φ satisfies Φ^v(h)↓=v_h for every h. Because Φ is self-avoiding, Φ^v(h)=Φ^{v⊕e_h}(h) whenever either side converges. Changing Φ on finitely many inputs preserves self-avoidance, so "for all h" may be replaced by "for all but finitely many h".

For a frame K put AR(K):={z : K(z) is Turing autoreducible} and AR^iso:=⋃_K AR(K), the union over all computable fair homeomorphisms K. AR^iso is closed under computable fair homeomorphisms and finite changes.

S092's GOL data for z in frame K (**coverage form**): a uniformly c.e. family W=(W_m) of strings and a computable n such that
* (C1) for every h, some σ∈W_{n(h)} satisfies z∈[σ] and ψ_h(z)∉[σ];
* (C2) for all but finitely many h, no τ∈W_{n(h)} satisfies ψ_h(z)∈[τ] and z∉[τ].

**Race form.** (C1), and
* (C2′) for all but finitely many h, at the first check of the canonical schedule at which some candidate of hold h is separately covered, only the true candidate is.

The canonical schedule at hold h is the one the S092 reader uses: checks at t=h, h+1, …, with frontier M=t+1, raw window ℓ(M), and the stage-t part W_{n(h),t}. It depends on h only, as noted in §0.

### 2.2 The theorem

**Theorem A.** Let z∈2^ω, K a computable fair homeomorphism and v=K(z). The following are equivalent:
(a) GOL data for z in frame K exist in the coverage form;
(a′) GOL data for z in frame K exist in the race form;
(b) v is Turing autoreducible.

*Proof.* (a)⇒(a′). If the partner of z is never separately covered at (h,n(h)), the first separate coverage, which exists by (C1) and the schedule, is of z only.

(a′)⇒(b). Define a self-avoiding Φ. On input h, with oracle u, let u^b:=u with position h set to b (Φ never reads u_h; it uses u^0 and u^1 only through positions ≠ h, plus the constant b). Run the canonical schedule of hold h. At each check compute the raw windows ρ^b:=K⁻¹(u^b)↾ℓ(M) (computable from u↾M with h overwritten, through the computable modulus of K⁻¹). Output the first b such that some σ∈W_{n(h),t} with |σ|≤ℓ(M) has σ⊑ρ^b and σ⋢ρ^{1−b}; if both appear at the same check, output 0. With oracle u=v the two raw completions are z (for b=v_h) and ψ_h(z), so by (C1) Φ^v(h) halts, and by (C2′) its output is v_h for all but finitely many h. Patch the finitely many exceptions.

(b)⇒(a). Let Φ autoreduce v. Put O_h:=K⁻¹{u : Φ^u(h)↓=u_h}. Uniformly in h this is an effectively open set. Enumerate every finite string ρ with |ρ|>h such that Φ^ρ(h) halts within |ρ| steps, querying only positions <|ρ|, with output ρ_h. For each such ρ enumerate every σ with [σ]⊆K⁻¹[ρ]; this condition is decidable because K⁻¹[ρ] is a uniformly computable clopen set. Let W_h be the c.e. set of all such σ, so that ⋃_{σ∈W_h}[σ]=O_h, and put n(h):=h. Since Φ^v(h)=v_h, the source z lies in O_h, so some σ∈W_h with [σ]⊆O_h contains z. Also ψ_h(z)∉O_h, because K(ψ_h(z))=v⊕e_h and Φ^{v⊕e_h}(h)=Φ^v(h)=v_h≠(v⊕e_h)_h. Hence σ separates z from ψ_h(z), giving (C1) for every h. Any τ∈W_h with ψ_h(z)∈[τ] would give ψ_h(z)∈O_h, impossible; so (C2) holds for every h. ∎

**Corollary A1.** GOL holds if and only if CR∖MLR ⊆ AR^iso. The same holds for the race form of GOL.

**Corollary A2.** If z∈CR and K(z) is Turing autoreducible, then the S092 reader built from the family of the proof of (b)⇒(a) destroys z on a singleton fibre. Hence CR∩AR^iso ⊆ CR∖OH^iso, and R₂∩AR^iso=∅. For z∈CR, the first assertion of S092 Corollary 2 (global partner entanglement) is *equivalent* to z∉AR^iso.

*Proof.* (C1) and (C2) hold at every hold, in particular at reached holds, so S092 Theorem 1 applies with Sel≡true. The equivalence is Theorem A applied frame by frame. ∎

*Remarks.* (i) Autoreducibility of CR sequences is not empty: the committed P4-S011 source Y is wtt-autoreducible (THM-0076), and Corollary A2 recovers, in reader form, the S011/S012 conclusion Y∉OH. (ii) S092 Theorem 1 needs (C1)/(C2) only at the holds the reader actually reaches. That reached-hold form is weaker than autoreducibility in general, and Theorem A does not cover it. Under the reached-hold form the self-avoiding search above computes v_h correctly at almost every reached hold, but the set of reached holds depends on the reader's own transcript, not on v alone. The reached-hold form is not used below.

### 2.3 Calibration of GOL

**Corollary A3.** GOL ⇒ OH^iso=MLR ⇒ Rute's automorphism randomness and endomorphism randomness both equal MLR.

*Proof.* GOL gives OH^iso=MLR (S092 Proposition 1.2). Automorphism randomness (DEF in SRC-0060, recorded STATEMENT_INSPECTED) asks that T(x) be Kolmogorov–Loveland random for every a.e.-computable measure-preserving automorphism T. Every computable fair homeomorphism K is such an automorphism, and KLR⊆OH (frozen). So automorphism randomness ⊆ OH^iso; this inclusion is already recorded in the catalogue's definition note. Rute's chain (10.1), THM-0080, gives MLR ⊆ endomorphism randomness ⊆ automorphism randomness. ∎

So any proof of GOL decides that the second implication of Rute's chain (10.1) reverses. That is part of QST-0002, recorded SOURCE-STATED OPEN in 2016 (SRC-0060 Question 10.8); no later status check has been made, and no openness or difficulty inference is drawn beyond this logical relationship. The first implication reverses already by the programme deduction R_tot=MLR (S083 Proposition 1.1, inherited from SRC-0071's preprint), because endomorphism randomness ⊆ R_tot. R₂=MLR obtained by a NON-orientation mechanism would not imply Corollary A3, since no inclusion between R₂ and automorphism randomness is known.

## 3. Proof gate 2 (equality, continued) — the left-c.e. instance carried to its decisive condition

Throughout, α is left-c.e. and not eventually constant (every CR source has this property), and (a_k) is a computable nondecreasing sequence of dyadic rationals with limit α. Then a_k<α for every k, since α is not dyadic. For σ∈2^{<ω} and a dyadic rational r, ρ(r) is the terminating binary expansion of r. On sequences that are not eventually constant, lexicographic order coincides with real order. For a strictly increasing computable g put W^{a,g}_m := {ρ(a_{g(k)})↾L : m ≤ L ≤ k}.

### 3.1 One-sidedness holds in every frame

**Proposition L1 (larger-candidate soundness).** Let K be any computable fair homeomorphism and h a hold. Let x^<, x^> be the two raw completions of the hold in lexicographic order (one of them is α). If some σ∈W^{a,g}_m with m≥1 satisfies σ⊑x^> and σ⋢x^<, then α=x^>.

*Proof.* Let δ be the first position where x^< and x^> differ, so x^<_δ=0 and x^>_δ=1. Since σ⊑x^> and σ⋢x^<, |σ|>δ and σ↾(δ+1)=x^<↾δ1. Write σ=ρ(a_{g(k)})↾L; then a_{g(k)} ≥ x^<↾δ10^∞ as reals. If α=x^< then, as α is not eventually 1, α < x^<↾δ10^∞ ≤ a_{g(k)} < α, a contradiction. ∎

Hence, in EVERY frame, the S092 reader with selection Sel_> ("bet only when the proposed completion is the lexicographically larger one") never makes a wrong selected bet on α. The selection is computable from the transcript, since the reader has both raw windows and they are already separated. It destroys α exactly when infinitely many reached holds are resolved in favour of the larger completion. S092 Lemma 5.2 is the raw-frame case.

### 3.2 The window criterion at an arbitrary computable precision

Raw frame (K=id). Fix a computable N with N(h) ≥ h+1, use the level n(h):=N(h), and put p_h:=α⊕e_h (the partner).

**Proposition L2 (window criterion).** Let h be a reached hold of T=T_{id,W^{a,g},N}.
(i) If α_h=0, the reader resolves h with proposal 0, which is correct.
(ii) If α_h=1, the reader proposes 1 if and only if ¬Land_N(h), where

  Land_N(h) :⟺ ∃k≥N(h): ρ(a_{g(k)})↾N(h) = p_h↾N(h).

If Land_N(h) holds, the resolution is a wrong proposal 0 or a tie.

*Proof.* Every hold is resolved: for large k, ρ(a_{g(k)})↾N(h)=α↾N(h) with k≥N(h), and this string is admissible once M≥N(h).
(i) The partner has prefix α↾h1, so a string of W of length ≥h+1 covering it would come from an approximation ≥α↾h10^∞>α, which is impossible.
(ii) A string of W at level N(h) covering p_h has length L≥N(h)>h, so it determines ρ(a_{g(k)})↾N(h)=p_h↾N(h) with k≥L≥N(h), i.e. Land_N(h). Conversely such a k gives ρ(a_{g(k)})↾N(h)∈W_{N(h)}, which covers p_h and not α (they differ at h<N(h)). Any approximation covering α at a length ≥N(h) is ≥α↾h10^∞, while any approximation with prefix p_h↾N(h) is below α↾h10^∞. Monotonicity puts every partner-covering index strictly before every α-covering index. So the partner, if covered at all, is seen strictly first (proposal 0) or in the same check (tie). Otherwise only α is ever covered (proposal 1). ∎

S092 Lemma 5.3 is the case N(h)=h+1, where ¬Land_{h+1}(h) is the jump-over of the whole interval [α↾h0]_ℝ. Since [p_h↾N]_ℝ⊆[p_h↾(h+1)]_ℝ, Land_N(h) ⇒ Land_{h+1}(h). At every fixed hold, the non-landing condition for a large computable N asks only that no approximation fall into a window of width 2^{−N(h)} around α−2^{−h−1}. That is strictly weaker than skipping the whole 2^{−h−1}-interval.

**Corollary L3.**
(a) With Sel₁=Sel_>, the reader destroys α on a singleton fibre iff infinitely many reached holds h have α_h=1 and ¬Land_N(h).
(b) If α∈R₂ (in particular if α is MLR), then for EVERY computable strictly increasing g and EVERY computable N≥h+1, Land_N(h) holds at all but finitely many reached holds with α_h=1, and infinitely many reached holds with α_h=1 land. For MLR α this strengthens S092 Corollary 5b from whole-interval jump-overs to windows of every computable precision.

*Proof.* (a) Proposition L2, legality (S092 Lemma 1.1), and the fact that every selected bet is correct. (b) Infinitely many non-landing reached 1-holds would destroy α by (a). Every hold resolves. A tie is a landing 1-hold, and a wrong bet occurs only at a landing 1-hold. If infinitely many resolutions are ties, we are done. Otherwise infinitely many resolutions are bets (Sel≡true), whose error stream is computably random (S092 Corollary 2 with S084 Theorem 1), hence contains infinitely many errors. ∎

### 3.3 A failed measure route

A Solovay-test argument against landing was tried. The landing sets E_h:={flip_h(ρ(a_{g(k)})↾N(h)) : k≥N(h), ρ(a_{g(k)})_h=0} are uniformly c.e., α∈[E_h] whenever h is a landing 1-hold, and λ[E_h] ≤ δ_h+2^{−N(h)} with δ_h:=α−a_{g(N(h))}, because the approximations from index N(h) on sweep an interval of length δ_h.

The route fails for every non-computable α. The sequence (δ_h) is non-increasing, and summability would give h·δ_{2h} ≤ Σ_{j≥h}δ_j ≤ S, a computable modulus of convergence (with S any rational bound on the sum). So Σ_h δ_h=∞ for every non-computable α, and measure considerations alone can never exclude landing. In particular, "Σ_h δ_h=∞ for MLR α", which the first version of this argument yielded, is a triviality and is recorded only as a failed attempt.

### 3.4 Monotone orientation does not transfer beyond Δ⁰₂

**Proposition L4.** If J(z) is left-c.e. for some computable fair homeomorphism J, then z ≤_T ∅′. Some z∈CR∖MLR is not ≤_T ∅′. Hence no transfer of one-sided monotone orientation through frames can reach all of CR∖MLR.

*Proof.* z=J⁻¹(J(z)) ≤_T J(z) ≤_T ∅′. By THM-0014 (SRC-0028, recorded STATEMENT_INSPECTED), every high degree contains a computably random non-MLR set. The degree of ∅″ is high, so it contains some z∈CR∖MLR with z ≡_T ∅″, hence z ≰_T ∅′. ∎

Within Δ⁰₂ the left-c.e. instance remains open. Its exact obligation is to find, for a given left-c.e. α∈CR∖MLR, a frame, a computable approximation subsequence and a computable precision with infinitely many reached holds at which α is the larger completion and the approximation skips the partner window. Corollary L3(b) shows this must use non-MLR-specific structure: computable randomness alone cannot exclude landing, since MLR sources land.

### 3.5 Literature calibration (abstract level; no proof dependence)

Non-landing asks the approximation to make a jump across a small window at the crossing of α−2^{−h−1}, i.e. not to "creep" there. Speedability (Merkle–Titov) is a related acceleration notion for left-c.e. approximations. A bounded web search located:
* Hölzl–Janicki, *Benign approximations and non-speedability* (arXiv:2303.11986), recorded as SRC-0073, ABSTRACT_INSPECTED. The abstract states that the paper resolves Merkle and Titov's question whether, among left-c.e. reals, Martin-Löf randomness is equivalent to non-speedability.
* Barmpalias–Fang–Merkle–Titov, *Speedability of computably approximable reals and their approximations* (arXiv:2603.26484), recorded as SRC-0074, ABSTRACT_INSPECTED, with an introduction excerpt seen through the search tool. The excerpt states that this question was answered in the negative by Hölzl and Janicki.

At this access level these sources indicate only that "non-MLR ⇒ some acceleration" fails for left-c.e. reals in general. Whether the counterexamples are computably random, and whether speedability would produce window skips at reached holds, were not determined. Nothing in §3 depends on these records, and no priority, novelty or openness inference is drawn.

## 4. Proof gate 3 — attacking (AR-cover), and searching for counterexamples

The strongest plausible lemma the equality route needs is (AR-cover): every z∈CR∖MLR is Turing autoreducible after some computable fair homeomorphism. By Theorem A this is exactly GOL.

### 4.1 Families derived from a failing test

Let V be any ML test with z∈⋂_m V_m, K a frame, and n computable with n(h)≥h+1 and so large that every cylinder of V_{n(h)} is longer than a computable bound on the first raw position where the two completions of hold h can differ. (Such a bound exists in every frame with computable partner onset, e.g. raw, D′, K_mix, K′_mix.) Then every V_{n(h)}-cylinder containing one completion excludes the other. Hence the partner is separately covered at (h,n(h)) exactly when ψ_h(z)∈V_{n(h)}, i.e. z∈ψ_h(V_{n(h)}). The derived family (ψ_h(V_{n(h)}))_h is uniformly c.e. with Σ_hλ ≤ Σ_h 2^{−n(h)} < ∞, so it is a Solovay test. A non-MLR source may fail it; nothing forces passing.
* For a universal V the derived test contains every non-MLR point (S092 Proposition 3).
* Removing from V the cylinders whose partners were enumerated first produces the race sub-tests, which are circular (S092 §3.3).
* Choosing V adapted to z is exactly the autoreducibility question again.

No construction of V (or of any Σ⁰₁ asymmetry) from an arbitrary failing test was found.

### 4.2 Capital-comparison self-readers

For any finite family of computable martingales, a self-avoiding Φ_cap can predict, at hold h, the completion with the smaller weighted capital at a computable time T(h). Φ_cap autoreduces every source produced by a construction that systematically keeps the lower-capital completion at frame-K holds. This explains why potential-minimizing constructions are read by self-readers (S083, S087 Theorem 8, S090). For a source whose completions' capitals are not systematically ordered, Φ_cap has no reason to succeed. This is analysis; it gives neither (AR-cover) nor its negation.

### 4.3 Counterexample search by category, and why it cannot finish

For a frame K and a self-avoiding Φ put AR(K,Φ):={x : Φ^{K(x)}(h)↓=K(x)_h for all but finitely many h}. Then AR(K)=⋃_Φ AR(K,Φ).

**Lemma G (category).** Each AR(K,Φ) is meager, so AR^iso is meager. Every 2-generic sequence lies outside AR^iso.

*Proof.* For h₀∈ℕ let D_{h₀} be the union of
* the open set of x such that Φ^{K(x)}(h)↓≠K(x)_h for some h≥h₀, and
* the interior of the set of x such that Φ^{K(x)}(h)↑ for some h≥h₀.

D_{h₀} is open. It is dense. Given a cylinder [τ], choose h≥h₀ so large that ψ_h fixes the first |τ| raw bits of every point. This is possible because K⁻¹(u)↾|τ| depends only on u↾μ(|τ|), where μ is a computable modulus of K⁻¹, so h≥μ(|τ|) suffices; then ψ_h([τ])=[τ].
* If Φ^{K(x)}(h)↓ for some x∈[τ], let y be whichever of x, ψ_h(x) has K(y)_h≠Φ^{K(x)}(h). Since K(ψ_h(x))=K(x)⊕e_h and Φ is self-avoiding, Φ^{K(y)}(h)=Φ^{K(x)}(h)≠K(y)_h. A neighbourhood of y inside [τ] lies in the first part of D_{h₀}.
* Otherwise Φ diverges at h on all of [τ], so [τ] lies in the second part.

A point in every D_{h₀} makes Φ fail at infinitely many h, so it is outside AR(K,Φ). For genericity, use the set of strings S_{h₀} := {σ : ∃h≥h₀ [Φ is wrong at h on all of [σ], witnessed by a finite computation]} ∪ {σ : ∃h≥h₀ ∀x∈[σ] Φ^{K(x)}(h)↑}. The first part is Σ⁰₁ by compactness of [σ]; the second is Σ⁰₂, since divergence on all of [σ] at a fixed h is Π⁰₁. By the density argument every string has an extension in S_{h₀}: in the first case take a long enough cylinder around y fixing the finite use. A 2-generic x therefore meets S_{h₀} for every h₀ and every (K,Φ), with K ranging over indices of computable fair homeomorphisms. A prefix of x in S_{h₀} makes Φ wrong or divergent at some h≥h₀ on x. ∎

**Lemma M (no Baire property).** CR∖MLR is meager in itself.

*Proof.* Let d be the computable martingale with d(σ0)=(3/2)d(σ), d(σ1)=(1/2)d(σ), d(∅)=1, and F_c:={x : d(x↾n)≤2^c for all n}. Each F_c is closed, and CR∖MLR ⊆ ⋃_c F_c. Each F_c∩(CR∖MLR) has empty interior in CR∖MLR. Indeed, if [τ]∩(CR∖MLR)≠∅, choose j with d(τ0^j)>2^c; then [τ0^j] meets CR∖MLR (a nonempty class closed under finite changes, hence dense) and is disjoint from F_c. So CR∖MLR is a countable union of closed nowhere-dense subsets of itself. ∎

So a counterexample to (AR-cover) cannot be obtained by category alone. Lemma G produces generic counterexamples, which are not computably random, and Lemma M blocks running the argument inside CR∖MLR. A counterexample must come from a measure-theoretic construction with forcing steps (§6). Neither a proof nor a counterexample of (AR-cover) was obtained.

## 5. Proof gate 4 — the full-family quantifier: not crossed

(EQ) follows from GOL ⟺ (AR-cover) (Theorem A and S092 Proposition 1.2); (AR-cover) is neither proved nor refuted. A proof of (AR-cover) would also yield Corollary A3, i.e. automorphism randomness = MLR. An equality proof avoiding this must use non-orientation F₂ mechanisms (non-scan maps, or fractional rather than all-correct orientation). None was found. No coverage theorem for every CR∖MLR source was obtained, and no obstruction to one construction is extrapolated.

## 6. Proof gate 5 — the opposite alternative: refuting GOL and the road to a survivor

### 6.1 The minimal target

Every z∈R₂∖MLR lies outside AR^iso (Corollary A2). The weakest necessary step towards (SEP) is therefore

  (¬AR-cover) ∃z∈CR∖MLR∖AR^iso,

which already refutes GOL and closes the S092 equality route. It is much weaker than (SEP): it needs only that every self-avoiding Φ fail infinitely often in every frame, not computably random error streams (S084), and it needs protection only of the identity-frame martingales (for CR), not of all one-hole scans in all frames.

### 6.2 The forcing step and its exact cost

**Proposition F (pairing forcing).** Let P be clopen, K a frame, Φ self-avoiding, and h≥H(P), where H(P) is computable from P and the modulus of K⁻¹, so that ψ_h(P)=P. Let C_h:={x∈P : Φ^{K(x)}(h)↓}, R_h:={x∈C_h : Φ right at h}, Wr_h:={x∈C_h : Φ wrong at h}. Then:
* C_h is open and ψ_h-invariant; ψ_h maps R_h onto Wr_h, and λ(R_h)=λ(Wr_h);
* every finite stage of Wr_h is a clopen subset of P on which Φ is wrong at h;
* if C_h=∅, then every point of P makes Φ diverge at h.

For any width-two strategy (G,d) with the consistency potential of S089 Definition 1.1, and any ψ_h-invariant clopen Q⊆C_h on which Φ's computation at h halts within a bounded use (so that A:=Q∩Wr_h and B:=Q∩R_h=ψ_h(A) are clopen):

  λ(A)Ψ(A,t)+λ(B)Ψ(B,t) = λ(Q)Ψ(Q,t) + λ(Q)γ(Q;A,B,t),

where γ is the capital-weighted mass of the time-t output cells meeting both A and B. Hence

  Ψ(A,t) = (Ψ(Q,t)+γ(Q;A,B,t))·(1+β), β := (Ψ(A,t)−Ψ(B,t))/(Ψ(A,t)+Ψ(B,t)).

So the cost of forcing Φ wrong is the split weight together with the **specified-side bias** β∈[−1,1].

*Proof.* The first three items follow from self-avoidance and K(ψ_h(x))=K(x)⊕e_h, as in Lemma G; ψ_h is λ-preserving. The identity is the counting identity c^Q=c^A+c^B−[cell meets both] of S082 Lemma 2.3 / S089 Definition 1.1, using λ(A)=λ(B)=λ(Q)/2. ∎

For identity-frame (monotone) strategies the split weight vanishes once t exceeds the first raw position where x and ψ_h(x) differ, because their time-t cells are cylinders [x↾t]. All of the cost is then the bias.

**The bias cannot be bounded in one step.** Suppose a protected monotone martingale makes one all-in bet inside the differing window on a bit whose two branch values are complementary, as for every window bit in the tail-coded frame D′. Then exactly one branch survives with doubled capital. A self-avoiding Φ that predicts the dead branch makes the forced side carry the whole capital: β=1 and the cost factor is 2. Any construction must therefore amortize. It must tax such strategies (min-side fixings where they bet, outside the forcing windows) before forcing.

**What amortization handles, and what it does not.**
* Against protected strategies whose large bets lie on a computable set not adapted to the construction, the construction chooses its forcing windows sparsely and spends the gaps on min-side fixings. All-in bettors are killed once. Fractional bettors are taxed by (1−|β|) per taxed bet against (1+|β|) per forced window, so the potential stays bounded.
* The obstruction is the protected **self-reader**. It simulates the guessed runs, so it can align its bets with the construction's own forcing windows (and cancel them elsewhere, against the min-side taxation). This is the familiar S083/S087/S090 phenomenon, now appearing already at the level of the much weaker target (¬AR-cover) and with only identity-frame protection.

### 6.3 Conditional reduction

**Amortized Specified-Side Cost Lemma (ASSCL; UNPROVED).** For every finite weighted family of total rational computable monotone martingales in savings form, every clopen state P with weighted potential Φ_pot(P,t), every frame K, every self-avoiding Φ, every h₀ and every ε>0, one of the following holds:
* there are a clopen P′⊆P, a time t′ and h≥h₀ such that Φ is wrong at h on all of P′, Φ_pot(P′,t′) ≤ Φ_pot(P,t)+ε, and P′ contains cylinders on which further coordinate fixings remain possible; or
* Φ diverges on all of P at every h≥max(h₀,H(P)).

**Proposition S (conditional; proof sketch).** ASSCL implies (¬AR-cover); hence ASSCL implies that GOL is false.

*Sketch.* Run S082 §4 with only identity-frame protected strategies, clopen states as in S089, coordinate fixings beyond the current cylinder lengths (each halves the measure; free for monotone strategies once read), and interleaved forcing stages for requirements (K,Φ,h₀).
* Validity of K is guessed as in S082 (Π⁰₂).
* Whether the Σ⁰₁ search for a cheap wrong extension halts is guessed by one additional bit per forcing stage. On a "halts" guess the run waits; wrong guesses may diverge, which is harmless. On a "does not halt" guess the run skips. On the true run, ASSCL turns non-halting into divergence of Φ on the whole current state.
* Forcing only shrinks states and raises Φ_pot by at most ε_i=2^{−i−5}, so S082 Propositions 4.1–4.3 go through.

The resulting z is computably random (bounded savings capital for every protected strategy), not ML-random (the guessed-run test), and fails every valid (K,Φ) infinitely often. A complete proof would only re-verify S082 §4 in this setting; it is not claimed here, since its hypothesis ASSCL is open. ∎

### 6.4 From (¬AR-cover) to (SEP)

Even with ASSCL, the source of Proposition S need not lie in R₂. Survival additionally requires the S084 computably random error stream for every infinitely resolving reader, and bounded capital for every fractional one-hole strategy in every frame and every non-scan F₂ map. Those are the obligations S087–S091 met only for restricted families, and on which the rigid three-involution core (S089, conditional on Conjecture R) and nonlinear self-readers (S090/S091) act. The decisive separation obligation therefore remains as recorded in S092 §5, now with a strictly weaker first milestone: ASSCL, or any other construction of a CR∖MLR source outside AR^iso.

## 7. Proof gate 6 — adversarial validation (summary)

No resolution was obtained, so gate 6 validated the proved components; details are in `P4-S093_VALIDATION.md`.
* **Theorem A.** Checked in both directions, including the race form, ties, the history-independence of the canonical schedule, the use of K⁻¹'s modulus, finite patching, and the self-avoidance identity Φ^{v⊕e_h}(h)=Φ^v(h).
* **Corollary A3.** Uses only recorded inclusions.
* **Propositions L1–L4.** Checked against non-dyadic edge cases. Lemma G and Lemma M were checked, as were the counting identity of Proposition F and the conditional status of Proposition S.

`phase4/P4-S093_AUTOREDUCIBILITY_AUDIT.py` checks the finite components in exact arithmetic; it cannot establish infinite statements.

## 8. Disposition

**Proved:** Theorem A, Corollaries A1–A3, Propositions L1, L2, L4, Corollary L3, Lemmas G and M, Proposition F.

**Conditional:**
* R₂=MLR (indeed OH^iso=MLR, and then automorphism randomness = MLR) under (AR-cover) ⟺ GOL.
* (¬AR-cover), hence the falsity of GOL, under ASSCL (Proposition S, sketched).
* Every left-c.e. CR∖MLR source lies outside R₂ under the window-skip property of §3.4.

**Refuted / failed routes:** measure (Solovay) exclusion of landing (trivial for non-computable sources); category construction of a GOL counterexample (Lemma M); single-step specified-side cost bounds (all-in example); frame transfer of monotone orientation beyond Δ⁰₂ (Proposition L4).

**Unresolved:** R₂ versus MLR; (AR-cover)/GOL; ASSCL; the left-c.e. window-skip property; any survivor; Conjecture R; R₂ versus OH^iso, U(H), X∈OH and fixed-S preservation (kept separate and untouched).

**Smallest remaining global obligations.**
* *Equality:* (AR-cover) — every z∈CR∖MLR is Turing autoreducible after a computable fair homeomorphism. Any proof also decides the automorphism-randomness part of QST-0002 (Corollary A3). Alternatively, a non-orientation F₂ destroyer for every CR∖MLR source.
* *Separation:* first ASSCL (or any z∈CR∖MLR∖AR^iso), which must defeat protected self-readers aligned with the construction's own forcing windows; then full F₂ survival.

**Frozen.** The entire incoming landscape; S084's whole-error-stream requirement; S085's representation-only c(n); S086's ∀F∃x and common-factor obstruction; all S087–S092 results with their theorem/experiment distinctions; the exact frames including K′_mix's preceding-control offset; original CR Y; unchanged globally use-clipped self-avoiding wtt M; repeated three-bit H with A=[101;110;111]; X=H⁻¹(Y); PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. No escrow, hazard, residue, unit-column, record-only z₀ or multi-hole detour; no spectral numerics or local frustration work. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No novelty, external openness, priority, publication or outreach claim. Owner/external blocker: NONE.
