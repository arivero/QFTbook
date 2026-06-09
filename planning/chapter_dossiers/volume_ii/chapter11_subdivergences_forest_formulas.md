# Volume II, Chapter 11 Dossier: Subdivergences And Forest Formulas
Source-File: monograph/tex/volumes/volume_ii/chapter09_subdivergences_and_bphz_subtractions.tex

## Source Position

- Primary local source: second-sequence handwritten material, pages 89--96,
  especially the higher-order \(D=6\), \(\phi^3\) self-energy insertion and
  Schwinger-parameter diamond graph.
- Immediate predecessor: renormalizability and local counterterms.
- Immediate successor in the source order: the 1PI renormalization group.
- Role in the monograph: turn the local two-loop subdivergence analysis into a
  systematic graph-level subtraction formalism before scale-dependent
  renormalized couplings are introduced.

## Source And Reference Controls

- `SRC-QFT-PDF`: `references/253b lecture notes 2023.pdf`, pages 89--96;
  checked against rendered page images.
- `SRC-BEN-COMPARISON`: `references/253b transcribed lecture notes.tex`,
  locality of higher-order subtractions and the start of the 1PI RG, used only
  as a comparison layer.
- `SRC-EXTERNAL`: Fredenhagen--Rejzner for locality/renormalization in
  perturbative AQFT and the Epstein--Glaser comparison.  The chapter is written
  in Euclidean momentum-space language, matching the preceding construction.
- `SRC-EXTERNAL-HEPP-ZIMMERMANN`: Hepp's and Zimmermann's momentum-space
  convergence theorem supplies the uniform Hepp-sector analytic estimate:
  sector charts, adapted loop bases, Jacobian and denominator comparison
  constants, simultaneous subgraph/quotient power counting, and the control of
  extra Taylor operators in the global forest formula.  The local text may
  explain the forest architecture and one-scale Taylor-remainder mechanism, but
  must not present the full sector estimate as locally derived.
- `SRC-EXTERNAL`: Lowenstein--Zimmermann/BPHZL for the massless extension of
  momentum-space subtraction, especially the power-counting theorem for
  massless propagators and the infrared convergence theorem for the massless
  \(\phi^4\) model.

## Construction Task

The chapter must define:

- the top-of-chapter path-integral status declaration: BPHZ is a
  coefficient-by-coefficient renormalization of the formal perturbative
  expansion extracted from a regulated Euclidean source functional, not a
  nonperturbative continuum measure construction;
- Euclidean Feynman graph \(\Gamma\), internal lines \(E(\Gamma)\), loop number
  \(L(\Gamma)\), external momenta \(p\), and integrand \(I_\Gamma(\ell,p)\);
- the convention that the chapter works with 1PI kernels, while connected
  Green functions are reconstructed by the Legendre tree expansion;
- momentum subgraph \(\gamma\subseteq\Gamma\), its external half-lines,
  external momenta \(p_\gamma\), and the contracted graph \(\Gamma/\gamma\);
- superficial degree of divergence \(\omega(\gamma)\);
- divergent 1PI subgraph;
- Taylor subtraction operator \(t_\gamma\) at a specified subtraction point,
  including what is held fixed during the operation;
- spinneys and forests;
- recursive preparation map \(\overline R_\Gamma\), counterterm map
  \(C_\gamma\), and full \(R_\Gamma\);
- the Bogoliubov preparation recursion as a well-founded graph induction;
- the Zimmermann forest formula as an identity of formal integrands before
  loop integration;
- the Hepp-sector forest extracted from an ordered ultraviolet hierarchy;
- the explicit theorem boundary for the imported Hepp--Zimmermann sector
  power-counting estimate used in the massive BPHZ finiteness proof;
- the overlapping-subgraph diamond example;
- the Zimmermann identity for oversubtracted normal products;
- locality of counterterms and the finite-list conclusion for
  power-counting-renormalizable theories.
- the theorem boundary between massive/nonexceptional BPHZ finiteness and the
  massless critical case, where BPHZL or an equivalent infrared-safe
  prescription is required.

## Claim Ledger

0. The BPHZ construction in this chapter acts on graph coefficient
   distributions in the formal expansion of regulated Euclidean Green functions
   and 1PI kernels.  It does not assert the existence of an unregulated
   continuum path-integral measure and is not by itself a nonperturbative
   construction of the QFT.
1. A UV subgraph is specified by a subset of internal lines; its external
   half-lines are all incident half-lines not contained in the subgraph.
   Internal loop momenta of the subgraph are scaled together while momenta in
   the contracted graph are held fixed.
2. The superficial degree \(\omega(\gamma)\) determines the Taylor degree needed
   to remove the leading UV boundary term associated with \(\gamma\).
3. \(t_\gamma I_\Gamma\) is polynomial in \(p_\gamma\) and therefore corresponds
   to a local vertex in the contracted graph.
4. A spinney is a set of mutually disjoint connected divergent proper
   subgraphs; a forest is a set of connected divergent subgraphs that are
   pairwise disjoint or nested.  Disconnected divergent subtractions are
   products over connected components.
5. The recursive BPHZ construction subtracts proper subgraphs first and the
   overall graph last.
5a. The recursive construction is well founded because every proper
    connected divergent subgraph has fewer internal lines than the graph whose
    counterterm is being constructed; each recursive counterterm is a local
    polynomial vertex of degree bounded by the corresponding superficial
    degree.
5b. Zimmermann's forest formula is the integrand-level expansion of the
    Bogoliubov recursion.  The proof is by induction using the maximal
    elements of a forest not containing the full graph as the spinney in the
    prepared graph.
