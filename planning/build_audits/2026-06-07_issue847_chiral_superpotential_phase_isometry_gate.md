# 2026-06-07 Issue #847 Chiral-Superpotential Phase-Isometry Gate

## Scope

- Target issue: #847, Hori--Vafa signs and normalization from compact flux
  conventions.
- Monograph target:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Added `ca:glsm-chiral-superpotential-phase-isometry-gate`.
- Companion target: `calculation-checks/susy_2d_lg_glsm_checks.py`.
- Dossier target:
  `planning/chapter_dossiers/volume_vii/chapter09_two_dimensional_supersymmetric_models.md`.

## Substance Audit

This pass addresses the issue-body risk that a generic chiral superpotential
can break the phase isometries needed for abelian dualization.  The chapter now
separates gauge invariance of a chiral monomial from preservation of the
phase-rotation lattice that can be Legendre transformed into periodic twisted
chirals.  For
`W_ch = sum_A lambda_A prod_i Phi_i^{p_Ai}`, the allowed phase directions are
recorded as
`L_W = {v in Z^m | sum_i p_Ai v_i = 0 for every active monomial A}`.

The finite example uses charges `(1,1,-2)` and the gauge-invariant monomial
`P X_1 X_2`.  Gauge neutrality alone does not justify dualizing all three
primitive phase rotations; the preserved directions satisfy
`v_1 + v_2 + v_P = 0`.  The block therefore prevents a chiral hypersurface
GLSM from being treated as the same object as the toric no-chiral-potential
Hori--Vafa derivation unless the broken-isometry data, spurion charges, mirror
interaction, orbifold, and operator map are supplied separately.

This is physics scope control rather than an extra mathematical side branch:
the point is to keep the mirror derivation tied to the actual QFT dualization
conditions and to block an overbroad use of Hori--Vafa primitives.

## Companion Evidence

`check_chiral_superpotential_phase_isometry_gate()` builds the exact
charge-monomial model and checks:

- gauge neutrality of `P X_1 X_2`;
- failure of individual phase rotations to preserve the chiral interaction;
- rank loss from three primitive phases to a two-dimensional preserved
  phase-isometry lattice;
- survival of relative phase directions inside the kernel;
- insufficiency of a charge-only gate for Hori--Vafa dualization;
- the need to carry spurion or mirror-interaction data when a broken phase is
  still used;
- preservation of the full phase lattice only in the zero-chiral-potential
  case.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `bash tools/audit_monograph_text.sh`
- `python3 tools/audit_negative_scope_prose.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `bash tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

The style-density audit still reports pre-existing Volume VII marked-term
windows, including older Chapter 9 windows before this insertion.  The new
gate did not introduce those windows, so this is recorded as a remaining
chapter-flow risk rather than a blocker for this targeted repair.
