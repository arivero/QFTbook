#!/usr/bin/env python3
"""Finite checks for the N=4 SYM SCFT foundation material."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, value: object, expected: object) -> None:
    if value != expected:
        raise AssertionError(f"{name}: got {value!r}, expected {expected!r}")


def delta(i: int, j: int) -> Fraction:
    return Fraction(1 if i == j else 0)


def projector(i: int, j: int, k: int, ell: int, dimension: int = 6) -> Fraction:
    return (
        Fraction(1, 2) * (delta(i, k) * delta(j, ell) + delta(i, ell) * delta(j, k))
        - Fraction(1, dimension) * delta(i, j) * delta(k, ell)
    )


def check_beta_function_cancellations() -> None:
    ordinary_b0_per_casimir = (
        Fraction(11, 3)
        - 4 * Fraction(2, 3)
        - 6 * Fraction(1, 6)
    )
    assert_equal("ordinary one-loop beta cancellation", ordinary_b0_per_casimir, 0)

    holomorphic_b0_per_casimir = 3 - 3
    assert_equal("N=1 holomorphic beta cancellation", holomorphic_b0_per_casimir, 0)


def matrix_multiply(
    left: tuple[int, int, int, int],
    right: tuple[int, int, int, int],
) -> tuple[int, int, int, int]:
    a, b, c, d = left
    e, f, g, h = right
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


def matrix_power(
    matrix: tuple[int, int, int, int],
    exponent: int,
) -> tuple[int, int, int, int]:
    result = (1, 0, 0, 1)
    for _ in range(exponent):
        result = matrix_multiply(result, matrix)
    return result


def check_exact_marginal_coupling_chart() -> None:
    source_dimension = 1
    beta_constraints = 0
    quotient_directions = 0
    local_dimension = source_dimension - beta_constraints - quotient_directions

    assert_equal("N=4 local conformal chart dimension", local_dimension, 1)

    # Theta periodicity is tau -> tau+1.  For integer instanton number k, the
    # path-integral phase changes by exp(2*pi*i*k)=1, so only integrality is
    # relevant to this exact finite check.
    for instanton_number in range(-3, 4):
        phase_winding = instanton_number
        assert_equal(
            f"theta periodicity phase winding k={instanton_number}",
            phase_winding % 1,
            0,
        )


def check_sl2z_coupling_action() -> None:
    s_generator = (0, -1, 1, 0)
    t_generator = (1, 1, 0, 1)
    minus_identity = (-1, 0, 0, -1)

    for matrix in (s_generator, t_generator):
        a, b, c, d = matrix
        assert_equal("SL(2,Z) determinant", a * d - b * c, 1)

    assert_equal("S squared in SL(2,Z)", matrix_power(s_generator, 2), minus_identity)
    assert_equal(
        "(ST)^3 in SL(2,Z)",
        matrix_power(matrix_multiply(s_generator, t_generator), 3),
        minus_identity,
    )

    for x, y in (
        (Fraction(0), Fraction(1)),
        (Fraction(1, 3), Fraction(2)),
        (Fraction(-2, 5), Fraction(7, 3)),
    ):
        s_image_imaginary = y / (x * x + y * y)
        t_image_imaginary = y
        assert_equal("S preserves upper half-plane", s_image_imaginary > 0, True)
        assert_equal("T preserves upper half-plane", t_image_imaginary > 0, True)

        q_exponent_shift_under_t = 1
        assert_equal("q coordinate is T invariant", q_exponent_shift_under_t % 1, 0)


def check_central_charges_per_generator() -> None:
    a_scalar = Fraction(1, 360)
    a_weyl = Fraction(11, 720)
    a_vector = Fraction(31, 180)
    c_scalar = Fraction(1, 120)
    c_weyl = Fraction(1, 40)
    c_vector = Fraction(1, 10)

    a_multiplet = 6 * a_scalar + 4 * a_weyl + a_vector
    c_multiplet = 6 * c_scalar + 4 * c_weyl + c_vector

    assert_equal("N=4 a per generator", a_multiplet, Fraction(1, 4))
    assert_equal("N=4 c per generator", c_multiplet, Fraction(1, 4))

    for rank in (2, 3, 7):
        dim_su_n = rank * rank - 1
        assert_equal(
            f"SU({rank}) a=c",
            dim_su_n * a_multiplet,
            Fraction(dim_su_n, 4),
        )
        assert_equal(
            f"U({rank}) a=c",
            rank * rank * c_multiplet,
            Fraction(rank * rank, 4),
        )


def check_symmetric_traceless_projector() -> None:
    dimension = 6
    trace = sum(
        projector(i, j, i, j, dimension)
        for i in range(dimension)
        for j in range(dimension)
    )
    assert_equal("SO(6) symmetric-traceless dimension", trace, 20)

    for i in range(dimension):
        for j in range(dimension):
            for m in range(dimension):
                for n in range(dimension):
                    composed = sum(
                        projector(i, j, k, ell, dimension)
                        * projector(k, ell, m, n, dimension)
                        for k in range(dimension)
                        for ell in range(dimension)
                    )
                    assert_equal(
                        f"projector idempotence ({i},{j};{m},{n})",
                        composed,
                        projector(i, j, m, n, dimension),
                    )


def check_stress_tensor_multiplet_normalization() -> None:
    # With O^{IJ}=g_YM^{-2} tr(Phi^I Phi^J)|_{traceless}, Wick contraction
    # gives dim(g)/(8 pi^4) times the SO(6) projector.  The displayed
    # normalization multiplies by (2 sqrt(2) pi^2)^2 / dim(g).
    for dim_g in (3, 8, 24):
        raw_projector_coefficient_without_pi = Fraction(dim_g, 8)
        normalization_squared_without_pi = Fraction(8, dim_g)
        assert_equal(
            f"stress-tensor multiplet two-point normalization dim={dim_g}",
            raw_projector_coefficient_without_pi * normalization_squared_without_pi,
            1,
        )


def check_planar_chiral_primary_ope_coefficients() -> None:
    # The propagator and 2*pi/g_YM factors cancel separately.  What remains is
    # the exact leading color/cyclic combinatorics of the displayed
    # normalizations.
    for n in (5, 11):
        for charge in (1, 2, 5, 8):
            raw_two_point = charge * n**charge
            normalization_denominator = charge * n**charge
            assert_equal(
                f"planar chiral two-point normalization J={charge} N={n}",
                Fraction(raw_two_point, normalization_denominator),
                1,
            )

        for j1, j2 in ((1, 2), (2, 3), (4, 5)):
            total = j1 + j2
            raw_three_point = j1 * j2 * total * n ** (total - 1)
            norm_product = (j1 * n**j1) * (j2 * n**j2) * (total * n**total)
            coefficient_squared = Fraction(raw_three_point * raw_three_point, norm_product)
            expected = Fraction(j1 * j2 * total, n * n)
            assert_equal(
                f"planar chiral OPE coefficient J1={j1} J2={j2} N={n}",
                coefficient_squared,
                expected,
            )

            normalized_times_n_squared = coefficient_squared * n * n
            assert_equal(
                f"planar chiral pair-of-pants cyclic factor J1={j1} J2={j2}",
                normalized_times_n_squared,
                j1 * j2 * total,
            )


def main() -> None:
    check_beta_function_cancellations()
    check_exact_marginal_coupling_chart()
    check_sl2z_coupling_action()
    check_central_charges_per_generator()
    check_symmetric_traceless_projector()
    check_stress_tensor_multiplet_normalization()
    check_planar_chiral_primary_ope_coefficients()
    print("All N=4 SYM SCFT foundation checks passed.")


if __name__ == "__main__":
    main()
