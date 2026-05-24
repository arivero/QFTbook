# Issue #313 Regulator Classification Audit

## Issue

GitHub issue #313 reported that cutoff regulators were named locally across
the perturbative/RG/statistical chapters but were not collected into a master
classification, and that dimensional regularization needed an explicit flag
as formal perturbative analytic continuation rather than a regulator on a
path-integral measure.

## Resolution

- Added Table `tab:regulator-integration-status-catalog` to the scalar
  path-integral foundations chapter.
- The table separates finite lattice/spin systems, finite Fourier-mode
  cutoffs, smooth covariance/Wilsonian cutoffs, heat-kernel/spectral or
  point-splitting cutoffs, dimensional regularization, and subtraction schemes
  such as BPHZ/MS.
- The dimensional-regularization row states explicitly that it is not a Borel
  measure, not a Berezin measure, and not a measure on a
  noninteger-dimensional field-configuration space; it is a meromorphic
  assignment to perturbative graph distributions and associated algebra.
- The renormalizability chapter now cross-references the table and separates
  cutoff path-integral regulators from dimensional regularization.
- The 1PI RG chapter now states that `\Lambda` denotes a cutoff-class
  regulator, while dimensional regularization replaces this by a formal
  meromorphic graph assignment.
- The Ising chapter now identifies the finite spin ensemble with the finite
  lattice row and states the additional continuum-limit hypotheses.

## Verification

- Working-tree verification before commit:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
