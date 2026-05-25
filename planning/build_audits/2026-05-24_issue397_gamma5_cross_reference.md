# Issue 397: Gamma-Five Cross-Reference

Date: 2026-05-24.

Issue:

- GitHub #397 reported a stale anomaly-chapter cross-reference claiming that
  the \(\gamma_5\) convention was fixed in the preceding QCD chapter.
- The QCD chapter is not the source of the gamma-matrix convention.  The
  convention is fixed in the spinor-field chapter and centralized in the
  chapter-local spinor-convention section.

Audit:

- A source scan found no remaining phrase `preceding QCD` in the anomaly
  chapter.
- The chapter opening already uses
  \(\gamma_5=-\ii\gamma^0\gamma^1\gamma^2\gamma^3\) and
  \(\operatorname{tr}(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)
  =4\ii\epsilon^{\mu\nu\rho\sigma}\).

Fix:

- Strengthened the chapter opening so the convention is explicitly attributed
  to `chapter16_spinor_fields_fermionic_statistics_and_grassmann_path_integrals.tex`
  and `volumes/volume_i/chapter16a_spinor_conventions.tex`.
- Updated the anomaly chapter dossier with the issue-pass note.

Verification to run:

- `rg -n -i "preceding QCD|QCD chapter.*gamma_5|gamma_5.*QCD chapter" monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
