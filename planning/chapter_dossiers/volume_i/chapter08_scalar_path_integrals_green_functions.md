# Volume I, Chapter 8 Dossier: Scalar Path Integrals and Green Functions

## Status

Current status: source-block certified against 253a pp. 72--79 on
2026-05-22. The chapter has been rebuilt and visually audited after adding the
functional-delta field-eigenstate representation, the formal \(Z\) shorthand
with regulator status, the Euclidean field-insertion notation, and a more
explicit \(k^0\)-plane pole/contour figure. Tightened on 2026-05-24 for
GitHub issue #299 so the Chapter 4 Trotter/Feynman--Kac theorem is invoked
only for finite-dimensional Schrödinger spatial regulators with a closed
semibounded form. Tightened again for issue #300 by adding a named catalog of
constructive existence and scalar triviality regimes relevant to \([D\phi]\).
Issue #310 added the canonical finite-regulator scalar integration convention:
reference density, Gaussian measure, and full Euclidean density are distinct
named objects with displayed Radon--Nikodym factors.
Issue #313 added a master regulator/subtraction classification table, with
dimensional regularization explicitly classified as formal perturbative
meromorphic graph assignment rather than a path-integral measure.
Issue #314 added the Pauli--Villars auxiliary-field/determinant status row and
states that it is not used as a default path-integral construction.
Issue #478 added a self-contained spectral zeta determinant section with the
one-loop quadratic-fluctuation formula, the thermal harmonic-oscillator
determinant, and the circle Casimir finite part.
The 2026-06-04 metastability pass added a false-vacuum decay section that
starts from a finite-volume metastable state, treats the negative mode as a
contour problem, works through the quartic scalar oscillator bounce,
separates the translation zero mode and determinant ratio, derives dilute
multi-bounce exponentiation, and states the field-theory proof-status
boundary.
The 2026-05-29 anti-wrapper pass retitled the finite-dimensional regulator
proposition positively, demoted the zeta-scale calculation and the free
Feynman pole-placement check to worked paragraphs, and kept the determinant
and boundary-value formulas in place for later reference.

## Logical Role

This chapter follows the Noether-current chapter and precedes the
Kallen-Lehmann spectral representation. Its role is to formulate the scalar
field path integral as a regulated extension of the time-sliced quantum
mechanical construction, then explain how Euclidean, Wightman, and
time-ordered Green functions are related by analytic continuation.

The chapter does not introduce scattering amplitudes or Feynman diagrams for
scattering. It also does not organize perturbation theory; that belongs after
the spectral and Green-function structure is in place.

## Primary Source Anchors

- `transcription/tex/253a/foundations.tex`, section "Path Integral
  Quantization of Scalar Field Theory", from the field wave functional through
  the definitions of Wightman, time-ordered, and Euclidean Green functions.
- Source visual trace:
  `monograph/tex/build/source_visual_trace/253a_trace-072.png` through
  `monograph/tex/build/source_visual_trace/253a_trace-079.png`.
- Rendered audit:
  `planning/build_audits/2026-05-22_scalar_path_integrals_green_functions_source_figures.md`.
- `references/253a_notes.tex`, corresponding section, used only as a
  comparison layer for figures and formulas.
- `monograph/tex/volumes/volume_i/chapter04_lagrangian_formalism_and_quantum_mechanical_path_integrals.tex`,
  for the finite-dimensional time-slicing construction.
- `monograph/tex/volumes/volume_i/chapter05_correlation_functions_wick_rotation_and_gaussian_integrals.tex`,
  for Euclidean correlation functions and Gaussian functional integrals.
- `monograph/tex/volumes/volume_i/chapter06_relativistic_scalar_fields_and_canonical_quantization.tex`,
  for the free scalar Hamiltonian and field normalization.

## External Reference Boundary

- Schmidt, "Euclidean Reconstruction in Quantum Field Theory", is kept as a
  theorem-boundary reference for the relation between Schwinger and Wightman
  functions. The chapter only states the elementary analytic-continuation
  construction and its assumptions.

## Framework

Working framework:

- real scalar field on \(\mathbb M^D\);
- \(\hbar=1\) unless displayed;
- finite spatial volume or spatial momentum cutoff whenever a functional
  integral is treated as an actual finite-dimensional integral;
- finite-dimensional Trotter/Feynman--Kac statements require an actual
  finite-dimensional configuration space \(E_\Lambda\), positive kinetic
  quadratic form, and locally Kato bounded-below potential \(U_\Lambda\);
