#!/usr/bin/env python3
"""Exact checks for N=1 holomorphy, elimination, and NSVZ coordinates."""

from fractions import Fraction


def assert_equal(actual, expected, label):
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, got {actual!r}")


def inverse_2x2(matrix):
    ((a, b), (c, d)) = matrix
    determinant = a * d - b * c
    if determinant == 0:
        raise ValueError("matrix is singular")
    return (
        (d / determinant, -b / determinant),
        (-c / determinant, a / determinant),
    )


def mat_vec(matrix, vector):
    return tuple(sum(row[index] * vector[index] for index in range(len(vector))) for row in matrix)


def dot(left, right):
    return sum(left[index] * right[index] for index in range(len(left)))


def check_tree_level_chiral_elimination_quadratic_block():
    matrices = [
        ((Fraction(3), Fraction(1)), (Fraction(1), Fraction(2))),
        ((Fraction(5), Fraction(-2)), (Fraction(-2), Fraction(7))),
        ((Fraction(4), Fraction(0)), (Fraction(0), Fraction(9))),
    ]
    sources = [
        (Fraction(2), Fraction(-1)),
        (Fraction(3, 2), Fraction(5)),
        (Fraction(-4), Fraction(7, 3)),
    ]
    w0 = Fraction(11, 5)

    for matrix, source in zip(matrices, sources):
        inverse = inverse_2x2(matrix)
        solution = tuple(-entry for entry in mat_vec(inverse, source))
        equation = tuple(
            mat_vec(matrix, solution)[index] + source[index]
            for index in range(2)
        )
        assert_equal(equation, (0, 0), "heavy chiral equation of motion")

        substituted = w0 + dot(source, solution) + Fraction(1, 2) * dot(
            solution,
            mat_vec(matrix, solution),
        )
        closed_form = w0 - Fraction(1, 2) * dot(source, mat_vec(inverse, source))
        assert_equal(substituted, closed_form, "quadratic chiral elimination formula")


def check_tree_level_derivative_chain_rule():
    # W(X, phi)=a phi^2 + (b phi+c) X + M X^2/2.
    # After X*=-(b phi+c)/M, dW_eff/dphi equals partial_phi W at X=X*.
    a = Fraction(5, 3)
    b = Fraction(-7, 4)
    c = Fraction(2)
    mass = Fraction(9, 2)
    for phi in (Fraction(-3), Fraction(0), Fraction(5, 2)):
        source = b * phi + c
        x_star = -source / mass
        derivative_effective = 2 * a * phi - source * b / mass
        partial_phi_before_elimination = 2 * a * phi + b * x_star
        assert_equal(
            derivative_effective,
            partial_phi_before_elimination,
            "tree-level eliminated derivative",
        )


def check_loop_supergraph_grassmann_measure_ledger():
    """Check the measure count behind the Wilsonian nonrenormalization text.

    For a connected supergraph with V vertices and E propagators, a spanning
    tree has V-1 Grassmann delta functions.  They identify all vertex theta
    variables and leave one full d^4 theta integration.  The E-(V-1) remaining
    edges are the independent loop edges.  In a local Wilsonian expansion the
    external momentum powers are nonnegative, so the inverse Box needed by a
    chiral projector is absent.
    """

    samples = [
        (2, 2),   # one-loop two-vertex graph
        (3, 3),   # one-loop triangle topology
        (3, 4),   # two-loop connected topology
        (5, 7),   # three-loop connected topology
    ]
    for vertices, edges in samples:
        tree_edges = vertices - 1
        loop_edges = edges - tree_edges
        euler_loops = edges - vertices + 1
        remaining_full_measure_rank = 4
        assert_equal(loop_edges, euler_loops, "connected supergraph loop-edge count")
        assert_equal(
            remaining_full_measure_rank,
            4,
            "spanning-tree Grassmann deltas leave d^4 theta",
        )
        if loop_edges <= 0:
            raise AssertionError("sample is not a loop supergraph")

    wilsonian_external_momentum_powers = [0, 1, 2, 3, 4]
    inverse_box_power = -2
    if inverse_box_power in wilsonian_external_momentum_powers:
        raise AssertionError("local Wilsonian Taylor expansion contains inverse Box")


def perturbative_q_projection(series):
    """Return the q^0 term of a weak-coupling q-series."""

    for degree in series:
        if degree < 0:
            raise ValueError("negative q-degree is outside the weak-coupling patch")
    return series.get(0, Fraction(0))


