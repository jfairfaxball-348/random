# Next Session Prompt — P4-S041

Continue the Fairfax-Ball Randomness Research Programme in https://github.com/jfairfaxball-348/random.

Run only Phase 4 — Mathematics session P4-S041. Treat committed repository state as authoritative. Pin live main at the exact P4-S040 outgoing checkpoint reported by the preceding session, reconcile any mismatch, confirm P4-S041 is unique, and read P4-S001 through P4-S040, the required CAND-01 authority, phase4/P4_RESEARCH_PIVOT_AFTER_S031.md, phase4/P4-S032_MATHEMATICS.md through phase4/P4-S040_MATHEMATICS.md, with special attention to P4-S011, P4-S012, P4-S039 and P4-S040.

## Sustained Phase-4 target — one-hole normalization after coded recoding

Freeze all validated mathematics through P4-S040. Do not return to the P4-S015–P4-S031 ticket/reserve/frontier/recycling sequence, the P4-S037/P4-S038 backward-price route, or ambiguity mass unless the theorem below genuinely requires them.

Retain

[
R_2={xin CR:	ext{every total computable fair-coin-preserving global-}k=2	ext{ map sends }x	ext{ to }CR},
]

[
OH={xin CR:	ext{every total computable adaptive no-repeat one-hole scan sends }x	ext{ to }CR},
]

and

[
OH^{iso}={xin CR:	ext{every computable fair-coin-preserving homeomorphism }H	ext{ sends }x	ext{ into }OH}.
]

The current inclusions remain

[
MLRsubseteq R_2subseteq OH^{iso}subseteq OHsubsetneq CR.
]

Retain the repeated three-bit recoding

[
u_0=x_0oplus x_2,qquad
u_1=x_0oplus x_1,qquad
u_2=x_0oplus x_1oplus x_2,
]

with

[
A=
egin{pmatrix}
1&0&1\
1&1&0\
1&1&1
end{pmatrix},
]

and inverse

[
x_0=u_0oplus u_1oplus u_2,qquad
x_1=u_0oplus u_2,qquad
x_2=u_1oplus u_2.
]

Let (Y) be the settled P4-S011 computably random wtt-autoreducible source, (M) its committed syntactically self-avoiding wtt autoreduction, (D) its one-hole destroyer, and

[
X=H^{-1}(Y).
]

Retain

[
Xin CR,qquad H(X)=Y
otin OH.
]

The missing source-side statement remains whether (Xin OH).

## P4-S040 boundary to retain

P4-S040 weakens P4-S039 local sibling totality to **raw-adjacent decisiveness**.

For a fresh block (B) and raw target direction (i), after the other two raw bits are read the two virtual endpoints differ by

[
c_i=Ae_i,
]

where

[
c_0=111,qquad c_1=011,qquad c_2=101.
]

The actual endpoint is eventually locally accepted by the three equations

[
M^{Y[Bleftarrow v]}(q_r)downarrow=v_r,qquad r=0,1,2.
]

The raw-adjacent companion is **decisive** when it is either:

- locally accepted by all three correct binary halts; or
- finitely refuted by at least one wrong/nonbinary halt.

Thus decisiveness excludes only divergence-only Case C.

P4-S040 proves:

1. if all three raw directions are decisive on every reached synchronized block, three total computable raw one-hole scans suffice;
2. no rejection-time bound is required;
3. the minimum-distance-two local code law forces at least one Case-A finite-rejection direction on every fully decisive block;
4. by infinite pigeonhole one fixed scan receives infinitely many correct all-in wagers, hence
   [
   X
otin OH
   ]
   under the decisiveness hypothesis;
5. this is materially weaker than full 24-computation local sibling totality;
6. Case B is positively visible but gives no prospective same-block handoff, because raw-adjacent endpoints differ only at the current sentinel and certify only already-read raw coordinates;
7. a globally one-hole scan cannot keep a second prospective sentinel permanently unread while the current sentinel is also left permanently unresolved;
8. Case C has no finite divergence certificate;
9. additional outside (M(n))-equations may supply more c.e. finite refutations, but the wtt use bound gives a finite forward oracle frontier for each fixed (n), not a computably finite reverse closure of all equations affected by the changed block;
10. the committed P4-S011 authority does not establish raw-adjacent decisiveness for the actual (M).

