# 2026-05-26 Zhu Algebra Top-Level Pass

Lane: 2D CFT / Liouville / BCFT / NLSM.

Substantive files:

- `monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`
- `calculation-checks/cft_voa_modular_checks.py`
- `planning/chapter_dossiers/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.md`
- `planning/source_inventory/stringbook_crosswalk.md`

Content added:

- Inserted a Zhu algebra and top-level module section in Volume V, Chapter 12.
- Defined the Zhu products \(a*b\) and \(a\circ b\), the quotient \(A(V)\),
  the subspace \(\Omega(M)\), and the zero-mode action on the lowest
  conformal-weight space.
- Recorded the component Jacobi identity used in the finite mode calculation
  proving that \(O(V)\) acts trivially on top levels and that
  \(o_M(a*b)=o_M(a)o_M(b)\).
- Replaced vague Zhu-classification assumptions with explicit CFT-type,
  ordinary-module, rationality, and \(C_2\)-cofiniteness hypotheses.
- Added the Ising Zhu algebra
  \(\mathbb C[x]/(x(x-1/16)(x-1/2))\) as a top-weight test.

Checks to run before closing the pass:

- `python3 calculation-checks/cft_voa_modular_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`
