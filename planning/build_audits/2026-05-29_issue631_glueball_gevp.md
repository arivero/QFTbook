# 2026-05-29 Issue #631 Glueball GEVP Pass

## Scope

- Added a finite-regulator glueball GEVP section to Volume XI Chapter 5.
- Defined vacuum-subtracted gauge-invariant time-slice sources, the connected
  correlator matrix, and its transfer-matrix spectral representation.
- Proved exact finite-state GEVP extraction when the chosen source space
  resolves finitely many transfer-matrix eigenvectors with invertible overlap.
- Added a whitened residual criterion using Weyl's inequality to make plateau
  claims into controlled finite-matrix statements.
- Added `qft_scripts/glueball_gevp_from_correlators.py`, a reader-facing
  script for CSV correlator matrices with an exact two-state smoke test.
- Updated the Volume XI Chapter 5 dossier, script README, smoke runner, and
  `claude_review.md` #631 ledger.

## Verification

- `python3 qft_scripts/glueball_gevp_from_correlators.py --smoke`
- `python3 calculation-checks/qcd_glueball_spectrum_checks.py`
- `python3 -m py_compile qft_scripts/glueball_gevp_from_correlators.py calculation-checks/qcd_glueball_spectrum_checks.py`
- `git diff --check`
- `bash -n tools/run_qft_scripts_smoke.sh`
- `python3 tools/audit_theorem_form.py`
- `bash tools/audit_chapter_dossiers.sh`
- `bash tools/build_monograph.sh` (clean; `monograph/tex/main.pdf` at 2555
  pages)
