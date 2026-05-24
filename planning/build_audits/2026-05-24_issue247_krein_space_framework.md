# Issue 247 Krein Space Framework

Date: 2026-05-24

Scope:
- Strengthened
  `monograph/tex/volumes/volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex`.
- Updated
  `planning/chapter_dossiers/volume_ii/chapter18_gauge_fixing_ghosts_brst.md`.
- Addressed GitHub issue #247 on naming and defining the Krein-space framework
  for covariant gauge quantization.

Changes:
- Added a dedicated Krein-space foundations section before the BRST state
  cohomology construction.
- Defined the fundamental decomposition
  \(\mathcal K=\mathcal K_+\oplus\mathcal K_-\), the fundamental symmetry
  \(J\), the Hilbert majorant inner product, and the Krein adjoint
  \(T^\times\).
- Stated explicit BRST domain hypotheses: a dense invariant domain,
  closed odd ghost-number-one \(Q\), \(Q^2=0\) on the domain, and
  \(Q\subset Q^\times\), with Krein self-adjoint closure separated from
  formal Hermiticity.
- Added proof/source references to Bognar, Dollard--Friedman, and
  Strocchi--Wightman/Strocchi.
- Updated the dossier symbols and claims so \(\mathcal K\) is recorded as a
  Krein state space rather than merely an indefinite inner-product space.

Verification:
- `git diff --check` clean.
- `tools/audit_monograph_text.sh` clean.
- `tools/audit_chapter_dossiers.sh` clean.
- `tools/build_monograph.sh` clean; rebuilt
  `monograph/tex/main.pdf`.
