# Twentieth Cross-Volume Wrapper and Hypothesis-Status Pass

Date: 2026-05-29.

Purpose: continue issue #691's theorem/proposition-status audit, now with an
explicit check for the pattern in which a nontrivial assumption or controlled
approximation is followed by a theorem-family statement whose proof only
performs a short calculation.  The pass distinguishes finite calculations
that should remain visible in prose from genuine theorem-level mechanisms
whose hypotheses and proof still carry mathematical substance.

## Demotions

This pass demoted seven theorem-family wrappers to named prose calculations:

- `Morse residue pairing on the LG Jacobi algebra` became the
  finite-dimensional residue-pairing check in the B-twisted Landau--Ginzburg
  sector.
- `Linking phase and mutual locality` became the Wilson--'t Hooft linking
  phase calculation, while retaining the mutual-locality condition as a
  numbered equation.
- `Finite-lattice Wilson flow` became the compact-manifold ODE and monotonicity
  calculation.
- `Leading heavy-quark center-breaking term` became the leading hopping
  expansion calculation following the controlled local Polyakov-loop action.
- `Fermionic trace identity` became the finite coherent-state trace identity
  used to derive thermal antiperiodic boundary conditions.
- `Chern--Simons transgression under a finite gauge transformation` became the
  finite-gauge transgression calculation feeding the level-quantization
  discussion.
- `Chern--Weil transgression` became the universal transgression calculation
  used in anomaly descent.

The theorem-form audit was extended with guardrails for these titles.

## Retained After Reading

The assumption-to-theorem proximity scan flagged several statements whose
status was read before editing.  The following were retained in theorem-family
form in this pass:

- higher-dimensional Froissart angular counting, because the proof combines
  angular degeneracy, coefficient decay, partial-wave unitarity, and polynomial
  boundedness rather than merely restating the angular-tube hypothesis;
- finite-order BPHZ--Wilsonian matching, because the proof now constructs the
  low-source Legendre comparison and the truncation estimate from the stated
  hypotheses;
- the BFKL Mellin eigenvalue, because the analytic-regularization beta-integral
  computation is a nontrivial integral identity;
- WZW level quantization, because the argument is the integral-cohomology
  obstruction needed for a well-defined exponentiated action.

The top score-four heuristic candidates were also left intact after prior
reading: finite Grassmann reflection positivity, the largest-time identity,
and positive-energy supersymmetric pairing still serve as reusable mechanisms,
not merely substitutions.

## Current Counts

- theorem/proposition/lemma/corollary environments in `monograph/tex/volumes`:
  612.
- proof environments in `monograph/tex/volumes`: 607.
- short/cue-heavy heuristic queue after this pass: 127 candidates, split as
  3 score-four, 12 score-three, and 112 score-two items.  This remains a
  reading queue rather than a defect count.

## Verification

The following checks were run after the edits:

- stale-label scan for the seven removed theorem labels: clean;
- `python3 tools/audit_theorem_form.py`: clean;
- `tools/audit_negative_scope_prose.py`: clean;
- `tools/audit_monograph_text.sh`: clean;
- `python3 tools/audit_unnumbered_display_labels.py`: clean;
- `git diff --check`: clean;
- `tools/build_monograph.sh`: clean;
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2583`.

The full build and log scan completed cleanly.
