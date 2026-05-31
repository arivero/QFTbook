# Chapter 09: Two-Dimensional Supersymmetric Models

## Source Position

Volume VII now leaves the four-dimensional gauge-dynamics core and begins the
lower-dimensional supersymmetric examples with `2D` `N=(2,2)` theories.
The LG/GLSM and mirror-duality material uses Xi's stringbook Appendix K as an
internal source lead and convention comparator.  It is rewritten here as an
intrinsic two-dimensional QFT development, with the charged-chiral
dualization, one-loop matching, vortex-term proof boundary, and
cigar/Liouville comparison made more explicit than the stringbook appendix.
Primary reference sidecars currently used for scrutiny, not authority, are
`references/susy_glsm_mirror/hori_vafa_mirror_symmetry_hep-th_0002222.txt`
and
`references/susy_glsm_mirror/hori_kapustin_cigar_liouville_hep-th_0104202.txt`.

## Notation Inventory

- `Q_pm`, `bar Q_pm`, `P_pm`: two-dimensional supersymmetry generators and
  light-cone momenta.
- `F_V`, `F_A`: vector and axial `R` charges.
- `s`, `s_A`, `s_B`: untwisted, A-twisted, and B-twisted Lorentz spins.
- `Q_A`, `Q_B`: scalar supercharges after the A and B twists.
- `Phi^i=(phi^i, psi^i_+, psi^i_-, F^i)`, `K`, `g_i bar j`, `W`:
  Landau-Ginzburg chiral multiplet variables, Kahler potential, metric, and
  superpotential.
- `q_i`: quasihomogeneous Landau-Ginzburg weights.
- `g_i`: background chiral Wilsonian couplings for Fermat
  Landau-Ginzburg monomials `g_i (Phi^i)^{d_i}`.
- `Jac(W)`: Landau-Ginzburg Jacobian ring.
- `chi_y`: finite protected Ramond charge polynomial coordinated with the
  Volume V elliptic-genus interface.
- `eta_i`: B-type odd local variables used in the cohomological derivation
  of the Jacobian quotient.
- `H_W`, `Res_W`: Landau-Ginzburg Hessian determinant and Morse residue
  functional.
- `X`, `g_i bar j`, `B`, `omega`, `chi^a`: sigma-model target, Kahler
  metric, `B`-field, Kahler form, and A-model odd zero modes.
- `vartheta`, `tilde vartheta`, `R`, `A`: compact scalar, dual compact
  scalar, radius, and first-order abelian duality one-form.
- `mathcal B`, `Y`, `u=Y+bar Y`, `K`, `tilde K`: local real superfield,
  twisted-chiral dual variable, real Legendre coordinate, original Kahler
  potential, and dual Kahler potential in abelian `N=(2,2)` duality.
- `G`, `V`, `r`, `Q_i`, `t`, `sigma`: GLSM gauge group, matter
  representation, Fayet-Iliopoulos coordinate, charges, complexified
  FI-theta coordinate, and vector-multiplet scalar.
- `Sigma`, `tilde W_eff`, `mu`, `Q_tot`: twisted chiral field strength,
  abelian Coulomb-branch effective twisted superpotential, renormalization
  scale, and total positive charge in the one-loop Coulomb ledger.
- `Y_i`, `B_i`, `U_i`, `M_i(Sigma)`, `c_i`, `X_i`: charged-chiral dual
  twisted variables, first-order real superfields, real dual coordinates,
  charge-linear Coulomb masses, vortex-normalization constants, and
  exponential torus coordinates in the abelian mirror presentation.
- `Y_P`, `rho`, `vartheta`, `u`, `chi`, `k`: logarithmic-chiral dual
  variable, polar coordinate for the charged chiral scalar, angular
  coordinate, real and periodic parts of `P`, and cigar level parameter.
- `X_i`, `P`, `G_d`, `d`, `mu_d`: hypersurface GLSM fields, homogeneous
  polynomial, degree, and residual finite gauge group.
- `H`, `Y_G`, `C_branch`, `T`: hyperplane Chern class on projective space,
  smooth hypersurface target in the positive chamber, branch-dependent
  Coulomb constant for the anomaly-free hypersurface charge vector, and the
  shifted additive FI coordinate.

## Claim Ledger

- Defines the `N=(2,2)` supersymmetry algebra and BPS positivity input.
- Defines polynomial Landau-Ginzburg data as field-variable presentations,
  including component variables, Kahler metric, and superpotential.
- Derives the auxiliary-field potential and identifies classical vacua as the
  critical locus of `W`.
- Defines quasihomogeneous isolated Landau-Ginzburg data and the Jacobi
  algebra.
- Proves that the B-type local differential with
  `Q_B eta_i = partial_i W` gives degree-zero polynomial cohomology
  `Jac(W)`.
