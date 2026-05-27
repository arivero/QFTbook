# 2026-05-27 Issue #630 QCD PDF Matrix-Element Datum

## Scope

- Upgraded Volume II, Chapter 19 around QCD nonperturbative observable
  definitions, DIS, PDFs, DGLAP kernels, and the endpoint/large-spin cusp
  boundary.
- Added a QCD-wide regulated gauge-invariant matrix-element datum: QCD
  quantities involving colored fields must be regulator-defined matrix
  elements with Wilson-line transporters and the required UV, cusp, endpoint,
  and rapidity subtractions.
- Rewrote the DIS/PDF definitions as renormalized gauge-invariant light-ray
  operator matrix elements rather than parton-model probability language.
- Added a proof of open Wilson-line gauge covariance.
- Stated inclusive DIS factorization as a compact-\(x_B\) leading-twist datum
  with a distributional power-remainder estimate, leaving threshold and
  small-\(x\) limits as separate boundary problems.
- Replaced ambiguous leading-order DGLAP plus-distribution notation with
  \(D_0=(1-x)^{-1}_+\), proved quark-number and momentum-column sum rules, and
  added the large-spin nonsinglet moment/cusp-coefficient normalization.
- Tightened the fragmentation-function paragraph in the jets/hadronization
  chapter to identify it as a renormalized Wilson-line matrix element requiring
  a regulator.

## Checks

- `python3 calculation-checks/qcd_dglap_checks.py`
- `python3 -m py_compile calculation-checks/qcd_dglap_checks.py`
- `git diff --check -- ...` on the changed manuscript, calculation-check,
  README, dossier, and audit files.
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`: 2152 pages, 8708204 bytes, PDF 1.5.

## Status

This pass addresses the A1 part of #630 at the level appropriate for the
current Volume II core QCD development.  It does not claim a theorem-level
construction of continuum four-dimensional QCD light-ray operators or a
complete nonperturbative proof of DIS factorization; those remain explicit
existence/factorization inputs unless later constructed from a regulator.
