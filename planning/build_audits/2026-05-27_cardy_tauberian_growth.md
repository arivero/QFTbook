# Build Audit: Cardy Tauberian Growth

## Scope

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Issue context: #606 stringbook-depth / 2D CFT rigor audit.
- Files touched:
  - `monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`
  - `calculation-checks/cft_voa_modular_checks.py`
  - `calculation-checks/README.md`
  - `planning/chapter_dossiers/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.md`
  - `planning/build_audits/2026-05-27_cardy_tauberian_growth.md`

## Content

This pass strengthens the Cardy formula discussion as a CFT-internal theorem
rather than a slogan.  The chapter now separates the modular
high-temperature partition-function asymptotic from the analytic
Tauberian theorem needed to turn it into a cumulative density-of-states
statement.  The resulting proposition states the compactness, discrete
spectrum, finite multiplicity, positivity, unique-vacuum, and no-continuous
spectrum hypotheses before deriving
`log N(E) = 2 pi sqrt(c_tot E / 6) + o(sqrt(E))`.

The calculation check records the Legendre/saddle arithmetic behind the
coefficient: after suppressing the common `pi^2` factor, the modular
coefficient `A=c_tot/6` is recovered from the stationary value of
`2 sqrt(A E) - beta E` at `E=A/beta^2`.

## Verification

- `python3 calculation-checks/cft_voa_modular_checks.py`
- `python3 -m py_compile calculation-checks/cft_voa_modular_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

After rebasing onto `origin/main` at `db4b3ee9`, the TeX build and final log
scan completed cleanly at 1869 pages.
