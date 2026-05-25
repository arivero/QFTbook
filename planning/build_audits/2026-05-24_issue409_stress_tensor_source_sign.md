# Issue 409: Stress-Tensor Source-Functional Sign

Date: 2026-05-24.

Issue:

- GitHub #409 flagged a possible sign conflict between the CFT opening source
  functional and the stress-tensor chapter.

Convention audit:

- The current CFT source chart uses
  \[
    W_\ast[g,J]=-\log Z_\ast[g,J],
    \qquad
    Z_\ast[g,J]\sim
    \int\mathcal D_g\Phi\,
    \exp\{-S_\ast[\Phi;g]+\int\sqrt g\,J^A\mathcal O_A\}.
  \]
- The stress-tensor chapter uses the contravariant-metric convention
  \[
    \delta S=\frac12\int\sqrt g\,T_{\mu\nu}\delta g^{\mu\nu}
    =
    -\frac12\int\sqrt g\,T^{\mu\nu}\delta g_{\mu\nu}.
  \]
- Combining these gives
  \[
    \delta_g W_\ast=\langle\delta_g S_\ast\rangle
    =
    -\frac12\int\sqrt g\,
    \langle T^{\mu\nu}\rangle\,\delta g_{\mu\nu},
  \]
  hence
  \[
    \langle T^{\mu\nu}\rangle
    =
    -\frac2{\sqrt g}\frac{\delta W_\ast}{\delta g_{\mu\nu}}.
  \]
- The operator-source derivative also carries a minus sign, but because
  \(J^A\mathcal O_A\) has a plus sign in the exponent while
  \(W_\ast=-\log Z_\ast\).

Fix:

- Inserted this derivation directly after
  `eq:cft-source-derivative-conventions` in the CFT opening chapter.
- Updated the chapter dossier.

Verification to run:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
