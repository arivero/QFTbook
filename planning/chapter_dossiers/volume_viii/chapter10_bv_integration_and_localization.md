# Chapter 10: BV Integration And Finite-Dimensional Localization

## Logical Role

Volume VIII uses this chapter as the finite-dimensional proof infrastructure
for cohomological localization and BV pushforward.  Later gauge-theoretic
applications must add regulator, compactness, determinant-line, and boundary
analysis before invoking the identities here.

## Definitions And Results

- Odd symplectic finite-dimensional graded manifold \((\mathcal F,\omega)\),
  Hamiltonian vector fields, BV bracket, and the classical master equation.
- Semidensity form of the quantum master equation \(\Delta\rho=0\), together
  with the action form
  \(\frac12\{S,S\}+\hbar\Delta_\mu S=0\).
- Quantum observable equation
  \(\Delta_\mu\mathcal O+\hbar^{-1}\{S,\mathcal O\}=0\).
- Product identity for \(\Delta_\mu(F\exp(S/\hbar))\).
- Lagrangian gauge-fixing cycles and the finite-dimensional BV Stokes
  theorem.
- Gauge-fixing independence under Lagrangian cobordism.
- BV pushforward along a fluctuation Lagrangian and preservation of the
  quantum master equation.
- BV pushforward with fluctuation boundary:
  \(\Delta_{\rm res}\pi_*\rho=-\mathcal B_{\partial\mathcal L}(\rho)\).
- Singular-stratum boundary data for localized gauge-theory moduli spaces,
  including the precise obstruction term and the resolution/relative-cycle/
  residue data required to cancel it.
- \(Q\)-exact deformation invariance for finite-dimensional cohomological
  integrals under the explicit hypothesis \(\int_M Q\beta=0\).
- One-loop normal form and the
  \(\operatorname{Pf}(B)/\sqrt{\det A}\) normal Gaussian factor.
- Rank-one Mathai--Quillen model with integral
  \(\int_{\mathbb R}\Theta_{t,a}=\operatorname{sign}(a)\).
- Compact \(S^2\) Atiyah--Bott fixed-point model with
  \(\int_{S^2}\exp(\omega+\lambda H)
  =2\pi(\ee^\lambda-\ee^{-\lambda})/\lambda\), derived both by direct
  integration and by the two fixed-point weights.
- Boundary and noncompact-cycle obligations for gauge-theoretic localization.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\mathcal F\) | finite-dimensional graded BV field space |
| \(\omega\) | odd symplectic form of degree \(-1\) |
| \(X_F\) | Hamiltonian vector field of \(F\) |
| \(\{F,G\}\) | BV odd Poisson bracket |
| \(S\) | degree-zero BV action |
| \(Q_S\) | Hamiltonian differential \(\{S,-\}\) |
| \(\rho\) | BV semidensity |
| \(\mu\) | compatible Berezinian density used to write \(\Delta_\mu\) |
| \(\Delta,\Delta_\mu\) | canonical semidensity BV operator and its function representative |
| \(\mathcal L\) | Lagrangian gauge-fixing cycle |
| \(\mathcal F_{\rm res},\mathcal F_{\rm fluc}\) | residual and fluctuation BV variables |
| \(\pi_*\rho\) | BV pushforward semidensity |
| \(\mathcal B_{\partial\mathcal L}\) | boundary functional of a fluctuation Lagrangian cycle |
| \(Q,V,I(t)\) | cohomological differential, odd deformation functional, and deformed integral |
| \(F,N_F,e_Q(N_F)\) | localization fixed locus, normal bundle, and equivariant Euler class |
| \(\mathcal M^{\rm sm},S_\alpha,\widetilde{\mathcal M}\) | smooth fixed locus, singular strata, and resolved fixed locus |
| \(A,B\) | even symmetric and odd antisymmetric normal quadratic operators |
| \(\Theta_{t,a}\) | rank-one Mathai--Quillen Thom density |
| \(V,\lambda,H,\Omega_\lambda\) | circle generator, equivariant parameter, moment map, and equivariantly closed form in the \(S^2\) model |

## Claim Ledger

1. The classical master equation is equivalent to \(Q_S^2=0\) by the graded
   Jacobi identity.
2. The semidensity quantum master equation is the coordinate-independent
   finite-dimensional BV condition; the displayed action form depends on the
   chosen Berezinian trivialization.
3. The BV product identity follows from the defining second-order property of
   \(\Delta_\mu\) and the quantum master equation for \(S\).
4. BV Stokes reduces locally to ordinary Stokes on a Lagrangian Darboux chart.
5. Gauge-fixing independence follows from BV Stokes on the Lagrangian
   cobordism swept by the family of gauge-fixing cycles.
6. BV pushforward preserves the quantum master equation after the fluctuation
   BV Laplacian integrates to zero on the chosen Lagrangian cycle.
7. If the fluctuation Lagrangian has boundary, BV pushforward obeys
   \(\Delta_{\rm res}\pi_*\rho=-\mathcal B_{\partial\mathcal L}(\rho)\);
   the boundary functional must vanish or be cancelled by additional data.
8. Singular fixed-locus strata are BV boundary data.  Smooth-stratum
   localization satisfies the residual QME only after vanishing,
   relative-cycle, resolution, or residue data have cancelled the stratum
   boundary functional.
9. \(Q\)-exact localization is valid exactly when the integration functional
   annihilates \(Q\)-exact terms in the class under consideration.
10. The normal localization factor is
   \(\operatorname{Pf}(B)/\sqrt{\det A}\) after Gaussian rescaling and
   determinant-line orientation choices.
11. The rank-one Mathai--Quillen density integrates to the local degree of the
   section at its transverse zero.
12. The \(S^2\) equivariant integral equals the sum of the north and south
    fixed-point contributions with weights \(w_N=1\) and \(w_S=-1\).
13. Noncompact ends, boundaries, reducible connections, small instantons, and
    residue prescriptions are part of the data required for any
    infinite-dimensional localization statement.

## Calculation Checks

- `calculation-checks/bv_localization_checks.py` verifies the one-pair BV
  Laplacian product identity, BV Stokes endpoint formula, the finite
  residual/fluctuation boundary-obstruction model, normal
  Pfaffian/determinant factor, rank-one Mathai--Quillen normalization, and
  the \(S^2\) fixed-point coefficient identity.

## Figure Ledger

No figure is included in this pass.  Future figures should include
Lagrangian-cycle deformation, fixed-locus normal complex, and boundary-term
flow diagrams.

## Audit Notes

- 2026-05-29 seventh anti-wrapper pass: expanded the BV pushforward with
  fluctuation boundary proof, and narrowed the observable version to
  finite-dimensional quantum observables satisfying
  \(\Delta_{\mathcal F}(\mathcal O\rho)=0\).
