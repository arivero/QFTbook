# Build Audit: Issue #605 SQCD Duality And Phase Ledger

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`.
- Issue: GitHub #605, selected four-dimensional `N=1` SCFT/gauge-dynamics
  foundations, with emphasis on general SQCD duality rather than string or
  compactification motivation.
- Main TeX target:
  `monograph/tex/volumes/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`.
- Dossier:
  `planning/chapter_dossiers/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.md`.
- New calculation check:
  `calculation-checks/susy_n1_sqcd_duality_checks.py`.

## Source Leads

- Local stringbook convention comparison:
  `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  especially the Wilsonian/NSVZ convention discussion near lines
  23170--23210 and the RG-cascade/Seiberg-duality discussion near lines
  18590--18670.  The monograph keeps only QFT-side conventions and excludes
  string compactification and holographic derivations.
- Local arXiv source payload:
  `references/susy_gauge_dynamics_localization/issue605_kw_ks/eprints/hep-th-9411149.eprint`.
  Used as a historical source lead for the SQCD magnetic rank, charge table,
  phase ranges, and anomaly-matching targets.  The monograph text rebuilds
  the charge and anomaly arithmetic explicitly and marks the full IR
  equivalence as a quoted nonperturbative input.

## Substantive Changes

- Added a general SQCD Seiberg-duality section before the KW/KS examples:
  electric and magnetic field tables, magnetic rank
  `tilde N_c=N_f-N_c`, baryon-charge normalization, meson normalization, and
  `W_mag=M q tilde q / mu_*`.
- Added `hyp:sqcd-ir-comparison-hypotheses`, making explicit the continuum,
  current-identification, superconformal-R, chiral-sector, and
  deformation-matching assumptions needed before treating electric and
  magnetic Lagrangians as the same infrared QFT.
- Proved the magnetic gauge-`R` anomaly cancellation, magnetic
  superpotential \(R=2\), magnetic NSVZ numerator cancellation, and full
  electric/magnetic matching of the displayed global 't Hooft anomalies.
- Added a phase ledger separating instanton/holomorphic-decoupling cases
  from duality-dependent cases: ADS runaway, quantum-modified moduli space,
  `N_f=N_c+1` confinement, free magnetic range, interacting conformal
  window, and free electric range.
- Added a dimension and \(R\)-charge check of the `N_f=N_c+1` confining
  superpotential.
- Added exact rational calculation checks for the dual-rank map, baryon map,
  NSVZ conventions, anomaly matching, confining-superpotential arithmetic,
  and phase inequalities.

## Verification

- `python3 calculation-checks/susy_n1_sqcd_duality_checks.py` passed.
- `python3 calculation-checks/susy_instanton_nekr_checks.py` passed.
- `tools/run_calculation_checks.sh` passed, including the Wolfram
  gamma-trace/anomaly-normalization check.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed; the script's TeX log scan was clean.
- `pdfinfo monograph/tex/main.pdf` reports 1547 pages.

## Status

Do not close #605 from this pass.  The pass substantially develops the
general SQCD duality and phase foundation needed by the KW/KS examples, but
the full continuum construction of Seiberg duality and the interacting SQCD
SCFT remains an honest quoted-theorem/nonperturbative-input boundary.
