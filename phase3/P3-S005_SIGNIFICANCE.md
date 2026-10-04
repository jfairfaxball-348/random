# P3-S005 — CAND-02 significance/usefulness and interested-community assessment

Date: 2026-10-04  
Session: `P3-S005`  
Incoming checkpoint: `af2c2986b1528ac65b18c381ebbeac870533f078`  
Scope: Phase 3 — Novelty / Prior Art; CAND-02 only  
Disposition: **PROVISIONALLY SUBSTANTIVE — CONTINUE PHASE-3 INVESTMENT WITH ELEVATED TECHNICAL-SLICE RISK**

## Authority and boundary

Live `main` matched the expected incoming checkpoint exactly before substantive work. The incoming session ledger contained no `P3-S005` heading and no committed `P3-S005_SIGNIFICANCE.md` existed; the sole incoming mention was the forward recommendation. P3-S005 was therefore unique.

Gate 1 and Gate 2 remain **PASS**. Phases 1–2 are completed for gate purposes. Phase 3 remains **OPEN**. Gate 3 is not reviewed and Phase 4 remains closed. No final candidate is selected and Fairfax-Ball Randomness is not defined.

This session assesses significance, usefulness and plausible interested communities only. It does not prove a theorem, construct a witness, run an experiment, use Lean/Palomar, investigate CAND-01 or retired CAND-03, select a candidate, review Gate 3, begin Phase 4, prepare publication material or contact third parties.

## Exact CAND-02 target unchanged

On fair-coin Cantor space, `B_open(x)` requires that for every **everywhere-total computable fair-coin-preserving Cantor self-map** `T` and every **effectively open** set `U`, the averages

\[
\frac1N\sum_{i<N}\mathbf 1_U(T^i(x))
\]

converge.

There is **no ergodicity assumption**, **no equality-to-expectation clause**, **no computability requirement on \(\lambda(U)\)** and **no convergence modulus or rate**.

The P3-S002 novelty/prior-art disposition remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. Nothing in P3-S005 upgrades that status.

## Is the formulation mathematically substantive?

**Assessment: provisionally yes as an effective-observation/dynamics boundary, but with materially higher technical-slicing risk than a formulation whose live hypothesis is already known to be structural in adjacent mathematics.**

Three parts of the formulation have independent mathematical motivation in the inspected primary literature.

First, **nonergodic convergence-only semantics are not an arbitrary weakening invented for the candidate**. SRC-0058 / DEF-0059 explicitly distinguish weak Birkhoff points, where averages merely converge, from Birkhoff points, where the limit is also the integral, and state that weak Birkhoff is the appropriate notion in the nonergodic case. Thus dropping equality-to-expectation is mathematically forced by the nonergodic setting rather than a cosmetic relaxation.

Second, **enumerable/effectively-open observations sit on a recognized effectiveness axis**. SRC-0058 separates computable observables from lower-semicomputable observables, and SRC-0062 explicitly studies effectivizations in which analytic objects are described by c.e. data such as lower-semicomputable functions. An effectively open indicator is the bounded event-level special case: membership has positive semidecidable information while the observable remains bounded, so unbounded-tail issues are not being used to manufacture difficulty. This gives the candidate a natural “frequency of positively recognizable events” interpretation.

Third, **everywhere-total computable dynamics are a legitimate effective-dynamics regime**, not a syntactically impossible corner. SRC-0063 uses total computable Cantor maps inside computable ergodic group actions and proves effective Birkhoff results for effectively open/lower-semicomputable observables. However, this is also the candidate's principal significance risk: SRC-0058 and SRC-0062 formulate the closest nonergodic results with a.e./possibly partial operators, and their constructions exploit that measure-theoretic convention. The present evidence does not show that restricting to total maps changes the randomness content rather than merely excluding known witness representations.

Accordingly, the exact three-way intersection is **not yet established as a new mathematical boundary**. It is worth continued Phase-3 investment because it isolates a natural event-frequency question at the interface of two independently meaningful effectivity axes, but a future result must show that totality and effectively-open observability have explanatory force together. If the exact predicate collapses by a routine totalization or observable-reduction argument, the significance case weakens sharply even if the formulation remains syntactically unmatched in the prior-art audit.

## What would make CAND-02 useful?

A useful outcome should explain why semidecidable event frequencies under total computable dynamics require exactly the randomness strength they do.

