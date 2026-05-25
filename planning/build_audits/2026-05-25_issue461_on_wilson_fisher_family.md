# Build Audit: Issue #461 O(N) Wilson-Fisher Family

## Issue

- GitHub issue: #461, oldest open issue after #460 was closed.
- Requested substance: add the \(O(N)\) Wilson-Fisher fixed-point family,
  including the leading \(N\)-dependent anomalous dimensions, the large-\(N\)
  analytic limit as a sequence of fixed points, and the relation to the
  spherical model / nonlinear sigma model in \(2+\epsilon\).

## Manuscript Edits

- Added `The O(N) Wilson--Fisher Family` to
  `monograph/tex/volumes/volume_ii/chapter14_the_wilson_fisher_fixed_point_and_scaling_operators.tex`.
- Defined the \(O(N)\)-vector action, the quartic vertex tensor in the same
  \(g_0(\phi^2)^2/4!\) normalization, and the singlet source
  \(S=\phi^i\phi^i/2\).
- Added the two-loop \(O(N)\) MS pole map and source/field pole factors, then
  derived
  \[
    \beta_x^\epsilon=-\epsilon x+\frac{N+8}{3}x^2
    -\frac{3N+14}{3}x^3+O(x^4),
  \]
  \[
    \gamma_S=\frac{N+2}{3}x-\frac{5(N+2)}{18}x^2+O(x^3),
    \qquad
    \gamma_\phi=\frac{N+2}{36}x^2+O(x^3).
  \]
- Solved for the fixed point
  \(x_*=3\epsilon/(N+8)+9(3N+14)\epsilon^2/(N+8)^3+O(\epsilon^3)\)
  and derived \(\eta\), \(\Delta_\phi\), \(\Delta_S\), \(y_t\), \(\nu\), and
  \(\omega\), with the \(N=1\) reduction made explicit.
- Added a large-\(N\) subsection deriving \(u=Nx\),
  \(\beta_u^\epsilon=-\epsilon u+u^2/3+O(1/N)\), the finite-cutoff
  Hubbard--Stratonovich saddle, the gap equations, the nonanalytic
  \(\Omega_D(m)-\Omega_D(0)\) term for \(2<D<4\), and the exact
  \(N=\infty\) results \(\eta=0\), \(\Delta_\sigma=2\), and
  \(\nu=1/(D-2)\).
- Added the nonlinear sigma-model chart in \(D=2+\widetilde\epsilon\), including
  the constrained action, large-\(N\) saddle matching, and the perturbative
  beta function
  \(\beta_{\mathfrak g}=\widetilde\epsilon\mathfrak g
  -(N-2)\mathfrak g^2/(2\pi)+O(\mathfrak g^3)\), with the \(N=2\) BKT
  exception stated.

## Calculation Check

- Added `calculation-checks/on_wilson_fisher_epsilon_checks.py`, using exact
  rational arithmetic to verify the \(O(N)\) fixed point and exponent algebra
  for representative integer \(N\), the \(N=1\) reduction, and the leading
  large-\(N\) behavior of \(u=Nx\).
- Updated `calculation-checks/README.md`.

## Dossier Edits

- Updated
  `planning/chapter_dossiers/volume_ii/chapter15_wilson_fisher_fixed_point_scaling_operators.md`
  with the \(O(N)\) construction task, source controls, claim ledger entries,
  and audit note.

## Verification

- `git diff --check`: clean.
- `python3 calculation-checks/on_wilson_fisher_epsilon_checks.py`: passed with
  exact rational arithmetic.
- `python3 calculation-checks/wilson_fisher_epsilon_checks.py`: passed, checking
  that the older \(N=1\) companion remains consistent.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean; wrote
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf`: 839 pages.
- Rendered and inspected PDF pages 489--493 for the new \(O(N)\) section,
  including the finite-\(N\) pole data, exponent proposition/proof, large-\(N\)
  saddle equations, and nonlinear sigma-model chart.
