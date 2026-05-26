# Build Audit: Issue 601 Virasoro Block Coefficients

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Scope: issue #601 / Volume V Chapter 13 Liouville conformal-block
  recursion depth pass.
- Substantive edits:
  - Added a Virasoro-block Gram-matrix section to
    `monograph/tex/volumes/volume_v/chapter13_liouville_cft.tex`.
  - Defined the four external weights, internal weight, central charge,
    normalized block expansion, level-two nondegeneracy assumptions, and
    the degenerate/null-vector boundary.
  - Derived the first two ordinary Virasoro four-point block coefficients
    from Ward-identity descendant matrix elements and the level-one and
    level-two Gram matrices.
  - Extended `calculation-checks/liouville_bpz_checks.py` with exact
    rational checks of the level-two Gram determinant, the displayed
    coefficients, and the large-`c` global-block limit.
  - Updated the Chapter 13 dossier.
- Verification completed before handoff:
  - `python3 calculation-checks/liouville_bpz_checks.py`
  - `tools/run_calculation_checks.sh`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `git diff --check`
  - `tools/build_monograph.sh`
