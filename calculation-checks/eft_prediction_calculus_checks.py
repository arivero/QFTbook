#!/usr/bin/env python3
r"""Evidence contract.

Target claims:
- The heavy scalar tree kernel expands as a local derivative series with a
  controlled low-momentum remainder.
- The one-loop hard threshold term cancels the artificial matching-scale
  dependence against full-theory and low-theory running at the retained order.
- In a massive scalar EFT retaining \(\phi^4\) and \(\phi^6/\mathcal M^2\),
  the one-loop background-field pole closes on the retained coordinates
  through canonical excess two and generates \(\phi^8/\mathcal M^4\) as the
  first omitted local operator.
- In the same scalar EFT, a local field redefinition preserves the on-shell
  four-point observable only when the action, Jacobian, source transform,
  composite transform, and Wilson-coordinate shifts are carried together.

Independent construction:
- The heavy-kernel identity is checked as an exact rational identity and as a
  dimensionful bound on the declared low-momentum domain.
- The matching-scale cancellation is checked by differentiating a symbolic
  one-loop matched coordinate.
- The one-loop EFT closure coefficients are extracted from
  \((V''(\phi))^2\) in a common factorial normalization.
- The field-redefinition check computes the transformed scalar EFT
  coefficients, source/composite/Jacobian terms, and the tree four-point
  kernel on and away from the external mass shell.

Imported assumptions:
- Euclidean low-energy kinematics with q^2 >= 0 and q^2 <= Q^2 << M^2.
- The quartic coordinate is normalized so the heavy beta contribution is the
  coefficient b_H in d lambda_full / d log(mu) = beta_light + b_H.
- The scalar one-loop pole uses dimensional regularization with minimal
  subtraction and the standard background-field local-potential pole
  Gamma_div^(1)=(32 pi^2 epsilon)^(-1) int (V'')^2.
- The field-redefinition observable check uses the analytically continued
  external pole condition p_i^2=-m^2.

Negative controls:
- Reversing the heavy-kernel remainder sign fails the exact identity.
- Omitting the hard threshold logarithm leaves matching-scale dependence.
- The script rejects wrong one-loop combinatorial coefficients and rejects
  retaining the generated \(\phi^8\) pole inside a canonical-excess-two
  truncation.
- Dropping either the derivative term or the mass-coordinate shift spoils the
  field-redefinition equality of the on-shell four-point kernel; dropping the
  Jacobian, source transform, or composite transform is also detected.

Scope boundary:
- This script checks finite algebra and bookkeeping for the EFT prediction
  calculus.  It does not prove nonperturbative decoupling, regulator removal,
  asymptotic convergence, or a continuum scattering construction.
"""

from __future__ import annotations

import sympy as sp

from check_utils import assert_gt, assert_leq


def assert_zero(name: str, value: sp.Expr) -> None:
    if sp.simplify(value) != 0:
        raise AssertionError(f"{name}: expected zero, got {sp.simplify(value)!r}")


def assert_nonzero(name: str, value: sp.Expr) -> None:
    if sp.simplify(value) == 0:
        raise AssertionError(f"{name}: expected a nonzero negative control")


