# P4-S083 CLOSE — tail-coded holes; north star decided negatively (R₂ ⊊ OH)

Date: 2026-10-10. Incoming remote main `d789bf0e0b743f9c49c6419d6fffe2639d74c060` (the P4-S082 outgoing SHA) was pinned, P4-S083 was confirmed unique, and the incoming prompt is `authoritative/NEXT_SESSION_PROMPT.md`.

**VALIDATED. The north star R₂ = OH is DECIDED NEGATIVELY: R₂ ⊊ OH. R₂ versus MLR, the incoming primary target, remains unresolved and is now the decisive CAND-01 question.**

**Theorem 3.8 (tail-coded separation).** There is a computably random, non-Martin-Löf-random z, computable from ∅‴, such that K(z)∈OH for every computable finite-block recoding K, but D′(z)∉OH. Here D′(z)₀ = z₀, D′(z)ᵢ = zᵢ⊕zᵢ₋₁ is a computable fair homeomorphism. G = F_{T*}∘D′ is a total computable fair-coin-preserving map with all fibres of size ≤ 2, and G(z)∉CR. On z itself the fibre of G is a singleton.

**Mechanism.**
* A one-hole scan of D′(z) holding v_q knows z↾q exactly and the raw tail up to one global complement. So any single absolute tail value determines v_q (Lemma 2.1).
* The S082 §5 construction is rerun with stage-i candidates in pairwise disjoint classes C_{ε↾(i+1)}. It still defeats every raw and block-recoded one-hole scan.
* T* holds the least unread virtual bit and waits until a completed guessed run that is consistent below q shows r = q+2m+4 relatively consistent fixes at or above q. It then predicts v_q all-in. It never needs to predict the potential's value choices; it reads them off.
* A wrong prediction forces anti-consistency on all r fixes. Class separation makes the fooling set W at most ⅛ of every [σ*_j]. Compactness with L_e = 2+4/w_e gives z∈S∖(O∪W).

**Consequences.**
* R₂ ⊊ OH, R_k ⊊ OH (all k ≥ 2) and R_fin ⊊ OH.
* OH^iso ⊊ OH^{blk}: OH is not homeomorphism-invariant.
* Raw one-hole normalization (the P4-S032 target) fails.
* The S082 trichotomy loses case (γ). Remaining: R₂ = MLR (collapse) or MLR ⊊ R₂ ⊊ OH.

**Calibration.**
* SRC-0060 §10 (Rute) read in full; QST-0002 records Rute's Question 10.8 (SOURCE-STATED OPEN, 2016).
* SRC-0071 (Petrović, universal pair of sequence-set strategies; preprint with proofs read; journal version metadata only) yields, as a programme deduction, Proposition 1.1: R_tot = MLR (all total computable fair maps, unbounded fibres). So fibre-boundedness is exactly the resource behind R₂ versus MLR.
* SRC-0019 upgraded; SRC-0072 abstract only; THM-0079–0081, DEF-0066.
* No novelty, priority or openness inference.

**Analysis.** The savings potential β (and Π_∞ for ≤2-to-1 maps) is an exact fixing-martingale for every total fair map, so the only obstruction to potential constructions is computable choice (§7.1).

**Validation.** The exact finite audit passes, and the frozen S082 audit was re-run and passes. Structured adversarial self-review found no fatal issue. Class separation was added in the first draft to close a fooling loophole, and catalogue IDs were reconciled. No multi-agent review was run.

**Frozen.** P4-S001–S082; original Y/M/H/X; S037; S057 (not invoked); S070–S082. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged; Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach claim. Owner/external blocker NONE.

**Files.**
* phase4/P4-S083_MATHEMATICS.md, phase4/P4-S083_VALIDATION.md, phase4/P4-S083_SEPARATION_AUDIT.py, this close record.
* catalog/sources.json, theorems.json, definitions.json, questions.json, authors.json, search-log.md.
* Authoritative records and ledgers.

Next session: **P4-S084**.

## Next-session prompt (copy-ready; identical to authoritative/NEXT_SESSION_PROMPT.md)

# P4-S084 — R₂ versus MLR after the tail-coded separation: is bounded-fibre robustness just Martin-Löf randomness?

Continue the Fairfax-Ball Randomness Research Programme, ONLY Phase 4 Mathematics, in https://github.com/jfairfaxball-348/random.
* Pin independently verified live remote main to the exact P4-S083 outgoing SHA; reconcile discrepancies and confirm P4-S084 uniqueness.
* Review P4-S001–S083 mathematics, especially S004 (asymmetric sheet weights), S007 (width-two skeleton c(n)), S008, S011/S012, S032/S033, S081 (Theorem A, Corollaries A1–A6, Theorem B), S082 (Lemmas 2.1–2.4, 3.1–3.2, Theorems 4.4, 5.1, 6.1, Proposition 6.2, Examples E1–E3) and S083 (Proposition 1.1, Lemma 2.1, Lemmas 3.1–3.6, Proposition 3.7, Theorem 3.8, Corollaries 4.1–4.3, Remarks 4.4–4.5, §§5 and 7).
* Also review the S083 validation and close records, CAND-01, the Gate-3 PASS, both Phase-4 pivots, and SRC-0019, SRC-0060 and SRC-0069–SRC-0072 at their recorded access levels.

