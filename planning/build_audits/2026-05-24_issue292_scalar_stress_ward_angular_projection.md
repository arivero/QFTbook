# Issue #292 Scalar--Scalar--Stress Ward Angular Projection Pass

## Scope

- Addressed GitHub issue #292:
  `[Vol V Ch 8] Ward-identity normalization C_{12T} derivation skips n^2=1 step`.
- Target chapter:
  `monograph/tex/volumes/volume_iii/chapter08_correlation_functions_and_conformal_frames.tex`.

## Content Added

- Expanded the angular projection in the scalar--scalar--stress Ward
  derivation:
  \[
    n^\mu n^\nu(n_\mu n_\nu-\delta_{\mu\nu}/D)
    =
    (n^\mu n_\mu)(n^\nu n_\nu)-D^{-1}n^\mu n_\mu.
  \]
- Stated explicitly that \(n^\mu n_\mu=1\) pointwise on the unit sphere,
  giving the integrand \(1-1/D\) and therefore
  \(A_{D-1}(1-1/D)\).
- Recorded the check in the Chapter 8 dossier.

## Verification Targets

- The derivation must no longer hide the \(n^2=1\) contraction.
- The sign and orientation conventions in the Ward coefficient derivation
  remain unchanged.
