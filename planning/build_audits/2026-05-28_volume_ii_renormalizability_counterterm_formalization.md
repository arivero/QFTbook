# 2026-05-28 Volume II Renormalizability Counterterm Formalization

## Scope

This pass targets `volume_ii/chapter08_renormalizability_and_local_counterterms.tex`.
The edit removes misleading older coordinate language, labels the regulated
coordinate-map definitions, supplies the proof of the scaling-degree extension
theorem at a diagonal, promotes the power-counting finite-list argument to a
proposition, and promotes the \(D=6-\varepsilon\) cubic one-loop pole
calculation to a proposition.

## Substantive Checks

- Counterterms remain regulator-dependent coordinates of the single regulated
  action, not an external second Lagrangian.
- Action regularization remains distinct from insertion regularization.
- The extension theorem is proven by Taylor-subtracting test functions through
  order \(\lfloor s\rfloor-n\), extending the subtracted functional, and using
  the classification of distributions supported at the origin.
- The finite-list criterion explicitly derives the superficial inequality
  \(D-d_I-\sum_v(D-d_v)\ge0\).
- The \(D=6\), \(\phi^3\) self-energy pole coefficients are guarded by a
  calculation-check companion.

## Verification

Run after editing:

```bash
python3 calculation-checks/renormalizability_counterterm_checks.py
python3 -m py_compile calculation-checks/renormalizability_counterterm_checks.py
tools/build_monograph.sh
```
