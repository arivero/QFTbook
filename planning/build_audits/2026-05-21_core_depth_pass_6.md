# Core Depth Pass 6

Date: 2026-05-21

Scope: a cross-volume strengthening pass aimed at hidden logical steps in the
core construction.  Deferred topics remained outside the active monograph.

## Content Added

- Added the Stieltjes positivity form of the Euclidean two-point function in
  the Kallen--Lehmann chapter, including complete-monotonicity inequalities
  and recovery of the spectral measure from the cut discontinuity.
- Added an LSZ section on contact terms and interpolating fields, separating
  external one-particle pole residues from local time-ordering ambiguities and
  field-coordinate choices.
- Added local twist-two operators and integer PDF moments in the QCD/DIS
  chapter, linking light-ray factorization, local OPE operators, reduced
  hadron matrix elements, and moment evolution.
- Added a counterterm section in the anomaly chapter, distinguishing anomaly
  representatives from cohomology classes and fixing the convention in which
  gauge Ward identities are preserved.
- Added reflection-positivity constraints on OPE coefficients in the CFT OPE
  chapter, including the positive-semidefinite matrix form for degenerate
  operator subspaces.
- Added the generating-functional form of Osterwalder--Schrader reflection
  positivity, together with the Gaussian covariance check for the free massive
  scalar.

## Verification

- `tools/build_monograph.sh`
  - Passed.
  - Built `monograph/tex/main.pdf`.
  - Log scan reported clean.
- `pdfinfo monograph/tex/main.pdf`
  - 320 pages.
- `git diff --check`
  - Passed after this audit note was added.
- `tools/audit_monograph_text.sh`
  - Passed after this audit note was added.
- Deferred-topic scan over active volume TeX files
  - Passed after this audit note was added.