Therefore P4-S040 does **not** give an actual raw destroyer for (X), and it does not prove (Xin OH).

## P4-S041 bounded task — finite-perturbation refutability and raw-radius-one partiality

Attack only the new boundary: can divergence-only raw-adjacent companions be eliminated, finitely refuted, or proved unavoidable for the actual wtt-autoreduction mechanism?

Do not return to ordinary raw-martingale compilation.

### 1. Formalize the finite-perturbation fixed-point relation

For any oracle (Z), distinguish carefully:

- target correctness (M^Y(n)downarrow=Y(n));
- local block consistency on the three (q_r);
- global fixed-point behaviour
  [
  M^Z(n)downarrow=Z(n)quad	ext{for every }n;
  ]
- finite refutation by one wrong/nonbinary halt;
- divergence-only failure.

For a raw finite perturbation (Fsubseteqomega), write

[
X^F=Xopluschi_F,qquad
Y^F=H(X^F).
]

Raw radius one means (F={j}), so inside its block (Y^F=Yoplus Ae_i).

Do not conflate local acceptance with global fixed-pointhood.

### 2. Prove the finite-perturbation totality collapse exactly

Use the wtt use bound correctly.

Test and, if valid, prove:

> If the committed self-avoiding wtt functional (M) halts on every input for every oracle which differs from (Y) on only finitely many coordinates, then (M) induces a truth-table autoreduction of (Y).

The intended compact finite-use argument is that, for a fixed input (n), every possible oracle-answer pattern below the computable use can be realized by a finite perturbation of (Y). Totality on all finite perturbations would therefore make the finite local truth table total.

Check the exact retained authority about computably random truth-table autoreducibility before drawing the consequence.

If the lemma holds, conclude only that **some** finite perturbation must expose partiality/divergence. Do not jump from this to radius-one divergence.

### 3. Determine the minimal raw perturbation radius at which divergence is forced

The P4-S040 theorem needs decisiveness only at raw radius one.

Ask whether all one-raw-bit companions can be decisive even though divergence is unavoidable at some larger finite raw perturbation.

Define, if useful, a hierarchy:

[
mathsf{Dec}(r):
	ext{ every raw perturbation of size }le r
	ext{ is either globally/local-relevantly accepted or finitely refuted}.
]

Use only a formulation that is actually needed; do not create notation for its own sake.

Test:

- whether (mathsf{Dec}(1)) is compatible with non-tt wtt autoreducibility;
- whether the three-bit block basis makes radius-one decisiveness propagate to larger finite perturbations;
- whether compositions of the three raw flip columns can force totality on every finite use pattern;
- or whether divergence can be hidden entirely in perturbations involving two or more raw coordinates.

A proof that radius-one decisiveness forces too much would identify a genuine obstruction to applying P4-S040 to the actual witness.

A construction/normal-form argument showing radius-one decisiveness can coexist with necessary higher-radius divergence would keep the positive route open.

### 4. Exploit the finite-difference dependency graph

If both (Y) and a finite perturbation (Z=Yopluschi_S) are global fixed points of the same self-avoiding (M), then for every changed coordinate (nin S), the computations on (Y) and (Z) must obtain different outputs without querying (n).

Test the exact consequence:

- some queried coordinate in (Ssetminus{n}) must influence the change;
- hence the changed coordinates carry a finite directed dependency graph of minimum out-degree at least one;
- therefore that graph contains a directed cycle.

For the raw-adjacent supports

[
operatorname{supp}(Ae_1)={q_1,q_2},qquad
operatorname{supp}(Ae_2)={q_0,q_2},qquad
operatorname{supp}(Ae_0)={q_0,q_1,q_2},
]

classify the possible two-cycle / three-cycle patterns precisely.

Determine whether these finite cycle constraints create a new finite refutation certificate or merely characterize the genuine Case-B companions.

Do not silently assume that a computation which differs between two oracles must halt on both unless that has been established.

### 5. Test target-equivalent wtt normal forms

