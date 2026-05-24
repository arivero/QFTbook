# Issue 246 Kugo--Ojima Quartet And Confinement Criterion

Date: 2026-05-24

Scope:
- Strengthened
  `monograph/tex/volumes/volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex`.
- Updated
  `planning/chapter_dossiers/volume_ii/chapter18_gauge_fixing_ghosts_brst.md`.
- Addressed GitHub issue #246 on the missing Kugo--Ojima quartet mechanism and
  nonperturbative confinement criterion.

Changes:
- Renamed the earlier doublet positivity theorem so it is not mistaken for the
  full Kugo--Ojima confinement criterion.
- Added a dedicated Kugo--Ojima section defining BRST quartets as conjugate
  doublet pairs in the indefinite metric state space.
- Stated the Landau-gauge Kugo--Ojima two-point function, the
  \(F_{\mathrm{KO}}(0)=1\) / \(u(0)=-1\) infrared condition, and the
  conditional relation to the ghost dressing function.
- Formulated the Kugo--Ojima confinement criterion as a conjectural
  nonperturbative BRST scenario with explicit hypotheses on the BRST charge,
  color charges, massless boundary terms, and longitudinal singularities.
- Recorded the Gribov/lattice status: minimal-Landau-gauge lattice and
  Gribov--Zwanziger infrared analyses generally do not realize the original
  Kugo--Ojima condition, while this is not a contradiction of gauge-invariant
  confinement diagnostics.
- Corrected the dossier's antighost convention to match the manuscript's
  \(b_A=\bar c_A\).

Verification:
- `git diff --check` clean.
- `tools/audit_monograph_text.sh` clean.
- `tools/audit_chapter_dossiers.sh` clean.
- `tools/build_monograph.sh` clean; rebuilt
  `monograph/tex/main.pdf`.
