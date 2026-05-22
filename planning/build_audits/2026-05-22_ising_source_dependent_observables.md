# Ising Source-Dependent Observables Audit

Date: 2026-05-22

This pass carries the operator-source/contact-coordinate framework into the
Ising universality chapter.  The goal is to formulate microscopic observable
limits as source-dependent distributions, not merely as separated-point
asymptotic formulas.

## Manuscript Changes

- Updated
  `monograph/tex/volumes/volume_ii/chapter15_the_statistical_ising_model_and_universality.tex`.
- Added "Observable Limits as Source-Dependent Distributions."
- Defined smeared renormalized lattice spin and energy observables
  \(\Sigma_a(f)\) and \(E_a(g)\) with the nonuniversal normalization constants
  from the scaling-field expansion.
- Defined a source-dependent scaling limit using local source maps
  \(\eta_a=\mathcal Z_a(\eta)\) and source-local vacuum subtractions
  \(P_a(\eta)\).
- Proved that, once linear source normalizations are fixed, microscopic
  realizations in the same fixed-point class have the same noncoincident
  continuum kernels, while higher local source jets and \(P_a\) affect only
  contact-term extensions.

## Planning Updates

- Updated the Ising/universality dossier with the new construction task,
  claim, and audit note.
- Updated the master architecture and dependency map so the next target is
  carrying the source-dependent observable framework into the opening
  fixed-point/CFT data chapter and Ward-identity contact conventions.

## Verification

- Ran `git diff --check`; no whitespace errors.
- Ran strict phrase scans on the edited manuscript and planning files; hits
  were confined to pre-existing manuscript clarifications and planning source
  references/guardrails.
- Built the monograph with `tools/build_monograph.sh`; the strict monograph
  text audit and LaTeX log scan were clean.
- Rendered and inspected the new section pages at
  `/tmp/qft_ising_source_dependent_observables-331.png` and
  `/tmp/qft_ising_source_dependent_observables-332.png`; the displayed
  source-functional formulas, proposition, proof continuation, and adjacent
  section transition were legible and nonoverlapping.
