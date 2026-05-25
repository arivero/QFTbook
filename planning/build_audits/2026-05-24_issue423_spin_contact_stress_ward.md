# Issue 423: Spin Contact Terms in the Stress Ward Identity

Date: 2026-05-24.

Issue:

- GitHub #423 flagged that the Volume V stress-tensor Ward identity used to
  hide spin-dependent contact terms behind an ellipsis, while the spinful
  current Ward identity is derived explicitly later from source variations.

Fix:

- Expanded the stress-tensor Ward identity discussion in Volume V, Chapter 3
  to state explicitly that the scalar formula is the
  \(\mathsf R^{\mu\nu}=0\) special case.
- Identified the derivative contact term in the local stress-tensor Ward
  identity as the term that becomes the local spin rotation contact term after
  smearing with a conformal Killing vector.
- Added the explicit primary contact operator
  \(-\epsilon^\rho\partial_\rho-\Delta\sigma_\epsilon
  -\frac i2\omega_\epsilon^{\mu\nu}S_{\mu\nu}\) and linked it to
  `eq:primary-spin-current-ward` in Chapter 6.
- Updated the Chapter 3 and Chapter 6 dossiers.

Verification:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf` reports 784 pages.
