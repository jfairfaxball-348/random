# P4-S029 validation

Date: 2026-10-06
Session: P4-S029
Incoming checkpoint: dbdee97f6981e00cd2a677b742de042f36c7dacc
Scope: selected CAND-01; k=2 finite-frontier necessity / bare reserve boundary only
Status: **VALIDATED**

## Repository and scope checks

- Live main matched the requested incoming checkpoint exactly before substantive work and immediately before writes.
- The incoming tree contained P4-S001 through P4-S028 and no committed P4-S029 result; commit search showed P4-S028 as the latest completed session.
- P4-S001 through P4-S028 and required CAND-01 authority were read.
- P4-S005 through P4-S028 remain settled.
- P4-S011 and P4-S015 through P4-S028 are preserved.
- PA-0001 remains **UNRESOLVED_UNDER_INSPECTED_EVIDENCE**.
- DEF-0020 is unchanged.
- No k>2, novelty, Gate-4, publication or outreach claim is made.

## Mathematical validation

### 1. The scan really is the P4-S028 no-frontier global-k=2 scan

The first epoch withholds sentinel 0 and queries positive coordinates until the first 1. If no 1 occurs, exactly coordinate 0 is omitted and the fibre has size two. If a 1 occurs, sentinel 0 is consumed and every later sentinel is consumed immediately, so the fibre is a singleton.

Every output query is fresh and selected from previous transcript data, giving fair-coin preservation by the settled fresh-coordinate induction.

After any finite prefix of zero fillers, a later unseen bit can still decide whether the first epoch triggers. Hence no finite dependency frontier exists.

### 2. The decaying martingale is total, computable and nonnegative

When the first 1 occurs at filler n, the sole nonzero sentinel wager has fractional stake (2^{-n}le1/2) on bit 1. Both child multipliers (1pm2^{-n}) are nonnegative computable rationals. The martingale is flat before that wager and freezes after it.

Before the wager the P4-S015 savings wrapper has savings 0 and active risk 1, so its positive skipped gain on stored sentinel 1 is exactly (2^{-n}).

### 3. The postmiss tickets remain genuinely one-sided at arbitrary depth

Take H=1. On the stored-sentinel-1 branch after zeros through filler n-1, n>=2, filler 0 leaves the epoch unresolved and filler 1 causes the sentinel trigger with skipped gain (2^{-n}).

Thus
[
(L_n(0),L_n(1))=(0,2^{-n}),
qquad
pi_n=2^{-(n+1)}.
]

This occurs for every n>=2, so the construction does not recover a finite frontier.

### 4. The reserve computation is exact

The entire positive-cost tail is
[
sum_{n=2}^{infty}2^{-(n+1)}=1/4.
]

Therefore P4-S016 supplies a uniform absolute premium bound B=1/4 and P4-S017's canonical full-ticket account is globally admissible with R=1/4.

On the all-zero avoiding sibling, after buying through ticket N the remaining cash is
[
1/4-sum_{n=2}^{N}2^{-(n+1)}=2^{-(N+1)}>0,
]
so every finite prescribed purchase is affordable. If a 1 eventually occurs, the triggering ticket pays (2^{-n}), improving the account. Stored sentinel 0 produces no positive-loss tickets. Later epochs have zero ticket cost because the martingale freezes.

Hence the global admissibility claim covers every sentinel-first completion branch.

### 5. The parametric comparison is correct

Replacing (2^{-n}) by any computable rational (0<alpha_nle1) leaves the scan geometry unchanged and gives, on the stored-sentinel-1/all-zero sibling,
[
(L_n(0),L_n(1))=(0,alpha_n),qquadpi_n=alpha_n/2.
]

A computably bounded summable tail gives a finite reserve. A divergent tail gives an unbounded cumulative zero-payout premium deficit, so no finite reserve can work.

Thus P4-S028's constant (alpha_n=1) witness and P4-S029's (alpha_n=2^{-n}) witness are exact opposite bankroll behaviours inside the same no-frontier scan.

### 6. P4-S011/P4-S027 remains a distinct deterministic mechanism

After P4-S027/P4-S028 frontier exhaustion, positive ticket vectors are ((ell,ell)): premium and certain payout agree. Reserve 1 therefore recycles even when the premium sum diverges.

Nothing in P4-S029 changes P4-S011's destroyer or restores coercivity, loss-properness, searchability or any later transfer hypothesis.

## Validation outcome

**PASS.**

P4-S029 disproves finite-frontier necessity for bare canonical full-ticket admissibility by an exact no-frontier global-k=2 example with arbitrarily late one-sided trigger risk and finite reserve. The controlling distinction in the fixed first-1-search family is the cumulative one-sided premium deficit, not the existence of a finite dependency frontier.

Owner/external blocker: **NONE**.
