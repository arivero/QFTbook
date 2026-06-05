# Issue #769 equal-mass threshold-family pass

Date: 2026-06-05.

Scope:

- Chapter: Volume II, Chapter 6, analyticity/crossing/Landau singularities.
- New monograph label: `ca:equal-mass-bubble-threshold-family`.
- Companion check:
  `check_equal_mass_bubble_threshold_family()` in
  `calculation-checks/generalized_unitarity_reduction_checks.py`.

Substance audit:

- This pass addresses the physical master-integral side of generalized
  unitarity.  It is not another cut-projection identity: it shows how an
  actual threshold family carries a lower-sector tadpole master, a Euclidean
  boundary condition, and a physical timelike branch.
- The finite equal-mass bubble part satisfies
  `2 z (1+z) F_m'(z) + F_m(z) = 2 z T_m`, so the lower-sector datum is visible
  already in the small-momentum expansion.  A homogeneous one-master shortcut
  is explicitly rejected.
- The Landau threshold is tied to the Feynman-parameter double root at
  `z=-1`, and the physical branch gives the phase-space square root
  `Im F_m(-r-i0) = -pi sqrt(1-1/r)`.

Negative controls:

- Dropping the lower tadpole master gives the wrong small-`z` coefficient.
- Reusing the Euclidean branch above threshold misses the imaginary part.
- A parent-cut-only view sees the square-root discontinuity but does not fix
  lower-sector normalization or branch data.

Expected verification:

- Run the focused generalized-unitarity companion script.
- Run the calculation evidence/inventory audits.
- Run Chapter 6 prose/form-label audits and the full monograph build.
