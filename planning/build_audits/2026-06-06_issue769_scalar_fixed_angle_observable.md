# Issue #769 Scalar Fixed-Angle Observable Pass

Scope: physics-endpoint refinement for the Volume II Chapter 6 generalized
unitarity section.

Change:
- Added `ca:phi4-fixed-angle-cross-section-rg-check` after the scalar
  UV/running block.
- The new block carries the cut-reconstructed and renormalized massless
  `lambda phi^4` four-point amplitude to a fixed-angle `2 -> 2` scattering
  density.
- The endpoint includes the physical-region logarithms, the `s`-channel
  imaginary part, identical-final-state counting, and the crossed-log
  cancellation of the one-loop running.
- Extended `generalized_unitarity_reduction_checks.py` with an exact rational
  scale-derivative check and a single-channel observable negative control.

Re-audit:
- This is not another isolated cut identity.  It turns the scalar reconstruction
  into a physical scattering-density statement and checks the renormalization
  scale cancellation at the observable endpoint.
- The gauge-theory sections still keep virtual amplitudes separate from
  infrared-safe observables because real radiation and factorization data are
  required there.
- Process and issue language stays in planning files; the TeX block is
  reader-facing physics exposition.

Verification:
- `python3 -m py_compile calculation-checks/generalized_unitarity_reduction_checks.py`
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity_reduction`
- focused Chapter 6 theorem-form, display-label, negative-scope, and
  style-density audits
- Chapter dossier metadata audit, strict monograph text audit, calculation
  inventory audit, and calculation evidence-contract audit
- `git diff --check`
- full `tools/run_calculation_checks.sh --python-only`
- full `tools/build_monograph.sh` clean at 3473 pages
