# Volume X Kinetic Theory Deepening Audit

## Scope

This pass addresses the later-volume thinness directive for Volume X,
Chapter 8.  The chapter is rewritten from a survey-level outline into a
derivation-level presentation of relativistic kinetic theory as a controlled
quasiparticle limit of thermal QFT.

## Edits

- Rewrote
  `monograph/tex/volumes/volume_x/chapter08_kinetic_theory_controlled_limit.tex`.
- Added the \(D=d+1\) convention, on-shell measure, and equal-time
  normalization.
- Defined the quasiparticle distribution through the pole coefficient of a
  Wigner-transformed two-point function, including narrow-width and
  slow-variation hypotheses.
- Replaced the collision-kernel sketch by the covariant Boltzmann equation
  and the explicit \(2\to2\) collision operator with Bose/Fermi factors.
- Derived detailed balance from
  \(1+\eta f=e^{\beta(-u_\mu p^\mu-\mu q)}f\).
- Derived the kinetic entropy-current divergence and the H-theorem
  integrand \((X-Y)\log(X/Y)\).
- Derived hydrodynamic Ward identities as collision-invariant moments.
- Added the linearized collision-operator inner product, positive quadratic
  form, and null-space statement.
- Added a controlled relaxation-time worked example for the shear channel,
  including \(\eta_{\rm RTA}=4p_{\rm therm}\tau_R/5\).
- Added `calculation-checks/kinetic_theory_checks.py` and documented it in
  `calculation-checks/README.md`.
- Rewrote the Volume X Chapter 8 dossier.

## Verification

- `python3 calculation-checks/kinetic_theory_checks.py`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed; rebuilt
  `monograph/tex/main.pdf` at 1320 pages.
