# P4-S144 — Compactness barriers and nonconvergent stopped-source pricing

Date 2026-10-14. Exactly ONE owner-invoked Phase4 CAND-01 mathematics session, INTERNAL same-agent proof, not formal or external review. ENTRY live main 24003a3624ae05679990a686cb927cdcf5605bc2 = S143 PR #43 directly fast-forward merged; sole parent 360919fb96124f3b983a0848b405d03cda2d6937, entry tree b10e1c0d4831560c0fd3736da2c7a0cfaf9a757f. No open PR, competing S144 record/branch. Zero Actions runs/check-runs/statuses: ABSENT_NOT_PASS. Rulesets [], protection UNKNOWN_403, workflows collection unsupported, directory absent. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.

Cantor X=2^ω, λ fair-coin product measure. G total computable fair means λ(G^-1[τ])=2^-|τ| for all finite output τ. F_k requires ≤k ACTUAL FULL infinite inverses over EVERY output. R_k sources survive ALL F_k observers and total nonnegative rational computable output martingales. E-08 is a same-source F2/e reduction for bad F3 output; E-00 is R2⊆R3; S-00 one source x∈R2 with a bad fair F3 image. Distinguish four ALIGNED cells for c2 from actual degree 2.

## A144.1 — all uniformly effective clopen eventual-stop certificates have an effective deadline

Fix total computable Cantor map G (not yet assumed fair), nonnegative unit total rational output martingale d and threshold T_k=2^(4k). Define finite threshold event V_(k,n)={y: max_(0≤j≤n) d(y↾j)≥T_k}; V_k=union over n V_(k,n). Finite V_(k,n) is effectively clopen and increasing with n. Set U_(k,n)=G^-1(V_(k,n)); total compact computability of G makes each U_(k,n) uniformly effectively clopen. E_k=union over n U_(k,n) is effectively OPEN, but not generally clopen and with no uniform decidable exact measure.

THEOREM (internal elementary deduction). For any UNIFORMLY COMPUTABLE family of SOURCE clopen sets C_k with C_k⊆E_k for every k, there is a TOTAL COMPUTABLE function B(k) with C_k⊆U_(k,B(k)) for every k.

PROOF. For each fixed k, the open increasing sets U_(k,n) cover the COMPACT C_k. The open-cover property gives finitely many stages whose union covers C_k; monotonicity collapses them to ONE n. Given effective clopen descriptions of C_k and U_(k,n), inclusion is DECIDABLE: refine their finite cylinder unions to common length and check every cell. Search n=0,1,... until inclusion is true. Compactness under the promise proves the search terminates FOR EACH k, hence the algorithm B is total. No oracle for x, noncomputable stopping limit, inverse decision, or fibre cap is used. QED.

COROLLARY (fair G). If x is computably random then x∈C_k for only FINITELY MANY k. Otherwise B witnesses infinitely many level-2^(4k) crossings on G(x); S143's one TOTAL RATIONAL SOURCE martingale succeeds on x. The S143 corollary was stated weakly as infinitely many failures: negating infinitely many successes gives the sharper assertion ∃k0∀k≥k0 max_(n≤B(k))d(G(x)↾n)<2^(4k). This logical sharpening uses only the already proved S143 result. For S011's legal F2 destroyer F and CR Y with nonCR F(Y), for every uniform clopen certificate family C_k⊆E_k, Y belongs to only finitely many C_k, even though each E_k is open and individually contains some cylinder about Y. The obstacle is UNIFORM computable selection. A merely c.e. OPEN C_k is not compact; its exact price is in general only left-c.e., and this proof does NOT apply.

## B144.1 — a GLOBAL LEGAL F3 hostile counterexample to source-price convergence

Use S135's COMPLETE computable additive-use-two globally fair F3 map G; no new map legality inferred from a local fragment. Its active outputs form T={y: y_(3j+1)=y_(3j+2)=0 for all j}. Every y∈T has EXACTLY TWO true inverses, one inside each root-sector A and B; all y∉T have degree THREE. For y=000...∈T the S135 four-cell table has q_A(n)=3 aligned cells above y↾n when n≡0,1 mod 3 and 2 cells when n≡2 mod 3, while q_B(n)=4−q_A(n). Here A=[00]∪[01]∪[10] and B=[11] are disjoint clopen source sectors. All eight source children at every row are used exactly once by BOTH output children; fairness is global.

