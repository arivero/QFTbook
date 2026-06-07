# Issue #848 Cigar/Liouville QFT Boundary Re-Audit

Date: 2026-06-07
Target: `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`

## Scope

This pass addresses the #848 review concern that the chapter still risked
turning protected Hori--Vafa/Hori--Kapustin formulas into full-QFT duality
claims.  The repair focuses on the cigar/Liouville endpoint, where the physics
depth comes from the full noncompact SCFT data rather than from the quotient
metric or the exponential superpotential alone.

## Repairs

- Separated the twisted-chiral GLSM dual variable from the ordinary-chiral
  Liouville endpoint presentation.  The chapter now says that a mirror/T-duality
  automorphism must transport the measure, fermions, supercharges, `R`-current,
  and noncompact boundary data before the ordinary-chiral action is used.
- Reclassified the cigar metric/dilaton as a large-level sigma-model
  representative, not exact finite-level QFT data.  Exactness is assigned to the
  supercoset Hilbert-space, branching, reflection, spectral-measure,
  normalizability, spin-structure, and sewing package.
- Added the noncompact effective-central-charge boundary
  `c_eff = c - 24 h_min = 3`, preventing compact `c`-theorem intuition from
  being applied to the `k -> 0` continuum regime.
- Imported the Vol V/stringbook spectral convention explicitly: bosonic
  `SL(2,R)_{k+2}` labels, spectral-flow momentum/winding, noncompact field
  identification, and the absence of the compact-style opposite-flow
  identification.
- Marked the reflection amplitude as an imported normalization target until the
  Liouville path-integral normalization, `mu`, additive dilaton constant,
  continuous measure, pole residues, and special-level limiting prescriptions
  are reconstructed.
- Added the Liouville background-charge curvature/source coupling and
  asymptotic improvement terms, so the flat superspace action is no longer
  presented as the whole endpoint datum.
- Recast the Hori--Kapustin `kappa` argument as physical continuity requiring
  existence, continuity, no-bifurcation/no-phase-transition, local rigidity, and
  boundary-deformation control.

## Companion Evidence

`calculation-checks/susy_2d_lg_glsm_checks.py` now includes finite negative
controls for:

- metric/dilaton representative versus exact QFT data;
- rescaling versus chirality-changing mirror map;
- local rigidity versus global uniqueness;
- compact `c`-theorem shortcut versus noncompact `c_eff`;
- noncompact field identification and rejection of opposite-flow shortcut.

The reflection check remains symbolic target bookkeeping, not evidence for the
path-integral normalization.

## Residual Debt

This is a partial #848 repair.  Still open are the actual Liouville-side
derivation of the reflection normalization, spectral measure and residues, full
operator/state map, defect and boundary-state matching, finite-field Kahler
control, and a proof-grade global uniqueness theorem excluding disconnected
fake-Liouville fixed points.
