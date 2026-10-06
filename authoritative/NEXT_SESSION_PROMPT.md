# Next Session Prompt — P4-S032

Continue the Fairfax-Ball Randomness Research Programme in https://github.com/jfairfaxball-348/random.

Run only Phase 4 — Mathematics session P4-S032. Treat committed repository state as authoritative. Pin live main at the exact post-P4-S031 pivot checkpoint reported by the preceding session, reconcile any mismatch, confirm P4-S032 is unique, and read P4-S001 through P4-S031, the required CAND-01 authority, and phase4/P4_RESEARCH_PIVOT_AFTER_S031.md.

## Sustained Phase-4 pivot

This session begins a sustained research pivot. Freeze all validated mathematics through P4-S031. Do not reopen or continue tightening the P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence merely because a local next lemma remains available. That machinery remains available only when it serves a deeper theorem.

The organising question is:

**What mathematical resource is exposed by the jump from injective observation to one binary degree of inverse ambiguity, and what else does that resource control?**

The previous session-local "strictly k=2" restriction is no longer the default: k=1 and k=2 remain the base phenomenon, but finite k>2, composition or factorisation may be used when the new questions genuinely require them. Do not broaden into an unfocused survey.

## P4-S032 task — reconnaissance and theorem selection

P4-S032 is not expected to settle the whole new programme. Its job is to perform mathematically disciplined reconnaissance across the new axes, prove enough exact lemmas/constructions/obstructions to distinguish promising routes from superficial ones, and select the strongest next theorem target for sustained multi-session work.

Start by formalising

R_k = {x in CR : F(x) remains computably random for every total computable fair-coin-preserving F with fibre size at most k},

and

R_fin = intersection over all finite k of R_k.

Record only the immediate consequences already forced by settled mathematics:

- P4-S001 gives R_1 = CR.
- P4-S011 gives a computably random source outside R_2, hence R_2 is a proper subclass of CR.
- R_{k+1} subseteq R_k is immediate from the map classes.

These are internal consequences, not novelty claims.

Then perform exact reconnaissance across several of the following axes, choosing the ones that can be tested most sharply in one session:

1. **Robustness hierarchy / source characterization:** test whether R_2,R_3,... form a strict hierarchy or collapse, whether R_2 robustness could imply all-finite robustness, and whether vulnerability under k=2 is tied to partial self-avoiding predictability/autoreducibility.
2. **Structural in-between threshold:** test natural subclasses strictly between injective and bare two-to-one maps — e.g. finitely many double fibres, ambiguity on null/effectively null sets, exactly-two-to-one a.e. behaviour, effective/partial inverse selectors, computably distinguishable branches, bounded ambiguity-resolution delay, finite dependency frontiers, local effective invertibility, branch-weight lower bounds, vanishing second-branch weights, one global unresolved bit versus renewable ambiguity — seeking a preservation/failure threshold theorem rather than another isolated example.
3. **Reverse direction / randomness creation:** test whether a finite-to-one fair-coin-preserving map can send an individually non-computably-random source to a computably random output, and whether this cleanly separates conservation from creation/no-randomness-from-nothing behaviour.
4. **Composition/factorisation / ambiguity budget:** test whether binary-ambiguity stages factor finite multiplicity in an effective way, whether robustness under all binary stages could imply robustness under arbitrary finite k, whether composing k=2 stages is equivalent to or stronger than one static k=4 map, and whether repeated temporal ambiguity is more important than raw fibre cardinality.
5. **Cross-randomness comparison:** probe one or two carefully chosen other randomness notions only where a sharp theorem is realistically available; candidates include Martin-Löf, Schnorr, Kurtz, Church-stochastic/computable-selection, nonmonotonic/Kolmogorov-Loveland-style notions, or effective dimension. Do not conduct an encyclopaedic survey.
6. **Machine mutations:** use the P4-S011 design pattern to test structurally important variants — especially exceptional sources on double fibres, exactly-two-to-one maps, recurrent/migratory/symmetric ambiguity, extra regularity or shift-like structure, sparse or arbitrarily weak prediction advantage, interacting sentinels under a small fibre bound, or renewed ambiguity — while explicitly tracking totality, fair-coin preservation, fibre bound, source randomness, output randomness and effective inverse information.
7. **Actual resource / invariant:** directly compare candidate explanations suggested by settled work: hidden inverse information, sibling partiality, self-avoiding prediction, nonuniform inverse selection, delayed revelation, unresolved binary choices, renewable ambiguity, and failure to aggregate branchwise betting advantages into one source martingale. Seek a criterion explaining both k=1 safety and k=2 failure.
8. **Converses:** test whether a natural subclass of k=2 destroyers necessarily induces partial self-avoiding prediction/stake structure, autoreduction, or a related source-side mechanism on the vulnerable computably random source.

You do not need to advance every axis. Prefer 3–4 serious mathematical probes with exact statements over shallow coverage of all directions.

## Selection requirement

By the end of P4-S032, choose the strongest next theorem target based on mathematical depth, explanatory power, tractability and ability to organise multiple subsequent sessions.

The selected target should ideally do at least one of the following:

- characterize vulnerability/robustness on the source side;
- identify a structural preservation threshold strictly between k=1 and bare k=2;
- establish a composition/factorisation principle or obstruction;
- reveal a genuine asymmetry between randomness destruction and randomness creation;
- show that the one-bit ambiguity mechanism has a sharp analogue or sharp failure for another randomness notion;
- isolate an invariant deeper than raw fibre cardinality.

Record why the selected target outranks the other tested routes, and give a bounded multi-session research plan without claiming it will succeed.

Do not automatically select the smallest unresolved technical lemma.

## Guards

Preserve P4-S005 through P4-S031 as settled, including P4-S011 and P4-S015 through P4-S031.

Preserve PA-0001 as **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and preserve DEF-0020 unchanged.

Make no novelty, openness, Gate-4, publication or outreach claim. Do not start prior-art work. Continue original mathematics only.

Record, validate and synchronize useful work, commit it, verify remote main, report the exact outgoing hash, and provide the next prompt aligned with the theorem target selected by this sustained pivot if no blocker exists.
