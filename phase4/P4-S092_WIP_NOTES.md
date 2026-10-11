# P4-S092 — WORK IN PROGRESS (scratch checkpoint, NOT a session close)

Status: **S092 IN PROGRESS. Not closed. No result claimed. Main untouched.**
Saved because of an owner-reported usage limit. Nothing here is a theorem unless marked PROVED; everything else is analysis.

## 0. Entry reconciliation (done)

* Live remote main: `ec2c6ff1b5050b1b324d10b007843b1336bd7010` (owner handoff amendment, docs only).
* Its sole parent: `6633f88ba8a0826442618f5062cb2d74b83c9e86` (S091 atomic close), whose sole parent is `971b3ccef56fc5654c857a32e882342c80e325c2` (S090). Matches the prompt.
* Amendment changes only the mandate (STATE.json `next_session_owner_direction`, prompt, close handoff); mathematics and session counter unchanged.
* No open/closed PRs via REST; zero check runs and zero commit statuses on main. Side branches are historical (S081–S091 work branches, `docs/strengthen-r2-mlr-handoff` = main).
* No S092 file or branch existed at entry. S092 unused.
* Incoming prompt is byte-identical to `authoritative/NEXT_SESSION_PROMPT.md` except a trailing newline; archived as `P4-S092_INCOMING_HANDOFF.md` (+ `.sha256`).
* Read: SESSION_PROTOCOL, GATE/SOURCE policies, both pivots, S082 §§2–6 (incl. §6.3), S083, S084, S085, S086, S087 (incl. §6.1–6.3), S088 opening/defs, S089 Thm 1 / §5 dichotomy, S090, S091. Source records SRC-0071 etc. read at recorded access only; no external retrieval.

## 1. Proof gate 1 — exact finishing statements

Equality: ∀z∈CR∖MLR ∃G∈F₂ ∃ computable martingale d: d succeeds on G(z). (Source-dependent choice among computable G allowed; no noncomputable G.)

Separation: ∃z∉MLR ∀G∈F₂: G(z)∈CR (same z; must handle non-effective validity).

Sufficient for equality (strictly stronger): OH^iso = MLR, i.e. every z∈CR∖MLR has a computable fair homeomorphism K and a one-hole scan T with F_T(K(z))∉CR (since R₂⊆OH^iso).

## 2. Equality-side analysis: race orientation (NOT proved)

Mechanism. Frame K, hold virtual q with partner involution ψ_q = K⁻¹∘flip_q∘K. Read fillers; resolve when exactly one candidate's raw window lies in V_{n(q),s} for an ML test V; bet all-in on it; use the S084 Lemma 3.2 restart martingale.

Candidate sufficient condition (Orientation property, OP): there are K, computable n(·) and an ML test V with z∈⋂_n V_n and ψ_q(z)∉V_{n(q)} for all large q. Then every hold on K(z) resolves (z∈V_{n(q)}), only finitely many errors occur, and d_restart succeeds, giving z∉R₂. Legality of the scan is as for S083 T* (bounded simulations, no repeats, ≤1 permanent hole). **Still to write out and audit; OP itself is the open global obligation.**

Observations so far:
* For any universal or partner-closed test, ψ_q(z) is also non-MLR (computable fair involution), so OP fails; deficiencies of z and ψ_q(z) differ by at most K(q)+O(1). Races are then decided by enumeration order (cf. S087 §6.1).
* A c.e. test can carry only finitely much information about z, so excluding infinitely many partners must be *structural* (the test's shape must break under ψ_q), not pointwise.
* Heuristic class where OP seems to hold: points with fixed values on a sparse set P whose positions are cheaply describable/approximable, random elsewhere; tail-coded holes + a test tailored to P's approximation let partners enter only by chance. Requires a real proof (CR of such points, chance bound, randomness of the free part) — not done.
* Open: does every z∈CR∖MLR admit such structural exclusion in some frame? No proof; no counterexample.

## 3. Separation-side analysis (NOT proved)

* S084: any z∈R₂ must make the error stream of every infinitely resolving scan computably random (frequency ½). A survivor must therefore lose a random half of races/readings in every frame.
* Decoys via wrong runs: a simulating self-reader identifies the true run by data consistency, so decoys must be genuine wrong runs consistent with the partner — not arrangeable by the uniform run procedure without knowing the true future.
* Forcing z into fooling events costs relative measure 2^{−r(q,m)} each and breaks the fixed compactness margins (27/32 etc.); not viable as stated.
* Making states symmetric under the current partner = invariant (halving) splits; blocked for the rigid three-core conditionally on Conjecture R (S089). Stalling via control concentration (S091 Prop 6) linearizes K_mix locally but creates control constraints readable in other frames; regress unresolved.

## 4. Side facts checked (standard-type arguments; to be re-verified before recording)

* CR^{∅′} ⊆ MLR: for a universal test U, Σ_n λ(U_n∩[σ])/λ[σ] is a ∅′-computable martingale succeeding on ⋂U_n. The same construction shows any CR^{∅′} point has every total computable fair image CR — consistent with R_tot = MLR, gives no survivor.
* For G∈F₂ and z∉MLR: G(z)∈MLR iff z's fibre partner is MLR (conservation + MLR no-randomness-from-nothing); destruction needs a non-MLR partner or a singleton fibre.
* AR ⊆ OH^iso (catalogue DEF-0066 caution). Whether AR ⊆ R₂ is unknown; if it held, R₂ = MLR would force AR = MLR (QST-0002 territory). Not established.

## 5. Next steps when resumed

1. Write the OP ⇒ z∉R₂ implication as a full lemma with all-transcript legality and audit it (likely PROVABLE; would be a conditional reduction, not a resolution).
2. Attack OP for arbitrary z∈CR∖MLR: try structural exclusion via a frame chosen from z's test; search for a counterexample class where every frame's tests are partner-closed near z.
3. If OP stalls, carry the failure into a separation construction that randomizes races in all frames while keeping the S082 potential invariant; address S082 §6.3 / S087 §6.2 explicitly.
4. Then gates 4–6, validation, close records, ledger sync, S093 prompt, single atomic commit merged to main.

Guards unchanged: PA-0001, DEF-0020, Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty/openness/publication claim.
