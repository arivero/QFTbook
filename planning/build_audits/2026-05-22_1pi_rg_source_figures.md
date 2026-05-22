# 2026-05-22 1PI Renormalization Group Source And Figure Audit

## Scope

- Source block: second-sequence handwritten material, pages 97--110.
- Local transcription comparison:
  `transcription/tex/253b/scattering_rg_qcd.tex`, around the
  renormalization-group introduction, scalar quartic running coupling,
  nearby-scale comparison, Landau scale, general 1PI coordinate construction,
  logarithmic consistency, scheme change, and handoff to renormalized
  operators.
- Manuscript home:
  `monograph/tex/volumes/volume_ii/chapter10_renormalization_group_and_running_couplings.tex`.

## Source Content Checked

- The distinction between the 1PI renormalization group and the finite-cutoff
  Wilsonian construction, with the latter deferred to its own chapter.
- The source-level diagrammatic idea that lower-order loop subgraphs are
  reused inside larger graphs, producing the scale-differential organization
  of perturbation theory.
- Four-dimensional Euclidean \(\phi^4\) bare and renormalized Lagrangians,
  including \(Z_R\), \(\delta m^2\), and \(\delta g\).
- Amputated 1PI four-point vertex \(-\Gamma^{(4)}(k_1,k_2,k_3)\), the
  arbitrary zero-momentum coordinate, and the scale-dependent symmetric
  Euclidean subtraction point.
- Two-point self-energy convention, field normalization
  \(Z(\mu)=(1-\partial\Sigma_R/\partial k^2)^{-1}_{k^2=\mu^2}\), and
  normalized field \([\phi]_\mu=Z(\mu)^{-1/2}\phi_R\).
- One-loop \(\phi^4\) four-point diagrams: tree vertex, the three bubble
  channels, and local counterterm; the one-loop two-point tadpole does not
  affect \(Z(\mu)\).
- Finite one-loop relation between \(g(\mu)\) and \(g_R=g(0)\), finite
  relation between nearby \(g(\mu')\) and \(g(\mu)\), threshold factor, and
  high-energy beta function \(3g^2/(16\pi^2)+O(g^3)\).
- Integrated one-loop running, perturbative domain controlled by the running
  coordinate, Landau scale \(\mu_0\), and the status of this scale as a
  perturbative-coordinate statement.
- General 1PI coordinates from Taylor coefficients of 1PI vertices around
  \(k_i=O(\mu)\), including the kinetic coordinate \(g_{2,2}=1-Z(\mu)\) and
  the mass coordinate \(\lambda_2(\mu)\).
- Dimensionless coordinates \(\lambda_I(\mu)=\mu^{d_I-D}g_I(\mu)\), the
  autonomous beta-function form once all dimensionless ratios are included,
  and the logarithmic-organization role of the 1PI RG.
- Callan--Symanzik equation derived from a bare-to-renormalized chart and
  fixed-bare-data differentiation, with noncoincident correlators separated
  from contact terms.
- Canonical homogeneity separated from auxiliary-scale dependence.
- Logarithmic consistency of the cutoff expansion, including
  \(c_1=-b_1^2\), the nested/permuted four-point diagrams, and the note that
  the two-loop self-energy contributes only a single logarithm in this
  example.
- Finite scheme redefinitions and beta-function transformation by the chain
  rule, with the first two coefficients invariant for one classically
  marginal coordinate.

## Manuscript Changes

- Added a source-level subdiagram-reuse figure before the general 1PI
  coordinate figure.
- Corrected the one-loop scalar-quartic text from "two-point bubble" to the
  one-loop two-point tadpole, which is momentum independent and does not
  affect \(Z(\mu)\) at this order.
- Replaced the compressed scalar-quartic diagram by separate tree,
  \(s\)-channel, \(t\)-channel, \(u\)-channel, and counterterm panels.
- Added the source-specific quadratic derivative coordinate
  \(g_{2,2}(\mu)=1-Z(\mu)\) and mass coordinate
  \(\lambda_2(\mu)=\mu^{-2}Z(\mu)
  [g_2^{\rm bare}-\Sigma(k)|_{k^2=\mu^2}]\).
- Expanded the logarithmic-consistency figure to show the nested four-point
  double logarithm and its permuted-channel companion.

## Rendered Check

Completed after the full build on 2026-05-22.

- Handwritten source pages rendered from
  `references/253b lecture notes 2023.pdf`:
  `monograph/tex/build/source_visual_1pi_rg/253b_rg-097.png` through
  `monograph/tex/build/source_visual_1pi_rg/253b_rg-110.png`.
- Compiled manuscript pages rendered from `monograph/tex/main.pdf`:
  `/tmp/qft_ch32_rg_audit-215.png` through
  `/tmp/qft_ch32_rg_audit-226.png`.
- Rendered figure checks covered `fig:volume-ii-rg-subgraph-reuse`,
  `fig:volume-ii-one-pi-rg-coordinate`,
  `fig:volume-ii-phi-four-one-loop-rg`,
  `fig:volume-ii-phi-four-landau-scale`,
  `fig:volume-ii-double-log-consistency`, and
  `fig:volume-ii-scheme-change`.
- The added and repaired figures render without label overlap.  The
  derivative-coordinate and mass-coordinate formulas render across pages
  204--205 without crowding.

## Verification

- `tools/build_monograph.sh` completed cleanly after the TeX edits.
- The strict monograph text audit inside the build completed cleanly.
- `git diff --check` completed cleanly.
- `tools/audit_monograph_text.sh` completed cleanly.

This promotes handwritten 253b pages 97--110 to certified coverage after the
1PI renormalization-group source and figure audit.
