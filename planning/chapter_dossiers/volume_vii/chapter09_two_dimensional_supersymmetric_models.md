# Chapter 09: Two-Dimensional Supersymmetric Models

## Source Position

Volume VII now leaves the four-dimensional gauge-dynamics core and begins the
lower-dimensional supersymmetric examples with `2D` `N=(2,2)` theories.

## Notation Inventory

- `Q_pm`, `bar Q_pm`, `P_pm`: two-dimensional supersymmetry generators and
  light-cone momenta.
- `F_V`, `F_A`: vector and axial `R` charges.
- `Phi^i=(phi^i, psi^i_+, psi^i_-, F^i)`, `K`, `g_i bar j`, `W`:
  Landau-Ginzburg chiral multiplet variables, Kahler potential, metric, and
  superpotential.
- `q_i`: quasihomogeneous Landau-Ginzburg weights.
- `Jac(W)`: Landau-Ginzburg Jacobian ring.
- `Q_B`, `eta_i`: B-type scalar differential and odd local variables used in
  the cohomological derivation of the Jacobian quotient.
- `X`, `g_i bar j`, `B`: sigma-model target, Kahler metric, and `B`-field.
- `G`, `V`, `r`, `Q_i`, `t`, `sigma`: GLSM gauge group, matter
  representation, Fayet-Iliopoulos coordinate, charges, complexified
  FI-theta coordinate, and vector-multiplet scalar.
- `X_i`, `P`, `G_d`, `d`, `mu_d`: hypersurface GLSM fields, homogeneous
  polynomial, degree, and residual finite gauge group.

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
- Defines sigma-model and GLSM data and separates protected coordinates from
  full infrared QFT equivalence.
- Defines abelian GLSM data with fields, integer charges, invariant
  superpotential, complexified FI-theta coordinate, gauge coupling, and
  regulator.
- States the axial anomaly charge sum as a finite ledger and a necessary
  condition, not a conformality proof.
- Proves the classical chamber analysis for the hypersurface GLSM with
  charges `(1,...,1,-d)`, including the `r>0` hypersurface quotient, the
  `r<0` Landau-Ginzburg finite-quotient chamber, and the singular status of
  `r=0`.
- Presents the quintic GLSM solely as intrinsic two-dimensional QFT data, not
  as a string compactification.
- Records the construction problem for GLSM flows to Landau-Ginzburg and
  hypersurface sigma-model fixed points as intrinsic two-dimensional QFTs.

## Calculation Checks

- `calculation-checks/susy_2d_lg_glsm_checks.py` verifies:
  - `A_k` quasihomogeneous superpotential and derivative charges;
  - `A_k` Jacobi dimensions and central charges;
  - Fermat tensor-product monomial charges and Jacobi dimensions;
  - quintic Landau-Ginzburg central charge `c=9` and Jacobi dimension `4^5`;
  - hypersurface GLSM gauge-invariance, axial-anomaly sum, positive-chamber
    dimension, and negative-chamber residual finite group order.

## Figure Ledger

No figure is included in this pass.  Future figures should include GLSM
chambers, LG critical loci, and quotient diagrams for simple toric examples.

## Issue Links

- Advances #603 by expanding Landau-Ginzburg and GLSM content as intrinsic
  two-dimensional `N=(2,2)` QFT and by excluding string-theory mirror or
  compactification interpretations from the proof content.
