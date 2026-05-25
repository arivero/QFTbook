# Volume IV Chapter: Standard Model Hybrid Definition

## Scope

- Compiled in Volume IV after QCD, jets, and anomaly technology are available.
- Addresses GitHub issue #486.
- Gives a reader-facing Standard Model chapter whose central object is the
  hybrid datum: lattice/nonperturbative QCD sector, electroweak finite-cutoff
  EFT, low-energy weak EFTs, and matching maps.

## Definitions and Symbols

- Defines the local gauge group, global-form caveat, hypercharge convention,
  one-generation left-handed Weyl representation, Higgs doublet, Yukawa
  tensors, and CKM/PMNS placement.
- Reminds the reader of the monograph's trace-delta Yang--Mills convention and
  states the explicit electroweak coupling-coordinate conversion used for mass
  formulae.
- Derives \(SU(2)_L\times U(1)_Y\to U(1)_{\rm em}\), \(m_W\), \(m_Z\),
  the photon, and the weak mixing angle from the Higgs kinetic term.
- Displays local gauge-anomaly cancellation:
  \(SU(3)^2U(1)_Y\), \(SU(2)^2U(1)_Y\), \(U(1)_Y^3\), mixed
  gravitational-\(U(1)_Y\), and the finite \(SU(2)\) doublet-parity check.
- Defines a Standard Model prediction in the hybrid framework by specifying
  regime, regulator/EFT, operator, matching map, error class, and
  gauge/infrared requirements.
- Derives the tree-level Fermi-theory matching
  \(G_F/\sqrt2=1/(2v^2)\).
- States the constructive Standard Model open problem.

## Figure Ledger

- No figures were added in this pass.  The chapter is algebraic and
  framework-definitional; later electroweak/global-form passes may add a
  gauge-group/global-form diagram or an EFT-matching flow diagram if it carries
  mathematical content rather than decoration.

## Calculation Checks

- `calculation-checks/standard_model_anomaly_checks.py` verifies the finite
  hypercharge anomaly sums, the even number of weak doublets, and the
  electric charges from \(Q=T^3+Y\).

## Claim Ledger

1. The local SM representation content is defined in a left-handed Weyl basis.
2. The electroweak mass formulas follow from the Higgs kinetic term evaluated
   at \(H_0=(0,v/\sqrt2)^T\).
3. Local and finite weak anomalies cancel generation by generation.
4. The Standard Model is used as a hybrid operational object, not as an
   assumed complete constructive four-dimensional continuum theorem.
5. The Fermi operator coefficient is a tree-level matched EFT coefficient;
   QCD matrix elements and radiative corrections are separate matching data.

## Audit Notes

- Keep the physical electroweak explicit-coupling convention visibly separated
  from the monograph trace-delta Yang--Mills convention.
- Do not describe the electroweak sector as a standalone nonperturbatively
  complete four-dimensional QFT.
- Keep chiral-lattice and hypercharge-triviality caveats conditional and
  theorem-status accurate.