The core constructive question is whether (M) can be replaced by another syntactically self-avoiding wtt functional (M') such that:

- (M'^Y(n)=Y(n)) for every (n);
- a computable use bound is retained;
- every raw-radius-one companion at the P4-S040 synchronized blocks is either a genuine accepted fixed-point candidate or has a finite wrong/nonbinary witness;
- divergence is permitted elsewhere, so full truth-table totality is not imposed.

Test concrete normal-form operations:

- dovetail several target-correct self-avoiding computations and accept the first finite disagreement;
- add redundant self-avoiding equations whose target values are forced but which may reject finite perturbations;
- compose or duplicate local checks without querying the input coordinate;
- use finite perturbation closure inside one wtt use window;
- or prove that every such attempted totalization necessarily requires negative divergence information.

Any modification must be computable uniformly from the committed data. Do not use (Y) as a noncomputable parameter in the program.

### 6. Separate finite refutation from totalization

A companion only needs **one** finite refutation witness.

Do not require all its computations to halt.

Test whether partial functions can be extended just enough to create wrong-halt witnesses on the three structured raw-adjacent patterns while leaving other answer patterns divergent.

If an abstract local extension is easy, identify the global uniformity obstruction: the compiler does not know which finite answer pattern belongs to the actual noncomputable (Y).

This distinction is central to deciding whether P4-S040's condition is realistically weaker for the actual source, rather than only logically weaker as a local table property.

### 7. Revisit outside equations only through finite witnesses

For a raw-adjacent companion, allow any outside input (n) whose (M(n)) computation can be simulated target-self-avoidingly.

If one such computation halts incorrectly, that is a valid finite refutation.

But do not quantify over infinitely many outside equations and then claim completion.

Test whether the finite-difference/cycle structure yields a computable **finite witness set** of outside inputs for the special supports (Ae_i). If no such set is forced, record the exact reason.

### 8. If raw-radius-one decisiveness is obtained, apply P4-S040 fully

Do not stop at the normal form.

Verify that the new (M') or the new finite refutation mechanism satisfies the exact P4-S040 decisiveness hypothesis on every reached synchronized block.

Then invoke the already-validated three-scan theorem and conclude only

[
X
otin OH.
]

This eliminates the present source as an OH non-invariance candidate. It does not prove (R_2=OH).

### 9. If radius-one Case C is unavoidable, state the narrowest theorem

A negative result should distinguish at least:

- divergence somewhere among arbitrary finite perturbations;
- divergence on some single raw-coordinate perturbation;
- divergence on infinitely many reached fresh blocks;
- divergence in enough raw directions to defeat every P4-S040 finite-family scan.

Do not infer the stronger statements from the weaker ones.

The strongest useful negative outcome would show that every target-equivalent self-avoiding wtt presentation of the actual source necessarily has persistent raw-radius-one divergence-only companions in the recoding geometry.

A weaker exact obstruction is still useful if clearly delimited.

### 10. Preserve the source-side separation guard

An OH non-invariance theorem still requires

[
Xin OH,qquad H(X)=Y
otin OH.
]

Only the second statement is settled.

If P4-S041 obtains raw-radius-one decisiveness and therefore a raw destroyer, then the present source is eliminated as a separation candidate.

If it proves only that P4-S040 extraction cannot be forced from the committed autoreduction data, (Xin OH) remains unproved.

### 11. Required session outcome

The output should be one of:

- an actual proof of raw-adjacent decisiveness for a target-equivalent self-avoiding wtt presentation of the P4-S011 source, followed by the P4-S040 raw one-hole destroyer;
- a finite-perturbation normal-form theorem materially advancing toward that goal;
- a rigorous theorem locating the unavoidable partiality at a specific raw perturbation radius;
- a finite-difference dependency/cycle theorem which sharply classifies Case-B versus Case-C companions;
- or, only if it follows directly, a genuine proof that (Xin OH).

The sustained question remains

[
R_2=OH;?
]

If no OH non-invariance witness is proved, preserve (OH^{iso}) as the comparison class and state separation status explicitly.

P4-S032 null-ambiguity preservation remains available. Do not return to ambiguity mass as an invariant.

Preserve PA-0001 as **UNRESOLVED_UNDER_INSPECTED_EVIDENCE** and DEF-0020 unchanged. Make no novelty, openness, prior-art, Gate-4, publication or outreach claim. Continue original mathematics only.

Record, validate and synchronize useful work, commit it, verify remote main, report the exact outgoing hash, and provide the next prompt if no blocker exists.
