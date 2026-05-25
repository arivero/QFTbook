# Build Audit: Issues 536, 537, 538 Integrable Bootstrap Analyticity

Date: 2026-05-25

## Scope

Development pass on
`monograph/tex/volumes/volume_vi/chapter02_two_dimensional_scattering_analyticity_bootstrap.tex`,
addressing the open rigor issues on growth hypotheses, elementary scalar
blocks, and the bound-state fusion bootstrap equation.

## Mathematical Changes

- Made explicit that the polynomial horizontal-substrip growth bound is part
  of the factorized scattering bootstrap datum itself, not a forward
  reference to later form-factor or TBA chapters.
- Recast the bound-state residue in terms of one-particle internal spaces
  \(V_a\), multiplicity spaces \(M_{ab}^e\), and projection/inclusion maps
  \(V_e\leftrightarrows V_a\otimes V_b\), with the sign tied to the chosen
  positive one-particle normalization.
- Derived fusing-angle relations from the complex on-shell momentum identity
  \(p_a(\theta+i\bar u)+p_b(\theta-i\bar u')=p_e(\theta)\).
- Replaced the structural fusion-bootstrap explanation by a small-contour
  residue proof: parametrize the unresolved rapidities near the
  \((a,b)\)-pole, assume the \(ak\) and \(bk\) factors are holomorphic on the
  contour, extract the residue, project to the \(e\)-channel, and identify
  the result with \(S_{ek}\).
- Kept the elementary scalar block proof explicit and moved the prose around
  it so the block identity is presented as a verified algebraic fact rather
  than an asserted property.
- Updated the Volume VI Chapter 2 dossier.

## Verification

- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed; `monograph/tex/main.pdf` was rebuilt
  without log-scan failures.
- `pdfinfo monograph/tex/main.pdf` reports 1269 pages.