- continuum smooth cutoffs that leave infinitely many modes, covariance
  cutoffs, direct Euclidean spacetime lattice actions without a transfer
  matrix, and purely formal perturbative cutoffs are not consequences of the
  Chapter 4 Trotter theorem and must be separately constructed;
- field eigenstates are distributional generalized vectors, used only as a
  regulated heuristic bridge to the path-integral kernel;
- Euclidean correlators are initially defined either by a regulated Euclidean
  functional expression or by analytic continuation of Wightman functions when
  the required analyticity is available.
- constructive existence claims are categorized explicitly: \(P(\phi)_2\),
  \(\phi^4_3\), selected low-dimensional superrenormalizable
  scalar--fermion models, two-dimensional Yang--Mills, scalar triviality in
  \(D\ge4\) under the standard reflection-positive scaling-limit hypotheses,
  the open four-dimensional Yang--Mills continuum problem, and the broader
  open problem of constructing physically interacting four-dimensional
  Wightman/OS QFTs of scalar or gauge type.

## Notation Inventory

| Symbol | Type | Meaning |
| --- | --- | --- |
| \(\Psi[\varphi]\) | generalized wave functional | state represented on a fixed-time field configuration |
| \(\ket{\varphi}\) | generalized vector | field-configuration eigenstate |
| \(U(t_f,t_i)\) | unitary operator | Hamiltonian time evolution |
| \(C\) | contour | complex-time contour for the Lorentzian action |
| \(x_E=(\tau,\vec x)\) | coordinate | Euclidean spacetime point |
| \(S_E[\phi]\) | functional | Euclidean action |
| \(G_E\) | distribution | Euclidean/Schwinger Green function |
| \(W\) | distribution | Wightman function |
| \(G_T\) | distribution | time-ordered Green function |
| \(\Delta_E\) | distribution | free Euclidean scalar propagator |
| \(\Delta_F\) | distribution | free Lorentzian Feynman propagator |
| \(\epsilon\) | positive regulator | pole-displacement parameter in the Feynman prescription |
| \(E_\Lambda\) | finite-dimensional real vector space | spatially regulated field configurations |
| \(G_\Lambda^{AB}\) | positive kinetic quadratic form | finite-dimensional regulator Hamiltonian |
| \(U_\Lambda\) | real potential on \(E_\Lambda\) | finite-dimensional regulator Hamiltonian |
| \(Q_\Lambda\) | closed semibounded quadratic form | condition for invoking Trotter/Feynman--Kac |
| \(D_\Lambda^{\rm ref}\phi\) | finite-regulator density | canonical reference density on bosonic scalar configurations |
| \(\dd\mu_{C_\Lambda}\) | Gaussian measure | normalized Gaussian measure after absorbing \(S_{\rm kin,\Lambda}\) |
| \(\dd\rho_{\Lambda,S}\) | Euclidean density | unnormalized full density \(\exp(-L_\Lambda)\dd\mu_{C_\Lambda}\) |
| Table `tab:regulator-integration-status-catalog` | regulator-status catalog | classification of finite lattice, finite Fourier, smooth covariance/Wilsonian, spectral/point-splitting, Pauli--Villars auxiliary-field/determinant, dimensional, and subtraction schemes |
| Table `tab:constructive-qft-status-catalog` | status catalog | constructive and triviality regimes |
| \(\zeta_A(s)\) | spectral zeta function | analytic continuation of \(\sum_j\lambda_j^{-s}\) for a positive elliptic operator \(A\) |
| \(\det_\zeta(A/\mu^r)\) | regularized determinant | zeta-regularized determinant of an order-\(r\) positive operator relative to scale \(\mu\) |
| \(A_\omega=-\dd_\tau^2+\omega^2\) | periodic operator | thermal oscillator fluctuation operator on \(S^1_\beta\) |
| \(\zeta_{\rm R}\) | Riemann zeta function | analytic continuation used in the circle Casimir finite part |
| \(\Psi_F\), \(A_F(t)\) | metastable-state datum | finite-volume false-vacuum vector/density matrix and survival amplitude |
| \(q_B\), \(B\), \(M_B\) | bounce data | quartic oscillator bounce profile, action, and fluctuation operator |
| \(\det{}''M_B\) | nonzero-mode determinant | determinant with negative and zero modes separated |
| \(K_B\), \(\Gamma\) | decay coordinates | semiclassical prefactor and real-time width in the exponential window |

