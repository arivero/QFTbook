# Build Audit: Ising Full-CFT Modular Invariant

## Scope

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Issue context: #606 stringbook-depth / 2D CFT rigor audit.
- Files touched:
  - `monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`
  - `calculation-checks/cft_voa_modular_checks.py`
  - `calculation-checks/README.md`
  - `planning/chapter_dossiers/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.md`
  - `planning/build_audits/2026-05-27_ising_full_cft_modular_invariant.md`

## Content

This pass strengthens the finite rational full-CFT example in the
VOA/modular-sewing chapter.  The Ising section now displays the `T`-matrix
from the exact shifted exponents `h_i-c/24`, and the full-CFT section proves
that a nonnegative integral torus multiplicity matrix with one vacuum that
commutes with the Ising `S` and `T` matrices must be the identity.  The proof
separates the `T` spin-selection rule, which first forces diagonal form, from
the `S` connectivity equations, which force the remaining diagonal
multiplicities to be one.

The calculation check mirrors this finite algebra: exact rational shifted
exponents identify the `T`-allowed pairs, and exact `Q(sqrt2)` matrix
arithmetic records the nonzero `S_{1,sigma}` and `S_{1,epsilon}` coefficients
that force the remaining diagonal multiplicities to be one.

## Verification

- `python3 calculation-checks/cft_voa_modular_checks.py`
- `python3 -m py_compile calculation-checks/cft_voa_modular_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

After rebasing onto `origin/main` at `db4b3ee9`, the TeX build and final log
scan completed cleanly at 1868 pages.
