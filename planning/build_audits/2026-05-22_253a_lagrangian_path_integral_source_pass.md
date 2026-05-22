# 253a pp. 10--14 Lagrangian And Path-Integral Source Pass

Date: 2026-05-22

Source pages checked:

- `references/253a lectures 2022.pdf`, pp. 10--14, rendered as
  `/tmp/253a_010_014-010.png` through `/tmp/253a_010_014-014.png`
- `transcription/tex/253a/foundations.tex`, Lagrangian formalism and
  time-evolution/path-integral measure block

Manuscript target:

- `monograph/tex/volumes/volume_i/chapter04_lagrangian_formalism_and_quantum_mechanical_path_integrals.tex`

Repairs made:

- Added the classical Lagrangian/Hamiltonian setup: configuration manifold,
  tangent and cotangent data, action, Euler--Lagrange equations, regular
  Legendre transform, canonical Poisson bracket, and Hamilton equations.
- Added a rendered Legendre-transform figure matching the source logic while
  stating the regularity hypothesis explicitly.
- Restored Schrödinger and Heisenberg time evolution before the path-integral
  construction.
- Added the formal \([Dq]\) transition-amplitude notation with its regulated
  meaning stated immediately.
- Inserted the position-only finite product before inserting momentum
  resolutions.
- Made the short-time symbol expansion and its \(O(\epsilon^2)\) and
  ordering-dependent \(O(\hbar)\) content explicit.
- Added the two representative finite time-lattice orderings, with symbols
  \(h\) and \(h'\), and identified their local \(O(\hbar)\) difference.
- Added the generalized-coordinate \(O(\hbar)\) ordering qualification for
  metric Lagrangians before the determinant measure.

Rendered manuscript pages inspected:

- `/tmp/qft_253a_010_014_cert_final-055.png` through
  `/tmp/qft_253a_010_014_cert_final-061.png`

Checks:

- The classical Legendre-transform figure is readable and has no label
  collisions.
- The finite time-slicing diagram is readable.
- The long phase-space and ordering formulas fit inside the text block.
- The Gaussian momentum integration and determinant measure are present.

Verification commands:

- `tools/build_monograph.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
