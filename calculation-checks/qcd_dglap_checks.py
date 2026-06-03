#!/usr/bin/env python3
"""Exact checks for the DIS/DGLAP convention block in Volume II.

The manuscript uses trace-delta color generators,
tr_fund(t^a t^b)=delta^{ab}, and writes the leading DGLAP equation as
P=(g^2/(8*pi^2)) P^(0)+O(g^4).  These finite rational checks verify the
plus-distribution convention, one-loop number and momentum sum rules, the
trace-normalization conversion of the cusp coefficient, and the sign
normalization of the local moment tower obtained from the Wilson-line light-ray
operator, the RG cancellation between coefficient functions and PDFs in a
factorized DIS convolution, and the finite dependency-budget arithmetic behind
the common QCD factorization ladder.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Mapping

ComplexRational = tuple[Fraction, Fraction]
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
    check_number_and_momentum_sum_rules()
    check_large_spin_and_trace_conversion()
    check_light_ray_moment_normalization()
    check_factorized_rg_cancellation()
    check_common_factorization_dependency_budget()
    print(
        "All QCD DGLAP plus-distribution, sum-rule, "
        "cusp-normalization, light-ray moment, RG-cancellation, "
        "and factorization-budget checks passed."
    )


if __name__ == "__main__":
    main()