## Definition Ledger

- regulated scalar-field path-integral kernel with fixed boundary field
  configurations;
- regulated scalar integration convention
  `def:regulated-scalar-integration-conventions`, distinguishing
  \(D_\Lambda^{\rm ref}\phi\), \(\dd\mu_{C_\Lambda}\), and
  \(\dd\rho_{\Lambda,S}\);
- finite-dimensional regulator class for which Trotter--Kato/Feynman--Kac is
  a theorem;
- Lorentzian oscillatory path-integral notation as finite-regulator
  oscillatory distributions, Fresnel boundary values, or stationary-phase
  asymptotic expansions;
- constructive-QFT status catalog for selected scalar and gauge examples;
- regulator/subtraction classification table distinguishing cutoff measures,
  regulated covariance assignments, operator-insertion regulators,
  Pauli--Villars auxiliary-field or determinant prescriptions, dimensional
  regularization, and subtraction prescriptions;
- spectral zeta function and determinant for positive self-adjoint elliptic
  operators with compact resolvent, zero-mode exclusion, heat-trace
  continuation, and reference scale \(\mu\);
- finite-volume false-vacuum datum: metastable vector/density matrix,
  survival amplitude, exponential time window, and regulator/volume limiting
  prescription;
- field wave functional and field-configuration generalized eigenstate;
- Euclidean scalar action and Euclidean correlation function;
- uniform Wick rotation preserving imaginary-time ordering;
- free Euclidean propagator as the inverse of \(-\partial_E^2+m^2\);
- Feynman \(i\epsilon\) prescription from momentum-contour rotation;
- Wightman, time-ordered, and Euclidean Green functions.

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| The field path-integral kernel is obtained from time-sliced quantum mechanics only after choosing a finite-dimensional Schrödinger spatial regulator satisfying closed-form hypotheses. | Conditional application of prior theorem | Finite-dimensional Schrödinger-regulator paragraph; Chapter 4 theorem applied to \(E_\Lambda\) |
| Field-configuration eigenvectors are represented by functional delta distributions after a finite spatial regulator is imposed. | Framework construction | Direct regulated field-coordinate basis |
| Finite lattice and genuine finite-mode stable polynomial regulators satisfy the finite-dimensional Trotter/Feynman--Kac hypotheses. | Worked regulator classification | Smooth bounded-below potential on \(E_\Lambda\) plus positive kinetic quadratic form |
| Continuum smooth cutoffs that leave infinitely many spatial modes, formal covariance cutoffs, and direct Euclidean spacetime lattice actions without transfer matrices do not inherit the finite-dimensional Trotter theorem. | Framework distinction | Chapter text requires separate Hilbert-space/domain/constructive/perturbative data |
| The formal notation \(Z=\int[D\phi]e^{iS[\phi]}\) has meaning as regulated shorthand or an asymptotic expansion derived from a regulated theory, and does not imply a Borel measure. | Framework statement | Regulator dependence stated explicitly; positive Borel measures restricted to some bosonic Euclidean scalar regimes |
| In a finite-dimensional bosonic scalar regulator, \(D_\Lambda^{\rm ref}\phi\), \(\dd\mu_{C_\Lambda}\), and \(\dd\rho_{\Lambda,S}\) are distinct objects related by explicit Radon--Nikodym factors. | Definition | Definition `def:regulated-scalar-integration-conventions`; equations `eq:gaussian-reference-measure-from-density` and `eq:full-density-reference-versus-gaussian` |
| Pauli--Villars is an auxiliary-field or determinant-ratio prescription, not a measure on the original field space; any path-integral use must specify the enlarged field variables, statistics, masses, coefficients, integration density or cycle, and symmetry action. | Framework distinction | Table `tab:regulator-integration-status-catalog` |
| Dimensional regularization is not a measure on field configurations; it is a formal perturbative meromorphic assignment to graph distributions and their tensor/spinor algebra. | Framework distinction | Table `tab:regulator-integration-status-catalog` |
| A Lorentzian finite-regulator path-integral expression is classified as an oscillatory integral/distribution; the continuum Lorentzian symbol is an oscillatory pseudo-integral specified by compatible finite-regulator boundary values or stationary-phase expansions. | Definition/framework statement | Definition `def:lorentzian-oscillatory-path-integral`; Fresnel formula with signature phase, Maslov-index note, and references to Hörmander and Albeverio--Høegh-Krohn frameworks |
| \(P(\phi)_2\), \(\phi^4_3\), selected low-dimensional superrenormalizable scalar--fermion models, and two-dimensional Yang--Mills are named rigorous construction regimes, while standard scalar \(\phi^4_D\) scaling limits in \(D\ge4\) are constrained by triviality theorems and broad four-dimensional interacting scalar/gauge construction remains open. | Status catalog | Table `tab:constructive-qft-status-catalog` with references paragraph and Open Problem `op:four-dimensional-constructive-qft` |
| Spectral zeta regularization defines a determinant of suitable positive elliptic operators by \(-\zeta_A'(0)-\zeta_A(0)\log\mu^r\), after zero modes are separated. | Definition | Definition `def:spectral-zeta-determinant` |
| The determinant scale change \(\mu\mapsto e^\sigma\mu\) shifts \(\log\det_\zeta(A/\mu^r)\) by \(-r\sigma a_d(A)\) under the stated heat-kernel hypotheses. | Worked calculation | Mellin transform of the heat trace; demoted from proposition wrapper on 2026-05-29 |
| A positive quadratic bosonic fluctuation operator contributes \(\frac12\log\det_\zeta(A/\mu^r)\) to the one-loop effective action, modulo zero modes and vacuum normalization. | Worked calculation | One-loop determinant paragraph; demoted from proposition wrapper on 2026-05-29 |
| For \(A_\omega=-\dd_\tau^2+\omega^2\) on the thermal circle, \(\det_\zeta A_\omega=4\sinh^2(\beta\omega/2)\), giving the canonical oscillator partition function. | Worked example | Example `ex:zeta-thermal-harmonic-oscillator`; calculation check `zeta_determinant_checks.py` |
| The zeta finite part of the massless real scalar circle vacuum energy is \(-\pi/(6L)\) after zero-mode separation. | Worked example | Example `ex:zeta-circle-casimir-energy`; calculation check `zeta_determinant_checks.py` |
| A finite-volume false vacuum is a metastable state or branch with a specified survival amplitude and time window, not an exact decaying eigenvector of a self-adjoint finite-volume Hamiltonian. | Definition/framework statement | Definition `def:finite-volume-false-vacuum-datum` |
| In the quartic scalar oscillator, \(q_B=\omega(2g)^{-1/2}\operatorname{sech}\omega(\tau-\tau_0)\), \(B=\omega^3/(3g)\), \(M_B=-\partial_\tau^2+\omega^2-6\omega^2\operatorname{sech}^2\omega(\tau-\tau_0)\), and \((\det{}''M_B/\det M_F)_{\rm reg}=1/(36\omega^2)\) when the negative and zero modes are separated. | Worked regulated scalar example | Example `ex:quartic-oscillator-false-vacuum-bounce`; calculation check `false_vacuum_decay_checks.py` |
| The negative mode supplies a half-contour factor \(\pm i/2\), while the translation zero mode gives \((B/2\pi)^{1/2}\dd\tau_0\); neither is part of an ordinary positive determinant. | Worked contour and collective-coordinate calculation | Equations `eq:false-vacuum-negative-mode-half-gaussian` and `eq:false-vacuum-translation-zero-mode-jacobian`; calculation check `false_vacuum_decay_checks.py` |
| Dilute multi-bounce exponentiation gives a complex resonance energy and a real-time width only after the state, contour, separation, and residual assumptions are supplied. | Controlled semiclassical framework | Equations `eq:false-vacuum-dilute-bounce-exponentiation` and `eq:false-vacuum-real-time-width`; calculation check `false_vacuum_decay_checks.py` |
| Euclidean ordering of insertion times gives analytic continuation to time-ordered Lorentzian correlators under spectral/analytic assumptions. | Framework statement with derivation in free case | Complex-time contour and uniform Wick rotation |
| Euclidean field-insertion notation records the boundary value \(x^0=-i\tau\) inside ordered correlation functions. | Definition | Analytic-continuation convention |
| The free Euclidean two-point function is the Green function of \(-\partial_E^2+m^2\). | Derived | Gaussian functional integral |
| Rotating the Euclidean momentum contour gives the Feynman denominator \(k^2+m^2-i\epsilon\). | Worked free-theory derivation | Pole tracking; demoted from proposition wrapper on 2026-05-29 |
| Wightman, time-ordered, and Euclidean Green functions are distinct distributions related by ordering and analytic continuation. | Definition plus framework statement | Explicit definitions |

## Figure Ledger

Figures to include:

- complex-time contour with insertion ordering;
- uniform Wick rotation from Euclidean insertions to ordered Lorentzian times;
- pole motion in the complex \(k^0\)-plane that records the \(i\epsilon\)
  prescription.

Rendered check:

- physical PDF pages 79--84 (`/tmp/qft_ch11_scalar_path_audit-079.png`
  through `/tmp/qft_ch11_scalar_path_audit-084.png`) were inspected after
  rebuild; the three TeX figures are legible and the revised pole figure
  displays both the real contour and the displaced poles.

## Audit Targets

- Keep all path-integral formulas marked as regulated constructions or formal
  expressions until a regulator is specified.
- Do not invoke Chapter 4's Trotter/Feynman--Kac theorem for a field-theory
  regulator unless the regulator produces a finite-dimensional Schrödinger
  Hamiltonian with a closed semibounded form.
- Do not say the Euclidean functional expression is positive in all theories.
- Do not introduce perturbative graph expansion in this chapter.
- Do not use scattering language.
- Preserve the transition into the Kallen-Lehmann chapter.
- Keep false-vacuum decay tied to state, contour, determinant, zero-mode,
  dilute-gas, and real-time interpretation data; do not reduce it to a bounce
  equation or a potential sketch.

## Audit Notes

- 2026-05-24, issue #299: added the finite-dimensional Schrödinger-regulator
  criterion separating finite lattice/finite-mode Schrödinger regulators from
  continuum smooth cutoffs, covariance cutoffs, direct Euclidean spacetime
  lattice actions without transfer matrices, and formal perturbative cutoffs.
- 2026-05-29 anti-wrapper pass: retitled
  the finite-dimensional Schrödinger-regulator criterion in positive language;
  demoted it on the later proof-status pass from proposition to framework
  paragraph because the mathematical work is the Chapter 4 Trotter--Kato
  theorem.  The same pass demoted the zeta determinant scale-dependence
  calculation and free Feynman boundary-value pole tracking to worked
  paragraphs.
- 2026-05-24, issue #300: added
  `tab:constructive-qft-status-catalog`, a named catalog of constructive
  scalar/gauge models, scalar triviality regimes, and the open four-dimensional
  Yang--Mills continuum problem.
- 2026-05-24, issue #333: expanded the catalog with selected
  low-dimensional superrenormalizable scalar--fermion constructions and an
  explicit four-dimensional interacting local-QFT row, linked conceptually to
  Open Problem `op:four-dimensional-constructive-qft` in the opening chapter.
- 2026-05-24, issue #301: added
  `def:lorentzian-oscillatory-path-integral`, classifying the Lorentzian
  finite-regulator object as an oscillatory integral/distribution and the
  continuum notation as an oscillatory pseudo-integral; also scoped the
  Glimm--Jaffe functional-integral reference to the positive-measure scalar
  sector.
- 2026-05-24, issue #310: added
  `def:regulated-scalar-integration-conventions`, fixing the canonical
  finite-regulator scalar notation.  Later chapters now write
  \(D_\Lambda^{\rm ref}\phi\) for the reference density,
  \(\dd\mu_{C_\Lambda}\) for the Gaussian measure, and
  \(\dd\rho_{\Lambda,S}\) for the full Euclidean density.
- 2026-05-24, issue #313: added
  `tab:regulator-integration-status-catalog`, classifying the regulator and
  subtraction schemes used later and explicitly excluding dimensional
  regularization from the class of path-integral measures.
- 2026-05-24, issue #314: added Pauli--Villars to the regulator catalog as an
  auxiliary-field/determinant prescription, not a measure on the original
  field space.
- 2026-05-25, issue #478: added spectral zeta determinants as a regulated
  determinant prescription for suitable positive elliptic operators, including
  the one-loop quadratic-fluctuation formula, the thermal oscillator
  determinant, and the circle Casimir finite part; added
  `calculation-checks/zeta_determinant_checks.py`.
- 2026-06-04, issue #788: added the false-vacuum decay contour construction.
  The pass develops a regulated scalar oscillator example from metastable
  state through negative-mode contour, determinant/zero-mode separation,
  dilute exponentiation, and real-time width, and registers
  `calculation-checks/false_vacuum_decay_checks.py` as a high-risk evidence
  contract.  This is physics-depth infrastructure for Higgs metastability and
  instanton/tunneling discussions, not a moduli-space mathematics addition.
