# Finite Reaction-Network Doi-Peliti Pass

Date: 2026-05-31

Scope:

- Volume X, Chapter 10, `Nonequilibrium Steady States And Open-System Limits`.
- GitHub issue context: #703 statmech-to-QFT absorption, nonequilibrium
  field-theory foundations.

Edits:

- Added a finite reaction-network and Doi-Peliti section after the finite-step
  MSRJD derivation.
- Defined occupation vectors, multi-index falling factorials, reaction
  input/output data, mass-action jump rates, and the master equation.
- Derived the normally ordered Doi-Peliti generator from the master equation
  on the algebraic occupation-number domain.
- Defined coherent states and the normal symbol
  \(H_{\rm DP}(\bar z,z)\), with probability conservation expressed as
  \(H_{\rm DP}(1,z)=0\).
- Derived the deterministic mass-action rate equation from
  \(\partial_{\bar z}H_{\rm DP}|_{\bar z=1}\).
- Extracted the finite-regulator dynamical large-deviation Hamiltonian from
  exponential test functions, with the proof boundary for a full path LDP
  stated separately.

Calculation checks:

- `calculation-checks/nonequilibrium_open_system_checks.py` now verifies the
  Doi-Peliti generator matrix against the direct master generator for a
  fixed-total-number two-species network.
- The same script checks \(H_{\rm DP}(1,z)=0\), the symbol-derived drift, and
  the exponential-test Hamiltonian formula.

Quality note:

- The section avoids treating the Doi-Peliti action as a formal definition.
  It derives the operator and symbol from a finite Markov generator, then
  identifies which additional estimates are needed for continuum
  reaction-diffusion QFT or large-deviation limits.
