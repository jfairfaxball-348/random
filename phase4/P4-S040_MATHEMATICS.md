# P4-S040 — raw-adjacent decisiveness and the online singleton-completion boundary

Date: 2026-10-07
Session: P4-S040
Incoming checkpoint: a2902d7aed904f0fcf36693cf7da6105a1f6ab34
Scope: Phase 4 — Mathematics; sustained one-hole normalization after coded recoding
Result: **FULL 24-COMPUTATION LOCAL SIBLING TOTALITY IS NOT NEEDED FOR SAME-SOURCE RAW ONE-HOLE DESTRUCTION. IT SUFFICES THAT, ON EVERY REACHED FRESH BLOCK, EACH OF THE THREE RAW-ADJACENT COMPANIONS IS POSITIVELY DECISIVE: IT EITHER BECOMES LOCALLY SELF-CONSISTENT OR IS FINITELY REFUTED BY ONE WRONG/NONBINARY HALT. THREE SYNCHRONIZED RAW ONE-HOLE SCANS THEN PROGRESS WITHOUT ANY REJECTION-TIME BOUND, AND THE MINIMUM-DISTANCE-TWO CODE LAW FORCES AT LEAST ONE FINITE-REJECTION DIRECTION ON EVERY BLOCK; HENCE ONE FIXED SCAN WAGERS CORRECTLY INFINITELY OFTEN AND DESTROYS THE RAW SOURCE. THIS CONDITION IS MATERIALLY WEAKER THAN LOCAL SIBLING TOTALITY. CASE B ITSELF CANNOT HAND OFF THE SENTINEL: A RAW-ADJACENT PAIR DIFFERS ONLY IN THE CURRENT RAW SENTINEL, SO EVERY RAW COORDINATE IT CERTIFIES HAS ALREADY BEEN READ. CASE C REMAINS THE SHARP EFFECTIVE OBSTRUCTION: DIVERGENCE HAS NO FINITE CERTIFICATE, A SECOND PROSPECTIVE PERMANENT HOLE IS FORBIDDEN BY GLOBAL ONE-HOLE GEOMETRY, AND THE WTT USE BOUND DOES NOT GIVE A FINITE REVERSE CLOSURE OF ALL OUTSIDE M-EQUATIONS AFFECTED BY THE COMPANION. THE COMMITTED P4-S011 AUTHORITY DOES NOT ESTABLISH RAW-ADJACENT DECISIVENESS, SO NO ACTUAL RAW DESTROYER FOR X, NO X IN OH, NO OH NON-INVARIANCE AND NO R_2 PROPER-SUBSET OH CONCLUSION ARE OBTAINED.**

## Authority, uniqueness and scope

Immediately before the first P4-S040 write, live main was exactly

\[
\texttt{a2902d7aed904f0fcf36693cf7da6105a1f6ab34},
\]

the final P4-S039 outgoing checkpoint. Repository history contained no P4-S040 mathematics record; the only P4-S040 hit was the forward prompt written by P4-S039. Hence the session identifier was unused.

P4-S001 through P4-S039, the selected CAND-01 authority, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, and P4-S032 through P4-S039 were read. All validated mathematics through P4-S039 is frozen. The P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence, the P4-S037/P4-S038 backward-price route, and ambiguity mass are not reopened.

Retain

\[
R_2=\{x\in CR:\text{every total computable fair-coin-preserving global-}k=2\text{ map sends }x\text{ to }CR\},
\]

\[
OH=\{x\in CR:\text{every total computable adaptive no-repeat one-hole scan sends }x\text{ to }CR\},
\]

and

\[
OH^{iso}=\{x\in CR:\text{every computable fair-coin-preserving homeomorphism }H\text{ sends }x\text{ into }OH\}.
\]

The retained inclusions remain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

Let \(Y\) be the settled P4-S011 computably random wtt-autoreducible source, \(M\) its committed syntactically self-avoiding wtt autoreduction, \(D\) its one-hole destroyer, and let

\[
X=H^{-1}(Y)
\]

