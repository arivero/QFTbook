# Yang-Mills Hermitian Convention Audit

Date: 2026-05-22

Scope:
- `monograph/tex/volumes/volume_ii/chapter17_yang_mills_theory_and_matter_fields.tex`
- `planning/chapter_dossiers/volume_ii/chapter18_classical_yang_mills_matter.md`

Changes:
- Made explicit the distinction between the anti-Hermitian mathematical Lie
  algebra
  \[
    \mathfrak g_{\mathrm{ah}}=\operatorname{Lie}(G)
  \]
  and the Hermitian generator coordinate space
  \[
    \mathfrak g=i\,\mathfrak g_{\mathrm{ah}}.
  \]
- Introduced the anti-Hermitian connection one-form
  \[
    \mathsf A_{\mathrm{ah}}=-iA
  \]
  corresponding to the Hermitian local representative \(A\).
- Stated that the compact real bracket in Hermitian coordinates is
  \[
    [X,Y]_{\mathrm H}=-i[X,Y]_{\mathrm{mat}},
  \]
  while the displayed Yang-Mills formulas use ordinary matrix commutators with
  explicit factors of \(i\).
- Added the overlap transformation law for local connection representatives
  on nontrivial principal bundles, together with covariant curvature gluing.
- Refined the \(SU(N)\) adjoint representation discussion by using the
  complexified adjoint space \(\mathfrak g_{\mathbb C}\) and stating the
  real-field reality condition separately.
- Added the representation-theoretic criterion for gauge-invariant scalar,
  Dirac, mass, and Yukawa contractions.
- Updated the chapter dossier to preserve these convention requirements for
  later BRST, anomaly, and Chern-Weil material.

Verification:
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`
- Rendered and inspected PDF pages 299--303, then re-rendered pages 299, 302,
  and 303 after notation refinements.

Residual risks:
- The Dirac kinetic and \(\gamma_5\) sign conventions are inherited from the
  spinor, QED, and anomaly chapters. A later pass should audit those chapters
  together rather than changing the convention in only this chapter.
