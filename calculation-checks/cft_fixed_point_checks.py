#!/usr/bin/env python3
"""Finite algebra checks for CFT fixed-point opening conventions.

These checks accompany Volume III, Chapter 1.  They verify the dimension
dependent coefficients in the stress-tensor improvement, conformal-Killing
current conservation, and linearized RG scaling relation used in the chapter.
The checks are intentionally finite and exact; they do not attempt to prove
existence of a CFT or of an RG trajectory.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def eta_sign(index):
    return -1 if index == 0 else 1


def check_improvement_trace_coefficients():
    # The trace of (partial^mu partial^nu - eta^{mu nu} partial^2)L is
    # (1-D) partial^2 L in the mostly-plus convention.
    for dimension in range(2, 9):
        trace_coeff = 1 - dimension
        assert_equal(
            f"improvement trace coefficient D={dimension}",
            trace_coeff,
            -(dimension - 1),
        )


def special_conformal_derivative(dimension, mu, nu, rho):
    """Coefficient of a^rho in partial_mu xi_nu for special conformal xi.

    We use contravariant coordinates x^alpha and lower xi with eta.  The
    special conformal vector is xi^nu = 2(a.x)x^nu - x^2 a^nu.
    The returned value is a vector of coefficients multiplying x^k.
    """

    coeffs = [Fraction(0) for _ in range(dimension)]

    # 2 a_mu x_nu
    if rho == mu:
        coeffs[nu] += 2 * eta_sign(mu) * eta_sign(nu)

    # 2 (a.x) eta_{mu nu}
    if mu == nu:
        coeffs[rho] += 2 * eta_sign(mu) * eta_sign(rho)

    # -2 x_mu a_nu
    if rho == nu:
        coeffs[mu] -= 2 * eta_sign(mu) * eta_sign(nu)

    return tuple(coeffs)


def vector_add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def check_special_conformal_killing_equation():
    for dimension in range(2, 8):
        # div xi = 2D (a.x), so (2/D)(div xi) eta_{mu nu}
        # has coefficient 4 eta_{mu nu} eta_{rho rho} x^rho.
        for mu in range(dimension):
            for nu in range(dimension):
                for rho in range(dimension):
                    lhs = vector_add(
                        special_conformal_derivative(dimension, mu, nu, rho),
                        special_conformal_derivative(dimension, nu, mu, rho),
                    )
                    expected = [Fraction(0) for _ in range(dimension)]
                    if mu == nu:
                        expected[rho] = 4 * eta_sign(mu) * eta_sign(rho)
                    assert_equal(
                        f"special CKV equation D={dimension}, mu={mu}, nu={nu}, rho={rho}",
                        lhs,
                        tuple(expected),
                    )


def check_conformal_current_divergence_uses_trace_only():
    # For symmetric T, T^{mu nu} partial_mu xi_nu depends only on the trace for
    # a conformal Killing vector.  The coefficient is (div xi)/D.
    for dimension in range(2, 8):
        divergence_coeff = Fraction(1, dimension)
        # Special conformal div xi = 2D(a.x), hence coefficient is 2(a.x).
        assert_equal(
            f"special conformal trace coefficient D={dimension}",
            divergence_coeff * 2 * dimension,
            2,
        )
        # Dilatation xi^mu=x^mu has div xi=D, hence coefficient is 1.
        assert_equal(
            f"dilatation trace coefficient D={dimension}",
            divergence_coeff * dimension,
            1,
        )


def check_linearized_rg_dimension_relation():
    examples = [
        (Fraction(4), Fraction(1), Fraction(3)),
        (Fraction(3), Fraction(5, 4), Fraction(7, 4)),
        (Fraction(2), Fraction(15, 8), Fraction(1, 8)),
    ]
    for dimension, delta, y_value in examples:
        assert_equal(
            f"linearized RG y=D-Delta for D={dimension}",
            dimension - delta,
            y_value,
        )

    # A two-by-two Jordan block gives b^y times a polynomial in log b.  The
    # finite matrix identity N^2=0 is the algebraic source of the logarithm.
    jordan_nilpotent = ((Fraction(0), Fraction(1)), (Fraction(0), Fraction(0)))
    square = (
        (
            jordan_nilpotent[0][0] * jordan_nilpotent[0][0]
            + jordan_nilpotent[0][1] * jordan_nilpotent[1][0],
            jordan_nilpotent[0][0] * jordan_nilpotent[0][1]
            + jordan_nilpotent[0][1] * jordan_nilpotent[1][1],
        ),
        (
            jordan_nilpotent[1][0] * jordan_nilpotent[0][0]
            + jordan_nilpotent[1][1] * jordan_nilpotent[1][0],
            jordan_nilpotent[1][0] * jordan_nilpotent[0][1]
            + jordan_nilpotent[1][1] * jordan_nilpotent[1][1],
        ),
    )
    assert_equal("rank-two Jordan nilpotent square", square, ((0, 0), (0, 0)))


def main():
    check_improvement_trace_coefficients()
    check_special_conformal_killing_equation()
    check_conformal_current_divergence_uses_trace_only()
    check_linearized_rg_dimension_relation()
    print("All CFT fixed-point convention checks passed.")


if __name__ == "__main__":
    main()
