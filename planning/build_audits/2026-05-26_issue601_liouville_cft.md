# Issue #601 Liouville CFT Partial Pass

Date: 2026-05-26.

## Scope

- GitHub issue: #601, `[Block R] Liouville CFT`.
- Lane: `02_2d_cft_liouville_bcft_nlsm`.
- Files edited:
  - `monograph/tex/volumes/volume_v/volume_v_current.tex`
  - `monograph/tex/volumes/volume_v/chapter13_liouville_cft.tex`
  - `planning/chapter_dossiers/volume_v/chapter13_liouville_cft.md`
  - `calculation-checks/liouville_bpz_checks.py`

## Monograph Content Added

- Added a dedicated compiled Volume V Liouville chapter.
- Defined the classical Liouville datum, including surface, metric, scalar
  field, background charge, curvature term, and exponential potential.
- Derived the classical equation of motion.
- Fixed the free-field OPE normalization and proved the improved central
  charge formula `c=1+6Q^2`.
- Derived the exponential weights `h_alpha=alpha(Q-alpha)` and the
  marginality condition `Q=b+b^{-1}`.
- Defined the Seiberg domain and checked the constant-mode inequality.
- Defined the GMC measure used by the probabilistic construction.
- Stated the GKRV probabilistic construction and the DOZZ formula as
  `quotedtheorem` boundaries with local roles.
- Defined the reflection relation.
- Added the canonical cylinder scattering basis, the reflection-phase
  asymptotics, and the continuous direct-integral conformal-block
  decomposition.
- Proved the level-two null-vector coefficient and derived the BPZ equation.
- Derived the scattering-normalized `P`-basis DOZZ representative from the
  conventional `alpha`-basis formula.
- Added the hypergeometric form of the BPZ solutions for one degenerate
  insertion and the resulting shift-equation logic.
- Recorded the remaining functorial sewing problem as an `openproblem`,
  cross-linked to the Volume IV Kontsevich-Segal ledger.

## Calculation Check

- Added `calculation-checks/liouville_bpz_checks.py`, a finite rational
  Laurent-polynomial check of the Virasoro arithmetic for
  `(L_{-1}^2+b^2L_{-2})|h>`.

## Remaining Obligations

- #601 remains open.  The chapter still needs a fully expanded gamma-product
  DOZZ shift-ratio calculation check, low-order conformal-block recursion
  examples beyond the first degenerate block, and eventual functorial sewing
  closure.
- #600 and #602 were not addressed by this pass.
