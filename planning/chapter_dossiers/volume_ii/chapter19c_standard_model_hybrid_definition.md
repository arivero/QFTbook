# Volume II Chapter: Standard Model Hybrid Definition

## Scope

- Compiled in Volume II after QCD, jets, and anomaly technology are available.
- Addresses GitHub issue #486.
- Gives a reader-facing Standard Model chapter whose central object is the
  hybrid datum: lattice/nonperturbative QCD sector, electroweak finite-cutoff
  EFT, low-energy weak EFTs, and matching maps.

## Definitions and Symbols

- Defines the local gauge group, global-form caveat, hypercharge convention,
  one-generation left-handed Weyl representation, Higgs doublet, Yukawa
  tensors, and CKM/PMNS placement.
- Computes the central \(\mathbb Z_6\) kernel of the minimal representation
  content using integer hypercharge \(y=6Y\), and records the four allowed
  quotients by subgroups \(1,\mathbb Z_2,\mathbb Z_3,\mathbb Z_6\).
- Reminds the reader of the monograph's trace-delta Yang--Mills convention and
  states the explicit electroweak coupling-coordinate conversion used for mass
  formulae.
- Defines quark mass coordinates by singular-value decompositions of
  \(M_u=vY_u/\sqrt2\) and \(M_d=vY_d/\sqrt2\), derives
  \(V_{\rm CKM}=(U_L^u)^\dagger U_L^d\), proves the quark flavor parameter
  count, proves tree-level GIM diagonality of neutral currents, and records
  the Jarlskog rephasing invariant.
- Derives \(SU(2)_L\times U(1)_Y\to U(1)_{\rm em}\), \(m_W\), \(m_Z\),
  the photon, and the weak mixing angle from the Higgs kinetic term.
- Derives \(m_h^2=2\lambda v^2\), the radial potential coefficients, the
  custodial \(SU(2)_L\times SU(2)_R\to SU(2)_V\) structure of the scalar
  sector, and \(\rho_{\rm tree}=1\).
- Displays local gauge-anomaly cancellation:
  \(SU(3)^2U(1)_Y\), \(SU(2)^2U(1)_Y\), \(U(1)_Y^3\), mixed
  gravitational-\(U(1)_Y\), and the finite \(SU(2)\) doublet-parity check.
- Defines the left-handed-convention \(B\), \(L\), and \(B-L\) charges,
  computes \(SU(2)_L^2B\), \(SU(2)_L^2L\), \(SU(3)^2(B-L)\), and the
  gravitational/cubic \(B-L\) anomalies, including the precise role of a
  singlet \(\nu^c\).
- Defines the SMEFT source chart as a scheme-dependent coordinate chart on
  local operators, derives the Weinberg-operator neutrino mass normalization,
  and gives the tree-level singlet-neutrino matching coordinate
  \(C_5/\Lambda=Y_\nu M^{-1}Y_\nu^T\).
- Defines the invariant strong-CP coordinate
  \(\overline\theta=\theta_3+\arg\det(M_uM_d)\) with the massless-quark caveat.
- Derives the one-loop gauge beta coefficients
  \(b_1=41/6\), \(b_2=-19/6\), \(b_3=-7\) in the unrescaled
  \(Q=T^3+Y\) hypercharge convention, records the GUT-rescaled conversion,
  and states the invariant one-loop top-Higgs subsystem for
  \((y_t,\lambda)\).
- Defines the precision electroweak \(S,T,U\) self-energy coordinates from
  renormalized transverse two-point functions after fixing the input scheme,
  and derives the relation between \(T\) and the first-order shift of the
  \(\rho\)-coordinate.
- Expands the hybrid matching datum \(\mathcal M\) into scales, parameter
  charts, threshold maps, anomalous dimensions, nonperturbative matrix
  elements, and error/remainder data.
- Defines a Standard Model prediction in the hybrid framework by specifying
  regime, regulator/EFT, operator, matching map, error class, and
  gauge/infrared requirements.
