# 2026-05-29 Volume II Anti-Wrapper Pass

## Scope

Read the Volume II theorem-family statements flagged by the short-proof
calculation heuristic.  The heuristic was used only to locate candidates; each
decision was made from the surrounding statement and proof.

## Demoted To Worked Paragraphs

- `Eikonal AGK cancellation as a factorial-moment identity`: a Poisson
  generating-function derivative and coefficient identity.  The important
  content is its restricted one-channel eikonal status.
- `Leading weak-coupling \(1S\) hyperfine coordinate`: a first-order
  pNRQCD contact-operator expectation value plus the Coulombic \(1S\)
  wavefunction at the origin.
- `Elastic unequal-mass projection`: the chosen partial-wave normalization,
  Legendre inversion, and elastic-unitarity coordinate.
- `Quarkonium \(J^{PC}\) rule`: Clebsch--Gordan, parity, and charge
  conjugation bookkeeping for the spectroscopy chart.
- `Custodial \(SU(2)\) and the tree-level \(\rho\) coordinate`: scalar
  invariant and electroweak mass-coordinate substitution.
- `Integrating out singlet neutrinos at tree level`: algebraic heavy-field
  elimination for the leading dimension-five operator coefficient.

## Retained For Later Strengthening

- `One-loop running factor in the one-instanton density`: retained because the
  proof uses scale covariance, zero-mode normalization, and RG invariance to
  determine the \((\mu\rho)^{b_0}\) factor; a later pass may still expand the
  determinant and scheme boundary.
- `Positive form of the subtracted kernel`: retained because the statement is
  a quadratic-form positivity result for the subtracted large-\(N\) two-
  dimensional QCD kernel; a later pass should sharpen the form-domain
  closure.

## Recurrence Guard

`tools/audit_theorem_form.py` now rejects the six demoted titles if they
reappear in theorem-family environments.

## Verification

The theorem-form/text/prose/display-label audits, `git diff --check`, and
the full monograph build were clean.  The rebuilt PDF has 2577 pages.
