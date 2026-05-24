# Volume I, Chapter 7 Dossier: Symmetries, Noether Currents, and Stress Tensors

## Status

Current status: source-block certified against 253a pp. 63--71 on
2026-05-22. The chapter has been rebuilt and visually audited in the rendered
PDF after adding the local-parameter current derivation, the explicit
canonical-generator check, the finite Poincare scalar transformation, and the
localized-translation stress-tensor derivation.

## Logical Role

This chapter follows the canonical free scalar construction. Its role is to
identify the local currents and charges attached to continuous symmetries of a
classical Lagrangian field theory, then state the corresponding quantum
operator interpretation with domain and renormalization qualifications.

The chapter does not introduce scattering, LSZ, or perturbative S-matrix
diagrams. It remains within local fields, canonical phase space, and conserved
currents.

## Primary Source Anchors

- `transcription/tex/253a/foundations.tex`, section "Symmetries and Noether's
  Theorem", including the translation-current and stress-energy tensor
  subsection.
- Source visual trace:
  `monograph/tex/build/source_visual_trace/253a_trace-063.png` through
  `monograph/tex/build/source_visual_trace/253a_trace-071.png`.
- Rendered audit:
  `planning/build_audits/2026-05-22_noether_stress_tensor_source_figures.md`.
- `references/253a_notes.tex`, corresponding section "Noether's Theorem and
  Conserved Currents", used only as a comparison layer.
- `monograph/tex/volumes/volume_i/chapter06_relativistic_scalar_fields_and_canonical_quantization.tex`,
  for the Poisson bracket convention, the Hamiltonian density, and the free
  scalar field normalization.
- `monograph/tex/volumes/volume_i/chapter03_local_field_operators_poincare_covariance_and_microcausality.tex`,
  for the quantum Poincare covariance convention.

## External Reference Boundary

- Harlow--Wu, "Covariant phase space with boundaries", arXiv:1906.08616,
  sections 2 and 4.2, is used only to locate the general theorem-level
  boundary: in theories with boundaries or nontrivial asymptotics, charges and
  Hamiltonians require precise boundary conditions and symplectic data. The
  chapter reproduces only the elementary first-derivative, compact-support
  derivation in flat spacetime.

## Framework

Working framework:

- \(D\)-dimensional Minkowski spacetime \(\mathbb M^D\) with mostly-plus
  metric \(\eta\);
- a finite set of bosonic classical fields \(\phi^A\), indexed by \(A\);
- a first-derivative local Lagrangian density
  \(\mathcal L(\phi,\partial_\mu\phi)\);
- compactly supported variations unless a boundary condition is explicitly
  stated;
- equal-time canonical phase space with fields \(\phi^A(t,\vec x)\) and
  conjugate momenta \(\Pi_A(t,\vec x)\);
- quantum fields understood as operator-valued distributions on a common dense
  invariant domain when current operators are discussed.
- quantum Ward identities in correlators understood as source-functional
  distributional identities after a regulator, integration density, and
  contact-term chart have been specified.

## Notation Inventory

| Symbol | Type | Meaning |
| --- | --- | --- |
| \(A,B\) | finite indices | field component labels |
| \(\phi^A\) | classical field | component of a bosonic field multiplet |
| \(\Pi_A\) | canonical density | momentum conjugate to \(\phi^A\) |
| \(E_A(\mathcal L)\) | local expression | Euler-Lagrange derivative of \(\mathcal L\) |
| \(R^A[\phi]\) | local expression | infinitesimal field variation for a one-parameter symmetry |
| \(K^\mu_R\) | local vector density | total-derivative term in \(\delta_R\mathcal L=\partial_\mu K^\mu_R\) |
| \(j^\mu_R\) | current | Noether current for \(R\) |
| \(Q_R(t)\) | charge | integral of \(j^0_R\) over a time slice |
| \(\xi^\mu\) | vector parameter | infinitesimal spacetime translation parameter |
| \(T^\mu{}_\nu\) | tensor density | stress tensor with one index lowered |
| \(P_\nu,P^\nu\) | charges | translation generators, related by \(P^\nu=\eta^{\nu\rho}P_\rho\) |
| \(J^{\mu\nu}\) | charges | Lorentz generators for symmetric stress tensor |

