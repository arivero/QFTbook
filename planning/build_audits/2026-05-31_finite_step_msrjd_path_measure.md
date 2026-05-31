# Finite-Step MSRJD Path-Measure Pass

Date: 2026-05-31

Scope:

- Volume X, Chapter 10, `Nonequilibrium Steady States And Open-System Limits`.
- GitHub issue context: #703 statmech-to-QFT absorption and finite-regulator
  nonequilibrium foundations.

Edits:

- Added a finite-step Langevin/MSRJD section before the weak-coupling
  open-system limit.
- Defined the regulated variables \(x_n\), increments \(\Delta x_n\),
  drift \(F_n\), Gaussian covariance \(2\Delta t\,D\), and response-field
  variables \(\hat x_n\).
- Derived the path density from the finite Ito Gaussian increment measure.
- Derived the MSRJD representation as the Fourier transform of the same
  Gaussian transition kernel at each time step.
- Derived the finite-step generator expansion and the corresponding
  Fokker-Planck adjoint equation from Gaussian moments.
- Updated the chapter dossier and calculation-check ledger.

Calculation checks:

- `calculation-checks/nonequilibrium_open_system_checks.py` now checks the
  one-dimensional Fourier kernel normalization, the two-dimensional
  determinant normalization, and the finite-step Langevin generator expansion
  on a cubic test function.

Quality note:

- The pass avoids presenting the response field as formal continuum
  notation.  It is introduced as a finite Fourier-dual integration variable,
  with continuum stochastic field theory described as a subsequent limiting
  problem requiring regulator, drift, covariance, discretization, and
  convergence data.
