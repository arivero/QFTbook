# Issue 396: Gamma-Five Convention Conflict

Date: 2026-05-24.

Issue:

- GitHub #396 flagged an inconsistent chirality-matrix sign between the
  spinor-field conventions and the anomaly/dimensional-regulator discussion.
- The monograph-wide Lorentzian convention is mostly plus,
  \(\eta=\operatorname{diag}(-,+,+,+)\), with
  \[
    \gamma_5=-\ii\gamma^0\gamma^1\gamma^2\gamma^3,
    \qquad
    \epsilon^{0123}=+1,
  \]
  and therefore
  \[
    \operatorname{tr}
    \left(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\right)
    =
    4\ii\epsilon^{\mu\nu\rho\sigma}.
  \]

Audit:

- `chapter20_chiral_axial_anomalies.tex` already used the monograph-wide
  sign at the chapter opening and in the dimensional-reduction triangle
  calculation.
- `volumes/volume_i/chapter16a_spinor_conventions.tex` records the same sign and trace
  identity as the global convention.
- `chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex` still had the
  opposite sign in the definition of the Breitenlohner--Maison/'t
  Hooft--Veltman chiral data.

Fix:

- Corrected the chapter 18 dimensional-regulator definition to
  \(\gamma_5=-\ii\gamma^0\gamma^1\gamma^2\gamma^3\).
- Added the associated trace identity in the same definition, with an explicit
  cross-reference to the chapter-local spinor-convention section, so that anomaly and
  regulator discussions use the same orientation and chirality data.
- Updated the BRST chapter dossier.

Verification to run:

- `rg -n -F "\\gamma_5=\\ii" monograph/tex`
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
