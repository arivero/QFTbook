# 2026-05-26 Volume XI Lattice Reflection-Positivity Character Pass

## Scope

This pass responds to the active review note that the constructive/lattice
volume needs derivation-level depth and paired calculation checks.  It
deepens Volume XI Chapter 3 at the Wilson plaquette reflection-positivity
point by adding an explicit \(SU(2)\) positive character expansion and a
public calculation-check companion.

## Edits

- Added Proposition `prop:su2-wilson-positive-character-coefficients` to
  `monograph/tex/volumes/volume_xi/chapter03_lattice_reflection_positivity.tex`.
- Derived the \(SU(2)\) Wilson coefficients from normalized Haar
  class-function orthogonality:
  \(a_\ell=I_\ell-I_{\ell+2}=2(\ell+1)I_{\ell+1}/\beta>0\).
- Added `calculation-checks/lattice_reflection_positivity_checks.py` to
  verify \(U(1)\) Bessel positivity, the \(SU(2)\) Bessel recurrence, sample
  reconstruction of Wilson weights, and finite \(SU(2)\) tensor-product
  character multiplicities.
- Updated the calculation-check index and the Volume XI Chapter 3 dossier.

## Verification

- `python3 calculation-checks/lattice_reflection_positivity_checks.py`
  passed.
- `git diff --check` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `tools/build_monograph.sh` passed with clean final log scan.
- `pdfinfo monograph/tex/main.pdf` reports 1339 pages.
