# P4-S012 validation

Date: 2026-10-06
Incoming baseline: 491c671be615abd9bef9b3e9239ccdb74b76b22b
Core mathematics commit checked: ce963d501d0162b52570a0cc1bd8a702e3bdcb8e

Result: **PASS** for uniqueness, k=2 scope discipline, sufficient partial-predictor/stake conversion, scan-converse construction, authority synchronization and preserved scope guards.

## Repository and scope checks

- live main matched the requested incoming baseline before substantive work;
- the incoming phase4 directory contained P4-S001 through P4-S011 and no P4-S012 mathematics/close/validation record, so P4-S012 was unique;
- Phase 4 was OPEN for selected CAND-01 and Phase 5 CLOSED;
- P4-S001 through P4-S011 were read and not edited;
- P4-S005 through P4-S011 were treated as settled;
- the incoming-baseline comparison after the core commit changes only P4-S012 records and current programme authority/index/summary files;
- no P4-S001 through P4-S011 record appears in the changed-file set;
- phase3/prior-art.json is unchanged and PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE;
- catalog/definitions.json is unchanged, so DEF-0020 is preserved;
- P4-S011's exact k=2 destroyer is preserved;
- no k>2, novelty, Gate-4, publication or outreach claim is made.

## Sufficient-hypothesis checks

1. Sentinel-local partial prediction.
   - The least-fresh scan withholds the current sentinel and otherwise emits one fresh filler coordinate at every stage until a finite self-avoiding prediction computation becomes visible.
   - A nontriggering epoch therefore remains total and eventually queries every coordinate except its sentinel.
   - If every epoch triggers, each least-unqueried sentinel is consumed and every coordinate is eventually queried.
   - Hence every fibre has size at most two, exactly as in P4-S011.
   - Fresh-coordinate induction gives fair-coin preservation independently of trigger probabilities.

2. Weakening of P4-S011.
   - The scan conversion needs no computable wtt use bound.
   - Predictions at filler coordinates are not used.
   - A target-total self-avoiding Turing autoreduction is sufficient because each target computation is finite and persistent fillers eventually reveal all oracle answers it uses.
   - P4-S012 makes no strict separation claim between wtt autoreducibility, target-total autoreducibility and the weaker sentinel-local property.

3. Fractional stake generalization.
   - At a visible rational stake theta in [-1,1] and capital C, the output children C(1-theta) and C(1+theta) are nonnegative and average to C.
   - Therefore the resulting output strategy is a computable fair martingale.
   - If the target stake capital is unbounded, the same least-fresh global-k=2 scan destroys computable randomness on that target.
   - The all-correct bit predictor of P4-S011 is the all-in special case theta in {-1,+1}.

## Converse checks

Let T be a global-k=2 adaptive no-repeat scan, x a computably random source, and d a rational-valued computable martingale succeeding on F_T(x).

1. Singletonhood.
   - P4-S008 is used as settled authority: a computably random winning source cannot omit any fixed coordinate.
   - Therefore T eventually queries every coordinate on x and the winning fibre is singleton.

2. Self-avoiding functional.
   - On input j, simulate T from the empty transcript and answer every requested coordinate k different from j from the oracle.
   - Stop before T queries j.
   - This computation never queries j and halts on x for every j.

3. Exact signed stake.
   - With C=d(tau), C_0=d(tau0), C_1=d(tau1), nonnegativity and the martingale equation give C=(C_0+C_1)/2.
   - For C>0, theta=(C_1-C_0)/(2C) lies in [-1,1].
   - Then C(1-theta)=C_0 and C(1+theta)=C_1.
   - If C=0, nonnegativity forces both children to be zero, so defining theta=0 is harmless.
   - Rational-valued martingales suffice for computable randomness by DEF-0004, so the stake is computable and rational.
   - In T's original query order, these stakes reproduce d exactly and are therefore unbounded.

4. Bit-prediction boundary.
   - If only finitely many nonzero favoured wagers were correct, then after the last such success every nonzero wager would strictly decrease capital and zero wagers would leave it fixed; capital could not become unbounded.
   - Hence infinitely many favoured-bit wagers are correct.
   - If |theta|=1 and the wager is wrong, capital becomes zero; a nonnegative martingale stays zero thereafter. Thus every all-in wager on a succeeding path is correct.
   - Arbitrary success does not force all favoured predictions to be correct. The recorded half-capital example has factors 3/2,3/2,1/2 on the repeating block 001, hence net factor 9/8 per block while being wrong on every 1.
   - That arithmetic example is explicitly not represented as a computably random source or a k=2 witness.
   - The induced stake functional is only proved to reproduce success in the original scan order; no reordering theorem or all-correct bit-autoreduction converse is claimed.

## Synchronization checks

- authoritative/STATE.json parses, records P4-S012 as last completed, P4-S013 as next, Phase 4 OPEN and no active blocker;
- phase2/candidates.json parses, records the P4-S012 stake-level structural boundary for CAND-01 and names P4-S013 next;
- authoritative/SESSION_LEDGER.md records P4-S012, D-0034 and FL-060 are present in the decision/failure ledgers;
- README.md, ROADMAP.md, AGENTS.md, authoritative/START_HERE.md and phase4/README.md are synchronized to the P4-S012 structural result;
- authoritative/NEXT_SESSION_PROMPT.md contains a bounded runnable P4-S013 prompt restricted to the sibling-totality question;
- PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE and DEF-0020 is unchanged;
- no owner/external blocker exists.

This is manual mathematical/bookkeeping validation, not proof-assistant verification and not a novelty theorem.

Final remote main is verified after this validation commit, and the exact outgoing hash is reported in the session response.
