# Issue #630 Drell-Yan/Glauber Pass

## Scope

Added a rigorous status layer for Drell--Yan factorization and Glauber
exchange in the QCD DIS/factorization chapter.

## Manuscript Changes

- Defined the Drell--Yan hadronic tensor as a timelike current-current
  Wightman matrix element between two hadron states.
- Derived the leading-power kinematic identities
  \(x_Ax_B=Q^2/s\) and \(y=\frac12\log(x_A/x_B)\).
- Stated the Drell--Yan small-\(q_\perp\) TMD factorization datum with
  past-pointing TMD staples, \(\zeta_A\zeta_B=Q^4\), a \(Y\)-term,
  a power-remainder estimate, and an explicit Glauber proof/hypothesis item.
- Proved a finite tensor-product unitarity identity that isolates the
  algebraic content of inclusive Glauber cancellation.
- Added a controlled-approximation status note explaining that the finite
  unitarity identity is not a proof of QCD factorization unless the
  leading-region, color-flow, rapidity-regulator, and measurement hypotheses
  are supplied.

## Verification

- `python3 calculation-checks/qcd_drell_yan_glauber_checks.py`
- `python3 -m py_compile calculation-checks/qcd_drell_yan_glauber_checks.py`
- targeted `git diff --check`
- full monograph build after the pass
