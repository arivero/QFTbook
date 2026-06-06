2026-06-06 #769 master-discontinuity closure audit

- Target issue: #769, generalized unitarity and loop-amplitude reconstruction.
- Chapter touched: Volume II, Chapter 6, generalized unitarity section.
- Main TeX addition: `ca:master-discontinuity-closure-gate`.
- Physics target: prevent dual-contour coefficient extraction from being
  mistaken for physical Cutkosky closure.  The new block requires the
  reconstructed amplitude to reproduce the physical channel discontinuity on a
  declared sheet after transported master jumps, lower-sector discontinuities,
  and subtraction-branch data have all been included.
- Companion check: `check_master_discontinuity_closure_gate()` in
  `calculation-checks/generalized_unitarity_reduction_checks.py`.
- Negative controls: raw contour values used as physical jumps, Euclidean master
  values used instead of boundary-value jumps, wrong sheet sign, omitted lower
  sector, and untransported subtraction branch.
- Scope audit: this is an architecture/physics-consistency pass, not a new
  solved integral family or a claim of #769 closure.  It strengthens the bridge
  from algebraic generalized cuts to physical discontinuities before the
  finite-remainder/observable assembly.
