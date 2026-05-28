# 2026-05-28 Volume III Correlator-Kinematics Formalization

## Scope

This pass targets `volume_iii/chapter08_correlation_functions_and_conformal_frames.tex`,
which was correct in its main formulas but too prose-driven for a load-bearing
CFT kinematics chapter.  The edit promotes the separated-correlator framework,
scalar one-point rule, spinning two-point transport, scalar three-point
kinematics, ordered four-point conformal frame, four-point cross-ratio
completeness, and four-point prefactor covariance to formal theorem-style
environments with proof text.

## Substantive Checks

- Separated correlators are explicitly distributions on
  `Conf_n(R^D)`, with contact-term extensions left outside the
  separated-point classification.
- The scalar three-point exponents are derived from inversion weights rather
  than asserted.
- The four-point frame proof constructs a representative by translation,
  special conformal transformation, rotation, dilation, and residual
  orthogonal rotation.
- The scalar four-point prefactor proof checks the inversion weight at each
  insertion by summing incident distance exponents.
- `calculation-checks/cft_correlator_kinematics_checks.py` guards the
  three-point exponent system, four-point inversion-weight ledger, generic
  four-point quotient dimension, and frame cross-ratio identities.

## Verification

Run after editing:

```bash
python3 calculation-checks/cft_correlator_kinematics_checks.py
python3 -m py_compile calculation-checks/cft_correlator_kinematics_checks.py
tools/build_monograph.sh
```
