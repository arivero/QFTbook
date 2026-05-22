# 2026-05-22 1PI/RG/Wilsonian Source Coverage Pass

## Scope

- Compared the operational source transcription for the second-sequence
  handwritten notes on generating functionals and the 1PI effective action
  against the current manuscript chapter
  `monograph/tex/volumes/volume_ii/chapter23_generating_functionals_and_the_one_particle_irreducible_effective_action.tex`.
- Compared the operational source transcription and Ben Lou comparison layer
  for the 1PI renormalization group, renormalized operators, trace identity,
  Wilson-Fisher fixed point, and Wilsonian effective action blocks against
  the current Volume II chapters 10, 12, 13, 14, and 16.
- This was a source-transcription audit, not a final handwritten-PDF visual
  certification pass.

## Findings

- The 1PI effective-action chapter contains the required source substance:
  regulated source functionals, connected generator, Legendre transform,
  inverse relation between \(W^{(2)}\) and \(\Gamma^{(2)}\), background-field
  shift, tadpole cancellation, tree reconstruction of connected functions
  from exact 1PI vertices, Euclidean convexity, Legendre-Fenchel language at
  finite regulator, and a zero-dimensional toy model.
- The 1PI RG chapter contains the required source substance:
  scale-dependent field normalization, symmetric Euclidean subtraction,
  one-loop \(\phi^4\) running with threshold factor, nearby-scale comparison,
  beta-function extraction, Landau-scale interpretation, general 1PI
  coordinates, Callan--Symanzik derivation from bare-scale independence,
  logarithmic consistency, and scheme changes.
- The Wilsonian chapter contains the required source substance:
  smooth cutoff covariance, source-supported generating-functional equality,
  covariance split, shell Gaussian integral, Wilson--Polchinski equation with
  sign derivation, linearized relevance convention, quartic-sextic slaving,
  and the perturbative continuum-limit construction.

## Patch Made

- Tightened the scheme-change discussion in the 1PI RG chapter.  The previous
  prose displayed the first nonlinear redefinition coefficient and then wrote
  a third beta-function coefficient transformation that could be misread as
  exact.  The revised text states the finite redefinition hypotheses and
  displays the cubic redefinition coefficient explicitly:
  \[
    \widetilde\lambda
    =
    \lambda+\alpha\lambda^2+\rho\lambda^3+O(\lambda^4),
    \qquad
    \widetilde b_3=b_3-\alpha b_2+(\rho-\alpha^2)b_1 .
  \]

## Register Update

- Promoted the source-register status of 253b pp. 71--80, pp. 97--110, and
  pp. 147--156 from `partial` to `mapped after 2026-05-22 source-transcription audit`.
- These rows should be promoted to `certified` only after a handwritten-PDF
  figure and derivation pass on the compiled manuscript.

