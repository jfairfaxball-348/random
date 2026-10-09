# P4-S081 — Bounded-hole collapse, van Lambalgen for OH, and the sharpened OH-certification gate

Date: 2026-10-09
Scope: Phase 4 Mathematics ONLY; selected CAND-01; pinned incoming live main `b8017ed6f3090bcdd5bcbd5f4ceba8058cc7bacf` (the P4-S080 outgoing SHA).
Disposition: **The certification gate is NOT passed: no computably random non-MLR member of OH is constructed, and no proof of OH=MLR, U(H), R₂=OH or R₂=OH^iso is obtained. PROVED instead three structural theorems that sharpen the gate. (A) Bounded-hole collapse: for every finite h, robustness against total computable adaptive no-repeat scans with at most h unread coordinates on every transcript is exactly OH. So within scans the whole finite-multiplicity hierarchy collapses to k=2, and OH is randomness against total computable non-monotonic strategies of uniformly bounded postponement width. (B) A van Lambalgen theorem for OH under uniform relativization: x⊕y∈OH iff x∈OH^[y] and y∈OH^[x]. (C) Consequences for U(H): a counterexample Y₂∈WAR must admit no block-avoiding partial predictor of any nonconstant function of its 3-blocks on any infinite decidable set of blocks; on every source that admits one, K⁻¹(Y′)∉OH for every computable blockwise recoding K. The catalogue check (step 0) finds no statement separating total-strategy non-monotonic randomness from MLR.**

## 0. Authority, uniqueness and frozen objects

Live remote `main` was verified with `git ls-remote` to equal `b8017ed6f3090bcdd5bcbd5f4ceba8058cc7bacf`, the P4-S080 outgoing commit, which embeds the P4-S081 prompt in `phase4/P4-S080_CLOSE.md`. The `phase4/` tree contained the P4-S001–S080 records and no P4-S081 file; the session ledger names P4-S081 only as the next session. P4-S081 is therefore unused. The incoming prompt agrees with `authoritative/NEXT_SESSION_PROMPT.md`; no discrepancy was found.

Reviewed: the phase summaries for P4-S001–S080, and in detail S008, S011, S012, S032, S033 (Lemma 1, Theorems 2 and 5, Corollary 4), S079, S080 (mathematics, validation and close), selected CAND-01, the P3-S008 Gate-3 PASS and both Phase-4 pivots.

Retain MLR ⊆ R₂ ⊆ OH^iso ⊆ OH ⊊ CR and KLR ⊆ OH (S080 Proposition 6). The ORIGINAL computably random Y, the clipped syntactically self-avoiding wtt autoreduction M, the repeated H with A=[101;110;111] and X=H⁻¹(Y) are untouched; nothing below alters them or assumes anything about them beyond the record. Conventions: a *scan* is a total computable adaptive no-repeat scan in the sense of S008 (the next queried source coordinate is a total computable function of the finite output transcript, and no coordinate repeats along any transcript); every such scan is fair-coin preserving. Martingales are nonnegative and rational-valued; this suffices for computable randomness (DEF-0004, as already used in S012).

## 1. Step (0): catalogue check, recorded access levels only

The prompt asks whether the existing catalogue already separates randomness against *total* computable non-monotonic strategies from MLR. That would immediately give a non-MLR member of OH, by S080 Proposition 6. No new retrieval was made. The relevant records are:

| Record | Content | Recorded access |
|---|---|---|
| DEF-0012 | KL-randomness via computable non-monotonic betting; the partial/total convention is not specified | SRC-0018, ABSTRACT_INSPECTED |
| THM-0011 | every KL-random sequence has arbitrarily dense ML-random subsequences | SRC-0018, ABSTRACT_INSPECTED |
| QST-0001 | does KLR coincide with MLR? SOURCE-STATED OPEN | SRC-0018 (2006); SRC-0019 (2025) status check, ABSTRACT_INSPECTED |
| DEF-0064 / THM-0071 | Rute's endomorphism randomness; CR is not conserved by all a.e.-computable endomorphisms | SRC-0060, STATEMENT_INSPECTED |
| THM-0014 | A is high iff deg(A) contains a CR non-MLR set; also with left-r.e. witnesses | SRC-0028, STATEMENT_INSPECTED |
| THM-0002, THM-0015, THM-0020 | strict MLR/CR/Schnorr hierarchy; a c.e. Schnorr-random non-MLR real; martingale resource formulations | SRC-0007, SRC-0008, SRC-0028 |