- Derives the tree-level Fermi-theory matching
  \(G_F/\sqrt2=1/(2v^2)\).
- Defines the muon \(g-2\) Pauli-coordinate observable as a low-energy
  hybrid prediction, derives the Schwinger term from the QED form-factor
  chapter, records the leading electroweak Pauli coefficient, and defines HVP
  and HLbL as functionals of gauge-invariant QCD electromagnetic current
  correlators.
- States the constructive Standard Model open problem.

## Figure Ledger

- No figures were added in this pass.  The chapter is algebraic and
  framework-definitional; later electroweak/global-form passes may add a
  gauge-group/global-form diagram or an EFT-matching flow diagram if it carries
  mathematical content rather than decoration.

## Calculation Checks

- `calculation-checks/standard_model_anomaly_checks.py` verifies the finite
  hypercharge anomaly sums, the even number of weak doublets, electric
  charges from \(Q=T^3+Y\), the \(\mathbb Z_6\) kernel generator, CKM
  parameter counts, Jarlskog rephasing cancellation, \(m_h^2=2\lambda v^2\),
  \(\rho_{\rm tree}=1\), \(B-L\) anomaly bookkeeping, Weinberg-operator
  mass normalization, singlet-neutrino tree matching, and strong-CP phase
  invariance, one-loop gauge beta coefficients, GUT hypercharge conversion,
  top-Higgs subsystem coefficient algebra, and elementary \(S,T,U\)
  source-chart identities, plus the muon \(g-2\) Schwinger coefficient,
  leading electroweak coefficient normalization, and HVP kernel algebra.

## Claim Ledger

1. The local SM representation content is defined in a left-handed Weyl basis.
2. The central \(\mathbb Z_6\) quotient is computed from the actual minimal
   field representations, not assumed from the Lie algebra.
3. CKM mixing is the mismatch of left singular-vector coordinates in the
   quark Yukawa sector; the neutral currents are tree-level flavor diagonal
   by unitarity in generation space.
4. The electroweak mass formulas follow from the Higgs kinetic term evaluated
   at \(H_0=(0,v/\sqrt2)^T\).
5. The Higgs radial mass and tree-level \(\rho\)-identity are coordinate
   identities in the finite-cutoff electroweak EFT.
6. Local and finite weak anomalies cancel generation by generation.
7. \(B+L\) is anomalous in the electroweak sector, while \(B-L\) has the
   stated mixed-gauge cancellations and requires \(\nu^c\) for cubic and
   gravitational anomaly cancellation if gauged.
8. The Weinberg operator and singlet-neutrino matching are EFT coordinate
   statements with declared normalization, not assumptions about the minimal
   datum.
9. \(\overline\theta\) is the invariant QCD theta/mass-phase coordinate;
   its empirical smallness is a parameter statement, not a selection
   principle.
10. The RG equations are source-chart equations in dimensional
   regularization/minimal subtraction; they do not assert a nonperturbative
   electroweak continuum construction or provide an ultraviolet-selection
   principle.
11. The \(S,T,U\) variables are finite coordinates on the two-point
   electroweak source chart under analyticity and input-scheme assumptions;
   they do not replace vertex, box, four-fermion, or detector-function data.
12. The Standard Model is used as a hybrid operational object, not as an
   assumed complete constructive four-dimensional continuum theorem.
13. The Fermi operator coefficient is a tree-level matched EFT coefficient;
   QCD matrix elements and radiative corrections are separate matching data.
14. The muon \(g-2\) number is a Pauli-form-factor coordinate produced by a
   declared hybrid computation; HVP and HLbL are QCD current-correlator
   inputs, not perturbative QCD expansions.

## Audit Notes

- Keep the physical electroweak explicit-coupling convention visibly separated
  from the monograph trace-delta Yang--Mills convention.
- Do not describe the electroweak sector as a standalone nonperturbatively
  complete four-dimensional QFT.
- Keep chiral-lattice and hypercharge-triviality caveats conditional and
  theorem-status accurate.
