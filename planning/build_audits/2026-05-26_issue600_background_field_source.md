# Build Audit: Issue #600 Background-Field Source Pass

Date: 2026-05-26

Lane: `codex/2d-cft-liouville-bcft-nlsm`

## Scope

- Volume V, Chapter 11 NLSM perturbative renormalization.
- GitHub issue: #600.
- Stringbook source: `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  especially `sec:bosoneloopbeta`.

## Substantive Changes

- Added a covariant background-field subsection defining the sigma-model
  split as \(X=\exp_x\xi\), with \(\xi\in\Gamma(x^*TM)\), rather than as a
  coordinate difference.
- Recorded the local coordinate expansion of the exponential map to quadratic
  order.
- Defined the source-coupled mean-zero 1PI effective action used in the
  background-field method.
- Proved at Gaussian order that
  \(\langle\xi\rangle_J=\mathcal A^{-1}(J-L)\), so the auxiliary source is
  fixed by \(J=L\), where \(L\) is the first-variation density.
- Derived the pure-metric first variation
  \(L_i=-(2\pi\alpha')^{-1}G_{ij}\nabla^a\partial_a x^j\) on a closed
  worldsheet and explained why the beta tensor is an off-shell local tensor
  on coupling space.
- Updated the Chapter 11 dossier, calculation-check inventory, and
  stringbook crosswalk.

## Calculation Checks

- Added `calculation-checks/nlsm_background_field_checks.py` to verify the
  finite Gaussian source algebra and square-completion sign in exact rational
  arithmetic.

## Verification

- `python3 calculation-checks/nlsm_background_field_checks.py`
- `python3 -m py_compile calculation-checks/nlsm_background_field_checks.py`
- `python3 calculation-checks/nlsm_buscher_checks.py`
- `python3 calculation-checks/nlsm_weyl_anomaly_checks.py`
- `python3 calculation-checks/nlsm_scheme_redefinition_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

Result: clean monograph build and log scan at 1589 pages.

## Remaining Status

Issue #600 remains open.  This pass fills in the source-coupled
background-field foundation for the one-loop derivation, but the full
Tseytlin-school higher-loop \(G+B+\Phi\), heterotic, and supersymmetric
renormalization program remains open.