**Finding.** The catalogue contains no statement, at any recorded access level, that separates randomness against total computable non-monotonic strategies (or KLR, or any intermediate non-monotonic notion) from MLR. There are no records of injection or permutation randomness. `catalog/README.md` classifies the abstract-level Kolmogorov–Loveland material as navigation-only for decisive purposes until upgraded. **No openness, priority or difficulty inference is drawn from this absence.** The gate is therefore not closed by the catalogue, and the session proceeds to the mathematics.

## 2. Bounded-hole scans, the frontier and the held/fill split

**Definition 1.** For h≥1, a scan T is an *h-hole scan* if every infinite output transcript leaves at most h source coordinates unread. Put

  OH_h := {z ∈ CR : F_T(z) ∈ CR for every h-hole scan T}.

So OH_1=OH, and OH_{h+1} ⊆ OH_h because every h-hole scan is an (h+1)-hole scan. By S032 Lemma 8, a scan has global fibre bound at most k exactly when it is a ⌊log₂k⌋-hole scan.

**Lemma 2 (computable frontier).** Let T be an h-hole scan. For every n there is a finite N such that every transcript prefix of length N leaves at most h coordinates below n unread. The least such N, written c(n), is computable from n, and c is nondecreasing.

*Proof.* The set of finite transcripts that leave more than h coordinates below n unread is closed under prefixes, since shorter transcripts read less. If it contained strings of every length, König's lemma on the binary tree would give an infinite transcript every prefix of which leaves more than h coordinates below n unread. The unread-below-n sets along that transcript form a decreasing sequence of finite sets of size greater than h, so their limit, the set of permanently unread coordinates below n, has more than h elements, contradicting the h-hole property. Hence N exists. For a candidate N all 2^N transcripts of length N can be simulated, because T is total computable, so the least N is found by search. Monotonicity: fewer than h+1 unread below n+1 implies fewer than h+1 unread below n. ∎

Fix an h-hole scan T with frontier c. Write q_t for the coordinate T queries at step t (so output bit t is z(q_t)), and put

  n_t := max{n : c(n) ≤ t},  U_t := {q < n_t : q ∉ {q_0,…,q_{t−1}}}.

Then n_t is nondecreasing, computable from t and unbounded, and |U_t| ≤ h for every t because t ≥ c(n_t). Every coordinate q falls in exactly one of two classes, determined online from the transcript:

* q is **fill** if T reads it at a step t with q ≥ n_t, before the frontier passes it;
* q is **held** otherwise. Then there is a first step e_q (its *entry*) with q < n_{e_q} and q still unread, and q belongs to U_t exactly for e_q ≤ t ≤ r_q, where r_q ≤ ∞ is the step at which T reads it. (U_t counts reads before step t, so q is still in U at its own read step.)

Since n_t → ∞, every coordinate is fill or held. A coordinate that T never reads is held and stays in U forever. The held intervals [e_q, r_q] have at most h members active at any step, because the active held coordinates at step t are exactly U_t.

## 3. Theorem A — bounded-hole collapse

**Theorem A.** For every h≥1, OH_h = OH. Equivalently, if z ∈ CR, T is an h-hole scan and d is a computable martingale succeeding on F_T(z), then there is a one-hole scan S and a computable martingale D succeeding on F_S(z). The pair (S, D) is uniformly computable from (T, d, h) and a colour index i ≤ h.

*Construction.*

**(i) Online colouring.** Process T's transcript step by step. When coordinates enter U at step t, take them in increasing order and give each the least colour in {1,…,h} not used by the other current members of U_t, including those just coloured. At most h−1 other coordinates are active, so a free colour always exists, and colours never change afterwards. Two coordinates of the same colour are never simultaneously in U. The permanently unread coordinates of a transcript are held and stay in U forever, so they are pairwise simultaneously active. Hence they receive pairwise distinct colours, and each colour has at most one permanently unread coordinate.

