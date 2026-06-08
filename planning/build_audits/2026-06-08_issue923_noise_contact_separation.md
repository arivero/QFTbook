# Issue #923 Noise/Contact Separation Audit

## Scope

- Target chapter:
  `monograph/tex/volumes/volume_xii/chapter11_semiclassical_backreaction_stress_tensor_fluctuations.tex`.
- Target check:
  `calculation-checks/semiclassical_backreaction_checks.py`.
- Target dossier:
  `planning/chapter_dossiers/volume_xii/chapter11_semiclassical_backreaction_stress_tensor_fluctuations.md`.

## Substance Audit

- Rebuilt the noise-kernel paragraph around the unordered covariance
  \(N(f,k)\) of centered smeared stress observables in one declared
  algebra/state.
- Added the Schwartz-kernel-theorem handoff: continuity of the bilinear
  covariance gives the bidistribution, while wavefront and Ward properties
  belong to the chosen algebra/state construction.
- Removed the suggestion that the noise kernel receives independently chosen
  time-ordered/coincident-point contact extensions.
- Repaired the interacting package so \(\mathsf N^{full}\) is computed with
  the unordered interacting product, while local metric-variation/time-ordered
  contacts enter the retarded response.
- Added a finite negative control: a Ward-clean local contact added directly
  to a positive covariance can make a physical variance negative.

## Physics-Depth Reaudit

- The repair is physics-substantive because the Einstein--Langevin source is a
  stochastic covariance, not an effective-action counterterm.  Positivity is
  what lets the noise become a classical Gaussian source.
- Response renormalization and noise renormalization are now separated at the
  level where the metric actually feels them: dissipative/retarded feedback
  versus stochastic fluctuations.

## Verification

- Passed: `python3 calculation-checks/semiclassical_backreaction_checks.py`.
- Passed: `python3 tools/audit_calculation_evidence_contracts.py`.
- Passed: `bash tools/audit_chapter_dossiers.sh`.
- Passed: `python3 tools/audit_calculation_check_inventory.py`.
- Passed: `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_xii/chapter11_semiclassical_backreaction_stress_tensor_fluctuations.tex --fail`.
- Passed: `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_xii/chapter11_semiclassical_backreaction_stress_tensor_fluctuations.tex`.
- Passed: `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_xii/chapter11_semiclassical_backreaction_stress_tensor_fluctuations.tex`.
- Passed: `tools/audit_monograph_text.sh`.
- Passed: `tools/run_calculation_checks.sh --python-only`.
- Passed: `tools/build_monograph.sh`.
- Passed: `git diff --check`.
