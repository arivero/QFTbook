# Build Audit: Issue 602 Ising Boundary-Changing Constants

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Scope: issue #602 / Volume V BCFT.
- Substantive edits:
  - Added the Ising boundary-condition-changing OPE constants to
    `monograph/tex/volumes/volume_v/chapter14_boundary_conformal_field_theory.tex`.
  - Stated the Cardy/F-symbol normalization explicitly and separated raw
    rescalable constants from invariant sewing data.
  - Extended `calculation-checks/bcft_cardy_checks.py` to verify the
    `F^{sigma sigma sigma}_sigma` matrix, its row normalization, the
    fixed-boundary relative sign, and the OPE powers.
  - Updated the BCFT chapter dossier and removed the Ising
    boundary-changing constants item from the remaining-obligation ledger.
- Verification completed before commit:
  - `python3 calculation-checks/bcft_cardy_checks.py`
  - `tools/run_calculation_checks.sh`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `git diff --check`
  - `tools/build_monograph.sh`
