# Charged LSZ Residue-Coordinate Pass

Date: 2026-06-01

Scope:

- `monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`
- `calculation-checks/charged_flux_dressing_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.md`

Purpose:

Issue #527 asks for a genuine Wilson-line/dressed LSZ framework, while also
warning against closing the full charged Haag--Ruelle theorem prematurely.
This pass adds a finite-regulator residue-coordinate synthesis rather than a
new theorem.  The text now defines the one-particle overlap map from a
physical charged shell to a finite family of dressed noncompact charged
interpolating operators, identifies the two-point pole residue as the Gram
matrix of this overlap map, and explains that normalized charged LSZ
extraction is a left-inverse operation on these coordinates.

Logical boundary:

- Same charged shell and same asymptotic Gauss-law flux: a finite invertible
  change of dressed operator coordinates sends \(z\mapsto Mz\),
  \(Z\mapsto MZM^\dagger\), and \(L\mapsto LM^{-1}\), leaving the extracted
  residue invariant.
- Different asymptotic ray or Coulomb tail in an unscreened Gauss-law theory:
  not a finite coordinate change on a common one-particle Hilbert shell.  The
  soft-sector sections below are still the relevant obstruction, and the full
  nonperturbative charged Haag--Ruelle/LSZ theorem remains open.

Calculation companion:

- `charged_flux_dressing_checks.py` now includes an exact rational check that
  the residue matrix \(Z=z z^T\) is rank one in a one-dimensional charged
  shell, that a left inverse extracts the external amplitude, and that the
  extraction is invariant under an invertible finite coordinate change.

Verification:

- `python3 calculation-checks/charged_flux_dressing_checks.py`
- `python3 -m py_compile calculation-checks/charged_flux_dressing_checks.py`
- `tools/run_calculation_checks.sh --list --only charged_flux`
- `tools/run_calculation_checks.sh --python-only --only charged_flux`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

Build result:

- Clean log scan.
- `monograph/tex/main.pdf` built successfully at 2836 pages.
