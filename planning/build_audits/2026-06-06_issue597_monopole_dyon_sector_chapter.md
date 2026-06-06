# Issue #597 Monopole/Dyon Quantum-Sector Chapter Pass

## Scope

- Added a compiled dedicated chapter:
  `monograph/tex/volumes/volume_ii/chapter17d_monopoles_dyons_quantum_sectors.tex`.
- Included it in
  `monograph/tex/volumes/volume_iv/volume_iv_current.tex` immediately after
  the soliton collective-quantization chapter.
- Updated the frontmatter source map and added a chapter dossier.
- Added `calculation-checks/monopole_dyon_sector_checks.py` plus README,
  inventory, and evidence-contract entries.

## Physics Substance

- The pass starts the monopole/dyon side of #597 at the quantum-sector level.
- It treats monopoles as long-range charged sectors, not merely smooth cores
  or points in a moduli space.
- It proves the theta-independent DSZ pairing from Witten-shifted physical
  charges.
- It derives the field angular momentum and monopole-harmonic partial-wave
  lower bound for a two-dyon sector.
- It records the same-ray BPS no-force benchmark as vector/scalar tail
  cancellation.

## Verification

- `python3 -m py_compile calculation-checks/monopole_dyon_sector_checks.py`
- `python3 calculation-checks/monopole_dyon_sector_checks.py`
- `tools/run_calculation_checks.sh --python-only --only monopole_dyon_sector_checks`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter17d_monopoles_dyons_quantum_sectors.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter17d_monopoles_dyons_quantum_sectors.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter17d_monopoles_dyons_quantum_sectors.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter17d_monopoles_dyons_quantum_sectors.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported 3426 pages.

The strict monograph-text harness rejected an initial "schematic form"
phrase in the BPS-tail paragraph.  The final chapter states the Abelian
BPS-tail normalization directly and builds cleanly.
