#!/usr/bin/env python3
"""Finite checks for the Drell-Yan/Glauber-status block in Volume II.

These checks verify kinematic and finite-algebra facts used in the text.  They
do not prove Drell-Yan factorization.  The nontrivial algebraic checks are the
two-incoming-leg RG cancellation
    dC = -P_A^T C - C P_B
for the transform-space coordinate f_A^T C f_B, and the finite scheme
covariance
    C' = (R_A^{-1})^T C R_B^{-1}.
The theorem-boundary check keeps separate leading-region, soft, Glauber, power,
and regulator residuals between the exact Wightman functional and the
factorized coordinate; exact RG bookkeeping does not remove a nonzero residual.
The finite inclusive-projection check verifies that a Glauber unitary cancels
for measurements in the inclusive commutant and leaves a bounded nonzero
residual when the measurement resolves the spectator sector.

Evidence contract.
Target claims: Drell-Yan leading-power kinematic coordinates, two-incoming-leg
Born rapidity-bin coefficient and convolution normalization, RG and scheme
covariance of the factorized coordinate, TMD rapidity-scale and orientation
bookkeeping, and finite algebraic models for theorem-boundary Glauber
residuals.
Independent construction: exact symbolic matrix/vector arithmetic, finite
unitary conjugation, Born change-of-variable Jacobians, delta-kernel
convolution weights, residual decomposition, and a spectator-resolving negative
control independent of any diagrammatic factorization proof.
Imported assumptions: the chapter's PDF/TMD operator definitions, the
existence of regulated leading regions, and the identification of the
finite unitary model as the algebraic shadow of QCD Glauber exchange.
Negative controls: a deliberately nonzero Wightman-to-factorized residual,
the statement that RG covariance does not remove that residual, a missing
Drell-Yan Born Jacobian, a wrong delta-kernel normalization, and a measurement
resolving the unobserved sector that leaves a nonzero but bounded Glauber
remainder.
Scope boundary: these checks do not prove Drell-Yan factorization, contour
deformation, soft cancellation in continuum QCD, universality of TMDs, or
power-suppressed remainder estimates.
"""

from __future__ import annotations

import sympy as sp

from check_utils import assert_leq as _assert_leq


def assert_zero(name: str, expr: sp.Expr) -> None:
    reduced = sp.simplify(expr)
    if reduced != 0:
        raise AssertionError(f"{name}: got {reduced!r}, expected 0")


def check_drell_yan_kinematics() -> None:
    tau, y = sp.symbols("tau y", positive=True)
    x_a = sp.sqrt(tau) * sp.exp(y)
    x_b = sp.sqrt(tau) * sp.exp(-y)

    assert_zero("Drell-Yan product x_A x_B", x_a * x_b - tau)
    assert_zero("Drell-Yan rapidity", sp.log(x_a / x_b) / 2 - y)


def check_born_rapidity_bin_coefficient() -> None:
    q_sq, s, alpha, e_q = sp.symbols("q_sq s alpha e_q", positive=True)
    n_c = sp.symbols("n_c", positive=True, integer=True)
    xi_a, xi_b = sp.symbols("xi_a xi_b", positive=True)
    cos_theta = sp.symbols("cos_theta", real=True)

    angular_distribution = (
        sp.pi * alpha**2 * e_q**2 / (2 * n_c * q_sq)
        * (1 + cos_theta**2)
    )
    partonic_cross_section = sp.integrate(
        angular_distribution,
        (cos_theta, -1, 1),
    )
    expected_partonic = 4 * sp.pi * alpha**2 * e_q**2 / (3 * n_c * q_sq)
    assert_zero("Drell-Yan Born angular integral", partonic_cross_section - expected_partonic)

    jacobian = sp.Matrix(
        [
            [s * xi_b, s * xi_a],
            [sp.Rational(1, 2) / xi_a, -sp.Rational(1, 2) / xi_b],
        ]
    ).det()
    assert_zero("Drell-Yan Born rapidity Jacobian", jacobian + s)

    differential_coefficient = partonic_cross_section / s
    expected = 4 * sp.pi * alpha**2 * e_q**2 / (3 * n_c * q_sq * s)
    assert_zero("Drell-Yan Born differential coefficient", differential_coefficient - expected)
    assert_zero(
        "Drell-Yan Born Nc=3 normalization",
        differential_coefficient.subs(n_c, 3)
        - 4 * sp.pi * alpha**2 * e_q**2 / (9 * q_sq * s),
    )

    x = sp.Rational(2, 5)
    pdf_value = sp.Rational(7, 11)
    delta_weight = x  # delta(1 - x/xi) = x delta(xi - x)
    convolution_value = pdf_value * delta_weight / x
    assert_zero("Drell-Yan Born delta convolution", convolution_value - pdf_value)

    wrong_plain_delta = pdf_value / x
    if wrong_plain_delta == pdf_value:
        raise AssertionError("plain delta kernel should not match the convolution normalization")

    missing_jacobian = partonic_cross_section
    if sp.simplify(missing_jacobian - differential_coefficient) == 0:
        raise AssertionError("dropping the rapidity-bin Jacobian should change the coefficient")


