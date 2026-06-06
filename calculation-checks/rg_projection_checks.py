#!/usr/bin/env python3
"""Exact finite checks for projected RG fixed-point warnings.

The Volume XI rigorous-RG chapter uses these two-dimensional examples to
separate projected fixed points from theorem-level fixed points of the full
Banach-space RG map.
"""

from fractions import Fraction


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_true(name, condition):
    if not condition:
        raise AssertionError(name)


def project(vector):
    return (vector[0], Fraction(0))


def complement(vector):
    return (Fraction(0), vector[1])


def add(left, right):
    return (left[0] + right[0], left[1] + right[1])


def sub(left, right):
    return (left[0] - right[0], left[1] - right[1])


def norm_l1(vector):
    return sum(abs(entry) for entry in vector)


def product(values):
    result = Fraction(1)
    for value in values:
        result *= value
    return result


RG_CLAIM_STAGES = (
    "map_in_declared_norm",
    "fixed_point_or_trajectory",
    "source_window_control",
    "observable_reconstruction",
    "target_identification",
)


def completed_prefix_length(stage_record):
    count = 0
    for stage in RG_CLAIM_STAGES:
        if not stage_record.get(stage, False):
            break
        count += 1
    return count


def check_spurious_projected_zero():
    def residual(point):
        _x, _y = point
        return (Fraction(0), Fraction(1))

    for x_value in [Fraction(-2), Fraction(0), Fraction(5, 3)]:
        point = (x_value, Fraction(0))
        assert_equal(
            "projected residual vanishes",
            project(residual(point)),
            (Fraction(0), Fraction(0)),
        )
        assert_true(
            "full residual remains nonzero",
            residual(point) != (Fraction(0), Fraction(0)),
        )


def check_projected_zero_lift_condition():
    epsilon = Fraction(1, 10)

    def residual(point):
        x_value, y_value = point
        return (x_value, y_value - epsilon)

    projected_zero = (Fraction(0), Fraction(0))
    assert_equal(
        "projected equation",
        project(residual(projected_zero)),
        (Fraction(0), Fraction(0)),
    )
    assert_equal(
        "complement residual",
        norm_l1(complement(residual(projected_zero))),
        epsilon,
    )

    # For this linear example A is the identity, rho=L=0, and the true zero
    # lies exactly at distance epsilon from the projected zero.
    radius = epsilon
    rho = Fraction(0)
    lipschitz = Fraction(0)
    assert_true(
        "Newton-Kantorovich projected lift inequality",
        epsilon + rho * radius + lipschitz * radius * radius / 2 <= radius,
    )
    true_zero = (Fraction(0), epsilon)
    assert_equal(
        "full residual at lifted zero",
        residual(true_zero),
        (Fraction(0), Fraction(0)),
    )
    assert_equal(
        "distance from projected zero",
        norm_l1(sub(true_zero, projected_zero)),
        radius,
    )

    # The projected-zero residual decomposes into P and Q parts exactly.
    full_residual = residual(projected_zero)
    assert_equal(
        "P plus Q decomposition",
        add(project(full_residual), complement(full_residual)),
        full_residual,
    )


def check_irrelevant_tail_residual():
    # Model B = R^1 + K with a finite irrelevant tail K = R^3.
    # The projected local equation vanishes at g=0, but the tail residual is
    # nonzero unless the kernel coordinate is solved as part of the full fixed
    # point equation.
    local_residual = Fraction(0)
    tail_residual = (Fraction(1, 2), Fraction(-1, 3), Fraction(1, 5))
    assert_equal("projected local residual", local_residual, 0)
    assert_true("irrelevant tail residual is nonzero", norm_l1(tail_residual[:2]) + abs(tail_residual[2]) > 0)

    # If the irrelevant equation is linear K' = lambda K + c with |lambda|<1,
    # the exact graph solution is K*=c/(1-lambda).  This is the finite algebra
    # behind solving the irrelevant tail by contraction rather than dropping it.
    lambdas = (Fraction(1, 2), Fraction(1, 3), Fraction(-1, 4))
    graph_solution = tuple(c / (1 - lam) for c, lam in zip(tail_residual, lambdas))
    residual_after_graph = tuple(lam * k + c - k for k, c, lam in zip(graph_solution, tail_residual, lambdas))
    assert_equal(
        "irrelevant graph residual",
        residual_after_graph,
        (Fraction(0), Fraction(0), Fraction(0)),
    )