## Definition Ledger

- first-derivative Euler-Lagrange derivative;
- infinitesimal variational symmetry of an action;
- Noether current with explicit boundary-term dependence;
- conserved charge on a fixed time slice;
- canonical generator convention \(\delta F=\{F,Q\}\);
- translation stress tensor \(T^\mu{}_\nu\);
- Hilbert stress tensor when a background-metric extension exists;
- Lorentz current and Lorentz charge for scalar fields;
- quantum current and charge as operator-valued distributions with regulator
  and domain status declared.
- regulated quantum Noether Ward identity with insertion contact terms and a
  possible local density/counterterm variation
  \(\mathcal A_{\epsilon,R}\).

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| The variation of a first-derivative action decomposes into Euler-Lagrange terms plus a total divergence. | Derived | Direct integration by parts |
| If \(\delta_R\mathcal L=\partial_\mu K^\mu_R\), then \(j^\mu_R=\partial\mathcal L/\partial(\partial_\mu\phi^A)R^A-K^\mu_R\) is conserved on shell. | Derived | Variation identity |
| The same current is the coefficient of \(\partial_\mu\epsilon\) when a constant symmetry parameter is localized to a compactly supported \(\epsilon(x)\). | Derived | Local-parameter variation with the constant-parameter total derivative separated |
| The integral \(Q_R(t)=\int j^0_R\) is time independent when the current is conserved and boundary flux vanishes. | Derived | Divergence theorem on a time slab |
| In canonical phase space, a charge generates the associated transformation when \(\delta F=\{F,Q\}\) and the required functional derivatives exist. | Derived in standard cases; framework statement generally | Direct computation for first-order internal transformations and the time-translation charge \(Q=-\tau H\) |
| For a scalar field, the finite Poincare law \(\phi'(x')=\phi(x)\) gives fixed-coordinate infinitesimal variation \(-\left(a^\mu+\omega^\mu{}_\nu x^\nu\right)\partial_\mu\phi\). | Derived | First-order expansion of \(x'=\Lambda x+a\) |
| The stress tensor \(T^\mu{}_\nu\) is the coefficient of \(\partial_\mu\xi^\nu\) in a compactly supported localized translation. | Derived | Localized translation variation after the total derivative is separated |
| The free scalar stress tensor gives \(T^{00}=\mathcal H\). | Derived | Substitution of the scalar Lagrangian |
| Lorentz-current conservation follows from stress-tensor conservation and symmetry. | Derived | Antisymmetry of Lorentz parameter |
| In quantum theory, local currents and stress tensors must be defined as renormalized operator-valued distributions in the chosen framework. | Framework statement | Local operator construction, not an automatic consequence of Poincare invariance alone |
| Quantum Noether identities in correlation functions include insertion contact terms and possible local terms from the regulated integration density and source-chart counterterms. | Framework statement | Equation `eq:quantum-noether-ward-regulated`; cross-reference to CFT source-functional Ward identities |

## Figure Ledger

Included figure:

- a time-slab diagram showing that charge conservation is flux conservation
  through the boundary of a spacetime region.

Rendered check:

- physical PDF pages 72--78 (`/tmp/qft_ch10_noether_audit-072.png` through
  `/tmp/qft_ch10_noether_audit-078.png`) were inspected after rebuild; the
  time-slab figure is legible and the added derivations fit without visual
  crowding.

## Audit Targets

- Do not state that every QFT automatically has a local stress tensor.
- Keep the sign distinction between fixed-coordinate Noether variations and
  translation covariance explicit.
- State all boundary and compact-support assumptions before using conserved
  charges.
- Do not turn anomaly or gauge subtleties into main-text negative framing; only
  mention them as framework qualifications when necessary.

## Audit Notes

- 2026-05-24 issue #307 pass: added the regulated quantum Noether Ward
  identity `eq:quantum-noether-ward-regulated`, connecting the classical
  localized-parameter identity to source-functional Ward identities with
  insertion contact terms and possible local density/counterterm variation;
  cross-referenced the CFT source-functional contact-term chart in Volume V.