for the repeated displayed three-bit recoding. Retain

\[
X\in CR,\qquad H(X)=Y\notin OH.
\]

The missing source-side statement remains whether \(X\in OH\).

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made.

## 1. Raw-adjacent companions and a positive three-way status test

Work in a fresh raw block \(B\) with

\[
u=Ax,\qquad
A=
\begin{pmatrix}
1&0&1\\
1&1&0\\
1&1&1
\end{pmatrix}.
\]

Write

\[
c_i=Ae_i,
\]

so

\[
c_0=111,\qquad c_1=011,\qquad c_2=101.
\]

Fix a raw target \(j=(B,i)\). Once the other two raw bits of \(B\) are known, there are exactly two raw completions, hence two virtual block assignments. Call them \(v_i^0,v_i^1\). They differ by

\[
v_i^0\oplus v_i^1=c_i.
\]

Equivalently, if \(v\) is the actual virtual block, the raw-adjacent companion is

\[
v\oplus c_i,
\]

corresponding globally to

\[
X^{\langle j\rangle}=X\oplus e_j,
\qquad
H(X^{\langle j\rangle})=Y\oplus c_i
\]

inside \(B\) and to \(Y\) outside \(B\).

For any candidate \(w\in\mathbb F_2^3\), run the three computations

\[
M^{Y[B\leftarrow w]}(q_r),\qquad r=0,1,2.
\]

There are two disjoint positively visible statuses.

### Definition 1 — acceptance and finite refutation

A candidate \(w\) is **accepted** when all three computations halt with binary outputs equal to the assigned bits:

\[
M^{Y[B\leftarrow w]}(q_r)\downarrow=w_r
\quad(r=0,1,2).
\]

A candidate \(w\) is **finitely refuted** when at least one of the three computations halts with a nonbinary output or with a binary output different from \(w_r\).

Both events are c.e. from the raw transcript avoiding the target \(x_i\). Queries inside \(B\) are answered from the finite hypothesis \(w\). Queries outside \(B\) are answered by exposing enough fresh raw coordinates in the corresponding outside blocks. The wtt use bound ensures that every individual finite halting witness uses only finitely many virtual oracle values. It supplies no bound on when a halt appears.

The actual block \(v\) is eventually accepted because \(M^Y(q_r)=v_r\) for all \(r\).

Hence the raw-adjacent companion \(v\oplus c_i\) has exactly the P4-S039 trichotomy:

- **A — finite rejection:** \(v\oplus c_i\) is finitely refuted;
- **B — second self-consistent endpoint:** \(v\oplus c_i\) is accepted;
- **C — divergence-only failure:** it is neither accepted nor finitely refuted.

There is no fourth possibility. In Case C at least one required local computation diverges, while every computation which does halt is compatible with the candidate.

### Definition 2 — raw-adjacent decisiveness

The pair \((B,i)\) is **raw-adjacent decisive** when the companion \(v\oplus c_i\) is either accepted or finitely refuted.

Equivalently, the pair is decisive exactly when Case C does not occur.

This is a positive completion property: on the target, finite simulation eventually tells the scan whether the pair is Case A or Case B. No rejection-time modulus is assumed.

## 2. A finite-rejection direction is forced if all three companions are decisive

Recall the P4-S039 local consistency code

\[
C_B=
\{w\in\mathbb F_2^3:
M^{Y[B\leftarrow w]}(q_r)\downarrow=w_r
\text{ for }r=0,1,2\}.
\]

The actual block \(v\) lies in \(C_B\), and

\[
d_H(C_B)\ge2.
\]

### Lemma 3 — not all three raw-adjacent companions can be accepted

For every \(v\in C_B\), at least one of

\[
v+c_0,\qquad v+c_1,\qquad v+c_2
\]

is not in \(C_B\).

**Proof.**
If all three were in \(C_B\), then in particular \(v+c_0\) and \(v+c_1\) would both lie in \(C_B\). Their difference is

\[
c_0+c_1=100,
\]

