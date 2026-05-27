# 2026-05-26 Liouville Dual BPZ Pass

## Scope

Issue #606 / Volume V Liouville depth follow-up.  This pass makes the
\(b\leftrightarrow b^{-1}\) dual level-two degenerate field explicit instead
of leaving it as an implicit symmetry of the \(V_{-b/2}\) derivation.

## Substantive Edits

- Added a proposition deriving the null vector
  \((L_{-1}^2+b^{-2}L_{-2})|h^\vee\rangle\) at
  \(h^\vee=-1/2-3/(4b^2)\).
- Derived the corresponding BPZ equation for \(V_{-1/(2b)}\), with the
  \(b^{-2}\) coefficient and the same separated-point Ward-identity
  hypotheses as the \(V_{-b/2}\) equation.
- Clarified that the \(b\)-shift and \(b^{-1}\)-shift equations are logically
  separate inputs in the standard Liouville bootstrap determination of the
  DOZZ constant.
- Extended `calculation-checks/liouville_bpz_checks.py` with exact Laurent
  arithmetic for the dual null-vector coefficient.
- Updated the calculation-check inventory, Chapter 13 dossier, stringbook
  crosswalk, and this build audit note.

## Verification

Final verification for this pass:

- `python3 calculation-checks/liouville_bpz_checks.py`
- `python3 -m py_compile calculation-checks/liouville_bpz_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The post-rebase TeX build completed cleanly at 1843 pages.
