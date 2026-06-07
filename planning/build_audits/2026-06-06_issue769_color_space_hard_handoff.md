# 2026-06-06 Issue #769 Color-Space Hard-Function Handoff

## Scope

- Target: issue #769, loop-level generalized unitarity and integral-reduction
  development.
- Chapter target: Volume II, Chapter 6, immediately after the one-loop
  finite-observable assembly.
- Physics point: a reconstructed finite one-loop remainder in a nonabelian
  channel is a color-space vector, not yet a scalar prediction.  The handoff to
  a measured observable requires the color Gram metric, color basis, real/soft
  or factorization operator, and finite infrared subtraction convention.

## Substance

- Added `ca:color-space-hard-function-handoff`.
- The block states the color-metric hard interference
  \(2\operatorname{Re} A^{(0)\dagger} G F^{(1)}\), the equivalent one-loop
  hard matrix, and the transport rules for a finite color-basis change.
- It records the matrix version of finite infrared-scheme transport:
  \(F^{(1)}\mapsto F^{(1)}-\Delta_{\rm fin}A^{(0)}\) must be paired with the
  compensating real/factorization contribution.
- It explicitly rejects scalar Born-norm replacements for color-correlated
  real/soft or factorization insertions in multicolor channels.

## Companion Evidence

- Added `check_color_space_hard_function_handoff()` to
  `calculation-checks/generalized_unitarity_reduction_checks.py`.
- The finite rational model verifies invariance under transported color metric
  and transported color operator data.
- Negative controls reject using the old color metric after a basis change,
  leaving the real/soft operator untransported, replacing a color insertion by
  a scalar Born norm, and making a finite color-space subtraction shift without
  the compensating nonvirtual term.

## Re-Audit

- This is architecture/depth work, not another granular cut identity.
- It does not claim to compute a full process-specific soft function, prove a
  factorization theorem, or close issue #769.
- It directly addresses the physics endpoint of the loop-amplitude chapter:
  how the reconstructed virtual amplitude enters a production observable.

## Verification

- `python3 -m py_compile calculation-checks/generalized_unitarity_reduction_checks.py`
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity_reduction`
- `python3 calculation-checks/scet_factorization_checks.py`
- `tools/run_calculation_checks.sh --python-only --only scet_factorization`
- `tools/run_calculation_checks.sh --python-only`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/audit_chapter_dossiers.sh`
- Focused Chapter 6 theorem-form, unnumbered-display-label, negative-scope,
  style-density, monograph-text, and process-language scans.
- `git diff --check`
- `tools/build_monograph.sh` clean; rebuilt `monograph/tex/main.pdf` at 3479
  pages.
