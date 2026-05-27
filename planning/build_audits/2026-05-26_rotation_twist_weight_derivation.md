# 2026-05-26 Rotation Twist-Weight Derivation Pass

## Scope

Issue #606 / 2D CFT stringbook-depth follow-up.  This pass expands the
free-orbifold twist-field section of Volume V, Chapter 11 by deriving the
complex-boson rotation twist weight from fractional oscillator moding.

## Substantive Edits

- Replaced the previous one-sentence zeta-regularization statement with a
  proposition deriving \(h_\alpha=\alpha(1-\alpha)/2\).
- Stated the oscillator-frequency shift for \(\partial Z\) and
  \(\partial\bar Z\), the relative zero-point energy, and the Hurwitz-zeta
  continuation used for the normal-ordering constant.
- Kept the real \(\mathbb Z_2\) reflection twist value \(h=\bar h=1/16\) as
  the half-complex specialization at \(\alpha=1/2\).
- Extended `calculation-checks/orbifold_twist_weight_checks.py` with exact
  rational checks of the Hurwitz-zeta subtraction.
- Updated the calculation-check inventory, Chapter 11 dossier, stringbook
  crosswalk, and this build audit note.

## Verification

Final verification for this pass:

- `python3 calculation-checks/orbifold_twist_weight_checks.py`
- `python3 -m py_compile calculation-checks/orbifold_twist_weight_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The post-rebase TeX build completed cleanly at 1833 pages.
