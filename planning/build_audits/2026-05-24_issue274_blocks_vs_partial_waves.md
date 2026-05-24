# Issue #274 Audit: Blocks Versus Partial Waves

## Scope

- GitHub source of truth: issue #274 was verified open after issue #273 was
  closed.
- Manuscript target: `monograph/tex/volumes/volume_iii/chapter09_operator_product_expansion.tex`.
- Dossier target: `planning/chapter_dossiers/volume_iii/chapter09_operator_product_expansion.md`.

## Manuscript Status

- Commit `846ddcd` added the subsection
  `Blocks, Shadows, and Partial Waves`.
- The subsection defines the OPE-channel conformal block by its OPE
  normalization and absence of the shadow branch.
- It defines the conformal partial wave as the shadow-projector harmonic
  associated with a principal-series representation.
- It displays the shadow-projector integral normalization
  `eq:shadow-projector-partial-wave`.
- It states the local block-plus-shadow decomposition
  `eq:partial-wave-block-shadow-block`.
- It records the principal-series Plancherel resolution
  `eq:conformal-partial-wave-plancherel`, with the density
  \(\mu(\nu,\ell)\) tied to the chosen shadow-projector normalization.

## Verification

- Passed before this audit file was added: `git diff --check`.
- Passed before this audit file was added: `tools/audit_monograph_text.sh`.
- Passed before this audit file was added: `tools/audit_chapter_dossiers.sh`.
- Passed before this audit file was added: `tools/build_monograph.sh`.
