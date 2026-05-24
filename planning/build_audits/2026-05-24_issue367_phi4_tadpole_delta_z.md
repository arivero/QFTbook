# 2026-05-24 Issue #367 Phi4 Tadpole Delta Z

GitHub issue #367 flagged that the one-loop RG chapter used
\(Z_R=1+O(g_R^2)\) and \(Z_{\rm MOM}(\mu)=1+O(g_R^2)\) without displaying the
one-loop \(\phi^4\) field-strength check.

Changes made:

- Inserted the explicit one-loop tadpole self-energy in the chapter's Dyson
  convention:
  \[
    \Sigma^{(1)}_{\rm tad}(k)
    =
    -{g_R\over2}
    \int^\Lambda {\dd^4\ell\over (2\pi)^4}
    {1\over \ell^2+m_R^2}.
  \]
- Stated the tadpole symmetry factor and the reason no external momentum flows
  through the loop.
- Derived
  \(\partial\Sigma^{(1)}_{\rm tad}/\partial k^2=0\), so the one-loop
  two-point subtraction is a mass subtraction and the kinetic subtraction starts
  at higher order.
- Updated the 1PI RG chapter dossier.

Verification targets:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
