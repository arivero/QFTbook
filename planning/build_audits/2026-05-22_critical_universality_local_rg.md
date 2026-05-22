# 2026-05-22 Critical Universality Local RG Audit

## Scope

This pass propagates the finite-coordinate Wilsonian cutoff-removal estimate
into the Wilson-Fisher and Ising universality chapters.  The purpose is to
make critical tuning and universality into local RG-coordinate statements
with explicit assumptions, rather than informal statements about microscopic
models becoming identical.

## Manuscript Changes

- Updated
  `monograph/tex/volumes/volume_ii/chapter14_the_wilson_fisher_fixed_point_and_scaling_operators.tex`.
- Added "Scaling Coordinates as a Local RG Chart."
- Defined a finite projected RG chart \(g^\alpha(\mu)\), the beta vector
  field, the linearized matrix at the fixed point, and the relevant and
  irrelevant eigenvalues
  \(y_A=D-\Delta_A\) and \(\omega_\rho=\Delta_\rho-D\).
- Defined the critical surface in a finite RG chart as the endpoint condition
  \(u(\mu_R)=0\), with symmetry restrictions stated explicitly.
- Derived the linear UV-to-reference-scale tuning powers for relevant
  coordinates and the suppression powers for bounded irrelevant coordinates.
- Updated
  `monograph/tex/volumes/volume_ii/chapter15_the_statistical_ising_model_and_universality.tex`.
- Added "Finite-Cutoff Universality in a Local Chart."
- Defined the microscopic endpoint map
  \(E_X(\Lambda_0,p_X)=u_X(\mu_R;\Lambda_0,p_X)\) for relevant coordinates.
- Added a conditional local universality proposition applying the
  finite-coordinate cutoff-removal estimate to tuned microscopic Ising-class
  realizations.
- Separated fixed-point data from nonuniversal coordinate maps, including
  the thermal metric factor \(A_X\) and the tuning relation for fixed
  \(\lambda_{t,R}\).
- Added the scaling-field expansion for microscopic odd and even lattice
  observables and the normalized separated-point correlator limit.
- Added the differentiable-coordinate correction-to-scaling expansion
  \(G^X_a=G_{u_R}+O((\mu_R a)^\kappa)\), separating universal correction
  exponents from microscopic amplitudes.

## Planning Updates

- Updated the Wilson-Fisher dossier with the finite RG-chart construction and
  critical-surface claim.
- Updated the Ising dossier with the local universality proposition and the
  observable scaling-field limit.
- Updated the master architecture and dependency map so the next target is
  the BPHZ--Wilsonian--1PI worked matching and the source-dependent operator
  bridge.

## Verification

- Strict phrase scans on the edited manuscript and audit file found no
  prohibited framing.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed and produced
  `monograph/tex/main.pdf`.
- Rendered the affected Wilson-Fisher and Ising pages; the final inspected
  correction-to-scaling page was
  `/tmp/qft_critical_univ_final-329.png`, with legible equations and no
  obvious layout collision.
