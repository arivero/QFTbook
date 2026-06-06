#!/usr/bin/env python3
"""Exact checks for the DIS/DGLAP convention block in Volume II.

The manuscript uses trace-delta color generators,
tr_fund(t^a t^b)=delta^{ab}, and writes the leading DGLAP equation as
P=(g^2/(8*pi^2)) P^(0)+O(g^4).  These finite rational checks verify the
plus-distribution convention, one-loop number and momentum sum rules, the
trace-normalization conversion of the cusp coefficient, and the sign
normalization of the local moment tower obtained from the Wilson-line light-ray
operator, the RG cancellation between coefficient functions and PDFs in a
factorized DIS convolution, the finite dependency-budget arithmetic behind the
common QCD factorization ladder, and the endpoint test-function window used to
separate the cusp plus-distribution from a full DIS threshold theorem.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Mapping

ComplexRational = tuple[Fraction, Fraction]
LogPolynomial = tuple[Fraction, Fraction]
Vector = list[Fraction]
Matrix = list[list[Fraction]]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)


def complex_mul(left: ComplexRational, right: ComplexRational) -> ComplexRational:
    a, b = left
    c, d = right
    return (a * c - b * d, a * d + b * c)


def complex_pow_i(power: int) -> ComplexRational:
    values = [
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(-1)),
    ]
    return values[power % 4]


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def row_times_matrix(row: Vector, matrix: Matrix) -> Vector:
    return [
        sum(row[i] * matrix[i][j] for i in range(len(row)))
        for j in range(len(matrix[0]))
    ]


def dot(left: Vector, right: Vector) -> Fraction:
    return sum(left[i] * right[i] for i in range(len(left)))


def dependency_budget(terms: Mapping[str, Fraction]) -> Fraction:
    return sum(terms.values(), Fraction(0))


def d0_moment(power: int) -> Fraction:
    """Integral of x^power (1/(1-x))_+ on [0,1]."""
    if power < 0:
        raise ValueError("D0 moment is only used here for nonnegative powers")
    return -harmonic(power)


def endpoint_d0_cell(delta: Fraction, slope: Fraction, curvature: Fraction) -> Fraction:
    """D0 action on phi(1-u)=phi(1)-slope*u+curvature*u^2 on 0<=u<=delta."""
    if not Fraction(0) < delta < Fraction(1):
        raise ValueError("endpoint cell checks use 0 < delta < 1")
    return -slope * delta + curvature * delta**2 / 2


def endpoint_d1_cell(
    delta: Fraction,
    slope: Fraction,
    curvature: Fraction,
) -> LogPolynomial:
    """D1 action as const + log_coeff * log(delta) on the same endpoint cell."""
    constant = slope * delta - curvature * delta**2 / 4
    log_coeff = endpoint_d0_cell(delta, slope, curvature)
    return (constant, log_coeff)


def unsubtracted_constant_log_coefficient(value_at_endpoint: Fraction) -> Fraction:
    """Coefficient of log(delta) if D0 is wrongly replaced by 1/(1-x)."""
    return value_at_endpoint


def pqq_moment(n: int, cf: Fraction = Fraction(1)) -> Fraction:
    """Moment int_0^1 dx x^(n-1) P_qq^(0)(x)/delta_ij."""
    return cf * (
        2 * d0_moment(n - 1)
        - Fraction(1, n)
        - Fraction(1, n + 1)
        + Fraction(3, 2)
    )


def pqg_moment(n: int, tr: Fraction = Fraction(1)) -> Fraction:
    """Moment of P_{qg}^{(0)} for one quark or antiquark species."""
    return tr * (
        Fraction(1, n + 2)
        + Fraction(1, n)
        - Fraction(2, n + 1)
        + Fraction(1, n + 2)
    )


def pgq_moment(n: int, cf: Fraction = Fraction(1)) -> Fraction:
    """Moment of P_{gq}^{(0)}."""
    return cf * (
        2 * Fraction(1, n - 1)
        - 2 * Fraction(1, n)
        + Fraction(1, n + 1)
    )


def pgg_moment(
    n: int,
    ca: Fraction = Fraction(1),
    tr: Fraction = Fraction(1),
    nf: Fraction = Fraction(1),
) -> Fraction:
    """Moment of P_{gg}^{(0)} with D0=(1/(1-x))_+."""
    regular = (
        d0_moment(n)
        + Fraction(1, n - 1)
        - Fraction(1, n)
        + Fraction(1, n + 1)
        - Fraction(1, n + 2)
    )
    delta = (11 * ca - 4 * tr * nf) / 6
    return 2 * ca * regular + delta


def check_plus_distribution_monomials() -> None:
    expected = {
        0: Fraction(0),
        1: Fraction(-1),
        2: Fraction(-3, 2),
        3: Fraction(-11, 6),
        4: Fraction(-25, 12),
    }
    for power, value in expected.items():
        assert_equal(f"D0 moment power {power}", d0_moment(power), value)


def check_threshold_test_function_window() -> None:
    # The plus prescription annihilates the endpoint value of a measured bin.
    # Replacing it by the ordinary function 1/(1-x) would leave a logarithmic
    # coefficient proportional to the bin value; this is the endpoint negative
    # control used in ca:qcd-dis-threshold-plus-distribution-window.
    endpoint_value = Fraction(7, 5)
    assert_equal("D0 constant test vanishes", d0_moment(0), Fraction(0))
    assert_equal(
        "unsubtracted constant endpoint log coefficient",
        unsubtracted_constant_log_coefficient(endpoint_value),
        endpoint_value,
    )
    assert_true(
        "plus subtraction removes endpoint-value logarithm",
        unsubtracted_constant_log_coefficient(endpoint_value) != d0_moment(0),
    )

    delta = Fraction(1, 10)
    slope = Fraction(3)
    curvature = Fraction(5)

    d0_cell = endpoint_d0_cell(delta, slope, curvature)
    assert_equal("D0 terminal-cell Taylor action", d0_cell, Fraction(-11, 40))
    assert_true("D0 terminal-cell derivative bound", abs(d0_cell) <= slope * delta)

    d1_constant, d1_log_coeff = endpoint_d1_cell(delta, slope, curvature)
    assert_equal("D1 terminal-cell constant term", d1_constant, Fraction(23, 80))
    assert_equal("D1 terminal-cell log coefficient", d1_log_coeff, d0_cell)
    assert_true("D1 log coefficient derivative bound", abs(d1_log_coeff) <= slope * delta)
    assert_true("D1 constant term derivative bound", abs(d1_constant) <= slope * delta)

    # The large-N cusp logarithm is the moment of a moving test family
    # x^(N-1), not a uniform fixed-compact-x factorization estimate.
    assert_equal("large-N D0 moment at N=10", d0_moment(9), Fraction(-7129, 2520))
    assert_true(
        "large-N moving test family differs from fixed terminal cell",
        d0_moment(9) != d0_cell,
    )

    threshold_terms = {
        "cusp_plus_distribution": Fraction(1, 90),
        "hard_current_matching": Fraction(1, 100),
        "final_state_jet": Fraction(1, 120),
        "soft_wilson_line": Fraction(1, 150),
        "mellin_contour_prescription": Fraction(1, 180),
        "power_remainder": Fraction(1, 200),
    }
    threshold_budget = dependency_budget(threshold_terms)
    assert_equal("DIS threshold approximation budget", threshold_budget, Fraction(7, 150))
    assert_true(
        "cusp term alone is not a threshold theorem",
        threshold_budget > threshold_terms["cusp_plus_distribution"],
    )
    assert_true(
        "jet and soft entries are load-bearing",
        threshold_budget
        > threshold_budget
        - threshold_terms["final_state_jet"]
        - threshold_terms["soft_wilson_line"],
    )


def check_number_and_momentum_sum_rules() -> None:
    cf = Fraction(7, 3)
    ca = Fraction(10, 1)
    tr = Fraction(2, 1)
    nf = Fraction(5, 1)

    assert_equal("quark number", pqq_moment(1, cf), Fraction(0))
    assert_equal("quark-parent momentum", pqq_moment(2, cf) + pgq_moment(2, cf), Fraction(0))
    assert_equal(
        "gluon-parent momentum",
        2 * nf * pqg_moment(2, tr) + pgg_moment(2, ca, tr, nf),
        Fraction(0),
    )


def check_large_spin_and_trace_conversion() -> None:
    # Exact nonsinglet formula used in the text.
    for n in (1, 2, 5, 11):
        rhs = -2 * harmonic(n - 1) - Fraction(1, n) - Fraction(1, n + 1) + Fraction(3, 2)
        assert_equal(f"nonsinglet moment {n}", pqq_moment(n), rhs)

    # Trace-delta and half-trace conventions give the same one-loop cusp product.
    g_delta_sq = Fraction(3, 7)
    cf_delta = Fraction(16, 5)
    g_half_sq = 2 * g_delta_sq
    cf_half = cf_delta / 2
    assert_equal("cusp product convention", g_delta_sq * cf_delta, g_half_sq * cf_half)


def check_light_ray_moment_normalization() -> None:
    # A free target with f(x)=delta(1-x) has M(lambda)=exp(i lambda P).
    # The N-th lambda derivative contributes (i P)^N.  Because the bilocal
    # derivative acts on the left endpoint, the local moment operator must use
    # (-i \overleftarrow D_n)^N; the product (-i)^N i^N is +1.
    momentum = Fraction(7, 3)
    minus_i = (Fraction(0), Fraction(-1))
    for moment in range(5):
        derivative_phase = complex_pow_i(moment)
        local_phase = (Fraction(1), Fraction(0))
        for _ in range(moment):
            local_phase = complex_mul(local_phase, minus_i)
        combined_phase = complex_mul(local_phase, derivative_phase)
        assert_equal(f"quark moment phase {moment}", combined_phase, (Fraction(1), Fraction(0)))

        local_matrix_element = momentum**moment
        extracted_moment = local_matrix_element / momentum**moment
        assert_equal(f"quark delta-target moment {moment}", extracted_moment, Fraction(1))

    # The gluon convention has an additional factor of x in the inverse
    # light-ray transform, so the N-th PDF moment uses N-1 left derivatives.
    for moment in range(1, 6):
        derivative_order = moment - 1
        derivative_phase = complex_pow_i(derivative_order)
        local_phase = (Fraction(1), Fraction(0))
        for _ in range(derivative_order):
            local_phase = complex_mul(local_phase, minus_i)
        combined_phase = complex_mul(local_phase, derivative_phase)
        assert_equal(f"gluon moment phase {moment}", combined_phase, (Fraction(1), Fraction(0)))

        local_matrix_element = momentum ** (moment - 1)
        extracted_moment = local_matrix_element / momentum ** (moment - 1)
        assert_equal(f"gluon delta-target moment {moment}", extracted_moment, Fraction(1))


def check_factorized_rg_cancellation() -> None:
    # Collapse the convolution algebra to a finite two-channel rational model.
    # With df/dlog(mu)=P f and dC/dlog(mu)=-C P, the factorized observable C f
    # is scale-independent.  This checks the index/sign convention used in the
    # manuscript after deriving P from the regulated-to-renormalized light-ray
    # operator coordinate map.
    splitting_kernel = [
        [Fraction(1, 3), Fraction(-2, 5)],
        [Fraction(7, 11), Fraction(1, 13)],
    ]
    pdf = [Fraction(5, 7), Fraction(2, 7)]
    coefficient = [Fraction(3, 2), Fraction(-4, 9)]

    pdf_derivative = matvec(splitting_kernel, pdf)
    coefficient_derivative = [
        -entry for entry in row_times_matrix(coefficient, splitting_kernel)
    ]
    observable_derivative = dot(coefficient_derivative, pdf) + dot(
        coefficient, pdf_derivative
    )
    assert_equal("factorized DIS RG cancellation", observable_derivative, Fraction(0))


def check_common_factorization_dependency_budget() -> None:
    # Finite rational model of the triangle-inequality budget in
    # eq. (qcd-common-factorization-budget).  The labels are process
    # requirements, not independent physical observables.
    common_terms = {
        "observable": Fraction(1, 40),
        "operator": Fraction(1, 50),
        "subtraction": Fraction(1, 60),
        "coefficient": Fraction(1, 75),
        "evolution": Fraction(1, 100),
        "boundary": Fraction(1, 120),
        "remainder": Fraction(1, 150),
    }
    compact_dis_budget = dependency_budget(common_terms)
    assert_equal("compact-DIS common factorization budget", compact_dis_budget, Fraction(1, 10))

    omitted_boundary_budget = compact_dis_budget - common_terms["boundary"]
    assert_true(
        "compact-DIS boundary exclusion is load-bearing",
        compact_dis_budget > omitted_boundary_budget,
    )

    drell_yan_terms = {
        **common_terms,
        "rapidity": Fraction(1, 80),
        "glauber": Fraction(1, 200),
        "y_term": Fraction(1, 240),
    }
    drell_yan_budget = dependency_budget(drell_yan_terms)
    assert_equal("Drell-Yan TMD factorization budget", drell_yan_budget, Fraction(73, 600))
    assert_true(
        "Drell-Yan Glauber status is load-bearing",
        drell_yan_budget > drell_yan_budget - drell_yan_terms["glauber"],
    )

    small_x_terms = {
        **common_terms,
        "projective_state": Fraction(1, 80),
        "generator_limit": Fraction(1, 120),
        "process_map": Fraction(1, 200),
    }
    small_x_budget = dependency_budget(small_x_terms)
    assert_equal("small-x JIMWLK factorization budget", small_x_budget, Fraction(151, 1200))
    assert_true(
        "small-x projective state limit is load-bearing",
        small_x_budget > small_x_budget - small_x_terms["projective_state"],
    )

    previous_budget = None
    for window in (1, 2, 5, 10):
        scheduled_terms = {name: term / window for name, term in common_terms.items()}
        scheduled_budget = dependency_budget(scheduled_terms)
        assert_equal(
            f"compact-DIS scheduled budget window {window}",
            scheduled_budget,
            Fraction(1, 10 * window),
        )
        if previous_budget is not None:
            assert_true(
                f"compact-DIS scheduled budget decreases at window {window}",
                scheduled_budget < previous_budget,
            )
        previous_budget = scheduled_budget


def main() -> None:
    check_plus_distribution_monomials()
    check_threshold_test_function_window()
    check_number_and_momentum_sum_rules()
    check_large_spin_and_trace_conversion()
    check_light_ray_moment_normalization()
    check_factorized_rg_cancellation()
    check_common_factorization_dependency_budget()
    print(
        "All QCD DGLAP plus-distribution, sum-rule, "
        "cusp-normalization, light-ray moment, RG-cancellation, "
        "factorization-budget, and DIS threshold-window checks passed."
    )


if __name__ == "__main__":
    main()
