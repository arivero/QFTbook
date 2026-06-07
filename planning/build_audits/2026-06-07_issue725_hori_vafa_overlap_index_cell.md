# Issue #725 Hori--Vafa overlap-index evidence repair

Date: 2026-06-07

## Scope

This pass addresses the #725 critique that
`finite_flux_dirac_index()` in `calculation-checks/susy_2d_lg_glsm_checks.py`
encoded the Fujikawa trace by assigning a chiral dimension mismatch.

The repair is local to the Hori--Vafa determinant/Fujikawa convention cell in
Volume VII Chapter 09.  It strengthens the finite evidence for the sign and
flux convention behind `Tr_reg gamma_*=-Qk`.

## Substantive changes

- Removed the rectangular-identity rank model whose index was determined by
  preselected chiral dimensions.
- Added a finite magnetic-torus regulator with explicit periodic link variables
  and uniform plaquette flux.
- Built the Hermitian Wilson kernel `H_W=gamma_*(D_W-m)` on that flux background
  and computed the overlap index `-1/2 Tr sign(H_W)` from its spectrum.
- Checked both signs of charge and flux, plus the zero-flux control.
- Kept the heat-kernel comparison as the continuum convention target while
  making the finite computation independent of an assigned zero-mode count.
- Updated the monograph, README, evidence contract, and dossier wording to name
  the Wilson-overlap regulator.

## Re-audit boundary

This is finite-regulator evidence for the same convention chain used by the
local determinant calculation.  It does not prove the continuum index theorem,
the full Hori--Vafa operator map, vortex compactness, or mirror-QFT
equivalence.  Those remain separate #847/#848 obligations.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/check_utils_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- Volume VII Chapter 09 theorem-form, unnumbered-display-label,
  certificate-language, strict-text, negative-scope, style-density, and
  directive-leakage audits.
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
