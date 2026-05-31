# DR Nonabelian Regular Field-Core Pass

Date: 2026-05-31.

Scope:
- Volume IV, Chapter 4, Doplicher--Roberts reconstruction discussion.
- GitHub issue context: #695 foundational/AQFT quoted-theorem proof debt.

Changes:
- Added a finite nonabelian charged-coordinate model for the categorical
  output of Doplicher--Roberts reconstruction.
- The new text uses \(\operatorname{Fun}(S_3)\) with right translation by
  \(S_3\), so that fixed points are constants and matrix coefficients form
  charged multiplets.
- It displays the right action on matrix coefficients, the Haar conditional
  expectation onto observables, and the multiplication rule identifying
  pointwise products with tensor-product matrix coefficients.
- The paragraph explicitly states the theorem-boundary status: this finite
  model suppresses the local observable algebra and does not prove the full
  DHR field-algebra reconstruction.  It makes the compact-group/charged-field
  output visible before the analytic burden of bounded-region DHR
  localization is imposed.

Companion checks:
- Extended `calculation-checks/dhr_dr_reconstruction_checks.py` with the
  \(S_3\) regular charged-coordinate core.
- The check verifies that right translation rotates matrix-coefficient
  columns, Haar averaging kills the nontrivial standard and sign multiplets
  while preserving constants, and \(\wedge^2 V\) is the sign representation.

Verification:
- `python3 calculation-checks/dhr_dr_reconstruction_checks.py`
- `python3 -m py_compile calculation-checks/dhr_dr_reconstruction_checks.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`

Full-build status:
- `tools/build_monograph.sh` completed cleanly; `main.pdf` rebuilt at 2749 pages.
