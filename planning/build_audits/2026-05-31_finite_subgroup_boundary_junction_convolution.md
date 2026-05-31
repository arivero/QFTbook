# Finite Subgroup Boundary Junction Convolution Pass

Date: 2026-05-31

## Trigger

Issue #703 still asks for stronger finite-gauge/TQFT boundary and junction
comparisons after the Abelian and subgroup-boundary passes.  The missing
finite operation was the actual composition of subgroup-boundary interval
sectors by a finite path-integral span.

## Edits

- Added the subgroup-boundary junction convolution proposition to Volume
  VIII, Chapter 11.
- Defined \(\mathcal V(H_i,H_j)=\operatorname{Fun}(G,\mathbb C)^{H_i\times
  H_j}\) for interval sectors between subgroup boundaries.
- Wrote the finite junction field groupoid
  \(G^2//(H_0\times H_1\times H_2)\) and the push-pull span to the two
  incoming interval groupoids and the outgoing interval groupoid.
- Derived the normalized convolution
  \[
    (f\star_{H_1}k)(g)=|H_1|^{-1}\sum_{xy=g}f(x)k(y),
  \]
  with the factor \(|H_1|^{-1}\) identified as the intermediate boundary
  gauge-volume denominator.
- Proved bi-invariance, associativity by finite Fubini, identity sectors,
  and integrality of double-coset structure constants from the free
  intermediate \(H_1\)-action on factorization sets.
- Added the \(S_3\), \(H=\langle(12)\rangle\), two-sector computation
  \(X^2=2\mathbf 1+X\).
- Extended `calculation-checks/finite_gauge_subgroup_boundary_checks.py` to
  verify the convolution operation, unit sectors, associativity, integral
  structure constants, and the \(S_3\) example in exact rational arithmetic.
- Updated the calculation-check manifest, chapter dossier, and statmech
  crosswalk.

## Verification Plan

- Run the extended subgroup-boundary calculation check.
- Run theorem-form, display-label, strict text, negative-scope, and
  chapter-dossier audits.
- Build the monograph and scan the log.
- Comment on #703 with the finite junction-convolution subpass while keeping
  the issue open for higher junctions, twisted examples, Hall-stability
  estimates, and remaining statmech crosswalk tracks.