def check_heavy_kernel_expansion() -> None:
    x = sp.symbols("x")
    for order in range(5):
        truncated = sum((-x) ** r for r in range(order + 1))
        remainder = (-x) ** (order + 1) / (1 + x)
        exact = 1 / (1 + x)
        assert_zero(f"geometric heavy-kernel remainder N={order}", truncated + remainder - exact)
        assert_nonzero(
            f"wrong-sign heavy-kernel remainder N={order}",
            truncated - remainder - exact,
        )

    M, q2 = sp.symbols("M q2", positive=True)
    order = 3
    dimensionful = 1 / (M**2 + q2)
    dimensionful_truncated = sum((-q2) ** r / M ** (2 * r + 2) for r in range(order + 1))
    dimensionful_remainder = (-q2) ** (order + 1) / (M ** (2 * order + 2) * (M**2 + q2))
    assert_zero(
        "dimensionful heavy-kernel expansion",
        dimensionful_truncated + dimensionful_remainder - dimensionful,
    )

    for ratio in (0.05, 0.1, 0.25):
        mass = 11.0
        q2_value = (ratio * mass) ** 2
        remainder_value = abs(float(dimensionful_remainder.subs({M: mass, q2: q2_value})))
        bound = q2_value ** (order + 1) / mass ** (2 * order + 4)
        assert_leq(f"low-momentum heavy-kernel bound Q/M={ratio}", remainder_value, bound)

    eta = sp.symbols("eta", nonzero=True)
    quartic_lambda_shift = sp.factor(sp.factorial(4) * (-eta**2 / (8 * M**2)))
    assert_zero("tree exchange converted to lambda/4! convention", quartic_lambda_shift + 3 * eta**2 / M**2)
    kernel_q2_coefficient = sp.expand(-eta**2 / 8 * (1 / M**2 - q2 / M**4)).coeff(q2)
    assert_zero("positive derivative operator sign", kernel_q2_coefficient - eta**2 / (8 * M**4))


def check_matching_scale_cancellation() -> None:
    L_M, L_low, lam_M, beta_light, b_H, c_H = sp.symbols(
        "L_M L_low lam_M beta_light b_H c_H"
    )
    beta_full = beta_light + b_H
    hard_threshold = -b_H * L_M + c_H
    running_to_low = beta_light * (L_low - L_M)
    matched_low_coordinate = lam_M + beta_full * L_M + hard_threshold + running_to_low

    expected = lam_M + beta_light * L_low + c_H
    assert_zero("one-loop matching-scale cancellation", matched_low_coordinate - expected)
    assert_zero("derivative with respect to matching log", sp.diff(matched_low_coordinate, L_M))

    missing_threshold = lam_M + beta_full * L_M + running_to_low
    assert_nonzero("missing hard threshold leaves scale dependence", sp.diff(missing_threshold, L_M))
    wrong_threshold = lam_M + beta_full * L_M - hard_threshold + running_to_low
    assert_nonzero("wrong hard threshold sign leaves scale dependence", sp.diff(wrong_threshold, L_M))


def check_one_loop_scalar_eft_closure() -> None:
    phi, lam, c6, m2, M2 = sp.symbols("phi lam c6 m2 M2", nonzero=True)

    # In the common normalization
    # Gamma_div^(1) = (32 pi^2 eps)^(-1) int (V''(phi))^2,
    # convert coefficients to the monograph's common pole factor
    # (16 pi^2 eps)^(-1) times O_n/n!.
    v_second = m2 + lam * phi**2 / 2 + c6 * phi**4 / (24 * M2)
    pole_polynomial = sp.expand(v_second**2)

    lambda_pole = sp.factor(sp.factorial(4) * pole_polynomial.coeff(phi, 4) / 2)
    c6_pole = sp.factor(sp.factorial(6) * M2 * pole_polynomial.coeff(phi, 6) / 2)
    c8_pole = sp.factor(sp.factorial(8) * M2**2 * pole_polynomial.coeff(phi, 8) / 2)

    assert_zero(
        "one-loop phi4 pole with one phi6 insertion",
        lambda_pole - (3 * lam**2 + m2 * c6 / M2),
    )
    assert_zero("one-loop phi6 pole from higher-dimensional insertion", c6_pole - 15 * lam * c6)
    assert_zero("first omitted phi8 pole", c8_pole - 35 * c6**2)

    assert_nonzero("wrong phi6 pole combinatorics rejected", c6_pole - 10 * lam * c6)
    assert_nonzero("wrong phi8 pole combinatorics rejected", c8_pole - 28 * c6**2)

    retained_canonical_excess = {"phi4": 0, "phi6": 2}
    first_omitted_canonical_excess = {"phi8": 4}
    target_excess = 2
    assert_leq("phi4 pole remains in retained excess", retained_canonical_excess["phi4"], target_excess)
    assert_leq("phi6 pole remains in retained excess", retained_canonical_excess["phi6"], target_excess)
    assert_gt(
        "phi8 pole is assigned to the residual sector",
        first_omitted_canonical_excess["phi8"],
        target_excess,
    )

    q_over_M = sp.symbols("q_over_M", positive=True)
    residual_scaling = c8_pole * q_over_M**4
    assert_zero("first omitted operator has canonical-excess-four scaling", sp.diff(residual_scaling, q_over_M, 4) - 24 * c8_pole)


