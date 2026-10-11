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
