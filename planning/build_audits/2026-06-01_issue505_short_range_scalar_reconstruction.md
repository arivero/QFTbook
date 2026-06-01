# 2026-06-01 Issue #505 Short-Range Scalar Reconstruction Pass

## Scope

This pass addresses one of the remaining #505 gaps: the Wilsonian RG chapter
had theorem-level fixed-point, hierarchical-scalar, fermionic, tensor-RG, and
source-reconstruction infrastructure, but the ordinary short-range scalar
lattice reconstruction object was not explicitly named.

## Manuscript Changes

- Added `Ordinary Short-Range Scalar Reconstruction Data` to Volume XI,
  Chapter 7.
- Defined a short-range scalar block-spin datum: finite-range lattice Gibbs
  measures, normalized block kernels, field scaling exponent, block-spin map,
  and localization into local coordinates plus polymer activity.
- Defined the normalized lattice field pairing
  \(a_k^D a_k^{-\Delta_\phi}\sum_x f(x)\phi_x\) and the connected cumulant
  distributions \(S_{n,k}\).
- Stated the reconstruction estimate required to turn a tuned short-range
  block-spin RG trajectory into distributional Schwinger functions.
- Recorded the current theorem status: ordinary short-range critical scalar
  Wilson-Fisher reconstruction still requires a model-specific Banach RG
  construction, source-extension estimates, and OS/Wightman reconstruction.

## Calculation Checks

- Added `calculation-checks/rg_short_range_reconstruction_checks.py`.
- The check verifies block-kernel normalization, constant-field scaling,
  block-constant distribution-pairing invariance, independent-site covariance
  scaling, and the geometric reconstruction-bound arithmetic.

## Verification Plan

- `python3 calculation-checks/rg_short_range_reconstruction_checks.py`
- `python3 -m py_compile calculation-checks/rg_short_range_reconstruction_checks.py`
- `tools/run_calculation_checks.sh --list`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

## Issue Status

This pass should not close #505.  It supplies the ordinary short-range scalar
reconstruction datum and paired finite checks, but the model-specific
short-range critical fixed-point construction, gauge-compatible constructive
examples, and deeper state-of-the-art synthesis remain open.
