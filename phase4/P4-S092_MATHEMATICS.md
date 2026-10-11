# P4-S092 — Partner orientation: a universal reader, the global entanglement condition, and one-sided orientation for left-c.e. sources

Date: 2026-10-11. Phase 4 Mathematics ONLY; selected CAND-01.
Incoming live main: `ec2c6ff1b5050b1b324d10b007843b1336bd7010` (owner handoff amendment, documentation only), sole parent `6633f88ba8a0826442618f5062cb2d74b83c9e86` (S091 atomic close), whose sole parent is `971b3ccef56fc5654c857a32e882342c80e325c2`.

**Disposition: R₂ versus MLR is NOT decided.** A sustained attempt was made through all six internal proof gates. The lead route was equality through *orientation readers*; it was carried to a single universally quantified obligation (the Global Orientation Lemma, §3), which was neither proved nor refuted. The opposite route (a survivor) was then attempted using the new necessary condition as a design constraint, and stalled at the invariance–neutralization dichotomy already recorded in S089, now sharpened.

Proved this session:

* **Theorem 1 (orientation reader).** For every computable fair homeomorphism K, every uniformly c.e. family of cylinders W=(W_m), every computable level function n and every computable bet-selection rule, an explicit total computable one-hole scan of K(x) is legal on every transcript. If, on a source x, x is *separately covered* at every hold and its hold partners are separately covered at only finitely many selected holds, the composite G∈F₂ destroys x on a singleton fibre.
* **Corollary 2 (global partner entanglement of survivors).** Every z∈R₂ (indeed every z∈OH^iso) satisfies: in every computable frame, for every uniformly c.e. cylinder family and every computable level function, separate coverage of z at all levels forces separate coverage of z's hold partners infinitely often. With S084, the induced error stream is computably random.
* **Proposition 3.** Universal ML tests violate the orientation hypothesis for every non-MLR source in every frame whose partner differences start computably early; any equality proof through Theorem 1 must use structurally non-universal families.
* **Lemma 4 (entry-time dominance).** For x∈CR and any ML test containing x in every level, the entry stages dominate every computable function. Hence computably time-bounded orientation is void on CR sources.
* **Proposition 5 (one-sided orientation for left-c.e. sources).** For a left-c.e. source and its own approximation family, every exclusive coverage of the 1-candidate is correct. Destruction is equivalent, for this reader, to infinitely many *late jump-overs* at 1-bit holds; *early* agreement at 1-bits is ruled out by computable randomness (Lemma 5a); for left-c.e. MLR sources jump-overs are finite for every computable subsequence (Corollary 5b).

Not proved: R₂=MLR; z∈R₂∖MLR; the Global Orientation Lemma; jump-overs for left-c.e. CR∖MLR sources; any survivor; Conjecture R. No new class inclusion is claimed.

## 0. Entry, review and challenge of immediate dependencies

Independent `git ls-remote` read of `refs/heads/main` gave the incoming SHA; commit metadata gave its sole parent as the S091 close, whose sole parent is S090's close, exactly as the prompt states. The amendment changes STATE `next_transition`, adds `next_session_owner_direction`, and rewrites the handoff; mathematics and the completed-session counter are unchanged. REST listing of pull requests (all states) is empty; zero check runs and zero commit statuses on the incoming SHA. Side branches are historical work branches; `docs/strengthen-r2-mlr-handoff` equals main. No S092 file or branch existed. The incoming prompt is byte-identical to `authoritative/NEXT_SESSION_PROMPT.md` except a final newline and is archived as `P4-S092_INCOMING_HANDOFF.md` with SHA256 `d892903904fe352ba9a40d9118be61ea9dd2f57a46a1e70205b0381cf24cdaa0`.

