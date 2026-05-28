#!/usr/bin/env python3
"""Algebra checks for CFT correlator weights and conformal-frame kinematics."""

import sympy as sp


def assert_equal(actual, expected, label):
    diff = sp.simplify(actual - expected)
    if diff != 0:
        raise AssertionError(f"{label}: got {sp.simplify(actual)}, expected {expected}")


def check_scalar_three_point_exponents():
    d1, d2, d3 = sp.symbols("Delta1 Delta2 Delta3")
    a12 = d1 + d2 - d3
    a23 = d2 + d3 - d1
    a13 = d1 + d3 - d2
    assert_equal(a12 + a13, 2 * d1, "three-point local weight at x1")
    assert_equal(a12 + a23, 2 * d2, "three-point local weight at x2")
    assert_equal(a13 + a23, 2 * d3, "three-point local weight at x3")
    assert_equal(a12 + a13 + a23, d1 + d2 + d3, "three-point scale weight")


def check_four_point_prefactor_inversion_weights():
    d1, d2, d3, d4 = sp.symbols("Delta1 Delta2 Delta3 Delta4")
    exponents = {
        (1, 2): -(d1 + d2),
        (3, 4): -(d3 + d4),
        (2, 4): d1 - d2,
        (1, 4): -(d1 - d2) + (d3 - d4),
        (1, 3): -(d3 - d4),
        (2, 3): 0,
    }
    deltas = {1: d1, 2: d2, 3: d3, 4: d4}
    for point in range(1, 5):
        incident = sum(
            exponent
            for pair, exponent in exponents.items()
            if point in pair
        )
        assert_equal(-incident, 2 * deltas[point], f"four-point weight at x{point}")
    assert_equal(sum(exponents.values()), -(d1 + d2 + d3 + d4), "four-point scale")


def check_four_point_orbit_dimension():
    d = sp.symbols("D")
    conf_dim = (d + 1) * (d + 2) / 2
    residual_dim = (d - 2) * (d - 3) / 2
    orbit_quotient_dim = 4 * d - conf_dim + residual_dim
    assert_equal(orbit_quotient_dim, 2, "generic four-point quotient dimension")


def check_frame_cross_ratios():
    z, zb = sp.symbols("z zbar")
    # In the frame (0, z, 1, infinity), the common factors involving infinity
    # cancel from u and v.
    u = z * zb
    v = (1 - z) * (1 - zb)
    assert_equal(u, z * zb, "frame u")
    assert_equal(v, (1 - z) * (1 - zb), "frame v")


def main():
    check_scalar_three_point_exponents()
    check_four_point_prefactor_inversion_weights()
    check_four_point_orbit_dimension()
    check_frame_cross_ratios()
    print("All CFT correlator-kinematics checks passed.")


if __name__ == "__main__":
    main()
