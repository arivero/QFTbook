# 2026-05-28 Issue #634: Standard Model Hybrid-QFT Depth Pass

## Scope

First focused development pass on GitHub issue #634 for
`monograph/tex/volumes/volume_ii/chapter19c_standard_model_hybrid_definition.tex`.

The goal of this pass is not to turn the chapter into a particle-physics
review.  It strengthens load-bearing Standard Model data that must be precise
in a hybrid-QFT treatment: global form, flavor coordinates, electroweak
scalar/custodial identities, baryon/lepton anomaly bookkeeping, SMEFT coupling
coordinates, neutrino mass coordinates, strong-CP phase bookkeeping, and the
matching datum.

## Manuscript Changes

- Added the central `Z_6` kernel calculation for the minimal representation
  content using integer hypercharge `y=6Y`.  This calculation was later
  demoted from proposition form to prose in the anti-wrapper pass.
- Added Definition `def:sm-ckm-matrix` and Propositions
  `prop:sm-flavor-parameter-counting`,
  `prop:sm-gim-tree-level-diagonality`, and the Jarlskog rephasing
  calculation.  The latter was later demoted from proposition form to prose in
  the anti-wrapper pass, while retaining the phase-cancellation and
  row/column-orthogonality derivation.
- Added the Higgs radial mass coordinate calculation and custodial
  `rho_tree=1` calculation.  The latter was later demoted from proposition
  form to a worked paragraph in the anti-wrapper pass.
- Added Definition `def:sm-b-l-charges`, Proposition
  `prop:sm-baryon-lepton-anomaly`, and the sphaleron-selection-rule remark.
- Added Definition `def:sm-smeft-coupling-chart`, Definition
  `def:sm-weinberg-operator`, and the type-I singlet-neutrino tree-matching
  calculation.  The matching calculation was later demoted from proposition
  form to a worked paragraph in the anti-wrapper pass.
- Added Proposition `prop:sm-strong-cp-phase` with the invariant
  `theta_bar = theta_3 + arg det(M_u M_d)` and the massless-quark caveat.
- Added Definition `def:sm-hybrid-matching-data`, expanding the contents of
  the hybrid matching datum `M`.

## Calculation Check

- Extended `calculation-checks/standard_model_anomaly_checks.py`.
- New checks cover the `Z_6` kernel generator, CKM parameter counts,
  Jarlskog rephasing cancellation, Higgs/rho identities, `B-L` anomalies with
  and without `nu^c`, Weinberg-operator mass normalization, singlet-neutrino
  tree matching, and strong-CP phase invariance.

## Verification

Passed before checkpoint:

- `python3 calculation-checks/standard_model_anomaly_checks.py`
- `python3 -m py_compile calculation-checks/standard_model_anomaly_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full monograph build and final log scan are clean.  The generated
`monograph/tex/main.pdf` has 2336 pages.

## Remaining Issue #634 Work

This pass does not close #634.  Remaining large items include the one-loop SM
RG system, Higgs vacuum-stability flow as a controlled EFT statement,
precision electroweak `S,T,U`, the full muon `g-2` hybrid calculation, a
more explicit dimension-six operator-basis treatment, and the chiral-lattice
construction connection.
