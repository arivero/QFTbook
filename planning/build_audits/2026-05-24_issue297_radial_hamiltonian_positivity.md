# Issue #297 Radial Hamiltonian Positivity Unification Pass

## Scope

- Addressed GitHub issue #297:
  `[Vol V Chs 4 vs 9] Radial Hamiltonian positivity hypothesis inconsistent across chapters`.
- Target chapters:
  `monograph/tex/volumes/volume_iii/chapter04_radial_quantization_and_state_operator_correspondence.tex`
  and
  `monograph/tex/volumes/volume_iii/chapter09_operator_product_expansion.tex`.

## Content Added

- Chapter 4 already states in Hypothesis `hyp:radial-reconstruction-data` that
  dilatations act by a nonnegative self-adjoint operator \(D_{\rm rad}\).
- Added an explicit explanatory paragraph after the hypothesis:
  the nonnegativity of \(D_{\rm rad}\) is the radial spectrum condition for
  the vacuum representation.
- Distinguished that hypothesis from the Chapter 7 unitarity lower bounds for
  non-identity primaries, which are derived later from descendant Gram
  positivity.
- Changed the Chapter 9 radial OPE convergence proof to use \(D_{\rm rad}\)
  by name and to identify it as the nonnegative self-adjoint radial
  Hamiltonian of `hyp:radial-reconstruction-data`.
- Updated the Chapter 4 and Chapter 9 dossiers.

## Verification Targets

- Chapter 4 and Chapter 9 must use the same radial spectrum hypothesis.
- No chapter should silently strengthen the radial reconstruction assumptions.
- The ground-state/spectrum condition \(D_{\rm rad}\ge0\) must remain distinct
  from the nontrivial unitarity bounds on primary dimensions derived in
  Chapter 7.
