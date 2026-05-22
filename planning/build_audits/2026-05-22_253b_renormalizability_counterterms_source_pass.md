# 2026-05-22 253b Renormalizability And Counterterms Source Audit

## Scope

- Source block: `references/253b lecture notes 2023.pdf`, pages 81--96.
- Local transcription comparison:
  `transcription/tex/253b/scattering_rg_qcd.tex`, around the
  renormalizability, counterterm census, \(D=6\ \phi^3\), Schwinger-parameter
  subdivergence, and BPHZ discussion.
- Additional comparison:
  `references/253b transcribed lecture notes.tex`, around the same source
  block.
- Manuscript homes:
  `monograph/tex/volumes/volume_ii/chapter08_renormalizability_and_local_counterterms.tex`
  and
  `monograph/tex/volumes/volume_ii/chapter09_subdivergences_and_bphz_subtractions.tex`.

## Source Content Checked

- Regulated Euclidean path integral, local bare action, and the two regulator
  languages: momentum cutoff and dimensional regularization.
- The finite-parameter renormalized-family criterion: bare local coordinates
  may diverge with the regulator, while finite physical/renormalized
  coordinates determine finite Green functions or 1PI local coefficients.
- Renormalized field normalization, effective couplings in the local 1PI
  action, and the relation between local 1PI finiteness and Green-function
  finiteness.
- \(D=4\) scalar examples:
  \(\phi^3\) needs the mass counterterm at one loop, \(\phi^4\) needs mass,
  wavefunction, and quartic counterterms, while \(\phi^6\) produces both a
  sextic self-counterterm and the higher local tower
  \(\phi^8,\phi^{10},\ldots\).
- Engineering dimensions
  \(d_I=\ell_I+n_I(D-2)/2\) and the source power-counting criterion for when a
  local operator coefficient can diverge.
- The \(D=6\ \phi^3\) example with \(\delta Z\), \(\delta m^2\), and
  \(\delta g\), including the one-loop self-energy Feynman-parameter integral,
  the dimensional-regularization pole polynomial in \(k^2\) and \(m_R^2\), and
  the one-loop triangle divergence.
- Higher-order locality for a renormalized self-energy insertion:
  Taylor expansion in the external momentum, local \(k^0,k^2\) pole structure,
  and the absence of an \(\varepsilon^{-1}\log k^2\) pole.
- The Schwinger-parameter two-loop diamond calculation:
  \(P(\ell)=\int_0^\infty d\alpha\,e^{-\alpha(\ell^2+m_R^2)}\), the Gaussian
  matrix \(A\), the nonnegative quadratic form \(Q\), the homogeneous scaling
  relation for \(F\), the two one-loop subdivergence limits, the explicit
  \(\widetilde F\) subtraction, and the final subtraction of the \(k^0\) and
  \(k^2\) overall Taylor terms.
- The transition from the example to the systematic BPHZ/forest-formula
  treatment in the following chapter.

## Manuscript Changes

- Expanded the \(D=4\ \phi^6\) discussion so the sextic local
  self-counterterm is not skipped before the higher \(\phi^8,\phi^{10},\ldots\)
  proliferation.
- Updated the counterterm-census figure label in the sextic panel to show the
  six-point local term as well as the higher tower.
- Added the explicit \(D=6-\varepsilon\) self-energy parameter integral, the
  local pole polynomial, and the large-\(k\) finite renormalized behavior with
  all mass dimensions displayed.
- Added the dimensional-regularization explanation for why logarithmic
  subgraph insertions give double and single local poles but no
  \(\varepsilon^{-1}\log k^2\) nonlocal pole.
- Added \(Q(\alpha)\), \(F(k^2;\alpha)\), the homogeneous Schwinger scaling
  relation, the two explicit subdivergence subtractions defining
  \(\widetilde F\), and the finite remainder \(\widetilde F_R\).
- Updated the chapter dossiers and the no-skip coverage register to mark
  pages 81--96 as certified.

## Rendered Check

- Handwritten source pages rendered from
  `references/253b lecture notes 2023.pdf`:
  `/tmp/253b_81_96-081.png` through `/tmp/253b_81_96-096.png`.
- Compiled manuscript pages rendered from `monograph/tex/main.pdf`:
  `/tmp/qft_ren_counterterms_final-225.png` through
  `/tmp/qft_ren_counterterms_final-235.png`.
- Visual checks covered the \(D=4\) counterterm-census figure, the
  \(D=6\ \phi^3\) one-loop two- and three-point figure, the self-energy
  insertion/Taylor-remainder figure, and the Schwinger subdivergence figure.
  No cropped equations, overlapping labels, or missing figure elements were
  found in the audited pages.

## Verification

- `tools/build_monograph.sh` completed cleanly after the TeX edits.
- The strict monograph text audit inside the build completed cleanly.
- `tools/audit_monograph_text.sh` completed cleanly.
- `git diff --check` completed cleanly.

This promotes handwritten 253b pages 81--96 to certified coverage after the
renormalizability, local-counterterm, and subdivergence source audit.
