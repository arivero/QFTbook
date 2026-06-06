# 2026-06-06 Issue 630 Quasi-PDF Primal/Dual Projection Audit

## Scope

- Repaired `ca:qcd-quasi-pdf-finite-momentum-inverse-matching` in Volume II
  Chapter 19 so the finite inverse datum uses separate primal reconstruction
  functions and dual coefficient functionals.
- Extended `calculation-checks/qcd_quasi_pdf_matching_checks.py` with a
  nonorthogonal finite trial-space regression before the left-inverse residual
  check.
- Updated the calculation-check README and Chapter 19 dossier.

## Depth Audit

- The repair keeps the physics target fixed: Euclidean equal-time spatial
  data become light-ray PDF bins only after a declared projection, matching
  matrix, stable inverse, and residual budget.
- The chapter no longer hides an orthonormal/self-dual basis assumption.  The
  matching matrix acts on the primal functions \(\psi_\ell\), while the PDF
  coordinates are coefficients against the dual functionals \(\phi^\ell\).
- The finite checker now rejects the shortcut in which nonorthogonal primals
  are used as their own duals.  It also shows the Gram-corrected coordinate
  matrix needed if one insists on self-pairing coordinates.

## Scope Guard

- This is a definition and extraction repair, not a proof of the continuum
  LaMET theorem, light-ray PDF existence, or the lattice continuum limit.
- Planning/process notes remain in planning files; the monograph TeX contains
  only the technical QCD content.
