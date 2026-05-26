# 2026-05-26 Liouville Elliptic-Recursion Coordinate Pass

Lane: 2D CFT / Liouville / BCFT / NLSM.

Substantive files:

- `monograph/tex/volumes/volume_v/chapter13_liouville_cft.tex`
- `calculation-checks/liouville_bpz_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_v/chapter13_liouville_cft.md`
- `planning/source_inventory/stringbook_crosswalk.md`

Content added:

- Added the elliptic nome \(q(z)\) for the four-punctured sphere and the
  modular-lambda expansion
  \(\lambda(q)=16q-128q^2+704q^3+O(q^4)\).
- Derived the first exact conversion formulas from the ordinary
  \(z\)-block coefficients \(f_1,f_2\) to raw elliptic-coordinate
  coefficients \(g_1,g_2\).
- Stated Zamolodchikov's elliptic recursion as a theorem boundary, with the
  pole locations \(h_{m,n}\) displayed and the residue-product normalization
  boundary made explicit.
- Extended `liouville_bpz_checks.py` to verify the modular-lambda expansion
  and \(z\)-to-\(q\) coefficient conversion in exact rational arithmetic.

Checks to run before closing the pass:

- `python3 calculation-checks/liouville_bpz_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
