# P4-S008 — k=2 scan freshness and permutation-completion boundary

Date: 2026-10-05
Session: P4-S008
Incoming checkpoint: 22fa3f66558a92eae070ded127035dec2f128e1e
Scope: Phase 4 — Mathematics; selected CAND-01 only; k=2 only
Result: **A GLOBAL k=2 NO-REPEAT SCAN CANNOT DESTROY COMPUTABLE RANDOMNESS ON A PERSISTENT-HOLE / DOUBLE-FIBRE SOURCE; ANY WINNING SCAN SOURCE MUST LIE ON A SINGLETON FIBRE WITH AN OUTWARD-MOVING HOLE. THE COMPUTABLE COALESCENCE SCHEDULE DOES NOT BY ITSELF TURN THAT SINGLETON ROUTE INTO ONE COMPUTABLE MARTINGALE OR PERMUTATION COMPLETION; NO EXACT k=2 DESTROYER OR GENERAL PRESERVATION THEOREM IS OBTAINED.**

## Authority, uniqueness and scope

Live `main` matched the incoming checkpoint exactly before substantive work. The expected P4-S008 mathematics/close/validation files did not exist on the incoming checkpoint, and the session ledger named P4-S008 only as the recommended next session. P4-S008 was therefore unused.

Gate 3 is PASS and Phase 4 is OPEN for selected CAND-01. Phase 5 remains CLOSED. P4-S001 through P4-S007 are preserved exactly. This session stays strictly at k=2.

P4-S005 through P4-S007 are treated as settled boundaries. This session does not revisit computability of the P4-S004 crossing measures, canonical-sheet mass, one-hole/XOR variants, or the P4-S007 coherent width-two skeleton/generalized collapse result.

PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. The pre-Phase-4 Gate-3 guard remains historical. DEF-0020 and all catalogue/source convention guards are unchanged. No k>2, novelty/open-status, Gate-4, publication or outreach claim is made.

## Exact scan model

Let T be a total computable adaptive no-repeat scan. From a finite transcript tau, T computes the next source coordinate q(tau), and along every transcript no coordinate is queried twice.

For source x, define y=F_T(x) recursively by

y(s) = x(q(y restricted to s)).

Because every new output bit reads a fresh fair-coin coordinate, F_T is everywhere total computable and fair-coin preserving.

For an infinite transcript y write

Q(y) = { q(y restricted to s) : s in omega }.

The fibre over y consists exactly of the assignments to coordinates outside Q(y), with the coordinates in Q(y) fixed by the transcript. Hence every fibre has size at most two exactly when every transcript leaves at most one source coordinate unqueried.

This is the P4-S003 scan-fibre calculation, now used together with the P4-S007 coalescence schedule.

## Lemma 1 — the P4-S007 schedule has an exact scan interpretation

Fix n and a transcript prefix tau of length m. Let

Q_m(tau) = { q(tau restricted to s) : s < m }.

Then the number of length-n source strings compatible with tau is exactly

2^(n - |Q_m(tau) intersect {0,...,n-1}|).

Therefore, for the P4-S007 computable monotone schedule c(n), every transcript prefix of length c(n) has queried at least n-1 of the first n source coordinates.

Equivalently, after c(n) there is at most one fresh source coordinate below n.

### Proof

The transcript fixes precisely the source bits at the fresh coordinates already queried. Every source coordinate below n not yet queried is still free, independently, and each choice gives a distinct compatible length-n source string. The displayed count follows.

P4-S007 gives at most two compatible length-n strings at stage c(n), so the number of unqueried coordinates below n is at most one. QED.

This is the exact freshness pressure imposed by global k=2 on a scan: after c(n), all low-coordinate freshness is concentrated in at most one moving hole.

## Lemma 2 — fixed-sentinel permutation completion

Fix a source coordinate j.

There is a total computable adaptive no-repeat scan P_j which queries every source coordinate exactly once on every transcript and has the following property:

