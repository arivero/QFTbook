# Buchholz Infraparticle Mechanism Expansion

Date: 2026-05-30.

## Scope

- Chapter:
  `monograph/tex/volumes/volume_ii/chapter22_infrared_divergences_and_inclusive_qed.tex`.
- Issues: contributes to the quoted-theorem proof-debt audit (#695), the
  anti-wrapper/proof-substance audit (#691), and the charged-sector
  Haag--Ruelle/LSZ backlog (#527/#528).

## Defect Addressed

The chapter quoted Buchholz's infraparticle obstruction and gave the
soft-profile non-Fock norm, but the immediate mechanism was still too terse
for the monograph standard.  The result should not read as an imported theorem
followed by a slogan that the electron is an infraparticle.

## Edit

- Inserted a mechanism paragraph explaining why a sharp Wigner one-particle
  charged representation is incompatible with velocity-dependent limiting
  electric flux when the flux is a superselection datum.
- Derived the boosted Coulomb flux normalization explicitly:
  `2 pi (1-beta^2) int_{-1}^1 dz/(1-beta z)^2 = 4 pi`.
- Derived the velocity-extraction ratio
  `E(beta, +zhat)/E(beta, -zhat)=((1+beta)/(1-beta))^2`, showing that the
  angular flux determines the charged velocity.
- Added the invariant angular soft-vector
  `V_v(n)=(v-(v.n)n)/(1-v.n)` and the logarithmic one-photon norm
  `||f_v-f_w||^2 = g^2/(2(2pi)^3) log(Lambda/mu) int |V_v-V_w|^2 + O(1)`.
- Clarified that these calculations explain the perturbative/coherent
  mechanism and are not a substitute for Buchholz's theorem.
- Updated the chapter dossier to record the new theorem-boundary mechanism.

## Checks

- Targeted check to run: `python3 calculation-checks/charged_flux_dressing_checks.py`.
- Standard text/build audits should be run before the next checkpoint.
