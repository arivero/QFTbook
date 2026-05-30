# General Method Placement Audit

Date: 2026-05-30

## Audit Target

The audit checks for a structural prose error: a general method is developed
inside a narrow example chapter in a way that can make the reader think the
method is intrinsic to that example.  The correct architecture is:

- methodological chapter: definitions, hypotheses, linear algebra, estimates,
  and proof of the general method;
- example chapter: model-specific sources, symmetry channels, regulator
  choices, renormalization data, limits, and diagnostics.

## Search Passes

Initial grep passes covered:

- `GEVP`, `generalized eigenvalue problem`, `spectral extraction`, source
  matrices, and residual criteria;
- `Monte Carlo`, `HMC`, `RHMC`, `DLCQ`, `TCSA`, `TFFSA`, Hamiltonian
  truncation, estimator, and algorithm;
- bootstrap and semidefinite-programming phrases;
- explicit wording that a method is a running example or is not tied to one
  dynamics.

## Fixes In This Pass

1. GEVP placement:
   - Volume XI now carries the general finite-regulator GEVP method,
     including exact finite-state extraction, source-basis covariance, and
     residual criteria.
   - Volume VII pure \(\mathcal N=1\) SYM now treats GEVP as an applied
     estimator and focuses on the channel/source data and the
     supersymmetry-restoration diagnostic.
   - Volume II QCD spectroscopy now refers to the general GEVP method and
     keeps only the QCD-specific interpretation of finite operator-source
     families and overlap labels.  The pass also avoids overloading the
     phrase "source chart", which elsewhere denotes a contact-term/source
     coordinate choice rather than a finite spectroscopy basis.
   - Volume II lattice Yang--Mills now keeps pure-glue source spaces and
     continuum spectral data while referencing Volume XI for the GEVP method.

2. TCSA placement:
   - Volume VI now keeps only the CFT-deformation Hamiltonian coordinate
     chart and the interface condition with form-factor perturbation theory.
     The local TCSA regulator setup and OPE counterterm-power derivation have
     been removed from the specialized chapter and left to the general
     Hamiltonian-truncation framework in Volume XI.

3. Harness rule:
   - `planning/12_strict_writing_harness.md` now contains a general-method
     placement rule to prevent future versions of the same error.

## Candidates Reviewed But Not Rewritten In This Pass

- The large-\(N\) two-dimensional QCD DLCQ matrix in Volume II is retained as
  a specific worked benchmark; it already points to the general DLCQ chapter
  and derives a model-specific positive quadratic form.
- The CFT bootstrap and semidefinite-programming material is retained in the
  CFT/OPE volume because crossing and conformal-block positivity are the
  natural general setting for that method rather than a narrow example.
- Jet algorithms remain in the QCD/jets chapter because the algorithm is part
  of the observable definition, not a numerical method being mistaken for
  QCD dynamics.

## Remaining Audit Queue

Future passes should continue checking localization templates, RG comparison
machinery, large-\(N\) numerical diagnostics, and special-function recursion
methods for the same placement error.