of Hamming weight one, contradicting \(d_H(C_B)\ge2\). ∎

The same calculation also shows that Case B for direction \(0\) is incompatible with Case B for either direction \(1\) or \(2\). Directions \(1\) and \(2\) may both be Case B because

\[
c_1+c_2=110
\]

has Hamming weight two.

### Corollary 4 — decisiveness forces at least one Case-A wager per block

If \((B,i)\) is raw-adjacent decisive for all \(i=0,1,2\), then at least one direction is Case A.

Indeed every companion is then either accepted or finitely refuted, and Lemma 3 says at least one is not accepted.

This is the key finite-pigeonhole input. It avoids computing the complete c.e. code \(C_B\).

## 3. Main positive theorem — raw-adjacent decisiveness suffices

### Theorem 5 — raw-adjacent decisiveness raw one-hole extraction

Use the displayed repeated recoding and the committed \(M\). Suppose that on the synchronized fresh-block run described below, every reached target block \(B_e\) is raw-adjacent decisive in all three raw directions.

Then one of three total computable raw one-hole scans has a computable output martingale succeeding on \(X\). Consequently

\[
X\notin OH.
\]

No computable bound on the time of acceptance or finite refutation is required.

### Construction

Build three scans

\[
S^0,S^1,S^2,
\]

where \(S^i\) uses local raw coordinate \(i\) as the sentinel in every target block.

Maintain a synchronized prefix invariant at the start of every target epoch: all raw coordinates below a common block boundary have been queried by all three scans, and the next target block \(B\) is completely fresh for all three.

For scan \(S^i\):

1. withhold raw coordinate \(x_i^{(B)}\);
2. query the other two raw coordinates of \(B\), at zero stake;
3. dovetail the finite family of 24 local candidate computations for all eight virtual block assignments, but **do not wait for all of them**;
4. whenever a simulated computation needs a virtual oracle value outside \(B\), expose enough raw support in that outside block to answer it; between such needs, continue querying the least fresh raw coordinate outside \(B\), always at zero stake;
5. from the two raw completions compatible with the observed non-sentinel bits, watch only the corresponding pair of candidate statuses;
6. if the pair becomes Case A, bet all current capital on the raw sentinel value belonging to the accepted endpoint, then query the sentinel;
7. if the pair becomes Case B, place zero stake and query the sentinel;
8. after its own sentinel is closed, continue the common outside filler/dovetail schedule until the Case-A/Case-B status of **all three** raw directions is visible;
9. once all three statuses are visible, query any finitely many zero-stake fillers needed to restore the common queried-prefix/block-boundary invariant and begin the next common fresh block.

The universal eight-candidate dovetail is only a synchronization device. The theorem does not require the other candidate computations to halt.

### Why the three target runs synchronize

Before a sentinel is closed, the three scans know different pairs of actual raw bits in \(B\), but all eight virtual block assignments are finite hypotheses. Hence all three can run the same 24 candidate simulations without knowing the withheld raw bit.

Outside \(B\), the source is the same and the common deterministic filler rule supplies the same raw values after the same number of outside-filler rounds. Thus the positive status events for all eight candidates occur at the same outside-filler rounds in the three scans.

A scan may close its own sentinel earlier than the others. That extra local query does not alter the outside data. Once all three target directions are decisive, there is a finite common outside-filler round by which all three statuses are visible. At that moment each scan has closed its sentinel, all three have the full current block and the same outside queried set, and the finite prefix-restoration sweep makes the next epoch identical again.

### Global totality and the one-hole bound

Fix one scan \(S^i\) and an arbitrary source transcript, not necessarily \(X\).

If its own raw-adjacent pair never becomes Case A or Case B, the scan never waits silently. It keeps querying fresh raw fillers outside \(B\). The other two raw coordinates of \(B\) were queried at the start, so eventually every raw coordinate except the current sentinel is queried. That complete transcript has exactly one hole.

