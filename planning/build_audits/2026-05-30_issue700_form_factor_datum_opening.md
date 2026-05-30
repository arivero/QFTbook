# 2026-05-30 Issue #700 Form-Factor Datum Opening Pass

## Target

- GitHub issue: #700.
- Local target: `monograph/tex/volumes/volume_vi/chapter04_form_factor_bootstrap_local_operators.tex`.
- Problem: the chapter used form-factor bootstrap equations before giving a
  defining datum for the local-operator form-factor object.

## Edit

- Added `Definition~\ref{def:form-factor-datum-local-operator}` at the
  chapter opening.
- The datum now contains the operator-valued distribution and scattering
  domain, meromorphic covectors on species spaces, semi-locality monodromies,
  kinematic annihilation-pole data, bound-state residue data, and growth or
  boundary-value bounds.
- Removed the late skeletal definition from the reconstruction section and
  replaced it by a reference back to the upfront datum.
- Updated the Volume VI Chapter 4 dossier so the source map records the new
  logical order.

## Verification

- `git diff --check` clean.
- `python3 tools/audit_theorem_form.py` clean.
- `python3 tools/audit_unnumbered_display_labels.py` clean.
- `tools/audit_negative_scope_prose.py` clean.
- `tools/audit_monograph_text.sh` clean.
- `tools/audit_chapter_dossiers.sh` clean.
- `tools/build_monograph.sh` clean.
- `pdfinfo monograph/tex/main.pdf`: 2683 pages.
