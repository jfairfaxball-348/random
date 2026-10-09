# P4-S081 CLOSE — bounded-hole collapse, van Lambalgen for OH, sharpened certification gate

Date: 2026-10-09. Incoming remote main `b8017ed6f3090bcdd5bcbd5f4ceba8058cc7bacf` (the P4-S080 outgoing SHA) pinned; P4-S081 unique. **VALIDATED STRUCTURAL THEOREMS. The certification gate is NOT passed; U(H) and the north star are unresolved.**

Step (0): the catalogue, at its recorded access levels, contains no statement separating randomness against total computable non-monotonic strategies (or KLR) from MLR. No openness inference is drawn.

**Theorem A (bounded-hole collapse).** For every finite h, robustness against total computable adaptive no-repeat scans with at most h unread coordinates on every transcript equals OH.
* Proof: a compactness frontier gives at most h held coordinates at any time. Online first-fit colouring gives h one-hole colour scans and one fill scan, the fill scan being an effective isomorphism. The log-capital splits, so one colour scan must win.
* Corollaries: R_k^scan = OH for all k≥2 (the scan multiplicity hierarchy collapses at two); the held-bit (single renewable sentinel) normal form; OH = randomness against total computable non-monotonic strategies of uniformly bounded postponement width.
* Bounded-window predictors of any nonconstant window function exclude OH membership. A block-predictable Y′ gives K⁻¹(Y′) ∉ OH for EVERY computable blockwise recoding K, so a U(H) counterexample must be block-unpredictable.

**Theorem B.** x⊕y ∈ OH ⟺ x ∈ OH^[y] and y ∈ OH^[x], under uniform relativization (the OH analogue of THM-0024). The gate is self-similar under joins.

**Exact remaining obstruction (certification).** The sparse late-revealed window construction needs (i) independence of window placement from the random background, and (ii) control of blind fill bets on revealed window content under a small c.e. content family. Neither was closed, so no non-MLR OH member is claimed. OH=MLR, U(H), X∈OH, fixed-S preservation, R₂=OH and R₂=OH^iso remain UNRESOLVED.

**Validation.** The exact finite audit passes: 9660 factor identities over 60 buffer scans, the Corollary A4 window scan, and the Theorem B factor split. An audit-check placement bug was found and fixed; no mathematical claim changed. A structured adversarial self-review applied wording fixes, including inclusive held intervals. No multi-agent review was run.

**Frozen.** P4-S001–S080; original Y/M/H/X; S037; S057 (not invoked); S070–S080. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty/openness/prior-art/publication/outreach claim. Owner/external blocker NONE.

Files: phase4/P4-S081_MATHEMATICS.md, phase4/P4-S081_VALIDATION.md, phase4/P4-S081_COLOURING_AUDIT.py, this close record.

Next session: **P4-S082**.

## Next-session prompt (copy-ready; identical to authoritative/NEXT_SESSION_PROMPT.md)

# P4-S082 — The certification construction against the exact obstruction, or a proof that it is unavoidable

Continue the Fairfax-Ball Randomness Research Programme, ONLY Phase 4 Mathematics, in https://github.com/jfairfaxball-348/random. Pin independently verified live remote main to the exact P4-S081 outgoing SHA; reconcile discrepancies and confirm P4-S082 uniqueness. Review P4-S001–S081 mathematics, especially S008, S011/S012, S032/S033, S079, S080 and S081 (Theorem A, Corollaries A1–A6, Theorem B, §7 obstruction), together with S081 validation and close, CAND-01, the Gate-3 PASS and both Phase-4 pivots.

NORTH STAR: decide R2=OH, keeping R2=OH^iso separate. Retain MLR ⊆ R2 ⊆ OH^iso ⊆ OH ⊊ CR and KLR ⊆ TKLR ⊆ OH. Preserve the ORIGINAL CR Y, the clipped syntactically self-avoiding wtt autoreduction M, the repeated H (A=[101;110;111]) and X=H^{-1}(Y), all unaltered.

