# Analytic uniqueness matching wrapper demoted

Date: 2026-05-31

Related issue: GitHub #691, theorem/proof substance and anti-wrapper audit.

## Scope

This pass audited the sigma-model family matching block in
`volume_vi/chapter09_on_gross_neveu_sigma_model_families.tex`.
The former proposition "Analytic uniqueness of a matched two-particle kernel"
was a correct one-variable boundary-uniqueness step, but theorem-family form
overstated its role: all hard QFT content is in the regulator realization and
bootstrap datum, namely Haag--Ruelle scattering, meromorphic boundary values,
pole and residue control, finite-volume data, and form factors.

## Change

- Replaced the proposition/proof shell by the paragraph "Analytic uniqueness
  after regulator matching."
- Kept the full derivation: matrix-entry reduction, local pole cancellation,
  vanishing boundary distribution, Morera extension across a real interval,
  identity theorem, and meromorphic continuation across the removed divisors.
- Rewrote the surrounding status language so the paragraph identifies the
  construction-level data as the mathematical burden, instead of presenting
  an identity-theorem application as a QFT proposition.
- Added a theorem-form audit guard against reintroducing the old title as a
  theorem/proposition/lemma/corollary wrapper.
- Updated the Volume VI Chapter 09 dossier anti-wrapper ledger.

## Status

This is one more concrete #691 demotion.  The global semantic audit of
theorem-family statements remains open.
