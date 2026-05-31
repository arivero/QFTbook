# Finite Schwinger-Keldysh / MSRJD Bridge Pass

Date: 2026-05-31.

Scope:
- Volume X, Chapter 10, Schwinger-Keldysh influence-functional section.
- GitHub issue context: #703 statmech-to-QFT nonequilibrium absorption and
  #691 theorem-form discipline.

Changes:
- Added a finite-regulator derivation of the Gaussian bridge from a quadratic
  Schwinger-Keldysh influence weight to a stochastic equation.
- The new text starts with the finite response weight
  `exp(i phi_a E(phi_r) - phi_a N phi_a / 2)` and states the hypotheses on
  the finite noise matrix `N`.
- It proves the Hubbard-Stratonovich characteristic-function identity for
  `N > 0`, explains the quotient convention when `N` has null directions, and
  derives the finite constraint `E(phi_r)+xi=0`.
- For a linear retarded equation `E=K phi_r-J`, it records the induced
  response covariance `K^{-1} N K^{-T}` and separates colored finite noise
  from the additional Markovian white-noise scaling limit.
- No theorem/proposition wrapper was added; this is a finite derivation at
  the point of use.

Companion checks:
- Extended `calculation-checks/nonequilibrium_open_system_checks.py` with a
  finite two-dimensional Gaussian characteristic-function check and a
  covariance reconstruction check `K (K^{-1} N K^{-T}) K^T=N`.
- Updated the calculation-check README, chapter dossier, and statmech
  crosswalk.

Verification:
- `python3 calculation-checks/nonequilibrium_open_system_checks.py`
- `python3 -m py_compile calculation-checks/nonequilibrium_open_system_checks.py`
- `git diff --check`

Full-build status:
- `tools/build_monograph.sh` completed cleanly; `main.pdf` rebuilt at 2748
  pages.
