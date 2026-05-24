# Issue #252 Anomaly Inflow Pass

## Scope

- Oldest active GitHub issue: `#252`, on the absence of anomaly inflow in the
  local and global anomaly chapters.
- Manuscript loci:
  - `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
  - `monograph/tex/volumes/volume_ii/chapter21_global_anomalies_spontaneous_symmetry_breaking_and_pions.tex`
- Planning loci:
  - `planning/chapter_dossiers/volume_ii/chapter20_chiral_axial_anomalies.md`
  - `planning/chapter_dossiers/volume_ii/chapter21_global_anomalies_ssb_pions.md`

## Content Added

- Added a local-anomaly inflow section after the descent construction:
  \[
    W_X^{\mathrm{bulk}}[\mathsf A_X]=-\int_X I_5^{(0)}(\mathsf A_X),
    \qquad
    \delta_\lambda W_X^{\mathrm{bulk}}
    =
    -\int_{\partial X}I_4^{(1)}(\lambda,\mathsf A_X).
  \]
- Displayed the bulk-boundary cancellation identity
  \[
    \delta_\lambda(W_M+W_X^{\mathrm{bulk}})
    =
    \int_M I_4^{(1)}-\int_{\partial X}I_4^{(1)}
    =
    0
  \]
  in the same convention as the chapter's consistent anomaly.
- Named and formulated the Callan--Harvey domain-wall realization: localized
  chiral modes and a jumping bulk Chern--Simons response carry opposite gauge
  variations.
- Added a finite anomaly-inflow section in the global-anomaly chapter:
  \[
    Z[B^g]/Z[B]=\mathcal I_5[X_g,B_g],
  \]
  where \(X_g\) is the mapping torus.
- Connected the existing \(SU(2)\) global anomaly calculation to the inflow
  phase
  \[
    \mathcal I^{SU(2)}_5[X_g,E_g]=(-1)^{\zeta(X_g,E_g)}.
  \]
- Added a careful SPT/cobordism paragraph that states the needed tangential,
  symmetry-background, invertibility, and Pfaffian-line data.
- Added a WZW cross-link: the gauged Wess--Zumino--Witten functional is
  described as a Goldstone-field realization of the same inflow class.
- Updated both chapter dossiers.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