**(ii) Colour scans S_i (1≤i≤h).** S_i keeps a simulated T-time τ, the T-transcript up to τ, the colouring, and its own read set R. It produces its next query as follows.
  (a) If some coordinate of U_τ has a colour ≠ i and is not in R, S_i reads the least such coordinate (a *pull*) with stake 0.
  (b) Otherwise let q=q_τ. If q ∈ R, S_i advances τ by one and returns to (a) without output. If q ∉ R, S_i reads q, then advances τ. Its stake is T's stake θ_τ if q is held of colour i, and 0 if q is fill.
In case (b), q cannot be held of another colour, because such a coordinate was pulled at its entry, which is at or before τ.

**(iii) Fill scan F.** F is S_i with clause (a) pulling every held coordinate of U_τ not yet in R, of any colour. Its stake is θ_τ on in-step fill reads and 0 otherwise.

Here θ_τ := (d(ρ1)−d(ρ0))/(2d(ρ)) for ρ the T-transcript up to τ (and 0 if d(ρ)=0), so d(ρb)=d(ρ)(1+θ_τ(2b−1)) and θ_τ ∈ [−1,1] is rational and computable from ρ.

*Verification.*

1. *Totality and computability.* The state of S_i (or F) is reconstructible from its own output transcript, because every simulated T-query is answered by a bit S_i has already read, in step or by an earlier pull. Between two outputs, clause (b) skips only coordinates in R that were pulled and not yet reached by T. Each pulled coordinate is skipped exactly once, and only finitely many coordinates are pulled before any given output, so every query is produced after finitely many computation steps. The next query is a total computable function of the transcript, and S_i never repeats a coordinate. Every infinite transcript of S_i drives τ to infinity: if τ stayed bounded, only finitely many pulls would be available. So S_i outputs infinitely many fresh bits and is fair-coin preserving.

2. *One hole on every transcript.* For any source, S_i reads every coordinate T reads (in step or earlier) and every pulled coordinate. A coordinate T never reads is held, enters U, and is pulled by S_i unless its colour is i. So the coordinates S_i never reads are exactly T's permanently unread coordinates of colour i, and by (i) there is at most one. S_i is a one-hole scan.

3. *F is an effective isomorphism.* F pulls every held coordinate at entry, and every coordinate is fill or held, so F reads every coordinate on every transcript. The frontier passes q at T-time c(q+1). F's output count up to T-time τ is at most τ (in-step reads) plus the number of pulls, and pulls are coordinates below n_τ. Since c(n)≥n−h (at least n−h coordinates below n must be read by time c(n)), n_τ ≤ τ+h. So q is read by F by output index 2c(q+1)+h+1, a computable bound. As in S008 Lemma 2, F is then exhaustive with a computable modulus on every transcript, so its induced map G_F is a computable fair-coin-preserving bijection of Cantor space with computable inverse. By S001 / THM-0038 it preserves computable randomness.

4. *Martingales.* Let D_i be the stake process of S_i and D_F that of F. Each stake is a computable rational in [−1,1] computed from the scan's own past, so D_i and D_F are nonnegative computable martingales on the outputs of S_i and F.

*Proof of the theorem.* Let z ∈ CR, let T be an h-hole scan and let d succeed on y=F_T(z). Along y, d never vanishes, because a nonnegative martingale that reaches 0 stays 0. Hence

  d(y↾τ) = Π_{s<τ} f_s,  f_s := 1+θ_s(2y_s−1) > 0.

Each step s reads a coordinate that is either fill or held of exactly one colour. Grouping the factors gives, for every τ,

  log d(y↾τ) = log D_F(τ) + Σ_{i=1}^{h} log D_i(τ),

where D_F(τ) and D_i(τ) are the capitals of F and S_i on z after they have processed T-time τ. These are values on prefixes of F(z) and S_i(z), and pulls leave capital unchanged.

