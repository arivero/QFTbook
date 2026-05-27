# Build Audit: Volume VII Localization Normal Gaussian

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

## Scope

This pass strengthens Volume VII Chapter 16, `Supersymmetric Localization On
Compact Manifolds`, by making the finite-dimensional normal one-loop model
fully parity-consistent.  The correction is deliberately local: it improves
the finite theorem boundary used by the later \(S^4\) and \(S^3\)
localization formulae without changing their displayed matrix models.

## Substantive Edits

- Replaced the informal normal quadratic expression containing an odd-even
  mixed term with an even quadratic model
  `1/2 x A x - 1/2 theta F theta`.
- Added a finite normal Gaussian proposition proving the local factor
  `Pf(F)/sqrt(det A)` and separating zero modes from the determinant.
- Recorded how a block fermion matrix `[[0,D],[-D^T,0]]` yields an
  orientation-dependent `+- det(D)` Pfaffian.
- Extended `calculation-checks/susy_localization_matrix_checks.py` with exact
  rational determinant/Pfaffian checks and zero-mode detection.
- Updated the Chapter 16 dossier and calculation-check README.

## Verification

- `python3 calculation-checks/susy_localization_matrix_checks.py`: passed.
- `python3 -m py_compile calculation-checks/susy_localization_matrix_checks.py`:
  passed.
- `tools/run_calculation_checks.sh`: passed, including the strengthened
  localization matrix-model check and the Wolfram gamma-trace check.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed.  The rebuilt
  `monograph/tex/main.pdf` has 1857 pages and size 7,402,939 bytes.
