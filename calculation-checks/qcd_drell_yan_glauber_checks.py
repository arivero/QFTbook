#!/usr/bin/env python3
"""Finite checks for the Drell-Yan/Glauber-status block in Volume II."""

from __future__ import annotations

import sympy as sp


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


def main() -> None:
    check_drell_yan_kinematics()
    check_rapidity_scale_product()
    check_t_odd_orientation_sign()
    check_finite_glauber_unitarity()
    print("All QCD Drell-Yan kinematics and Glauber-status checks passed.")


if __name__ == "__main__":
    main()
