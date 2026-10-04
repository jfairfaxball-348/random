# P3-S003 — CAND-03 primary-source prior-art attack

Date: 2026-10-04  
Session: `P3-S003`  
Incoming checkpoint: `ac2ff8cdba4783b8c5f06ee84588766ed8c27a22`  
Scope: Phase 3 — Novelty / Prior Art; CAND-03 only  
Disposition: **EQUIVALENT / REBRANDED AT THE DEFINITION LEVEL**

## Authority and boundary

Live `main` matched the expected incoming checkpoint exactly before substantive work. Repository search found no committed P3-S003 record, so the session identifier was unique.

Gate 1 and Gate 2 remain **PASS**. Phases 1–2 are completed for gate purposes. Phase 3 is **OPEN**. Gate 3 is not reviewed and Phase 4 remains closed. No final candidate is selected and Fairfax-Ball Randomness is not defined.

This session performs one bounded primary-source prior-art attack on CAND-03 only. It does not prove a theorem, construct a witness, run an experiment, use Lean/Palomar, investigate CAND-01 or CAND-02, select a final candidate, review Gate 3, begin Phase 4, prepare publication material or contact third parties.

## Exact target retained

CAND-03 fixes an oracle (A) and asks for
`L_u = {A : for every X in CR, X is UCR^A}`,
where `UCR^A` is DEF-0025 uniformly relative computable randomness. A permitted uniform martingale family is coded by one total computable procedure over the full oracle space, and every oracle instance must be a valid martingale. A procedure total or valid only at the chosen oracle is excluded.

The target is universal lowness over **all unrelativized computably random inputs**. It is not THM-0024's pairwise join condition and not an existential base condition.

## Primary prior art inspected

### SRC-0064 — Kihara and Miyabe, *Unified characterizations of lowness properties via Kolmogorov complexity*

This source is decisive at the definition level. It defines a uniform test for a randomness notion (mathcal C) as a **total computable procedure** which, at every oracle, produces a valid (mathcal C)-test. It then defines `Low^star(C,D)` to be the oracles (A) such that every (mathcal C)-random is (mathcal D)-random **uniformly relative to (A)**.

Taking (mathcal C=mathcal D=CR), with the uniformly relative computable-randomness component supplied by SRC-0032 / DEF-0025, yields exactly CAND-03's (L_u). The universal quantifier, fixed oracle, and global total/all-oracle-valid uniform-family convention all line up.

The inspected SRC-0064 statement gives explicit characterization results for other Low-star pairs, including `Low^star(MLR,SR)` and `Low^star(SR,WR)`. No inspected statement in this bounded attack gives an intrinsic characterization of the specific `Low^star(CR,CR)` instance. That narrower characterization question therefore remains unresolved under the inspected evidence.

### SRC-0032 — Miyabe and Rute

DEF-0025 supplies the exact computable-randomness realization of the uniform-test convention: one total computable family over all oracle instances, every instance a martingale. THM-0024 remains a symmetric pairwise join theorem and THM-0025 an existential pairwise ordinary/uniform separation. They support the convention match but do not substitute for the universal Low-star definition.

### SRC-0009 — Nies

Theorem 5.7, promoted here as THM-0075, gives the contrasting ordinary-relativization result: every oracle low for ordinary computable randomness is computable, hence ordinary low-for-CR oracles are exactly the computable ones.

This does **not** settle `Low^star(CR,CR)`. Ordinary oracle-computable martingales and globally total uniform families are different resource conventions, and no reduction between the corresponding lowness classes is inferred.

### SRC-0010 — Hirschfeldt, Nies and Stephan

Retained only for the universal-lowness versus existential-baseness guard. Its base-for-randomness syntax is existential and cannot replace CAND-03's universal quantifier.

## Alternate terminology searched

Searches included `low for uniformly computable randomness`, `uniform lowness computable randomness`, `Low star computable randomness`, `Low^star(C,D)`, `truth-table reducible randomness lowness`, `truth-table computable randomness low`, `uniform relativization lowness`, `uniform test lowness`, and `computable randomness low oracle uniform martingale`.

The material terminology resolution is that pairwise uniformly relative computable randomness has appeared under **truth-table reducible randomness**, while universal uniform lowness is explicitly parameterized by **Low-star** notation. Searching only the pairwise terminology would miss the exact universal prior-art schema.

## Quantifier / convention matrix

| Item | Random-input quantifier | Oracle/test convention | Kind of statement | Consequence |
|---|---|---|---|---|
| **CAND-03** | every unrelativized (X\in CR) | DEF-0025 total all-oracle-valid martingale family; fixed A | universal lowness | target |
| **SRC-0064 / DEF-0065** | every C-random | total uniform procedure valid at every oracle; fixed A | parameterized universal lowness Low-star(C,D) | **exact definition-level schema match at C=D=CR** |
| **SRC-0032 / THM-0024** | one fixed pair | DEF-0025 | symmetric pairwise join equivalence | not a lowness theorem |
| **SRC-0032 / THM-0025** | existential pair | ordinary vs uniform | pairwise separation | not universal preservation |
| **SRC-0009 / THM-0075** | every CR input | ordinary A-computable martingales | ordinary lowness characterization | resource convention differs |
| **SRC-0010 / DEF-0009** | existential random witness | ordinary relative ML randomness | baseness | quantifier differs |

## Prior-art classification

**Disposition: EQUIVALENT_OR_REBRANDED at the definition level.**

- **Already known:** yes in the precise sense that the parameterized prior-art class `Low^star(C,D)` already contains CAND-03 as the (CR,CR) instance.
- **Equivalent/rebranded:** yes. CAND-03's exact oracle-class formula is a relabelling/instantiation of the Low-star schema once DEF-0025 fixes uniform computable relativization.
- **Materially distinct:** no at the definition level under the inspected evidence. Its claimed structural distinction—universal lowness with globally total uniform families—is precisely what the Low-star framework records.
- **Unresolved remainder:** the specific intrinsic characterization of `Low^star(CR,CR)` was not located in the inspected primary statements. This session does not infer that problem is open from search absence.

Accordingly CAND-03 is **retired as a candidate for a new named notion**. This does not assert that studying or characterizing `Low^star(CR,CR)` lacks mathematical interest.

## Durable consequence

CAND-03 moves from `RETAIN_PROVISIONAL` to `REJECT_PRIOR_ART_REBRANDING`. Its exact formula and P2-S004 E3 alignment are unchanged; the change is literature classification, not mathematics.

SRC-0064 and DEF-0065 are added to record the decisive Low-star framework. THM-0075 promotes the already statement-inspected ordinary-CR lowness contrast from SRC-0009 so that the ordinary/uniform guard is machine-searchable.

CAND-01 and CAND-02 are untouched and retain their P3-S001/P3-S002 dispositions. DEF-0020 and all existing convention/evidence guards are preserved.

No openness claim, original theorem, witness, experiment, final candidate selection, Gate-3 review or Phase-4 action occurs in this session.
