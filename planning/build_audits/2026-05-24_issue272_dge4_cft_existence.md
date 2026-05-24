# Issue #272 Audit: \(D\geq4\) CFT Existence Status

## Scope

- GitHub source of truth: issue #272 was verified open before this pass.
- Manuscript target: `monograph/tex/volumes/volume_iii/chapter01_fixed_points_and_conformal_data.tex`.
- Dossier target: `planning/chapter_dossiers/volume_iii/chapter01_fixed_points_conformal_data.md`.

## Manuscript Change

- Added `Remark~\ref{rem:cft-opening-dgefour-existence}` after the Ising
  numerical provenance remark, where the opening CFT chapter first displays
  \(D=2,3\) Ising data.
- Defined the distinction used in the chapter between free conformal theories
  with Wick factorization and dynamically interacting stress-tensor CFTs.
- Recorded explicit free unitary Gaussian examples in \(D\geq4\): improved
  massless scalars, massless Dirac fields, and Maxwell theory in \(D=4\).
- Stated the status of the Wilson--Fisher \(\epsilon\)-expansion as formal
  perturbative CFT data in nonintegral dimension, not an integer-dimensional
  Hilbert-space construction by itself.
- Connected the four-dimensional scalar route to critical Ising and
  \(\phi^4_4\) triviality constraints.
- Separated gauge-theory fixed-point mechanisms, including Banks--Zaks and
  later supersymmetric gauge-theory constructions, from rigorous use in this
  core CFT volume: their stress tensor, positivity, locality, spectrum, and
  conformal Ward identities must be supplied as data.

## Verification

- Passed: `git diff --check`.
- Passed: `tools/audit_monograph_text.sh`.
- Passed: `tools/audit_chapter_dossiers.sh`.
- Passed: `tools/build_monograph.sh`.
