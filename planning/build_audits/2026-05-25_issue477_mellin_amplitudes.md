# Build Audit: Issue #477 Mellin Amplitudes

## Scope

Addressed GitHub issue #477, which asked for Mellin amplitudes to be included
in the CFT/OPE development with at least the definition and OPE-pole
interpretation.

## Manuscript Changes

- Added a Mellin-representation subsection to Volume III, Chapter 9.
- Defined the constrained \(n\)-point Mellin space
  \(\delta_{ij}=\delta_{ji}\), \(\delta_{ii}=0\),
  \(\sum_{j\ne i}\delta_{ij}=\Delta_i\), together with the gamma-normalized
  Mellin-Barnes kernel.
- Derived the four-point formula in the chapter's existing reduced-correlator
  convention:
  \(u^{\mathfrak s/2}v^{(\mathfrak t-\Delta_2-\Delta_3)/2}\) times the six
  gamma factors.
- Added a proof that the formula is compatible with the scalar four-point
  prefactor already used in Chapter 8.
- Explained the contour-shift mechanism that maps simple Mellin poles to
  \(u\)-power OPE terms and higher-order poles to logarithms.
- Derived the \(12\)-channel OPE pole family
  \(\mathfrak s=\Delta-\ell+2m\) under explicit Mellin-representability,
  meromorphy, and vertical-growth hypotheses, and identified the
  gamma-stripped residues as Mack-polynomial residues fixed by the conformal
  block Casimir equation and OPE boundary condition.
- Recorded the crossing action as a permutation of constrained Mellin
  variables.

## Calculation Check

- Added `calculation-checks/mellin_four_point_checks.py`.
- The script verifies the constrained \(\delta_{ij}\) equations, the
  prefactor/cross-ratio exponent reduction, the \(1/4\) Jacobian from
  \((\delta_{12},\delta_{14})\) to
  \((\mathfrak s,\mathfrak t)\), the
  \(\mathfrak s=\tau+2m\) OPE-exponent map, and the identical-scalar
  \(2\leftrightarrow4\) channel permutation.

## Verification Results

- `python3 calculation-checks/mellin_four_point_checks.py` passed.
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed clean after replacing the unsupported
  `\mathscr` symbol by the manuscript's `\mathcal` convention and adding the
  missing label on the Euclidean radial OPE theorem.
- `pdfinfo monograph/tex/main.pdf` reports 880 pages.
- Rendered and visually inspected the affected physical PDF pages 856--859;
  the Mellin definition, four-point gamma kernel, contour-shift formula, and
  OPE-pole proposition fit without overfull displayed equations.
