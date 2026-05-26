# Build Audit: Issue 601 Liouville Screening Coefficient Pass

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Scope: issue #601 / Volume V Liouville CFT.
- Substantive edits:
  - Added a self-contained Coulomb-gas derivation of the degenerate
    one-screening OPE coefficient `C_-(alpha)` in
    `monograph/tex/volumes/volume_v/chapter13_liouville_cft.tex`.
  - Stated the Dotsenko-Fateev beta integral with its meromorphic
    continuation boundary, so the physical Liouville exponents are not
    treated as if the intermediate integral were absolutely convergent.
  - Extended `calculation-checks/liouville_bpz_checks.py` to verify the
    screening OPE power, beta-integral gamma arguments, and equivalent gamma
    rewrites of `C_-(alpha)`.
  - Updated the Liouville chapter dossier and removed the screening
    coefficient item from the remaining-obligation ledger.
- Verification to record at close of pass:
  - `python3 calculation-checks/liouville_bpz_checks.py`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `git diff --check origin/main..HEAD && git diff --check`
  - `tools/build_monograph.sh`
