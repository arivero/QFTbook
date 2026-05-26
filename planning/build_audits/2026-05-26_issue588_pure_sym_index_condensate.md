# Build Audit: Pure SYM Witten Index And Condensate Ledger

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

Issue focus: #588, pure four-dimensional `N=1` supersymmetric gauge dynamics.

## Scope

This pass expands the pure `SU(N_c)` supersymmetric Yang--Mills treatment in
Volume VII Chapter 06.  The goal is to make the Witten-index computation and
gaugino-condensate story less like folklore and more like a ledger of
precise assumptions, finite-dimensional derivations, and honest status
boundaries.

## Source And Convention Notes

- This is entirely QFT-internal.  No superstring, D-brane, holographic, or
  compactification-to-string argument is used.
- The stringbook was consulted only for convention comparison and for the
  general Witten-index warning that graded-trace cyclicity can fail in
  gapless/non-trace-class settings
  (`/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`, around
  lines 19668-19692).
- The chapter keeps the existing trace and glueball conventions:
  `S=-(1/(32 pi^2)) tr(W^alpha W_alpha)` and `T(adj)=N_c`.
- The `SU(N_c)` result is developed explicitly.  The general simply
  connected simple-group statement `I_G=h_G^vee` is mentioned only as a
  broader expected extension, not used as a derived input.

## Substantive Changes

- Added `prop:pure-sym-condensate-branches-source`, deriving the branch
  values, source identity `L dW_k/dL=<S>_k`, and theta-loop/chiral-generator
  branch monodromy.
- Added `hyp:pure-sym-finite-volume-index-problem`, spelling out the
  finite-volume Hilbert-space assumptions: `T^3_L`, periodic gaugino spin
  structure, Gauss-law projection, trivial discrete-flux sector, exact
  regulated supersymmetry, trace-class heat operator, and finite zero-energy
  space.
- Added `prop:pure-sym-finite-volume-graded-trace`, proving the
  positive-energy boson-fermion pairing and stating the spectral leakage
  caveat for deformation invariance.
- Added `hyp:pure-sym-small-circle-affine-toda-input`, recording the
  small-circle assumptions, root/affine-root data, monopole-instanton
  two-zero-mode input, and instanton-weight product coordinate `eta`.
- Added `prop:pure-sym-affine-toda-critical-count`, proving directly that
  `x_1...x_N=eta` and stationarity of `sum_i x_i` force
  `x_1=...=x_N`, hence `x^N=eta`, with a nondegenerate constrained Hessian.
- Added `hyp:pure-sym-index-continuation-massive-branch` and
  `prop:pure-sym-index-condensate-ledger`, separating what the index proves
  from what requires the massive-branch/glueball hypothesis.
- Extended `calculation-checks/susy_n1_pure_sym_checks.py` and updated the
  Chapter 06 dossier and calculation-check README.

## Verification

- `python3 calculation-checks/susy_n1_pure_sym_checks.py`: passed.
- `tools/run_calculation_checks.sh`: passed, including the Wolfram
  gamma-trace check.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed with a clean final log scan after an
  overfull-line wording adjustment.
- `pdfinfo monograph/tex/main.pdf`: 1561 pages, 6171472 bytes, PDF 1.5.

## Status

This advances #588 but does not close it.  The pass improves the pure
`N=1` SYM foundation while preserving the nonconstructive status boundary
around confinement, mass gap, and the continuum Wilsonian construction.
