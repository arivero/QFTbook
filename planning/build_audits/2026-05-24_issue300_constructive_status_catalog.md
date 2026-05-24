# Issue #300 Audit: Constructive Existence and Triviality Catalog

## GitHub Issue

- #300, opened 2026-05-22:
  `[Vol I, III] Constructive existence regimes for [Dφ] not catalogued`.

## Manuscript Changes

- Added Table `tab:constructive-qft-status-catalog` to
  `monograph/tex/volumes/volume_i/chapter08_scalar_path_integrals_and_euclidean_green_functions.tex`,
  immediately after the first regulator-status discussion of `[D\phi]`.
- The catalog names:
  - `P(\phi)_2`, including `\phi^4_2`, as constructed non-Gaussian
    Euclidean/Wightman scalar models after Wick ordering and local
    renormalization;
  - `\phi^4_3` as a constructed non-Gaussian massive scalar model after the
    required counterterms;
  - two-dimensional Yang--Mills as a rigorous gauge construction through
    heat-kernel/holonomy measures on generalized connections or lattice
    projective limits;
  - `\phi^4_D`, `D\ge5`, as Gaussian/trivial for the standard
    reflection-positive lattice/Ising/positive-quartic critical scaling
    problem covered by triviality theorems;
  - `\phi^4_4` as marginally trivial for the standard
    reflection-positive lattice/Ising/positive-quartic critical scaling
    problem, while preserving the separate open question of another
    UV-complete four-dimensional QFT matching formal `\phi^4_4` perturbation
    theory to all orders;
  - four-dimensional pure Yang--Mills as finite-cutoff rigorous on Wilson
    lattices, with continuum existence and mass gap remaining a separate
    constructive problem.
- Added a references paragraph naming Nelson, Simon, Glimm--Jaffe,
  Driver/Sengupta/Lévy, Aizenman, Fröhlich, and Aizenman--Duminil-Copin.
- Added cross-references to the catalog from:
  - `monograph/tex/volumes/volume_ii/chapter01_local_qft_spectral_data_and_path_integrals_revisited.tex`;
  - `monograph/tex/volumes/volume_ii/chapter08_renormalizability_and_local_counterterms.tex`.
- Added `array` to the TeX preamble so the status table can use ragged-right
  paragraph columns without underfull log noise.

## Planning Updates

- Updated the Volume I scalar path-integral dossier with the new catalog,
  notation entry, claim ledger entry, and audit note.
- Updated the Volume II local-data dossier and renormalizability dossier with
  cross-references to the catalog.

## Verification

- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; full TeX build and final log scan clean.
