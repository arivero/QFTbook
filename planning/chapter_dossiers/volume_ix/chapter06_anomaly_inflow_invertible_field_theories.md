# Chapter 06: Anomaly Inflow And Invertible Field Theories

## Source Position

This chapter follows global forms, extended operators, confinement data, and
discrete theta terms.  It introduces anomaly lines and invertible bulk
theories as the object-level language for anomalous background-field
dependence.

## Notation Inventory

- `B(M)`: groupoid of background fields on spacetime `M`.
- `L_M(A)`: anomaly line over a background `A`.
- `Z_N(Atilde)`: invertible bulk theory on a `(D+1)`-manifold.
- `I_{D+1}`, `P_{D+2}`: Chern-Simons cocycle and invariant polynomial.
- `I_D^{(1)}`: descent variation.
- `mathcal I_6(R)`: index-normalized six-form anomaly polynomial
  `[A-hat(TX) ch_R(F_X)]_6` for a four-dimensional left-handed Weyl fermion.
- `W_X^{inv}`: five-dimensional invertible response whose boundary variation
  cancels the four-dimensional anomaly.
- `p_1(TX)`: first Pontryagin Chern--Weil form.
- `D_g`: codimension-one defect obtained by tensoring a transformation wall
  with a wall theory that trivializes its anomaly line.
- `B in Z^2(M,A)`: one-form symmetry background for finite abelian `A`.

## Claim Ledger

- Defines anomalous partition functions as sections of anomaly lines.
- Defines inflow as an invertible bulk theory whose boundary line is the
  anomaly line.
- Derives the descent variation from `dI_{D+1}=P_{D+2}`.
- Proves that changing the bulk cocycle by a coboundary shifts the boundary
  anomaly by a local counterterm.
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
- Records the resulting gauged \(U(1)\) constraints
  \(\sum q_i^3=0\), \(\sum q_i=0\), and the mixed nonabelian-\(U(1)\)
  constraints.
- Defines noninvertible chiral defects as anomaly-trivialized
  codimension-one transformation walls; fusion is noninvertible when the wall
  trivialization involves summing over finite higher-form gauge sectors.
- Connects compact-QED axial defects to the magnetic one-form anomaly and to
  the detailed construction in Volume IX Chapter 11.
- States the gauging criterion as trivialization of the invertible anomaly
  theory.

## Calculation Checks

- `calculation-checks/anomaly_polynomial_descent_checks.py` verifies the
  rational coefficients used in the Weyl-fermion inflow calculation and the
  one-generation Standard Model anomaly sums.

## Figure Ledger

No figure is included.  Future diagrams should show a bulk manifold with
boundary, anomaly line assignment over background fields, and defect action of
one-form backgrounds.
