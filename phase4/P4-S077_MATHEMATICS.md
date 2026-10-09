# P4-S077 — Direct OH-invariance attack: finite-support global transfer and infinite-support obstruction

Date: 2026-10-09
Scope: Phase 4 Mathematics ONLY; selected CAND-01.
Incoming remote main (verified): `11ee3b55f1ed7d544c60594994f8c1dec7979cce`
Disposition: **PROVED a global same-source OH-invariance theorem for every effectively finite-support coordinate recoding, without any effective-retirement premise; full repeated H, arbitrary infinite supported shears, X∈OH, R₂=OH and R₂=OH^iso remain UNRESOLVED.**

## 0. Authority and north-star reconciliation

At start remote main equalled the exact P4-S076 checkpoint; 76 consecutive mathematics/validation/close triplets were present and no P4-S077 files existed. The selected CAND-01 formulation and P3-S008 Gate-3 PASS, both Phase-4 pivots, P4-S001–S076 including S011–S012, S032–S044, S057, S069–S076, and especially S033/S037/S070/S071, were checked against the authoritative records. The old NEXT_SESSION_PROMPT.md prioritized a further price-stabilization investigation; the owner's P4-S077 instruction overrides that session-local direction without changing frozen mathematics. This session does **not** continue S076's escrow programme.

Retain MLR ⊆ R₂ ⊆ OH^iso ⊆ OH ⊊ CR. Keep EXACT original computably random Y, globally use-clipped syntactically self-avoiding wtt autoreduction M, repeated three-bit H, and X=H⁻¹(Y) with H(X)=Y∉OH. From S033, R₂ is homeomorphism invariant; X∉R₂ and X∉OH^iso already hold. The primary target is R₂=OH, with R₂=OH^iso separate; neither is decided here.

## 1. Exact global bridge theorem: finite-support recodings need no retirement

Let F⊂ℕ be a given *finite* source-coordinate set, and K_F be the computable fair-coin-preserving homeomorphism which is an arbitrary bijection of {0,1}^F and is the identity outside F. This includes every finite family of the S070 supported XOR shears and every invertible finite-block recoding on finitely many blocks. The permutation table on F is effectively available.

**Theorem 1 — uniform all-observer finite-support transfer.** For EVERY everywhere-total computable adaptive no-repeat virtual scan T with at most one omitted virtual coordinate on EVERY infinite transcript, and EVERY rational-valued nonnegative computable martingale d on the virtual transcript, there are uniformly:
* an everywhere-total computable adaptive no-repeat raw scan P with at most one omitted RAW coordinate on EVERY transcript, preserving fair coin; and
* one strictly positive rational-valued computable raw martingale e, normalized at 1,

such that, with D=(d+1)/2 if d(empty)=1, for EVERY raw x and EVERY virtual prefix length m,
[
D(T(K_F(x))\upharpoonright m)\ \leq\ 2^{|F|}\ e(P(x)\upharpoonright n_x(m)),
]
where n_x(m)=|F| + the number of T-queries outside F in the first m virtual steps. In particular success of d on T(K_F(x)) implies success of e on P(x), for the SAME raw source x. This includes arbitrarily delayed, non-effectively retiring virtual requests and arbitrary partial-computation dependence inside the total T; there is no price-stabilization or halting-decider hypothesis.

**Proof.** (1) P first queries each raw coordinate in F once in a fixed computable order, giving all these steps ZERO martingale stake. Having learned x|F, P can calculate K_F(x)|F. It now runs the entire virtual scan T from its empty transcript. When T asks q∈F, P silently appends the already determined virtual bit K_F(x)(q), without issuing a raw query. When T asks q∉F, P queries fresh raw q and appends that same observed bit (K_F fixes all coordinates outside F). Resume simulation.

(2) At every raw step the virtual simulation reaches another q∉F after at most |F| silent steps, because T never repeats a virtual coordinate and at most |F| of them are inside F. Therefore the next raw query is computable by a finite calculation on EVERY finite raw transcript, not just on the designated x. No raw coordinate repeats: F was read exactly once in the initial finite prefix, and subsequent q's are distinct and outside F. The virtual transcript on every infinite raw branch is exactly T(K_F(x)). T omits at most one virtual coordinate globally, so P reads ALL F and all but at most one outside-F raw coordinates on every branch. It emits infinitely many genuinely fresh raw bits and is everywhere total. A fresh adaptive raw bit remains conditionally fair, so every output cylinder has measure 2^{-length}; P preserves fair coin. No speculative query, two-hole reservation or negative halting information occurs.

(3) Normalize d(empty)=1 (a nonnegative martingale with zero initial capital is identically zero). D=(d+1)/2 is everywhere total rational, positive and fair, has D(empty)=1, and succeeds wherever d succeeds. At every virtual prefix τ the two positive child factors
[
f(τ,b)=D(τb)/D(τ)
]
have average 1 and each is in (0,2). P bets factor 1 throughout the initial real F prefetch. At a subsequent genuine raw q∉F, using the virtual prefix τ reached after any intervening known-F silent steps, let e's two children have factors f(τ,0) and f(τ,1). They are computable BEFORE raw q is read and have mean 1; this defines a single total positive rational raw martingale on every raw prefix. At each virtual F request the virtual capital receives one f(τ,b), but e makes no wager; at each other virtual request both capitals receive exactly the same factor. Their exact product relation is
[
D(τ_m)=e(ρ_{n_x(m)})\prod_{t<m:q_t∈F} f(τ_t,K_F(x)(q_t)).
]
There are at most |F| factors in the product and each is below 2, establishing the displayed inequality on ALL raw sources and ALL m. Because infinitely many virtual T-queries lie outside F, n_x(m)→∞. An unbounded d therefore forces an unbounded e on the same raw x. QED.

