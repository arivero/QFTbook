# Chapter 10: Bridges To Nonintegrable Two-Dimensional QFT And CFT

## Source Position

Volume VI closes its initial integrable-QFT spine by explaining how exact
integrable data can be used as coordinates near nonintegrable deformations
and near two-dimensional CFT perturbations.

## Notation Inventory

- `Q_0`, `A_0`, `H_0`, `Q_s`: integrable QFT, operator algebra, Hamiltonian,
  and higher conserved charges.
- `O_b`, `epsilon`: integrability-breaking local operator and coupling.
- `H(epsilon,L,Lambda)`: finite-volume cutoff Hamiltonian with local
  coordinate counterterms.
- `B_s`: local operator measuring violation of the `s`-charge conservation
  law.
- `M_beta alpha`, `Gamma_A`: first-order transition matrix element and
  second-order decay width.
- `Gamma_A^lead(C)`, `R_weak`, `R_L`, `R_BY`, `R_ff`, `R_chan`,
  `R_th`, `R_epsilon3`: retained connected-form-factor decay-width coordinate
  and the residuals separating it from a physical continuum rate.
- `M_Gamma`, `kappa_Gamma`: absolute phase-space/form-factor majorant and
  noncancellation margin for relative rate statements.
- `lambda(x,y,z)`, `p_*`: Kallen polynomial and relative momentum for the
  two-particle \(1+1\)-dimensional decay-width formula.
- `E_cut`: truncated conformal-space cutoff.

## Claim Ledger

- Defines an integrability-breaking deformation as a regulated Hamiltonian
  datum with local coordinates.
- Derives the first-order breaking of higher-charge conservation.
- Derives the translation-covariant form-factor expression for transition
  matrix elements.
- Derives the finite-volume route to a decay width by a weak spectral-measure
  limit: the \(T\to\infty\) golden-rule kernel is applied only after the
  finite-volume spectral sums converge to an absolutely continuous
  infinite-volume rapidity measure, avoiding the false pointwise
  \(T\to\infty\) limit at fixed \(L\).
- Adds a decay-rate reconstruction certificate: the retained connected
  form-factor width is separated from weak-kernel, finite-volume,
  Bethe--Yang normalization, form-factor-boundary, channel-tail,
  threshold/window, and higher-order/counterterm residuals before it is
  identified with a physical nonintegrable decay or damping rate.
- Evaluates the two-particle \(1+1\)-dimensional phase-space integral from
  the rapidity measure, including the Jacobian, threshold condition, and
  identical-particle counting convention.
- Identifies the CFT-deformation Hamiltonian coordinates needed to interface
  with form-factor perturbation theory, while sending the detailed TCSA
  regulator machinery and counterterm-power derivations to the general
  Hamiltonian-truncation chapter in Volume XI unless this chapter later
  extracts a concrete nonintegrable finite-volume spectrum.

## Calculation Checks

- `calculation-checks/nonintegrable_bridge_checks.py` verifies the broken
  higher-charge commutator ledger, first-order form-factor mass shift,
  semi-local kinematic residue, Ising false-vacuum string tension,
  two-particle \(1+1\)-dimensional phase-space Jacobian, TCSA coupling and
  counterterm powers, the finite residual telescope for the decay-rate
  reconstruction certificate, negative controls against finite-box and exact
  form-factor overread, omitted threshold residuals, and signed cancellations,
  and the Airy scaling of confined kink--antikink bound states.

## Figure Ledger

No figure is included in this pass.  Future figures should include charge
breaking, finite-volume level crossings, and integrable-to-nonintegrable
deformation diagrams.

## Placement Audit

- 2026-05-30 general-method exposure pass: removed the local TCSA regulator
  definition and OPE counterterm-power derivation from this specialized bridge
  chapter.  The chapter now keeps only the CFT-deformation Hamiltonian
  coordinate chart and states that detailed TCSA machinery belongs in
  Volume XI until an actual nonintegrable spectrum is extracted here.
- 2026-06-02 issue #561 dossier-link pass: recorded the already-existing
  nonintegrable-bridge calculation check explicitly in the chapter dossier.
  No new formula was changed in the manuscript.
- 2026-06-04 issue #728 decay-rate reconstruction pass: added
  `ca:nonintegrable-decay-rate-reconstruction-certificate`, making the
  transition from integrable form-factor data to a physical nonintegrable rate
  depend on weak-kernel, finite-volume, Bethe--Yang, form-factor-boundary,
  channel-tail, threshold, and higher-order residual control.  The companion
  check now carries an evidence contract and exact negative controls for
  finite-box overread, exact-form-factor overread, omitted threshold budgets,
  and signed cancellation.
