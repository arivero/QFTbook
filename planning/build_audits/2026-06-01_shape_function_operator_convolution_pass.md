# Shape-Function Operator And Convolution Pass

Date: 2026-06-01.

Scope:

- Addressed part of GitHub issue #526 in
  `monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex`.
- Replaced the short phenomenological shape-function paragraph with a leading
  shape-function operator datum, distributional endpoint-convolution
  controlled approximation, normalization and first-moment diagnostics, and
  finite scheme-translation bookkeeping.
- Added a lattice/reconstruction matching caveat for lightlike Wilson-line
  shape coordinates.
- Added `calculation-checks/shape_function_convolution_checks.py`.

Verification:

- `python3 calculation-checks/shape_function_convolution_checks.py`
- `python3 -m py_compile calculation-checks/shape_function_convolution_checks.py`
- `tools/run_calculation_checks.sh --list | rg -n "selected Python|selected Wolfram|shape_function"`
  reported 215 selected Python checks, the new shape-function script, and 2
  Wolfram Language checks, for 217 active checks total.
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`, clean log scan; `main.pdf` builds at 2824 pages.

Status:

- This pass advances #526's nonperturbative shape-function requirement.
- The issue remains open for measured-function-specific grooming proofs,
  explicit resummation examples, and deeper shape/operator treatments beyond
  the leading single-soft-coordinate endpoint convolution.
