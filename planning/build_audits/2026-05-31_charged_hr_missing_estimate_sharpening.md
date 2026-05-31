# Charged Haag--Ruelle Missing-Estimate Sharpening

Date: 2026-05-31

Files touched:

- `monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`
- `planning/chapter_dossiers/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.md`

Purpose:

- Tighten the charged-sector Haag--Ruelle/LSZ discussion for issues #527 and
  #528 without pretending that the full nonperturbative theorem has been
  proved.
- Make explicit that the obstruction is not merely the absence of a convenient
  local charged field.  If an operator is almost local with respect to the
  gauge-invariant observable net, the closed Gauss-law charge still forces its
  vacuum vector to be neutral.
- Replace the compressed "missing estimate" prose by the actual estimate
  package a charged theorem would need: dressed creators labelled by charge,
  dressing geometry, limiting flux and multiplicity data; a velocity-separated
  exchange relation with possible Dollard/Faddeev--Kulish phase; a modified
  Cook estimate after subtracting the comparison phase; and scalar-product
  limits in the appropriate asymptotic representation.

Mathematical boundary:

- The new almost-local obstruction is a theorem under the displayed closedness
  and domain hypotheses for the Gauss-law charge.
- The charged exchange and modified Cook estimates are not asserted as known
  gauge-theory theorems.  They are stated as the precise analytic content
  required to complete the nonperturbative charged Haag--Ruelle construction.

Verification:

- `python3 calculation-checks/charged_flux_dressing_checks.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`, clean, `main.pdf` at 2698 pages.