**Corollary 2 — finite-support OH-invariance.** For every such K_F and every z∈CR,
[
z∈OH\quad\Longleftrightarrow\quad K_F(z)∈OH.
]
Indeed K_F and its computable inverse preserve CR by S001, and a failed OH test on K_F(z) would transfer by Theorem 1 to a globally legal failed OH test on z; apply the same reasoning to K_F⁻¹. In particular, ALL finitely supported S_E preserve OH against arbitrary T,d, even with partial sibling computations and no finite claim-retirement time.

**Corollary 3 — finite symmetric-difference equivalence for the S070 family.** For computable block supports E,E' with finite E△E', S_E=S_{E△E'}∘S_{E'} and S_{E△E'} is an OH-automorphism. Therefore
[
S_E[OH]⊆OH\quad\Longleftrightarrow\quad S_{E'}[OH]⊆OH.
]
Any supported-shear failure of OH-invariance, hence any route through S070 to R₂⊊OH, needs genuinely infinite block support (and cannot be certified merely by a single finite-prefix change). This is a global localization of where a counterexample MUST occur; it is NOT a witness.

## 2. Why this is a direct global result and its exact limit

* Global conclusion helped: an all-T, all-d, same-source preservation theorem for every effectively finite source recoding; it proves the finite-support case of H/supported-shear invariance without assumptions about virtual claim retirement. It tests the exact implication OH(z)⇒OH(S_E(z)) from S070, not a fixed financing architecture.
* Unresolved implication: extending finite-support preservation to infinite computable E, notably E=ℕ and even blocks; by S070 universal supported-shear invariance is equivalent to H-preservation. Since Y=H(X)∉OH, proving H-preservation would give X∉OH but not R₂=OH.
* Why prior S037/S070–S076 do not suffice: S037 requires effective price renewal; S070 is an equivalence but no martingale transfer; S071 can lose exp(B_m) on infinitely many spoiled requests; S072–S076 finance specified retiring architectures only. Here an arbitrary globally legal T can defer or permanently omit F-sites non-effectively; each site contributes at most one virtual wager, so simply IGNORING all their gains has a deterministic finite 2^|F| loss.
* What would follow from the MISSING bridge (not asserted): a uniformly successful extension handling an infinite number of non-effectively retiring mixed coordinates for every T,d would imply supported-shear preservation, then H-preservation, and X∉OH via S070. Conversely an explicit z∈OH and infinite-support E with S_E(z)∉OH would imply R₂⊊OH. Neither direction has been proved.

The `2^{|F|}` bound depends on |F|. For finite approximations F_n increasing to all coordinates, the bound diverges, and the raw scans/martingales P_n,e_n depend on n. There is NO legitimate inference from pointwise K_{F_n}(x)→H(x) or from the finite transfer theorem to one computable witness for the infinite recoding. Failure of this limiting argument is not a general impossibility theorem. S071's unbounded spoiled exposure remains potentially essential, not resolved by finite preloading.

## 3. Direct-route dispositions

**Route A:** X∈CR and X∉R₂,OH^iso are inherited; X∈OH remains **unclassified**. No globally legal winning raw scan on X and no universal OH-membership proof was found. No inference from failing S057 or S076 architectures.

**Route B:** proved finite-support global invariance as Theorem 1 and Corollary 2, with exact all-transcript raw legality and no effective retirement assumption. Infinite H and infinite supported shears remain unresolved; no actual OH source leaving OH constructed. This is a restricted positive GLOBAL theorem, not full preservation.

**Route C:** R₂=OH and R₂=OH^iso remain distinct and unresolved. No general width-two same-source normalization beyond the S033 boundaries follows.

Failed methods: passing from finite-support approximants to an infinite product with nonuniform loss; declaring finite bad virtual wager count to control the infinite-support problem; treating price-finance failures as global impossibility; assuming a target-sided M halt gives a uniform negative sibling certificate; and assuming an OH source from lack of a compiler.

## 4. Validation, authority and decision

A finite adversarial test on a 2-coordinate XOR shear inside an 8-coordinate universe, with adaptive virtual ordering and nonzero fractional stakes, exhausted 256 raw assignments × 8 prefixes = 2048 prefix checks. It detected zero violations of the sharp proved bound D_m≤4e and zero repeated/missing raw queries. This is only a sanity audit; the above all-infinite-branch proof is decisive. The incoming repository had 76 consecutive mathematics/validation/close triplets and no S077 prior file.

Freeze ALL S001–S076, in particular S037 effective renewal, S073 LFΠ=dA, S074 exact sharp 3/16, S075 savings mirror and S076 multistage construction; all original Y/M/H/X remain intact. The S057 controller was NOT used; if used later its exact four clipped paired M traces, prospective deadlines, true fillers, zero-stake t/u timeout release, compulsory non-s sweep without resetting old sentinel, and seven 8/7 vs one ZERO terminal payoffs remain mandatory. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claim. Owner/external blocker NONE.
