# Volume I, Chapter 7 Dossier: Symmetries, Noether Currents, and Stress Tensors

## Status

Current status: ready for TeX rewrite.

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

## Claim Ledger

| Claim | Status | Certification |
| --- | --- | --- |
| The variation of a first-derivative action decomposes into Euler-Lagrange terms plus a total divergence. | Derived | Direct integration by parts |
| If \(\delta_R\mathcal L=\partial_\mu K^\mu_R\), then \(j^\mu_R=\partial\mathcal L/\partial(\partial_\mu\phi^A)R^A-K^\mu_R\) is conserved on shell. | Derived | Variation identity |
| The integral \(Q_R(t)=\int j^0_R\) is time independent when the current is conserved and boundary flux vanishes. | Derived | Divergence theorem on a time slab |
| In canonical phase space, a charge generates the associated transformation when \(\delta F=\{F,Q\}\) and the required functional derivatives exist. | Derived in standard cases; framework statement generally | Direct computation for first-order internal transformations and translations |
| The free scalar stress tensor gives \(T^{00}=\mathcal H\). | Derived | Substitution of the scalar Lagrangian |
| Lorentz-current conservation follows from stress-tensor conservation and symmetry. | Derived | Antisymmetry of Lorentz parameter |
| In quantum theory, local currents and stress tensors must be defined as renormalized operator-valued distributions in the chosen framework. | Framework statement | Local operator construction, not an automatic consequence of Poincare invariance alone |

## Figure Ledger

Included figure:

- a time-slab diagram showing that charge conservation is flux conservation
  through the boundary of a spacetime region.

## Audit Targets

- Do not state that every QFT automatically has a local stress tensor.
- Keep the sign distinction between fixed-coordinate Noether variations and
  translation covariance explicit.
- State all boundary and compact-support assumptions before using conserved
  charges.
- Do not turn anomaly or gauge subtleties into main-text negative framing; only
  mention them as framework qualifications when necessary.
