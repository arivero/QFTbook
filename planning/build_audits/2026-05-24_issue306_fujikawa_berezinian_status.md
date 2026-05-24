# Build Audit: Issue #306 Fujikawa Berezinian Status

Issue:

- GitHub #306: `[Vol IV Ch 10] Anomaly Fujikawa 'measure derivation':
  measure-change not connected to defined measure`.

Files changed:

- `monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `planning/chapter_dossiers/volume_ii/chapter20_chiral_axial_anomalies.md`
- `tools/audit_monograph_text.sh`

Resolution:

- Replaced the untyped statement that a formal fermion measure changes by a
  Jacobian with a finite-dimensional Berezinian change-of-variables
  construction.
- Tied the transformed object to Volume I's fermionic path-integral framework:
  the ordered Berezinian density
  \(\Omega_\Lambda=\prod_{n\in I_\Lambda}d\bar c_n\,dc_n\) on the odd
  coefficient variables of a finite spectral cutoff \(V_\Lambda\).
- Defined the finite spectral projector \(P_\Lambda\), the cutoff eigenspace
  \(V_\Lambda\), the finite chiral-rotation matrix \(U_{\Lambda,\beta}\), and
  the finite Berezinian Jacobian \(J_\Lambda\).
- Classified the heat kernel \(\exp(-\mathcal D_A^2/M^2)\) as a
  gauge-covariant spectral regulator for the Berezinian trace.  No
  Pauli--Villars regulator field is introduced.
- Added a harness check rejecting the old untyped phrase "measure changes by
  a Jacobian" in reader-facing TeX.

Verification:

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean full XeLaTeX build and log scan;
  generated `/Users/xiyin/QFT/monograph/tex/main.pdf`.
