# Issue #848 Noncompact D-Term Boundary Phase Diagnostic

Date: 2026-06-07

## Scope

This pass advances the #848 full mirror-QFT lane for Volume VII Chapter 09.
It targets the residual weakness that finite-field Kahler/D-term and
noncompact boundary data were named as obligations, but the reader still needed
a concrete spectral reason why they are physical data rather than decorative
metadata.

## Source/Recheck Inputs

- Refreshed #848 and #847 issue comments after commit `736c8dc1`.
- Confirmed `claude_review.md` had no new update and that the saved monitor
  automations remained paused.
- Rechecked the stringbook Appendix K source ranges cited by #848, especially
  the abelian dual action, the `Re(Y)>0` domain and induced-measure/anomaly
  warning, the intermediate cigar dual D-term action, and the limited
  Hori--Kapustin conclusion that finite-field `K(Y,bar Y)` remains unknown.

## Substantive Repair

- Added a half-line radial scattering diagnostic to the cigar/Liouville QFT
  comparison: with Robin wall condition `psi'(0)=lambda psi(0)`, the exact
  reflection factor
  `R_lambda(p)=(lambda+i p)/(i p-lambda)` has unit modulus but changes the
  continuous density by `lambda/(pi(lambda^2+p^2))`.
- Connected this diagnostic to noncompact D-term total derivatives:
  `int_0^infty dJ = J(infty)-J(0)` can retain the wall current rather than
  vanish.
- Strengthened `susy_2d_lg_glsm_checks.py` so the finite companion checks the
  Robin boundary equation, unitary reflection, nonzero phase-density shift, and
  rejection of boundary-blind Liouville data.
- Updated the README, evidence contract, and chapter dossier to classify this
  as a noncompact D-term boundary reflection diagnostic.

## Re-Audit Boundary

This is a physics diagnostic for why `K`, measure, and boundary conditions are
part of the full noncompact QFT datum.  It is not a derivation of the actual
cigar/Liouville reflection amplitude from the Liouville path integral, not a
proof of finite-field Kahler control, not a proof of Hori--Kapustin global
uniqueness, and not an operator/state-map or boundary-state matching theorem.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- Volume VII Chapter 09 theorem-form, unnumbered-display-label,
  certificate-language, strict-text, negative-scope, style-density, and
  process-leakage audits.
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
- `git diff --check`
