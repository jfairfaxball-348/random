# P4-S167 — Full quantifier ledger

H1 POSITIVE obligation still OPEN:
`for all x in CR\MLR, exists k>=2, exists total computable globally fair G, [for all y, |G^-1(y)|<=k] and exists total nonnegative exact rational d such that limsup_n d(G(x)|n)=infinity.`
G,d,k may depend NONuniformly on x but are finite computable objects, not x-oracle programs. Failed: universal pre-revelation predictor and unbounded composition do not provide the required existential objects.

H1 NEGATIVE obligation still OPEN:
`exists ONE x in CR\MLR, for all k>=1, for all total computable globally fair G with for all y |G^-1(y)|<=k, for all total exact rational d, sup_n d(G(x)|n)<infinity.`
Neither full-measure preservation nor separate x_k witnesses proves this.

C167.1: `for all TOTAL computable G, for all j>=2, E_j(G)=union_n C_{j,n}(G)`, C_{j,n} uniformly effectively closed, each y in C has j distinct ACTUAL complete inverse streams. No fairness or global cap assumption.

C167.2: `for all G as above, j,n, and all Schnorr-random y in C_{j,n}, lambda(C_{j,n})>0`; and `lambda(E_j)=0 => E_j contains NO Schnorr-random output`. Positivity is NOT an effective lower bound.

C167.3: `for all TOTAL computable globally fair G and every k>=1, [lambda(E_{k+1}(G))=0] => [for every x in CR, |G^-1(G(x))|<=k]`. **This implication DOES NOT assert for all y cap k.**

H2 `exists K R_K=MLR`: OPEN. H3 `for all k>=2 R_{k+1} strictly contained R_k`: OPEN. H4 `F_ub strictly contained F_pf`: family-level proven by prior-known variable deletion benchmark; `R_pf strictly contained R_fin` NOT proved. H5 R_pi/growth undefined, modular restrictions exploratory. R2/R3 E-08/E-00/S-00 and A source OPEN.
