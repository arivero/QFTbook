# Build Audit: Logarithmic Jordan Cell

## Scope

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Issue context: #606 stringbook-depth / 2D CFT rigor audit.
- Files touched:
  - `monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`
  - `calculation-checks/cft_voa_modular_checks.py`
  - `calculation-checks/README.md`
  - `planning/chapter_dossiers/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.md`
  - `planning/build_audits/2026-05-27_logarithmic_jordan_cell.md`

## Content

This pass strengthens the logarithmic CFT section from a short status marker
into a local derivation.  The chapter now defines a rank-two logarithmic
Virasoro pair, derives the finite state and field scaling laws, and proves
the logarithmic two-point functions from the \(L_0\) and \(L_1\) Ward
identities.  The proof keeps the scale-covariant intermediate family
visible, then shows that global conformal invariance forces
\(\langle\mathcal C\mathcal C\rangle=0\) for the rank-two global pair.

The text also records the basis change \(D\mapsto D+\lambda C\), distinguishing
the invariant logarithmic coefficient from the basis-dependent constant term,
and explains why the ordinary character cannot see the nilpotent extension
class of the \(L_0\) Jordan block.  The pseudo-trace discussion is kept at the
theorem-boundary level: the chapter says what additional objects are needed
for modular closure without pretending that the full logarithmic tensor
category theorem has been proved in the chapter.

## Verification

- `python3 calculation-checks/cft_voa_modular_checks.py`
- `python3 -m py_compile calculation-checks/cft_voa_modular_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

After rebasing onto `origin/main` at `6db08739`, the TeX build and final log
scan completed cleanly at 1879 pages.
