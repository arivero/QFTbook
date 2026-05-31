# 2026-05-31 Notation and Convention Guide Seed

Scope: issue #701, item A2.

Changes:

- Added `monograph/tex/notation_guide.tex` as a reader-facing backmatter guide
  to stable notation and recurrent convention choices.
- Inserted the guide before the bibliographic guide in `monograph/tex/main.tex`.
- Covered global spacetime conventions, Hilbert-space/operator-algebra
  notation, correlation/scattering/spectral symbols, path-integral and RG
  symbols, gauge/BV notation, CFT/integrability/thermal symbols, and
  constructive/lattice/stochastic symbols.
- Added an overload-warning section for symbols whose meaning must be
  declared locally: `Delta`, `S`, `Z`, `Gamma`, `rho`, `beta`, `Lambda`,
  `mathcal F`, `G`, and `K`.
- Updated `planning/12_strict_writing_harness.md` to state explicitly that the
  backmatter guide is a navigation layer and consistency check, not a
  replacement for local first-use definitions.
- Updated `claude_review.md` so #701 records A2 as partially addressed while
  leaving the full index/glossary/nomenclature expansion open.

The pass intentionally does not claim to close #701.  The guide is a seed:
later passes should expand it as further persistent conventions stabilize,
and a proper index/glossary/nomenclature system remains a separate project.
