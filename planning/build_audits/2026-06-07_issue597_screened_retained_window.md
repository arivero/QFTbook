# 2026-06-07 Issue #597 Screened Retained-Window Pass

## Scope

- Target issue: #597, instantons as physical amplitudes rather than
  moduli-space data.
- Monograph target:
  `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Added `ca:instanton-hard-screened-retained-window` after the hard-window
  tail-subtraction block.

## Quality Audit

- This pass is fluctuation/source/projection amplitude work, not ADHM or
  moduli-space infrastructure.  It asks when a hard four-source instanton
  channel has a controlled retained-size window after a hard source envelope
  and a physical screening scale have both been supplied by the regulated
  observable.
- The monograph keeps the \(SU(3)\), \(N_f=2\) hard four-source distinction
  between the raw logarithmic shell power \(35/3\) and the post-tail
  endpoint shell \(-1/3\).  The former can enter a screened retained-window
  saddle; the latter belongs to the tail-subtracted endpoint calculation.
- The finite companion rejects hard-only, screening-only, wrong-log-power, and
  moduli-only shortcuts, and it keeps source/projection residuals in the
  long-size bound.
- The addition does not claim a continuum determinant constant, a validated
  phenomenological instanton regime, or a Lorentzian scattering theorem.

## Re-Audit Note

- Same-day review correctly identified that the screened shell is only the
  stationary point of a majorant.  A peak of the envelope does not locate a
  signed or complex physical amplitude unless a separate comparability,
  positivity/rate, and noncancellation estimate is supplied.
- The monograph has therefore been narrowed: the block now defines a
  pre-projection kernel, source and physical-projection norms, endpoint and
  weak-coupling gates, a boundary-dominated alternative when `rho_* < R/Q`,
  and an explicit boundary that the result is a majorant-window diagnostic.
- The companion no longer solves backward for `m_scr`.  It derives the hard
  envelope from finite source gaps and the screening mass from an independent
  finite Rayleigh quotient, then constructs different actual kernels obeying
  the same majorant to reject majorant-as-amplitude shortcuts.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  passed.
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  passed.
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
  passed.
- TeX directive/planning/review-monitoring scan for Ch20D returned no
  matches.
- Focused Ch20D theorem-form, display-label, negative-scope, style-density,
  and monograph-text audits passed.
- `python3 tools/audit_calculation_evidence_contracts.py` passed.
- `python3 tools/audit_calculation_check_inventory.py` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed before full verification.
- `tools/run_calculation_checks.sh --python-only` passed.
- `tools/build_monograph.sh` passed; the generated PDF/log scan was clean.

## Re-Audit Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  passed.
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  passed.
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
  passed.
- Focused Ch20D theorem-form, unnumbered-display-label, monograph-text,
  negative-scope, and style-density audits passed.
- TeX directive/planning/review-monitoring scan for Ch20D returned no matches.
- `python3 tools/audit_calculation_evidence_contracts.py` passed with the
  standing non-blocking risk report.
- `python3 tools/audit_calculation_check_inventory.py` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/run_calculation_checks.sh --python-only` passed.
- `tools/build_monograph.sh` passed; the generated PDF/log scan was clean.
