# 2026-06-01 SoV Local Shift Pass

## Scope

Volume VI, Chapter 5B had a separated-variable section that stated the
one-coordinate Baxter equation but did not display the RTT component algebra
that moves a single zero of \(B(u)\).  This pass adds the local \(AB/DB\)
relations and evaluates them at \(u=x_\alpha\), making the shift
\(x_\alpha\mapsto x_\alpha\mp i\) an explicit finite-chain consequence of
the RTT algebra.

## Manuscript Changes

- Added the paragraph `Local RTT shift algebra` in
  `monograph/tex/volumes/volume_vi/chapter05b_nested_tba_tq_relations_and_separation_variables.tex`.
- Derived the shifted \(B(v)\)-eigenvalue factors for
  \(\bra{\boldsymbol x}A(x_\alpha)\) and
  \(\bra{\boldsymbol x}D(x_\alpha)\).
- Rewrote the finite-chain SoV reduction so the separated Baxter equation
  follows from the displayed covector normalization rather than from an
  implicit slogan about separated coordinates.
- Added a companion calculation check for the single-zero shift factors in
  `calculation-checks/nested_integrability_checks.py`.
- Updated the calculation-check ledger and chapter dossier.

## Verification

- `python3 calculation-checks/nested_integrability_checks.py`: passed.
- `python3 -m py_compile calculation-checks/nested_integrability_checks.py`: passed.
- `git diff --check`: passed.
- `python3 tools/audit_theorem_form.py`: passed.
- `python3 tools/audit_unnumbered_display_labels.py`: passed.
- `tools/audit_negative_scope_prose.py`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; rebuilt
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`:
  `Pages:           2807`.
