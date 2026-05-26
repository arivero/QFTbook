# 2026-05-26 Issue #582 Physical-Parameter Entropy

## Manuscript Change

- Volume XI, Chapter 9 now proves
  `prop:spde-negative-sector-physical-parameter-entropy`.
- The proposition separates the test-function supremum from the finite
  physical parameters by introducing
  \[
    Q_{n,\tau}^{\#}(z,\delta)
    =
    \sup_{\varphi\in\mathcal B_r}
    \delta^{-|\tau|}
    |\langle\Pi_z^{(n)}\tau,\varphi_z^\delta\rangle|.
  \]
- After this dualization, the \(\Pi\)-coordinate parameter spaces are
  \(K\times[1/2,1]\), where the second factor is the dyadic scale ratio.
- The \(c_n\) reexpansion coordinate is parametrized by \(K\) times the
  parabolic annulus of normalized separations.

## Entropy Constants

- For dynamic \(\Phi^4_3\), \(\mathfrak s=(2,1,1,1)\) and
  \(Q=|\mathfrak s|=5\).
- \(\Pi\)-coordinates have scale entropy \(D=5\) and edge entropy \(d=6\):
  five dimensions for the base point plus one dimension for the scale ratio.
- The \(c_n\) coordinate has scale entropy \(D=5\) and edge entropy \(d=10\):
  five dimensions for the base point plus five dimensions for the normalized
  separation.
- `calculation-checks/constructive_scalar_spde_checks.py` now verifies these
  exponents and a sample high-moment scale-slack inequality.

## Remaining Issue #582 Obligations

- Prove the Banach-valued or dual-norm stochastic coordinate estimates for
  \(Q_{n,\tau}^{\#}\), rather than relying on pointwise test-function estimates.
- Prove the concrete BPHZ kernel estimates for each negative-sector coordinate
  in the physical parameter spaces introduced here.
- Extend the same parameter-space treatment to the positive sector needed by
  the nonlinear fixed-point theorem.
