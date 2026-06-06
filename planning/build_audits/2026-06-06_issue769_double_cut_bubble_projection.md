# Build Audit: Issue #769 Double-Cut Bubble Projection

Date: 2026-06-06

Scope:
- Continued `monograph/tex/volumes/volume_ii/chapter06_analyticity_crossing_and_landau_singularities.tex`.
- Added a double-cut bubble projection block after the triple-cut triangle
  projection block.
- Updated the focused generalized-unitarity companion check, calculation-check
  inventory, and Chapter 6 dossier.

Physics-depth rationale:
- The pass completes a missing step in the one-loop coefficient hierarchy:
  maximal cuts fix boxes, subtracted triple cuts fix triangles, and subtracted
  double cuts fix bubbles only after the physical or algebraic projection
  measure is declared.
- The result ties coefficient extraction back to the two-particle
  phase-space/state-sum normalization instead of treating a cut point or raw
  algebraic residue as a physical amplitude coefficient.

Companion evidence:
- `calculation-checks/generalized_unitarity_reduction_checks.py` now verifies
  exact angular-moment projection of a bubble coefficient after subtracting
  known box and triangle double-cut shadows.
- Negative controls reject raw double-cut averages, partial higher-topology
  subtraction, point-sampling a cut, and using the wrong projection measure.

Scope guard:
- No directives, issue-tracker text, or monitoring instructions were inserted
  into monograph TeX.
- This is a physics-amplitude reconstruction step for issue #769, not a
  standalone finite-polynomial exercise.