- it first queries j and ignores that bit for purposes of simulating T;
- it then follows T as long as T does not request j;
- if T ever requests j, P_j abandons the T simulation and queries all remaining unqueried coordinates in increasing order;
- if T never requests j, global k=2 forces T to query every coordinate other than j, so P_j again queries every coordinate exactly once.

Consequently the map G_j induced by P_j is an everywhere-total computable fair-coin-preserving bijection of Cantor space with an everywhere-total computable inverse.

### Proof

Before T requests j, all T-queries are fresh and different from the already queried sentinel j, so P_j is no-repeat. If T requests j at a finite stage, switching to the increasing enumeration of as-yet-unqueried coordinates gives a computable exhaustive fresh scan.

If T never requests j, then j is absent from the original T-query set. Since every T transcript omits at most one coordinate, no other coordinate can be omitted; T therefore queries every k different from j. Thus P_j is exhaustive on this branch as well.

An exhaustive adaptive fresh scan is bijective: an output transcript computes the successive queried coordinates and therefore assigns one bit to every source coordinate. The inverse computes any requested source bit by simulating until its coordinate is queried. Fair-coin preservation follows from freshness of every query. This is exactly the k=1 effective-isomorphism regime of P4-S001. QED.

## Lemma 3 — an omitted coordinate kills the scan counterexample route

Let d be any computable martingale on the output transcript of T.

For each fixed j there is a computable martingale d_hat_j on the output of G_j such that, on every source x for which T never queries j, d_hat_j(G_j(x)) has exactly the same capital evolution as d(F_T(x)), apart from the initial ignored sentinel bit.

Therefore, if x is computably random and d succeeds on F_T(x), T must query every source coordinate on x.

### Proof

The first output bit of G_j is the sentinel x(j); d_hat_j leaves its capital unchanged there.

While P_j is following T, the subsequent output bits are exactly the T-transcript bits. On those steps d_hat_j uses the same wagers as d.

From the simulated T-transcript, d_hat_j can detect before the next fresh output bit whether T's next requested coordinate would be j. If so, P_j switches to filler mode and d_hat_j freezes its capital forever. This preserves the martingale equation because both children then receive the same capital.

If T never queries j on x, the switch never occurs and the post-sentinel output of G_j(x) is exactly F_T(x). Hence success of d transfers to success of d_hat_j.

But G_j is a computable fair-coin-preserving bijection with computable inverse. By P4-S001, it preserves computable randomness. Thus no computable martingale can succeed on G_j(x) when x is computably random. Contradiction. QED.

## Corollary 4 — any scan destroyer must win on a singleton fibre

Suppose a total computable adaptive no-repeat scan T is fair-coin preserving, has global fibres of size at most two, x is computably random, and F_T(x) is not computably random.

Then Q(F_T(x)) = omega. In particular F_T^{-1}(F_T(x)) = {x}.

So a scan-based k=2 non-conservation witness, if one exists, cannot use a persistent missing coordinate or a double fibre at the winning source.

This removes the most direct way to keep one genuine betting coordinate permanently fresh.

## Lemma 5 — on the only surviving route, the hole must move outward

Let x be on a singleton fibre of a global k=2 scan and put y=F_T(x).

At stage c(n), at most one coordinate below n is unqueried. If such a coordinate exists, call it h_n(y).

Because the fibre is singleton, every fixed source coordinate is eventually queried. Hence no fixed coordinate can equal h_n(y) for all sufficiently large n.

More strongly, for every r there is N such that for every n >= N, either no coordinate below n is unqueried at c(n), or h_n(y) >= r.

Thus the only surviving freshness mechanism is a moving hole whose location escapes every fixed finite source prefix.

### Proof

This is the scan specialization of P4-S007's singleton-phantom theorem. Two compatible n-prefixes for a scan differ exactly at the one unqueried coordinate below n. If a recurrent hole stayed below a fixed r along arbitrarily large n, the coherent skeleton would retain a second infinite path differing from x below r, contradicting singletonhood. QED.

## Why the fixed-sentinel theorem does not yet extend to the moving-hole singleton route

