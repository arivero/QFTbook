# Issue #594 Conformal-Manifold Framework Pass

## Scope

This pass addresses the general-framework part of GitHub issue #594 without
claiming to close the issue.  The existing manuscript already had worked
supersymmetric slices for KW, \(\mathcal N=4\) Yang--Mills, and ABJM, but the
CFT volume did not state a general local definition of conformal manifold or
explain what exactly marginal means as a source-coordinate statement.

## Manuscript Changes

- Added `Conformal Manifolds and Exactly Marginal Deformations` to
  `monograph/tex/volumes/volume_iii/chapter01_fixed_points_and_conformal_data.tex`.
- Defined a local conformal-family datum: parameter manifold, fixed-point
  source functionals, dimension-\(D\) scalar-operator bundle, tangent-operator
  map, and renormalized integrated insertion formula with contact terms.
- Formulated the local exact-marginality source-coordinate criterion
  \(\mathcal M_{\rm loc}=\{\beta=0\}/G_{\rm red}\) and the rank count
  \(m-r_\beta-r_{\rm red}\), with emphasis that the beta obstructions,
  current/virial obstructions, redundancies, and contact chart are the
  substantive inputs.
- Connected second-order conformal perturbation theory to OPE collision
  singularities of dimension-\(D\) operators.
- Defined the general-\(D\) Zamolodchikov metric as the separated two-point
  coefficient on tangent operators, quotienting redundant/null directions and
  displaying the coordinate transformation law.
- Cross-linked the framework to the already-developed KW, \(\mathcal N=4\),
  and ABJM examples in Volume VII.

## Calculation Check

- Added `calculation-checks/conformal_manifold_checks.py`.
- The check verifies the finite linear algebra used in the text:
  rank-one KW dimension count, one-dimensional local \(\mathcal N=4\)
  \(\tau\)-chart, zero-dimensional standard ABJM fixed-datum locus,
  beta/redundancy quotient rank count, Zamolodchikov metric coordinate
  transformation, and quotient by a redundant null marginal direction.

## Status

This is not a closure of #594.  Remaining work includes a fuller dedicated
chapter-level treatment of global conformal manifolds, Kähler/special geometry
under supersymmetric hypotheses, D1-D5 and other two-dimensional examples, and
non-supersymmetric exactly marginal deformations where rigorous source-coordinate
control is available.
