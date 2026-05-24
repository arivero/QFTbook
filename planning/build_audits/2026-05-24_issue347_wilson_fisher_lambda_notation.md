# 2026-05-24 Issue #347 Wilson--Fisher Quartic Notation Audit

## Issue

GitHub issue #347 flagged a notation drift in the Wilson--Fisher chapter:
\(\lambda(\mu)\) was declared as the dimensionless quartic running coordinate,
but later formulae used an undeclared \(\lambda_4(\mu)\).

## Edits

- Replaced the figure label \(\gamma_2=\lambda_4/(16\pi^2)+\cdots\) by
  \(\gamma_2=\lambda/(16\pi^2)+\cdots\).
- Replaced the one-loop anomalous-dimension formula for \(\gamma_2(\mu)\) so it
  uses \(\lambda(\mu)\) and \(O(\lambda(\mu)^2)\).
- Replaced the \(O_4=\phi^4\) linearized-RG formula so
  \(\partial\beta^\epsilon/\partial\lambda\) is evaluated at
  \(\lambda=\lambda_*\), not at an undeclared \(\lambda_4=\lambda_{4*}\).
- Left \(\delta g_4\) unchanged, because it denotes the source perturbation for
  the operator \(O_4\), not the running quartic coordinate.
- Updated the chapter dossier with the notation convention.

## Verification

- Direct search for `\lambda_4` in
  `chapter14_the_wilson_fisher_fixed_point_and_scaling_operators.tex`: no
  matches.
- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 754 pages.