By verification 3, G_F(z)=F(z) is computably random, so sup_τ log D_F(τ) < ∞. Since sup_τ log d(y↾τ) = ∞, the finite sum Σ_{i≤h} log D_i(τ) is unbounded above. So for some i, sup_τ log D_i(τ) = ∞, and D_i succeeds on S_i(z) for the one-hole scan S_i. Hence z ∉ OH. Thus OH ⊆ OH_h, and OH_h ⊆ OH is trivial. ∎

*Remarks.* (0) The proof uses only three properties of the frontier: n_t is computable, nondecreasing and unbounded; |U_t| ≤ h for every t and every transcript; and n_t ≤ t+h. Any computable frontier with these properties may replace the least one from Lemma 2. (1) The proof does not use the S008 fact that a winning scan reads every coordinate of a computably random source. (2) The colouring is the online first-fit colouring of an interval family of clique number at most h. That the frontier makes the clique number uniformly bounded is exactly where the global h-hole hypothesis and compactness (Lemma 2) enter. (3) With no uniform bound, for example finitely many holes on each transcript but unboundedly many across transcripts, Lemma 2 fails and infinitely many colours would be needed. The finite-sum step then has no analogue, and nothing is claimed.

## 4. Immediate corollaries

**Corollary A1 (the scan multiplicity hierarchy collapses at two).** For k≥2 let R_k^scan be the class of z ∈ CR such that F_T(z) ∈ CR for every scan T with global fibre bound at most k. Then R_k^scan = OH for every k≥2. Hence

  R_fin ⊆ R_k ⊆ R_k^scan = OH (all k≥2),

and the power-of-two plateaux of S032 Lemma 8 all define the same robustness class. Inside the scan subclass, every finite multiplicity bound beyond k=2 is useless for destroying computable randomness. *Proof.* S032 Lemma 8 and Theorem A. ∎

**Corollary A2 (held-bit normal form).** Let T be a one-hole scan, z ∈ CR, and d succeed on F_T(z). Then the martingale that copies T's stakes on held coordinates and stakes 0 on fill coordinates also succeeds on F_T(z). The held coordinates are bet on one at a time. Each is the least unread coordinate at its entry, they are strictly increasing, and each is read before the next one enters.

*Proof.* With h=1 there is one colour and S_1=T. The proof of Theorem A gives log d = log D_F + log D_1 with D_F bounded above. For the structure: |U_t|≤1, so a new coordinate can enter only after the previous held coordinate is read. At entry every other coordinate below n_t has been read, so the entrant is the least unread coordinate. If h_{k+1}<h_k, then at the step where the frontier first passed h_{k+1}, at or before h_k's entry, h_{k+1} was unread and would have entered then, putting two coordinates in U together. That is impossible. ∎

So on a computably random source, every one-hole destruction is carried by a single renewable sentinel. This is the least-unread-sentinel geometry of S011/S012, here proved to be forced for an arbitrary one-hole scan, with an arbitrary adaptive filler order. Converting the filler order to increasing order is not claimed; see §7.

**Corollary A3 (bounded-width characterization).** Call a total computable non-monotonic betting strategy *of width h* if its scan is an h-hole scan. Equivalently (Lemma 2), it admits a computable unbounded frontier n_t such that at every step at most h coordinates below n_t are still unread: at most h coordinates are postponed past the frontier at any time. Then

  OH = {z : no total computable non-monotonic strategy of any finite width succeeds on z},

and KLR ⊆ TKLR ⊆ OH, where TKLR denotes randomness against all total computable non-monotonic strategies (S080 Proposition 6).

*Proof.* A width-0 scan is exhaustive with a computable modulus, by Lemma 2 with h=0, so it induces an effective isomorphism. The identity scan is width 0, and by S001 effective isomorphisms preserve computable randomness in both directions. So "no width-0 strategy succeeds" is exactly z ∈ CR. Given z ∈ CR, "no width-h strategy succeeds" is z ∈ OH_h, which is OH by Theorem A. ∎

The certification gate therefore asks exactly: **is there a non-MLR sequence on which no total computable non-monotonic strategy of uniformly bounded postponement width succeeds?** Unbounded postponement width, which KL-style half-splitting arguments use, is precisely what OH does not grant.

