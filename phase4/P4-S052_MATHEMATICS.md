# P4-S052 — certified escrow cash-out and the shielded-old turnover barrier

Date: 2026-10-08
Session: P4-S052
Incoming checkpoint: a157f51f8c57b851a2f4bc3d32696109255df51b
Scope: Phase 4 — Mathematics, selected CAND-01; one-hole normalization after coded recoding.

Result: **The P4-S051 two-target 4/3 escrow has an exact old-sentinel cash-out table. Two of its three surviving future outcomes positively orient the old bit and allow a further fair double (combined 8/3), while the third does not (combined 4/3 with zero-stake old release). On a P4-S049 shielded-old epoch, *all* positive square refutations involve the opposite of the actual future value; hence every executed opposed-row escrow ends in the unoriented outcome, and no finite wrong-output old-orientation certificate of the specified kinds exists. An explicit finite-window success-gated controller legally couples profits to old turnovers. Infinitely many executed profitable turnovers would show X not in OH, but no infinite timely capture theorem for committed X is proved.**

## 0. Authority and retained data

Remote main equalled the exact P4-S051 outgoing SHA \`a157f51f8c57b851a2f4bc3d32696109255df51b\` before this session; the three P4-S052 records did not exist. P4-S001–P4-S051 mathematics, selected CAND-01 authority, the P4-S031 research pivot and the later mathematics records were read, emphasizing P4-S008, P4-S011, P4-S012, P4-S027, P4-S041, P4-S044–P4-S051. All validated mathematics through P4-S051 is frozen.

Retain Y in CR with its syntactically self-avoiding globally use-clipped wtt autoreduction M, satisfying M^Y(n)=Y(n); P4-S033 repeated three-bit linear computable fair-coin homeomorphism H; and X=H^{-1}(Y) in CR with H(X)=Y not in OH. Retain
\[
MLR\subseteq R_2\subseteq OH^{iso}\subseteq OH\subsetneq CR.
\]
The questions X in OH and R_2=OH remain unresolved.

A finite positive \`Ref_{s,t}(a,beta)\` is a wrong/nonbinary halt of a tested M-equation under the raw counterfactual s=a,t=beta, with all other accessed raw coordinates taken from the observed source, and is a sound exclusion of that pair on X. The simulator never treats silence, timeouts or divergence as a refutation.

## 1. The exact combined future/old cash-out theorem

Fix distinct unread raw coordinates s,t,u, the future t/u belonging to different fresh recoding blocks from each other and from the old s. Suppose that before either future coordinate was consumed a positive symmetric simulation found
\[
E_1=\mathrm{Ref}_{s,t}(a,\beta),\qquad E_2=\mathrm{Ref}_{s,u}(1-a,\gamma).
\]
By P4-S051 the future tuple (t,u)=(beta,gamma) is excluded. Starting from capital C, its fair future-only hedge queries t with child capitals 2C/3 for beta and 4C/3 for 1-beta, then queries u with (0,4C/3) for (gamma,1-gamma) if t=beta and zero stake otherwise. Its final capital on each possible future tuple is 4C/3.

**Theorem 1 (escrow-to-old cash-out table).** From *exactly the two stated refutations* the surviving observations imply:

| Actual observed (t,u) | Permitted s by E1,E2 | Fair old query and terminal capital |
|---|---|---|
| (beta,gamma) | none; impossible on X | terminal future capital 0 |
| (beta,1-gamma) | s=1-a | bet all-in on 1-a; terminal 8C/3 |
| (1-beta,gamma) | s=a | bet all-in on a; terminal 8C/3 |
| (1-beta,1-gamma) | both s-values permitted | query s at zero stake; terminal 4C/3 |

Proof: E1 forbids s=a exactly when t=beta, while E2 forbids s=1-a exactly when u=gamma. Thus a single match excludes exactly one old row, a double match excludes both, and a double nonmatch excludes neither. A correct all-in s wager gives next-child capitals 0,2D for D=4C/3, in the appropriate order, whose mean is D. The double-nonmatch cash-out has next-child capitals D,D and thus no wager. Each t, u and s query precedes its own observation and occurs only once; all child-capital means are exactly the current capital on every transcript, even if a proposed refutation would be unsound off X. Every actually surviving terminal payoff is >=4C/3. In the double-nonmatch case no fair s wager can strictly increase capital at both surviving s-values, since its two child capitals must average D. Further *additional* finite information could still orient s. QED.

Thus zero-stake old-sentinel release after a successful escrow legally starts a fresh least-unread epoch; it neither improves the guaranteed 4/3 payoff nor implies the existence of a successful escrow in that new epoch. The stronger 8/3 multiplier is conditional on a positive observed match, never automatic.

**Lemma 2 (sound positive old orientations).** Any one of the following finite positive patterns, while s is still unread, permits a correct fair doubled s wager followed by consumption:

(i) \`Ref_{s,t}(a,0)\` and \`Ref_{s,t}(a,1)\` for the *same* future target t, since old s=a is excluded regardless of t.

(ii) An observed actual t=beta and a finite \`Ref_{s,t}(a,beta)\`, even if its witness is discovered **after** t is consumed. This justifies a future wager on s, not retroactive profit on t.

(iii) A positive old-only wrong/nonbinary halt \`Ref_s(a)\` for the counterfactual old value s=a and the actually observed outside raw bits, with any protected support request suspended until resolved.

(iv) Either single-match case of Theorem 1, or an independently checked family of positive exclusions leaving one old row.

Two exclusions in the *same* old row at distinct future targets do not orient s before a matching future observation: both targets may avoid their refuted values while s=a. Neither wtt finite value use nor existence of some finite halt bounds when the positive evidence becomes visible. Proof of each positive rule is direct substitution into the forbidden-pair constraints. QED.

## 2. The shielded-old no-orientation theorem

A **semantically shielded old epoch** is an epoch with old unread s such that the virtual recoding of the actual old completion is the total M-fixed source Y, and the virtual recoding Z of the opposite-old completion (with all other raw bits their actual values) is a *global partial fixed point*: if M^Z(n) halts its output equals Z(n). P4-S049 establishes this for its genuinely unresolved old epoch. Shielding is not a c.e. test and cannot be built into a total controller as an oracle.

**Theorem 3 (actual-future column shield).** At a shielded epoch and any fresh future t with actual raw value g=X(t), neither \`Ref_{s,t}(0,g)\` nor \`Ref_{s,t}(1,g)\` is possible. Every positively refuted square corner has future beta=1-g. Hence:

(a) An observed future value never matches the beta of any positive square refutation for that t, so Lemma 2(ii) cannot orient s.

(b) Both \`Ref_{s,t}(a,0)\` and \`Ref_{s,t}(a,1)\` cannot occur, so Lemma 2(i) cannot orient s.

(c) Neither old-only \`Ref_s(0)\` nor \`Ref_s(1)\` can occur.

(d) Whenever the two distinct-future opposite-old-row certificates of Theorem 1 appear, the actual observed t,u are respectively (1-beta,1-gamma). The executed fair 4/3 escrow necessarily takes the *unoriented* third surviving outcome. It cannot generate an 8/3 cash-out from those two refutations alone.

Proof: setting t to its actual g leaves exactly the two counterfactual old completions Y and Z. On Y every equation halts correctly; on Z each equation that halts is correct. Neither gives a finite wrong/nonbinary halt. This excludes both actual-future corners, leaving only future 1-g available for a positive square refutation. (a), (b), (d) follow immediately. The old-only counterfactuals likewise are just Y and Z, proving (c). A divergence is not called a negative certificate. QED.

This is a sharper *finite-information* obstruction than the isolated P4-S051 cash-out table: the shielded regime allows reset-free gains on caught fresh targets but denies exactly the matching-value old-orientation evidence that would justify a doubled reset. An optional zero-stake old query can still reset the epoch, but timing of infinitely many later profitable captures is unproved. P4-S008 independently excludes infinite reset-free success while one fixed s is omitted forever on the computably random X.

## 3. An actual total computable combined cash-out scan

Define a fixed scan \`S_cash\` on every raw binary source together with a rational nonnegative computable output martingale. Maintain the finite table of previously queried coordinates and bits, old sentinel s chosen as the *least unread* coordinate, counters e (epoch) and k (reservation), and at most two additional protected fresh targets. The code contains M,H and a fixed computable source-coordinate order but neither X-bits nor semantic shielding information.

**Initial reservation:** Choose least unread t in a recoding block different from s. Protect s,t for exactly \`L(e,k)=2^(e+k+3)\` ordinary output-query rounds. At global finite simulation stage N dovetail the first N M-inputs for N steps for all four raw (s,t) counterfactual corners. Use synthetic protected answers; put all real outside-support requests on a deterministic queue. Alternate one zero-stake unprotected pending-support query (or a least-unread unprotected filler) with one zero-stake least-unread unprotected sweep query. Never query s,t as support, and suspend every simulation needing an unresolved protected coordinate. Before each ordinary output bit do only finite work; every round emits one fresh real unprotected bit.

**Finite escrow window:** If a finite \`Ref_{s,t}(a,beta)\` is positively seen while s,t remain unread, retain the finite witness and choose least unread u in a distinct third recoding block. Protect s,t,u for exactly \`K(e,k)=2^(e+k+4)\` further ordinary output rounds. Symmetrically dovetail (s,u) four-corner finite simulations as well, with the same support/sweep rule and suspension of protected inputs. Fix a deterministic priority order for all events. Certificates have no inferred deadline.

**Positive exits:** If a positively witnessed \`Ref_{s,u}(1-a,gamma)\` arrives while t,u are still unread, execute the fair t-then-u 4/3 escrow and then **consume old s**: all-in only if Theorem 1 or other actually observed positive evidence uniquely orients s; otherwise query s at zero stake. Release any remaining transient reservation at zero stake, then start epoch e+1 with the new least unread s. If same-target opposite-old-row certificates with a shared future beta arrive first, bet correctly all-in on that future target (factor 2), release other futures and consume s at zero stake or with separately certified orientation, then restart. When a standalone positively sound old-only or same-row orientation is visible, a fixed higher-priority branch may bet correctly all-in on s, release any remaining protected futures at zero stake, and restart. A simulation requiring still-protected other-coordinate actual values cannot fire as an old-only witness until its support is exposed.

**Mandatory timeouts:** If the initial L window expires without a positive executed exit, consume t at zero stake, leave s unread, and begin k+1. If the K escrow window expires, consume t,u at zero stake, leave s unread and begin k+1, except that separately positively verified matching observation may trigger a certified old s wager at the fixed priority point. A witness emerging only *after* t/u consumption may justify future old orientation but never a t/u wager that was not made in time. No-event infinite branches do not stop the scan.

The distinct future targets have strictly finite protection; the old sentinel is never forcibly released by a bare timeout. An optional variant can keep s briefly after success, but must give every transient future an explicit finite release. The specified \`S_cash\` instead always consumes s following any successful escrow.

**Theorem 4 (global legality).** This is an everywhere-total computable adaptive no-repeat scan, fair-coin preserving with fibres of size at most two. Its associated output martingale is total computable, rational, nonnegative and exactly fair.

Proof: each simulation slice has a fixed finite bound. Protected future coordinates are consumed on a finite timeout or exit; at every stage there is a fresh unprotected coordinate to query. The alternating least-unread sweep consumes every nonpermanently protected raw coordinate eventually. Every reset consumes old s and replaces it with the least unread. If infinitely many old turnovers occur, their successive least-unread values tend to infinity and every fixed coordinate is eventually consumed. If there are finitely many, one final s may remain unread, but all other coordinates are eventually consumed by the sweep and compulsory finite target releases. Thus every transcript omits at most one coordinate. Query choice depends computably only on preceding transcript bits, always reads a new fair source bit, and every m-bit output cylinder therefore has fair-coin preimage probability 2^{-m}. The omitted-coordinate fibre formula gives global fibre bound 2. The future 4/3 wagers are the exact fair child-capital expectations above; certified all-in wagers have child pair (0,2C) in the proper order; all zero stakes have (C,C). Thus the output martingale satisfies the exact fair equation on *every* transcript, including losing branches. QED.

**Theorem 5 (infinite executed-turnover sufficient condition).** If this fixed \`S_cash\` or any fixed variant with the same globally legal fair accounting executes infinitely many *completed* profitable exits along the committed X—escrow factors at least 4/3, or correctly certified doubled one-bit exits—then its one computable output martingale succeeds and X not in OH. Zero-stake sweep and timeouts do not change completed capital; any interim 2/3 drop during a two-bit hedge is finite and does not spoil unbounded completed capital. In this success-gated controller each positive closure consumes s, so genuinely infinite profitable exits would entail infinitely many old-sentinel turnovers on the target. No such source-specific infinite exit sequence is proved. QED.

## 4. Reset deadlines versus branchwise avoidability

**Proposition 6 (uniform all-transcript reset collapse).** Consider a total computable no-repeat scan with least-unread s epochs, each of which, on *every* transcript continuation, consumes its s after finite time and enters a next such epoch. Then every transcript queries all source coordinates. The induced fair-coin map is a computable bijection with total computable inverse (simulate a given output until each source coordinate is requested), hence preserves CR by P4-S001. Therefore resetting s at zero stake on **every finite timeout**, on every continuation, cannot produce a CR destroyer. To retain a possible destroying branch the successful target turnover must remain avoidable on some sibling continuation, as in P4-S011 and the present no-event infinite epoch.

This proposition does not prohibit consuming s unconditionally at zero stake **after a positive escrow**: that event may be absent forever on some continuations. It shows why finite mandatory future timeout and finite mandatory old timeout have opposite consequences.

**Theorem 7 (algorithm-relative capture/turnover obstruction).** Under the hypothetical \`X in OH\`, every fixed controller of this stated globally legal family executes only finitely many profitable exits on X; otherwise Theorem 5 would contradict the definition of OH. If old resets in that controller occur only upon positive profitable exits, there are finitely many resets, a final persistent old sentinel s, and no further *timely executed* positive exit along that run. Under the additional semantic P4-S049 shielding hypothesis, Theorem 3 further rules out the described finite wrong-halt old-orientation certificates at that epoch. The conclusions are policy-relative and give no computable index of the last reset, no absence of passive late refutations, no infinite capture theorem, and no proof of X in OH. P4-S008 already rules out infinitely many reset-free gains at any fixed permanently omitted s even without assuming X in OH. QED.

## 5. Exact stopping point

Established: finite cash-out trichotomy and correct 8/3-or-4/3 terminal accounting; positive old-orientation rules; shielded-old no-orientation theorem; explicit bounded-support finite-window total fair one-hole controller with mandatory temporary releases; all-transcript old-deadline permutation collapse; and the conditional infinite-profitable-turnover criterion with algorithm-relative absence under X in OH.

Not established: an executable infinite cross-epoch timely-capture sequence for the committed X, X in OH, X not in OH, OH non-invariance, R_2=OH or strict R_2 versus OH separation. Do not infer them from semantic actual-A recurrence, witness c.e.-ness, finite wtt value use, increasing finite windows or a trapped-epoch oracle.

Next bounded P4-S053 task: isolate a *branchwise-avoidable, source-effective* pre-consumption capture condition that guarantees infinitely many executed profitable old turnovers, or sharpen the algorithm-relative capture obstruction. Distinguish all-transcript reset deadlines from successful target turnovers and passive late discoveries.

PA-0001 remains UNRESOLVED_UNDER_INSPECTED_EVIDENCE; DEF-0020 unchanged. No novelty, openness, prior-art, Gate-4, publication or outreach claim. Phase 4 OPEN, Phase 5 CLOSED.
