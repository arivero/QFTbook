# Issue #728/#597 DHN-to-breather mass consistency pass

Date: 2026-06-05.

Scope:

- Chapter: Volume VI, Chapter 8, sine-Gordon / massive Thirring / affine Toda.
- New monograph label:
  `prop:sine-gordon-dhn-breather-mass-consistency`.
- Companion check:
  `check_dhn_breather_mass_weak_coupling_consistency()` in
  `calculation-checks/sine_gordon_smatrix_checks.py`.

Substance audit:

- This pass is not a new moduli-space or S-matrix identity cell.  It connects
  the semiclassical soliton fluctuation determinant to the exact on-shell
  breather spectrum.
- The calculation shows that the finite DHN shift `-m/pi` is required for the
  exact pole formula `m_1=2 M_s sin(pi xi/2)` to reproduce the perturbative
  elementary boson mass through order `beta^2 m`.
- The proposition therefore makes the physical mass coordinate depend on the
  determinant/counterterm calculation, not only on the classical soliton
  profile.

Negative controls:

- Using the classical soliton mass alone leaves a spurious
  `beta^2/(8 pi)` correction to `m_1/m`.
- Using half of the finite DHN shift leaves half of the same spurious
  correction.
- The check keeps the weak-coupling series exact enough to catch either
  normalization failure.

Expected verification:

- Run the focused sine-Gordon S-matrix companion.
- Run focused Chapter 8 theorem/display/negative-scope/style audits.
- Run the calculation inventory/evidence audits, dossier audit, and monograph
  build before landing.
