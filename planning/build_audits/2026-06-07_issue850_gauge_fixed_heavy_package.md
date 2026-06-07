# Issue 850 Gauge-Fixed Heavy Package Audit

Date: 2026-06-07.

Scope:
- Volume VII Chapter 08 now inserts the gauge-map/gauge-fixing-adjoint layer
  between the rank-one row-Jacobian derivation and the regulator-compatible
  heavy-complex supertrace.
- The new block derives the ghost operator as
  \({\mathcal G}_{B,\xi}{\mathcal R}_B\), assembles the moment-map, kinetic, and
  Yukawa rows into a gauge-fixed heavy package, and projects away the Higgs
  tangent zero modes before the trace-log inverse is used.
- The companion `susy_moduli_space_checks.py` adds a finite rational check that
  rejects an independently chosen ghost row, an unprojected tangent zero mode,
  and a missing normal-heavy row.

Quality boundary:
- This is a substantive background-field architecture repair for #850.  It does
  not claim the all-order Higgs-branch metric theorem or the full continuum
  determinant evaluation.
