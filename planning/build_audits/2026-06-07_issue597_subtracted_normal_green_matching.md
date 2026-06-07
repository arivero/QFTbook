# 2026-06-07 Issue #597 Subtracted Normal-Green Matching Pass

## Scope

- Target issue: #597, instantons as physical amplitudes with carefully
  regularized fluctuation and measure data.
- Monograph target:
  `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Added `ca:instanton-subtracted-normal-green-matching` immediately after the
  source-projected normal-propagator insertion block.

## Quality Audit

- This pass is fluctuation/amplitude work, not moduli-space infrastructure.
  It treats the instanton-background Green function as a source bilinear whose
  projector, UV subtraction, logarithmic local term, finite local matching, and
  Wilsonian coefficient compensation must be fixed before it can enter a
  physical four-point channel.
- The determinant trace identity is kept in its proper role: it calibrates the
  Gaussian determinant response, but it does not replace the external-source
  bilinear.
- The finite companion rejects unsubtracted, unprojected, trace-only,
  wrong-basis, and uncompensated finite-local subtraction shortcuts, and checks
  that local matching errors are included in the residual budget.
- The addition stays inside a retained finite-regulator instanton window.  It
  does not claim a continuum instanton Green function, a phenomenological
  instanton regime, or a completed Lorentzian scattering theorem.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  passed.
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  passed.
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
  passed.
- Focused Ch20D theorem-form, display-label, negative-scope, style-density,
  and monograph-text audits passed.
- TeX scan for planning/directive/review-monitoring language returned no
  matches in Ch20D.
- `python3 tools/audit_calculation_evidence_contracts.py` passed.
- `python3 tools/audit_calculation_check_inventory.py` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed before staging.
- `tools/run_calculation_checks.sh --python-only` passed.
- `tools/build_monograph.sh` passed after replacing an undefined `\Tr` macro
  with `\operatorname{Tr}`; the generated PDF/log scan was clean.
