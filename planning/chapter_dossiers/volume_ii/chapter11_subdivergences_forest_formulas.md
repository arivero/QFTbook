# Volume II, Chapter 11 Dossier: Subdivergences And Forest Formulas

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
  perturbative AQFT and the Epstein--Glaser comparison; classic BPHZ theorem
  enters as a theorem-level mathematical control.  The chapter is written in
  Euclidean momentum-space language, matching the preceding construction.
- `SRC-EXTERNAL`: Lowenstein--Zimmermann/BPHZL for the massless extension of
  momentum-space subtraction, especially the power-counting theorem for
  massless propagators and the infrared convergence theorem for the massless
  \(\phi^4\) model.

## Construction Task

The chapter must define:

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
- the forest formula;
- the overlapping-subgraph diamond example;
- locality of counterterms and the finite-list conclusion for
  power-counting-renormalizable theories.
- the theorem boundary between massive/nonexceptional BPHZ finiteness and the
  massless critical case, where BPHZL or an equivalent infrared-safe
  prescription is required.

## Claim Ledger

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
6. In the two-loop diamond graph, the left and right one-loop subgraphs overlap;
   the compatible forests are therefore
   \(\emptyset,\{\gamma_L\},\{\gamma_R\},\{\Gamma\},
   \{\gamma_L,\Gamma\},\{\gamma_R,\Gamma\}\).
7. The forest formula is an inclusion-exclusion formula over compatible UV
   boundary regions.
8. In a massive Euclidean scalar theory with nonexceptional external momenta,
   the BPHZ-renormalized integrand is UV integrable.
9. Counterterms produced by \(C_\gamma\) are local polynomials bounded in degree
   by \(\omega(\gamma)\).
10. In a finite-list power-counting-renormalizable theory, the recursive
    counterterms remain in the finite local operator space established in the
    previous chapter.
11. The proof sketch must explicitly use the fact that external-momentum
    derivatives lower the superficial UV degree, so the Taylor remainder has
    negative UV degree in each forest sector.
12. Massless zero-momentum subtractions require separate infrared control:
    BPHZL introduces auxiliary mass/subtraction data and IR degrees so that
    UV-local subtractions possess a distributional massless limit when the
    Lowenstein--Zimmermann power-counting conditions hold.

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
