# Chapter 07: Thermal Gauge Theory And Screening
Source-File: monograph/tex/volumes/volume_x/chapter07_thermal_gauge_theory_screening.tex

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
- `mathcal A_mu`, `mathcal F_mu nu`: connection-normalized gauge field and
  curvature used in the Yang--Mills action, EQCD, Wilson lines, and Polyakov
  holonomies.
- `a_mu=mathcal A_mu/g`, `f_mu nu=mathcal F_mu nu/g`: canonical soft gauge
  potential and curvature used for real-time HTL source response.
- `v^\mu`, `W(x,v)`, `K_R^{\mu\nu}`: unit hard-particle velocity, adjoint
  HTL auxiliary field, and canonical-source retarded induced-current kernel
  whose static electric component is the Debye coefficient.
- `n_B`, `n_F`: Bose and Fermi occupation functions used in the
  susceptibility derivation of the one-loop Debye coefficient.
- `g_3^2=g^2T`: connection-normalized three-dimensional coupling; the
  three-dimensional EQCD zero-mode correlator of `mathcal A_0` carries
  `g_3^2/(k^2+m_E^2)`.
- `P(x)`, `C_R`, `C_{R\bar R}`, `F_Q`, `Delta F_{R\bar R}`:
  Polyakov loop, one-line expectation, neutral pair correlator, static
  external-charge free energy, and line-renormalization-independent pair
  excess free energy in sectors where the one-line expectations are nonzero.
- `F_avg`, `F_1`, `F_adj`: color-averaged traced Polyakov-pair free energy
  and singlet/adjoint channel coordinates, with the latter requiring a
  gauge-fixed or cyclic-Wilson-loop definition rather than separately traced
  loops.
- `M_hard`: hard gap for modes integrated out in the local EQCD expansion,
  normally of order `2 pi T` only under the declared weak-coupling and
  holonomy assumptions.

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
- Proves the origin of the Debye term from the second variation of the
  background-field effective action, including contact/seagull terms
  `<S''>` in addition to the connected product of first variations; the
  determinant calculation then computes the coefficient through thermal
  susceptibility integrals and background-field vector-minus-ghost counting.
- Separates connection-source and canonical-source Debye curvatures:
  varying with respect to `mathcal A_0` gives `chi=m_D^2/g^2`, while varying
  with respect to `a_0=mathcal A_0/g` gives the canonical HTL polarization
  `m_D^2`.
- Records the convention distinction that a complex scalar in representation
  `R` contributes `g^2 T^2 T_R/3`, while one real scalar degree in a real
  representation contributes `g^2 T^2 T_R/6`.
- Adds the HTL bridge from static Debye matching to the conserved retarded
  induced-current response: the chapter derives the covariant auxiliary-field
  conservation law in canonical variables, the linear retarded angular kernel,
  its transversality, the zero-frequency static electric limit, and the
  conversion to connection-source current `j_mathcal A=j_a/g`.
- Separates electric matching from nonperturbative magnetic screening in the
  dimensionally reduced theory.
- Defines the separately traced Polyakov-pair observable as color averaged,
  distinguishes it from gauge-fixed singlet coordinates and gauge-invariant
  cyclic Wilson loops, and records their different gauge-dependence and
  line/cusp/intersection/mixing renormalization data.
- Proves that the connected color-averaged pair excess free energy cancels
  local line self-energies only in a fixed state/center sector or
  source-selected limit with nonzero one-line expectations.  Separately proves
  that the static source-pair force cancels local line self-energies without
  dividing by one-point functions.
- Defines local EQCD as a controlled approximation: a weak-coupling hierarchy
  `p,m_E,g_3^2 << M_hard ~ 2 pi T`, a regulator and matching prescription, a
  static operator basis, a truncation/remainder status, and explicit failure
  modes from holonomy-shifted light modes, strong coupling near transitions,
  imaginary chemical potentials, or additional light scalars.
- Carries the connection/canonical conversion through EQCD kinetic and mass
  terms, the static longitudinal propagator normalization, `g_3^2=g^2T`, and
  the Polyakov holonomy exponent
  `P exp(int mathcal A_0)=P exp(g int a_0)`.

## Figure Ledger

No figure is included in this pass.  Future figures should show the thermal
circle, a Polyakov loop pair, and the hierarchy of static scales
`T`, `gT`, and `g^2 T`.

## Calculation Checks

- `calculation-checks/thermal_screening_checks.py` verifies the static
  Yukawa/Bessel asymptotic powers, the transverse-projected pole residue, and
  the trace-convention conversion of the Debye coefficient; the
  second-background-variation contact/seagull ledger; the HTL angular kernel's
  transversality and static-limit algebra; the exact connection/canonical
  conversion under `mathcal A=ga` for the kinetic term, Debye mass term,
  one-particle-irreducible kernel, static propagator, induced current, and
  holonomy exponent; color-averaged versus singlet Polyakov-channel weights and
  cyclic-loop renormalization extras; the exact finite algebra by which
  Polyakov-loop pair ratios and static forces cancel line self-energies,
  including the zero-one-point center-symmetric domain distinction; and the
  finite hierarchy/exceptions logic behind local EQCD matching.

## Audit Notes

- 2026-05-30 full-development pass: corrected the static correlator power
  from \(r^{-(d-2)/2}\) to \(r^{-(d-1)/2}\), added the Bessel-function
  derivation and spatial-transfer-matrix interpretation, and made explicit
  that gauge-invariant screening masses are not the same object as the
  gauge-fixed perturbative Debye pole.
- 2026-06-03 static-source renormalization pass: added the finite-regulator
  datum for Polyakov-line multiplicative renormalization, derived cancellation
  of local line self-energies in connected pair ratios and source-pair forces,
  and extended the thermal screening companion check to guard the cancellation
  and finite line-scheme invariance.
- 2026-06-03 ratio-domain correction: qualified the pair-excess ratio by the
  nonzero one-line expectation/source-selected sector hypothesis, separated it
  from the direct source-pair force, and recorded the finite-volume
  center-symmetric observable as the neutral pair correlator or its
  \(r\)-derivative rather than a one-source free energy.
- 2026-06-03 HTL-response bridge: added the real-time hard-thermal-loop
  mechanism behind the static Debye coefficient, with the retarded angular
  kernel, covariant current-conservation derivation, static electric limit,
  and companion finite algebra check.
- 2026-06-05 issue #792 pass: corrected Polyakov-pair channel language from
  singlet to color-averaged, separated gauge-fixed singlet and cyclic Wilson
  loop definitions, rewrote the Debye origin lemma as a full background-field
  second variation including contact/seagull terms, and upgraded EQCD from a
  distance-only statement to a controlled local matching approximation with
  hard-gap, weak-coupling, holonomy, operator-basis, and remainder hypotheses.
- 2026-06-08 issue #885 pass: separated connection-normalized
  `mathcal A_mu` from canonical `a_mu`, made the Debye curvature conversion
  explicit, rewrote the HTL bridge as a canonical-source response, carried the
  conversion through EQCD and Polyakov holonomy conventions, and added an exact
  finite regression check for the normalization chain.
