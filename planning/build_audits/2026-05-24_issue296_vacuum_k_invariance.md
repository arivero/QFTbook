# Issue #296 Vacuum Special-Conformal Invariance Pass

## Scope

- Addressed GitHub issue #296:
  `[Vol V Ch 8] Vacuum K_mu-invariance not derived from P_mu-invariance + spectrum condition`.
- Target chapter:
  `monograph/tex/volumes/volume_iii/chapter08_correlation_functions_and_conformal_frames.tex`.

## Content Added

- Added Lemma `lem:vacuum-k-invariance-from-radial-spectrum`.
- Stated the exact radial assumptions:
  \(\widehat D_{\rm rad}\) is nonnegative and self-adjoint,
  \(\widehat D_{\rm rad}|\Omega\rangle=0\), and
  \([\widehat D_{\rm rad},\widehat K_\mu]=-\widehat K_\mu\) holds on a common
  domain containing the vacuum.
- Proved that
  \[
    \widehat D_{\rm rad}\widehat K_\mu|\Omega\rangle
    =
    -\widehat K_\mu|\Omega\rangle .
  \]
  A nonzero \(\widehat K_\mu|\Omega\rangle\) would therefore be an eigenvector
  of \(\widehat D_{\rm rad}\) with eigenvalue \(-1\), contradicting the radial
  spectrum condition.
- Updated the chapter opening so the global Ward identity refers to the
  derived special-conformal vacuum invariance.
- Updated the Chapter 8 dossier.

## Verification Targets

- The chapter must not treat \(K_\mu|\Omega\rangle=0\) as a bare assumption.
- The proof must explicitly use the radial conformal commutator and
  nonnegativity of \(D_{\rm rad}\).
- The result must be tied to the common vacuum identification introduced in
  the issue #295 pass.
