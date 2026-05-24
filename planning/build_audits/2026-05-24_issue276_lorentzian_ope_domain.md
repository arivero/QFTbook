# Issue #276 Audit: Euclidean and Lorentzian OPE Convergence Domains

## Scope

- GitHub issue: #276, ``[Vol V Ch 9] OPE convergence domain: Lorentzian
  extension unstated''.
- Manuscript file:
  `monograph/tex/volumes/volume_iii/chapter09_operator_product_expansion.tex`.
- Dossier file:
  `planning/chapter_dossiers/volume_iii/chapter09_operator_product_expansion.md`.

## Manuscript Changes

- Renamed the radial OPE convergence theorem as a Euclidean radial theorem and
  made the Euclidean point configuration explicit.
- Added a Lorentzian continuation proposition using fixed Wightman ordering,
  forward-tube holomorphy, \(i\epsilon\) boundary values, and the radial
  channel bounds \(|\rho|,|\bar\rho|\le q<1\).
- Stated how strictly timelike future/past configurations enter through the
  ordered boundary value, while null and coincident strata remain
  distributional boundary questions.
- Added references to Mack, Kravchuk--Qiao--Rychkov, and Qiao for the
  theorem-level Lorentzian OPE convergence and channel classification context.

## Verification

- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed.
