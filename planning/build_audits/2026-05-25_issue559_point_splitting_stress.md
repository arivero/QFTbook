# 2026-05-25 Issue 559: Point-Splitting Stress-Tensor Computation

## Scope

Issue #559 flagged that Volume XII Chapter 2 defined point-splitting stress
tensor renormalization but did not display a worked computation.

## Edits

- Added a flat-space worked computation for the massless real scalar in
  four-dimensional Minkowski spacetime.
- Displayed the vacuum two-point function and the flat Hadamard subtraction
  \(H_0=W_0\), giving zero vacuum stress tensor after the finite flat
  cosmological term is set to zero.
- Displayed the smooth thermal KMS remainder \(\Delta W_\beta=W_\beta-W_0\).
- Wrote the explicit bidifferential operators for \(T_{00}\) and \(T_{ij}\).
- Applied them to plane waves and evaluated the Bose integral to obtain
  \(\rho_\beta=\pi^2/(30\beta^4)\), \(p_\beta=\rho_\beta/3\), and zero trace.
- Added a constant-curvature de Sitter diagnostic for the massless
  conformally coupled scalar, using the four-dimensional anomaly
  coefficients and de Sitter curvature invariants to obtain
  \(\langle T_{\mu\nu}\rangle=-H^4(960\pi^2)^{-1}g_{\mu\nu}\) in the stated
  convention.
- Added `calculation-checks/point_splitting_stress_checks.py` to verify the
  finite integrals, plane-wave differential-operator identities, and
  de Sitter curvature/anomaly arithmetic.
- Updated the Volume XII Chapter 2 dossier and calculation-check README.

## Targeted Verification

- `python3 calculation-checks/point_splitting_stress_checks.py`

## Repository Verification

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`

The first build pass caught an overfull line in the new de Sitter paragraph;
the sentence was shortened and the rerun completed cleanly.  The rebuilt PDF
has 1287 pages.
