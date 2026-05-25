# Issue 424: Translation Generator Sign Convention

Date: 2026-05-24.

Issue:

- GitHub #424 flagged an apparent contradiction between the opening
  translation convention and the Wightman framework chapter that
  cross-references it.

Fix:

- Made the opening convention explicit:
  \(U(a,1)=\exp(i a_\mu P^\mu)=\exp(i a^\mu P_\mu)\).
- Stated that the spectrum condition is imposed on the contravariant
  energy-momentum \(P^\mu\), while \(P_\mu=\eta_{\mu\nu}P^\nu\) is used when
  the translation parameter is written with an upper index.
- Added the time-translation check
  \(U(a^0,\vec0)=\exp(-i a^0P^0)\), with \(P^0\) the Hamiltonian.
- Mirrored the same convention in the Wightman chapter and in nearby recalled
  Poincare-convention passages.
- Updated the affected chapter dossiers.

Verification:

- `rg -n -F "exp(-\\ii a" monograph/tex/volumes` finds only the explicit
  positive-time-translation checks \(\exp(-i a^0P^0)\), not an opposite
  translation-generator convention.
- `rg -n -F "P=(P_0" monograph/tex/volumes` finds no remaining covariant-index
  spectral-vector declaration.
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 784 pages.
