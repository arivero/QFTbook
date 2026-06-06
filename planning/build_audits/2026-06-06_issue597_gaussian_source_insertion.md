# Issue #597 Gaussian Source-Insertion Estimator

Date: 2026-06-06

## Scope

This pass addresses the instanton-physics depth concern at the nonzero-mode
fluctuation layer.  It does not add moduli-space infrastructure.  Instead, it
turns the source-dependent fluctuation quotient into a finite Gaussian
source-insertion estimator before any continuum limit.

The manuscript insertion is
`ca:instanton-finite-gaussian-source-insertion`.  It records:

- the exact quotient
  \(\langle(1+U_z)e^{-V_z}\rangle_\gamma/
    \langle e^{-V_z}\rangle_\gamma\);
- the covariance identity separating source mean from interaction covariance;
- the quadratic normal-mode source trace
  \(\frac12\operatorname{Tr}(Q_zC_z)\);
- the Cauchy majorant
  \(\epsilon_U+M_UM_V/d_0\);
- the zero-saddle-source case where an absolute insertion replaces the
  relative quotient.

This keeps the amplitude object centered on the same hard part emphasized by
the original one-instanton four-point calculation: the determinant normalizes
the fluctuation measure, but the chosen source still has to be integrated and
bounded against that measure.

## Evidence Companion

`calculation-checks/bpst_instanton_normalization_checks.py` now includes
`check_finite_gaussian_source_insertion_estimator()`.  The check verifies:

- the finite covariance identity for determinant average, source mean, and
  interaction covariance;
- the Cauchy covariance bound and its residual form;
- a constant determinant-weight negative control, where the source mean still
  survives;
- the quadratic normal-mode trace correction in an exact rational covariance
  matrix.

## Verification

- `python3 -m py_compile calculation-checks/bpst_instanton_normalization_checks.py`
- `python3 calculation-checks/bpst_instanton_normalization_checks.py`
- `tools/run_calculation_checks.sh --python-only --only bpst_instanton_normalization_checks`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `tools/build_monograph.sh`

The full build completed clean and produced
`monograph/tex/main.pdf` at 3398 pages.