6. In the two-loop diamond graph, the left and right one-loop subgraphs overlap;
   the compatible forests are therefore
   \(\emptyset,\{\gamma_L\},\{\gamma_R\},\{\Gamma\},
   \{\gamma_L,\Gamma\},\{\gamma_R,\Gamma\}\).
7. The forest formula is an inclusion-exclusion formula over compatible UV
   boundary regions.
8. In a massive Euclidean scalar theory with nonexceptional external momenta,
   the BPHZ-renormalized integrand is UV integrable.
8a. A Hepp-sector partition turns each ordered ultraviolet hierarchy into a
    forest of divergent 1PI components; this is the sector-local reason that
    the global forest formula subtracts all ultraviolet boundary strata.
8b. The sector product majorant for \(R_\Gamma I_\Gamma\) is an imported
    Hepp--Zimmermann analytic estimate.  The chapter must state that the
    estimate includes adapted routing for branches, uniform denominator and
    numerator-derivative bounds, simultaneous subgraph/quotient exponents, and
    harmlessness of extra global forest subtractions.
9. Counterterms produced by \(C_\gamma\) are local polynomials bounded in degree
   by \(\omega(\gamma)\).
10. In a finite-list power-counting-renormalizable theory, the recursive
    counterterms remain in the finite local operator space established in the
    previous chapter.
11. The proof sketch must explicitly use the fact that external-momentum
    derivatives lower the superficial UV degree for one isolated scale, but
    must also state that this one-scale mechanism does not by itself prove the
    multiscale Hepp-sector product estimate.
12. Massless zero-momentum subtractions require separate infrared control:
    BPHZL introduces auxiliary mass/subtraction data and IR degrees so that
    UV-local subtractions possess a distributional massless limit when the
    Lowenstein--Zimmermann power-counting conditions hold.
13. The finite local freedom produced by Taylor subtractions is the BPHZ side
    of the BPHZ--Wilsonian comparison: in the Wilsonian chapter, these local
    polynomials are identified with finite local coordinates in the retained
    Wilsonian chart.
14. Changing the subtraction degree of a marked insertion produces a
    Zimmermann normal-product identity: the difference between the two
    subtraction schemes is a finite sum of renormalized local insertions with
    the same exact quantum numbers and bounded engineering degree.

## Figure Requirements

- Compatible subgraph collections: disjoint, nested, and overlapping.
- Taylor subtraction of a subgraph into a local contracted vertex.
- Diamond graph forest list showing \(\gamma_L\), \(\gamma_R\), and \(\Gamma\).

## Audit Notes

- No reader-facing source-page references.
- Avoid slogan language.  State graph-theoretic definitions before using the
  forest formula.
- Keep the chapter as the bridge from local counterterms to the 1PI RG: finite
  renormalization and movement of subtraction points should point forward but
  not replace the RG chapter.
- Keep the massless critical extension tied to the later Wilson--Fisher and
  Ising chapters: they may use nonexceptional momenta, finite volume/small mass
  limits, BPHZL, or Wilsonian exact RG, but the massive theorem alone is not
  the full critical subtraction theorem.
- 2026-05-22 pass: tightened the 1PI graph convention, external-half-line
  definition of subgraphs, Taylor-operator holding data, connected spinney and
  forest conventions, and the BPHZ proof sketch.
- 2026-05-22 source-certification pass for pp. 89--96: the preceding local
  counterterm chapter now contains the handwritten Schwinger-parameter
  \(D=6\ \phi^3\) diamond calculation through \(A\), \(Q\), the homogeneous
  scaling relation, the two \(\widetilde F\) subdivergence subtractions, and
  the final \(k^0,k^2\) overall Taylor subtraction.  This chapter supplies the
  systematic forest-formula continuation of that source calculation.
- 2026-05-24 issue pass: addressed #219 by adding a massless/BPHZL remark to
  the chapter, distinguishing the massive BPHZ theorem from the infrared-safe
  subtraction framework needed for critical massless kernels.
- 2026-05-24 issue pass: addressed #316 by adding the missing
  top-of-chapter path-integral status declaration.  The chapter now states
  before the graph formalism that BPHZ renormalizes formal perturbative
  coefficient distributions extracted from a regulated source functional and
  is not a nonperturbative continuum path-integral construction.
- 2026-05-24 issue #497 pass: added a forward cross-reference from the finite
  subtraction-coordinate discussion to the Wilsonian comparison theorem, where
  BPHZ local Taylor parts are identified with Wilsonian local-coordinate data.
- 2026-05-28 issue #633 correction pass: strengthened the BPHZ chapter by
  adding proposition/theorem/lemma statements with proofs for the Bogoliubov
  preparation recursion, Zimmermann forest formula, Hepp-sector forest
  extraction, and Zimmermann normal-product identity.  Added
  `calculation-checks/bphz_forest_formula_checks.py` to verify the finite
  recursive/forest combinatorics for nested, disjoint, and overlapping
  subgraph configurations.
- 2026-06-09 issue #970 correction pass: separated the finite forest
  architecture from the hard Hepp--Zimmermann analytic convergence theorem.
  The chapter now quotes the sector power-counting estimate explicitly, marks
  the sector product bound as imported analytic input, and treats the
  Taylor-remainder calculation as a one-scale diagnostic rather than a
  self-contained multiscale proof.  The companion check now carries an evidence
  contract and negative finite controls for missing quotient decay and naive
  routing factorization.