def check_projected_observable_lift_budget():
    # A projected fixed point is useful for observables only after the
    # complement residual is small enough to lift it and after the
    # reconstruction map is controlled in the relevant seminorm.
    epsilon = Fraction(1, 20)
    rho = Fraction(1, 4)
    lipschitz_derivative = Fraction(1, 2)
    radius = Fraction(1, 10)

    ball_budget = (
        epsilon
        + rho * radius
        + lipschitz_derivative * radius * radius / 2
    )
    assert_equal("projected observable NK ball budget", ball_budget, Fraction(31, 400))
    assert_true("projected observable NK ball condition", ball_budget <= radius)
    assert_true(
        "projected observable NK contraction condition",
        rho + lipschitz_derivative * radius < 1,
    )

    reconstruction_lipschitz = Fraction(3)
    chart_error = Fraction(1, 50)
    observable_lift_bound = chart_error + reconstruction_lipschitz * radius
    assert_equal("projected observable lift bound", observable_lift_bound, Fraction(8, 25))

    actual_window_error = Fraction(1, 4)
    assert_true(
        "projected observable finite window controlled",
        actual_window_error <= observable_lift_bound,
    )

    # Matching the projected observable exactly is not enough when the lift
    # residual is too large for the Newton-Kantorovich ball.
    bad_epsilon = Fraction(1, 3)
    bad_ball_budget = (
        bad_epsilon
        + rho * radius
        + lipschitz_derivative * radius * radius / 2
    )
    assert_true(
        "projected observable bad residual detected",
        bad_ball_budget > radius,
    )


def check_frg_projected_flow_residual_budget():
    # Finite-step version of the FRG projected-flow residual estimate:
    # e_{j+1} <= a e_j + h delta_j with e_0=0.
    step_size = Fraction(1, 2)
    lipschitz = Fraction(1)
    amplification = 1 + step_size * lipschitz
    residuals = (Fraction(1, 20), Fraction(1, 40), Fraction(1, 80))

    error = Fraction(0)
    for residual in residuals:
        error = amplification * error + step_size * residual

    closed_form = sum(
        amplification ** (len(residuals) - 1 - index)
        * step_size
        * residual
        for index, residual in enumerate(residuals)
    )
    assert_equal("FRG projected-flow residual recurrence", error, Fraction(13, 160))
    assert_equal("FRG projected-flow residual closed form", closed_form, error)

    reconstruction_lipschitz = Fraction(5, 2)
    observable_error = reconstruction_lipschitz * error
    assert_equal("FRG projected-flow observable error", observable_error, Fraction(13, 64))

    bad_residuals = (Fraction(1, 2), Fraction(1, 40), Fraction(1, 80))
    bad_bound = sum(
        amplification ** (len(bad_residuals) - 1 - index)
        * step_size
        * residual
        for index, residual in enumerate(bad_residuals)
    )
    assert_true("FRG projected-flow bad residual detected", bad_bound > Fraction(1, 4))


def check_frg_projected_fixed_point_residual_gate():
    # A projected fixed point of a dimensionless FRG beta vector field is not
    # a full fixed point until the omitted beta component is lifted in the full
    # Banach chart.  The triangular finite model below has a projected zero at
    # the origin, but the exact zero shifts all coordinates.
    epsilon = Fraction(1, 30)

    def beta(point):
        x_value, y_value, z_value = point
        return (
            x_value + z_value / 2,
            y_value - z_value / 3,
            z_value - epsilon,
        )

    projected_zero = (Fraction(0), Fraction(0), Fraction(0))
    projected_beta = beta(projected_zero)[:2] + (Fraction(0),)
    complement_beta = (Fraction(0), Fraction(0), beta(projected_zero)[2])
    assert_equal("FRG projected fixed point retained beta", projected_beta, (Fraction(0), Fraction(0), Fraction(0)))
    assert_equal("FRG projected fixed point omitted beta", complement_beta, (Fraction(0), Fraction(0), -epsilon))

    def approximate_inverse(vector):
        first, second, third = vector
        return (first - third / 2, second + third / 3, third)

    lifted_residual = approximate_inverse(complement_beta)
    lift_radius = norm_l1(lifted_residual)
    assert_equal("FRG projected fixed point lifted residual", lifted_residual, (epsilon / 2, -epsilon / 3, -epsilon))
    assert_equal("FRG projected fixed point NK radius", lift_radius, Fraction(11, 180))

    rho = Fraction(0)
    lipschitz_derivative = Fraction(0)
    assert_true(
        "FRG projected fixed point lift condition",
        lift_radius + rho * lift_radius + lipschitz_derivative * lift_radius * lift_radius / 2 <= lift_radius,
    )

    exact_zero = (
        -epsilon / 2,
        epsilon / 3,
        epsilon,
    )
    assert_equal("FRG projected fixed point exact beta", beta(exact_zero), (Fraction(0), Fraction(0), Fraction(0)))
    distance = tuple(left - right for left, right in zip(exact_zero, projected_zero))
    assert_equal("FRG projected fixed point distance", norm_l1(distance), lift_radius)

    observable_chart_error = Fraction(1, 100)
    reconstruction_lipschitz = Fraction(4)
    observable_error = observable_chart_error + reconstruction_lipschitz * lift_radius
    assert_equal("FRG projected fixed point observable window error", observable_error, Fraction(229, 900))

    # If the complement beta is ignored, the retained critical exponents look
    # exact while the vector field is still nonzero in the full chart.
    retained_linear_eigenvalues = (Fraction(1), Fraction(1))
    assert_equal("FRG retained eigenvalue list unchanged", retained_linear_eigenvalues, (Fraction(1), Fraction(1)))
    assert_true("FRG omitted beta obstruction detected", norm_l1(complement_beta) > 0)


