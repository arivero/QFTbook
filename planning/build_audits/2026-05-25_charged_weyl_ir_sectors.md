# Charged Weyl IR-Sector Development Audit

## Scope

This pass advances GitHub issues #527 and #528 without claiming to solve the
full nonperturbative charged-sector Haag--Ruelle theorem.  The added content
develops the representation-theoretic input behind Wilson-line and
Faddeev--Kulish charged dressings:

- finite-cutoff photon Weyl algebra;
- coherent-state characteristic functional for a charged soft cloud;
- proof that Weyl implementers changing between distinct charged velocities
  have no strong operator limit and no nonzero weak operator limit as the
  infrared cutoff is removed;
- calculation-check support for the Weyl/coherent formulas.

## Edits

- Expanded
  `monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`
  with the subsection "Weyl Implementation and the Failure of a Common Photon
  Fock Space".
- Added Proposition `prop:no-common-fock-implementer-distinct-velocities`,
  proving from the logarithmic soft coherent norm divergence that distinct
  charged velocities cannot be implemented as a limiting Weyl displacement on
  one fixed photon Fock representation.
- Extended `calculation-checks/charged_flux_dressing_checks.py` to verify the
  finite-dimensional Weyl/coherent characteristic functional and the monotone
  decay of the coherent overlap as the infrared cutoff is removed.
- Updated the Volume IV Chapter 5 dossier with the new symbols, claim, and
  calculation-check coverage.

## Verification

- `python3 calculation-checks/charged_flux_dressing_checks.py`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 1306 pages.

## Issue Status

Issues #527 and #528 should remain open.  The monograph now proves another
necessary structural ingredient: charged velocities with distinct angular
flux data cannot be represented inside one ordinary photon Fock space by an
infrared-limit Weyl unitary.  The still-open theorem is the full
nonperturbative charged-sector Haag--Ruelle/LSZ construction with noncompact
gauge-invariant charged creators and the required large-time estimates.
