# Volume I Chapter 3 Local-Field Formalization Follow-Up

Date: 2026-05-27.

Files:

- Chapter 3 TeX source.
- Chapter 3 dossier.

Scope:

- Promoted the operator-valued distribution datum, localization of smeared
  fields, Poincare pullback on test functions, homogeneous parity and graded
  commutator, local polynomial field algebra, and Wightman distribution into
  labeled definitions.
- Added proof blocks for distributional product matrix elements,
  infinitesimal translation covariance, covariance of localization regions,
  Poincare invariance of spacelike support separation, isotony and graded
  locality of polynomial field algebras, and inheritance of covariance and
  locality by Wightman distributions.
- Preserved the chapter's convention that point-field notation is shorthand
  for smeared distributional matrix elements on a common invariant domain.

Verification:

- `python3 calculation-checks/local_field_covariance_checks.py`
- `python3 -m py_compile calculation-checks/local_field_covariance_checks.py`
- targeted ASCII scan on the edited chapter/dossier/audit
- targeted weak-language scan on the edited chapter/dossier/audit
- targeted long-line scan on the edited chapter/dossier/audit
- `git diff --check` on edited files
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`
