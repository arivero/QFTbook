# Issue #527 Flux-Sector LSZ Projection Pass

## Scope

This pass strengthens Volume IV Chapter 5 at the dressed Wilson-line LSZ
interface.  The chapter already separated boundary-charge neutrality from the
full angular Gauss-law flux profile; the new prose block connects that
distinction directly to simultaneous external-shell residue extraction.

The added manuscript block states that dressed LSZ residues are block diagonal
in angular flux characters.  A vacuum-to-vacuum residue must match the full
signed angular flux profile, while zero total charge only tests the constant
mode.  Finite same-flux coordinate changes act inside one residue block; a
matrix mixing different angular-flux characters is a sector change, not a
harmless dressing-coordinate transformation.

## Companion Check

`calculation-checks/charged_flux_dressing_checks.py` now includes
`check_flux_sector_projection_in_dressed_lsz()`.  The finite check verifies:

- opposite charges at the same velocity have zero sampled angular flux and
  are accepted in the vacuum flux block;
- opposite charges at distinct velocities have zero total charge but a
  nonzero sampled angular flux profile;
- a charge-only selector would accept that distinct-velocity pair, while the
  angular-flux selector rejects it from the vacuum residue;
- the same finite residue is accepted as a sector-changing flux matrix
  element;
- a finite same-flux coordinate change preserves the selected LSZ coefficient.

## Verification

- `python3 calculation-checks/charged_flux_dressing_checks.py`
- `python3 -m py_compile calculation-checks/charged_flux_dressing_checks.py`
- `tools/run_calculation_checks.sh --python-only --only charged_flux`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_iv/chapter05_haag_ruelle_and_mathematical_scattering.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `python3 tools/audit_style_density.py --root monograph/tex --window 120 --stride 60`
- `tools/build_monograph.sh`

The full build completed clean and produced
`monograph/tex/main.pdf` at 3397 pages.  The broad style-density scan reported
only existing density clusters outside this Ch05 pass.
