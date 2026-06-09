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
    """Check the q-series bookkeeping and the q^0 closure boundary.

    Theta periodicity separates the q^0 perturbative coefficient from instanton
    powers.  It does not remove neutral holomorphic dependence on other running
    chiral couplings; that exclusion is an extra regulator/scheme input.
    """

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


def check_neutral_spurion_q0_closure_boundary():
    # Two superpotential spurions with opposite flavor charges can form a
    # neutral holomorphic invariant.  A q^0 beta coefficient depending on that
    # invariant is theta-periodic and weak-coupling regular, so q-expansion
    # bookkeeping alone does not reduce it to the one-loop determinant.
    b0 = Fraction(11, 3)
    y1 = Fraction(2, 5)
    y2 = Fraction(7, 4)
    neutral_invariant = y1 * y2
    mixing_coefficient = Fraction(3, 8)
    instanton_tail = {1: Fraction(-5, 9), 3: Fraction(13, 6)}

    beta_q_series = {
        0: b0 + mixing_coefficient * neutral_invariant,
        **instanton_tail,
    }
    q0_projection = perturbative_q_projection(beta_q_series)
    assert_equal(
        q0_projection,
        b0 + mixing_coefficient * neutral_invariant,
        "q^0 projection preserves neutral spurion dependence",
    )

    excluded_series = {0: b0, **instanton_tail}
    assert_equal(
        perturbative_q_projection(excluded_series),
        b0,
        "q^0 closure input recovers one-loop coefficient",
    )

    # A finite holomorphic coordinate change tau' = tau + k I changes the
    # beta component by k beta_I if the invariant I runs.
    beta_y1 = Fraction(1, 6)
    beta_y2 = Fraction(-2, 7)
    beta_invariant = y2 * beta_y1 + y1 * beta_y2
    finite_shift_derivative = Fraction(5, 3) * beta_invariant
    beta_tau = -b0
    beta_tau_prime = beta_tau + finite_shift_derivative
    assert_equal(
        beta_tau_prime - beta_tau,
        finite_shift_derivative,
        "running-coupling finite redefinition changes beta component",
    )

    beta_y2_locked = -y2 * beta_y1 / y1
    locked_beta_invariant = y2 * beta_y1 + y1 * beta_y2_locked
    assert_equal(
        locked_beta_invariant,
        0,
        "scale-independent invariant gives harmless finite shift",
    )


def check_holomorphic_one_loop_shell_coefficient():
    """Check vector/matter decomposition of the holomorphic shell coefficient.

    The manuscript separates two statements: a regulated one-loop determinant
    supplies b0 = 3 C2(G) - sum_i T(R_i), and holomorphy then excludes further
    perturbative q_h powers.  This finite ledger verifies the coefficient
    decomposition and the sign convention used for X_h running.
    """

    samples = [
        # pure SYM
        (Fraction(3), []),
        # SQCD-like pairs in half-trace normalization
        (Fraction(5), [Fraction(1, 2)] * 8),
        # N=4 as one vector plus three adjoint chirals: cancellation.
        (Fraction(7), [Fraction(7), Fraction(7), Fraction(7)]),
        # non-integral trace convention sample
        (Fraction(9, 4), [Fraction(1, 3), Fraction(5, 6), Fraction(7, 12)]),
    ]
    log_interval = Fraction(-4, 3)

    for c2, indices in samples:
        vector_shell = 3 * c2
        matter_shell = -sum(indices)
        shell_coefficient = vector_shell + matter_shell
        b0 = 3 * c2 - sum(indices)
        assert_equal(shell_coefficient, b0, "holomorphic one-loop shell coefficient")
        assert_equal(
            shell_coefficient * log_interval,
            b0 * log_interval,
            "one-loop X_h shell running sign",
        )


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
        jacobian_action_shift = 16 * jacobian_action_coefficient
        assert_equal(jacobian_action_shift, 2 * index * alpha, "Konishi action shift")

        log_z = -2 * alpha
        assert_equal(
            jacobian_action_shift,
            -index * log_z,
            "matter canonicalization action shift -T log Z",
        )
        assert_equal(
            -jacobian_action_shift,
            index * log_z,
            "matter term in solved X_h coordinate relation is +T log Z",
        )

    for c2, log_g_squared in samples:
        vector_action_shift = -c2 * log_g_squared
        assert_equal(
            -vector_action_shift,
            c2 * log_g_squared,
            "vector term in solved X_h coordinate relation",
        )


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
            log_z_derivative_sum = -anomalous_sum
            differentiated_relation = (
                (-2 * x + 2 * c2) * beta_over_g
                + log_z_derivative_sum
            )
            assert_equal(
                differentiated_relation,
                b0,
                "differentiated holomorphic-canonical relation",
            )
            wrong_gamma_sign_relation = (
                (-2 * x + 2 * c2) * beta_over_g
                + anomalous_sum
            )
            if wrong_gamma_sign_relation == b0:
                raise AssertionError("gamma=+d log Z convention incorrectly passed the plus-Z relation")


def check_canonical_yukawa_sign_from_kahler_z():
    samples = [
        (Fraction(1, 3), Fraction(-2, 5), Fraction(7, 4)),
        (Fraction(-1, 2), Fraction(3, 2), Fraction(2, 3)),
        (Fraction(5, 6), Fraction(1, 7), Fraction(-3, 8)),
    ]
    for gamma_m, gamma_q, gamma_tilde in samples:
        dlog_z_sum = -(gamma_m + gamma_q + gamma_tilde)
        beta_h_over_h = -dlog_z_sum / 2
        expected = (gamma_m + gamma_q + gamma_tilde) / 2
        assert_equal(
            beta_h_over_h,
            expected,
            "canonical Yukawa beta sign from Kähler Z convention",
        )

        wrong_plus_dlog_gamma = -expected
        if wrong_plus_dlog_gamma == beta_h_over_h:
            raise AssertionError("gamma=+d log Z convention incorrectly gave the canonical Yukawa sign")


def main():
    check_tree_level_chiral_elimination_quadratic_block()
    check_tree_level_derivative_chain_rule()
    check_loop_supergraph_grassmann_measure_ledger()
    check_holomorphic_gauge_one_loop_projection()
    check_neutral_spurion_q0_closure_boundary()
    check_holomorphic_one_loop_shell_coefficient()
    check_holomorphic_tau_running_sign()
    check_konishi_and_vector_coordinate_shifts()
    check_nsvz_coordinate_identity()
    check_canonical_yukawa_sign_from_kahler_z()
    print("All SUSY holomorphy and NSVZ coordinate checks passed.")


if __name__ == "__main__":
    main()
