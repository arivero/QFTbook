# 2026-06-06 Issue #755/#626 SW Physical Output Surface

## Scope

- Focused reader-surface and physics-architecture pass on Volume VII Chapter 07.
- Retitled the visible pure `su(2)` global/line object as an input package
  while preserving the existing labels and formulas.
- Replaced the visible argument-status surface with argument roles tied to the
  Wilsonian low-energy description.
- Added a physical-output map immediately after the central conjecture.

## Quality Intent

The Seiberg-Witten curve and ADHM/Nekrasov computations should read as tools
for physical low-energy quantities, not as autonomous mathematical
constructions of the full four-dimensional QFT.  The revised surface says
what the supplied curve-and-period package computes: Abelian Wilsonian
couplings, central charges, BPS mass bounds, singular light charges,
monodromies, and protected prepotential coefficients after scheme matching.
It also states what remains outside the period calculation: microscopic
Hilbert-space construction, complete BPS spectrum, genuine Wilson-'t Hooft
line lattice, and the full continuum regulator construction.

## Verification Passed

- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter07_four_dimensional_n2_seiberg_witten.tex --window 120 --stride 60 --fail --limit 20`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter07_four_dimensional_n2_seiberg_witten.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter07_four_dimensional_n2_seiberg_witten.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter07_four_dimensional_n2_seiberg_witten.tex --fail`
- Process-language scan against the touched TeX: no matches.
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_negative_scope_prose.py`
- `git diff --check`.
- `tools/build_monograph.sh`, clean at 3478 pages.
