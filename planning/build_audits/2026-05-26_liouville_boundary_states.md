# Build Audit: Liouville Boundary States

Date: 2026-05-26

Lane: `codex/2d-cft-liouville-bcft-nlsm`

Scope:

- Expanded Volume V, Chapter 13 with boundary Liouville action, boundary
  Euler equation, FZZT one-point and boundary-state wavefunctions, and ZZ
  states as finite differences of imaginary FZZT parameters.
- Expanded Volume V, Chapter 14 with the nonrational BCFT interpretation:
  continuous direct-integral spectrum, distributional boundary
  wavefunctions, and hyperbolic annulus kernels replacing finite rational
  Cardy sums.
- Added exact public calculation checks for the FZZT-to-ZZ hyperbolic
  identity and the degenerate Liouville shift-sum identity.
- Updated Volume V chapter dossiers, the stringbook crosswalk, and local
  reference intake notes for the downloaded FZZT/ZZ TeX sources.

Required verification before handoff:

- `python3 calculation-checks/bcft_cardy_checks.py` passed.
- `python3 -m py_compile calculation-checks/bcft_cardy_checks.py` passed.
- `python3 calculation-checks/liouville_bpz_checks.py` passed.
- `tools/run_calculation_checks.sh` passed, including Wolfram checks.
- `tools/audit_monograph_text.sh` passed after tightening one weakener in
  the new BCFT bridge text.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed with a clean log scan; rebuilt
  `monograph/tex/main.pdf` at 1580 pages.

Status: verified in this pass.
