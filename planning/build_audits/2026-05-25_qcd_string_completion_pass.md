# QCD String Completion Pass Build Audit

Date: 2026-05-25.

Scope:

- completed the issue-#492 QCD-string pass in
  `monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`;
- added the static-observable extraction of the string tension from Wilson
  loops, Polyakov-loop correlators, and transfer-matrix spectral data;
- added a transfer-matrix proposition equating the rectangular area
  coefficient with the static-potential slope under explicit spectral
  hypotheses;
- added baryonic junction operators, the \(SU(3)\) \(Y\)-string potential, a
  proof of the Fermat/Steiner \(2\pi/3\) condition and length formula, and a
  new baryonic \(Y\)-network figure;
- added closed winding flux tubes, the boundary with local glueball channels,
  large-\(N_c\) string-coupling counting, and the \(D=3\) effective-string
  testbed discussion;
- extended `calculation-checks/qcd_string_luscher_checks.py` to verify the
  displayed baryonic \(Y\)-string geometry.

Verification:

- `python3 calculation-checks/qcd_string_luscher_checks.py`
  passed with `All QCD-string effective-spectrum checks passed.`;
- `tools/audit_chapter_dossiers.sh` passed;
- `git diff --check` passed;
- from `monograph/tex`,
  `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` passed;
- final `main.log` scan found no undefined references, no duplicate labels,
  no label-change warnings, and no PDF-string warnings;
- `pdfinfo monograph/tex/main.pdf` reported 1232 pages.
