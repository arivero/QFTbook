# 2026-05-25 Issue #574 RG Stable-Graph Pass

GitHub issue: #574, concerning `thm:rg-local-stable-manifold` in
`monograph/tex/volumes/volume_xi/chapter07_rigorous_renormalization_group.tex`.

## Manuscript Changes

- Replaced the vague stable-manifold proof paragraph with an explicit
  Lyapunov-Perron construction.
- Strengthened the theorem statement by specifying the product splitting
  \(\mathcal B=E_u\oplus E_s\), the local map
  \[
    \mathcal R(u,s)=(Au+F_u(u,s),Bs+F_s(u,s)),
  \]
  constants \(\|A^{-1}\|\le a<1\), \(\|B\|\le b<1\), and the nonlinear
  Lipschitz constant \(\kappa\).
- Introduced the weighted complete sequence space
  \(\mathcal X_{\gamma,\rho}(s_0)\) with norm
  \(\sup_n\gamma^{-n}\|(u_n,s_n)\|\).
- Displayed the Lyapunov-Perron map, including the unstable summation formula
  and the stable recurrence.
- Displayed the contraction estimates
  \(q_u=\kappa a/(1-a\gamma)\), \(q_s=(b+\kappa)/\gamma\), and
  \(q=\max(q_u,q_s)<1\).
- Proved the graph Lipschitz bound and the tangent-to-\(E_s\) statement from
  \(DF(0)=0\).

## Status

This pass proves the local functional-analytic stable-graph lemma used as RG
proof infrastructure.  It does not assert the existence of a non-Gaussian RG
fixed point; that remains the separate constructive/nonperturbative RG
problem recorded later in the chapter.

## Verification

- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean; the monograph built to
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf`: 1255 pages.