1. **Exact characterization of `B_open`.** A two-sided theorem locating the exact predicate among established randomness notions, or a sharp separation if it defines a genuinely different class. A one-way sufficiency statement alone would not justify a new notion.
2. **Totality mechanism or collapse theorem.** Explain whether the restriction from a.e./partial computable measure-preserving transformations to everywhere-total self-maps changes the pointwise randomness requirement. Either a structural separation or a principled totalization equivalence would be informative; an accidental representation artifact would be a significance falsifier.
3. **Observable-boundary theorem.** Compare effectively-open indicators with computable observables and bounded/lower-semicomputable observables under the same total-map convention. The candidate becomes more useful if the event class is shown to be a natural minimal complete family, or if its precise loss of strength is characterized.
4. **Operational dynamics consequence.** Translate the characterization into a clean statement about limiting frequencies of positively recognizable events in natural total computable systems, preferably with nontrivial nonergodic examples where the limiting value need not be the global expectation.
5. **Placement and sharpness.** Relate the resulting class exactly to Martin-Löf, Schnorr, weak-2 and Oberwolfach randomness only as supported by proved implications/equivalences/separations. No such placement is presumed here.
6. **Rates or moduli only if independently natural.** CAND-02 deliberately asks for convergence only. Quantitative convergence should not be imported merely to inflate a theorem package; it would count as additional value only if the exact mathematics naturally yields it.

A result that merely says “the Franklin–Towsner theorem still works after a routine change of representation,” or that reduces effectively-open indicators to an already settled observable class without revealing a new boundary, would substantially weaken the case for continued programme investment.

## Plausibly interested communities

- **Algorithmic randomness and computability:** the core audience, because the target asks for an exact randomness characterization through orbit-frequency convergence.
- **Effective ergodic theory / computable dynamical systems:** directly relevant because the formulation isolates map totality, nonergodicity and observable effectivity as separate resources.
- **Computable analysis / effective probability:** plausibly interested because a.e.-computable versus everywhere-total operators and lower-semicomputable/event observables are standard representation/effectivity distinctions.
- **Classical ergodic theory:** plausibly interested only if a future result connects the effective restriction to natural total nonergodic systems or a structural totalization obstruction rather than to coding details of one computability representation.

These are plausibility judgments, not claims of community endorsement, priority or likely publication.

## Primary-source significance support

No new catalogue source is required for this assessment. The significance claims use already statement-inspected primary anchors and a bounded recheck of their current primary-source pages:

- **SRC-0058 — Franklin–Towsner:** weak Birkhoff is the nonergodic convergence-only notion; computable versus lower-semicomputable observables are treated as distinct complexity regimes; their converse machinery uses the source's a.e.-defined transformation convention.
- **SRC-0062 — Miyabe–Nies–Zhang:** effective almost-everywhere theorems with c.e.-described objects, including lower-semicomputable observables and Birkhoff convergence, form a recognized route to randomness notions stronger than basic Martin-Löf randomness; the recorded Birkhoff operator is explicitly not assumed total.
- **SRC-0063 — Moriakov:** total computable Cantor maps and effectively-open/lower-semicomputable observables occur in a genuine effective-dynamics framework, though with ergodicity, automorphism-group structure and Følner averaging.
- **SRC-0057 / SRC-0012:** retained as guards showing that equality-to-expectation and dynamical typicality belong to stronger ergodic/mixing settings and must not be silently imported into CAND-02.

The sources support the naturalness of the component axes. They do **not** establish that their exact intersection is novel, distinct, or theorem-worthy.

## Future theorem package required for continued investment

A Phase-4-worthy package would need substantially more than an unmatched hypothesis combination:

- a main exact characterization theorem for `B_open`, or a decisive collapse/retirement result;
- a theorem explaining the role of everywhere-totality relative to the a.e./partial transformation literature;
- an observable-boundary theorem comparing effectively-open indicators with computable and lower-semicomputable observables under matched map hypotheses;
- sharp placement/equivalence/separation against established randomness notions, without assuming the answer;
- natural total nonergodic examples or system classes demonstrating that the characterization has dynamical content beyond a coding artifact;
- optionally, an intrinsic test/robustness characterization or a quantitative consequence if the exact mathematics produces one naturally.

## Phase-3 significance disposition

**PROVISIONALLY SUBSTANTIVE — CONTINUE PHASE-3 INVESTMENT WITH ELEVATED TECHNICAL-SLICE RISK.**

The reason is not novelty. Nonergodic convergence-only semantics and c.e./lower-semicomputable observation complexity are established structural themes in the primary literature, and total computable Cantor dynamics are a legitimate effective regime. The weakness is that no inspected evidence yet shows the exact total-map restriction is more than a representation boundary, or that effectively-open indicators yield a characterization not already forced by nearby observable classes.

CAND-02 therefore remains **RETAIN_PROVISIONAL**. Its formula, E2 alignment and PA-0002 novelty classification are unchanged. No openness, mathematical distinctness, theorem, candidate-selection or Gate-3 claim is made.

DEF-0020 and all existing convention/evidence guards are preserved.
