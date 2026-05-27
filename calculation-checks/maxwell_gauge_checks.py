#!/usr/bin/env python3
"""Exact checks for Maxwell gauge-fixing and photon-helicity algebra.

The Maxwell chapter contains sign-sensitive formulas: mostly-plus quadratic
operators, axial and covariant gauge inverses, the finite Faddeev--Popov slice
Jacobian, Gupta--Bleuler null vectors, and cancellation of longitudinal terms
from field-strength correlators.  This script checks those finite algebraic
pieces with rational arithmetic.
"""

from fractions import Fraction


ETA = [Fraction(-1), Fraction(1), Fraction(1), Fraction(1)]


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: got {actual}, expected {expected}")


def metric(i, j):
    return ETA[i] if i == j else Fraction(0)


def lower(v):
    return [ETA[i] * v[i] for i in range(4)]


def dot_up_lower(v_up, w_down):
    return sum(v_up[i] * w_down[i] for i in range(4))


def dot_up_up(v, w):
    return sum(ETA[i] * v[i] * w[i] for i in range(4))


def matmul_upper_lower(d_upper, inv_lower, indices):
    out = []
    for mu in indices:
        row = []
        for nu in indices:
            row.append(sum(d_upper[mu][rho] * inv_lower[rho][nu] for rho in indices))
        out.append(row)
    return out


def check_axial_inverse():
    k_up = [Fraction(5), Fraction(2), Fraction(3), Fraction(7)]
    k_down = lower(k_up)
    k2 = dot_up_up(k_up, k_up)
    assert_equal(k2, Fraction(37), "sample axial momentum has nonzero k^2")

    d_upper = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    inv_lower = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for mu in range(4):
        for nu in range(4):
            d_upper[mu][nu] = -metric(mu, nu) * k2 + k_up[mu] * k_up[nu]
            inv_lower[mu][nu] = -(metric(mu, nu) + k_down[mu] * k_down[nu] / (k_up[3] ** 2)) / k2

    product = matmul_upper_lower(d_upper, inv_lower, [0, 1, 2])
    identity = [[Fraction(int(i == j)) for j in range(3)] for i in range(3)]
    assert_equal(product, identity, "axial 3x3 quadratic inverse")


def check_covariant_inverse():
    k_up = [Fraction(5), Fraction(2), Fraction(3), Fraction(7)]
    k_down = lower(k_up)
    k2 = dot_up_up(k_up, k_up)
    xi = Fraction(3)

    d_upper = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    inv_lower = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for mu in range(4):
        for nu in range(4):
            d_upper[mu][nu] = (
                -metric(mu, nu) * k2
                + (1 - Fraction(1, 1) / xi) * k_up[mu] * k_up[nu]
            )
            inv_lower[mu][nu] = (
                -metric(mu, nu) / k2
                + (1 - xi) * k_down[mu] * k_down[nu] / (k2 * k2)
            )

    product = matmul_upper_lower(d_upper, inv_lower, [0, 1, 2, 3])
    identity = [[Fraction(int(i == j)) for j in range(4)] for i in range(4)]
    assert_equal(product, identity, "covariant gauge quadratic inverse")


def field_strength_kernel(k_down, p_lower, mu, nu, rho, sigma):
    return (
        k_down[mu] * k_down[rho] * p_lower[nu][sigma]
        - k_down[nu] * k_down[rho] * p_lower[mu][sigma]
        - k_down[mu] * k_down[sigma] * p_lower[nu][rho]
        + k_down[nu] * k_down[sigma] * p_lower[mu][rho]
    )


def check_longitudinal_cancellation():
    k_up = [Fraction(5), Fraction(2), Fraction(3), Fraction(7)]
    k_down = lower(k_up)
    longitudinal = [[k_down[mu] * k_down[nu] for nu in range(4)] for mu in range(4)]
    for mu in range(4):
        for nu in range(4):
            for rho in range(4):
                for sigma in range(4):
                    value = field_strength_kernel(k_down, longitudinal, mu, nu, rho, sigma)
                    assert_equal(value, Fraction(0), "longitudinal field-strength cancellation")


def check_helicity_completeness_c_cancellation():
    k_up = [Fraction(1), Fraction(0), Fraction(0), Fraction(1)]
    k_down = lower(k_up)
    c_up = [Fraction(1, 2), Fraction(0), Fraction(0), Fraction(-1, 2)]
    c_down = lower(c_up)
    assert_equal(dot_up_up(k_up, k_up), Fraction(0), "null k")
    assert_equal(dot_up_up(c_up, c_up), Fraction(0), "null C")
    assert_equal(dot_up_lower(k_up, c_down), Fraction(-1), "k dot C normalization")

    eta_lower = [[metric(mu, nu) for nu in range(4)] for mu in range(4)]
    projector = [
        [
            eta_lower[mu][nu] + k_down[mu] * c_down[nu] + k_down[nu] * c_down[mu]
            for nu in range(4)
        ]
        for mu in range(4)
    ]

    for mu in range(4):
        for nu in range(4):
            for rho in range(4):
                for sigma in range(4):
                    with_c = field_strength_kernel(k_down, projector, mu, nu, rho, sigma)
                    no_c = field_strength_kernel(k_down, eta_lower, mu, nu, rho, sigma)
                    assert_equal(with_c, no_c, "C-dependent helicity-completeness cancellation")


def check_faddeev_popov_slice_model():
    a = Fraction(2)
    b = Fraction(3)
    x = Fraction(5)
    y = -a * x - b
    u = x - y
    slice_coordinate = (1 + a) * x + b
    fp_derivative = 1 + a
    assert_equal(u, slice_coordinate, "finite FP slice invariant coordinate")
    assert_equal(fp_derivative, Fraction(3), "finite FP slice derivative")


def check_gupta_bleuler_null_quotient():
    k_up = [Fraction(1), Fraction(0), Fraction(0), Fraction(1)]
    k_down = lower(k_up)
    f_down = [Fraction(-4), Fraction(2), Fraction(3), Fraction(4)]
    h = Fraction(7)
    gauge_down = [h * component for component in k_down]
    assert_equal(dot_up_lower(k_up, f_down), Fraction(0), "mass-shell Lorenz condition")

    norm_gauge = sum(metric(mu, nu) * gauge_down[mu] * gauge_down[nu] for mu in range(4) for nu in range(4))
    inner_gauge_f = sum(metric(mu, nu) * gauge_down[mu] * f_down[nu] for mu in range(4) for nu in range(4))
    norm_f = sum(metric(mu, nu) * f_down[mu] * f_down[nu] for mu in range(4) for nu in range(4))
    assert_equal(norm_gauge, Fraction(0), "gauge vector is null")
    assert_equal(inner_gauge_f, Fraction(0), "gauge vector is orthogonal to GB subspace")
    assert_equal(norm_f, Fraction(13), "GB quotient leaves positive transverse norm")


def main():
    check_axial_inverse()
    check_covariant_inverse()
    check_longitudinal_cancellation()
    check_helicity_completeness_c_cancellation()
    check_faddeev_popov_slice_model()
    check_gupta_bleuler_null_quotient()
    print("All Maxwell gauge-fixing and photon-helicity checks passed.")


if __name__ == "__main__":
    main()