S081 SETTLED:
(A) Bounded-hole collapse: OH_h=OH for every finite h. Robustness against total computable adaptive no-repeat scans with at most h unread coordinates on every transcript equals OH. Within scans the finite-multiplicity hierarchy collapses at k=2 (R_k^scan=OH for all k≥2).
(A2) Held-bit normal form: on computably random sources, every one-hole destruction is carried by bets on held coordinates (sentinels). Held coordinates are the least unread at entry, strictly increasing, one at a time.
(A3) OH = randomness against total computable non-monotonic strategies of uniformly bounded postponement width.
(A4–A6) A correct block-avoiding predictor of any nonconstant function of bounded disjoint windows, on an infinite decidable set, excludes OH membership. If Y′ ∈ CR is block-predictable in this sense, then K^{-1}(Y′) ∉ OH for EVERY computable blockwise recoding K. A counterexample to U(H) must therefore be block-unpredictable.
(B) Van Lambalgen for OH under uniform relativization: x⊕y ∈ OH ⟺ x ∈ OH^[y] and y ∈ OH^[x]. The gate is self-similar under joins.
The catalogue contains no statement separating total-strategy non-monotonic randomness from MLR. The certification gate (OH∖MLR ≠ ∅?) and U(H) remain UNRESOLVED.

PRIMARY TARGET: attack the exact obstruction isolated in S081 §7.
(a) Construct a computably random z ∉ MLR and PROVE z ∈ OH, using the held-bit normal form: only one held coordinate survives any unbounded wait. A natural design uses sparse windows whose content comes from a small c.e. family and is revealed only after every high-priority strategy's frontier has passed it, with the windows positioned away from held coordinates. Resolve explicitly (i) independence of window placement from the random background, for example by effective Borel–Cantelli over held-coordinate probabilities, and (ii) blind fill bets on the revealed window content, by a content-selection rule compatible with a small c.e. family and with late revelation. Then test z, or a modification, for R2-membership or for H(z) ∉ OH, aiming at R2 ⊊ OH; or
(b) prove the obstruction unavoidable for a precisely defined natural class of constructions, or reduce OH∖MLR ≠ ∅ to a stated catalogued problem.
A proof of U(H) is an acceptable alternative, for example by showing that every Y′ ∈ WAR is block-predictable in the sense of S081 Corollary A5, or is otherwise one-hole exploitable after recoding. It would give X ∉ OH but not R2=OH.

Do NOT attempt a record-only proof of z0 ∈ OH (impossible by S080). Do NOT resume finite price/escrow/hazard/renewal work, residue tables, unit-column enumeration, or multi-hole variants of one-hole arguments; S081 Theorem A makes bounded hole budgets irrelevant. Every scan must be everywhere total, computable, no-repeat, fair-coin preserving and at most one-hole on EVERY transcript (via Theorem A, boundedly many holes is equivalent). Distinguish MLR, KLR, TKLR, OH, OH^[A], R2 and OH^iso carefully. No openness or priority inference may be drawn from missing searches.

Freeze all P4-S001–S081 results, especially S037, S057 (exact four paired clipped traces, prospective deadlines, genuine fillers, t/u zero-stake timeout release, mandatory non-s sweep without old-sentinel reset, seven 8/7 vs one ZERO) and S070–S081. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE, DEF-0020 unchanged, Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach assertions.

CLOSEOUT (mandatory, per docs/SESSION_PROTOCOL.md): validate; synchronize authoritative records; commit atomically; push the session branch; merge it into main (fast-forward when possible, never rewriting main history) and push main; independently verify with `git ls-remote origin refs/heads/main` that remote main equals the outgoing SHA. The P4-S082 close record and the final report must both contain the full copy-ready P4-S083 prompt, identical to authoritative/NEXT_SESSION_PROMPT.md, unless an owner/external blocker exists, in which case state the blocker and give no prompt.
