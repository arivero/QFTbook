# Charged Many-Body Dollard Phase Datum

Date: 2026-06-01.

Scope:

- Continued GitHub issue #527 without closing it.
- Added finite many-body Dollard bookkeeping to Volume IV Chapter 5 after the
  one-pair Coulomb-tail calculation.
- Defined the creator/adjoint orientation sign \(\eta_i\), the relative
  velocity \(u_{ij}=v_i-v_j\), and the pair data
  \((a_{ij},b_{ij},\kappa_{ij})\) entering the finite comparison model.
- Made explicit that the nonintegrable part of the charged comparison phase
  must be exhausted by oriented pair fluxes:
  \[
    \Theta_I(T)=
    \sum_{i<j}\eta_i\eta_j{\kappa_{ij}\over |u_{ij}|}\log T+O(1).
  \]
- Recorded the velocity-separation boundary: equal-velocity charged pairs are
  not covered by this datum and must be treated as charged clusters or as
  separate infraparticle/bound-state sectors.

Calculation checks:

- Extended `calculation-checks/charged_flux_dressing_checks.py` with exact
  rational checks for the oriented pairwise many-body logarithmic coefficient.
- The check verifies ordering independence, the sign change induced by
  conjugating one charged creator, and decay of the log-subtracted finite
  Coulomb-pair remainder on large dyadic time intervals.

Status:

- This is finite comparison bookkeeping, not a theorem about QFT.  The
  theorem-level debt in #527 remains: derive the pair coefficients and the
  \(L^1\) remainder from noncompact Wilson-line or Coulomb-dressed charged
  creators, prove the modified Cook estimate, construct the charged
  asymptotic representation, and establish the dressed LSZ reduction.
