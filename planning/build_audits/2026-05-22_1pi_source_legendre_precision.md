# 1PI Source and Legendre Precision Pass

Date: 2026-05-22

Scope:
- Tightened the source-space definition for the generating functional, treating sources as test functions paired with distributional fields and then interpreted at finite regulator.
- Separated the vacuum-bubble constant in \(\mathcal W[0]\) from the connected logarithm used for source derivatives.
- Replaced repeated source integrals with the pairing notation \(\langle J,\phi\rangle\), including the Lorentzian, inverse Legendre, and Euclidean conventions.
- Clarified that 1PI kernels are functional derivatives of \(\Gamma\) around a chosen background and that their external momenta are off-shell vertex variables before LSZ is applied.
- Reframed one-particle-reducible diagrams as the tree reconstruction of connected functions from lower exact kernels, rather than as new kernels in \(\Gamma\).
- Fixed the exact three-point tree reconstruction in the \(W\)-derivative convention, with the sign tied to \(\int\Gamma^{(2)}G=-1\).
- Refined the Legendre--Fenchel discussion so the convex-conjugate formula is the exact finite-regulator definition, including multi-source and boundary-domain cases.
- Updated the chapter dossier to record the current monograph placement of the 1PI chapter.
- Improved the tadpole and connected-from-1PI figures by separating crowded labels.

Verification:
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`
- Rendered and visually inspected PDF pages 185--193 at 150 dpi, covering the chapter opening, source/Legendre figure, tadpole/1PI figure, connected-tree reconstruction figure, Euclidean convexity material, and the transition into local counterterms.

Follow-up:
- The next renormalization pass should use these conventions to sharpen the local-counterterm chapter, especially the exact meaning of finite 1PI coordinates and regulator-dependent action parameters.
