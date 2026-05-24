# Issue #273 Audit: Casimir Block Existence And Uniqueness

## Scope

- GitHub source of truth: issue #273 was verified open before this pass.
- Manuscript target: `monograph/tex/volumes/volume_iii/chapter09_operator_product_expansion.tex`.
- Dossier target: `planning/chapter_dossiers/volume_iii/chapter09_operator_product_expansion.md`.
- Pre-existing uncommitted chapter 9 changes for the later conformal
  partial-wave issue were preserved.

## Manuscript Change

- Replaced the one-paragraph Casimir characterization of scalar conformal
  blocks with the explicit \(12\)-channel scalar Casimir operator.
- Displayed the reduced \(u,v\) differential operator
  \(\mathcal C_{12}^{(u,v)}=2\mathcal D_{a,b}\), with the external-dimension
  parameters \(a=(\Delta_2-\Delta_1)/2\), \(b=(\Delta_3-\Delta_4)/2\).
- Recorded the equivalent \(z,\bar z\) form, the chain-rule conversion to
  \(u,v\), and the normalization of the quadratic Casimir eigenvalue
  \(C_{\Delta,\ell}=\Delta(\Delta-D)+\ell(\ell+D-2)\).
- Stated the two local radial Frobenius branches at the \(12\) OPE boundary,
  with exponents \(\Delta\) and \(D-\Delta\), and specified that the OPE block
  selects the \(\Delta\) branch with zero shadow coefficient.
- Added `Theorem~\ref{thm:casimir-block-local-existence-uniqueness}` proving
  local existence and uniqueness from the descendant Gram-matrix construction,
  quotienting null descendants, the conformal Ward recursion, and radial OPE
  convergence.

## Verification

- Passed: `git diff --check`.
- Passed: `tools/audit_monograph_text.sh`.
- Passed: `tools/audit_chapter_dossiers.sh`.
- Passed: `tools/build_monograph.sh`.
