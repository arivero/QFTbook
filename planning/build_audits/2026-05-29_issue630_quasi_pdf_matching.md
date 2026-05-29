# 2026-05-29 Issue #630 Quasi-/Pseudo-PDF Matching Pass

## Scope

Advanced the QCD rigor-uplift issue by adding a finite-regulator treatment of
Euclidean equal-time spatial bilocals, quasi-PDF coordinates, pseudo-Ioffe-time
coordinates, and the status of large-momentum matching.

## Manuscript Changes

- `monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`
  now distinguishes the nonperturbative light-ray PDF definition from
  Euclidean spatial-bilocal matrix elements used for lattice access.
- Added the regulated spatial Wilson-line operator
  \(\mathcal Q_\Gamma(z;\Lambda)\) and proved its gauge invariance by endpoint
  cancellation.
- Defined quasi-PDF and pseudo-Ioffe-time coordinates with explicit Fourier
  normalization and Ioffe-time conventions.
- Stated large-momentum matching as a `controlledapproximation`, not as a
  theorem: the formula is distributional against test functions and records
  hadron-mass, higher-twist, lattice-spacing, finite-volume, and endpoint
  qualifications.
- Added a finite matching-kernel scheme-covariance lemma, including the
  charge-preserving column-sum condition.

## Calculation Checks

- Added `calculation-checks/qcd_quasi_pdf_matching_checks.py`.
- The check covers:
  - the Fourier prefactor/inversion convention in a finite Fourier model;
  - cancellation of multiplicative spatial-Wilson-line factors in reduced
    pseudo-Ioffe-time ratios;
  - finite light-ray scheme covariance of matching kernels;
  - quark-number preservation from matching-kernel column sums.

## Review Ledger

- Updated `calculation-checks/README.md`.
- Updated the Volume II Chapter 19 dossier.
- Updated `claude_review.md` so the #630 row no longer lists lattice
  quasi-/pseudo-PDF matching as untouched; #630 remains open because other QCD
  subclusters still require full development.

## Verification

- `python3 calculation-checks/qcd_quasi_pdf_matching_checks.py`: passed.
- `python3 -m py_compile calculation-checks/qcd_quasi_pdf_matching_checks.py`:
  passed.
- `python3 tools/audit_theorem_form.py`: passed.
- `bash tools/audit_chapter_dossiers.sh`: passed.
- `bash tools/build_monograph.sh`: passed; generated
  `monograph/tex/main.pdf` with 2550 pages and clean log scan.