Lemma 3 gives a computable permutation completion for every fixed sentinel j. On a singleton transcript, however, T eventually queries every j. Therefore every fixed-sentinel martingale d_hat_j eventually freezes after only finitely many genuine T-bets.

One can build a uniformly computable family of these permutation completions, but P4-S007 supplies no computable relation between the time at which d reaches a new large capital level and the time at which a chosen sentinel j is eventually consumed by T.

A static computable mixture over j therefore incurs an index-dependent weight with no proved compensation from the growth rate of d. This is the same type of rate/coherence obstruction already seen for fixed-stage mixtures, but no P4-S004 crossing-measure argument is reopened here.

A dynamic permutation completion faces the complementary problem. To remain globally exhaustive it must move to a new sentinel when the old one is consumed. Prequerying the next sentinel can steal a coordinate that T later wants as a genuine nonmonotonic bet. Repeating this indefinitely on a singleton path is exactly the freshness/pre-revelation issue isolated by P4-S007.

The computable c(n) bounds how many low coordinates remain fresh at the sampled stage. It does not give a computable deadline by which the unique current hole, when it is only a singleton phantom, must be consumed. Such a deadline would amount to the last-injury/stabilization information that P4-S007 explicitly does not force.

Accordingly, the fixed-sentinel permutation argument cannot be promoted in this bounded session to a general scan-preservation theorem.

## SRC-0061 consequence

SRC-0061 / THM-0072 is not reused as a k=2 witness.

To reuse its unrestricted nonmonotonic scan, one would now need all of the following:

1. a total no-repeat completion whose every transcript leaves at most one coordinate unread;
2. a computably random winning source on a singleton fibre, by Corollary 4;
3. a proof that the moving-hole completion never pre-reveals enough later genuine betting positions to destroy the win;
4. fair-coin preservation on every transcript, not only the winning one.

The committed SRC-0061 mechanism supplies no such singleton-fibre moving-hole freshness theorem. The previous filler route therefore remains unlicensed.

## Successful and failed mechanisms

Successful:

1. Exact scan interpretation of c(n): after c(n), every transcript has queried at least n-1 of the first n source coordinates.
2. A fixed-sentinel construction turning any global k=2 scan into a total computable adaptive permutation.
3. A computable output martingale transfer showing that a computably random winning source cannot lie on a double-fibre / persistent-hole transcript.
4. Reduction of any possible scan-based k=2 destroyer to the singleton-fibre case.
5. Identification of the surviving freshness pattern as an outward-moving hole.

Failed or incomplete:

1. Combining the uniformly computable fixed-sentinel permutation completions into one computable source martingale without assuming a computable success-rate/query-time relation.
2. Turning c(n) into a computable deadline for consumption of the singleton phantom hole.
3. Constructing a dynamic sentinel scheme that is globally exhaustive while never pre-revealing later decisive bets.
4. Reusing SRC-0061 with the full global fibre, freshness and non-pre-revelation checks.
5. Constructing an exact total computable fair-coin-preserving k=2 computable-randomness destroyer.
6. Proving general forward computable-randomness preservation for k=2, or even for the full global k=2 no-repeat-scan subclass.

## Proof dependencies and guards

The new mathematics uses the P4-S003 scan-fibre identity, P4-S007's computable coherent width-two skeleton/coalescence schedule, and P4-S001's k=1 effective-isomorphism preservation theorem. No new literature theorem is imported.

SRC-0061 / THM-0072 is used only as the previously recorded unrestricted scan mechanism. It is not claimed to satisfy the newly isolated singleton moving-hole condition.

- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- The pre-Phase-4 Gate-3 guard is preserved historically.
- P4-S001 through P4-S007 are unchanged exactly.
- General k=2 forward computable-randomness preservation/failure remains unresolved.
- No result is claimed for k>2.
- DEF-0020 and all catalogue/source convention records are unchanged.
- No novelty/open-status claim is made.
- Gate 4 is not reviewed. Phase 5 remains CLOSED.
