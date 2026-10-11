# P4-S093 validation — orientation as autoreducibility, left-c.e. window criterion, category and forcing obstructions

Date: 2026-10-11. Phase 4 Mathematics ONLY. Mode: written adversarial self-review and exact finite audit. No Lean, no independent agent, no external review, no hosted CI success claimed.

## 1. What is validated

**Theorem A.**
* *(b)⇒(a).* The sets O_h=K⁻¹{u : Φ^u(h)↓=u_h} are effectively open uniformly in h. Each is enumerated through finite strings ρ with a halting, use-bounded, correct computation, and then cylinders [σ]⊆K⁻¹[ρ]. That inclusion is decidable because K⁻¹[ρ] is a uniformly computable clopen set. z∈O_h is immediate. ψ_h(z)∉O_h uses only self-avoidance and K(ψ_h(z))=K(z)⊕e_h. Both (C1) and (C2) then hold at every h, not merely at reached holds or almost all h.
* *(a′)⇒(b).* The search is self-avoiding: it never reads oracle position h. It uses the two completions u^0, u^1, computed from the oracle with position h overwritten. The canonical schedule (t from h, M=t+1) is history-independent. This was re-derived: when h becomes a hold, exactly h coordinates have been read, and every later step reads exactly one coordinate. So the race the oracle procedure runs is the reader's race. Ties and the finitely many exceptional holds are patched; patching preserves self-avoidance.
* The coverage form implies the race form trivially.
* *Edge cases checked.* The partner is computed through K⁻¹ from the flipped virtual window, not assumed. Raw windows use ℓ(M)=max{ℓ : μ(ℓ)≤M} with μ a modulus of K⁻¹. A separating string automatically separates the two completions, because one completion is in [σ] and the other is not.
* *What Theorem A does not cover.* The reached-hold form of S092 Theorem 1's hypotheses. The record says so explicitly (Remark (ii)).

**Corollary A2.** Uses S092 Theorem 1 with Sel≡true. Theorem 1's legality was re-checked on every transcript (resolutions, ties, permanent holds). Its success claim needs (C1) at reached holds (true, since (C1) holds at all holds) and (C2) at almost all reached holds (true at all holds).

**Corollary A3.** Uses only:
* the frozen S092 Proposition 1.2;
* the frozen inclusion KLR⊆OH;
* the fact that computable fair homeomorphisms are a.e.-computable measure-preserving automorphisms in SRC-0060's sense;
* THM-0080's chain, at its recorded STATEMENT_INSPECTED level.

The catalogue's own definition note already records "automorphism randomness ⊆ OH^iso". QST-0002 is cited only at its recorded status (SOURCE-STATED OPEN, 2016 evidence, no later check). No openness, novelty or difficulty claim is drawn beyond the stated implication.

**Proposition L1.** The proof uses only that approximations are strictly below α (α not dyadic) and that the smaller completion, being a computable homeomorphic image of α or α itself, is not eventually 1. For a computably random α both completions are computably random (THM-0038), hence not eventually constant. For a general non-dyadic left-c.e. α the argument still holds on the branch α=x^<, since α itself is not eventually 1.

**Proposition L2.**
* Ties are possible only if the partner and α are first seen at the same check, and are zero-stake.
* The length constraint |σ|≤M can delay both coverages but cannot reverse their order. Monotonicity of the approximations forces every partner-covering index below every α-covering index.
* Level N(h)≥h+1 guarantees that every string at the level separates the two completions.
* S092 Lemma 5.3 is the case N=h+1, and Land_N ⇒ Land_{h+1} by nesting of windows.

**Corollary L3(b).** Uses S092 Corollary 2 / S084 Theorem 1 as frozen. Infinitely many reached holds exist because every hold resolves.

**§3.3 failed route.** The inequality h·δ_{2h} ≤ Σ_{j≥h}δ_j for non-increasing nonnegative δ is exact. It turns summability into a computable modulus, so the route excludes nothing for non-computable α. It is recorded as a failure.

**Proposition L4.** Turing invariance under computable homeomorphisms is elementary. The existence of z∈CR∖MLR with z≡_T∅″ uses THM-0014 at its recorded STATEMENT_INSPECTED level, applied to the high degree of ∅″.

**Lemma G.** Density was re-checked: ψ_h([τ])=[τ] once h≥μ(|τ|); the wrong point y lies in [τ]; a neighbourhood fixing the finite use lies in the "wrong" part. The genericity sets S_{h₀} are Σ⁰₂ (a Σ⁰₁ part, by compactness, and a ∃h Π⁰₁ divergence part). A 2-generic meets every dense Σ⁰₂ set of strings.

**Lemma M.** CR∖MLR is nonempty (THM-0002; S082) and closed under finite changes, hence dense. The martingale d(σ0)=3d(σ)/2, d(σ1)=d(σ)/2 is computable and fair.

**Proposition F.**
* The counting identity c^A+c^B=c^Q+[cell meets both] holds for disjoint A,B with A∪B=Q; with λ(A)=λ(B)=λ(Q)/2 it gives the stated formula.
* The equal-measure claim uses that ψ_h is λ-preserving, maps C_h to itself, and swaps right and wrong.
* For identity-frame strategies the split weight vanishes once t exceeds the onset of the pair difference.
* The all-in example (β=1) is checked exhaustively on small windows of the tail-coded frame.

**Proposition S.** Presented as a conditional sketch only. Its hypothesis ASSCL is open, and the complete re-verification of S082 §4 in the clopen, identity-frame, forcing-augmented setting is not claimed. The guessing of the Σ⁰₁ halting bits was checked for consistency: wrong guesses may diverge harmlessly; on the true run ASSCL converts non-halting into divergence on the whole state.

## 2. Exact finite audit

`phase4/P4-S093_AUTOREDUCIBILITY_AUDIT.py` (exact integers and fractions, deterministic seed, about 1 s) performs 72,834 checks:
* **A.** Theorem A on finite frames (random causal frames and random bijections): autoreduction ⇒ separated families, the self-avoidance identity, family ⇒ search output, and the race form.
* **L1.** Larger-candidate soundness for increasing approximations below a non-dyadic real.
* **L2.** Check-by-check simulation of the canonical schedule at one hold against the closed-form window criterion, exercising α_h=0 (546 cases), landing (146) and no landing (508).
* **G.** The pairing/density dichotomy in causal frames: 1,078 forced-wrong and 50 forced-divergence cases.
* **M.** The Lemma M martingale.
* **F.** The Proposition F counting identity and bias formula for random balanced maps whose cells meet both sides.
* **E.** The tail-coded all-in example (β=1 for every window content).
* **S.** The §3.3 inequality.

It prints `ALL P4-S093 AUDITS PASS`. The audit supports finite identities and inequalities only. Theorem A's infinitary content, Lemma G's genericity, Lemma M's meagerness, L3(b) and every claim about infinite sources rest on the written proofs.

Frozen audits were re-run on the incoming tree: S092 (103,286 checks), S091, S090 and S089 PASS (see the close record).

## 3. Status discipline

* No class inclusion is added.
* No claim that R₂=MLR, MLR⊊R₂, GOL, ¬GOL, ASSCL, the left-c.e. window-skip property or Conjecture R holds.
* The new literature records (SRC-0073, SRC-0074) are ABSTRACT_INSPECTED calibration only and support no proof.
* R₂ versus OH^iso, U(H), X∈OH and fixed-S preservation are untouched.
* Original Y/M/H/X, PA-0001 and DEF-0020 are unchanged.
* Gate 3 PASS, Gate 4 NOT REVIEWED, Phase 4 OPEN, Phase 5 CLOSED.