STATUS: the north star R2=OH is DECIDED NEGATIVELY (P4-S083 Corollary 4.1): R2 ⊊ OH. Retain:
* MLR = R_tot ⊆ R_fin ⊆ R_k ⊆ R2 ⊆ OH^iso ⊊ OH^blk ⊆ OH^lin3 ⊆ OH = OH_h = R_k^scan ⊊ CR, for k ≥ 2;
* MLR ⊊ OH, OH^blk∖R2 ≠ ∅, and KLR ⊆ TKLR ⊆ OH.

MLR = R_tot is a programme deduction from SRC-0071, an unrefereed preprint whose journal version is recorded at metadata level only. Preserve the ORIGINAL CR Y, the clipped syntactically self-avoiding wtt autoreduction M, the repeated H (A=[101;110;111]) and X=H^{-1}(Y), all unaltered.

S083 SETTLED:
(1) Tail-coded holes. Let D′(z)_0=z_0 and D′(z)_i=z_i⊕z_{i−1}, a computable fair homeomorphism. A one-hole scan of D′(z) holding v_q knows z↾q exactly and z↾[q,M) up to one global complement, and any single absolute value z_F with F≥q determines v_q.
(2) Class separation. The S082 §5 runs keep all their invariants when the stage-i candidates are taken from class C_{ε↾(i+1)} (classes pairwise disjoint). The fixes an incomparable run makes from its divergence stage on avoid every true-run fix.
(3) The scan T*. It holds the least unread virtual coordinate and reads fillers. It resolves when a completed run of length m is consistent below q and shows r(q,m)=q+2m+4 relatively consistent fixes in [q,∞), predicting v_q all-in. A prediction is wrong iff the run is anti-consistent on all selected fixes, and the fooling set W has relative measure ≤1/8 in every [σ*_j]. T* can be fooled by adversarial completions.
(4) Theorem 3.8. There is z∈OH^blk∖MLR (≤_T ∅‴) with D′(z)∉OH. G=F_{T*}∘D′ is total computable fair with all fibres ≤2, and G(z)∉CR. Hence R2 ⊊ OH, R_k ⊊ OH, R_fin ⊊ OH and OH^iso ⊊ OH^blk; OH is not homeomorphism-invariant, and raw one-hole normalization fails.
(5) Proposition 1.1. Petrović's universal pair of sequence-set strategies gives robustness under ALL total computable fair maps = MLR. Unbounded fibres suffice to destroy every CR∖MLR source.
(6) §7.1. The savings potential β is an exact fixing-martingale for every total fair map; the counting potential Π_∞ plays this role for ≤2-to-1 maps. The only obstruction to potential constructions is the computability of the choices.

PRIMARY TARGET: decide R2 versus MLR. This is the decisive CAND-01 collapse question. R2=MLR means the bounded-fibre preservation notion collapses to MLR=R_tot; MLR⊊R2⊊OH means a genuinely intermediate notion.
(a) Construct z∈R2∖MLR. A necessary first step is z∈OH^iso∖MLR. Such a z must defeat every coded-hole scan, including self-referential tail-coded scans that simulate the construction (the S083 T* mechanism). Candidate tools:
  * fixing inside gaps below the current maximum, which is free against tail-coded holes;
  * selecting completions inside fooling sets, with a potential that accounts for this;
  * exact fixing-martingales (β or Π_∞) whose choices are made from finitely many guesses;
  * the S007 width-two skeleton.
Or (b) prove R2 = MLR, or the stronger OH^iso = MLR: every CR∖MLR source is destroyed by some total computable fair map with all fibres ≤2. One route is to orient coded holes using Martin-Löf tests, adapting the T* mechanism and Petrović's half-betting universality to bounded fibres. Or (c) prove a sharp structural theorem separating the two possibilities for a precisely defined class.
Secondary, only where it serves the primary target: R2 versus OH^iso (is every k=2 destruction a homeomorphism-coded one-hole destruction? note asymmetric sheet weights, P4-S004), and R_fin versus R2.

Do NOT:
* attempt a record-only proof of z0∈OH;
* resume finite price/escrow/hazard/renewal work, residue tables, unit-column enumeration, or multi-hole variants of one-hole arguments.

Every scan must be everywhere total, computable, no-repeat, fair-coin preserving and at most one-hole on EVERY transcript. Every k=2 map must be total computable, fair-coin preserving, with all fibres of size ≤2. Distinguish MLR, R_tot, R_fin, R2, OH^iso, OH^blk, OH^lin3, OH, KLR, TKLR and Rute's ER/AR carefully. No openness or priority inference may be drawn from missing searches; record access levels for any literature used.

Freeze all P4-S001–S083 results, especially S037, S057 (exact four paired clipped traces, prospective deadlines, genuine fillers, t/u zero-stake timeout release, mandatory non-s sweep without old-sentinel reset, seven 8/7 vs one ZERO) and S070–S083. PA-0001 UNRESOLVED_UNDER_INSPECTED_EVIDENCE, DEF-0020 unchanged, Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED. No novelty, openness, prior-art, publication or outreach assertions.

CLOSEOUT (mandatory, per docs/SESSION_PROTOCOL.md):
1. Validate, synchronize the authoritative records, and commit atomically.
2. Push the session branch, merge it into main (fast-forward when possible, never rewriting main history) and push main.
3. Independently verify with `git ls-remote origin refs/heads/main` that remote main equals the outgoing SHA.

The P4-S084 close record and the final report must both contain the full copy-ready P4-S085 prompt, identical to authoritative/NEXT_SESSION_PROMPT.md, unless an owner/external blocker exists, in which case state the blocker and give no prompt.
