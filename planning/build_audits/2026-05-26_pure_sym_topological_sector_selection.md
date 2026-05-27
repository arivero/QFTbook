# Build Audit: Pure SYM Topological-Sector Selection

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
  `/Users/xiyin/PhysicsLogic/references/stringbook/string notes.tex`.
- The pass is intrinsic supersymmetric QFT. No superstring,
  compactification, brane, or holographic argument is used.

## Substantive Changes

- Added `prop:pure-sym-topological-sector-s-selection`, a separated
  correlator selection rule for pure `SU(N_c)` N=1 SYM in instanton number
  `nu`.
- The proposition proves from the adjoint index theorem and Berezin
  top-degree condition that a self-dual charge-`nu` sector has
  `2 nu N_c` adjoint gaugino zero modes and hence requires `nu N_c`
  separated insertions of `S = -(32 pi^2)^{-1} Tr W^alpha W_alpha` for
  zero-mode saturation.
- It makes explicit that the standard `N_c`-point pure-SYM instanton
  correlator is a charge-one test at Berezin level: sectors with
  `nu >= 2` leave unsaturated adjoint zero modes unless extra sources,
  contacts, or boundary mechanisms are supplied.
- It records the conjugate chirality check for anti-self-dual sectors:
  anti-instanton zero modes pair with anti-chiral `overline S` insertions,
  not separated chiral `S` insertions.
- Extended the pure-SYM calculation check with a finite instanton-number
  verifier for the first saturated insertion count, anomalous charge and
  dimension matching, the charge-one nature of the `N_c`-point correlator,
  and the anti-instanton chirality mismatch.

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
- Output PDF metadata after the build: 1844 pages, 7349001 bytes.

## Status

This pass proves the finite Berezin/topological selection rule used to keep
the pure-SYM instanton root equation honest. It does not solve the analytic
instanton-size integral, determinant nonvanishing, moduli-space
compactification and boundary analysis, mass-gap input, or cluster theorem
needed for a constructive one-point condensate derivation.
