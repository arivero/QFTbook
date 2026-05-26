# 2026-05-26 Issue 494: Finite Z2 Gauge Companion

GitHub issue: #494, numerical methods with lattice Monte Carlo,
Hamiltonian truncation/TCSA, DLCQ, and reader-facing Python scripts.

This pass adds a compact-gauge finite-regulator benchmark rather than another
scalar or spin model.

## Manuscript Additions

- Expanded Volume XI, Chapter 5 with the finite periodic
  \(\mathbb Z_2\) lattice gauge model:
  - link variables \(U_e=\pm1\);
  - plaquette variables \(U_p\);
  - finite partition function
    \(Z_\Lambda(\beta)=\sum_U\exp(\beta\sum_p U_p)\);
  - gauge transformations \(U_{xy}\mapsto g_xU_{xy}g_y\);
  - Wilson loops \(W(C)=\prod_{e\in C}U_e\).
- Proved the exact finite character expansion:
  \(Z\) is a sum over closed plaquette surfaces, while
  \(\langle W(C)\rangle\) is a ratio whose numerator sums plaquette
  surfaces with boundary \(C\).
- Expanded Volume XI, Chapter 6 with the single-link Metropolis theorem for
  the same finite gauge model, including the local score change
  \(Q(U^e)-Q(U)=-2B_e(U)\), detailed balance, irreducibility on full link
  space, and the relation to gauge-invariant orbit averages.

## Code Additions

- Added `qft_scripts/z2_gauge_3d_metropolis.py`.
  It samples the finite periodic three-dimensional \(\mathbb Z_2\) gauge
  model, reports plaquette and rectangular Wilson-loop means, and has a
  small smoke-mode beta scan.
- Added `calculation-checks/z2_gauge_metropolis_checks.py`.
  It verifies:
  - local link-flip plaquette-score changes against total-score differences;
  - pairwise detailed balance;
  - gauge invariance of the plaquette action and Wilson loop;
  - equality of the \(1\times1\) Wilson-loop average and plaquette average.
- Updated `tools/run_qft_scripts_smoke.sh` and `qft_scripts/README.md`.

## Verification

- `python3 qft_scripts/z2_gauge_3d_metropolis.py --smoke`
- `python3 calculation-checks/z2_gauge_metropolis_checks.py`
- `python3 -m py_compile qft_scripts/z2_gauge_3d_metropolis.py calculation-checks/z2_gauge_metropolis_checks.py`
- `tools/run_qft_scripts_smoke.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`

Issue #494 remains open: production-grade numerical-method development still
requires richer SU(2)/SU(3) pure-gauge examples, toy scalar HMC, nonintegrable
TCSA examples, systematic continuum/truncation extrapolations, and deeper
DLCQ comparisons.
