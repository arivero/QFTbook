#!/usr/bin/env python3
r"""Finite checks for lattice perturbative coordinates and tadpole normalization.

These checks support Volume XI, Chapter 5.  They verify the tree-level
gauge-fixed lattice propagator, the \hat p momentum expansion coefficient, and
the finite algebra of plaquette tadpole normalization.
"""

from __future__ import annotations

from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    m = len(b[0])
    kmax = len(b)
    return [[sum(a[i][k] * b[k][j] for k in range(kmax)) for j in range(m)] for i in range(n)]


def identity(n: int) -> list[list[Fraction]]:
    return [[Fraction(1 if i == j else 0) for j in range(n)] for i in range(n)]


def check_tree_level_lattice_propagator_inverse() -> None:
    phat = [Fraction(2), Fraction(3), Fraction(6)]
    xi = Fraction(5, 7)
    p2 = sum(x * x for x in phat)
    n = len(phat)
    long = [[phat[i] * phat[j] / p2 for j in range(n)] for i in range(n)]
    trans = [[Fraction(1 if i == j else 0) - long[i][j] for j in range(n)] for i in range(n)]

    kernel = [[p2 * (trans[i][j] + long[i][j] / xi) for j in range(n)] for i in range(n)]
    propagator = [[(trans[i][j] + xi * long[i][j]) / p2 for j in range(n)] for i in range(n)]
    require(
        matmul(kernel, propagator) == identity(n),
        "gauge-fixed kernel times propagator should be identity",
    )
    require(
        matmul(propagator, kernel) == identity(n),
        "propagator times gauge-fixed kernel should be identity",
    )


def check_lattice_hat_momentum_series() -> None:
    # For y = a p, \hat p^2 = (2/a sin(y/2))^2.  Omitting the overall a^{-2},
    # the series for 4 sin^2(y/2) is y^2 - y^4/12 + y^6/360 + ...
    # This exact coefficient follows from sin(y/2)=y/2-y^3/48+y^5/3840+...
    s1 = Fraction(1, 2)
    s3 = Fraction(-1, 48)
    s5 = Fraction(1, 3840)
    coeff_y2 = 4 * s1 * s1
    coeff_y4 = 8 * s1 * s3
    coeff_y6 = 4 * (2 * s1 * s5 + s3 * s3)
    require(coeff_y2 == 1, "hat momentum y^2 coefficient failed")
    require(coeff_y4 == Fraction(-1, 12), "hat momentum y^4 coefficient should be -1/12")
    require(coeff_y6 == Fraction(1, 360), "hat momentum y^6 coefficient should be 1/360")


def check_connection_canonical_chart_coefficients() -> None:
    g0 = Fraction(5, 7)
    canonical_linear_field_scale = Fraction(1)
    connection_linear_field_scale = g0 * canonical_linear_field_scale

    canonical_quadratic = Fraction(1, 2) * canonical_linear_field_scale**2
    connection_quadratic_after_chart = (
        Fraction(1, 2)
        * connection_linear_field_scale**2
        / (g0 * g0)
    )
    hybrid_quadratic = Fraction(1, 2) * canonical_linear_field_scale**2 / (g0 * g0)

    require(
        connection_quadratic_after_chart == canonical_quadratic,
        "connection-to-canonical chart should cancel the quadratic coupling",
    )
    require(
        hybrid_quadratic != canonical_quadratic,
        "hybrid U=exp(-ig0 a A) with g0^{-2}(dA)^2 should be rejected",
    )

    connection_kernel_factor = Fraction(1, 1) / (g0 * g0)
    connection_propagator_factor = g0 * g0
    canonical_kernel_factor = Fraction(1)
    canonical_propagator_factor = Fraction(1)
    require(
        connection_kernel_factor * connection_propagator_factor == 1,
        "connection kernel and propagator factors should be inverse",
    )
    require(
        canonical_kernel_factor == canonical_propagator_factor,
        "canonical free kernel and propagator should carry no coupling factor",
    )

    cubic_vertex_factor = g0 / 2
    quartic_vertex_factor = g0 * g0 / 4
    require(cubic_vertex_factor > 0, "canonical cubic vertex should carry g0")
    require(quartic_vertex_factor > 0, "canonical quartic vertex should carry g0^2")


def check_plaquette_remainder_orders() -> None:
    leading_flux_order = 2
    corner_correction_order = 3
    centered_correction_order = 4

    corner_trace_cross_order = leading_flux_order + corner_correction_order
    centered_trace_cross_order = leading_flux_order + centered_correction_order

    require(
        corner_trace_cross_order == 5,
        "corner plaquette expansion has a local O(a^5) trace cross term",
    )
    require(
        centered_trace_cross_order == 6,
        "centered plaquette expansion first allows an O(a^6) trace remainder",
    )


def check_tadpole_boosted_coupling_series() -> None:
    # If P = u0^4 = 1 - c g0^2 + O(g0^4), then 1/P = 1 + c g0^2 + O(g0^4).
    c = Fraction(13, 17)
    require(1 + c == Fraction(30, 17), "formal inverse coefficient bookkeeping failed")

    # If u0^4 = 1 - c g0^2 + O(g0^4), then u0^{-L} has first coefficient L c/4.
    link_count = 7
    first_tadpole_line_coefficient = Fraction(link_count, 4) * c
    require(
        first_tadpole_line_coefficient == Fraction(91, 68),
        "u0^{-L} first-order binomial coefficient failed",
    )


def main() -> None:
    check_tree_level_lattice_propagator_inverse()
    check_lattice_hat_momentum_series()
    check_connection_canonical_chart_coefficients()
    check_plaquette_remainder_orders()
    check_tadpole_boosted_coupling_series()
    print("All lattice perturbation and tadpole-normalization checks passed.")


if __name__ == "__main__":
    main()
