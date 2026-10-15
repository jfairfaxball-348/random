# Owner steer — finite-fibre randomness hierarchy and its limit (2026-10-15)

**Status: AUTHORISED ROADMAP/PROMPT CHANGE ONLY, NOT A MATHEMATICS SESSION.** Last completed P4-S166; next P4-S167 FUTURE UNEXECUTED. The preceding S166 closeout contains the then-current S167 proposal and remains immutable as historical provenance. This document and the live authoritative/NEXT_SESSION_PROMPT.md supersede only that unexecuted proposal; they do not alter historical proof results. No Gate4, Phase5, Lean, Palomar or publication.

## Framework and established notation

Work in Cantor space 2^ω with fair coin λ. F_k consists of **total computable globally λ-preserving maps** G:2^ω→2^ω having **at most k actual complete infinite inverse sequences for every output**. R_k is the set of x∈CR for which G(x)∈CR for every G∈F_k. Crucially: no common computable use bound, no surreptitious "almost everywhere" cap and no finite-prefix approximation to actual fibre cardinality. As fixed in P4-S127, R_fin := ⋂_{k≥1} R_k. Notation R_ω^ub may be a descriptive alias, not a competing definition.

Existing framework: MLR ⊆ R_fin ⊆ … ⊆ R_3 ⊆ R_2 ⊊ R_1=CR. These are the known inclusions and established k=2/CR separation, **not** claims of properness at higher levels. Earlier work discusses all total fair observers and MLR; keep any inherited theorem and evidence grade unchanged.

## Priority order: one primary attack and retained research obligations

**H1 — PRIMARY P4-S167: finite-limit collapse, R_fin ?= MLR.**
Prove or disprove the quantified assertion:
For every x∈CR\MLR, there exist a *single finite integer k depending on x*, a total computable globally fair G with |G⁻¹(y)|≤k for **all outputs y**, and a total computable exact nonnegative rational output martingale d successful on G(x).
The reverse inclusion MLR⊆R_fin is already part of the baseline. A negative answer demands a **single same-source** x∈CR\MLR satisfying ∀k∀G∈F_k, G(x)∈CR. Producing one x_k per k is not enough. Seek a proof, a counterexample, or a genuine general-k reduction/barrier; do not dilute the primary effort into a survey.

**H2 — universal finite threshold, secondary:** Is there a fixed K≥2 with R_K=MLR? If so all later classes equal MLR. Failure of every finite threshold does not determine H1: intersection may still be MLR. Target a least K or prove no K exists, without a forbidden exchange ∀k∃x_k ⇒ ∃x∀k.

**H3 — strictness at every finite level, secondary:** For each k≥2 is R_(k+1) ⊊ R_k? Each separation requires a *single* x∈R_k and a globally fair total F_(k+1) observer G with G(x)∉CR; nonfactorability or presence of k+1 inverse branches alone cannot prove strictness. Infinite strictness rules out H2, but need not decide H1.

**H4 — fibre-geometry boundary, secondary:** Compare family F_pf of all total fair computable maps each of whose fibres is finite, with NO globally uniform cardinal bound, F_ub=⋃_{k≥1}F_k, F_count with all fibres at most countable, and F_all with no restriction. Distinguish observer-family inclusion from randomness-class separation. Define R_pf, R_count by universal preservation of CR, and investigate:
MLR ⊆ R_count ⊆ R_pf ⊆ R_fin; whether any inclusion is proper is unproved here. R_fin uses uniform bounded k per map, not pointwise-finite maps.
Concrete all-output fair continuous sanity witness for F_pf\F_ub: partition [1^n0] (n≥0), on each cylinder delete the next n bits after 1^n0, and fix 1^ω. Fibre size on [1^n0] is 2^n; singleton at 1^ω. Prove computability at boundary, full λ-preservation and exact all-output fibres before using. This map alone is NOT a randomness-class separator.

**H5 — arithmetic and modular programmes, exploratory only:** Explore exact-prime or prime-bounded fibre strata, prime/composite factorisation and modular cardinality restrictions (e.g. all *finite* output-fibre sizes ≡r mod m), with well-formed all-output definitions. The elementary composition bound F_a∘F_b ⊆ F_(ab) does NOT imply a factorisation theorem, and prime factorisation of integer cardinalities does NOT imply factorisation of globally fair computable maps. R_π has NO approved mathematical definition yet: distinguish prime-indexed levels {R_p:p prime} from a prospective π(n) prefix-resolution growth constraint, whose choice of resolution/invariant must first be canonical and distinguish finite-stage compatible cells from genuine inverse paths. R_mod is similarly a family of *proposals*, not a theorem or silently established class. Never claim plain computable coordinate permutations induce a new CR class.

## Logic / scorecard

Three mutually exclusive coarse global outcomes should remain visible:
(I) ∃K≥2 with R_K=MLR;
(II) R_fin=MLR but ∀k R_k≠MLR;
(III) R_fin\MLR≠∅.
These exhaust possibilities given MLR⊆R_fin, though they do NOT resolve adjacent-level strictness. Cases (I)/(II) together are H1 positive; case (III) is H1 negative. An observer F_pf\F_ub does not establish R_pf⊊R_fin. A nonCR image of x∈CR does not imply x∈R_fin.

## Prior-work retention and safety gates

Do NOT replace or weaken existing S011, S101–S103, S117, S127, S135, S141, S155–S166, including the exact S165 fair F3 map and the S166 B-source nonCR martingale. For S165/S011 candidate, B is nonCR and A source remains UNKNOWN; R2=R3, R2=MLR, E-08/E-00/S-00 remain OPEN. This previous priority is retained as a named future branch, but NOT S167's headline.

Proof before formalisation before publication. Every theorem requires exact universal quantifiers on each source/observer/output; distinguish internal mathematics from external independent verification, hosted CI, local sanity, and novelty. Preserve frozen Y/M/H/X, DEF-0020, PA-0001, Gate3 PASS, Gate4 NOT REVIEWED, Phase4 OPEN, Phase5 CLOSED.

**The next owner instruction "Run next session" authorises execution of S167 as installed in authoritative/NEXT_SESSION_PROMPT.md.** This owner-steer commit itself performs NO S167 research and must leave S168 unprepared until S167 closes.
