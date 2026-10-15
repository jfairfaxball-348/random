# P4-S164 — Schnorr-slow destructive-output clocks and countable selector finance

15 October 2026. INTERNAL same-agent mathematics only, no novelty, Lean, Palomar, manuscripts or outside checking. Entry live main 9cac7391ea9634d3c5f3493379b14b403cac031f, tree f917254484744caf2054839e4c7905844bb7580c; S163 PR #63 merged at exact authored SHA, sole parent ad52060089cce2615a191481461d6bb8e940e91d, exactly 19 changed paths. No open PRs/competing S164 branch; preceding Actions runs 0, check runs 0, individual statuses 0=ABSENT_NOT_PASS (empty combined status may say pending). Rulesets []; main protection GET 403=UNKNOWN_403. Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.

Definitions: lambda is fair measure on 2^omega. F_k are total computable globally fair maps with at most k ACTUAL COMPLETE inverse streams over EVERY output. R_k={x: for EVERY F∈F_k, F(x) is computably random}. Martingales here are total ordinary nonnegative rational computable except when labelled computable-real.

## A164 — Central obligation attempted, unresolved

Hypothesise total fair additive-two G∈F3, x∈R2, y=G(x) nonCR, and |G^{-1}{y}|=2 actual complete streams. Equality requires a globally legal F2 detector winning on THIS SAME x; strictness requires the universal survival of x against ALL F2. Identity implies x∈CR, and fairness implies y∈Schnorr random. S011 Y is CR but already destroyed by a legal F2; S135's T inverses are nonCR; S163's 0/10/11 decoder has THREE actual inverses over every output and preserves ALL CR. Neither a singular tilt nor aligned row multiplicities proves R2 survival. No such F2 detector, coupled x, or F3 separator was found.

## B164 — A necessary SAME-source Schnorr-slow clock (scoped internal theorem)

THEOREM B164.1. For ANY total computable globally lambda-preserving map G (no fibre or use restriction), ANY CR source x, ANY total nonnegative exact rational computable output martingale d with d(empty)=1, if d succeeds on y=G(x), its finite crossing times
  t_d(k)=min{n:d(y|n)>=2^k}
eventually dominate EVERY total computable schedule T(k): for every T there is K such that ∀k≥K, t_d(k)>T(k).

PROOF. CR implies Schnorr random, and total computable fair G preserves Schnorr randomness: inverse images of uniformly effective open Schnorr tests are effective open and have the SAME computable measures. Thus y is Schnorr random. For each k let
  B_k={z: there exists n≤T(k) with d(z|n)>=2^k}.
This is FINITE CLOPEN, uniformly decidable from rational d and computable T; lambda(B_k) is exact dyadic rational. The prefix-free first-hit inequality (Ville inequality for a nonnegative fair martingale) yields lambda(B_k)≤2^-k. Hence Σ_k lambda(B_k) converges with a computable tail modulus, so (B_k) is a Schnorr-Solovay test. A Schnorr random y lies in only finitely many B_k. As d succeeds every t_d(k) is finite, and t_d(k)>T(k) eventually. No computability of t_d is asserted. QED.

COROLLARY B164.2. A hypothesised SAME x∈R2 fair F3 destroyer cannot have a witness output martingale reaching capital 2^k by a total computable T(k) for infinitely many k. This is a rigorous conditional impossibility applying to the central SAME SOURCE, not an F2 detector. It leaves exceptional Schnorr-random nonCR outputs alive. In S011 a CR source has just such an output under F2 but source Y∉R2, so that example does not separate the hierarchy.

## C164 — Effective countable projective source-law finance, exact rational on all strings

THEOREM C164.1. Assume an infinite uniformly computable family (nu_i) of EXACT RATIONAL projective probabilities nu_i[s] (nu_i[empty]=1, nu_i[s]=nu_i[s0]+nu_i[s1]). Assign weights w_i=2^{-(i+1)}, or any computable nonnegative weights of sum 1 with GIVEN effective tails. Define
  nu[s]=Σ_i w_i nu_i[s], D(s)=2^|s|nu[s].
Truncating after N components errors nu[s] by ≤2^-N for dyadic weights and errors D(s) by ≤2^{|s|-N}. Hence nu and D are uniformly computable REALS, projective, and D a nonnegative computable-real martingale normalised to 1.

There exists an EXPLICIT SINGLE TOTAL EXACT RATIONAL martingale E satisfying
  E(s)≥(1+D(s))/4≥D(s)/4
