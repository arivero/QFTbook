# Issue 419: Conformal Scalar Cylinder Mass

Date: 2026-05-24.

Issue:

- GitHub #419 flagged that the free massless scalar section computed a
  nonzero cylinder mass
  \(m_{\rm cyl}^2=\xi_\ast R_{\rm cyl}=(D-2)^2/4\) without first explaining why
  a flat massless scalar has a curvature term after the Weyl map.

Fix:

- Inserted the Weyl-covariant conformal scalar action
  \[
    S[\phi;g]
    =
    \frac12\int\sqrt g\,
    \bigl(g^{\mu\nu}\nabla_\mu\phi\nabla_\nu\phi
    +\xi_\ast R[g]\phi^2\bigr),
    \qquad
    \xi_\ast=\frac{D-2}{4(D-1)}.
  \]
- Explained that the flat representative has \(R=0\), while the cylinder
  representative has \(R_{\rm cyl}>0\), so the same Weyl-covariant term becomes
  the cylinder mass term.
- Updated the Chapter 4 dossier.

Verification:

- `git diff --check` clean.
- `tools/audit_monograph_text.sh` clean.
- `tools/audit_chapter_dossiers.sh` clean.
- `tools/build_monograph.sh` clean.
- `pdfinfo monograph/tex/main.pdf` reports 781 pages.
