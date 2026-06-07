# 2026-06-07 Issue #844 Forward Positivity Subtracted Measure

## Scope

- Responds to the fresh #844 review that the forward-positivity section treated
  \(\sigma_{\rm abs}^{\rm sub}\) as positive by notation after permitting
  infrared, inclusive, or long-distance subtractions.
- Keeps the repair in the physics of observable amplitudes: a positivity bound
  is a statement about a Hilbert-space absorptive measure for the declared
  observable, not about a formal subtraction label.

## Changes

- Strengthened `hyp:forward-scalar-positivity-ledger` in Volume II Chapter 16.
  Any subtraction with support on the physical cut must now supply its own
  positivity proof.
- Distinguished four cases in the text:
  - no-cut first-sheet pole or local subtractions, where the cut measure is
    unchanged;
  - positive spectral-window splits, where the retained UV measure is positive
    by construction;
  - inclusive/regulator observables with an optical theorem for the regulated
    measured final-state sum;
  - generic long-distance amplitude subtractions, whose discontinuity can be a
    signed measure and therefore cannot feed \(T(S_0)\ge0\).
- Updated `calculation-checks/eft_prediction_calculus_checks.py` with a
  positive spectral-window split, a positive inclusive measurement window, a
  signed measurement-kernel rejection, and a cut-supported oversubtraction
  negative control.
- Updated the calculation README and the Volume II Wilsonian/EFT dossier so the
  evidence boundary records positivity-preserving subtraction as an explicit
  hypothesis.

## Quality Re-Audit

- The repair deepens the physical interpretation of the positivity bound rather
  than adding an adjacent lemma.  The issue is whether the object entering the
  dispersion integral is a positive Hilbert-space observable measure.
- The section still treats forward positivity as a conditional UV-completion
  consistency test after the EFT prediction datum is specified.  It does not
  turn a generic EFT coefficient into an unconditional sign constraint.
- The companion remains finite and adversarial: it checks the algebraic
  normalization and supplies a concrete signed-subtraction failure mode, without
  claiming to construct the continuum scattering amplitude.

## Verification

- `python3 -m py_compile calculation-checks/eft_prediction_calculus_checks.py`
- `python3 calculation-checks/eft_prediction_calculus_checks.py`
- `tools/run_calculation_checks.sh --python-only --only eft_prediction_calculus`
- `python3 tools/audit_theorem_form.py monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`
- `python3 tools/audit_unnumbered_display_labels.py monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`
- `bash tools/audit_monograph_text.sh monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex --window 120 --stride 60 --fail --limit 20`
- `bash tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
