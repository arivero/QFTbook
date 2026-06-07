# 2026-06-07 Issue #597 Finite Source-Functional Laboratory Pass

## Scope

- Target issue: #597, instantons as physical amplitudes with carefully
  regularized fluctuation and measure data.
- Monograph target:
  `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Added `ca:instanton-finite-source-functional-laboratory` immediately after
  the front source-functional route block.

## Quality Audit

- This pass is amplitude architecture, not additional moduli-space
  infrastructure.  The finite laboratory assembles collective weight,
  nonzero-mode determinant normalization, zero-mode source differentiation,
  normal-mode source quotient, and physical projection in one retained-cell
  coefficient.
- The inserted block explicitly says that ADHM or BPST collective-volume data
  supply at most the collective side of the coefficient, and do not compute a
  physical instanton amplitude without source determinant, fluctuation, and
  projection data in the same channel.
- The companion check computes the laboratory coefficient in exact rational
  arithmetic and keeps the mass-saturated, determinant-only, and raw-Euclidean
  shortcuts as different finite values.
- The addition is a finite order-of-operations test.  It does not claim a
  continuum instanton theorem, a phenomenological instanton regime, or a
  Lorentzian scattering construction.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  passed.
- `PYTHONPATH=calculation-checks python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
  passed.
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
  passed.
- Focused Ch20D theorem-form, unnumbered-display-label, negative-scope prose,
  and style-density audits passed.
- Ch20D scan for review/directive/monitoring language returned no matches.
- `python3 tools/audit_calculation_evidence_contracts.py` passed.
- `python3 tools/audit_calculation_check_inventory.py` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/run_calculation_checks.sh --python-only` passed.
- `tools/build_monograph.sh` passed after replacing old-style `\over`
  fractions in the new block with `\frac{...}{...}`; the final build log scan
  was clean.
