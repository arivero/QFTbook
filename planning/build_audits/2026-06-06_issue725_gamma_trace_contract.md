# Issue #725 Gamma-Trace Evidence Contract

Date: 2026-06-06.

Scope:
- Promoted `calculation-checks/gamma_trace_checks.py` to the extended evidence
  tier.
- Added a finite spinor-convention remark in Volume I Chapter 16a clarifying
  that the \(\gamma_5\) trace fixes the finite spin-trace/orientation slot of
  anomaly formulae, not the anomaly calculation itself.
- Added negative controls for a flipped \(\gamma_5\) orientation, a
  four-dimensional two-plane shortcut for the two-dimensional Dirac anomaly
  trace, a four-dimensional \(\gamma_5\) projection used in two dimensions,
  and the missing anticommutator factor one half.

Quality audit:
- This pass improves convention-to-physics handoff for anomaly coefficients.
- It does not add tangential Clifford-algebra material beyond what is needed
  to prevent sign and dimension mistakes in physical anomaly calculations.
- Review and directive metadata remain in planning files, not in monograph
  TeX.

Remaining scope:
- Divergent triangle integrals.
- Heat-kernel asymptotics and index-theorem input.
- Anomaly-line/global-anomaly claims.
- All-order anomaly conclusions.
