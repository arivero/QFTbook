# Chapter 07: Mirror-Channel TBA And Finite-Size Effects
Source-File: monograph/tex/volumes/volume_vi/chapter07_mirror_channel_tba_finite_size_wrapping.tex

## Source Position

Volume VI now moves from ground-state TBA and integrable RG-flow scaling
functions to finite-size interpretation on the Euclidean torus.  The chapter
prepares later exact model chapters and later planar-integrability comparison
by separating relativistic mirror thermodynamics from spin-chain wrapping
language.

## Notation Inventory

- `mathfrak M`: mirror finite-size TBA datum, collecting the torus functional,
  direct and mirror Hamiltonian decompositions, diagonal mirror scattering
  phases, thermodynamic density/entropy convention, bulk energy coordinate,
  and analytic strip/pole data.
- `R`, `L`: torus cycle lengths and direct/mirror inverse temperatures.
- `H_R`, `E_0(R)`: direct-channel Hamiltonian and circle vacuum energy.
- `tilde H_L`, `f_mir(R)`: mirror Hamiltonian and mirror free-energy density.
- `m_a`, `theta`, `S_ab`, `varphi_ab`: masses, rapidity, diagonal scattering
  amplitude, and TBA kernel.
- `rho_a`, `rho_a^h`, `epsilon_a`: Bethe particle density, hole density, and
  pseudoenergy.
- `S_mir`, `P_mir`: mirror thermodynamic entropy/density convention and
  mirror analytic strip/pole ledger.
- `q_a(theta)`: large-circumference mirror occupation factor.
- `mathsf A`, `m_*`, `Phi`: finite mirror-species set, lightest mirror mass,
  and \(L^1\) kernel bound used in the vacuum Luescher remainder theorem.
- `Delta E_Psi^F`: first finite-size mirror correction to an excited state.
- `E_Psi^BY`, `Delta E_Psi^mu`, `R_trace`, `R_cont`, `R_branch`,
  `R_pole`, `R_multi`, `R_dens`, `R_norm`: Bethe--Yang energy, crossed-pole
  mu-term, and the residual coordinates separating the exact direct
  excited-state spectral trace from the Bethe--Yang plus one-winding
  F-/mu-term approximation.

## Claim Ledger

- Aggregates the finite-size framework into Hypothesis
  `hyp:mirror-finite-size-tba-datum` before using mirror rotation, TBA
  kernels, density equations, or wrapping contours.
- Proves the relation between direct-channel vacuum energy and mirror-channel
  pressure from equality of torus decompositions.
- Derives the mirror TBA functional from the density constraint and entropy
  extremization; the mirror variational equation is recorded as the same
  calculation in the mirror channel rather than a separate theorem-family
  result.
- Extracts the first large-circumference vacuum correction as a one-mirror
  occupation contribution.
- Proves the vacuum Luescher coefficient
  \(-\sum_a m_aK_1(m_aR)/\pi\) from the TBA fixed point under a finite species,
  positive mass gap, and integrable-kernel hypothesis, with a
  \(O(R^{-1/2}e^{-2m_*R})\) bound on the two-winding remainder.
- States the first excited-state finite-size correction with the required
  analytic-strip and pole-data hypotheses.
- Adds an excited-state continuation status checkpoint: direct-state
  insertions, continuation path in \(R\) and rapidity space, crossed
  singularities, source terms, omitted-pole control, and comparison with the
  direct-channel spectral trace are theorem obligations beyond the
  one-winding formula.
- Adds a finite excited-state continuation proof-obligation map: the difference
  between the direct-channel excitation energy and the Bethe--Yang plus
  one-winding F-/mu-term coordinate is decomposed into trace, contour, branch,
  missed-pole, multi-mirror, density, and normalization residuals, with a
  conditional triangle propagation once component estimates are supplied.
- Defines wrapping effects as finite-cycle mirror propagation and records the
  distinction from later planar spectral wrapping.

## Calculation Checks

- `calculation-checks/mirror_tba_wrapping_checks.py` verifies the two-winding
  expansion of the mirror occupation functional, the vacuum-energy
  coefficients, the Bessel \(K_1\) normalization in the Luescher term, the
  large-\(R\) asymptotic coefficients and exponential-remainder threshold,
  the F-term product subtraction, and the orientation sign in the
  \(\mu\)-term residue ledger.  It also checks the excited-state
  continuation proof-obligation telescope and keeps the residual nonzero unless the
  theorem-level trace, contour, pole, multi-mirror, density, and normalization
  controls are supplied.

## Audit Notes

- 2026-06-02 issue #561 dossier-link pass: recorded the already-existing
  mirror-channel finite-size calculation check explicitly in the chapter
  dossier.  No new formula was changed in the manuscript.
- 2026-06-03 reconstruction-spine point-of-use pass: added the excited-state
  continuation checkpoint so F-terms and \(\mu\)-term residues are presented
  as the first entries of a contour/singularity ledger rather than as a
  theorem-level excited-state TBA construction.
- 2026-06-04 issue #728 excited-state TBA residual pass: added the
  continuation proof-obligation map from the direct spectral trace to the
  one-winding coordinate.  The companion check verifies the telescope,
  conditional triangle propagation, and nonzero residual so finite F-/mu-term
  formulae are not overclaimed as exact excited-state reconstruction.
- 2026-06-06 issue #844 residual-status audit: demoted the continuation
  display to `rem:excited-state-continuation-proof-obligation-map`, since its
  proof content is identity plus declared component estimates.

## Figure Ledger

No figure is included in this pass.  A future figure should draw the same
Euclidean torus with the direct and mirror Hamiltonian cuts, plus a rapidity
strip showing the contour displacement by \(i\pi/2\) and possible pole
crossings.
