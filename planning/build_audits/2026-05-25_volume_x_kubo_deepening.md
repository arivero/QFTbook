# Volume X Kubo Deepening Audit

## Scope

This pass addresses the later-volume thinness directive in Volume X by
substantially expanding the Kubo/transport chapter.  The focus is not a new
topic wrapper, but a proof-level clarification of the finite-volume spectral
representation, KMS fluctuation--dissipation, contact terms, and transport
sign conventions.

## Edits

- Rewrote
  `monograph/tex/volumes/volume_x/chapter04_spectral_functions_kubo_transport.tex`
  into a fuller derivation.
- Added the finite-volume Lehmann representation with explicit Boltzmann
  weights and the positivity statement \(\omega\rho_{AA}\ge0\).
- Added the retarded spectral representation and fixed the sign convention
  \(\rho=-2\operatorname{Im}G^R\), making the shear-viscosity Kubo formula
  consistent with the thermal-foundations chapter.
- Added a separate contact-term section distinguishing the commutator
  spectral measure from the full background-source response kernel.
- Expanded conductivity, shear viscosity, and bulk viscosity with explicit
  order of limits, Drude-weight warnings, and conserved-density projection.
- Added a subtracted dispersion-relation boundary statement.
- Added `calculation-checks/thermal_kubo_checks.py` and documented it in
  `calculation-checks/README.md`.
- Updated the Volume X Chapter 4 dossier with new symbols, claims, and the
  calculation-check companion.

## Verification

- `python3 calculation-checks/thermal_kubo_checks.py`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean rebuild with log scan.
- `pdfinfo monograph/tex/main.pdf`: 1311 pages, generated 2026-05-25.
