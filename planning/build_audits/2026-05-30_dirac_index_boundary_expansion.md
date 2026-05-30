# Dirac index theorem boundary expansion

Date: 2026-05-30.

Targets:
- GitHub issue #696, anomaly quoted-theorem proof debt.
- Cross-cutting directive that quoted theorems must expose the mechanism and
  convention boundary rather than functioning as opaque citations.

Files touched:
- `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `planning/chapter_dossiers/volume_ii/chapter20_chiral_axial_anomalies.md`
- `calculation-checks/anomaly_polynomial_descent_checks.py`

Change:
- Added a mechanism paragraph after the closed spin Dirac index quoted theorem.
- Made the McKean--Singer heat-supertrace cancellation explicit:
  positive nonzero eigenvalues cancel pairwise between chiralities, leaving
  `dim ker D_+ - dim ker D_-`.
- Stated the remaining analytic theorem boundary: the local heat coefficient
  comes from Lichnerowicz formula, Chern--Weil invariance, and Getzler
  rescaling.
- Derived the monograph convention for the gauge four-form:
  `ch(E)=tr exp(i mathsf F/2pi)=tr exp(F/2pi)`, hence
  `[ch(E)]_4 = tr(F wedge F)/(8 pi^2)
  = epsilon tr(F F) d^4x/(32 pi^2)`.
- Extended the anomaly-polynomial calculation check to verify the
  four-dimensional closed-index coefficient in addition to the existing
  six-form descent coefficients.

Status:
- This does not prove the full Atiyah--Singer or APS index theorem in the
  monograph.  It narrows the quoted boundary by deriving the heat-supertrace
  and normalization parts actually used in the anomaly chapter.

