# Issue #924 Chart-Exit Observable Tail Audit

## Scope

- Target chapter:
  `monograph/tex/volumes/volume_xii/chapter11_semiclassical_backreaction_stress_tensor_fluctuations.tex`.
- Target check:
  `calculation-checks/semiclassical_backreaction_checks.py`.
- Target dossier:
  `planning/chapter_dossiers/volume_xii/chapter11_semiclassical_backreaction_stress_tensor_fluctuations.md`.

## Substance Audit

- Added the retained Gaussian metric law \(H=h_*+Z\), its chart margin
  \(\rho_h=r_h-\|h_*\|\), and the chart-exit event.
- Added Markov and finite-dimensional Gaussian exit bounds from the metric
  covariance and declared norm.
- Required one of three controls before averaging a local observable Taylor
  expansion: global out-of-chart integrability, a stopped/truncated process
  with an exit error, or a conditional-on-chart prediction plus exit
  probability.
- Added chart-exit terms to observable mean and covariance budgets.
- Reworded signal-to-noise as a self-averaging/detectability condition, not as
  the validity criterion for the stochastic probability law.

## Physics-Depth Reaudit

- This is not a mathematical side annex.  The repair changes how metric
  fluctuations become physical observable predictions: rare but large
  Einstein-Langevin excursions can dominate nonlinear geometry observables.
- The text now separates three physics claims that were previously too close:
  validity of the stochastic law, self-averaging of the geometry, and
  detectability of a mean shift.

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
