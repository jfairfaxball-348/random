# P4-S126 — Hostile distinct-method SAME-AGENT validation

INTERNAL re-derivation, not independent outside verification, automated CI, Lean, Palomar or novelty audit. The incoming handoff was read verbatim from live main; S125 entry/outgoing commit distinction, sole parent, tree, PR #23, rulesets [], workflow/runs/check-runs/status absence, UNKNOWN 403 protection and no competing S126 record were independently checked. Gate3 PASS; Gate4 NOT REVIEWED; Phase4 OPEN; Phase5 CLOSED.

### 1. Re-derive construction without trusting earlier prose
Recompute the S125 header weights: headers 00,01,10,11 each arise from precisely two three-bit inputs, mass 2/8=1/4. For each output two-bit header and arbitrary tail prefix length n, conditioning on its two input headers leaves a fair computably permuted tail; thus the mass is 1/4 times 2^{-n}. Use bound 3+(n+1)=n+4=m+2 for m=n+2. Each output fibre has exactly the two explicitly listed input streams; no third limit path is hidden by finite-row fold ghosts. For first-bit overlap outputs 01,10 the two real inputs start in opposite source first-key cones. The erased c on 00,11 is genuine but lies OUTSIDE the overlap. The map preserves CR via finite prefixes and computable fair tail permutations. Therefore it cannot witness paired destruction.

### 2. Check the inherited real-to-rational transfer independently
For output rational martingale d, (M_l(u)=2^{-l}\sum_v d(vu)) (|v|=l) satisfies child averaging and (M_l(u)\le2^{|u|}), by including the entire level-l+|u| mass. (T_{k,l}) switches coherently after depth k. Weighted l-tail at |s|=n has bound 2^{n-L}; k>=n collapses to a computable exact tail. Approximating child increments within 2^{-n-4} and adding the buffer +1 gives exact nonnegative rational source values, error under 1/8. No finite-horizon martingalization or noncomputable output modulus is smuggled in.

### 3. New proof first: path-topology minimax, not a computation argument
Let y* be a CR point of K touching U. On K two true preimages have DIFFERENT initial keys; after ANY delayed release they have the SAME initial key c, and E cannot unwrite earlier first bits. Every sufficiently long prefix of y* admits a triggered continuation, and choosing c does not change the trigger (it is decided from prior output). Every nonempty positive cylinder contains CR points, so all comparisons fall within the advertised CR oracle domain.

Almost-sure total model: a.s. both initial candidate bits exist at y*; select a common finite time and use for probability >=1-epsilon, including all prior random coins. Partition the *same event* into p distinct, q0 00, q1 11 (no falsely independent decisions). Uniform guarantee r satisfies r<=p+epsilon at y*, and, for the least-mass same-bit key c, r<=q_c+1-e<= (1-p)/2+epsilon/2 at a triggered CR z. The minimum of p and (1-p)/2 over p∈[0,1] is maximized at p=1/3. Written proof is for unbounded oracle running times; finite-time approximation applies only to probability mass, not all runs.

Partial model: only the event that TWO bits have both appeared and are unequal can contribute success on K. Its finite approximation E has mass >=p-epsilon, and E necessarily fails on ALL released outputs, regardless of c. Hence r<=min(p,1-p+epsilon)<=1/2+epsilon. Not necessary to assume termination on K or on U. These are unconditional measures, not conditional-on-termination probabilities.

### 4. Constructive lower test and adversarial countermodels
For candidate C_{a,b}: no release y gives a y; triggered y=rho c v gives a rho b v. True preimages on release require a=c and b∈{0,1}; on K exactly (a=0 or1) and b immaterial. Three a.s.-total pairs D=(C00,C10), P0=(C00,C01), P1=(C10,C11) succeed respectively on K, U0, U1 and nowhere else, so uniform 1/3 mixture is exact. Rejection sampling three equiprobable choices terminates a.s. Partial heads D succeeds only K; partial tails waits until release then outputs P_c, succeeds only U, uniform 1/2. Clopen U has no CR boundary point and admits deterministic exact inversion after bounded lookahead, so no universal constant threshold without hypothesis. Example U=0V has the required CR boundary at 0w while [1] has no trigger: global density was NEVER used. Fat diagonal K contains CR boundary points but no computable measure supported there, proving the threshold cannot depend on that certificate.

Finite sanity: 6 exact equalities over the three K/U0/U1 regimes and the two specified strategies; for denominators 1..39, 78 exact rational grid maximization bounds (partial <=1/2 and a.s. <=1/3). **84 direct finite assertions PASS; SANITY ONLY**, not a substitute for the continuity/topology proof.

### 5. Most serious false bridges tried and rejected
- A permanent same-cone double erasure at an output already in the other key image produces at least three FULL inverses, not a legal F2 map. Ghost resets are not that erasure.
- A source capital defined afresh at output horizon m is not a single martingale under source length. Freezing at FOLD protects source fairness but can delete an arbitrarily long winning output subsequence. S121 posterior stabilization applies only to CR outputs; bad target NONCR is outside its premise.
- A random pair algorithm succeeding only conditionally on the event that it terminates cannot claim these unconditional sharp guarantees. A two-candidate hitting list is neither a selector nor an exact pair.
- Recovering source degree from finite fibres relative to output does NOT make a noncomputable, nonCR y's preimages nonrandom. It excludes merely COMPUTABLE y targets.
- Neither this inverse obstacle nor preserving safe-map families proves all-source EQ, one-survivor SEP, DP2/CP2, SAME-SOURCE or unrestricted composition.

No fatal error found in C126-1 under its stated probability models/hypotheses; separate-method SAME-AGENT check is not independent certification. No owner/external blocker; S127 unexecuted.
