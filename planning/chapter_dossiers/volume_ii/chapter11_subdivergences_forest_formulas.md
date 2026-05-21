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

## Construction Task

The chapter must define:

- Euclidean Feynman graph \(\Gamma\), internal lines \(E(\Gamma)\), loop number
  \(L(\Gamma)\), external momenta \(p\), and integrand \(I_\Gamma(\ell,p)\);
- subgraph \(\gamma\subseteq\Gamma\), its external momenta \(p_\gamma\), and the
  contracted graph \(\Gamma/\gamma\);
- superficial degree of divergence \(\omega(\gamma)\);
- divergent 1PI subgraph;
- Taylor subtraction operator \(t_\gamma\) at a specified subtraction point;
- spinneys and forests;
- recursive preparation map \(\overline R_\Gamma\), counterterm map
  \(C_\gamma\), and full \(R_\Gamma\);
- the forest formula;
- the overlapping-subgraph diamond example;
- locality of counterterms and the finite-list conclusion for
  power-counting-renormalizable theories.

## Claim Ledger

1. A UV subgraph is specified by a subset of internal lines whose loop momenta
   are scaled together while momenta in the complement are held fixed.
2. The superficial degree \(\omega(\gamma)\) determines the Taylor degree needed
   to remove the leading UV boundary term associated with \(\gamma\).
3. \(t_\gamma I_\Gamma\) is polynomial in \(p_\gamma\) and therefore corresponds
   to a local vertex in the contracted graph.
4. A spinney is a set of mutually disjoint divergent proper subgraphs; a forest
   is a set of divergent subgraphs that are pairwise disjoint or nested.
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