If its own pair resolves and the sentinel is closed, but one of the other two synchronization statuses never becomes visible, the scan again keeps emitting fresh filler queries forever. Its sentinel has already been consumed, so this transcript is exhaustive and has no hole.

If target epochs continue completing forever, the prefix-restoration invariant makes the common queried prefix tend to infinity. Hence every raw coordinate is eventually queried.

Therefore every complete transcript omits at most one raw coordinate.

At each output stage exactly one fresh raw coordinate is queried. The next coordinate is a computable function of the finite transcript. Thus every \(S^i\) is total computable, adaptive and no-repeat.

Exactly as in P4-S011/P4-S012, any such no-repeat adaptive scan preserves fair coin: an output cylinder of length \(m\) fixes \(m\) distinct fair source bits and therefore has measure \(2^{-m}\).

### Correctness and success on \(X\)

On \(X\), the actual endpoint is accepted.

In a Case-A epoch, the other endpoint is finitely refuted, so the unique accepted endpoint among the pair is the actual one. The all-in raw sentinel wager is therefore correct.

In a Case-B epoch, the scan wagers zero.

By Corollary 4, every completed target block has at least one Case-A direction. Hence across the three scans there is at least one correct nonzero wager per block.

By the infinite pigeonhole principle, some fixed index \(i\in\{0,1,2\}\) is Case A on infinitely many target blocks. The computable output martingale for \(S^i\) holds capital on all filler and Case-B queries and bets all capital on the certified sentinel value in Case A. It never loses on \(X\) and doubles infinitely often.

Therefore it succeeds, and \(S^i(X)\notin CR\). Thus

\[
X\notin OH.
\]

∎

## 4. The new hypothesis is materially weaker than local sibling totality

P4-S039 required all 24 candidate computations to halt at every reached block. Theorem 5 does not.

For an accepted raw-adjacent companion, three correct halts are needed. For a rejected companion, **one** wrong or nonbinary halt suffices; its other two computations may diverge. Candidate assignments which are not one of the actual block or its three raw-adjacent companions may behave arbitrarily.

The weakening is strict already as a finite self-avoiding local table condition.

Take actual block \(v=000\). For the three input coordinates, let the local partial outputs depend only on the other two candidate bits, as self-avoidance requires. Arrange:

- all three computations on \(000\) halt with output \(0\);
- on \(111\), let the \(q_0\)-computation halt with output \(0\), finitely refuting the expected bit \(1\);
- on \(011\), let the \(q_1\)-computation halt with output \(0\), finitely refuting the expected bit \(1\);
- on \(101\), let the \(q_0\)-computation halt with output \(0\), finitely refuting the expected bit \(1\);
- leave, for example, the \(q_2\)-computation on other-bit pattern \(11\) divergent.

This respects local self-avoidance and makes all three raw-adjacent companions finitely decisive while local sibling totality fails.

This is only a logical separation of the hypotheses. It is not asserted to be the actual P4-S011 machine.

## 5. Case B gives no prospective same-block sentinel handoff

P4-S039 showed that two visible codewords give a finite raw-coordinate certificate. For a **raw-adjacent** pair, that positive certificate is necessarily retroactive.

### Lemma 6 — exact no-handoff invariant for a raw-adjacent pair

Suppose the two raw endpoints for target direction \(i\) are both locally self-consistent.

Their raw preimages differ by

\[
e_i.
\]

Therefore every raw coordinate on which the pair agrees is a coordinate \(k\ne i\). Those coordinates were already queried before the pair was classified, because \(S^i\) began by reading the other two raw bits.

Concretely:

- \(i=0\): the virtual pair differs by \(111\); it certifies raw \(x_1,x_2\), both already read;
- \(i=1\): the virtual pair differs by \(011\); it certifies raw \(x_0,x_2\), both already read;
- \(i=2\): the virtual pair differs by \(101\); it certifies raw \(x_0,x_1\), both already read.

Thus a Case-B certificate cannot nominate a still-unread raw coordinate in the same block as the next sentinel.

It may justify closing the present sentinel at zero stake, as Theorem 5 does when some external reason guarantees future progress, but it cannot itself carry a fresh target forward.

