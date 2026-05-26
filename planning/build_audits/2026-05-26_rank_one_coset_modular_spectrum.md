# Build Audit: Rank-One Coset Modular And Spectrum Data

Date: 2026-05-26

Lane: `codex/2d-cft-liouville-bcft-nlsm`

Scope:

- Deepened the Volume V, Chapter 11 rank-one coset section by adding
  compact parafermion primary-orbit counting, fusion rules, modular
  \(S\)-matrix, and the diagonal torus partition function.
- Added the Ising fusion example and the order-\(k\) parafermion
  simple-current action as exact compact checks.
- Added a quoted status boundary for the bosonic cigar spectrum, separating
  the continuous \(j=1/2+\ii s\) sector and reflection relation from the
  discrete normalizable residue data that are not determined by the local
  metric.
- Extended the public WZW/coset calculation check with parafermion orbit
  counts, fusion tests, simple-current tests, and cigar reflection-weight
  invariance.
- Updated the Chapter 11 dossier, calculation-check inventory, and
  stringbook crosswalk.

Required verification before handoff:

- `python3 calculation-checks/wzw_sugawara_coset_checks.py` passed.
- `python3 -m py_compile calculation-checks/wzw_sugawara_coset_checks.py`
  passed.
- `tools/run_calculation_checks.sh` passed, including Wolfram checks.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed with a clean log scan; rebuilt
  `monograph/tex/main.pdf` at 1585 pages.

Status: verified in this pass.
