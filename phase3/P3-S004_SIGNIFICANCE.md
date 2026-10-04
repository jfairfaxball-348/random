# P3-S004 — CAND-01 significance/usefulness and interested-community assessment

Date: 2026-10-04  
Session: `P3-S004`  
Incoming checkpoint: `1d5a9b63305f1b75700d55c709b3e10d66d18e88`  
Scope: Phase 3 — Novelty / Prior Art; CAND-01 only  
Disposition: **PROVISIONALLY SUBSTANTIVE — CONTINUE PHASE-3 INVESTMENT**

## Authority and boundary

Live `main` matched the expected incoming checkpoint exactly before substantive work, and no committed P3-S004 record existed. Gate 1 and Gate 2 remain **PASS**. Phase 3 remains **OPEN**. Gate 3 is not reviewed and Phase 4 remains closed. No final candidate is selected and Fairfax-Ball Randomness is not defined.

This session assesses significance, usefulness and plausible interested communities only. It does not prove preservation or failure, construct a witness, run an experiment, use Lean/Palomar, investigate CAND-02 or retired CAND-03, select a candidate, review Gate 3, begin Phase 4, prepare publication material or contact third parties.

## Exact CAND-01 target unchanged

For each fixed integer (k\ge 1), CAND-01 quantifies over everywhere-total computable fair-coin-preserving Cantor self-maps (F) satisfying the global set-theoretic bound

[
|F^{-1}(y)|\le k\qquad\text{for every }y\in 2^\omega.
]

No computable inverse branch, selector, fibre enumeration or inverse map is assumed. The question remains whether every computably random input has computably random image under every such map.

The P3-S001 novelty/prior-art disposition remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. Nothing in P3-S004 upgrades that status.

## Is the finite-fibre restriction substantive?

**Assessment: provisionally yes as a research axis, but not yet as an established randomness boundary.**

There are two independent reasons.

First, inside the existing algorithmic-randomness evidence, finite multiplicity is now the live structural discriminator. SRC-0061 / THM-0072 already eliminate everywhere-totality plus fair-coin preservation alone: such maps can destroy computable randomness. SRC-0015 / THM-0038 gives positive computable-randomness invariance when explicit a.e.-computable inverse data are available. CAND-01 asks whether a strictly weaker kind of control—bounded cardinal ambiguity with no effective inverse data—has explanatory force. That is a coherent boundary question rather than a mere restatement of either known regime.

Second, adjacent primary literature treats finite multiplicity as structural rather than decorative. SRC-0065 studies uniformly finite-to-one measure-preserving endomorphisms through entropy and conjugacy; its uniformly (p)-to-one notion adds entropy (log p), almost-everywhere (p)-to-one multiplicity and equal conditional preimage weights. SRC-0066 treats finite-to-one factor codes as a meaningful symbolic-dynamics constraint and explicitly places factor-code questions in an information-theoretic channel setting. These sources do **not** match CAND-01: they add substantial dynamical/shift structure and supply no computable-randomness theorem for the bare global cardinal bound.

Accordingly, the evidence supports the statement “bounded ambiguity is a recognized mathematical structural axis.” It does **not** support “bounded ambiguity preserves computable randomness,” “the CAND-01 distinction is novel,” or “the bare cardinal restriction is sufficient.”

## What would make CAND-01 useful?

A technically correct yes/no answer is not enough by itself. Continued investment should aim at consequences that explain the finite-ambiguity boundary.

1. **Exact preservation/failure result.** Determine the exact CAND-01 preservation question for globally (k)-to-one total fair-coin-preserving maps, ideally sharply enough to expose whether (k) matters.
2. **Mechanism or intrinsic characterization.** Explain how bounded ambiguity interacts with effective betting/tests without importing effective inverse branches by assumption.
3. **Boundary/sharpness theorem.** Relate the exact cardinal-fibre regime to the known explicit-inverse positive regime and unrestricted-total negative regime. If preservation fails even for small finite (k), identify the missing effective structure rather than stopping at a counterexample.
4. **A meaningful robustness class, if one exists.** If (R_{fin}) is proper, give an intrinsic characterization and informative comparisons with established randomness notions. If (R_{fin}=CR), the preservation theorem still needs an explanatory structural proof to carry significance.
5. **Information/dynamics consequences only when earned.** A quantitative information-loss bound, coding interpretation, or bridge to finite-to-one dynamics would materially strengthen usefulness, but no (O(\log k))-type bound or entropy/channel conclusion is assumed here.

A routine adaptation of an existing theorem, or a result in which the finite-fibre condition plays no essential explanatory role, would substantially weaken the case even if the result were correct.

## Plausibly interested communities

- **Algorithmic randomness and computability:** the core audience, because the question asks for stability of computable randomness under a sharply restricted effective observation class.
- **Computable analysis / effective probability:** a natural adjacent audience because the distinction among total maps, a.e.-computable morphisms and effective inverse information is central to the formulation.
- **Ergodic theory / symbolic dynamics:** plausibly interested only if a future theorem connects the bare effective finite-fibre question to established finite-to-one endomorphism or factor-code structure rather than borrowing terminology alone.
- **Information theory / algorithmic information:** plausibly interested only if the mathematics produces a genuine coding/channel or quantitative information-loss consequence. SRC-0066 supplies an adjacent bridge, not present evidence that CAND-01 itself is an information-theory result.

These are plausibility judgments about communities, not claims of community endorsement or anticipated publication interest.

## Future theorem package required for continued investment

A Phase-4-worthy package would need substantially more than “finite-to-one was the one hypothesis not searched before”:

- a main exact conservation theorem or sharp finite-multiplicity counterexample;
- a structural characterization/transfer principle explaining the role of bounded ambiguity;
- a sharp boundary result against explicit effective inverse/isomorphism assumptions and unrestricted total-map non-conservation;
- natural examples or subclasses that connect the Cantor-space formulation to recognizable finite-to-one dynamics;
- if a proper class (R_{fin}) arises, an intrinsic characterization and meaningful comparison theorem;
- optionally, a quantitative information/coding consequence, but only if established under the exact effective hypotheses.

## Phase-3 significance disposition

**PROVISIONALLY SUBSTANTIVE — CONTINUE PHASE-3 INVESTMENT.**

The reason is not novelty. It is that the surviving hypothesis lies on a recognized structural axis and marks a genuine gap between two different effective-resource regimes already present in the catalogue. The reason is also conditional: the current evidence does not show that bare finite cardinal fibres have any computable-randomness effect.

CAND-01 therefore remains **RETAIN_PROVISIONAL**. Its formula, E1 alignment and PA-0001 novelty classification are unchanged. No openness, mathematical distinctness, theorem, candidate-selection or Gate-3 claim is made.

DEF-0020 and all existing convention/evidence guards are preserved.
