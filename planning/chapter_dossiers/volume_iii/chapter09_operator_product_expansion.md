# Volume III, Chapter 9 Dossier: Operator Product Expansion

## Logical Role

- Role in the monograph: formulate the OPE as a convergent radial Hilbert-space
  expansion under stated hypotheses and connect OPE coefficients to
  conformal-block decompositions and positivity.
- Immediate predecessor: correlation functions and conformal frames.
- Immediate successor: later special volumes on bootstrap, two-dimensional
  CFT, supersymmetry, or integrability.

## Definitions And Results

The chapter establishes:

- the radial Hilbert-space statement of OPE convergence for insertions inside
  a separating sphere;
- the local operator expansion into primaries and descendants;
- coefficient functions as distributions or analytic functions on the
  convergence domain;
- conformal blocks as sums over descendant states in a fixed conformal
  multiplet;
- the scalar four-point Casimir equation with the \(u,v\) differential
  operator displayed, the two Frobenius branches \(\Delta\) and \(D-\Delta\),
  and the radial descendant/Gram-matrix construction proving local existence
  and uniqueness of the OPE-normalized block;
- conformal partial waves as shadow-projector/harmonic-analysis kernels,
  distinct from OPE-channel blocks and normalized together with their
  Plancherel density;
- reflection-positivity constraints on OPE coefficient matrices;
- the boundary between core OPE machinery and later specialized bootstrap
  methods.

## Claims To Verify

1. OPE convergence is a Hilbert-space norm statement under radial
   reconstruction, discreteness, and finite-multiplicity assumptions.
2. Correlator convergence follows by pairing the inside state with exterior
   states at larger radius.
3. Positivity of squared OPE coefficients is a Gram-matrix statement in a
   reflection-positive channel.
4. Angular variables use \(n_x\)-type notation so that \(\vac\) remains
   reserved for the vacuum.
5. A conformal block is an OPE-boundary-condition solution of the Casimir
   equation; a conformal partial wave is the single-valued Euclidean harmonic
   that combines the block and its shadow block and is normalized as part of
   the principal-series Plancherel resolution.
6. The scalar Casimir equation has two local branches with radial exponents
   \(\Delta\) and \(D-\Delta\); the OPE block is selected by normalizing the
   \(\Delta\) branch and setting the shadow-branch coefficient to zero.
7. Local existence and uniqueness of the OPE-normalized block follow from the
   finite-level descendant construction, invertibility of Gram matrices after
   quotienting null descendants, and radial OPE convergence.

## Figures

- Keep figures that show the separating sphere, radial ordering, or
  conformal-block channel.

## Checks

- Do not import analytic or numerical bootstrap claims into the core chapter.
- Every convergence claim must state the Hilbert-space and spectral
  hypotheses being used.
- Do not use ``conformal block'' and ``conformal partial wave''
  interchangeably; later inversion formulae use the latter.

## Audit Notes

- 2026-05-24 issue pass: addressed #273 by displaying the scalar Casimir
  differential operator in \(u,v\), recording the \(z,\bar z\) form, stating
  the \(\Delta\) and \(D-\Delta\) Frobenius branches, and proving local
  existence/uniqueness of the OPE-normalized block through the finite-level
  descendant Gram construction.
- 2026-05-24 issue pass: addressed #274 by adding a subsection distinguishing
  OPE-normalized conformal blocks from shadow-projector conformal partial
  waves and recording the associated Plancherel normalization convention.
