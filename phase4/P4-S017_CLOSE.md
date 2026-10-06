# P4-S017 close

Date: 2026-10-06
Session: P4-S017
Incoming checkpoint: 4f587d38ff58c3eb6314c4f1d22bfd57594c77ea
Scope: selected CAND-01; k=2 self-financing last-chance reserve boundary only
Status: **COMPLETED**

## Result

P4-S017 weakens the bankroll hypothesis in P4-S016 for the same exact last-chance ticket stream.

For exact premiums pi_i and realized ticket payouts e_i, start with finite computable reserve R. The new condition is **coercive self-financing admissibility**: the full-ticket account can pay every premium without borrowing on every run, and whenever cumulative realized skipped gain diverges its capital is unbounded.

The settled P4-S016 restart hedge handles finite realized skipped gain while the ticket account handles divergent realized loss. Their sum is one computable completion martingale; the sentinel-first completion remains a P4-S001 effective isomorphism, so one computable source martingale follows. No infinite optional projection or future-loss envelope is computed.

P4-S016's finite absolute premium budget implies the new condition. A stronger easy certificate is an explicit computable unbounded reserve floor g(E), but the theorem itself needs no such modulus.

For a fixed H/ticket stream the weakening is strict. A two-filler functional triggers with all-in +1 when its second filler is 1 and diverges forever when it is 0. With H=1, the savings-wrapped positive gains are ell_r=1/(r+1), premiums are ell_r/2, and reserve R=1/2 is self-financing and coercive while the absolute premium sum diverges on an all-trigger path. This separation is only for fixed H.

Bare no-overdraft is not enough. If the same functional always triggers after the second filler, a positive-sentinel last-chance ticket has price equal to its certain payout. The same reserve can be recycled forever while realized skipped gain diverges, and the restart hedge can remain bounded. This is an obstruction to the ticket/restart architecture, not a universal martingale impossibility theorem.

P4-S011 fails the new condition for every computable horizon selector. P4-S016 already forces divergent realized skipped gain on its computably random target Y. A coercive admissible account would succeed on the effective-isomorphism completion of Y, contradicting P4-S001. Bare admissibility alone is not ruled out for P4-S011.

P4-S011, P4-S015 and P4-S016 remain unchanged. P4-S005 through P4-S016 remain settled. PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**. DEF-0020 is unchanged. No k>2, novelty, Gate-4, publication or outreach claim is made.

Owner/external blocker: **NONE**.

Validation: phase4/P4-S017_VALIDATION.md.

Recommended next bounded session: P4-S018, still at k=2, testing only whether semantic coercivity can be replaced by a local computable reserve-floor / retained-surplus modulus without restoring absolute premium summability.
