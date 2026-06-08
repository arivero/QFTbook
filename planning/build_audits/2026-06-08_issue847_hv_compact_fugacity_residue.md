# Issue #847 Hori--Vafa Compact Fugacity Residue Audit

## Scope

- Tightened `rem:cpn-hv-residue-instanton-cross-check` in Volume VII Ch09 so
  the mirror residue coordinate \(q_{\rm mir}\) is explicitly the transported
  image of the same compact FI character as the direct vortex coordinate
  \(q_\Lambda\).
- Added the same-line mismatch
  \(\delta T_q=T_\Lambda-T_{\rm mir}+
  \sum_i(\log c_{i,\Lambda}-\log c_i^{\rm mir})\) and recorded that
  \(q_\Lambda-q_{\rm mir}\) belongs to the FI-coordinate residual \(B_q\)
  whenever the two coordinates are not transported together.
- Added a companion finite check rejecting stale bare mirror fugacities after
  coefficient transport, period-one `exp(tau)` drift, and omitted
  \(q\)-transport residuals in the degree-one residue/direct-instanton
  comparison.

## Architecture Re-Audit

- Old interrupted route: the critical-point equation had been moved to the
  transported \(q_{\rm phys}\) coordinate, but the later residue/direct-vortex
  comparison still allowed \(q_{\rm mir}\) to look like an independently chosen
  mirror-residue fugacity.
- New canonical route: the residue comparison first types \(q_{\rm mir}\) and
  \(q_\Lambda\) as the same compact FI character, then compares the mirror root
  sum with the direct incidence/Berezin/contact package plus the retained
  measure and operator residuals.
- Physics-depth check: this is a convention-and-measure-interface repair, not
  a new moduli-space cell.  It protects the direct amplitude comparison from
  hidden FI-coordinate drift while leaving the hard fluctuation determinant,
  vortex-regulator, and operator-map inputs visible.
- Unresolved theorem boundary: the pass does not prove the full Hori--Vafa
  mirror QFT, the continuum vortex limit, the nonzero-mode determinant, or the
  original-to-mirror source/operator theorem.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail --limit 40`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 -m json.tool calculation-checks/evidence_contracts.json`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