Define d(τ)=2^|τ| if τ=0^|τ|, and 0 otherwise. This is TOTAL NONNEGATIVE RATIONAL martingale of root 1, doubling on 0 and losing on 1 from a zero-only output prefix; otherwise it holds at 0. It succeeds on the computable ray y.

For every n let ν_n(D)=integral over source D of d(G(x)↾n) dλ(x). By fair G, ν_n(X)=1, so ν_n is a computable finite-horizon probability measure. For the FIXED CLOPEN A:
    ν_n(A)=2^n λ(A∩G^-1[0^n])=q_A(n)/4
           =3/4 for n≡0,1 (mod3), and 1/2 for n≡2 (mod3).
Therefore ν_n has NO setwise limit, even on this fixed clopen source set. Bounded posterior likelihood factors still telescope (S143); they do NOT guarantee a limit of the output-martingale-tilted source measures.

Moreover, for EACH k≥1, the first threshold-hitting stopped version of d at 2^k has EXACT terminal payoff 2^k 1_[0^k] (on any first 1 earlier the bankroll is zero forever). Therefore its stopped-source probability measure ν^stop_k(D)=2^k λ(D∩G^-1[0^k]) has ν^stop_k(A)=q_A(k)/4 and also FAILS to converge as k→∞. Every separate stop k has a computable exact rational price; COHERENCE as thresholds diverge fails. This falsifies the precise unconditional claim 'finite threshold-stopped pullbacks converge setwise on source cylinders for every fair F3 and rational d'. It does not falsify non-limit escrow schemes or finite priced accounts.

HOSTILE CONTROL: S135 already proves a single ordinary TOTAL RATIONAL source W wins on every x with G(x)∈T; hence neither actual inverse over 0∞ is CR or R2. This is NOT a counterexample to R2=R3 or CR conservation of S135 G. No priority/novelty claimed: S135 is reused legal machinery, the stopped-price nonconvergence is this session's elementary derived result.

## B144.2 — dynamic actual-two E-08 unresolved despite complete sibling tracking

S143's seven legal isolated-cone transitions (q,target t,sibling 2q−t) are (1,1,1),(1,2,0),(2,1,3),(2,2,2),(2,3,1),(3,2,4),(3,3,3). Each applies to FOUR aligned cells in a fair c2 G, not to two abstract sheets. q=1→2 sends BOTH source children from the sole A-cell to the winning output bit and leaves zero A-cells on its sibling: no binary source prediction win. q=2→1 sends ONE of four A-children to the chosen bit while THREE occupy its sibling; a strategy cannot condition its wager on an unseen output bit. q=2→3 leaves its minority A-child on the opposite output sibling; biased splitting can lose on the actual source. The S135 complete 3:1→2:2→3:1 recurring example prevents stationary 2:2 normalization; S129 stable-two fallback is not a global dynamic theorem. The q-edge factors multiply to a bounded endpoint quotient q_final/q_initial rather than the desired unbounded same-source capital. No TOTAL globally fair cap-two simulator covering EVERY output or same-source rational output gain compiler is established. E-08 OPEN.

## C — arbitrary use and one-source strictness

A144.1 works for arbitrary computable use because fixed output horizon has an effective uniform source horizon by compact totality. It cannot prove E-00 because CR source to bad image already happens for S011 F2, and its threshold source events are merely effectively open without uniform clopen selection. Nor can S135 supply S-00: its exceptional outputs have a total rational SOURCE killer.

The necessary exact S-00 quantifiers remain: ONE total globally fair G∈F3, ONE total rational output d, ONE x whose G-image makes d unbounded AND for EVERY globally legal total fair F∈F2 and total rational e, e(F(x)) stays bounded. A measure-one R2 set cannot simply be intersected with the λ-null preimage of d-success. Partial F2/e code indices require priority budgets against every legal completion without a legality oracle. First unsatisfied obligation: keep an infinitely growing same-source d-target while guaranteeing total finite-extension reserves for all possible legal F2/e requirements. No verified common budget or witness.

CONCLUSION: two scoped internally proved obstacles (clopen compactness-collapse and explicit nonconverging stopped-source prices), finite sanity only, not central theorem. E-08/E-00/S-00, F2(R2) closure, R2=R3 or R2≠R3 unresolved. S011/Rute original source grades unchanged; frozen Y/M/H/X, S101–S103 A–C, DEF-0020 and PA-0001 untouched. No novelty/Lean/Palomar/manuscript or external contact.
