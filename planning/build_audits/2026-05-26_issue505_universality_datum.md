# 2026-05-26 Issue 505: Universality Datum

GitHub issue: #505, nonperturbative Wilsonian fixed-point theory and rigorous
RG state of the art.

This pass strengthens the treatment of "universality class" in Volume XI,
Chapter 7.  The term is now tied to a convergence datum rather than used as a
physics label.

## Manuscript Addition

Added `def:wilsonian-universality-datum`, specifying:

- an index set \(I\) of microscopic regulators;
- tuned initial points \(V_i\) in a common Banach RG chart or in specified
  identified charts;
- an RG map \(\mathcal R\), neighborhood \(\mathcal N\), and fixed point
  \(V_\ast\);
- a topological vector space \(\mathcal O\) of normalized long-distance
  observable data;
- reconstruction maps \(\operatorname{Rec}_{i,n}\);
- a normalization group \(G\) acting continuously on \(\mathcal O\).

The definition requires both
\(\mathcal R^n(V_i)\to V_\ast\) in the Banach RG chart and
\[
  g_i\,\operatorname{Rec}_{i,n}(V_i)\to O_\ast
\]
in the observable topology.  Coupling-coordinate convergence alone is
explicitly not a QFT universality theorem.

Added `prop:universality-equivalence-relation`, proving that the relation
defined by convergence of normalized reconstructed observables is an
equivalence relation once a common reconstructed limit is part of the datum.

## Rigor Boundary

The new formulation separates three statements that are often conflated:

1. a formal or numerical fixed point of an RG coordinate system;
2. a Banach-space fixed point of a specified nonperturbative RG map;
3. an equivalence class of microscopic regulators whose reconstructed
   long-distance observables converge to common normalized data.

Only the third deserves the monograph's use of "universality class."

## Verification

- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`

Issue #505 remains open: model-specific nonperturbative fixed-point
construction and reconstruction estimates are still required.
