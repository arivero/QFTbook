# Build Audit: Issue #592 ADS Higgs-Patch Instanton Foundation

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`.
- Issue: GitHub #592, supersymmetric gauge-theory instanton calculus slice.
- Main TeX target:
  `monograph/tex/volumes/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`.
- Dossier:
  `planning/chapter_dossiers/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.md`.
- Calculation check:
  `calculation-checks/susy_instanton_nekr_checks.py`.

## Source Leads

- Local stringbook convention comparison:
  `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`, especially
  the supersymmetric Wilsonian/NSVZ and ADS discussion near lines
  23170--23220.  The monograph text keeps only the four-dimensional QFT
  instanton calculation and does not import string/D-brane motivation.
- Existing local source payloads under
  `references/susy_gauge_dynamics_localization/issue592_instanton_nekr/`.

## Substantive Changes

- Added the explicit Higgs-patch collective-coordinate ledger for the
  `N_f=N_c-1` ADS instanton calculation.
- Displayed local diagonal Higgs coordinates on the `det M != 0` patch and
  proved that the gauge group is completely Higgsed there.
- Counted the charge-one instanton bosonic collective coordinates:
  translations, size, and orientation space, giving real dimension `4N_c`
  uniformly including `N_c=2`.
- Counted the adjoint and matter fermion zero modes by the same
  index-theorem convention used in the BPST instanton chapter.
- Made the Yukawa-lifting rank statement explicit: nonzero Higgs
  expectation values lift `2N_c-2` non-Goldstino gaugino modes together with
  the `2N_c-2` matter zero modes, leaving precisely the two Grassmann modes
  needed for a `d^2 theta` superpotential.
- Rewrote the ADS one-instanton proof around the reduced integral
  `d^4x_0 d^2 eta Lambda_h^(2N_c+1) F(M)`, the Higgs large-size cutoff, and
  the holomorphic/flavor/dimension/R-charge derivation of `F(M)=kappa/det M`.
- Extended the instanton calculation check with exact counts for the
  orientation dimension, bosonic moduli, Yukawa-lifting rank, and reduced
  determinant dimension.

## Verification

- `python3 calculation-checks/susy_instanton_nekr_checks.py` passed.
- `tools/run_calculation_checks.sh` passed, including the Wolfram
  gamma-trace/anomaly-normalization check.
- `tools/audit_monograph_text.sh` passed after replacing imprecise
  "schematic" wording with reduced-integral/zero-mode terminology.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed; the script's TeX log scan was clean.
- `pdfinfo monograph/tex/main.pdf` reports 1548 pages.

## Status

Do not close #592 from this pass.  The ADS Higgs-patch derivation is now more
self-contained inside the supersymmetric gauge-dynamics chapter, but the
dedicated cross-volume instanton-measure construction requested by #592
remains open.
