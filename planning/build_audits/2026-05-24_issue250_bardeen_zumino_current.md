# Issue #250 Bardeen--Zumino Current Pass

## Scope

- Oldest active GitHub issue: `#250`, on the missing explicit component form
  of the Bardeen--Zumino current.
- Manuscript locus:
  `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`.
- Planning locus:
  `planning/chapter_dossiers/volume_ii/chapter20_chiral_axial_anomalies.md`.

## Content Added

- Kept the existing anti-Hermitian descent convention
  \(\mathsf A=-\ii A\), \(\mathsf F=d\mathsf A+\mathsf A^2\), and
  \(\kappa=\ii/(24\pi^2)\).
- Displayed the Bardeen--Zumino component current
  \[
    J_{\mathrm{BZ}}^{a\mu}
    =
    \frac{\kappa}{2}\epsilon^{\mu\nu\rho\sigma}
    \operatorname{tr}_R T_R^a
    (\mathsf A_\nu\mathsf F_{\rho\sigma}
    +\mathsf F_{\rho\sigma}\mathsf A_\nu
    -\mathsf A_\nu\mathsf A_\rho\mathsf A_\sigma).
  \]
- Expanded \(\mathsf F_{\rho\sigma}\) and displayed the derivative polynomial
  with the matrix ordering explicit:
  \[
    \kappa\epsilon^{\mu\nu\rho\sigma}\operatorname{tr}_R T_R^a
    (\mathsf A_\nu\partial_\rho\mathsf A_\sigma
    +\partial_\rho\mathsf A_\sigma\mathsf A_\nu
    +\tfrac12\mathsf A_\nu\mathsf A_\rho\mathsf A_\sigma
    +\mathsf A_\rho\mathsf A_\sigma\mathsf A_\nu).
  \]
- Updated the chapter dossier with the component polynomial and the audit
  note.

## Verification

- Clean:
  - `git diff --check`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `tools/build_monograph.sh`
