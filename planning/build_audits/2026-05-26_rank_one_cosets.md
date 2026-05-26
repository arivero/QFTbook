# Build Audit: Rank-One Coset CFTs

Date: 2026-05-26

Lane: `codex/2d-cft-liouville-bcft-nlsm`

Scope:

- Expanded Volume V, Chapter 11 with a self-contained current-algebra-first
  treatment of \(SU(2)_k/U(1)\) parafermions, including branching labels,
  the selection rule, field identification, central charge, conformal
  weights, Ising/Potts checks, and the parafermion current weight.
- Added the bosonic \(SL(2,\mathbb R)_k/U(1)\) cigar coset with explicit
  noncompact CFT data requirements, central charge, weights, and
  momentum/winding spin convention.
- Derived the bell and cigar large-level metrics and dilatons from local
  gauged-WZW actions by gauge fixing, algebraically integrating the gauge
  fields, and tracking the Gaussian determinant.
- Updated the public WZW/coset calculation check, Chapter 11 dossier,
  calculation-check inventory, and stringbook crosswalk.

Required verification before handoff:

- `python3 calculation-checks/wzw_sugawara_coset_checks.py` passed.
- `python3 -m py_compile calculation-checks/wzw_sugawara_coset_checks.py`
  passed.
- `tools/run_calculation_checks.sh` passed, including Wolfram checks.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed with a clean log scan; rebuilt
  `monograph/tex/main.pdf` at 1583 pages.

Status: verified in this pass.
