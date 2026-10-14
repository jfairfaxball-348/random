# P4-S149 — Arbitrary-use conditional-bias decomposition; R2/R3 remains open

One owner-invoked mathematical session, 14 October 2026. LIVE entry main `1fb31030ee5efb95f92b27e4f68ae2a4e22f95f0`, S148 PR #48 merged directly at that same SHA; sole parent `64fd2f2fc88d2524d7603bf3a38695a9e3e8dfbb`, tree `7a3670ae8deb90b2de11454b085272b4bafe06ce`, 19 changed paths. No S149 competing branch, records or open PR on entry. Actions runs 0, check runs 0, status contexts 0: **ABSENT_NOT_PASS**; workflow listing inaccessible by connector allowlist (UNKNOWN), rulesets [], protection 403 **UNKNOWN_403**. This is internally reasoned mathematics only, not an independently reviewed proof, formalisation or novelty result.

Let `CR` denote computable randomness under total nonnegative rational computable martingales, `F_k` the class of total computable globally fair Cantor maps with at most k **actual complete** preimages above **every** output, and `R_k={x : G(x) in CR for every G in F_k}`. Inclusion R3 ⊆ R2 is immediate; E-00 is the OPEN opposite inclusion. Frozen S101-S103, original Y/M/H/X, DEF-0020, PA-0001, Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN and Phase5 CLOSED are unchanged.

## A149.1 — Exact conditional-bias decomposition for arbitrary computable use (INTERNAL PROOF)

**Statement.** Let `G:2^omega -> 2^omega` be **any total computable Cantor map**, not necessarily fair or finite-fibre. Choose a total computable strictly increasing `u:N->N` with `u(0)=0` and such that the first n output bits of G are fixed by every source word of length u(n). Such a computable modulus exists for an everywhere-total computable Cantor functional, by enumerating a finite clopen cover of its halting prefix computations for each n, then enforcing strict growth. Let d be any total nonnegative rational computable output martingale, let p=d+1>0, and for s of length u(n) set tau=G([s])|n. Write Delta_n=u(n+1)-u(n)>0, r_b=p(tau b)/p(tau) in (0,2), and

`rho_n(s)=2^{-Delta_n} * #{ t in {0,1}^{Delta_n}: G([st])|(n+1)=tau1 }`,

`A_n(s)=(1-rho_n(s))*r_0+rho_n(s)*r_1>0`.

All terms are *uniformly computable rational* from n,s,G,p,u, without oracle for x or its output. There is ONE total strictly positive rational computable **SOURCE martingale e**, root 1, such that for ALL x and n

`p(G(x)|n)/p(empty) = e(x|u(n)) * product_{m<n} A_m(x|u(m)).`  (A149)

**Construction/proof.** At milestone u(0)=0 put e(empty)=1. Given e(s) for |s|=u(n), for each word t of length Delta_n put
`e(st)=e(s) * [p(G([st])|(n+1))/p(tau)] / A_n(s)`.
The dyadic average of these 2^Delta_n child multipliers is exactly one by the definition of A_n(s). Thus the mean of e over the entire descendant block is e(s). Define e at each intermediate length by the dyadic averages of the already computable endpoint capitals. This gives a single everywhere-defined total positive *rational* martingale on the **entire source tree**, including all intermediate source lengths. On any x, the endpoint ratio e(x|u(n+1))/e(x|u(n)) equals r_actual/A_n. Multiplication over m<n telescopes r_actual to p(G(x)|n)/p(empty), proving (A149). No fibre-cap or pushforward measure hypothesis, no uncomputable conditional pricing, and no oracle branch selection is invoked. **This is not a construction of an observer F in F2.**

For additive use c, take u(n)=n+c for n>=1, u(0)=0 (first block absorbs c+1 bits). At later source blocks Delta=1, rho_n(s) belongs to {0,1/2,1}: rho=1/2 exactly when the two children emit different output bits, yielding A=1; rho=0 or 1 when they emit the same bit, yielding A equal to the forced child p-ratio. This recovers S148 after its harmless initial finite offset, with arbitrary computable use now handled by finite dyadic blocks.

## A149.2 — Absolute local-bias firewall and necessary divergence (INTERNAL PROOF)

Martingality gives `r_0+r_1=2`. Consequently

`A_n(s)=1+(rho_n(s)-1/2)*(r_1-r_0)`,
`|A_n(s)-1| <= 2*|rho_n(s)-1/2|` (strict for p=d+1).

For each CR source x, e(x|u(n)) is bounded along x. If d succeeds on G(x), (A149) forces the product of A_n along x to be unbounded above. Since `A_n<=1+2|rho_n-1/2|` and `log(1+t)<=t`, necessarily

`sum_{n>=0} |rho_n(x|u(n))-1/2| = infinity.`  (B149)

