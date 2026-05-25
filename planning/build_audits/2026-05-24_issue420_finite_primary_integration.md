# Issue 420: Integrating Infinitesimal Primary Transformations

Date: 2026-05-24.

Issue:

- GitHub #420 flagged that the primary-operator chapter stated the finite
  primary transformation law as the integrated form of the infinitesimal
  contact action without displaying the integration step.

Fix:

- Added a one-parameter conformal flow \(f_s\) with
  \(M_s=\partial f_s/\partial x=\Omega_sR_s\).
- Derived
  \[
    \dot\Omega_0=\sigma_\epsilon,\qquad
    \dot R_{0,\mu}{}^\nu=\omega_{\epsilon,\mu}{}^\nu
  \]
  from the conformal Killing equation.
- Differentiated the finite law at a fixed final coordinate
  \(y=f_s(x)\), using \(x=f_s^{-1}(y)\), to recover the full infinitesimal
  primary contact operator, including the derivative, scale, and spin terms.
- Added explicit checks for translations, dilatations, rotations, and finite
  special conformal transformations \(f_c=I\circ T_c\circ I\).
- Updated the Chapter 6 dossier.

Verification:

- `git diff --check` clean.
- `tools/audit_monograph_text.sh` clean.
- `tools/audit_chapter_dossiers.sh` clean.
- `tools/build_monograph.sh` clean.
- `pdfinfo monograph/tex/main.pdf` reports 782 pages.