## 5. Window predictors and the universal question U(H)

**Corollary A4 (bounded-window predictors).** Let z ∈ CR. Suppose there are:
* a computable sequence of pairwise disjoint finite sets W_0, W_1, … with |W_k| ≤ h,
* an infinite decidable set J ⊆ ℕ,
* a computable sequence of nonconstant Boolean functions g_k on {0,1}^{W_k}, and
* a partial oracle procedure P such that, for every k ∈ J,
  (a) every halting computation P^w(k), on every oracle w, reads no coordinate of W_k; and
  (b) P^z(k) halts with output g_k(z↾W_k).

Then z ∉ OH.

*Proof.* We build an h-hole scan in the style of S079 Theorem 1, with a window in place of the sentinel.

*Epochs.* At the start of an epoch choose the least k ∈ J whose window W_k is entirely unread. One exists because J is infinite, the windows are disjoint, and only finitely many coordinates have been read. Keep W_k unread. At each step read the least unread coordinate outside W_k as a zero-stake filler, and run a bounded simulation of P(k) on the read coordinates, increasing the time bound by one per step. By (a), a halting computation that uses only read coordinates is a valid halting computation for every oracle extending them.

*Trigger.* When a binary halt p becomes visible, read the coordinates of W_k one at a time in a fixed order. Before each one, stake according to the uniform conditional distribution on {w ∈ {0,1}^{W_k} : g_k(w)=p} given the bits already read. Over the window this multiplies capital by 2^{|W_k|}/|g_k^{−1}(p)| ≥ 2^{|W_k|}/(2^{|W_k|}−1) > 1 when the prediction is correct. On a wrong prediction the total window factor is 0. These are fair conditional bets, so the capital process is a nonnegative martingale. Then perform one zero-stake sweep read of the least unread coordinate, and start the next epoch.

*Legality.* An epoch that never triggers reads every coordinate outside its window, leaving at most h holes. If infinitely many epochs trigger, the sweeps read every coordinate. The scan is total, no-repeat and fair, and its next query and stakes are computable from its transcript, so it is an h-hole scan with a computable martingale.

*Success on z.* Each P^z(k) uses finitely many coordinates outside W_k, which fillers eventually expose, so every epoch triggers with a correct prediction. The capital tends to infinity, because each factor is at least 1+1/(2^h−1). By Theorem A, z ∉ OH. ∎

For h=1 and g_k the identity on one coordinate, this is S079 Theorem 1. The new content is that bounded windows and arbitrary nonconstant window functions, for example parities, cost nothing beyond one hole.

**Corollary A5 (U(K) on block-predictable sources).** Fix a block size B and a computable family K=(κ_b) of bijections of {0,1}^B, acting on consecutive B-blocks. Let Y′ ∈ CR. Suppose some block-avoiding partial predictor correctly predicts some nonconstant function of Y′'s blocks on an infinite decidable set of blocks: that is, (a) and (b) of Corollary A4 hold for Y′ with W_k the k-th B-block. Then K⁻¹(Y′) ∉ OH, for every such K simultaneously.

*Proof.* Put z=K⁻¹(Y′) ∈ CR (S001). The predictor for z computes each Y′-block b′≠k from z's block b′ by κ_{b′}, runs P on that virtual oracle, never touches z's block k, and predicts the nonconstant function g_k∘κ_k of z's block k. Corollary A4 applies. ∎

This subsumes S080 Theorem 2, whose block-avoiding autoreduction predicts the whole block. Together with S080 Theorem 4 and Corollary 5′ it sharpens what a counterexample to U(H) must look like:

**Corollary A6 (necessary structure of a U(H) counterexample).** If Y₂ ∈ WAR and H⁻¹(Y₂) ∈ OH, then:
* for every admissible autoreduction M₂ and every role r there are infinitely many non-A_r blocks (S080 Corollary 5′); and
* for every infinite decidable set J of 3-blocks, every computable sequence (g_k) of nonconstant functions on {0,1}³, and every partial procedure that never reads block k on any oracle when computing at k, the procedure fails on Y₂ (diverges or outputs a wrong value) at some k ∈ J.

