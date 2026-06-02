#!/usr/bin/env python3
"""Exact finite checks for CFT energy-detector contact bookkeeping.

The checks model a finite positive calorimetric measure on the detector
sphere.  They verify the algebra behind the diagonal contact terms used in
the CFT light-ray/energy-correlator chapter.  The finite model is not a
substitute for the operator-valued-distribution construction; it fixes the
partition and moment bookkeeping that the continuum construction must
preserve.  The finite-resolution checks verify the Lipschitz partition
estimates used to pass from finite angular bins to statewise detector
measures and detector-product measures.  The finite light-ray OPE chart
check verifies the detector-functional bound obtained from retained
coefficient-map norms, light-ray form bounds, and the declared remainder,
and it detects the loss of the diagonal contact coordinate in a
separated-angle-only chart.  The finite light-ray chart covariance check
verifies retained-basis changes and diagonal-contact reshuffling as separate
coordinate operations on the same detector functional.
The small-angle pushforward check verifies the EEC angular-kernel Jacobian
that turns a homogeneous relative-coordinate light-ray coefficient into a
one-variable small-angle EEC power.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


Atom = tuple[Fraction, str]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_nonnegative(name: str, value: Fraction) -> None:
    if value < 0:
        raise AssertionError(f"{name}: got negative value {value!r}")


def detector_value(atoms: list[Atom], values: list[Fraction]) -> Fraction:
    if len(atoms) != len(values):
        raise ValueError("one detector-test value is required for each atom")
    return sum(energy * value for (energy, _), value in zip(atoms, values))


def state_measure_pairing(weights: list[Fraction], v: list[Fraction], w: list[Fraction]) -> Fraction:
    if len(weights) != len(v) or len(weights) != len(w):
        raise ValueError("bin weights and test vectors must have equal length")
    return sum(weight * vi * wi for weight, vi, wi in zip(weights, v, w))


def polynomial_moments(weights: list[Fraction], points: list[Fraction], max_degree: int) -> list[Fraction]:
    if len(weights) != len(points):
        raise ValueError("weights and points must have equal length")
    return [sum(weight * point**degree for weight, point in zip(weights, points)) for degree in range(max_degree + 1)]


def solve_three_point_grid_weights(moments: list[Fraction]) -> list[Fraction]:
    """Invert moments m_0,m_1,m_2 on the fixed grid {-1,0,1}."""

    if len(moments) < 3:
        raise ValueError("three moments are required on the three-point grid")
    m0, m1, m2 = moments[:3]
    weight_plus = (m2 + m1) / 2
    weight_minus = (m2 - m1) / 2
    weight_zero = m0 - m2
    return [weight_minus, weight_zero, weight_plus]


def two_detector_product(atoms: list[Atom], f: list[Fraction], g: list[Fraction]) -> Fraction:
    return detector_value(atoms, f) * detector_value(atoms, g)


def two_detector_off_diagonal(atoms: list[Atom], f: list[Fraction], g: list[Fraction]) -> Fraction:
    total = Fraction(0)
    for i, (energy_i, _) in enumerate(atoms):
        for j, (energy_j, _) in enumerate(atoms):
            if i != j:
                total += energy_i * energy_j * f[i] * g[j]
    return total


def two_detector_diagonal(atoms: list[Atom], f: list[Fraction], g: list[Fraction]) -> Fraction:
    return sum(energy * energy * fi * gi for (energy, _), fi, gi in zip(atoms, f, g))


def set_partitions(items: tuple[int, ...]) -> list[tuple[tuple[int, ...], ...]]:
    """Return all set partitions of the ordered tuple items."""

    if not items:
        return [()]
    first, *rest_list = items
    rest = tuple(rest_list)
    partitions: list[tuple[tuple[int, ...], ...]] = []
    for partition in set_partitions(rest):
        partitions.append(((first,),) + partition)
        for block_index, block in enumerate(partition):
            new_block = tuple(sorted((first,) + block))
            new_partition = list(partition)
            new_partition[block_index] = new_block
            partitions.append(tuple(sorted(new_partition)))
    unique: list[tuple[tuple[int, ...], ...]] = []
    for partition in partitions:
        normalized = tuple(sorted(tuple(block) for block in partition))
        if normalized not in unique:
            unique.append(normalized)
    return unique


def injective_block_assignments(num_atoms: int, num_blocks: int) -> list[tuple[int, ...]]:
    if num_blocks == 0:
        return [()]
    assignments: list[tuple[int, ...]] = []
    for combo in combinations(range(num_atoms), num_blocks):
        # Generate all permutations without importing itertools.permutations for
        # these tiny fixed checks.
        if num_blocks == 1:
            assignments.append(combo)
        elif num_blocks == 2:
            a, b = combo
            assignments.extend(((a, b), (b, a)))
        elif num_blocks == 3:
            a, b, c = combo
            assignments.extend(((a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)))
        else:
            raise ValueError("this finite check only uses up to three blocks")
    return assignments


def partition_decomposition(atoms: list[Atom], test_values: list[list[Fraction]]) -> Fraction:
    k = len(test_values)
    total = Fraction(0)
    for partition in set_partitions(tuple(range(k))):
        for assignment in injective_block_assignments(len(atoms), len(partition)):
            term = Fraction(1)
            for block, atom_index in zip(partition, assignment):
                energy = atoms[atom_index][0]
                term *= energy ** len(block)
                for detector_index in block:
                    term *= test_values[detector_index][atom_index]
            total += term
    return total


def check_statewise_riesz_bound() -> None:
    weights = [Fraction(1, 7), Fraction(2, 7), Fraction(4, 7)]
    f = [Fraction(-3, 2), Fraction(5, 4), Fraction(1, 6)]
    total_energy = sum(weights)
    integral = sum(weight * value for weight, value in zip(weights, f))
    sup_norm = max(abs(value) for value in f)
    assert_equal("finite partition total energy", total_energy, Fraction(1))
    assert_nonnegative("Riesz sup-norm detector bound", sup_norm * total_energy - abs(integral))


def check_finite_bin_cauchy_schwarz() -> None:
    weights = [Fraction(1, 5), Fraction(3, 10), Fraction(1, 2)]
    v = [Fraction(2), Fraction(-1, 3), Fraction(4, 7)]
    w = [Fraction(5, 6), Fraction(3, 8), Fraction(-2)]
    vv = state_measure_pairing(weights, v, v)
    ww = state_measure_pairing(weights, w, w)
    vw = state_measure_pairing(weights, v, w)
    assert_nonnegative("finite-bin detector Gram diagonal vv", vv)
    assert_nonnegative("finite-bin detector Gram diagonal ww", ww)
    assert_nonnegative("finite-bin detector Cauchy-Schwarz determinant", vv * ww - vw * vw)


def check_finite_partition_lipschitz_estimate() -> None:
    # One-dimensional finite shadow of angular bin refinement.  Points are
    # binned to representatives within distance delta.  For an L-Lipschitz
    # test, the detector error is bounded by L delta times total energy.
    weights = [Fraction(1, 5), Fraction(3, 10), Fraction(1, 2)]
    points = [Fraction(1, 10), Fraction(2, 5), Fraction(9, 10)]
    representatives = [Fraction(0), Fraction(1, 2), Fraction(1)]
    delta = Fraction(1, 5)
    total_energy = sum(weights)
    lipschitz_f = Fraction(2)

    def f(point: Fraction) -> Fraction:
        return 2 * point - 1

    exact = sum(weight * f(point) for weight, point in zip(weights, points))
    binned = sum(weight * f(rep) for weight, rep in zip(weights, representatives))
    error = abs(exact - binned)
    bound = lipschitz_f * delta * total_energy

    assert_equal("finite partition total energy", total_energy, Fraction(1))
    assert_equal("finite partition detector error", error, Fraction(3, 25))
    assert_equal("finite partition detector bound", bound, Fraction(2, 5))
    assert_nonnegative("finite partition Lipschitz estimate", bound - error)

    # Product-measure version for F(x,y)=x-2y.  With the sum product metric,
    # an admissible Lipschitz constant is max(1,2)=2, and the chapter's
    # bound is k L delta times the total product mass.
    lipschitz_F = Fraction(2)

    def F(left: Fraction, right: Fraction) -> Fraction:
        return left - 2 * right

    exact_product = Fraction(0)
    binned_product = Fraction(0)
    for weight_left, point_left, rep_left in zip(weights, points, representatives):
        for weight_right, point_right, rep_right in zip(weights, points, representatives):
            weight = weight_left * weight_right
            exact_product += weight * F(point_left, point_right)
            binned_product += weight * F(rep_left, rep_right)

    product_error = abs(exact_product - binned_product)
    product_bound = 2 * lipschitz_F * delta * total_energy**2
    assert_equal("finite product partition error", product_error, Fraction(3, 50))
    assert_equal("finite product partition bound", product_bound, Fraction(4, 5))
    assert_nonnegative("finite product partition Lipschitz estimate", product_bound - product_error)


def check_compact_moment_positive_matrix() -> None:
    weights = [Fraction(1, 6), Fraction(1, 3), Fraction(1, 2)]
    points = [Fraction(-1), Fraction(0), Fraction(1, 2)]
    moments = polynomial_moments(weights, points, 2)
    m0, m1, m2 = moments
    assert_equal("compact moment total mass", m0, Fraction(1))
    assert_nonnegative("degree-one moment matrix determinant", m0 * m2 - m1 * m1)


def check_three_point_grid_moment_reconstruction() -> None:
    points = [Fraction(-1), Fraction(0), Fraction(1)]
    weights = [Fraction(1, 5), Fraction(1, 2), Fraction(3, 10)]
    moments = polynomial_moments(weights, points, 2)
    recovered = solve_three_point_grid_weights(moments)
    assert_equal("three-point grid moment reconstruction", recovered, weights)


def check_truncated_moment_ambiguity() -> None:
    two_endpoint_weights = [Fraction(1, 2), Fraction(1, 2)]
    two_endpoint_points = [Fraction(-1), Fraction(1)]
    midpoint_weights = [Fraction(1)]
    midpoint_points = [Fraction(0)]
    endpoint_moments = polynomial_moments(two_endpoint_weights, two_endpoint_points, 2)
    midpoint_moments = polynomial_moments(midpoint_weights, midpoint_points, 2)
    assert_equal("same zeroth truncated moment", endpoint_moments[0], midpoint_moments[0])
    assert_equal("same first truncated moment", endpoint_moments[1], midpoint_moments[1])
    assert_equal("different second moment resolves ambiguity", endpoint_moments[2] - midpoint_moments[2], Fraction(1))


def check_two_detector_diagonal_split() -> None:
    atoms: list[Atom] = [(Fraction(2, 5), "n1"), (Fraction(1, 3), "n2"), (Fraction(4, 15), "n3")]
    f = [Fraction(1, 2), Fraction(-2, 3), Fraction(5, 7)]
    g = [Fraction(3, 11), Fraction(4, 9), Fraction(-1, 5)]
    full = two_detector_product(atoms, f, g)
    off_diagonal = two_detector_off_diagonal(atoms, f, g)
    diagonal = two_detector_diagonal(atoms, f, g)
    assert_equal("two-detector diagonal split", off_diagonal + diagonal, full)


def check_disjoint_support_removes_diagonal() -> None:
    atoms: list[Atom] = [(Fraction(1, 2), "north"), (Fraction(1, 4), "east"), (Fraction(1, 4), "south")]
    f = [Fraction(2), Fraction(0), Fraction(-3)]
    g = [Fraction(0), Fraction(5), Fraction(0)]
    assert_equal("pointwise disjoint tests have no diagonal", two_detector_diagonal(atoms, f, g), Fraction(0))
    assert_equal(
        "disjoint-support product equals off diagonal",
        two_detector_product(atoms, f, g),
        two_detector_off_diagonal(atoms, f, g),
    )


def check_total_energy_ward_identity() -> None:
    atoms: list[Atom] = [(Fraction(1, 6), "a"), (Fraction(1, 2), "b"), (Fraction(1, 3), "c")]
    ones = [Fraction(1)] * len(atoms)
    total_energy = detector_value(atoms, ones)
    assert_equal("normalized total energy", total_energy, Fraction(1))
    assert_equal("two-detector total energy square", two_detector_product(atoms, ones, ones), total_energy ** 2)
    assert_equal(
        "off diagonal plus contact gives total-energy square",
        two_detector_off_diagonal(atoms, ones, ones) + two_detector_diagonal(atoms, ones, ones),
        total_energy ** 2,
    )
    separated_only = two_detector_off_diagonal(atoms, ones, ones)
    contact = two_detector_diagonal(atoms, ones, ones)
    assert_equal("separated-only observable needs displayed contact", separated_only + contact, Fraction(1))


def check_three_detector_partition_decomposition() -> None:
    atoms: list[Atom] = [(Fraction(1, 5), "a"), (Fraction(3, 10), "b"), (Fraction(1, 2), "c")]
    tests = [
        [Fraction(2), Fraction(-1, 3), Fraction(4, 7)],
        [Fraction(5, 6), Fraction(3, 8), Fraction(-2)],
        [Fraction(-1, 4), Fraction(7, 9), Fraction(1, 11)],
    ]
    product = Fraction(1)
    for values in tests:
        product *= detector_value(atoms, values)
    assert_equal("three-detector partition decomposition", partition_decomposition(atoms, tests), product)


def check_finite_light_ray_ope_chart_bound() -> None:
    detector_test_norm = Fraction(6)
    light_form_bounds = [Fraction(2), Fraction(3, 2)]
    coefficient_map_bounds = [Fraction(1, 3), Fraction(5, 6)]
    remainder_constant = Fraction(5)
    epsilon = Fraction(1, 10)
    sigma = 2

    chart_factor = (
        sum(
            light_bound * coefficient_bound
            for light_bound, coefficient_bound
            in zip(light_form_bounds, coefficient_map_bounds)
        )
        + remainder_constant * epsilon**sigma
    )
    detector_bound = chart_factor * detector_test_norm
    assert_equal("finite light-ray OPE chart factor", chart_factor, Fraction(59, 30))
    assert_equal("finite light-ray OPE detector bound", detector_bound, Fraction(59, 5))

    retained_light_ray_terms = [Fraction(7, 3), Fraction(-5, 2)]
    remainder_value = Fraction(1, 10)
    actual_detector_value = sum(retained_light_ray_terms) + remainder_value
    assert_equal("finite light-ray OPE chart sample value", actual_detector_value, Fraction(-1, 15))
    assert_nonnegative(
        "finite light-ray OPE chart bound controls sample",
        detector_bound - abs(actual_detector_value),
    )

    separated_angle_value = Fraction(4, 5)
    diagonal_contact_coordinate = Fraction(1, 3)
    full_detector_moment = separated_angle_value + diagonal_contact_coordinate
    assert_equal("finite light-ray OPE full moment with contact", full_detector_moment, Fraction(17, 15))
    if separated_angle_value == full_detector_moment:
        raise AssertionError("separated-angle chart incorrectly determines contact coordinate")


def check_finite_light_ray_chart_covariance() -> None:
    # Retained finite chart value V = c ell + k.  A change of retained
    # light-ray basis is ordinary row/column covariance and must leave c ell
    # invariant.
    ell = [Fraction(2), Fraction(-1)]
    c = [Fraction(3), Fraction(5)]
    contact = Fraction(7, 11)
    value = c[0] * ell[0] + c[1] * ell[1] + contact

    # B = [[1,2],[0,1]], B^{-1} = [[1,-2],[0,1]].
    ell_prime = [ell[0] - 2 * ell[1], ell[1]]
    c_prime = [c[0], 2 * c[0] + c[1]]
    value_prime = c_prime[0] * ell_prime[0] + c_prime[1] * ell_prime[1] + contact
    assert_equal("finite light-ray basis covariance", value_prime, value)

    # Adding diagonal distributions to the retained coefficient maps changes
    # the row c by d.  The same full detector distribution is obtained only
    # after shifting the explicit contact coordinate by -d ell.
    d = [Fraction(1, 3), Fraction(-2, 5)]
    d_ell = d[0] * ell[0] + d[1] * ell[1]
    c_new = [c[0] + d[0], c[1] + d[1]]
    contact_new = contact - d_ell
    value_new = c_new[0] * ell[0] + c_new[1] * ell[1] + contact_new
    assert_equal("finite light-ray contact reshuffle", value_new, value)

    bad_value = c_new[0] * ell[0] + c_new[1] * ell[1] + contact
    assert_equal("finite light-ray unshifted contact defect", bad_value - value, d_ell)
    assert_equal("finite light-ray contact defect value", bad_value - value, Fraction(16, 15))
    if bad_value == value:
        raise AssertionError("unshifted contact coordinate failed to change the detector functional")


def check_small_angle_eec_pushforward_exponents() -> None:
    # Detector sphere dimension d_perp = D-2.  The local angular shell has
    # power d_perp-1, while the EEC kernel
    # delta(cos chi - cos theta) contributes one inverse power from
    # |d cos theta / d theta| = sin theta.  A coefficient homogeneous of
    # degree -lambda therefore contributes chi^(d_perp-2-lambda).
    spacetime_dimension = 4
    detector_sphere_dimension = spacetime_dimension - 2
    coefficient_lambda = Fraction(3, 2)
    eec_exponent = Fraction(detector_sphere_dimension - 2) - coefficient_lambda
    delta_theta_exponent = Fraction(detector_sphere_dimension - 1) - coefficient_lambda
    assert_equal("small-angle EEC delta-cos exponent in D=4", eec_exponent, Fraction(-3, 2))
    assert_equal("small-angle delta-theta exponent differs by one", delta_theta_exponent - eec_exponent, Fraction(1))

    spacetime_dimension_five = 5
    detector_sphere_dimension_five = spacetime_dimension_five - 2
    lambda_five = Fraction(2)
    eec_exponent_five = Fraction(detector_sphere_dimension_five - 2) - lambda_five
    assert_equal("small-angle EEC delta-cos exponent in D=5", eec_exponent_five, Fraction(-1))

    z_variable_exponent = eec_exponent / 2
    assert_equal("small-angle z-variable exponent", z_variable_exponent, Fraction(-3, 4))

    log_power = 2
    polyhomogeneous_label = (eec_exponent, log_power)
    assert_equal("small-angle log power preserved by pushforward", polyhomogeneous_label, (Fraction(-3, 2), 2))


def main() -> None:
    check_statewise_riesz_bound()
    check_finite_bin_cauchy_schwarz()
    check_finite_partition_lipschitz_estimate()
    check_compact_moment_positive_matrix()
    check_three_point_grid_moment_reconstruction()
    check_truncated_moment_ambiguity()
    check_two_detector_diagonal_split()
    check_disjoint_support_removes_diagonal()
    check_total_energy_ward_identity()
    check_three_detector_partition_decomposition()
    check_finite_light_ray_ope_chart_bound()
    check_finite_light_ray_chart_covariance()
    check_small_angle_eec_pushforward_exponents()
    print("All CFT energy-detector contact and moment checks passed.")


if __name__ == "__main__":
    main()
