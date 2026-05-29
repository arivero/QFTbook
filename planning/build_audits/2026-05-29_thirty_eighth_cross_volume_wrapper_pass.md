# Thirty-Eighth Cross-Volume Anti-Wrapper Pass

Date: 2026-05-29.

Issue context: continuing GitHub issue #691 after checkpoint `e9addf64`.
The pass focused on compact theorem-family proofs and on statements whose
content could be hidden in a strong hypothesis.  No theorem-family statement
was demoted in this batch; the audited weak-looking items either carried
genuine structural content or needed proof expansion.

## Proofs Strengthened

Three theorem-family proofs were expanded.

1. `prop:time-ordered-wightman-piece-compatibility` in Volume I, Chapter 11.
   The proof now works on a small product neighborhood in the off-diagonal
   configuration space, treats codimension-one and higher-codimension chamber
   walls by adjacent transpositions of spacelike separated equal-time points,
   and uses the sheaf property of distributions to glue the chamber
   distributions.

2. `lem:hepp-sector-forest-extraction` in Volume II, Chapter 9.
   The proof now constructs the threshold subgraphs \(H_j\), proves the
   laminar forest property using 1PI block decomposition under nested edge
   inclusions, and then derives the representation of ultraviolet sector
   boundaries by induction over Hepp scale ratios and quotient graphs.

3. `prop:bv-renormalizable-ghost-zero-cohomology` in Volume II, Chapter 24.
   The proof now spells out the antifield-number spectral-sequence reduction,
   deletion of the nonminimal BRST doublet, the ghost-number-zero longitudinal
   gauge-invariance condition, the finite-dimensional invariant-tensor
   structure of covariant jet monomials, the dimension-four enumeration, and
   the separation between genuine interaction-density coordinates and
   antifield representatives of field redefinitions or currents.

## Read And Retained

After these edits, the local compact-proof parser found no theorem-family
proofs at or below 220 lexical tokens and seven at or below 260 tokens.  I
read these seven in context:

- `prop:sm-chiral-lattice-anomaly-necessity`
- `prop:hr-scalar-wave-operator-isometry`
- `prop:singular-stratum-obstruction-localized-qme`
- `prop:lorentzian-ope-continuation-domain`
- `prop:form-factor-exchange`
- `prop:two-dimensional-axial-contact-term`
- `thm:jost-edge-gluing-primitive-tubes`

These were retained.  Each packages a structural input whose statement is
used elsewhere: determinant-line obstruction for chiral lattice regulators,
Haag--Ruelle wave-operator isometry, BV boundary obstruction for singular
localization strata, Lorentzian OPE boundary-value convergence, Watson
exchange from factorized scattering, the two-dimensional anomaly contact
term, and edge-of-the-wedge gluing of primitive Wightman tubes.  None is a
mere algebraic substitution after reading the surrounding derivation.

I also read the next hypothesis-heavy samples surfaced by cue search,
including the local \(P\)-\(Q\) bridge consequences in the planar QSC chapter,
the observable-threshold preservation statement in the SUSY-family chapter,
the odd-symplectic origin of the BV antibracket, the BPS singular-value bound,
the reflection adjoint of defect actions, the displayed sausage Yang--Baxter
identity, the finite \(\mathfrak{su}(N)\) line lattice, and the self-dual
finite gauging fusion ring.  These are not immediate demotion targets:
several are already prose consequences rather than propositions, and the
remaining theorem-family statements either perform nontrivial finite
enumeration or record a calculation whose proof is supported by symbolic
checks or by an explicit construction.

## Current Counts

After this pass:

- theorem environments: 94
- proposition environments: 367
- lemma environments: 29
- corollary environments: 10
- theorem-family total: 500
- proof environments: 495
- proof environments at or below 220 lexical tokens: 0
- proof environments at or below 260 lexical tokens: 7

The remaining work on #691 is not closed by these counts.  The next passes
should continue semantic reading above the short-proof threshold and should
focus especially on conditional statements where the mathematical content may
still reside mainly in a hypothesis rather than in the named result.

## Verification

Checks clean for this pass:

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- direct missing-reference scan: `missing_count 0`
- primitive-TeX division scan: no `\over` hits in `monograph/tex/volumes`
- `tools/build_monograph.sh`

The full build and log scan are clean.  The rebuilt
`monograph/tex/main.pdf` has 2592 pages.
