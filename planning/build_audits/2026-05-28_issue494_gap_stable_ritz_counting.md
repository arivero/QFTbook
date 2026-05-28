# Issue 494 Gap-Stable Ritz Counting Pass

## Scope

This pass deepens the fixed-Hamiltonian part of Volume XI, Chapter 10.  The
earlier Rayleigh--Ritz proposition gave convergence of individual Ritz values
under a form-norm approximation hypothesis.  For spectral comparisons in TCSA,
TFFSA, and DLCQ, one also needs a statement about spectral windows: a numerical
method should not only move a named eigenvalue, but eventually count the same
number of levels in an isolated gap.

## Changes

- Added Proposition `Gap-stable Ritz counting for a fixed Hamiltonian` to
  `monograph/tex/volumes/volume_xi/chapter10_hamiltonian_truncation_dlcq_benchmarks.tex`.
- The proposition states precise hypotheses: lower-bounded self-adjoint
  Hamiltonian, closed quadratic form, increasing form-norm dense finite trial
  spaces, and an interval `(a,b)` below the essential spectrum with endpoints
  in the resolvent set.
- The proof uses the prior Rayleigh--Ritz convergence, min--max lower bounds,
  and a min--max exclusion of spurious extra Ritz levels below `b`.
- The text explicitly says that the theorem applies to one fixed quadratic
  form only and does not justify counterterm-dependent truncations without a
  separate convergence theorem.
- Updated the Chapter 10 dossier with the spectral-counting notation and claim.

## Mathematical Status

The statement is a fixed-operator Galerkin theorem for isolated spectral
windows below the essential spectrum.  It is deliberately not a theorem about
renormalized finite matrices whose counterterms depend on the cutoff; those
families still require an independent convergence statement in an appropriate
operator or form topology.

## Verification

Verification for this pass should include:

- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`
