# 2026-05-31 Mori-Zwanzig/Kubo Bridge Pass

## Scope

- Implemented the Volume X component of the statmech crosswalk in GitHub
  issue #703.
- Target chapter:
  `monograph/tex/volumes/volume_x/chapter04_spectral_functions_kubo_transport.tex`.

## Substance

- Added a finite-regulator Kubo--Mori projection section after the
  order-of-limits discussion and before the conductivity/viscosity Kubo
  formulae.
- Defined the finite operator space, Liouville generator, Kubo--Mori inner
  product, susceptibility matrix, slow projection, frequency matrix, and
  memory kernel.
- Proved the finite-regulator projection identity by block decomposition and
  Duhamel's formula.
- Stated precisely what the identity does not supply: decay of the projected
  kernel, a thermodynamic limit, a controlled \(k\to0\) limit, or a
  Markovian hydrodynamic closure.
- Connected conserved-density Ward identities to the \(k^2\) memory kernel
  form and recorded the additional hypotheses needed to identify the local
  diffusion matrix.

## Calculation Check

- Expanded `calculation-checks/thermal_kubo_checks.py` with a
  two-dimensional rotation model:
  \[
    \dot x(t)=-\omega y_0-\omega^2\int_0^t x(s)\,ds.
  \]
- Checked the corresponding Laplace-space Schur complement
  \[
    \frac{1}{z+\omega^2/z}=\frac{z}{z^2+\omega^2}.
  \]

## Status Boundary

This pass proves only the finite-regulator projection identity.  The
existence of a nonperturbative hydrodynamic limit remains a separate
theorem-status problem requiring decay, clustering, scaling, and
limit-exchange control.
