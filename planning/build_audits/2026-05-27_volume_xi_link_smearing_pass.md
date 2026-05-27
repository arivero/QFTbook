# 2026-05-27 Volume XI Link-Smearing Pass

## Scope

This pass continues issue #631 by developing gauge-covariant link smearing in
Volume XI, Chapter 5 as regulator-level data rather than informal numerical
preprocessing.

## Substantive Additions

- Defined smearing as a local map \(\mathcal S:G^E\to G^E\) with a precise
  endpoint gauge-covariance law.
- Defined the oriented staple sum and the APE preprojection matrix.
- Proved equivariance of polar link projection and recorded the smooth-branch
  condition for the \(SU(N)\) determinant normalization.
- Defined stout smearing using the projection
  \(\Pi_{\mathfrak{su}(N)}(M)\) onto anti-Hermitian traceless matrices.
- Proved stout smearing is a smooth \(SU(N)\)-valued gauge-covariant link
  map.
- Explained hypercubic smearing as a finite composition of local covariant
  maps and stated the locality-radius condition needed for continuum
  operator schemes.
- Added `calculation-checks/link_smearing_checks.py` to verify the matrix
  algebra behind polar projection and stout-smearing covariance.

## Verification

- Passed: `python3 calculation-checks/link_smearing_checks.py`
- Passed: `python3 -m py_compile calculation-checks/link_smearing_checks.py`
- Passed: primitive-fraction scan on touched files.
- Passed: `git diff --check` on touched files.
- Passed: `tools/build_monograph.sh`
- Built PDF: `/Users/xiyin/QFT/monograph/tex/main.pdf`, 2234 pages.

## Remaining Work

- Chapter 5 still needs lattice perturbation theory and tadpole-improvement
  conventions, explicit static-potential and Wilson-flow measurement
  pipelines, and cluster-runnable implementations tied to the finite
  definitions in the text.