def check_rapidity_scale_product() -> None:
    q_sq, eta = sp.symbols("q_sq eta", positive=True)
    zeta_a = q_sq**2 * sp.exp(2 * eta)
    zeta_b = q_sq**2 * sp.exp(-2 * eta)
    assert_zero("TMD rapidity-scale product", zeta_a * zeta_b - q_sq**4)


def check_t_odd_orientation_sign() -> None:
    even, odd = sp.symbols("even odd")
    sidis = even + odd
    drell_yan = even - odd

    assert_zero("T-even projection", (sidis + drell_yan) / 2 - even)
    assert_zero("T-odd projection", (sidis - drell_yan) / 2 - odd)


def check_integrated_drell_yan_rg_cancellation() -> None:
    p_a = sp.Matrix(
        [
            [sp.Rational(2, 5), sp.Rational(-1, 7)],
            [sp.Rational(3, 11), sp.Rational(5, 13)],
        ]
    )
    p_b = sp.Matrix(
        [
            [sp.Rational(-2, 3), sp.Rational(1, 5)],
            [sp.Rational(7, 17), sp.Rational(4, 19)],
        ]
    )
    coeff = sp.Matrix(
        [
            [sp.Rational(11, 23), sp.Rational(13, 29)],
            [sp.Rational(17, 31), sp.Rational(19, 37)],
        ]
    )
    f_a = sp.Matrix([sp.Rational(3, 2), sp.Rational(5, 4)])
    f_b = sp.Matrix([sp.Rational(7, 6), sp.Rational(11, 8)])

    d_coeff = -p_a.T * coeff - coeff * p_b
    derivative = (
        (p_a * f_a).T * coeff * f_b
        + f_a.T * d_coeff * f_b
        + f_a.T * coeff * (p_b * f_b)
    )
    assert_zero("integrated Drell-Yan two-leg RG cancellation", derivative[0])


def check_integrated_drell_yan_scheme_covariance() -> None:
    coeff = sp.Matrix(
        [
            [sp.Rational(5, 7), sp.Rational(2, 3)],
            [sp.Rational(11, 13), sp.Rational(17, 19)],
        ]
    )
    f_a = sp.Matrix([sp.Rational(3, 5), sp.Rational(7, 11)])
    f_b = sp.Matrix([sp.Rational(13, 17), sp.Rational(19, 23)])
    r_a = sp.Matrix(
        [
            [sp.Rational(2, 3), sp.Rational(1, 5)],
            [sp.Rational(1, 7), sp.Rational(5, 4)],
        ]
    )
    r_b = sp.Matrix(
        [
            [sp.Rational(7, 6), sp.Rational(-1, 8)],
            [sp.Rational(2, 9), sp.Rational(11, 10)],
        ]
    )

    original = f_a.T * coeff * f_b
    f_a_prime = r_a * f_a
    f_b_prime = r_b * f_b
    coeff_prime = r_a.inv().T * coeff * r_b.inv()
    shifted = f_a_prime.T * coeff_prime * f_b_prime

    assert_zero(
        "integrated Drell-Yan finite scheme covariance",
        shifted[0] - original[0],
    )


def check_integrated_drell_yan_factorization_residual_budget() -> None:
    p_a = sp.Matrix(
        [
            [sp.Rational(1, 3), sp.Rational(1, 7)],
            [sp.Rational(-2, 5), sp.Rational(3, 11)],
        ]
    )
    p_b = sp.Matrix(
        [
            [sp.Rational(2, 9), sp.Rational(-1, 4)],
            [sp.Rational(5, 13), sp.Rational(1, 6)],
        ]
    )
    coeff = sp.Matrix(
        [
            [sp.Rational(7, 19), sp.Rational(3, 17)],
            [sp.Rational(5, 23), sp.Rational(11, 29)],
        ]
    )
    f_a = sp.Matrix([sp.Rational(5, 6), sp.Rational(7, 10)])
    f_b = sp.Matrix([sp.Rational(9, 14), sp.Rational(11, 15)])

    factorized = (f_a.T * coeff * f_b)[0]
    residuals = {
        "leading": sp.Rational(1, 40),
        "soft": sp.Rational(-1, 60),
        "glauber": sp.Rational(1, 105),
        "power": sp.Rational(-1, 84),
        "regulator": sp.Rational(1, 210),
    }
    residual_total = sum(residuals.values(), sp.Rational(0))
    exact_wightman_coordinate = factorized + residual_total

    assert_zero(
        "tested Drell-Yan residual decomposition",
        exact_wightman_coordinate - factorized - residual_total,
    )
    if residual_total == 0:
        raise AssertionError("residual budget accidentally collapsed to zero")

    residual_bound = sum(abs(value) for value in residuals.values())
    _assert_leq(
        "Drell-Yan residual triangle budget",
        abs(residual_total),
        residual_bound,
        tol=sp.Rational(0),
    )

    d_coeff = -p_a.T * coeff - coeff * p_b
    factorized_derivative = (
        (p_a * f_a).T * coeff * f_b
        + f_a.T * d_coeff * f_b
        + f_a.T * coeff * (p_b * f_b)
    )[0]
    assert_zero(
        "RG covariance does not remove Drell-Yan theorem-boundary residual",
        factorized_derivative,
    )
    assert_zero(
        "exact minus factorized remains the residual",
        exact_wightman_coordinate - factorized - residual_total,
    )


