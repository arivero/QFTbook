# 2026-05-24 Issue #369 Kallen-Lehmann Commutator Antisymmetry

GitHub issue #369 flagged that the canonical Kallen--Lehmann sum-rule
derivation compared the spectral derivative with the equal-time canonical
delta distribution without spelling out the commutator-antisymmetry sign.

Changes made:

- Inserted the explicit sign bridge:
  \[
    [\pi_0(\vec r),\phi_0(\vec0)]
    =
    -[\phi_0(\vec0),\pi_0(\vec r)]
    =
    -\ii\delta^{(d)}(\vec r)\mathbf1.
  \]
- Stated that the derivative of
  \([\phi(t,\vec r),\phi(0,\vec0)]\) differentiates the first field, so the
  matching spectral derivative is the \(-\ii\delta\) distribution.
- Updated the Kallen--Lehmann chapter dossier.

Verification targets:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
