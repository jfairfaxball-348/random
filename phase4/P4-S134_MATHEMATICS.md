# P4-S134 — Fully completed cap-three boundary oscillator; restricted nonfactorability

2026-10-14; one owner-invoked Phase4/CAND-01 session. Live ENTRY main bb901e53261a8d4809b85ebaef506fcd85f9d5c2, actual S133 authored commit (sole parent 16c0f8d8e4dd4ab39e29466a029a729c38ac0590, tree f9aff3b0aa0c1adb0a215e8bd58e720a39d56dee, PR #32 merged/closed with main at its authored head). This S134 handoff archived verbatim. Evidence INTERNAL only, hostile checking SAME AGENT, no novelty/formal/publication implication.

Let X=2^omega, lambda fair product measure. F_k consists of total computable globally fair maps with at most k ACTUAL FULL infinite inverse sequences above EACH output. R_k means every F_k observer produces a computably random output. CR is defined using total nonnegative rational computable martingales. Additive c=2 means an output m-prefix is determined by an input (m+2)-prefix.

## A134 — ALL-OUTPUT explicitly complete boundary oscillator (THEOREM, internal proof)

For every finite output word tau of length m recursively construct an ordered row R(tau) of FOUR DISTINCT source words of length m+2, carrying labels. Root R(empty)=[(A,00),(A,01),(A,10),(B,11)].

On the zero spine tau=0^m at EVEN m, label the ordered A words a0,a1,a2 and the B word b0. Define:
R(tau0)=[(A,a0 0),(A,a0 1),(B,b0 0),(B,b0 1)];
R(tau1)=[(P,a1 0),(P,a1 1),(S,a2 0),(S,a2 1)].
On the zero spine tau=0^m at ODD m, label A words a0,a1 and B words b0,b1. Define:
R(tau0)=[(A,a0 0),(A,a0 1),(A,a1 0),(B,b0 0)];
R(tau1)=[(P,a1 1),(P,b0 1),(S,b1 0),(S,b1 1)].
On every OFF-SPINE tau containing 1, its row has order [(P,p),(P,q),(S,r),(S,s)]; define:
R(tau0)=[(P,p0),(P,p1),(S,r0),(S,s0)];
R(tau1)=[(P,q0),(P,q1),(S,r1),(S,s1)].
At the FIRST SAFE node the pair p,q need not be siblings; after the next level it always is. This qualification was caught in the first finite-audit draft and corrected BEFORE treating it as an invariant.

Each row's eight source children appear EXACTLY ONCE across its two four-cell child rows. Hence induction on all m shows R(tau) partitions all source (m+2)-words as tau ranges through 2^m output words. The unique coherent tau path for any infinite source defines a TOTAL COMPUTABLE observer G with additive use exactly at most two. For EVERY tau of length m, G^-1[tau] is precisely the union of its four source cylinders, giving lambda=4·2^(-m-2)=2^(-m). This is global FAIRNESS at EVERY depth, independently of any finite enumeration.

For every y with a 1, enter its first SAFE node. The P pair eventually holds two sibling candidate source cells; each future output bit retains BOTH children of exactly one of the two parents, so its nested cylinders yield exactly ONE infinite inverse. The two S singleton cells each retain exactly one child for every output bit and yield one infinite inverse apiece. Distinct origins persist; therefore |G^-1(y)|=3 for ALL y≠0^omega.

On y*=0^omega, spine aligned occupancies oscillate (A,B)=(3,1) at even m and (2,2) at odd m. In fact for even m its A candidates are 0^(m+2), 0^(m+1)1, 0^m10 and its only B candidate is 11 0^m. For odd m≥1, A candidates are 0^(m+2),0^(m+1)1 and B candidates are 11 0^m, 11 0^(m-1)1. Taking nested infinite paths leaves EXACTLY x_A=0^omega and x_B=11 0^omega. Thus |G^-1(y*)|=2 and sup_y|G^-1(y)|=3. Every even 3:1→2:2 transition sends FOUR A and ZERO B source cells to its output sibling 0^m1. Thus y* is a boundary point of G([11]), since y* itself lies in that compact image and excluded sibling cones converge to it. This is a genuine infinite repeated boundary return with ALL sibling outputs fully completed and true fibre cap three. It does NOT satisfy S133's hypothesis that both isolating sheets are locally onto.

## B134 — no fair clopen one-bit tag, but arbitrary F2 factorisation unresolved

THEOREM (internally proved): There is NO clopen set C⊆X such that lambda(C∩G^-1[tau])=(1/2)lambda[tau] for ALL finite output tau. Proof: every clopen C is decided by finitely many input bits. For sufficiently long zero-spine prefixes, ALL four compatible source cells are in fixed small neighbourhoods of the TWO actual inverses x_A and x_B, so membership in C is constant across A cells and separately across B cells. The number of the four cells in C is eventually one of 0,4,q_A(m),q_B(m), where q_A alternates 3,2 and q_B alternates 1,2. NONE stays equal to 2 on ALL large m. Half output mass would require exactly 2 of 4 cells in C on every sufficiently long 0^m. Contradiction.

If F is continuous and shift∘F=G, writing F(x)=b(x)G(x) makes b a continuous {0,1}-valued bit, so C={b=1} is clopen. Fairness of F on cylinders [1 tau] forces the impossible half output mass. Therefore NO fair F, with ANY inverse cap, can yield this particular tagged-shift factorisation. **This is not nonfactorability under arbitrary H,F∈F2.** A failed half-selector cannot exclude an H other than shift.

## C134 — the headline SAME-SOURCE test FAILS; global CR conservation

The output y*=0^omega is NON-CR via the TOTAL rational martingale d(s)=2^|s| if all bits of s are zero, else 0. But both actual inverse streams 0^omega and 110^omega are COMPUTABLE, each defeated by the analogous total rational source martingale betting on its own computable prefixes; they are not even CR, hence neither lies in R2. FIRST failed inference: 'a degree-two bad output with recurrent oscillation creates x∈R2\R3' is false here.

Moreover this G preserves CR on EVERY CR source. If y≠y*, its first 1 enters one SAFE subtree. Within each of the three actual inverse charts, after a fixed finite tag (and in the P chart at most one delayed tag bit), every subsequent output bit is a chronological source tail bit. Thus source and output have the same infinite tail up to finite-prefix deletion/replacement. Finite-prefix CR invariance (S113) gives CR(Gx) whenever x is CR. If y=y*, both inverse sources are computable, so no CR source exists there. We only prove G(CR)⊆CR; we do NOT prove G(R2)⊆R2. No x∈R2\R3, R2\MLR or R_fin\MLR was constructed. R2=R3, R2=MLR, R3=MLR, R2/R4 and F2(R2) closure are UNRESOLVED.

## D134 — nonhomeomorphic pointwise-finite fat boundary patch trial, STILL CR safe

Use S130/S131's effectively closed nowhere-dense fat C_t, its decidable disjoint removed cylinders [rho] (first zero block at stage n), and S127's complete fair prefix code T_(n+1) with exactly n+1 full inverses and finite-tail CR preservation. Put E_n=T_(n+1)∘G (both globally fair and CR-preserving; actual fibres at most 3(n+1)). Define Q_t(x)=x for x∈C_t, and Q_t(rho u)=rho E_n(u) on each removed patch. This is total computable and continuous at C_t because the preserved patch prefixes grow unboundedly as stage n increases; each required finite output prefix is eventually determined by finite input bits. It is globally fair by conditional fairness separately inside each disjoint clopen patch and identity on C_t. An output in C_t has exactly its own inverse, while an output in a removed patch of stage n has finitely many (≤3(n+1)) inverses entirely inside that patch. Thus pointwise-finite but nonuniform, genuinely nonhomeomorphic, with fat local-unbounded locus. Nonetheless the map fixes C_t and every CR source in a patch stays CR under G followed by T_(n+1), by finite-prefix invariance. No R_fin witness: nonhomeomorphic patch surgery is not enough unless one changes the selected boundary input or breaks finite-tail safety.

## E134 — hostile first-line corrections and priorities

S129 one-surplus source betting assumes actual degree 2^c−1; at our c2 degree-two target there are TWO surplus aligned cells, so that theorem cannot rule it out. S131 onto-clopen-sheet CR firewall does not apply to A,B because B misses infinitely many sibling cones. S132's K selector depends on the SECOND actual output bit y[1], S133's unrelated sheet renaming on FIRST y[0]. S133 local two-onto-sheet 2:2 rigidity is respected because B is not locally onto. S133 boundary necessity is now shown achievable in a FULL globally fair F3 construction. No clopen-tag does not settle arbitrary-H decomposition. Explicit COMPUTABLE source failures disqualify the apparent output destroyer. S130 fat C_t meeting MLR/R_fin does not make Q_t destructive.

Decision: RETIRE mere computable-spine and patchwise finite-tail-safe examples as separators; RETAIN G as an exact adversarial benchmark for arbitrary-H factorisation and generalising oscillations to a computably branching PERFECT family, with ONE R2 source test or genuine universal rational source compiler. Frozen Y/M/H/X, S101–S103 A–C, DEF-0020/PA-0001 and source grades unchanged. INTERNAL same-agent proof and sanity only; no novelty, Lean, Palomar, publication or Gate4. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.
