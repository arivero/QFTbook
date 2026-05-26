# Volume X Hydrodynamic Ward-Identity Deepening Audit

## Scope

This pass addresses the later-volume thinness directive by rewriting Volume X,
Chapter 5 as a derivation-level bridge from microscopic Ward identities and
Kubo coefficients to deterministic first-order hydrodynamics.

## Edits

- Rewrote
  `monograph/tex/volumes/volume_x/chapter05_hydrodynamics_from_ward_identities.tex`.
- Added a precise \(D=d+1\) mostly-plus convention layer, Landau-frame
  definition, and thermodynamic closure.
- Added propositions deriving the ideal energy equation, Euler equation,
  charge equation, and ideal entropy-current conservation.
- Added the first-order Landau-frame constitutive relations with
  \(J_A^\mu=n_Au^\mu-T\Sigma_{AB}\Delta^{\mu\nu}\partial_\nu(\mu_B/T)\).
- Derived the first-order entropy-production formula and the positivity
  requirements on \(\eta\), \(\zeta\), and \(\Sigma_{AB}\).
- Derived charge diffusion, shear diffusion, and sound poles with explicit
  attenuation
  \[
    \Gamma_s=(\zeta+2\eta(d-1)/d)/(\varepsilon+p).
  \]
- Added the diffusive density retarded correlator and the hydrodynamic
  scaling-limit theorem boundary.
- Added `calculation-checks/hydrodynamic_modes_checks.py` and documented it
  in `calculation-checks/README.md`.
- Rewrote the Volume X Chapter 5 dossier with updated symbols, claims, and
  the calculation-check companion.

## Verification

- `python3 calculation-checks/hydrodynamic_modes_checks.py`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed; rebuilt
  `monograph/tex/main.pdf` at 1314 pages.
