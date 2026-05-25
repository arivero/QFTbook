# 2026-05-22 Finite-Coordinate Cutoff Removal Audit

## Scope

This pass strengthens the Wilsonian effective-action chapter by adding a
general finite-coordinate estimate behind cutoff removal and universality.
The new material generalizes the existing quartic-sextic example without
claiming control of the full infinite-dimensional Wilsonian space.

## Manuscript Changes

- Updated
  `monograph/tex/volumes/volume_ii/chapter16_wilsonian_effective_field_theory.tex`.
- Added the section "A Local Estimate for Cutoff Removal."
- Introduced a projected coordinate split \(z=(u,v)\), with \(u\) fixed by
  renormalization conditions at \(\Lambda_R\) and \(v\) irrelevant in the
  chosen projection.
- Stated the local projected flow
  \[
    \dd u/\dd t=B(u,v),\qquad \dd v/\dd t=Av+F(u,v),
    \qquad t=\log\Lambda .
  \]
- Stated the backward semigroup estimate
  \[
    \|e^{A\tau}\|\le K_A e^{\omega\tau},\qquad \tau\le0 ,
  \]
  for irrelevant coordinates.
- Derived the variation-of-constants formula that separates direct irrelevant
  boundary memory from the generated integral along the tuned trajectory.
- Added a proposition proving the power suppression
  \[
    \|e^{A(t_R-t_0)}v(t_0)\|
    =O((\Lambda_R/\Lambda_0)^\omega).
  \]
- Defined the finite-coordinate continuum graph \(v=V_R(u_R)\) through the
  cutoff limit of the generated integral after imposing \(u(t_R)=u_R\).
- Defined the generated-integral remainder \(R_F(t_0;u_R)\) and kept its
  convergence rate distinct from the direct irrelevant-boundary suppression
  rate.
- Added a proposition giving
  \[
    v(t_R)
    =
    V_R(u_R)
    +
    O((\Lambda_R/\Lambda_0)^{\min(\omega,\omega_F)})
  \]
  under explicitly stated uniform-control hypotheses.
- Added a figure showing the separation between irrelevant boundary memory,
  the generated integral, and the continuum graph.

## Planning Updates

- Updated the Wilsonian chapter dossier with the new construction task,
  claim ledger entry, figure requirement, and audit note.
- Updated the master architecture and dependency map so the next Volume III
  target is to propagate the cutoff-removal estimate into critical scaling
  and universality.

## Verification

- Strict phrase scans on the edited manuscript and planning files found no
  prohibited framing.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed and produced
  `monograph/tex/main.pdf`.
- Rendered the figure page as
  `/tmp/qft_cutoff_removal_estimate_final3-306.png` and inspected it
  visually; node text and arrows are legible, and the figure no longer has
  label collisions or unintended hyphenation.