Reviewed: repository authority, SESSION_PROTOCOL, gate and source policies, both Phase-4 pivots, CAND-01 selection and Gate-3 PASS, and S082 §§2–6 (including §6.3), S083, S084, S085, S086, S087 (including §6.1–6.3), S088 §§0–1, S089 Theorem 1 and §5, S090, S091 in detail, with S003–S008, S011–S012 and S032–S033 through the cumulative authority summaries. This is not a claim to have re-proved historical mathematics.

Sources are used only at recorded access: SRC-0015, SRC-0019, SRC-0060, SRC-0069 and SRC-0071 STATEMENT_INSPECTED (with previously recorded particular proof inspections); SRC-0070 and SRC-0072 ABSTRACT_INSPECTED; SRC-0071's journal version METADATA_ONLY. R_tot=MLR remains the S083 programme deduction from the inspected preprint. THM-0014 (SRC-0028, STATEMENT_INSPECTED) is cited only as the catalogued statement that high degrees contain left-r.e. computably random non-MLR sets; nothing below depends on it except the remark that the class treated in Proposition 5 is not empty as recorded there. No external literature was retrieved this session.

**Challenge of S090/S091 before use.** S090 Theorem 7 and S091 Theorem 4/Corollary 5 are used only as calibration. Their readers are instances of Theorem 1 below (frame K_mix, the construction's guessed-run equations as the cylinder/affine family, selection = all resolutions, all-in bets). Their fooling and stall covers are exactly the failure sets of the hypotheses of Theorem 1 on the selected witness; the selected-witness character is confirmed: neither result asserts anything about non-selected points. S091 Proposition 6's finite countermodels and the exact K′_mix preceding-control offset are retained unchanged. No error was found requiring a documented correction.

## 1. Proof gate 1 — the exact finishing statements and the dependency plan

F₂ is the committed class: everywhere-total computable λ-preserving maps G:2^ω→2^ω with |G⁻¹(y)|≤2 for every y. Computable martingales are rational-valued (the standard equivalence with computable real-valued martingales is used as in S083/S084).

**Equality.** It suffices to prove

  (EQ) ∀z∈CR∖MLR ∃G∈F₂ ∃ computable martingale d: d succeeds on G(z).

G may be chosen depending on z among genuinely computable maps (countably many indices); no noncomputable G. With MLR⊆R₂ (frozen) this gives R₂=MLR.

**Separation.** It suffices to prove

  (SEP) ∃z∉MLR ∀G∈F₂: G(z)∈CR,

with non-ML-randomness and survival for the same z, and explicit oracle use.

**Dependency plan (lead route: equality).** Every known destroyer of a CR∖MLR point (S011, S083, S087 Theorem 8, S090) is a one-hole scan in some frame that *orients a held bit*: it waits until some c.e. evidence separates the two completions of the hold and bets on the evidenced one. Petrović's universal pair (R_tot=MLR) uses unbounded fibres (S083 §1, S085), and S086 excludes single maps and rank-one families. So the natural equality route is:

1. a uniform *orientation reader* for an arbitrary frame and arbitrary c.e. evidence (Theorem 1);
2. the **Global Orientation Lemma** (GOL): every z∈CR∖MLR admits a frame and a c.e. family in which z is separately covered at every level while its hold partners are separately covered only finitely often;
3. 1+2 ⇒ (EQ).

Step 2 is the genuinely missing global implication. If it fails, its failure gives a structural property every survivor must have (Corollary 2), which is the entry point for the separation route.

## 2. Proof gate 2 — the orientation reader and its decisive obligation

### 2.1 Frames, partners, separate coverage

Let K be a computable fair homeomorphism (K and K⁻¹ total computable; K⁻¹ has a computable modulus μ by effective compactness). For a virtual coordinate h write the **partner involution**

  ψ_h := K⁻¹∘flip_h∘K,   flip_h(v):=v⊕e_h.

ψ_h is a computable fair involution; x and ψ_h(x) are the two raw completions of a held virtual bit h.

Let W=(W_m)_{m∈ℕ} be a uniformly c.e. family of finite binary strings, W_{m,t} its stage-t part (finite, computable in m,t). A string σ **separates x from x′** if x∈[σ] and x′∉[σ]. Say x is **separately covered at (h,m)** if some σ∈W_m separates x from ψ_h(x). Say the **partner of x is separately covered at (h,m)** if some τ∈W_m separates ψ_h(x) from x.

Let n:ℕ→ℕ be computable (the level used at hold h) and let Sel be a computable predicate of a finite scan transcript together with a proposed bit (the bet-selection rule; "always true" is allowed).

### 2.2 The reader

For a virtual input v, the scan T=T_{K,W,n,Sel} keeps a **hold** h and a **frontier** M>h; its read set is [0,M)∖{h}. Initially h=0, M=1. At output time t:

* Form the two virtual candidates u^b∈2^M (b∈{0,1}) agreeing with the read bits on [0,M)∖{h} with u^b_h=b. Let ℓ(M):=max{ℓ: μ(ℓ)≤M} and ρ^b := the raw prefix of length ℓ(M) determined by u^b (computable from u^b through K⁻¹).
* Put c_b := 1 iff some σ∈W_{n(h),t} with |σ|≤ℓ(M) satisfies σ⊑ρ^b and σ⋢ρ^{1−b}.
* If exactly one c_b=1: **resolve**: query h. If Sel(transcript,b) holds, the stake is all-in on v_h=b; otherwise zero stake. Set h:=M, M:=M+1.
* If c_0=c_1=1: **tie**: query h at zero stake; h:=M, M:=M+1.
* If c_0=c_1=0: query the filler M at zero stake; M:=M+1.

The base martingale d₀ starts at 1, is unchanged at zero-stake reads, and on a selected resolution sets children 0 and 2d₀ according to the bet. The **restart martingale** is S084 Lemma 3.2's

  d(u) := Σ_{j≤|u|} 2^{−j−1}M_j(u) + 2^{−|u|−1},

where M_j copies d₀'s selected bets starting at output time j (with capital 1 at time j).

**Lemma 1.1 (legality).** T is a total computable adaptive no-repeat scan and every infinite transcript leaves at most one coordinate unread. Hence G:=F_T∘K∈F₂. d₀ and d are total rational computable martingales.

*Proof.* Each step performs finitely many decidable checks: W_{n(h),t} is a finite list, ℓ and ρ^b are computable, and string prefix tests are decidable. Every query is either the current unread hold or the current unread frontier, so no repeats. If resolutions or ties occur infinitely often, holds strictly increase and every coordinate is read; otherwise the last hold is the only unread coordinate. S008's scan fibre formula gives fibres of size ≤2, preserved by composing with the fair homeomorphism K. The stake at each read is decided before the bit is read and the two children average to the parent (fair-child identity, also after capital 0); d is a convex combination with the exact tail term, as in S084. ∎

### 2.3 The orientation theorem

**Theorem 1 (orientation reader).** Let x∈2^ω, v=K(x). Assume

  (O1) for every hold h reached by T on v, x is separately covered at (h,n(h));
  (O2) for all but finitely many holds h reached by T on v, the partner of x is NOT separately covered at (h,n(h));
  (O3) Sel holds at infinitely many resolutions of T on v whose proposed bit is v_h.

Then T resolves infinitely often on v, all but finitely many selected bets on v are correct, d succeeds on G(x)=F_T(v), and G⁻¹(G(x))={x}. In particular G(x)∉CR, K(x)∉OH and x∉R₂.

*Proof.* Fix a reached hold h. While h is held, M→∞ and t→∞ (fillers are read at each unresolved step). By (O1) some σ∈W_{n(h)} separates x from ψ_h(x); once σ is enumerated and ℓ(M)≥|σ|, σ⊑ρ^{v_h} (as ρ^{v_h} is a prefix of x, the raw completion with the true hold value) and σ⋢ρ^{1−v_h} (as ρ^{1−v_h} is a prefix of ψ_h(x) and ψ_h(x)∉[σ], provided ℓ(M)≥|σ|). So c_{v_h}=1 eventually and h is resolved or tied. Hence every reached hold is left, the holds increase without bound, and there are infinitely many resolutions or ties.

At a hold satisfying (O2), c_{1−v_h} is never 1: c_{1−v_h}=1 would give τ∈W_{n(h)} with τ⊑ρ^{1−v_h}, hence ψ_h(x)∈[τ], and τ⋢ρ^{v_h} with |τ|≤ℓ(M), hence x∉[τ], i.e. separate coverage of the partner. So such a hold is resolved (not tied) with proposed bit v_h, which is correct. Only the finitely many holds violating (O2) can produce ties or wrong proposed bits. By (O3) there are infinitely many selected correct bets and only finitely many selected wrong ones. After the last wrong selected bet, every later-started account M_j doubles at each subsequent selected resolution and never drops, so d is unbounded. Infinitely many resolutions read every virtual coordinate, so the virtual fibre, and hence the G-fibre through the homeomorphism K, is {x}. ∎

**Remarks.** (a) W need not be a test; no measure bound is used. (b) S083's T*, S087 Theorem 8 and S090's G_* are instances (with W the guessed-run constraints, n(h) chosen through r(q,m), Sel≡true); their fooling and stall sets are exactly the failure sets of (O2) and (O1) on the selected witness. (c) The level n(h) may grow arbitrarily; only computability is used.

### 2.4 The decisive obligation, and its contrapositive

Under Sel≡true, (O3) follows from (O1)+(O2). Theorem 1 therefore reduces equality to:

**Global Orientation Lemma (GOL; OPEN).** For every z∈CR∖MLR there are a computable fair homeomorphism K, a uniformly c.e. cylinder family W and a computable n such that z is separately covered at (h,n(h)) for every h, and the partner of z is separately covered at (h,n(h)) for only finitely many h.

**Proposition 1.2.** GOL ⇒ R₂=MLR (indeed OH^iso=MLR).

*Proof.* Theorem 1 with Sel≡true destroys every z∈CR∖MLR; MLR⊆R₂⊆OH^iso are frozen. ∎

**Corollary 2 (global partner entanglement).** Let z∈OH^iso (in particular z∈R₂). For every computable fair homeomorphism K, every uniformly c.e. cylinder family W and every computable n: if z is separately covered at (h,n(h)) for every h, then the partner of z is separately covered at (h,n(h)) for infinitely many h. Moreover, for the reader T_{K,W,n,true} on K(z): if infinitely many holds are resolved with a bet, the sequence of bet errors is computably random (hence has limiting frequency ½); otherwise all but finitely many holds are ties, each of which is a separate partner coverage.

*Proof.* The first assertion is the contrapositive of Theorem 1 (Sel≡true), since z∈OH^iso gives K(z)∈OH. For the second, the resolution flag and proposed bit are computable from the preceding transcript of the output y=F_T(K(z))∈CR, so S084 Theorem 1 applies to the selected bets. A tie means c_0=c_1=1, i.e. separate coverage of both candidates, in particular of the partner. ∎

Corollary 2 is a necessary condition on ANY survivor, quantified over all frames and all c.e. families simultaneously; it is not tied to a construction or a frame. It is the entry point for §5.

**Timing form.** The proof of Theorem 1 uses (O2) only to guarantee that, at almost every reached hold, the first check at which some candidate is separately covered covers the true candidate exclusively. Call this (O2′) (the reader *wins the race* at h). Theorem 1 holds verbatim with (O2′) in place of (O2). (O2′) refers to enumeration times and is the form in which S087 §6.1's race discussion lives.

## 3. Proof gate 3 — attacking GOL; failed repairs; one successful one-sided repair

### 3.1 Universal evidence is always entangled

Say a frame K has **computable partner onset** L if L is computable and min(x⊕ψ_h(x))≤L(h) for all x,h. The raw frame (L(h)=h), D′ (L(h)=h), and both exact nonlinear frames K_mix and K′_mix (the raw difference of the hold at virtual 2q+1, resp. 2q, starts at raw coordinate 2q+1, resp. 2q) have computable onset.

**Proposition 3.** Let K have computable onset L, let U be an ML test whose intersection is exactly the non-MLR sequences, and let n be computable with n(h)>L(h) for all h. Then for every non-MLR x and every h, both x and ψ_h(x) are separately covered at (h,n(h)). Hence (O2) fails at every hold for every non-MLR source.

*Proof.* Every σ∈U_m satisfies 2^{−|σ|}≤λ(U_m)≤2^{−m}, so |σ|≥n(h)>L(h) for σ∈U_{n(h)}; such a cylinder contains at most one of x, ψ_h(x), since they differ at a coordinate ≤L(h). ψ_h is a computable fair homeomorphism, so ψ_h(x) is non-MLR exactly when x is (THM-0035 in both directions). Both lie in U_{n(h)}, each through a separating cylinder. ∎

So any proof of GOL must use families that are *not* closed under the partner maps on their intersection. Universal evidence gives only the race form (O2′), decided by enumeration order (S087 §6.1). Finite pinning does not help: for a fixed σ₀⊑z, W_m:=U_m∩[σ₀] separates the partner of z only for the finitely many h with min(z⊕ψ_h z)<|σ₀| whenever L(h)→∞ is forced by injectivity of h↦onset; every partner beyond |σ₀| is covered exactly as in Proposition 3. A c.e. family carries only finite information about the particular z, so excluding infinitely many partners must come from the *shape* of the family.

### 3.2 Entry-time dominance: computable deadlines are void

**Lemma 4.** Let U be an ML test (λ(U_m)≤2^{−m}, U_{m,s} the clopen stage-s parts) and let x∈CR with x∈U_m for every m. Put f_x(m):=min{s: x∈U_{m,s}}. Then for every computable g, f_x(m)>g(m) for all but finitely many m.

*Proof.* S_m:=U_{m,g(m)} is clopen and uniformly computable. Put
  d(σ):=Σ_m 2^{m/2}·2^{|σ|}λ(S_m∩[σ]).
Each summand is a computable martingale. The m-th summand is at most 2^{|σ|−m/2}, so the series converges with a computable modulus uniformly in σ; d is a computable real-valued martingale with d(∅)≤Σ_m 2^{−m/2}<4. If x∈S_m then the m-th summand equals 2^{m/2} along all sufficiently long prefixes of x. If x∈S_m for infinitely many m, d is unbounded along x, and the standard rational-valued replacement contradicts x∈CR. ∎

Since computable fair homeomorphisms preserve CR (THM-0038), the same holds for every partner ψ_h(x). Consequently any reader that consults an ML test only up to a computable stage bound at hold h obtains, on a CR source, no separate coverage at almost every hold: its holds end in timeouts, and Theorem 1's waiting is essential. This is the test-level form of the S009/S013 finite-deadline collapse; no new class consequence is claimed.

### 3.3 Repairs that fail (recorded precisely)

* **Race sub-tests.** W′_m := cylinders of U_m enumerated before every separating cover of the corresponding partner. Then z∈⋂W′ iff z wins its races, i.e. (O2′) for the universal reader: circular.
* **Level transport.** For a universal U, ψ_h(U_m)⊆U_{m−c_h} up to a constant c_h depending on h. Comparing the two candidates at different levels requires knowing which candidate is the source; the comparison is symmetric under ψ_h.
* **Time truncation.** Void on CR sources by Lemma 4.
* **Transcript-adaptive families.** The family may depend on the read transcript, but the transcript is common to both candidates; this cannot break the ψ_h symmetry.
* **Several readers.** Corollary 2 applies to each reader separately. The XOR of two readers' error streams is computable from the transcript; that is not a contradiction with both streams being computably random, so no combination argument followed.

### 3.4 A repair that succeeds one-sidedly: monotone evidence

A source is **left-c.e.** if its real r(z)=Σz_i2^{−i−1} is the limit of a computable nondecreasing sequence of dyadic rationals r_0≤r_1≤…. For a dyadic rational r, ρ(r) denotes its terminating binary expansion. If z∈CR then z is not eventually constant, so r(z) is not dyadic and r_k<r(z) for all k. For σ∈2^{<ω}, [σ]_ℝ denotes the half-open interval [σ0^∞, σ0^∞+2^{−|σ|}).

Fix a computable strictly increasing g and use the raw frame (K=id, ψ_h=flip_h), the family

  W^g_m := {ρ(r_{g(k)})↾L : m≤L≤k},

the level n(h):=h+1, and the selection Sel₁(·,b):=[b=1].

**Lemma 5.1 (coverage).** If z is left-c.e. and not eventually constant, z is separately covered at (h,h+1) for every h.

*Proof.* For L≥h+1, r_{g(k)}↑r(z) with r_{g(k)}<r(z), so for all large k, r_{g(k)}∈[z↾L]_ℝ and ρ(r_{g(k)})↾L=z↾L; take such k≥L. A cylinder of length L>h separates z from z⊕e_h. ∎

**Lemma 5.2 (one-sidedness).** If z_h=0, no string of W^g_{h+1} covers z⊕e_h. Hence every resolution of the reader at which the proposed bit is 1 has z_h=1.

*Proof.* If ρ(r)↾L⊑z⊕e_h with L≥h+1 and r=r_{g(k)}, then ρ(r) agrees with z below h and has 1 at h, so r≥z↾h10^∞. As z_h=0 and z is not eventually 1, r(z)<z↾h10^∞, contradicting r<r(z). The second sentence: proposed bit 1 means the 1-candidate is separately covered; if z_h=0 that candidate is z⊕e_h. ∎

**Definition.** A hold h with z_h=1 is a **jump-over for g** if r_{g(k)}∉[z↾h0]_ℝ for every k≥h+1.

**Lemma 5.3 (exact criterion).** Let h be a reached hold of T^g on z. If z_h=0 the reader resolves h with proposed bit 0. If z_h=1 it proposes 1 iff h is a jump-over, and otherwise proposes 0 or ties.

*Proof.* If z_h=0, Lemmas 5.1–5.2 give exclusive coverage of the true candidate. Let z_h=1 and p:=z⊕e_h. Any string of length ≥h+1 covering p excludes z. Some ρ(r_{g(k)})↾L (h+1≤L≤k) covers p iff ρ(r_{g(k)})↾(h+1)=z↾h0 for some k≥h+1 (take L=h+1), i.e. iff h is not a jump-over. If h is a jump-over the partner is never covered and z is, so the proposal is 1. Otherwise let k_p be the least k≥h+1 with r_{g(k)}∈[z↾h0]_ℝ. Separate coverage of z needs some k≥h+1 with r_{g(k)}∈[z↾h1]_ℝ, which lies above [z↾h0]_ℝ; monotonicity forces such k to exceed k_p. At the first check that sees any coverage, either only p is covered (proposal 0) or both are (tie). ∎

**Proposition 5 (one-sided destroyer for left-c.e. sources).** Let z be left-c.e. and not eventually constant. With Sel₁, every selected bet of the reader on z is correct. Hence the all-in martingale d₀ never loses on G(z)=F_T(z), and d₀ succeeds iff infinitely many reached holds are jump-overs for g. In that case z∉OH and z∉R₂.

*Proof.* Lemma 5.2 and Lemma 1.1; every hold is left by Lemma 5.1, so holds tend to infinity; Lemma 5.3 identifies the selected bets. ∎

**Lemma 5a (early agreement is excluded by computable randomness).** If z∈CR is left-c.e. and g is computable, then only finitely many h satisfy z_h=1 and r_{g(h+1)}∈[z↾h1]_ℝ.

*Proof.* The monotone computable martingale that, at position h after reading z↾h, bets all-in on 1 exactly when ρ(r_{g(h+1)})↾h=z↾h and ρ(r_{g(h+1)})(h)=1 never loses: those conditions give r_{g(h+1)}≥z↾h10^∞, and r_{g(h+1)}<r(z) forces z_h=1. Every h in the statement triggers such a bet. Infinitely many would make it succeed, contradicting z∈CR. ∎

So for a CR left-c.e. source, at almost every 1-bit hold the approximation at index h+1 is still below [z↾h1]_ℝ, and a jump-over must be a **late skip**: some step of (r_{g(k)})_{k≥h+1} passes from below [z↾h]_ℝ directly into [z↾h1]_ℝ. In error coordinates δ_k:=r(z)−r_{g(k)}, the skipped interval is (τ_h, τ_h+2^{−h−1}] with τ_h:=r(z)−z↾h10^∞∈(0,2^{−h−1}), so the skipping step satisfies δ_{k+1}/δ_k<τ_h/(τ_h+2^{−h−1})<½: jump-overs require error-halving steps at the scale of the hold.

**Corollary 5b (MLR left-c.e. sources).** If z is left-c.e. and MLR, then for every computable strictly increasing g only finitely many reached holds of T^g on z are jump-overs.

*Proof.* Otherwise Proposition 5 gives z∉OH, contradicting MLR⊆R₂⊆OH (frozen). ∎

**Status.** For left-c.e. sources in CR∖MLR (a class recorded as nonempty in THM-0014 at statement level), whether some computable g produces infinitely many jump-overs at reached holds is OPEN. A positive answer would place every such source outside R₂ by an explicit F₂ destroyer. The one-sidedness of Lemma 5.2 is exactly the asymmetry that universal evidence lacks (Proposition 3): monotone evidence can only certify the larger completion of a raw hold.

## 4. Proof gate 4 — crossing the full-family quantifier: not achieved

(EQ) would follow from GOL (Proposition 1.2), but GOL was neither proved nor refuted. The obstruction is precise:

* universal evidence is entangled for every non-MLR source (Proposition 3), so only races remain, and race outcomes on a survivor must be computably random (Corollary 2 with S084);
* a single c.e. family can exclude infinitely many partners only by its shape (§3.1), and no shape was found that works for an arbitrary z∈CR∖MLR;
* the one-sided shape of §3.4 exists exactly for left-c.e. sources, and even there it needs infinitely many late error-halving skips at the scales of reached holds (Lemmas 5.3, 5a), which was not proved.

Neither a universal family of destroyers nor a coverage theorem for every CR∖MLR source was obtained. No bounded-potential obstruction or selected-witness theorem is extrapolated to all sources.

## 5. Proof gate 5 — the opposite alternative, using Corollary 2 as a design constraint

Corollary 2 states what every survivor must do in every frame: whenever some c.e. family separately covers it at all levels, its hold partners are separately covered infinitely often, with computably random race outcomes. Applied to a guessed-run construction (S082–S091 type) and W := all completed runs' constraint cylinders, this forces the partners of the selected witness to be separately covered by run cylinders infinitely often in EVERY frame. The true run's state cannot cover a partner it separates, so the coverage must come from wrong runs: a survivor needs *designed fooling*, not the incidental fooling that compactness selections avoid (S083 Lemma 3.5, S090 Lemma 6, S091 Lemma 3).

Attempted designs and their exact failure points (analysis; no theorem claimed):

1. **Mirror runs for one involution.** Let a wrong guess differ from the true one only in a guessed bit that decides on which side of a neutralizing split the state is placed. The two runs are images under the partner involution, enumerated at the same time: the reader ties. This is an invariant split in disguise; its potential cost is the S089 normalized cost of the split.
2. **Several frames.** For involutions ψ₁,…,ψ_k from different frames, a family containing the true state P and the single images ψ_i(P) has a computably recognizable center (the unique member all of whose single images are present) unless the family is closed under the generated group. For commuting involutions (tail flips, translations, the CDZ₂/linear regime) a closed family indexed by k guess bits exists, consistent with S088's survivor. For non-commuting families, closure means invariance of a small state under the generated group; for the rigid three-involution core this is exactly what Conjecture R (if true) forbids. So designed fooling against rigid families reduces to the S089 invariance problem.
3. **Linearization by conditioning.** S091 Proposition 6 linearizes K_mix by control values a_odd=1 (and K′_mix by b_even=1). Those are value constraints, separately covering every tail-coded (D′) partner above their positions. Tail flips commute, so item 1–2 permit designed fooling against D′ in principle; but a construction carrying linearization, D′ mirror families and potential control simultaneously was not obtained, and the next frame in the enumeration can read the conditioning again. No convergent scheme was found.

**Decisive obligation for separation.** A potential-controlled construction whose neutralizations against non-commuting partner families are either hidden by group-closed decoy families of bounded measure cost or replaced by invariant splits, together with designed fooling with computably random outcomes against every infinitely resolving reader. Equivalently by Corollary 2: a CR∖MLR source that is globally entangled AND defeats every non-orientation F₂ strategy. Not achieved.

## 6. Proof gate 6 — adversarial validation (summary)

Detailed in `P4-S092_VALIDATION.md`. The reader is checked against every transcript, including ties, timeouts, wrong proposals and permanent holds; the separate-coverage tests use only strings no longer than the determined raw window; the partner of a hold is computed through K⁻¹ from the flipped virtual window, not assumed; selection and restart accounting follow S084. Lemma 5.2 depends on the terminating-expansion convention and on non-eventual-constancy; both are explicit. Lemma 5a's martingale is monotone and needs no hold. Corollary 5b uses only frozen inclusions. `phase4/P4-S092_ORIENTATION_AUDIT.py` checks the finite components in exact arithmetic; it cannot establish infinite statements.

## 7. Disposition

**Proved:** Lemma 1.1, Theorem 1 (and its timing form), Proposition 1.2, Corollary 2, Proposition 3, Lemma 4, Lemmas 5.1–5.3, Proposition 5, Lemma 5a, Corollary 5b.

**Conditional:** R₂=MLR (indeed OH^iso=MLR) under GOL. Every left-c.e. CR∖MLR source lies outside R₂ under infinitely many jump-overs for some computable g.

**Unresolved:** R₂ versus MLR; GOL; jump-overs for left-c.e. CR∖MLR sources; any survivor; Conjecture R; R₂ versus OH^iso, U(H), X∈OH and fixed-S preservation (kept separate and untouched).

**Smallest remaining global obligations.** Equality: GOL, or any other theorem assigning an F₂ destroyer to EVERY CR∖MLR source; its left-c.e. instance is the late-skip property. Separation: a globally entangled CR∖MLR source (Corollary 2) that also defeats every F₂ strategy; the construction must handle non-commuting partner families (designed fooling or invariance) with controlled potential.

**Frozen.** The entire incoming landscape, S084's whole-error-stream requirement, S085's representation-only c(n), S086's ∀F∃x and common-factor obstruction, all S087–S091 results with their theorem/experiment distinctions, the exact frames including K′_mix's preceding-control offset, original CR Y, unchanged globally use-clipped self-avoiding wtt M, repeated three-bit H with A=[101;110;111], X=H⁻¹(Y), PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE and DEF-0020 unchanged. No escrow, hazard, residue, unit-column, record-only z₀ or multi-hole detour; no spectral numerics or local frustration work. Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No novelty, external openness, priority, publication or outreach claim. Owner/external blocker: NONE.
