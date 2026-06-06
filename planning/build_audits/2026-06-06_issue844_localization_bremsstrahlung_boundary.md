# Issue 844 Localization Bremsstrahlung Boundary Build Audit

## Scope

- Rewrote the Volume VII Ch16 protected-insertion passage after the Pestun
  formula from process-facing proof-obligation language into a
  QFT-to-matrix-model comparison for protected observables.
- Kept the five-residual comparison identity
  `Z_reg - Z_loc = E_Stokes + E_normal + E_res + E_inst + E_cont`, while
  making its role explicit: residual estimates are the bridge from the
  regulated QFT functional to the localized matrix-model functional.
- Strengthened the circular Wilson-loop/Bremsstrahlung discussion by separating
  the localized Bessel derivative from the two field-theory inputs needed to
  read it as a physical radiation/small-angle cusp coefficient: the protected
  Ward identity and the residual comparison.
- Extended `calculation-checks/susy_localization_matrix_checks.py` with a
  Bremsstrahlung Bessel-derivative check, a missing-prefactor negative control
  detecting the spurious `1/(4*pi^2)` shift, and a weak-coupling cubic
  truncation check.
- Updated the calculation README and Ch16 dossier to record the new observable
  boundary and executable check.

## Verification

- `python3 -m py_compile calculation-checks/susy_localization_matrix_checks.py`
- `python3 calculation-checks/susy_localization_matrix_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_localization_matrix`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter16_supersymmetric_localization_compact_manifolds.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter16_supersymmetric_localization_compact_manifolds.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter16_supersymmetric_localization_compact_manifolds.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter16_supersymmetric_localization_compact_manifolds.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
- `git diff --check`

All selected checks passed.  Wolfram Language checks were not selected.  The
full monograph build/log scan was clean at 3452 pages.

## Re-audit Notes

- This is a physics-depth cleanup rather than another localization or ADHM
  lemma cell: it makes the physical observable boundary explicit at the point
  where the chapter passes from the localized Wilson loop to the
  Bremsstrahlung/cusp coefficient.
- The edit reduces coherence drift by replacing planning vocabulary in the TeX
  surface with reader-facing QFT comparison language.
- The new executable check targets a convention-sensitive physical failure
  mode: differentiating `I_1(sqrt(lambda))` without the `2/sqrt(lambda)`
  prefactor produces a definite wrong shift in the Bremsstrahlung coefficient.
- No directive, monitoring, or GitHub-process language was added to the
  monograph TeX.