def check_tensor_rg_truncation_window_budget():
    # Exact finite recursion for tensor-RG truncation residuals:
    # e_{j+1} <= L_j e_j + delta_j.
    lipschitz = (Fraction(3, 4), Fraction(2, 3), Fraction(1, 2))
    residuals = (Fraction(1, 100), Fraction(1, 150), Fraction(1, 200))

    error = Fraction(0)
    for factor, residual in zip(lipschitz, residuals):
        error = factor * error + residual

    closed_form = sum(
        product(lipschitz[index + 1 :])
        * residual
        for index, residual in enumerate(residuals)
    )
    assert_equal("tensor RG truncation recurrence", error, Fraction(7, 600))
    assert_equal("tensor RG truncation closed form", closed_form, error)

    observable_lipschitz = Fraction(6)
    normalization_error = Fraction(1, 100)
    window_error = observable_lipschitz * error + normalization_error
    assert_equal("tensor RG observable window bound", window_error, Fraction(2, 25))

    bad_residuals = (Fraction(1, 5), Fraction(1, 150), Fraction(1, 200))
    bad_bound = sum(
        product(lipschitz[index + 1 :])
        * residual
        for index, residual in enumerate(bad_residuals)
    )
    assert_true("tensor RG bad truncation residual detected", bad_bound > Fraction(1, 16))


def check_rg_claim_observable_output_stage_map():
    # The model-by-model synthesis in the chapter orders claims by the physical
    # observable layer they actually control.  A later flag cannot be used when
    # an earlier layer is missing.
    auxiliary_hierarchical = {
        "map_in_declared_norm": True,
        "fixed_point_or_trajectory": True,
        "source_window_control": True,
        "observable_reconstruction": True,
        "target_identification": False,
    }
    frg_projected_fixed_point = {
        "map_in_declared_norm": True,
        "fixed_point_or_trajectory": False,
        "source_window_control": False,
        "observable_reconstruction": False,
        "target_identification": False,
    }
    ordinary_short_range_complete = {
        stage: True for stage in RG_CLAIM_STAGES
    }
    skipped_reconstruction_claim = {
        "map_in_declared_norm": True,
        "fixed_point_or_trajectory": True,
        "source_window_control": False,
        "observable_reconstruction": True,
        "target_identification": True,
    }

    assert_equal(
        "hierarchical observable stages stop before target identification",
        completed_prefix_length(auxiliary_hierarchical),
        4,
    )
    assert_equal(
        "projected FRG beta zero lacks fixed-point lift stage",
        completed_prefix_length(frg_projected_fixed_point),
        1,
    )
    assert_equal(
        "ordinary short-range complete observable stages",
        completed_prefix_length(ordinary_short_range_complete),
        len(RG_CLAIM_STAGES),
    )
    assert_equal(
        "skipped reconstruction does not count later target labels",
        completed_prefix_length(skipped_reconstruction_claim),
        2,
    )

    # A physical short-range Wilson-Fisher claim requires every stage in the
    # ordered prefix.  Auxiliary fixed-point data and a projected beta zero both
    # fail this finite claim test for different reasons.
    required_physical_prefix = len(RG_CLAIM_STAGES)
    assert_true(
        "auxiliary fixed point is not a short-range observable reconstruction",
        completed_prefix_length(auxiliary_hierarchical) < required_physical_prefix,
    )
    assert_true(
        "projected FRG fixed point is not an observable reconstruction",
        completed_prefix_length(frg_projected_fixed_point) < required_physical_prefix,
    )
    assert_true(
        "complete short-range package reaches the physical observable layer",
        completed_prefix_length(ordinary_short_range_complete) == required_physical_prefix,
    )


def main():
    check_spurious_projected_zero()
    check_projected_zero_lift_condition()
    check_irrelevant_tail_residual()
    check_projected_observable_lift_budget()
    check_frg_projected_flow_residual_budget()
    check_frg_projected_fixed_point_residual_gate()
    check_tensor_rg_truncation_window_budget()
    check_rg_claim_observable_output_stage_map()
    print("All RG projection checks passed.")


if __name__ == "__main__":
    main()
