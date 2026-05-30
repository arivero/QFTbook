# Pure SYM GEVP Removal Pass

Date: 2026-05-30

Scope:
- `monograph/tex/volumes/volume_vii/chapter07b_susy_yang_mills_family_spectra.tex`
- `planning/12_strict_writing_harness.md`

Reason:
- Xi flagged that even an "application of the general spectral estimator" is
  misplaced inside the pure \(\mathcal N=1\) SYM spectral chapter when the
  chapter does not use it to extract an actual supersymmetric-gauge-theory
  result.

Change:
- Removed the explicit channel-by-channel GEVP equation from the pure-SYM
  chapter.
- Removed the generic projected-correlator residual estimate from the
  pure-SYM chapter.
- Reframed the pure-SYM section so it stops at the model-specific spectral
  data: even scalar, odd scalar, and fermionic source matrices; spin/rest-frame
  projection; gluino-mass tuning; finite-volume and continuum limits; and the
  supersymmetry-restoration mass-splitting diagnostic.
- Tightened the writing harness: if a specialized chapter has no concrete
  model-specific result to extract using a general method, the method must not
  be exposed there.

Remaining architecture:
- The general finite-volume correlator-matrix and GEVP machinery remains in
  the Volume XI lattice/methodological chapter.
- The pure-SYM chapter may cite or use such machinery in the future only when
  it presents an actual computation, theorem, or benchmark specific to
  \(\mathcal N=1\) SYM.
