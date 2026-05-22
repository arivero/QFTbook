# 2026-05-22 1PI Effective Action Source And Figure Audit

## Scope

- Source block: second-sequence handwritten material, pages 71--80.
- Local transcription comparison:
  `transcription/tex/253b/scattering_rg_qcd.tex`, around the source
  functional, connected generator, Legendre transform, background split, 1PI
  vertices, Euclidean convexity, and finite-dimensional convexification
  discussion.
- Manuscript home:
  `monograph/tex/volumes/volume_ii/chapter23_generating_functionals_and_the_one_particle_irreducible_effective_action.tex`.

## Source Content Checked

- Regulated Lorentzian source functional \(Z[J]\), source pairing, and the
  momentum-space source vertex.
- Connected logarithm \(Z[J]=e^{iW[J]}\) and the statement that \(iW[J]\)
  sums connected diagrams.
- Functional derivatives of \(Z[J]\) and \(W[J]\), with the time-contour
  prescription fixing the operator ordering.
- Source-dependent mean field
  \(\langle\phi(x)\rangle=\delta W/\delta J(x)\).
- Legendre transform
  \(\Gamma[\varphi]=W[J_\varphi]-\int\varphi J_\varphi\), its inverse
  field-source relation, and the sign convention
  \(\delta\Gamma/\delta\varphi=-J_\varphi\).
- Background split \(\phi=\varphi+\widehat\phi\), shifted integral
  representation of \(e^{i\Gamma[\varphi]}\), and the condition
  \(\langle\widehat\phi\rangle_\varphi=0\).
- Cubic-interaction split into background and fluctuation vertices, including
  the \(J_\varphi\widehat\phi\) one-point vertex.
- Diagrammatic removal of one-particle-reducible vacuum graphs by the
  tadpole condition: cutting one quantum propagator gives two tadpole
  functionals, hence no contribution to \(\Gamma\).
- Off-shell 1PI kernels \(\Gamma^{(n)}\), the inverse-propagator convention
  for \(\Gamma^{(2)}\), and the derivative expansion with the massless
  nonanalyticity caveat.
- Exact reconstruction of connected Green functions as trees built from exact
  propagators and exact 1PI vertices.
- Euclidean Holder concavity of \(W_E[J]\) for positive bosonic measure and
  convexity of the Legendre effective action.
- Finite-dimensional nonconvex toy model, supporting-line
  Legendre--Fenchel convexification, and the perturbative branch condition
  obtained by subtracting the tangent line at \(\phi_0\).

## Manuscript Changes

- Added the Fourier convention for the source pairing and an inline
  momentum-space source-vertex diagram with factor \(i\widetilde J(k)\).
- Added the explicit cubic background-field expansion
  \(\phi^3=\varphi^3+3\varphi^2\widehat\phi
  +3\varphi\widehat\phi^2+\widehat\phi^3\), with an accompanying diagram
  distinguishing background legs, quantum legs, and the source one-point
  vertex.
- Expanded the tadpole/1PI explanation so the absence of one-particle cuts in
  \(\Gamma\) follows directly from the Legendre tadpole condition.
- Added the finite-dimensional branch/tangent perturbation condition:
  \(J_0=-S'(\phi_0)\), the shifted exponent, and the requirement that its
  quadratic part be positive for a Gaussian saddle expansion.
- Polished the branch/tangent figure labels after rendering so the tangent
  line and source-condition labels do not overlap.

## Rendered Check

Completed after the full build on 2026-05-22.

- Handwritten source pages rendered from
  `references/253b lecture notes 2023.pdf`:
  `/tmp/qft253b_1pi_src-071.png` through
  `/tmp/qft253b_1pi_src-080.png`.
- Compiled manuscript pages rendered from `monograph/tex/main.pdf`:
  `/tmp/qft_ch29_1pi_actual-186.png` through
  `/tmp/qft_ch29_1pi_actual-196.png`.
- Polished branch/tangent figure render:
  `/tmp/qft_ch29_1pi_polished-195.png`.
- Rendered figure checks covered the source/Legendre display, the source
  one-valent vertex, the cubic background split, the tadpole/1PI cancellation
  figure, connected-tree reconstruction from exact 1PI vertices, Euclidean
  concavity/convexity, and the finite-dimensional branch/tangent
  perturbation-condition figure.

## Verification

- `tools/build_monograph.sh` completed cleanly after the TeX edits.
- The strict monograph text audit inside the build completed cleanly.
- `git diff --check` completed cleanly.
- `tools/audit_monograph_text.sh` completed cleanly.

This promotes handwritten 253b pages 71--80 to certified coverage after the
1PI effective-action source and figure audit.
