# 2026-05-24 Issue #285 Verma Module Pass

## Scope

- GitHub issue: #285, "[Vol V Chs 4, 6] Verma module structure of primary
  multiplets never named".
- Manuscript targets:
  `monograph/tex/volumes/volume_iii/chapter04_radial_quantization_and_state_operator_correspondence.tex`,
  `monograph/tex/volumes/volume_iii/chapter06_primary_operators_and_finite_transformations.tex`,
  and
  `monograph/tex/volumes/volume_iii/chapter07_unitarity_bounds_and_short_multiplets.tex`.
- Dossier targets:
  `planning/chapter_dossiers/volume_iii/chapter04_radial_quantization_state_operator.md`,
  `planning/chapter_dossiers/volume_iii/chapter06_primary_operators_finite_transformations.md`,
  and
  `planning/chapter_dossiers/volume_iii/chapter07_unitarity_bounds_short_multiplets.md`.

## Content Added

- Added the conformal generalized Verma module definition
  \[
    M(\Delta,\rho)
    =
    U(\mathfrak g_{\mathbb C})
    \otimes_{U(\mathfrak l\oplus\mathfrak n_-)}
    V_{\Delta,\rho}
  \]
  with \(\mathfrak n_+=\operatorname{span}\{P_\mu\}\),
  \(\mathfrak n_-=\operatorname{span}\{K_\mu\}\), and
  \(\mathfrak l=\mathfrak{so}(D,\mathbb C)\oplus
  \mathbb C D_{\rm rad}\).
- Stated the PBW level decomposition
  \(M(\Delta,\rho)_n\simeq\operatorname{Sym}^n(\mathbb C^D)\otimes V_\rho\).
- Explained singular vectors, null submodules, and the irreducible quotient
  associated with the physical primary multiplet.
- Connected the radial descendant Gram form to the Shapovalov form and named
  the finite conformal-algebra Kac determinant and BGG organization of nested
  singular submodules.
- Added a Chapter 4 cross-reference so the primary-descendant figure is read
  as a Verma-module picture before the null quotient.
- Updated chapter dossiers to preserve the representation-theoretic
  framework and the requirement that bounds remain derived from explicit Gram
  matrices.

## Harness

- Passed: `git diff --check`
- Passed: `tools/audit_monograph_text.sh`
- Passed: `tools/audit_chapter_dossiers.sh`
- Passed: `tools/build_monograph.sh`
