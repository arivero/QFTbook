# Issue #268 State-Operator Theorem Audit

## Scope

- Oldest active GitHub issue addressed: `#268`, on the state-operator
  correspondence in the radial-quantization chapter.
- Manuscript file:
  - `monograph/tex/volumes/volume_iii/chapter04_radial_quantization_and_state_operator_correspondence.tex`
- Dossier:
  - `planning/chapter_dossiers/volume_iii/chapter04_radial_quantization_state_operator.md`

## Content Added

- Strengthened the labeled radial reconstruction hypothesis by adding radial
  local completeness: after quotienting by the null radial two-point pairing,
  origin insertions of local operators and descendants span
  \[
    \mathcal H_{\rm fin}
    =
    \bigoplus_{\lambda<\infty}\ker(D_{\rm rad}-\lambda).
  \]
- Removed the conditional surjectivity sentence from Theorem
  `thm:state-operator-correspondence`.
- The theorem now states directly that
  \[
    \mathcal V_{\rm loc}\xrightarrow{\sim}\mathcal H_{\rm fin}
  \]
  is an isometric linear isomorphism, and that completion gives the radial
  Hilbert-space isomorphism onto \(\mathcal H_{S^{D-1}}\).
- The proof now derives the extension to the full Hilbert space from strong
  convergence of the spectral projections \(P_{[0,E]}(D_{\rm rad})\) to the
  identity.

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

All checks completed cleanly on 2026-05-24.