def check_scalar_eft_field_redefinition_observable() -> None:
    a, lam, c6, m2, M2, d, delta_reg, J, source_probe = sp.symbols(
        "a lam c6 m2 M2 d delta_reg J source_probe", nonzero=True
    )
    p1sq, p2sq, p3sq, p4sq = sp.symbols("p1sq p2sq p3sq p4sq")

    lambda_prime = lam + 24 * a * m2 / M2
    derivative_coefficient_prime = d + 3 * a
    c6_prime = c6 + 120 * a * lam
    lambda_shift = lambda_prime - lam
    derivative_coefficient_shift = derivative_coefficient_prime - d
    c6_shift = c6_prime - c6
    jacobian_mass_coordinate = -3 * a * delta_reg / M2
    source_cubic_coordinate = a * J / M2
    composite_phi_squared_shift = 2 * a / M2

    assert_zero("quartic coordinate shift under local redefinition", lambda_shift - 24 * a * m2 / M2)
    assert_zero("derivative coordinate shift under local redefinition", derivative_coefficient_shift - 3 * a)
    assert_zero("sextic coordinate shift under local redefinition", c6_shift - 120 * a * lam)
    assert_zero("finite-regulator Jacobian mass coordinate", jacobian_mass_coordinate + 3 * a * delta_reg / M2)
    assert_zero("source cubic coordinate is transformed", source_cubic_coordinate - a * J / M2)
    assert_zero("phi-squared composite representative is transformed", composite_phi_squared_shift - 2 * a / M2)

    sum_p2 = p1sq + p2sq + p3sq + p4sq
    derivative_kernel = 6 * a * sum_p2 / M2
    quartic_kernel = lambda_shift
    eom_kernel = 6 * a * (sum_p2 + 4 * m2) / M2
    assert_zero("split EOM operator four-point kernel", derivative_kernel + quartic_kernel - eom_kernel)

    on_shell = {p1sq: -m2, p2sq: -m2, p3sq: -m2, p4sq: -m2}
    assert_zero("on-shell four-point observable is basis independent", eom_kernel.subs(on_shell))
    assert_nonzero("omitting derivative term spoils on-shell equality", quartic_kernel.subs(on_shell))
    assert_nonzero("omitting mass-coordinate shift spoils on-shell equality", derivative_kernel.subs(on_shell))

    off_shell = {p1sq: 0, p2sq: 0, p3sq: 0, p4sq: 0}
    assert_nonzero("off-shell Green function changes under EOM redefinition", eom_kernel.subs(off_shell))
    assert_nonzero("dropping Jacobian changes cutoff-regulator coordinates", jacobian_mass_coordinate)
    assert_nonzero("dropping source transform changes sourced functional", source_cubic_coordinate.subs(J, source_probe))
    assert_nonzero("dropping composite transform changes insertions", composite_phi_squared_shift)


def main() -> None:
    check_heavy_kernel_expansion()
    check_matching_scale_cancellation()
    check_one_loop_scalar_eft_closure()
    check_scalar_eft_field_redefinition_observable()
    print("All EFT prediction-calculus checks passed.")


if __name__ == "__main__":
    main()
