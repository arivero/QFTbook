# Issue #549 Supersymmetric Localization

## Scope

- GitHub issue: `#549`.
- Manuscript locus:
  `monograph/tex/volumes/volume_vii/chapter16_supersymmetric_localization_compact_manifolds.tex`.
- Calculation-check locus:
  `calculation-checks/susy_localization_matrix_checks.py`.

## Content Added

- Added a dedicated compact-space supersymmetric localization chapter in
  Volume VII.
- Proved the finite-dimensional \(Q\)-exact deformation identity with the
  boundary condition and \(Q\)-invariant Berezinian density stated explicitly.
- Stated the regulated QFT localization datum required before an
  infinite-dimensional localization formula is used.
- Added the \(S^4\) \(\mathcal N=2\) Pestun matrix integral in the monograph
  trace-delta gauge convention, including the classical Gaussian,
  vector/hyper one-loop determinants, and north/south Nekrasov factors.
- Added the \(\mathcal N=4\) degeneration to the Gaussian matrix model and
  the \(U(1)\) Gaussian integral.
- Added the \(S^3\) \(\mathcal N=2\) Kapustin-Willett-Yaakov matrix integral,
  including Chern-Simons, FI, vector, and chiral determinant factors.
- Added worked \(U(1)_k\) Chern-Simons Fresnel and conjugate-chiral-pair
  determinant integrals.
- Recorded the theorem boundary for instanton compactifications, noncompact
  Coulomb directions, parity anomaly, framing, contours, and contact terms.
- Added a Volume VII chapter dossier and indexed the calculation check.

## Verification

- `python3 calculation-checks/susy_localization_matrix_checks.py` passed.
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed.
- Independent log scan passed:
  `rg -n "LaTeX Warning: Reference|LaTeX Warning: Citation|Latex failed to resolve|Undefined control sequence|Overfull|Underfull|Fatal error|Emergency stop|Missing .* inserted|Token not allowed" monograph/tex/main.log monograph/tex/build/latexmk.out`
  returned no matches.
- `pdfinfo monograph/tex/main.pdf` reports `Pages: 1447`.