### Corollary 7 — finite equation tests cannot break a Case-B pair

Consider any finite target-self-avoiding test which sees the raw source outside \(x_i\) and only finitely many \(M\)-equations which both raw-adjacent endpoints satisfy.

The two endpoints give the same observed raw data outside \(x_i\), and by assumption both satisfy every tested equation. Therefore the test has identical finite evidence under the two possible target values.

No such test can correctly determine \(x_i\) on both endpoints.

This is the exact one-bit circularity of Case B.

## 6. Global one-hole geometry forbids two permanent prospective sentinels

A handoff might try to keep the current unresolved sentinel while reserving a second target in another block. The global scan condition gives a simple invariant.

### Lemma 8 — no double permanent reservation

Let \(T\) be any globally one-hole no-repeat scan. Suppose a complete transcript leaves coordinate \(j\) permanently unread.

Then every coordinate \(k\ne j\) is eventually queried on that transcript.

In particular, while an unresolved search at \(j\) is allowed to stall forever, no second prospective target \(k\) may also remain unread forever on that stalled branch.

**Proof.**
Two permanently unread coordinates would give a fibre of size at least four in the scan model and directly violate the definition that every complete transcript omits at most one source coordinate. ∎

Consequently a prospective second sentinel may be delayed only temporarily while the first one remains unresolved. If the first search is a genuine Case-C search which can last forever, global one-hole admissibility forces every prospective alternative eventually to be consumed on that branch.

This does not rule out every imaginable adaptive handoff scheme. It rules out the specific hoped-for resource of preserving two unresolved raw targets until one of their c.e. searches resolves.

## 7. Case C is a genuine no-finite-certificate obstruction

In Case C the actual endpoint is eventually accepted. The companion is not accepted, but no wrong or nonbinary halt ever appears.

After the actual acceptance is visible, every finite stage at which the companion remains unresolved is observationally compatible with three future possibilities:

1. a later wrong halt, yielding Case A;
2. enough later correct halts, yielding Case B;
3. no completing halt, yielding Case C.

Finite simulation can semidecide the first two outcomes when they occur. It cannot certify the third.

### Proposition 9 — the elementary races do not resolve Case C

The following mechanisms do not, from the committed P4-S011 data alone, give a total progress theorem:

- race actual acceptance against companion acceptance;
- race companion acceptance against finite refutation;
- use finitely many fixed waiting/abandonment policies;
- reserve finitely many prospective raw targets while keeping the present sentinel open;
- abandon at zero stake and hope that a later block supplies the missed certificate.

Waiting forever is globally admissible for one scan, because it can exhaust every coordinate except the current sentinel, but on the target it stops all future wagers.

Abandoning after a finite amount of positive evidence preserves totality but may abandon immediately before an arbitrarily late finite rejection or acceptance. The wtt use bound gives no rejection-time or acceptance-time modulus.

A finite family of such abandonment policies has no rate-free guarantee from the abstract authority: finite certificate times, when they exist, can occur later than every member's chosen finite abandonment stage at successive epochs.

This is a mechanism-level obstruction only. The committed record does not establish that the actual \(M\) realizes such adversarial delays on infinitely many target blocks.

## 8. Enlarging the equation set gives more c.e. rejection, not finite completion

A raw companion changes two or three virtual bits in \(B\). It is legitimate to test additional autoreduction equations outside \(B\).

Fix a finite set \(E\) of virtual input indices. For each \(n\in E\), simulate

