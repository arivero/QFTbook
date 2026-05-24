# 2026-05-24 OPE Product and BPZ Topology Clarification

## Issue

The OPE text must not identify the product of two separated local operators
with a new local operator.  A separated pair creates a state on a separating
sphere.  The OPE is convergence of finite local-operator partial sums to that
state in the BPZ/radial Hilbert norm.

## Edits

- Replaced the opening literal equality by a state-valued definition
  \(\Psi_{ij}(x)\) and a BPZ/radial convergence statement using
  \(P_{\le E}\).
- Marked the coordinate expansion by \(\sim_{\rm BPZ}\), with an explicit
  warning that it is not equality in a pointwise local-operator algebra.
- Replaced "multiplication table" and "binary local product" language in the
  reconstruction discussion by radial-expansion coefficient and
  binary-limit language.
- Updated the OPE chapter dossier to record this as a standing check.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 747 pages.
