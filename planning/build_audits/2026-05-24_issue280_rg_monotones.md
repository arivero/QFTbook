# 2026-05-24 Issue #280 RG Monotones Pass

## Scope

- GitHub issue: #280, "[Vol V] a-theorem (Komargodski-Schwimmer) not
  mentioned".
- Manuscript target:
  `monograph/tex/volumes/volume_iii/chapter01_fixed_points_and_conformal_data.tex`.
- Dossier target:
  `planning/chapter_dossiers/volume_iii/chapter01_fixed_points_conformal_data.md`.

## Content Added

- Added `RG Monotones and Fixed-Point Ordering` to the opening CFT/fixed-point
  chapter.
- Defined an endpoint RG monotone for a stated class of unitary Lorentzian RG
  trajectories, with length scale \(R\) increasing toward the infrared.
- Added the two-dimensional \(c\)-function statement as a stress-tensor
  two-point construction with reflection-positivity hypotheses and endpoint
  limit \(c_{\rm UV}\geq c_{\rm IR}\).
- Added the three-dimensional entropic \(F\)-monotone
  \(\mathcal F(R)=R S'(R)-S(R)\), the strong-subadditivity/Lorentz-invariance
  monotonicity condition, and the endpoint identification with the \(S^3\)
  free energy under the required CFT/counterterm hypotheses.
- Added the four-dimensional Komargodski--Schwimmer mechanism:
  \(a_{\rm W}\) as Euler anomaly coefficient, weak spectator dilaton,
  Wess--Zumino anomaly matching, the forward four-dilaton amplitude
  \(\mathcal A(s)=2(a_{\rm UV}-a_{\rm IR})s^2/f^4+\cdots\), the dispersion
  sum rule, and positivity from the optical theorem.
- Stated status boundaries so the chapter does not promote monotonicity
  claims beyond their analytic assumptions.

## Harness

- Passed: `git diff --check`
- Passed: `tools/audit_monograph_text.sh`
- Passed: `tools/audit_chapter_dossiers.sh`
- Passed: `tools/build_monograph.sh`
