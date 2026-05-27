# 2026-05-27 QCD HQET Current Symmetry Audit

## Scope

- Added a Volume II Chapter 19 section on heavy-light and heavy-to-heavy HQET
  currents.
- Fixed the current normalization to use the monograph mostly-plus spinor
  convention: Hermitian vector and axial currents carry an explicit factor of
  \(\ii\).
- Derived the QCD/HQET residual-state normalization relation and the
  leading \(f_H\sqrt M\) scaling law.
- Defined the recoil variable \(w=-v\cdot v'\), the leading Isgur-Wise
  function, and the zero-recoil normalization from the heavy-flavor Noether
  charge.
- Added `calculation-checks/qcd_hqet_current_checks.py` for finite convention
  checks of the displayed normalization algebra.

## Checks

- `python3 calculation-checks/qcd_hqet_current_checks.py`: passed.
- `python3 -m py_compile calculation-checks/qcd_hqet_current_checks.py`:
  passed.
- `git diff --check` on the touched files: passed.
- `tools/build_monograph.sh`: passed with clean strict text audit and clean
  final log scan.
- `pdfinfo monograph/tex/main.pdf`: 2167 pages, created
  2026-05-27 11:13 EDT.