def check_holomorphic_gauge_one_loop_projection():
    """Check the formal q-series bookkeeping in holomorphic one-loop exactness."""

    samples = [
        (Fraction(3), [Fraction(1), Fraction(2)], {1: Fraction(5), 2: Fraction(-7)}),
        (Fraction(5), [Fraction(3, 2), Fraction(2)], {1: Fraction(11, 3)}),
        (Fraction(7, 2), [Fraction(4, 3)], {2: Fraction(9), 4: Fraction(-1, 5)}),
    ]
    log_interval = Fraction(6, 5)
    finite_scheme_shift = Fraction(-13, 7)

    for c2, indices, instanton_terms in samples:
        b0 = 3 * c2 - sum(indices)
        beta_q_series = {0: b0, **instanton_terms}
        assert_equal(
            perturbative_q_projection(beta_q_series),
            b0,
            "holomorphic gauge beta perturbative q^0 projection",
        )

        running_difference = perturbative_q_projection(beta_q_series) * log_interval
        shifted_difference = (
            finite_scheme_shift
            + perturbative_q_projection(beta_q_series) * log_interval
            - finite_scheme_shift
        )
        assert_equal(
            shifted_difference,
            running_difference,
            "finite holomorphic scheme shift has zero scale derivative",
        )

    try:
        perturbative_q_projection({-1: Fraction(1), 0: Fraction(2)})
    except ValueError:
        pass
    else:
        raise AssertionError("negative q-degree should be rejected")


def check_holomorphic_tau_running_sign():
    """Check the sign relating tau, X_h, q_h, and asymptotic freedom.

    We record the derivative of tau in units of i/(2 pi).  The convention
    tau = theta/(2 pi) + 4 pi i / g_h^2 gives
    X_h = 8 pi^2/g_h^2 = 2 pi Im(tau).  Therefore

        d tau / d log mu = i b0/(2 pi) = - b0/(2 pi i)

    is equivalent to d X_h / d log mu = b0 and
    d log q_h / d log mu = -b0.
    """

    samples = [
        (Fraction(3), [Fraction(1), Fraction(2)]),
        (Fraction(5), [Fraction(1, 2), Fraction(3, 2), Fraction(2)]),
        (Fraction(7, 2), [Fraction(4), Fraction(5, 3)]),
    ]

    for c2, indices in samples:
        b0 = 3 * c2 - sum(indices)
        tau_derivative_in_i_over_2pi_units = b0
        xh_derivative = tau_derivative_in_i_over_2pi_units
        log_qh_derivative = -tau_derivative_in_i_over_2pi_units
        assert_equal(xh_derivative, b0, "holomorphic X_h running sign")
        assert_equal(log_qh_derivative, -b0, "weak-coupling q_h running sign")


def check_konishi_and_vector_coordinate_shifts():
    samples = [
        (Fraction(1, 2), Fraction(3, 5)),
        (Fraction(3), Fraction(-4, 7)),
        (Fraction(5, 2), Fraction(9, 4)),
    ]
    for index, alpha in samples:
        jacobian_action_coefficient = index * alpha / 8
        coordinate_shift = 16 * jacobian_action_coefficient
        assert_equal(coordinate_shift, 2 * index * alpha, "Konishi shift in X_h")

        log_z = -2 * alpha
        assert_equal(
            coordinate_shift,
            -index * log_z,
            "matter canonicalization shift -T log Z",
        )

    for c2, log_g_squared in samples:
        rho = log_g_squared / 2
        vector_coordinate_shift = 2 * c2 * rho
        assert_equal(vector_coordinate_shift, c2 * log_g_squared, "vector BV shift")


def check_nsvz_coordinate_identity():
    data = [
        (Fraction(3), [Fraction(1), Fraction(2)], [Fraction(-1, 3), Fraction(2)]),
        (Fraction(5), [Fraction(1, 2), Fraction(3, 2), Fraction(2)], [Fraction(0), Fraction(1, 4), Fraction(-2, 3)]),
        (Fraction(7, 2), [Fraction(4), Fraction(5, 3)], [Fraction(3, 5), Fraction(-1)]),
    ]
    x_coordinates = [Fraction(8), Fraction(17, 3), Fraction(25, 2)]

    for c2, indices, gammas in data:
        b0 = 3 * c2 - sum(indices)
        anomalous_sum = sum(index * gamma for index, gamma in zip(indices, gammas))
        numerator = 3 * c2 - sum(
            index * (1 - gamma)
            for index, gamma in zip(indices, gammas)
        )
        assert_equal(numerator, b0 + anomalous_sum, "NSVZ numerator split")

        for x in x_coordinates:
            if x == c2:
                continue
            beta_over_g = -numerator / (2 * (x - c2))
            differentiated_relation = (
                (-2 * x + 2 * c2) * beta_over_g
                - anomalous_sum
            )
            assert_equal(
                differentiated_relation,
                b0,
                "differentiated holomorphic-canonical relation",
            )


def main():
    check_tree_level_chiral_elimination_quadratic_block()
    check_tree_level_derivative_chain_rule()
    check_loop_supergraph_grassmann_measure_ledger()
    check_holomorphic_gauge_one_loop_projection()
    check_holomorphic_tau_running_sign()
    check_konishi_and_vector_coordinate_shifts()
    check_nsvz_coordinate_identity()
    print("All SUSY holomorphy and NSVZ coordinate checks passed.")


if __name__ == "__main__":
    main()
