# Issue #597 Soliton Collective-Quantization Chapter Pass

## Scope

- Added a compiled dedicated chapter:
  `monograph/tex/volumes/volume_ii/chapter17c_solitons_collective_quantization.tex`.
- Included it in
  `monograph/tex/volumes/volume_iv/volume_iv_current.tex` immediately after
  Ch17.
- Updated the frontmatter source map and added a chapter dossier.
- Added `calculation-checks/soliton_quantization_channel_checks.py` plus
  README, inventory, and evidence-contract entries.
- Repaired three pre-existing overfull-box defects in
  `monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
  that the final monograph log scan exposed during this pass.

## Physics Substance

- The pass starts the soliton side of #597, complementing the new instanton
  physical-amplitudes chapter.
- It derives the dimensionless kink center metric
  `G_XX=M_cl=4/3`, showing explicitly how the translation zero mode is
  converted into a collective coordinate and removed from the normal
  determinant.
- It states and derives the sine-Gordon DHN mass shift `-m/pi` as a
  determinant-plus-counterterm statement, not as a classical-moduli result.
- It records the Jackiw-Rebbi zero-mode sector and the resulting
  `N_0-1/2` half-charge coordinate.

## Verification

- `python3 -m py_compile calculation-checks/soliton_quantization_channel_checks.py`
- `python3 calculation-checks/soliton_quantization_channel_checks.py`
- `tools/run_calculation_checks.sh --python-only --only soliton_quantization_channel_checks`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter17c_solitons_collective_quantization.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter17c_solitons_collective_quantization.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter17c_solitons_collective_quantization.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter17c_solitons_collective_quantization.tex --window 120 --stride 60 --fail --limit 20`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter13_planar_n4_asymptotic_bethe_ansatz.tex --fail`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `git diff --check`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported 3422 pages.

The first full build after the chapter addition correctly failed on the
duplicate Jackiw-Rebbi label inherited from an older chapter.  The final pass
uses local `soliton-chapter` labels for the new Jackiw-Rebbi displays and
builds cleanly.
