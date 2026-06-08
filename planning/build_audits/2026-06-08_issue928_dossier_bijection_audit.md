# Issue #928 Dossier Bijection Audit

## Scope

- Target audit: `tools/audit_chapter_dossiers.sh`.
- Target dossier tree: `planning/chapter_dossiers/`.
- Missing dossier repaired:
  `planning/chapter_dossiers/volume_vii/chapter07b_susy_yang_mills_family_spectra.md`.

## Substance Audit

- Added explicit `Source-File:` metadata to every active chapter dossier.
- Added the missing Volume VII Chapter 7b dossier and tied it to the compiled
  source key
  `monograph/tex/volumes/volume_vii/chapter07b_susy_yang_mills_family_spectra.tex`.
- Strengthened the dossier audit so it parses every compiled
  `volume_*_current.tex` manifest, requires exactly one dossier source key for
  every compiled chapter input, and rejects missing, duplicate, or orphan
  keys.
- Added an in-memory deletion negative control: the audit simulates removal
  of one dossier key and requires the missing-source check to detect it.
- Updated planning docs so future dossiers treat `Source-File:` as the stable
  database key rather than the numeric filename prefix.

## Physics-Depth Reaudit

- This pass is intentionally infrastructure.  It does not claim to solve the
  Chapter 7b physics gap.
- The new Chapter 7b dossier records the existing chapter as a comparison map
  with finite Abelian and holomorphic checks, and explicitly keeps #927 as
  the frontier for constructing a non-tautological spectral bridge.
- This prevents the dossier system from masking exactly the kind of
  architecture gap identified by the review: protected holomorphic data and
  finite trigonometric identities remain separate from nonchiral spectral
  transport.

## Verification

- Passed: `bash tools/audit_chapter_dossiers.sh`.
  - Reported `manifest_count=161`, `dossier_count=161`,
    `matched_count=161`, `deletion_negative_control=passed`.
- Passed: `python3 calculation-checks/susy_yang_mills_family_checks.py`.
- Passed: `python3 calculation-checks/susy_yang_mills_deformation_ladder_checks.py`.
- Passed: `python3 tools/audit_calculation_check_inventory.py`.
- Passed: `git diff --check`.
