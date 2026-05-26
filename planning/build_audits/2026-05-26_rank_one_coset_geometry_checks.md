# Build Audit: Rank-One Coset Geometry Checks

Date: 2026-05-26

Lane: `codex/2d-cft-liouville-bcft-nlsm`

Scope:

- Added a self-contained rotational-curvature calculation for the bell and
  cigar sigma-model representatives in Volume V, Chapter 11.
- Verified locally that the displayed bell and cigar metrics and dilatons
  solve the one-loop metric Weyl-anomaly equation
  \(R_{ij}+2\nabla_i\nabla_j\Phi=0\) on their coordinate patches.
- Computed the constant scalar dilaton-anomaly terms
  \(|\nabla\Phi|^2-\nabla^2\Phi/2=\pm K^{-1}\), showing how the large-level
  central-charge shifts \(2\pm6/k\) arise before the exact affine shifts
  \(k\mapsto k\mp2\).
- Extended the public WZW/coset calculation check with exact rational tests
  of the bell/cigar metric residuals, scalar anomaly constants, and
  leading-versus-exact central-charge differences.
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
  `monograph/tex/main.pdf` at 1586 pages.

Status: verified in this pass.