- Proves the quasihomogeneous charge ledger, Fermat Jacobi basis, Fermat
  Jacobi dimension, and protected central-charge test, while marking the
  infrared fixed-point existence claim as a separate construction problem.
- Adds the Fermat Wilsonian superpotential coordinate argument: under a
  declared chiral Wilsonian scheme, regularity at `g_i=0`, flavor spurion
  symmetries, and `R(W)=1`, the only regular holomorphic monomials in the
  superpotential are the original `g_i (Phi^i)^{d_i}` terms.  This is a
  coordinate-level nonrenormalization statement, not an infrared existence
  theorem.
- Adds the coordination bridge to Volume V: if the infrared SCFT exists and
  `Jac(W)` classes become NS chiral primaries, then spectral flow by
  `eta=-1/2` shifts a monomial charge to the left Ramond charge
  `Q_R-c_LG/6`, giving the finite `chi_y` protected polynomial required by
  the elliptic-genus interface.
- Defines sigma-model and GLSM data and separates protected coordinates from
  full infrared QFT equivalence.
- Defines the A/B twist spin-shift convention and proves that
  `Q_A = bar Q_+ + Q_-` and `Q_B = bar Q_+ + bar Q_-` are scalar nilpotent
  supercharges in the central-charge-free local sector.
- States the anomaly requirements for the vector and axial `R` symmetries
  and identifies the axial GLSM obstruction as the charge sum.
- Proves that the Morse residue functional descends to `Jac(W)` and gives a
  nondegenerate pairing when the critical points of `W` are nondegenerate.
- Records the genus-`g` B-twisted LG zero-mode formula with its determinant
  and regulator status boundary.
- Proves that the constant-map A-model zero-mode algebra is the de Rham
  complex of the target.
- States the A-model holomorphic-map energy decomposition and names the
  compactification/orientation/contact-term inputs required for genuine
  correlation functions.
- Defines abelian duality as an intrinsic two-dimensional QFT operation,
  not a string-theoretic mirror-symmetry argument.
- States the compact scalar first-order duality hypotheses, including
  winding sectors, integral-period normalization, Gaussian contour, and
  determinant normalization.
- Proves the local compact-scalar radius inversion `R -> R^{-1}` from the
  first-order Gaussian path integral and records the momentum-winding
  spectrum test.
- Defines the local `N=(2,2)` chiral/twisted-chiral Legendre-transform
  duality datum and proves the Hessian inversion `tilde K'' = 1/K''`.
- Records the GLSM charged-chiral dualization ledger and marks
  nonperturbative exponential twisted-superpotential terms as requiring a
  separate vortex-instanton compactness/zero-mode/determinant proof.
- Derives the first-order charged-chiral dualization with real superfield
  `B_i`, twisted-linear constraint, Legendre elimination, and the
  superspace integration-by-parts identity producing the linear
  `-Q_i^a Sigma_a Y_i` twisted `F`-term.
- Defines the dual mass linear form `M_i(Sigma)=sum_a Q_i^a Sigma_a` and the
  protected dual twisted-superpotential datum with exponential
  `-mu c_i exp(-Y_i)`, while recording the vortex-term proof obligations
  left schematic in classic mirror-duality papers.
- Proves that eliminating `Y_i` reproduces the Coulomb one-loop
  superpotential and that the constants `c_i` shift the finite definition of
  the FI coordinate.
- Derives the low-energy `Sigma_a` constraints
  `sum_i Q_i^a Y_i=-t_a`, producing the logarithmic-torus mirror
  Landau-Ginzburg presentation of protected twisted-chiral data.
- Works out the `P^{N-1}` mirror critical equations and matches their `N`
  simple critical points to the Coulomb vacuum count.
- Derives the classical cigar quotient metric by solving the auxiliary
  constraint, gauge fixing the logarithmic chiral scalar, and eliminating the
  gauge field.
- Develops the cigar/Liouville mirror chain as a QFT comparison problem:
  dual variables `Y,Y_P`, the single exponential from the ordinary charged
  chiral multiplet, absence of a logarithmic-chiral vortex exponential,
  the `Y+Y_P=0` vector constraint, the resulting `N=2` Liouville
  superpotential, and the theorem-status boundary for full equality with the
  cigar coset QFT.
- Defines abelian GLSM data with fields, integer charges, invariant
  superpotential, complexified FI-theta coordinate, gauge coupling, and
  regulator.
- States the axial anomaly charge sum as a finite ledger and a necessary
  condition, not a conformality proof.
- States the abelian GLSM Coulomb-branch one-loop determinant hypotheses,
  including logarithm branches, regulator scheme, and exclusion of
  boundary/vortex/singular-locus contributions from the local determinant,
  and then derives the perturbative local determinant contribution from the
  proper-time subtracted massive propagator plus the axial-anomaly phase that
  completes the holomorphic logarithm.