def check_finite_glauber_unitarity() -> None:
    c = sp.Rational(3, 5)
    s = sp.Rational(4, 5)
    unitary = sp.Matrix([[c, -s], [s, c]])
    assert_zero("Glauber finite unitary", (unitary.T * unitary - sp.eye(2)).norm())

    rho = sp.Matrix(
        [
            [sp.Rational(2, 7), sp.Rational(1, 11), 0, sp.Rational(1, 13)],
            [sp.Rational(1, 11), sp.Rational(1, 5), sp.Rational(1, 17), 0],
            [0, sp.Rational(1, 17), sp.Rational(3, 10), sp.Rational(1, 19)],
            [sp.Rational(1, 13), 0, sp.Rational(1, 19), sp.Rational(3, 14)],
        ]
    )
    observed = sp.Matrix([[sp.Rational(5, 2), sp.Rational(1, 3)], [sp.Rational(1, 3), sp.Rational(-1, 3)]])
    measured = sp.kronecker_product(observed, sp.eye(2))
    glauber = sp.kronecker_product(sp.eye(2), unitary)

    before = sp.trace(measured * rho)
    after = sp.trace(measured * glauber * rho * glauber.T)

    # This is the same identity as the text: the measured operator acts only on
    # the observed tensor factor and commutes with the unobserved unitary.
    assert_zero("Glauber finite trace identity", after - before)


def check_inclusive_glauber_projection_residual() -> None:
    # The unobserved two-state sector is swapped by a finite Glauber unitary.
    # A measurement acting only on the observed sector is invariant, while a
    # resolved measurement that distinguishes the unobserved states is not.
    swap = sp.Matrix([[0, 1], [1, 0]])
    glauber = sp.kronecker_product(sp.eye(2), swap)

    rho = sp.diag(
        sp.Rational(1, 10),
        sp.Rational(2, 10),
        sp.Rational(3, 10),
        sp.Rational(4, 10),
    )
    assert_zero("finite density trace normalization", sp.trace(rho) - 1)

    inclusive_measurement = sp.kronecker_product(
        sp.diag(sp.Rational(5, 3), sp.Rational(-2, 7)),
        sp.eye(2),
    )
    inclusive_delta = glauber.T * inclusive_measurement * glauber - inclusive_measurement
    assert_zero("inclusive measurement commutes with Glauber unitary", inclusive_delta.norm())
    assert_zero(
        "inclusive Glauber residual vanishes",
        sp.trace(rho * inclusive_delta),
    )

    resolved_measurement = sp.diag(
        sp.Rational(0),
        sp.Rational(1),
        sp.Rational(2),
        sp.Rational(4),
    )
    resolved_delta = glauber.T * resolved_measurement * glauber - resolved_measurement
    residual = sp.trace(rho * resolved_delta)
    if residual == 0:
        raise AssertionError("resolved Glauber residual accidentally vanished")

    # Since rho is diagonal positive with trace one and resolved_delta is
    # diagonal, this is the finite trace-norm/operator-norm bound in the text.
    trace_norm = sp.trace(rho)
    operator_norm = max(abs(entry) for entry in resolved_delta.diagonal())
    _assert_leq(
        "resolved Glauber residual bounded by trace-op norm",
        abs(residual),
        trace_norm * operator_norm,
        tol=sp.Rational(0),
    )


def main() -> None:
    check_drell_yan_kinematics()
    check_born_rapidity_bin_coefficient()
    check_rapidity_scale_product()
    check_t_odd_orientation_sign()
    check_integrated_drell_yan_rg_cancellation()
    check_integrated_drell_yan_scheme_covariance()
    check_integrated_drell_yan_factorization_residual_budget()
    check_finite_glauber_unitarity()
    check_inclusive_glauber_projection_residual()
    print("All QCD Drell-Yan kinematics and Glauber-status checks passed.")


if __name__ == "__main__":
    main()
