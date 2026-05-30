# Chapter 07: Thermal Gauge Theory And Screening

## Source Position

Volume X now applies thermal and Schwinger-Keldysh foundations to gauge
theories.  The chapter introduces static screening, Debye masses, magnetic
infrared dynamics, Polyakov loops, and dimensionally reduced static effective
theories before kinetic theory and anomalous transport.

## Notation Inventory

- `beta=1/T`, `omega_n`: thermal circle length and Matsubara frequencies.
- `O_0(x)`, `M_alpha`: static projection and screening masses.
- `T_R`, `C_A`: group invariants in the monograph trace convention.
- `m_D`, `m_E`: perturbative Debye mass and matched electric mass parameter.
- `n_B`, `n_F`: Bose and Fermi occupation functions used in the
  susceptibility derivation of the one-loop Debye coefficient.
- `A_0`, `A_i`, `g_3^2`: temporal scalar, spatial gauge field, and
  three-dimensional coupling.
- `P(x)`, `F_Q`: Polyakov loop and static external-charge free energy.

## Claim Ledger

- Defines static screening masses through gauge-invariant static correlators.
- Corrects and derives the unprojected static Yukawa asymptotic:
  an isolated scalar pole in \(d\) spatial dimensions contributes
  \(e^{-Mr}/r^{(d-1)/2}\), while transverse projection gives the pure
  transfer-matrix exponential \(Ze^{-M|z|}/(2M)\).
- Separates physical screening masses, defined by gauge-invariant static
  transfer-matrix channels, from the perturbative Debye pole/matching
  coefficient of a gauge-fixed static effective theory.
- Derives the one-loop Debye mass in the monograph trace and coupling
  convention, including gauge, Dirac, complex-scalar, and real-scalar
  coefficients and the `SU(N)` fundamental-trace conversion.
- Proves the origin of the Debye term from the static current-current
  correlator, then computes the coefficient through thermal susceptibility
  integrals and background-field vector-minus-ghost determinant counting.
- Records the convention distinction that a complex scalar in representation
  `R` contributes `g^2 T^2 T_R/3`, while one real scalar degree in a real
  representation contributes `g^2 T^2 T_R/6`.
- Separates electric matching from nonperturbative magnetic screening in the
  dimensionally reduced theory.
- Defines Polyakov-loop free energies and the EQCD matching problem.

## Figure Ledger

No figure is included in this pass.  Future figures should show the thermal
circle, a Polyakov loop pair, and the hierarchy of static scales
`T`, `gT`, and `g^2 T`.

## Calculation Checks

- `calculation-checks/thermal_screening_checks.py` verifies the static
  Yukawa/Bessel asymptotic powers, the transverse-projected pole residue, and
  the trace-convention conversion of the Debye coefficient.

## Audit Notes

- 2026-05-30 full-development pass: corrected the static correlator power
  from \(r^{-(d-2)/2}\) to \(r^{-(d-1)/2}\), added the Bessel-function
  derivation and spatial-transfer-matrix interpretation, and made explicit
  that gauge-invariant screening masses are not the same object as the
  gauge-fixed perturbative Debye pole.
