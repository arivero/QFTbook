# Soft-Drop Mass Factorization Datum Pass

Date: 2026-06-01

Issue lane: #526, with overlap to #630.

Scope:
- Volume II Chapter 19b, the modern jet-substructure and SCET section.
- `calculation-checks/scet_factorization_checks.py`.
- Chapter 19b dossier and calculation-check README.

What changed:
- Added the renormalized soft-drop groomed-mass factorization datum after the
  fixed-coupling radiator chart.
- Derived the boundary scales directly from
  \(z\theta^2=\rho\) and \(z=z_{\rm cut}\theta^{\beta_{\rm SD}}\), giving
  \(\theta_*=(\rho/z_{\rm cut})^{1/(2+\beta_{\rm SD})}\) and
  \(z_*=z_{\rm cut}^{2/(2+\beta_{\rm SD})}
  \rho^{\beta_{\rm SD}/(2+\beta_{\rm SD})}\).
- Stated the natural scales
  \(\mu_H\sim Q\), \(\mu_G\sim Qz_{\rm cut}\),
  \(\mu_J\sim Q\sqrt\rho\), and
  \(\mu_{\rm cs}\sim Q\sqrt{\rho z_*}\), with the
  \(\beta_{\rm SD}=0\) mMDT specialization made explicit.
- Defined the factorization datum as hard, global-soft, collinear-jet, and
  collinear-soft distributions paired with endpoint test functions, plus
  overlap subtraction, rapidity data when present, anomalous-dimension
  consistency, and a remainder functional.
- Added a controlled-approximation boundary: perturbative soft-drop mass
  resummation is controlled only when the stated scales remain perturbative,
  the remainder is bounded in the declared topology, and nonperturbative
  collinear-soft regions are replaced by a shape coordinate or a
  regulator-level reconstruction observable.

Calculation check:
- Extended `calculation-checks/scet_factorization_checks.py` with exact
  rational checks that the stated \(\theta_*,z_*\) solve the mass and grooming
  equations, that \(\mu_{\rm cs}^2=\rho z_*\) lies below the collinear scale
  for \(z_*<1\), and that hard/global-soft/jet/collinear-soft RG transport is
  independent of the common scale when
  \(\gamma_H+\gamma_G+\gamma_J+\gamma_{\rm cs}=0\).

Status:
- This is not a closure of #526.  It closes one concrete measured-observable
  factorization gap between the fixed-coupling soft-drop radiator and a
  renormalized resummation datum.  The issue remains open for broader
  jet-substructure regimes and stronger continuum factorization examples.
