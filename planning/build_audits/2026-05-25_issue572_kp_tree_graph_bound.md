# 2026-05-25 Issue #572 KP Tree-Graph Bound Pass

GitHub issue: #572, concerning the proof of
`thm:constructive-kp-cluster-convergence` in
`monograph/tex/volumes/volume_xi/chapter02_constructive_scalar_models_os_data.tex`.

## Manuscript Changes

- Replaced the schematic one-paragraph Kotecky--Preiss proof with an explicit
  hard-core finite-range polymer theorem.
- Defined the incompatibility relation \(X\nsim Y\), the numerical majorant
  \(\kappa(X)\), and the finite-range cell-neighbourhood constant
  \(B_{R_0}\).
- Added Lemma `lem:constructive-penrose-tree-graph-bound`, including the
  hard-core Ursell coefficient and the Penrose tree-graph inequality
  \[
    |\varphi_{\mathrm c}(X_1,\ldots,X_n)|
    \leq
    \sum_{T\in\mathcal T_n}
    \prod_{\{i,j\}\in E(T)}u_{ij}.
  \]
- Rewrote Theorem `thm:constructive-kp-cluster-convergence` with the explicit
  smallness condition \(B_{R_0}\epsilon\le a'\), the connected-cluster
  expansion for \(\log Z_\Lambda\), and the rooted-tree bound.
- Displayed the rooted-tree recursion
  \[
    F_{N+1}(X)
    \leq
    \exp\!\left(\sum_{Y\nsim X}\kappa(Y)F_N(Y)\right),
  \]
  and the induction that closes it using the \(a\)-weighted polymer norm.
- Replaced the previous clustering sentence by the path-size estimate and
  the unused \(a-a'\) weight that yields exponential decay between separated
  supports.

## Status

This pass proves the abstract tree-graph and rooted-tree convergence step
used locally in the chapter.  It does not claim to reproduce the
model-specific Glimm--Jaffe--Spencer construction of the polymer activities;
that construction is still represented by the surrounding constructive scalar
discussion and by the remaining broader \(\phi^4_2\) cluster-expansion issue.

## Verification

- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean; the monograph built to
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf`: 1253 pages.