- Derives the effective twisted-superpotential critical equation
  `prod_i (Q_i sigma/mu)^{Q_i}=e^t` and proves that all-positive charges
  give `sum_i Q_i` simple local Coulomb vacua.
- Works out the `P^{N-1}` charge-one vacuum count and records the
  hypersurface charge-vector signal: the Coulomb `sigma` exponent is
  `N-d`, equal to the axial anomaly coefficient, so the anomaly-free case
  gives a FI-theta singular-locus condition rather than isolated Coulomb
  roots.
- Derives the classical chamber analysis for the hypersurface GLSM with
  charges `(1,...,1,-d)`, including the `r>0` hypersurface quotient, the
  `r<0` Landau-Ginzburg finite-quotient chamber, and the singular status of
  `r=0`.
- Derives the hypersurface adjunction formula
  `c1(TY_G)=(N-d)H|_{Y_G}` and `K_{Y_G}=O(d-N)|_{Y_G}`, making the
  `d=N` Calabi-Yau condition a finite geometric consequence rather than a
  slogan.
- Compares the large-volume sigma-model central-charge target
  `3(N-2)` with the Fermat Landau-Ginzburg protected central charge
  `3N(1-2/d)`, proving equality precisely for `d=N`.
- Makes the residual finite gauge theory explicit in the `r<0` chamber:
  after fixing nonzero `P`, the unbroken group is `mu_d`, it acts by
  `X_i -> zeta X_i`, the degree-`d` superpotential descends, and the
  untwisted Jacobi-basis invariant condition is
  `sum_i a_i = 0 mod d`.
- Derives the hypersurface Coulomb-coordinate signal
  `(sigma/mu)^{N-d}(-d)^{-d}_{branch}=exp(t)` and the anomaly-free
  branch condition `exp(t)=C_branch`, or `T=0` after an additive FI-coordinate
  shift.
- Presents the quintic GLSM solely as intrinsic two-dimensional QFT data, not
  as a string compactification.
- Records the construction problem for GLSM flows to Landau-Ginzburg and
  hypersurface sigma-model fixed points as intrinsic two-dimensional QFTs.

## Calculation Checks

- `calculation-checks/susy_2d_lg_glsm_checks.py` verifies:
  - `A_k` quasihomogeneous superpotential and derivative charges;
  - `A_k` Jacobi dimensions and central charges;
  - Fermat tensor-product monomial charges and Jacobi dimensions;
  - Fermat Wilsonian superpotential spurion selection, showing that
    regular holomorphic monomials obeying the declared flavor and `R` charges
    are exactly the original superpotential monomials;
  - quintic Landau-Ginzburg central charge `c=9` and Jacobi dimension `4^5`;
  - hypersurface GLSM gauge-invariance, axial-anomaly sum, positive-chamber
    dimension, and negative-chamber residual finite group order;
  - A/B twist spin shifts and scalar-supercharge nilpotence ledger;
  - abelian circle-duality momentum-winding spectrum invariance and
    chiral/twisted-chiral Legendre-Hessian inversion;
  - abelian GLSM Coulomb one-loop charge-exponent, positive-charge
    vacuum-count, hypersurface exponent/anomaly, quintic exponent-zero
    arithmetic, and the primitive of the Coulomb logarithmic derivative with
    its finite FI-coordinate shift under determinant normalization changes.
  - charged-chiral mirror-variable elimination matching the Coulomb one-loop
    superpotential and the finite FI-coordinate shift induced by vortex
    coefficient normalizations;
  - the `P^{N-1}` mirror critical-point simplicity ledger;
  - the cigar quotient metric coefficients after algebraic elimination of
    the gauge field.
  - hypersurface adjunction signs, LG/sigma-model central-charge matching,
    residual finite-gauge invariant Jacobi monomial counting, and the
    Coulomb-coordinate singular-signal ledger.

## Figure Ledger

No figure is included in this pass.  Future figures should include GLSM
chambers, LG critical loci, and quotient diagrams for simple toric examples.

## Issue Links

- Advances #603 by expanding Landau-Ginzburg and GLSM content as intrinsic
  two-dimensional `N=(2,2)` QFT and by excluding string-theory mirror or
  compactification interpretations from the proof content.
- The 2026-05-31 GLSM/mirror pass advances the same issue by incorporating
  and deepening the stringbook Appendix K charged-chiral mirror and
  cigar/Liouville material, while recording the regulator-level vortex and
  full-QFT equivalence proof obligations explicitly.
- The 2026-05-31 hypersurface phase pass further deepens Appendix K's
  Calabi-Yau/Landau-Ginzburg chamber discussion with adjunction, central
  charge, finite-gauge, and Coulomb-coordinate derivations.
- The 2026-05-31 Fermat Wilsonian pass imports and sharpens Appendix K's
  nonrenormalization footnote into an explicit two-dimensional
  holomorphic-coordinate selection argument with calculation-check coverage.
