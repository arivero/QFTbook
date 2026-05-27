# Build Audit: SUSY N=2 QCD Superpotential

Date: 2026-05-27

## Scope

- Added an intrinsic QFT section to Volume VII, Chapter 3 deriving the
  four-dimensional N=2 gauge-matter superpotential in N=1 variables.
- Updated the Volume VII, Chapter 3 dossier and the calculation-check index.
- Extended `calculation-checks/susy_gauge_foundation_checks.py` with exact
  finite checks for the N=2 QCD cubic gauge contraction and its
  `2 g_YM^2` F-term coefficient.

## Verification

- `python3 calculation-checks/susy_gauge_foundation_checks.py`
  - Passed: `All supersymmetric gauge-foundation checks passed.`
- `python3 -m py_compile calculation-checks/susy_gauge_foundation_checks.py`
  - Passed.
- `tools/audit_monograph_text.sh`
  - Passed: `Strict monograph text audit clean.`
- `tools/audit_chapter_dossiers.sh`
  - Passed: `Chapter dossier metadata audit clean.`
- `git diff --check`
  - Passed.
- `tools/build_monograph.sh`
  - Passed: monograph build and log scan clean.
  - Output PDF:
    `/Users/xiyin/QFT_susy_gauge_dynamics_localization/monograph/tex/main.pdf`.

## Notes

- A first build exposed a PDF-bookmark warning from the math-heavy section
  title.  The title was changed to use `\texorpdfstring`, and the build was
  rerun successfully.
