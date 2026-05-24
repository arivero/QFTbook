# Issue #289 Lorentzian Conformal Group Cover Pass

## Scope

- Addressed GitHub issue #289:
  `[Vol V Ch 2] Lorentzian conformal group: algebra given, group not constructed`.
- Target chapter:
  `monograph/tex/volumes/volume_iii/chapter02_conformal_killing_vectors_and_the_conformal_group.tex`.

## Content Added

- Added Section `sec:lorentzian-conformal-group-cover`.
- Constructed compactified Minkowski space as the projective null cone in
  \(\mathbb R^{D,2}\) with a stated ambient bilinear form.
- Identified the Poincare patch by \(X^+=1\), \(X^\mu=x^\mu\),
  \(X^-=x^2\).
- Defined the connected projective Lorentzian conformal group
  \(PO_0(D,2)\) and separated it from the universal cover.
- Wrote explicit ambient linear formulae for Lorentz transformations,
  translations, dilatations, and special conformal transformations, deriving
  the usual rational special conformal action on the patch.
- Stated that the Hilbert space of a unitary Lorentzian CFT carries a
  strongly continuous unitary representation of the universal cover, with the
  lift of the maximal compact subgroup covered by
  \(\operatorname{Spin}(D)\times\mathbb R\).
- Explained why the cover is necessary: \(2\pi\) cylinder-time periodicity
  would incorrectly force integral scaling dimensions, and spinorial
  operators require the spin cover of spatial rotations.

## Verification Targets

- The chapter must no longer pass from the algebra \(\mathfrak{so}(D,2)\) to
  Hilbert-space covariance without constructing the finite group and its
  cover.
- Later radial-quantization uses of conformal covariance should be read as
  covariance under the universal cover, projected to spacetime only after
  quotienting.
