# Ising Scaling Fields And Universality Pass

Date: 2026-05-22

Scope:
- `monograph/tex/volumes/volume_ii/chapter15_the_statistical_ising_model_and_universality.tex`
- `planning/chapter_dossiers/volume_ii/chapter16_statistical_ising_model_universality.md`

Changes:
- Added the boundary-convention role of `E(Lambda)` in the finite lattice
  ensemble.
- Replaced the unsigned massive scaling parameter by a signed thermal
  parameter `mathfrak m`, whose absolute value is the continuum inverse
  correlation length and whose sign records the high- or low-temperature side.
- Stated that magnetic scaling limits require a second relevant coordinate
  `L^{D-Delta_sigma} u_h`, set to zero in the displayed `Z_2`-symmetric
  scaling limit.
- Rewrote the operator dictionary as a leading scaling-field expansion:
  the lattice spin has leading field `sigma`, and the subtracted lattice
  energy density has leading field `epsilon`.
- Clarified that scalar continuum coordinates represent these fields as
  `phi -> sigma` and the identity-subtracted mass operator `[phi^2] ->
  epsilon`.
- Corrected the generalized Ising partition function by replacing the
  free-index single-site factor with `exp[-sum_x P(s_x) + beta sum_<xy> s_x
  s_y]`.
- Recast the universality discussion in terms of fixed-point basins and
  relevant coordinates, with the `Z_2`-even restriction explicit.

Verification:
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`
- Rendered and inspected Chapter 37 pages covering the scaling-limit map,
  the lattice scalar path-integral figure, and the universality-class diagram.
