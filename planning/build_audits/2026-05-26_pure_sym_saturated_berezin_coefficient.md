# Build Audit: Pure SYM Saturated Berezin Coefficient

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`.
- Issues: #562, #597, and #606.
- Main TeX target:
  `monograph/tex/volumes/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`.
- Companion files:
  - `calculation-checks/susy_n1_pure_sym_checks.py`.
  - `calculation-checks/README.md`.
  - `planning/chapter_dossiers/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.md`.

## Source Leads

- Internal monograph source: Volume II BPST instanton and 't Hooft vertex
  normalization, especially `sec:bpst-instanton-thooft-vertex`, and the
  existing pure-SYM instanton/Witten-index discussion in Volume VII
  Chapter 06.
- Stringbook convention floor: Appendix M and the Wilsonian
  supersymmetric-gauge-theory discussion around
  `/Users/xiyin/PhysicsLogic/references/stringbook/string notes.tex`
  lines 23140--23220.
- The pass is intrinsic supersymmetric QFT.  No superstring, compactification,
  brane, or holographic argument is used.

## Substantive Changes

- Added `prop:pure-sym-saturated-berezin-coefficient`, an exterior-algebra
  proposition for the saturated pure-SYM one-instanton zero-mode integral.
- The proposition defines the fixed-moduli coefficients
  `K_a^{pq}(x_a; m)` for the zero-mode part of each `S(x_a)` insertion and
  proves that the zero-mode integral is exactly the coefficient of
  `eta_1 ... eta_{2N_c}` in the product of the corresponding quadratic
  forms.
- It records two convention checks in the text: the canonical separated-pair
  coefficient is `1`, while identical canonical two-form insertions give
  `N_c!`.
- Tightened the pure-SYM instanton-correlator hypothesis so the nonzero
  instanton input explicitly includes the saturated Berezin coefficient after
  bosonic collective-coordinate integration, in addition to the size
  integral, determinant, collision, and boundary controls.
- Extended the pure-SYM calculation check with a finite Grassmann/exterior
  algebra verifier for saturation, repeated zero-mode failure, the `N_c!`
  identical-two-form coefficient, and crossing signs.

## Verification

- `python3 calculation-checks/susy_n1_pure_sym_checks.py` passed.
- `python3 -m py_compile calculation-checks/susy_n1_pure_sym_checks.py`
  passed.
- `tools/run_calculation_checks.sh` passed, including the Wolfram gamma-trace
  check.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.
- Output PDF metadata after the build: 1837 pages, 7326395 bytes.

## Status

This pass makes the zero-mode saturation coefficient itself a proved object in
the monograph.  It still does not provide the analytic instanton-size
compactness, nonzero determinant, mass-gap, or infinite-volume cluster proof
needed to derive the pure-SYM one-point condensate constructively.
