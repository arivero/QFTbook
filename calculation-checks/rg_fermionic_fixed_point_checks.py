#!/usr/bin/env python3
"""Exact checks for the fermionic rigorous-RG benchmark.

These checks verify the finite scaling-dimension and irrelevant-tail
bookkeeping used in Volume XI, Chapter 7 for the long-range fermionic
fixed-point benchmark.  They do not reproduce the constructive determinant
expansion; they check the algebraic ledger that the manuscript uses to state
the theorem boundary.
"""

from fractions import Fraction


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_true(name, condition):
    if not condition:
        raise AssertionError(name)


def dsc(dimension, psi_dim, delta_1, delta_2, n, m, ell, derivative_count):
    """Kernel scaling exponent D_sc(n,m,ell,p).

    Here delta_1 and delta_2 are the operator dimensions; the source fields
    coupled to those operators have dimensions dimension-delta_i.
    """
    return (
        dimension
        - n * (dimension - delta_1)
        - m * (dimension - delta_2)
        - ell * psi_dim
        - derivative_count
    )


def check_fermionic_relevance_ledger():
    d = Fraction(3)
    epsilon = Fraction(1, 10)
    psi = d / 4 - epsilon / 2
    delta_1 = psi
    delta_2 = 2 * psi

    assert_equal("fermion dimension", psi, Fraction(7, 10))
    assert_equal(
        "mass bilinear exponent",
        dsc(d, psi, delta_1, delta_2, 0, 0, 2, 0),
        d / 2 + epsilon,
    )
    assert_equal(
        "quartic exponent",
        dsc(d, psi, delta_1, delta_2, 0, 0, 4, 0),
        2 * epsilon,
    )
    assert_equal(
        "source-field local coordinate exponent",
        dsc(d, psi, delta_1, delta_2, 1, 0, 1, 0),
        delta_1 - psi,
    )
    assert_equal(
        "density-source local coordinate exponent",
        dsc(d, psi, delta_1, delta_2, 0, 1, 2, 0),
        delta_2 - 2 * psi,
    )
    assert_equal(
        "first-derivative bilinear exponent",
        dsc(d, psi, delta_1, delta_2, 0, 0, 2, 1),
        d / 2 + epsilon - 1,
    )
    assert_true(
        "six-fermion coordinate is irrelevant in this bookkeeping",
        dsc(d, psi, delta_1, delta_2, 0, 0, 6, 0) < 0,
    )


def check_kernel_l1_scaling_relation():
    d = Fraction(3)
    epsilon = Fraction(1, 10)
    psi = d / 4 - epsilon / 2
    delta_1 = psi
    delta_2 = 2 * psi

    # delta_sc is the pointwise kernel scaling exponent before subtracting the
    # volume of all but one integrated variable.  The pinned L1 exponent is
    # delta_sc - d*(total_variables - 1).
    n, m, ell, derivative_count = 2, 1, 2, 1
    total_variables = n + m + ell
    delta_sc = (
        d * total_variables
        - n * (d - delta_1)
        - m * (d - delta_2)
        - ell * psi
        - derivative_count
    )
    pinned_l1_exponent = delta_sc - d * (total_variables - 1)
    assert_equal(
        "pinned L1 exponent equals D_sc",
        pinned_l1_exponent,
        dsc(d, psi, delta_1, delta_2, n, m, ell, derivative_count),
    )


def check_trimmed_local_coordinate_set():
    local_coordinates = {
        (0, 0, 2, 0),
        (0, 0, 4, 0),
        (1, 0, 1, 0),
        (0, 1, 2, 0),
        (0, 0, 2, 1),
    }
    assert_true("quartic is trimmed local", (0, 0, 4, 0) in local_coordinates)
    assert_true("source-field is trimmed local", (1, 0, 1, 0) in local_coordinates)
    assert_true("density-source is trimmed local", (0, 1, 2, 0) in local_coordinates)
    assert_true(
        "generic six-fermion term is not a local trimmed coordinate",
        (0, 0, 6, 0) not in local_coordinates,
    )


def check_irrelevant_tail_fixed_point_equation():
    # Finite model of K = A_irr K + B_irr(g,K) with contraction |A_irr|<1.
    a_irr = Fraction(2, 5)
    g = Fraction(1, 20)
    quadratic_source = g * g
    k_star = quadratic_source / (1 - a_irr)
    assert_equal(
        "irrelevant tail graph solves fixed-point equation",
        a_irr * k_star + quadratic_source - k_star,
        Fraction(0),
    )

    projected_tail_residual = quadratic_source
    assert_true(
        "projected local equation misses nonzero irrelevant residual",
        projected_tail_residual != 0,
    )
    assert_equal(
        "tail solution differs from dropped-tail truncation",
        k_star,
        Fraction(1, 240),
    )


def main():
    check_fermionic_relevance_ledger()
    check_kernel_l1_scaling_relation()
    check_trimmed_local_coordinate_set()
    check_irrelevant_tail_fixed_point_equation()
    print("All fermionic rigorous-RG benchmark checks passed.")


if __name__ == "__main__":
    main()
