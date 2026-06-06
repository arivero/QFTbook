# 2026-06-06 Issue 630 Quasi-PDF Inverse-Matching Audit

## Scope

- Added `ca:qcd-quasi-pdf-finite-momentum-inverse-matching` to Volume II
  Chapter 19 after the quasi-/pseudo-PDF scheme-covariance paragraph.
- Extended `calculation-checks/qcd_quasi_pdf_matching_checks.py` with an
  evidence contract and a finite inverse-matching check.
- Updated the calculation-check README, evidence-contract manifest, and Ch19
  dossier.

## Depth Audit

- This pass is a physics-extraction pass, not a new notation layer.  It asks
  when Euclidean equal-time Wilson-line data can be turned into tested
  light-ray PDF bins.
- The monograph now requires a finite matching matrix, a declared stable left
  inverse, omitted-test-space residuals, finite-momentum power corrections,
  regulator/window errors, and ensemble errors before a quasi-PDF coordinate
  is read as a lightcone PDF bin.
- The companion exact model verifies stable inverse matching and residual
  propagation, and rejects raw quasi-bin reading, singular matching matrices,
  omitted residual budgets, and treating quasi-coordinate negativity as PDF
  negativity.

## Scope Guard

- The finite check is a normalization/stability regression model for the
  matching algebra.  It is not independent evidence for the continuum LaMET
  theorem, lattice continuum limit, infinite-volume limit, or nonperturbative
  existence of light-ray PDFs.
- Planning/process notes remain in planning files; monograph TeX contains only
  the technical QCD content.
