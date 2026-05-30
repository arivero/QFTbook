# Forty-Seventh Cross-Volume Wrapper Pass

Date: 2026-05-29

Purpose: continue issue #691 by reading theorem-family statements whose
proofs still looked like finite calculations, transport arguments, or direct
consequences of strong hypotheses.  The pass distinguishes genuine machinery
from support lemmas and removes proposition form where the statement is mainly
bookkeeping.

## Demoted To Lemmas

- Volume II, Chapter 6:
  `Distributional Cauchy formula for the six-dimensional wave equation`.
  The distributional Cauchy representation is a technical PDE lemma used by the
  analyticity argument, not a QFT theorem-level assertion.
- Volume II, Chapter 12:
  `Existence and uniqueness of the MS pole recursion`.  The result is the
  finite-dimensional invertible-sector recursion after the pole equations and
  nonresonance hypotheses have been specified.
- Volume II, Chapter 17b:
  `Exact center symmetry of pure thermal lattice Yang--Mills`.  This is the
  finite-lattice center-transformation check that preserves Haar measure and
  plaquettes.
- Volume II, Chapter 23:
  `Euclidean convexity at finite regulator`.  The calculation is the
  Holder/Legendre-Fenchel convexity lemma for a positive finite regulator.
- Volume V, Chapter 11:
  `Flatness and four-point reduction`.  The KZ flatness verification is the
  infinitesimal-braid identity plus the four-point specialization.
- Volume VI, Chapter 8:
  `Yang-Baxter equation for the soliton matrix part`.  The component
  verification of the displayed sine-Gordon matrix factor is retained as a
  lemma.
- Volume VII, Chapter 13:
  `Generic rank certificate for the one-copy intertwiner`.  The row-echelon
  certificate is finite linear algebra supporting the planar N=4 S-matrix
  construction.
- Volume XI, Chapter 9:
  `Passing invariance through a cutoff limit`.  This is a Markov-semigroup
  transport lemma; the hard work is tightness, compact-set convergence, and
  identification of the limiting law.
- Volume XI, Chapter 9:
  `Finite negative-sector coordinates for dynamic Phi^4_3`.  The homogeneity
  ledger and coordinate domination are essential support infrastructure, but
  the proof is a finite-sector enumeration and reexpansion calculation.
- Volume XI, Chapter 10:
  `Feshbach--Schur reduction with resolvent control`.  This is the finite
  block-matrix Schur complement lemma used by truncation analysis.
- Volume XI, Chapter 11:
  `Exact lattice chiral symmetry and the finite Berezinian`.  The
  Ginsparg--Wilson action variation, Berezinian, and finite index trace are
  convention-sensitive and important, but their local status is lemma-level
  finite algebra.

## Reframed As Prose / Remark

- Volume X, Chapter 12:
  `Physical collective-mode content of ideal CFL` was removed from
  proposition/proof form and rewritten as a paragraph-level calculation in the
  ideal CFL effective-coordinate chart.  The text now states explicitly that
  the result is a consequence of the assumed chart, not an independent theorem
  about dense QCD.
- Volume XI, Chapter 9:
  `Why the Sobolev DPD closure is two-dimensional` was rewritten as a remark
  titled `Sobolev DPD closure and the three-dimensional obstruction`.  The
  exponent calculation remains visible, but the title and environment no
  longer pretend to be theorem-level structure.

## Retained After Reading

The following candidates remain in theorem-family form after semantic reading:

- local conformal-current Ward identity: the statement packages source-derived
  translation, trace, and conformal-current contact distributions in one chart;
- mid-link free-fermion reflection positivity and finite Grassmann reflection
  positivity: these encode the lattice-fermion reflection-positive crossing
  structure;
- finite-codimension critical surface: the proof uses the stable graph and
  submersion/implicit-function theorem, not merely terminology;
- isolated spectral atom gives a first-sheet pole: the spectral atom-to-pole
  argument is load-bearing foundational material;
- Euclidean radial OPE convergence and Lorentzian OPE continuation: these
  depend on radial spectral estimates and analytic continuation domains;
- form-factor exchange from factorized scattering: this is the wall-crossing
  relation defining locality in the factorized form-factor framework;
- Osterwalder-Seiler reflection positivity for Wilson action and character
  criterion: these are finite-lattice positivity mechanisms, not mere
  substitutions.

## Harness Update

`tools/audit_theorem_form.py` now rejects reintroducing the old DPD obstruction
title or the CFL collective-mode calculation as theorem-family wrappers.

## Inventory After This Pass

- theorem: 87
- proposition: 278
- lemma: 103
- corollary: 10
- theorem-family total: 478
- proof: 473
- remark: 313
- example: 75

Working estimate: the obvious finite-calculation proposition layer is now much
thinner.  The remaining #691 work is mostly semantic: statements whose
hypotheses contain the true difficulty, propositions whose proof is a named
standard theorem applied to a QFT object, and theorem labels attached to
criteria or conditional constructions.
