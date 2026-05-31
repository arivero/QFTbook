# Doi-Peliti Non-Hermitian QFT Synthesis Pass

Date: 2026-05-31

## Trigger

GitHub issue #704 noted that Volume X, Chapter 10 derived the finite
Doi-Peliti algebra mechanically but did not synthesize why it belongs in a
QFT monograph: it is the finite-regulator bridge from classical stochastic
occupation dynamics to local non-Hermitian field theory.

## Edits

- Rewrote the opening of the Doi-Peliti section to state the construction as
  a map from a master equation to linear Fock-space evolution
  `partial_t |P_t> = L_DP |P_t>`.
- Identified `L_DP` as a Markov generator rather than a unitary Hamiltonian.
- Made the projection-state conservation law `<1| L_DP=0`, equivalently
  `H_DP(1,z)=0`, the structural replacement for unitary norm conservation in
  the non-Hermitian setting.
- Explained the complementary roles of MSRJD and Doi-Peliti:
  continuous Gaussian-increment variables versus integer occupation-number
  jump systems.
- Replaced loose universality language by an operational fixed-point
  statement: common scaling limits, relevant perturbations, and matching
  scaling correlation/response functions.
- Added canonical reaction-diffusion examples only as targets of such
  controlled continuum fixed-point claims, not as theorem statements.
- Extended the theorem-boundary/open-problem paragraph to include continuum
  limits of spatially regulated Doi-Peliti reaction networks.
- Updated the Volume X Chapter 10 dossier.

## Verification Plan

- Run the nonequilibrium open-system calculation check.
- Run text/proof/label/dossier audits and build the monograph.
- Comment on and close GitHub issue #704 if the build is clean.