for ALL source strings s. In particular any source x on which D succeeds is beaten by E, and if SOME component D_i(s)=2^{|s|}nu_i[s] succeeds on x then D(s)≥w_i D_i(s) forces E to succeed on SAME x.

PROOF (constructive rationalisation). Set P(s)=(1+D(s))/2, a positive computable-real martingale with P(empty)=1, P(s)≥1/2. Its conditional probability r_s=P(s0)/(2P(s)) is uniformly computable and in [0,1]; the known positive denominator permits total division. For n=|s| put epsilon_n=2^{-(n+2)}, a_s=(1-epsilon_n)r_s+epsilon_n/2. Compute exact rational q_s with |q_s-a_s|≤epsilon_n/4, using any name for the computable real a_s. The smoothing guarantees both q_s≥(1-epsilon_n)r_s and 1-q_s≥(1-epsilon_n)(1-r_s), with q_s strictly between 0 and 1. Put E(empty)=1; E(s0)=2E(s)q_s, E(s1)=2E(s)(1-q_s). All values terminate and are EXACT rationals; sibling equality is exact on EVERY source node. Along either child relative to P the multiplicative loss is at most (1-epsilon_n); hence
  E(s)≥P(s) product_{j<|s|}(1-epsilon_j)≥P(s)(1-Σ_j epsilon_j)=P(s)/2=(1+D(s))/4,
because Σ epsilon_j=1/2. QED.
This rationalisation actually works for ANY nonnegative uniformly computable-real martingale D normalised to 1, not just mixture martingales. However FINITE ACTUAL fibre count alone neither supplies source laws nu_i nor their effective presentation; C164 is NOT a universal F3→F2 compiler.

## D164 — Countable mixture can win though EVERY component stays bounded

For each i≥0, let nu_i be lambda conditioned on cylinder [0^i] (nu_0=lambda). Each D_i(s)=2^|s|nu_i[s] is total rational and bounded by 2^i ON EVERY path. With w_i=2^{-(i+1)} the infinite mixture D happens to be EXACT RATIONAL:
  D(0^n)=1+n/2,    D(0^r 1 v)=(r+1)/2.
On 0^n the i<n components contribute n/2 and i≥n contribute 1; on a first-1 word, only i≤r survive, each contributing 1/2. In particular D(0^n)→∞ although all D_i are bounded. Parent-child equation at 0^r is (1+(r+1)/2)+(r+1)/2=2(1+r/2), and descendants after first 1 have constant capital. This refutes extending S163's FINITE mixture 'wins iff some component wins' to countable mixtures. The unique winning zero stream is computable and nonCR: NO hierarchy evidence.

## E164 — Non-effective Cesaro convergence does not grant computable source finance

Choose c.e. noncomputable A with alpha=Σ_{e∈A}4^{-(e+1)} noncomputable (S155), and let alpha_m be its computable rational enumeration-stage approximants. Define rational projective law nu_m: its first bit is 1 with probability alpha_m and all later bits fair, so nu_m[1v]=alpha_m 2^{-|v|}, nu_m[0v]=(1-alpha_m)2^{-|v|}. All stages and siblings are exact rationals. The ordinary Cesaro average of the nu_m converges cylinderwise and projectively to nu with nu[1]=lim_m alpha_m=alpha noncomputable. Therefore ordinary convergent Cesaro limits do NOT supply a uniformly computable-real source measure, much less an exact rational martingale; an effective modulus or independent computable presentation must be provided. This is a stage-law effectiveness countermodel, not an F3 destroyer.

## F164 — Adversarial controls and unresolved central gap

S135 global additive-two F3 oscillator over effectively closed null T has nonCR inverse sources; S162 finance already beats them and C164 can rationalise an effective mixture there without producing R2 membership. S158 global fair exact F2 late reveal preserves all CR despite nonuniform posterior cutoffs. S155 noncomputable multiplicity mass coexists with exact rational local kernels and conservation. S141 positive benign folds, S117 paired reservoirs and S163 globally fair prefix decoder still do NOT couple an R2 source to a legal destructive F3. S011 gives Schnorr-random nonCR output but destroys its source under F2. No added construction hides FOUR complete inverses: C164/D164/E164 are laws, not purported F3 maps; B164 uses a truly global fairness hypothesis.

E-08/E-00/S-00 and R2=R3 equality/strictness OPEN. No claims of novelty, priority, external verification, Lean or Palomar. Exact Fraction checks are finite sanity only.