In particular, no nonzero F₂-linear functional of Y₂'s virtual blocks is predictable from outside the block on an infinite decidable set of blocks. This second item does not depend on H: by Corollary A5, a block-predictable source is excluded simultaneously for every blockwise recoding K, not only for A.

*Proof.* The first item is S080. The second is the contrapositive of Corollary A5. A nonzero linear functional ℓ·y_b is nonconstant. ∎

Informally, every bitwise autoreduction of such a Y₂ must be essentially in-block circular: each virtual bit is computed with the help of block-mates, while no nonconstant block statistic is computable from outside on any infinite decidable set of blocks. Whether such a Y₂ exists, and whether H⁻¹(Y₂) can lie in OH, remains open. U(H) is NOT decided.

## 6. Theorem B — van Lambalgen for OH under uniform relativization

For an oracle A, let OH^[A] be the class of z such that:
* no martingale functional d^(·), total on every oracle, succeeds on z with oracle A; and
* for every scan functional T^(·) that is total, no-repeat and one-hole on every transcript for EVERY oracle, and every martingale functional d^(·) total on every oracle, d^A does not succeed on F_{T^A}(z).

This is the *uniform* (tt-style) relativization. Its first clause is modelled on uniformly relative computable randomness (DEF-0025, SRC-0032 Definitions 5.1–5.2). Theorem B below is the OH analogue of the symmetric van Lambalgen theorem for uniformly relative computable randomness (THM-0024, SRC-0032 Theorem 1.3). Computable scans and martingales ignore the oracle, so OH^[A] ⊆ OH. Relativized Martin-Löf conservation gives MLR^A ⊆ OH^[A].

**Theorem B.** For all x, y: x⊕y ∈ OH ⟺ x ∈ OH^[y] and y ∈ OH^[x].

*Proof of ⇐.* Let T be a one-hole scan and d a computable martingale succeeding on F_T(x⊕y); the identity scan covers computable randomness. Along the winning transcript the factors f_s are positive, and

  log d = Σ_{q_s even} log f_s + Σ_{q_s odd} log f_s =: a + b.

Define the y-scan T^x on x. Simulate T on x′⊕y′: answer odd queries from the oracle y′, and output x′(i) when T queries 2i. This needs no assumption on y′:
* Every T-transcript is one-hole, so it reads infinitely many even coordinates. Hence the search for the next even query terminates on every oracle and every finite x-history, and T^x is total on every oracle.
* Its unread x-coordinates are T's unread even coordinates, at most one.
* The stake at an x-read is T's θ, computed from the T-transcript, so it is a uniformly total martingale functional.

Its capital on x with oracle y is exp(a). If x ∈ OH^[y] then sup a < ∞. Symmetrically, sup b < ∞ if y ∈ OH^[x]. Then sup(a+b) < ∞, a contradiction.

*Proof of ⇒.* Let T^(·), d^(·) be uniformly total, T^(·) one-hole for every oracle, with d^y succeeding on F_{T^y}(x). Build a scan S on x⊕y:
1. To compute T^{y′}'s next x-query and d^{y′}'s stake, simulate the oracle computations. Each time an oracle bit y′(i) not yet read is needed, read coordinate 2i+1 with stake 0.
2. Read the x-query 2j with d's stake.
3. Read the least unread odd coordinate with stake 0 (a sweep).

Uniform totality makes every simulation in step 1 terminate on every oracle, so S is total; every read is fresh. The unread even coordinates of S are those T^{y′} leaves unread, at most one. Since T^{y′} makes infinitely many x-queries, the sweeps read every odd coordinate. So S is a one-hole scan, its stake process is a computable martingale, and its capital on x⊕y equals d^y's capital on F_{T^y}(x), which is unbounded. Hence x⊕y ∉ OH. The case of uniformly relative computable randomness is the same argument with T the identity scan. By symmetry the same holds for y. ∎

*Remark.* In the ⇒ direction the uniform relativization is essential. If T^y were total only for the true oracle y, S could stall on another oracle y′, and repairing that by also sweeping even coordinates would destroy one-holeness or pre-read the held coordinate. The ⇐ direction holds with the stronger hypothesis automatically, because scans derived from computable T are uniformly total.

