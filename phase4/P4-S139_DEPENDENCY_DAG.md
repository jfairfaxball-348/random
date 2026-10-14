# P4-S139 — shortest sufficient chains, forks, barriers

## DAG of logical sufficiency (edges not conjectured equivalences)
```text
                                      [R3 subset R2: DEFINITIONS]
                                                 |
                  +------------------------------+-----------------------------+
                  |                                                            |
   EQUALITY: prove R2 subset R3                                   STRICTNESS: prove R2 not subset R3
                  |                                                            |
          +-------+-------+----------------+                      +-------------+-----------------+
          |               |                |                      |             |                 |
  E-01 direct     E-05 all F3          E-07 R2=MLR             S-01 global     S-02 output    S-03 universal
  source/sim      factor via F2             |                   legal F3         rational d      R2 for SAME x
     |           AND E-06 closure       MLR -> R3                \             /                /
 E-02/E-04        required              implies equality           \          /                /
 optional scaffolding                                              S-04 jointly compatible x,G,d
          |                                                                   |
  E-08 direct tests                                                x in R2\R3  (one object)
          |
  every F3,d bad x in R2 gets F2,e winning ON x  -> contradiction
```
The logical DAG has two alternative proof endings. **E-01 is SUFFICIENT, not asserted logically necessary**; a non-uniform contradiction might avoid a compiler. **E-05 without E-06 is invalid.** Separation S-01/02/03/04 all necessary in the operational certificate.

## Restricted-class dependency map (must not float free)
```text
total G + fair all cylinders + cap3 ALL output fibres
    |
    +-- additive c=2 and bad output degree=3
    |    +-- S129 one-surplus (2^2-1) + normalized fair F2 detector
    |         -> NO x in R2 on that bad output
    |
    +-- G is conull singleton
    |    +-- finite clopen compatibility + unique inverse -> partial effective inverse
    |    +-- check Rute E-ISO (E-10) -> likely qualitative CR firewall
    |    +-- S138 provides independent explicit-rate compiler for ONE such G
    |
    +-- globally clopen 3 onto injective sheets with c=2
    |    +-- S131/S133 chart CR firewall; S132/S133 half-mass tag factor
    |         -> no CR-destroyer in this architecture
    |
    +-- positive-measure multi-degree / non-clopen / arbitrary-use
         +-- E-02/E-03/E-04 or E-08 OR separator S-09
         +-- all-output degree/price tests unresolved
```
**Shared choke points:** global fair/actual fibre legality and SAME-source rational martingales matter to BOTH sides. **Independent escape:** equality via R₂=MLR may bypass chart/factorization altogether; strictness via coupled forcing may bypass universal normal forms. A finite sanity table is not a graph edge to an infinite theorem.

## Why S129/S138 do not concatenate into universal equality
S129 only handles c2 at a **degree-three BAD output**; S138 only handles **one specified conull-singleton G** (entire CR, any output d), not every cap-three map. There is no theorem that any arbitrary G∈F₃ is reducible to these two cases. The degree-two c2 case and arbitrary-use positive multidegree remain genuine holes. E-10 may eliminate the **conull singleton** family broadly, but cannot fill positive-measure multidegree.

## Structural stopping distinctions
1. A local two-prefix candidate bound is an INPUT approximation, not a computable inverse list.
2. A finite output-row balanced 4-cell diagram proves neither a full three-path cap nor fairness on all other outputs.
3. The density of a null exceptional degree locus has no implication of positive measure or positive probability for CR inputs.
4. A Borel inverse partition can have uncomputable sheet masses; finite dyadic prices need not converge effectively.
5. A rational bounded-stopped output test may yield only a computable-real source measure; ordinary CR requires one total rational martingale.
6. Countable R₂ tests yield conull R₂ but cannot intersect an arbitrary null G-bad preimage class without a constructive intersection argument.

## Decision certificates
**Equality COMPLETE:** verified universal E-00 with arbitrary-use/global-fibre scope, or fully verified sufficient chain E-05+E-06, or E-07. **Separation COMPLETE:** legal algorithm and proofs for one G, one exact x∈R₂, one winning d on G(x), and same-source consistency. **Scoped theorem:** hypotheses and all exceptions explicitly declared; no R₂/R₃ headline. **Route dead:** concrete counterexample violating its proposed sufficient lemma or an inherited no-go applying to EVERY allowed member, not 'no search result'. **Prior art:** verify original source theorem/hypotheses before novelty or outside claims.

See [obligation IDs](P4-S139_OBLIGATIONS.md), [competitive triage](P4-S139_ROUTE_TRIAGE.md), [future agenda](P4-S139_RESEARCH_ROADMAP.md).