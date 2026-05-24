# 2026-05-24 Issue #365 Diffeomorphism-Regulator Assumption

GitHub issue #365 flagged that the compactly supported diffeomorphism Ward
identity was derived from a hidden regulator hypothesis.

Changes made:

- Promoted the invariance clause to
  `ass:diffeomorphism-covariant-source-regulator`.
- Stated that \(Z_\Lambda[g,\eta]\), the subtraction functional
  \(P_\Lambda[g,\eta]\), and the limiting source chart \(\mathcal W[g,\eta]\)
  must be invariant under compactly supported diffeomorphisms.
- Made clear that this is not automatic for fixed coordinate lattices, fixed
  momentum cutoffs, or noncovariant smoothing kernels.
- Added the curved-background dimensional-regularization caveat: the tensor
  continuation and subtraction prescription must be covariant.
- Stated that chiral gravitational anomalies obstruct such a fully invariant
  source functional; the Ward identity then has an anomaly functional on the
  right-hand side.
- Updated the stress-tensor chapter dossier.

Verification targets:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