**Corollary B1 (half-splitting of the gate).** If z ∈ OH∖MLR and z=x⊕y, then x ∈ OH^[y] ⊆ OH and y ∈ OH^[x] ⊆ OH (Theorem B). By van Lambalgen's theorem for MLR (THM-0021), either
* x ∉ MLR, so x ∈ OH∖MLR; or
* x ∈ MLR and y ∈ OH^[x]∖MLR^x, a relativized instance of the gate.

Conversely, any x ∈ MLR and y ∈ OH^[x]∖MLR^x with x ∈ OH^[y] give x⊕y ∈ OH∖MLR. The gate is self-similar under joins.

Unlike the KL setting, where one half of every KL-random sequence must be ML-random, no such splitting theorem is claimed for OH. The usual half-splitting strategy reads one half arbitrarily far ahead while postponing the other, which has unbounded width.

## 7. The certification gate after P4-S081

**What is now excluded.** Any computably random z ∉ MLR in OH must survive every total computable strategy of bounded postponement width (Theorem A). In particular:

1. **Bounded-window non-randomness does not help.** Suppose z's deviation from randomness is detectable from finitely many simultaneously unknown coordinates of uniformly bounded number, with a correct visible prediction at every window of an infinite decidable family. Then z ∉ OH (Corollary A4). This covers block-autoreducibility, predictable parities and the like.
2. **Local c.e. tests with readable structure do not help.** A candidate tried during the session illustrates this. It used c.e. test components closed under single-coordinate flips, so that one held coordinate cannot see which completion is "real". This fails. A 2-hole strategy can wait for the enumeration and read off its structure, for example the centre of an enumerated Hamming ball. By Theorem A, a 2-hole strategy is no stronger than a one-hole one. Any non-MLR certificate must therefore defeat every strategy that postpones boundedly many coordinates and waits on c.e. events.
3. **One-sided c.e. certificates do not help.** Left-c.e. reals carry self-avoiding certificates for the bit value 1: if all coordinates of α↾m except q are read and α_s↾m reaches the completion with α(q)=1, then α(q)=1. Bit value 0 has no c.e. certificate. So neither a one-hole exploitation nor a certification follows for the left-c.e. CR non-MLR reals of THM-0014. Both directions are recorded as open.