Equivalently, for ANY chosen computable output-use schedule u, **summable local next-bit conditional bias along a CR source is sufficient for CR preservation by G at that source**, against every output rational martingale simultaneously; given d, the source e is uniformly constructed, while the summability bound along x need not be computably known. This is a structural *sufficient* condition for preservation, not a characterisation of CR-preserving maps or an R2-specific proof. This additional necessary condition is weaker than (A149)'s actual unbounded signed product.

If `sum_n sup_{|s|=u(n)}|rho_n(s)-1/2|<infinity` then G sends **every** computably random source to a computably random image. This uniform corollary also does not depend on global fairness or finite fibre count. It is a useful filter for candidate F3 constructions, not an R2=R3 implication.

## B149 — Attempts to finance A with a legal F2 observer; where they fail

**First candidate: turn A_n into source capital.** A_n is predictable and rational, but it is an *average of output p-ratios conditioned on the source cell*, not a source martingale increment. Betting multiplier A_n simultaneously on all children with A_n>1 violates source martingality. The sole universally valid capital is e, which is bounded on every CR source. Thus the exact factorisation isolates the unpaid debt but supplies NO globally fair F2 observer and no source lottery without a price.

**Second candidate: two-bank hedging at c2 exact-two cones.** At a q_A=1->2 forced step the two children agree on the next output bit; after one further output bit the selected leaf set has t in {1,2,3} of four source grandchildren. The sharp finite allocation is `t*a+(4-t)*b<=4` (S147). Splitting capital to guarantee growth >1 for both future output children is impossible on this known-leaf finite tree. A future-dependent policy selecting the successful continuation is not computable from the present source prefix. Exhaustive 178 labelled S146/S147 legal transitions classify finite tables, **not global maps**. We did not find a repeated-bank rescue satisfying all-cylinder fairness and <=2 ACTUAL INFINITE preimages for ALL outputs.

**Third candidate: reserve compensators in a global fair cap-two chart.** Computing rho is possible, but rho itself depends on G and its finite blocks; assigning output labels to a new F from rho requires simultaneously (i) `lambda(F^{-1}[sigma])=2^{-|sigma|}` for EVERY sigma and (ii) `|F^{-1}{z}|<=2` for EVERY complete z. No coherent globally computable chart extension meeting both was constructed. The S135 globally fair c2 F3 3:1<->2:2 recurrent oscillator defeats naive static sheets but itself conserves CR. S141 positive-folded benign F2 pockets defeat bare geometric sufficiency.

**Fourth candidate: price via high-output-gain stopping events.** S145/S147 imply that at any CR source destroyed by an arbitrary-use fair G, exact local stopped-event source prices are not uniformly computable even on computable unbounded subsequences in ANY joint source/output clopen cone. rho_n is computable at finite blocks but does NOT compute these infinite stopping prices, so no contradiction to S145 or automatic escrow. The S011 genuine fair F2 map destroys a CR (not R2) source; it already exhibits every local obstruction in A149/B149, so none is inherently three-sheet-specific.

**Fifth candidate: strict separation.** The required witness is ONE fair G in F3, ONE rational d and ONE SAME x in R2 with d(G(x)) unbounded. A149 holds for the genuine S011 CR/F2 destroyer, so it does not isolate a source surviving EVERY F2 observer. S135 boundary and S138 dense-restart sources are CR-defeated or CR-conserving; no survivor or separator was produced. Conull R2 cannot be intersected with a null d-success preimage to conjure x.

## C149 — Hostile controls and limitations

1. A149 is valid for nonfair maps (constant-output counterexample) as well as fair maps: local debt by itself does NOT imply that a fair observer exists.
2. The sufficient condition depends on the chosen **effective use schedule**. Over-reading artificially makes rho=0 or 1 for identity (which preserves CR). Therefore divergent bias is not sufficient for destruction, and the sum is NOT intrinsic to G unless schedule is specified. The S148 adjacent-swap fair degree-one homeomorphism has forced rows on half its clock yet conserves CR.
3. No upper bound on rho from finite fibre cap alone was proved; uniformly summable local bias is a restricted firewall, not an F3 theorem.
4. A149 does not supply a total rational F2 image witness, effective inverse selector, source-local stopped-price compiler, R2 survivor or F2(R2) iteration theorem. No proof of E-08/E-00/S-00, R2=R3, strictness, R2=MLR or R3=MLR.
5. The finite audit tests algebra, not all cylinders, infinite fibres, novelty, original Rute theorem correctness or independent formal proof.

**Disposition:** A149.1/A149.2 are internally proved algebraic extensions of S148 to unrestricted computable use; B149 records five failed or blocked central attempts with FIRST quantifier gap. The strongest result is an all-use, all-source positive rational martingale factorisation and a local-bias summability firewall. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED; frozen objects/grades untouched.