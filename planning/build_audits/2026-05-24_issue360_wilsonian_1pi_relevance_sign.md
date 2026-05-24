# 2026-05-24 Issue #360 Wilsonian And 1PI Relevance-Sign Bridge

GitHub issue #360 flagged that the Wilsonian chapter introduced
\(\dd u_\alpha/\dd\log\Lambda=-y_\alpha u_\alpha+\cdots\), while the
Wilson--Fisher chapter used
\(\dd\tau/\dd\log\mu=-y_t\tau+\cdots\), without explicitly identifying the
common sign convention.

Changes made:

- Added a first-use footnote in the Wilsonian linearized-flow section stating
  that both equations are differentiated with respect to increasing scale
  variables.
- Displayed the infrared-oriented variables
  \(s_{\rm W}=\log(\Lambda_0/\Lambda)\) and
  \(s_{\rm 1PI}=\log(\mu_0/\mu)\), for which the relevant-coordinate equations
  acquire positive linear terms.
- Stated that the Wilsonian cutoff vector field and the 1PI subtraction-scale
  vector field are different mathematical objects until a finite
  Wilsonian--1PI matching map is specified.
- Updated the Wilson--Fisher and Wilsonian chapter dossiers so the convention
  bridge is part of the persistent audit ledger.

Verification targets:

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf`