**What remains possible.** A certified z must hide its non-randomness so that the only exploiting strategies either
(a) postpone unboundedly many coordinates at once (outside OH's strategy class; the KL half-splitting regime), or
(b) would have to bet on a coordinate that no bounded-width strategy can be holding when the c.e. evidence about it appears.

Every total computable bounded-width strategy holds at most one coordinate across any unbounded wait (Corollary A2). A natural construction therefore suggests itself:
* z agrees with a sequence x random relative to a strong oracle, except on one sparse window per stage;
* the window contents are drawn from a small c.e. family, so z ∉ MLR;
* each window's true content is revealed only after every high-priority strategy's frontier has passed it;
* each window is positioned away from the coordinate that each such strategy holds at the revelation time.

**Why it was not completed (exact obstruction).** Two points were not closed.

(i) *Independence.* The window positions must be chosen without consulting x. Otherwise their positions leak information about held x-coordinates. The construction must then rely on effective Borel–Cantelli over x, which needs the probability that a strategy holds a window coordinate at that window's revelation time to be summable along the chosen windows. Different windows have different revelation times, so this is not automatic.

(ii) *Blind bets on revealed content.* Strategies read window contents as fill coordinates before revelation. Their bets there are bets on a fixed ∅′-computable string taken from a computable family. Keeping the weighted capital of the high-priority strategies from increasing requires choosing the content so as to keep that capital non-increasing. The content family must stay small (for the Martin-Löf test) and c.e. (enumerable by the test). The construction does not control which revelation stages qualify as late enough. No argument reconciling these constraints was completed, so no certification is claimed.

This is the precise remaining obstruction on the construction side. The gate stays open: neither OH∖MLR ≠ ∅ nor OH=MLR is established. The QST-0001 calibration of S080 is unchanged, and it extends trivially to every finite width: OH_h=MLR for any h would answer QST-0001 affirmatively, because KLR ⊆ OH_h.

## 8. Finite audit

`phase4/P4-S081_COLOURING_AUDIT.py` checks the finite combinatorics of Theorem A exactly, with rational arithmetic. On randomly generated buffer scans with up to h postponed coordinates (frontier n_t=⌊t/2⌋), random sources and random rational martingales, it verifies:
* the frontier invariant |U_t| ≤ h;
* first-fit uses at most h colours, and same-coloured held intervals are disjoint;
* every colour scan S_i and the fill scan F is no-repeat, emits one fresh coordinate per step, reads a superset of T's reads, and leaves unread below the frontier only coordinates of its own colour (at most one);
* F reads every coordinate q within 2c(q+1)+h+1 outputs;
* the factor identity d_T = D_F·Π_i D_i holds exactly at every simulated T-time.

It also checks the bookkeeping of Corollary A4's window scan on a planted parity predictor, and the even/odd factor split of Theorem B on random one-hole scans of joins.

These checks support only the finite colouring, pull and factor bookkeeping on truncations. Totality, global hole counts on infinite transcripts, computable randomness and OH membership rest on the written proofs.

## 9. Failed or rejected routes

* **A certified non-MLR OH member via sparse late-revealed windows.** Not completed; obstruction in §7 (i)–(ii).
* **Left-c.e. CR non-MLR reals (THM-0014).** One-sided certificates only; neither OH membership nor exploitation established.
* **Single-flip-closed local tests.** Excluded by Theorem A, since 2-hole strategies reduce to one hole.
* **Simulating partial computable monotone martingales by one-hole scans** (to place OH inside partial computable randomness). Waiting for convergence forces filler reads. The waiting coordinate must eventually be abandoned on stalled branches, and the attempted two-scan product split loses the bets placed while waiting. No inclusion either way is claimed.
* **Normalizing filler order to increasing order** (to reach S012's least-fresh form). Increasing fillers can pre-read the next held coordinate when the original scan looks far ahead. Not claimed.
* **Unbounded-width extension of Theorem A.** With no uniform hole bound, the frontier lemma fails and infinitely many colours would be needed; a sum of infinitely many bounded terms can be unbounded. Not claimed.
* **A record-only proof of z₀ ∈ OH** (impossible by S080), and finite price/escrow/hazard/renewal work, residue tables and unit-column enumeration. Not attempted.

## 10. Disposition

**Proved.**
* Theorem A: OH_h=OH for all h, so the finite-multiplicity hierarchy collapses at two within scans.
* Corollaries A1–A6: the held-bit normal form; the bounded-width characterization of OH; bounded-window predictors; U(K) on block-predictable sources for every blockwise K; the necessary structure of a U(H) counterexample.
* Theorem B: van Lambalgen for OH under uniform relativization, with the half-splitting reduction of the gate.

**Recorded.** The step-(0) catalogue finding: no separation statement in the catalogue.

**Unresolved.** OH∖MLR ≠ ∅ (the certification gate), OH=MLR, U(H), X∈OH for the committed Y, fixed-S preservation, R₂=OH, R₂=OH^iso. No conclusion about the committed X, Y, M or H is drawn.

**Frozen.** All P4-S001–S080 results, including S011/S012, S027 clipping, S033, S037, S057 (exact four paired clipped traces, prospective deadlines, genuine fillers, t/u zero-stake timeout release, mandatory non-s sweep without old-sentinel reset, seven 8/7 versus one ZERO; NOT invoked), S070–S080, and the original Y/M/H/X. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS; Gate 4 NOT REVIEWED; Phase 4 OPEN; Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claim. No owner or external blocker.

**Next: P4-S082.** Attempt the certification construction against the exact obstruction of §7, using the new tools: Corollary A2's single-sentinel normal form, Theorem B's half-splitting, and Corollary A6's constraints. The target is either a CR non-MLR member of OH or a proof that the obstruction is unavoidable for a natural class of constructions. A proof of U(H) through the block-unpredictability constraint of Corollary A6 remains an acceptable alternative.
