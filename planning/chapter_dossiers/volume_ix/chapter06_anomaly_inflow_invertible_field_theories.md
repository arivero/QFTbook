# Chapter 06: Anomaly Inflow And Invertible Field Theories

## Source Position

This chapter follows global forms, extended operators, confinement data, and
discrete theta terms.  It gives the relative-QFT language needed to treat
anomalous background-field dependence as an anomaly-line functor and as a
boundary condition for an invertible bulk theory.

## Notation Inventory

- `B(M)`: groupoid of background fields on spacetime `M`.
- `u:A->A'`: background-field isomorphism.
- `L_M(A)`: anomaly line over a background `A`.
- `alpha_M(u;A)`: scalar representative of the anomaly-line functor in a
  chosen frame.
- `Z_bulk`: invertible `(D+1)`-dimensional bulk theory valued in complex
  lines.
- `I_{D+1}^{(0)}`, `P_{D+2}`: Chern-Simons representative and invariant
  polynomial.
- `I_D^{(1)}`: descent variation form.
- `B in Z^{p+1}(X,A)`: finite higher-form background.
- `b,c in C^2(X,Z_N)`: paired one-form-symmetry backgrounds in the finite
  five-dimensional Heisenberg/BF model.
- `mathcal I_6(R)`: index-normalized six-form anomaly polynomial
  `[A-hat(TX) ch_R(F_X)]_6` for a four-dimensional left-handed Weyl fermion.
- `W_X^{inv}`: five-dimensional invertible response whose boundary variation
  cancels the four-dimensional anomaly.
- `p_1(TX)`: first Pontryagin Chern--Weil form.
- `D_g`: codimension-one defect obtained by tensoring a transformation wall
  with a wall theory that trivializes its anomaly line.

## Claim Ledger

- Defines anomalous partition functions as sections of anomaly-line functors
  over background-field groupoids.
- Proves the functorial cocycle condition for scalar anomaly representatives
  and the frame-change law under local counterterms.
- Constructs the boundary anomaly line from an invertible bulk by comparing
  fillings and proves that bulk gluing gives the line functor.
- Derives the connected-symmetry descent variation from
  `dI_{D+1}^{(0)}=P_{D+2}`.
- Derives Wess--Zumino consistency as the infinitesimal form of anomaly-line
  functoriality.
- Proves that changing the Chern-Simons representative by `dK_D` shifts the
  boundary anomaly by the variation of a local counterterm.
- Defines finite higher-form inflow by cochain cocycles on `B^{p+1}A`.
- Proves the finite `Z_N` one-form `BF` inflow variation:
  `int_X delta lambda cup delta c = int_boundary lambda cup delta c`.
- Derives the five-dimensional response for a four-dimensional left-handed
  Weyl fermion from the index-normalized polynomial
  `[A-hat(TX) ch_R(F_X)]_6`.
- Carries the \(U(1)\) coefficient explicitly:
  \[
    W_X^{inv}
    =
    -2\pi i\int_X
    \left[
      q^3 A F^2/(6(2\pi)^3)
      -
      q A p_1(TX)/(24(2\pi))
    \right],
  \]
  whose boundary variation is the cubic and mixed gravitational anomaly.
- Records the local gauged \(U(1)\) conditions
  \(\sum q_i^3=0\), \(\sum q_i=0\), while emphasizing that global anomalies
  are statements about the full invertible theory.
- Defines noninvertible chiral defects as anomaly-trivialized
  codimension-one transformation walls and proves the wall-trivialization
  criterion.
- Connects compact-QED axial defects to the magnetic one-form anomaly and to
  the detailed construction in Volume IX Chapter 11.
- Proves that finite gauging requires a trivialized anomaly line.

## Calculation Checks

- `calculation-checks/anomaly_polynomial_descent_checks.py` verifies the
  rational coefficients used in the Weyl-fermion inflow calculation and the
  one-generation Standard Model anomaly sums.
- `calculation-checks/inflow_anomaly_line_checks.py` verifies anomaly-line
  cocycle composition, frame/counterterm shifts of representatives, and the
  finite cochain Stokes identity for one-form \(BF\) inflow.

## Figure Ledger

- `fig:inflow-boundary-line-gluing`: compares two fillings of the same
  boundary background and shows how the closed bulk phase relates frames of
  the anomaly line.
