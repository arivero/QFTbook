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
    # The raw planar extremal three-point combinatorics is
    # J1 * J2 * J * N^(J-1), with J=J1+J2.  Dividing by normalized two-point
    # factors J1 N^J1, J2 N^J2, and J N^J leaves J1 J2 J / N^2.
    for n in (5, 11):
        for j1, j2 in ((1, 2), (2, 3), (4, 5)):
            total = j1 + j2
            raw_squared = (j1 * j2 * total) ** 2 * n ** (2 * total - 2)
            norm_product = (j1 * n**j1) * (j2 * n**j2) * (total * n**total)
            coefficient_squared = Fraction(raw_squared, norm_product)
            expected = Fraction(j1 * j2 * total, n * n)
            assert_equal(
                f"planar chiral OPE coefficient J1={j1} J2={j2} N={n}",
                coefficient_squared,
                expected,
            )


def main() -> None:
    check_beta_function_cancellations()
    check_central_charges_per_generator()
    check_symmetric_traceless_projector()
    check_stress_tensor_multiplet_normalization()
    check_planar_chiral_primary_ope_coefficients()
    print("All N=4 SYM SCFT foundation checks passed.")


if __name__ == "__main__":
    main()
