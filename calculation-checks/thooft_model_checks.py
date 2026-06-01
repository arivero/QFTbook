#!/usr/bin/env python3
"""Exact finite checks for the large-N two-dimensional QCD chapter.

The chapter uses the subtracted 't Hooft kernel

    PV int (phi(x)-phi(y))/(x-y)^2 dy

and its DLCQ finite matrix. These checks use rational arithmetic to verify
the color normalization, the finite quadratic-form identity, positivity in a
sample positive-mass case, the exact constant zero mode in the massless
subtracted kernel, the endpoint-exponent small-mass expansion in the
subtracted finite-part convention, and finite-form monotonicity shadows of
the continuum closed-form spectral construction.
"""

from fractions import Fraction


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_true(name, condition):
    if not condition:
        raise AssertionError(name)


def casimir_fund_trace_delta(nc):
    return Fraction(nc * nc - 1, nc)


def check_trace_delta_color_normalization():
    for nc in range(2, 9):
        cf = casimir_fund_trace_delta(nc)
        planar = Fraction(nc, 1)
        trace_subtraction = Fraction(1, nc)
        assert_equal(f"C_F decomposition N={nc}", cf, planar - trace_subtraction)


def thooft_matrix(k, m1_sq, m2_sq, gamma):
    size = k - 1
    matrix = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    xs = [Fraction(n, k) for n in range(1, k)]
    for n in range(size):
        diagonal = m1_sq / xs[n] + m2_sq / (1 - xs[n])
        diagonal += gamma * k * sum(
            Fraction(1, (n - j) * (n - j))
            for j in range(size)
            if j != n
        )
        matrix[n][n] = diagonal
        for m in range(size):
            if m != n:
                matrix[n][m] = -gamma * k * Fraction(1, (n - m) * (n - m))
    return matrix


def quadratic_form(matrix, vector):
    return sum(
        vector[i] * matrix[i][j] * vector[j]
        for i in range(len(vector))
        for j in range(len(vector))
    )


def displayed_quadratic_form(k, m1_sq, m2_sq, gamma, vector):
    xs = [Fraction(n, k) for n in range(1, k)]
    mass = sum(
        (m1_sq / xs[n] + m2_sq / (1 - xs[n])) * vector[n] * vector[n]
        for n in range(k - 1)
    )
    kernel = sum(
        gamma * k * (vector[n] - vector[m]) ** 2 / Fraction((n - m) * (n - m), 1)
        for n in range(k - 1)
        for m in range(n + 1, k - 1)
    )
    return mass + kernel


def matrix_vector(matrix, vector):
    return [
        sum(matrix[i][j] * vector[j] for j in range(len(vector)))
        for i in range(len(vector))
    ]


def check_dlcq_quadratic_form_identity():
    k = 8
    m1_sq = Fraction(2, 5)
    m2_sq = Fraction(3, 7)
    gamma = Fraction(11, 13)
    vector = tuple(Fraction((-1) ** n * (n + 2), 9) for n in range(k - 1))
    matrix = thooft_matrix(k, m1_sq, m2_sq, gamma)
    assert_equal(
        "finite 't Hooft quadratic form",
        quadratic_form(matrix, vector),
        displayed_quadratic_form(k, m1_sq, m2_sq, gamma, vector),
    )


def check_positive_mass_sample_positive():
    k = 7
    matrix = thooft_matrix(k, Fraction(1, 3), Fraction(1, 4), Fraction(5, 6))
    vector = tuple(Fraction(n + 1, 5) for n in range(k - 1))
    assert_true("positive endpoint-mass form", quadratic_form(matrix, vector) > 0)


def check_massless_constant_zero_mode():
    k = 9
    matrix = thooft_matrix(k, Fraction(0), Fraction(0), Fraction(7, 5))
    constant = tuple(Fraction(1) for _ in range(k - 1))
    assert_equal("massless constant kernel zero mode", matrix_vector(matrix, constant), [Fraction(0)] * (k - 1))
    assert_equal("massless constant quadratic form", quadratic_form(matrix, constant), Fraction(0))


def check_endpoint_exponent_series():
    # The endpoint equation in the subtracted convention is
    #   r := m^2/gamma = 1 - pi beta cot(pi beta).
    # With z=(pi beta)^2,
    #   r = z/3 + z^2/45 + 2 z^3/945 + O(z^4).
    # Formal inversion gives
    #   z = 3 r - 3 r^2/5 + 12 r^3/175 + O(r^4).
    endpoint_series = {
        1: Fraction(1, 3),
        2: Fraction(1, 45),
        3: Fraction(2, 945),
    }
    inverse_series = {
        1: Fraction(3, 1),
        2: Fraction(-3, 5),
        3: Fraction(12, 175),
    }
    a = inverse_series[1]
    b = inverse_series[2]
    c = inverse_series[3]
    assert_equal("endpoint inverse linear coefficient", endpoint_series[1] * a, Fraction(1))
    assert_equal(
        "endpoint inverse quadratic coefficient",
        endpoint_series[1] * b + endpoint_series[2] * a * a,
        Fraction(0),
    )
    assert_equal(
        "endpoint inverse cubic coefficient",
        endpoint_series[1] * c
        + 2 * endpoint_series[2] * a * b
        + endpoint_series[3] * a * a * a,
        Fraction(0),
    )


def check_finite_form_monotonicity_shadow():
    # The continuum closed form is monotone in each nonnegative coordinate
    # m_1^2, m_2^2, and gamma_2.  The DLCQ matrix has the same exact
    # quadratic-form difference: mass-coordinate increments plus the
    # positive subtracted-kernel increment.
    k = 8
    base_m1 = Fraction(1, 7)
    base_m2 = Fraction(2, 9)
    base_gamma = Fraction(3, 11)
    delta_m1 = Fraction(5, 13)
    delta_m2 = Fraction(7, 17)
    delta_gamma = Fraction(2, 19)
    vector = tuple(Fraction((n + 1) * (-1 if n % 2 else 1), 10) for n in range(k - 1))

    base = thooft_matrix(k, base_m1, base_m2, base_gamma)
    higher = thooft_matrix(
        k,
        base_m1 + delta_m1,
        base_m2 + delta_m2,
        base_gamma + delta_gamma,
    )
    diff = quadratic_form(higher, vector) - quadratic_form(base, vector)
    expected = displayed_quadratic_form(k, delta_m1, delta_m2, delta_gamma, vector)
    assert_equal("finite form monotonicity exact difference", diff, expected)
    assert_true("finite form monotonicity positivity", diff > 0)


def main():
    check_trace_delta_color_normalization()
    check_dlcq_quadratic_form_identity()
    check_positive_mass_sample_positive()
    check_massless_constant_zero_mode()
    check_endpoint_exponent_series()
    check_finite_form_monotonicity_shadow()
    print("All large-N two-dimensional QCD checks passed.")


if __name__ == "__main__":
    main()