\[
M^{Y'}(n),
\]

where \(Y'\) is the raw-adjacent companion: it has the hypothesized changed values in \(B\) and agrees with \(Y\) elsewhere.

If \(n\notin B\), the expected fixed-point value is the actual \(Y(n)\). That value can be acquired from raw coordinates outside the target block. A finite wrong/nonbinary halt is therefore another target-self-avoiding c.e. refutation certificate.

This can strengthen Case A.

### Proposition 10 — the wtt use bound does not give a finite reverse closure

For each fixed input \(n\), the wtt use bound gives a computable finite set/frontier of virtual oracle coordinates relevant to that computation.

It does **not** imply that only finitely many inputs \(n\) can query one of the changed coordinates in \(B\). Infinitely many inputs may have use above the location of \(B\), and the use bound gives no computable finite bound on the reverse dependency set

\[
\{n:\ M(n)\text{ may inspect one of the changed coordinates of }B\}.
\]

Hence the committed wtt information does not supply a computably finite set of all \(M\)-equations whose satisfaction would certify the raw-adjacent companion as a global fixed point, nor a finite set whose failure is guaranteed to refute every non-fixed companion.

Dovetailing more and more outside equations can discover additional finite refutations. It cannot turn absence of refutation into a finite positive fact.

This is why “take the finite closure of all affected computations” is not licensed.

## 9. Exact boundary established by P4-S040

The source-side completion problem now has three levels.

### Level 1 — full local sibling totality

P4-S039: all 24 local candidate computations halt. This computes \(C_B\) completely and yields a raw one-hole destroyer.

### Level 2 — raw-adjacent decisiveness

P4-S040: only the actual block and its three raw-adjacent companions matter, and rejected companions need only one finite refutation witness. If every reached target block is decisive in all three directions, three synchronized scans yield a raw one-hole destroyer.

This is materially weaker than Level 1.

### Level 3 — divergence-only raw-adjacent companions

Still unresolved for the actual P4-S011 machine.

Case B is not itself fatal to the positive theorem; it becomes harmless zero stake once its positive second endpoint appears, provided the other directions also eventually classify.

Case C is the unique local arm which can prevent synchronized forward progress without ever producing contradictory finite evidence.

The wtt use bound supplies finite source values for each individual computation, not a halting-time modulus and not a finite reverse closure over all affected equations.

## 10. Separation status

The committed P4-S011 authority does not classify the three raw-adjacent companions on the fresh blocks selected by Theorem 5.

Therefore P4-S040 does **not** establish the raw-adjacent decisiveness hypothesis for the actual source.

No total raw one-hole destroyer for the actual recoded source \(X\) is obtained.

Equally, the failure of the tested Case-C compilers does not prove

\[
X\in OH.
\]

Thus no OH non-invariance theorem and no strict inclusion

\[
R_2\subsetneq OH
\]

is claimed.

Retain

\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]

P4-S032 null-ambiguity preservation remains unchanged and ambiguity mass is not reinstated as an invariant.

## 11. Next bounded target

The new positive boundary is no longer local sibling totality. It is **finite refutability of raw-adjacent non-solutions**.

P4-S041 should attack that property for the actual wtt-autoreduction mechanism rather than add more waiting policies.

The central question should be whether a self-avoiding wtt autoreduction of the P4-S011 source can be put into, or replaced by, a target-equivalent normal form in which every raw-adjacent finite perturbation at the synchronized blocks is either another genuine \(M\)-fixed point or has a finite wrong/nonbinary \(M\)-equation witness.

Equivalently, study the finite-perturbation fixed-point class of \(M\) near \(Y\):

- can divergence-only finite perturbations be eliminated without making the functional truth-table total on all siblings;
- can finitely many additional self-avoiding equations force raw-adjacent decisiveness;
- or can one prove an exact partiality obstruction showing that Case C must survive for some raw directions/blocks under every target-equivalent wtt presentation?

A positive answer which establishes P4-S040 decisiveness on the actual synchronized run would give

\[
X\notin OH,
\]

eliminating this source as an OH non-invariance candidate.

A negative normal-form theorem would still not prove \(X\in OH\), but would identify divergence-only finite-perturbation noncompactness as a more intrinsic source-side resource.

Do not return to ordinary raw-martingale pricing, the P4-S015–P4-S031 bankroll sequence, or ambiguity mass.

## Guards

All validated mathematics through P4-S039 is preserved.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim is made. Phase 4 remains OPEN; Phase 5 remains CLOSED.
