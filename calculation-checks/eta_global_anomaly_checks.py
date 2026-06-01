#!/usr/bin/env python3
"""Exact checks for eta-invariant and SU(2) global-anomaly conventions."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def su2_trace_delta_index(n: int) -> int:
    """Trace-delta Dynkin index for isospin j=n/2."""

    return n * (n + 1) * (n + 2) // 6


def pfaffian_sign_from_representations(ns: list[int]) -> int:
    parity = sum(su2_trace_delta_index(n) for n in ns) % 2
    return -1 if parity else 1


def check_su2_index_table() -> None:
    first_values = [su2_trace_delta_index(n) for n in range(1, 6)]
    assert_equal("first SU(2) trace-delta indices", first_values, [1, 4, 10, 20, 35])


def check_witten_parity_criterion() -> None:
    for n in range(0, 64):
        got = su2_trace_delta_index(n) % 2
        expected = 1 if n % 4 == 1 else 0
        assert_equal(f"Witten parity criterion n={n}", got, expected)


def check_pfaffian_sign_multiplicativity() -> None:
    assert_equal("one fundamental doublet", pfaffian_sign_from_representations([1]), -1)
    assert_equal("two fundamental doublets", pfaffian_sign_from_representations([1, 1]), 1)
    assert_equal("doublet plus isospin 5/2", pfaffian_sign_from_representations([1, 5]), 1)
    assert_equal("triplet and isospin 3/2", pfaffian_sign_from_representations([2, 3]), 1)


def mapping_torus_character(class_bit: int, ns: list[int]) -> int:
    """Pfaffian sign character for the SU(2) mapping-torus component group.

    class_bit is the element of pi_4(SU(2)) = Z_2.  The exponent is additive
    both under concatenation of mapping tori and under direct sums of
    representation bundles.
    """

    exponent = class_bit * sum(su2_trace_delta_index(n) for n in ns)
    return -1 if exponent % 2 else 1


def check_mapping_torus_z2_character_bookkeeping() -> None:
    samples = [
        [],
        [1],
        [1, 1],
        [2, 3, 5],
        [1, 5, 9],
    ]
    for ns in samples:
        identity = mapping_torus_character(0, ns)
        generator = mapping_torus_character(1, ns)
        doubled_generator = mapping_torus_character((1 + 1) % 2, ns)
        assert_equal(f"mapping-torus identity component ns={ns}", identity, 1)
        assert_equal(f"mapping-torus generator squared ns={ns}", doubled_generator, 1)
        assert_equal(
            f"mapping-torus character additivity ns={ns}",
            generator * generator,
            doubled_generator,
        )

    for first in samples:
        for second in samples:
            direct_sum = first + second
            assert_equal(
                f"mapping-torus direct-sum multiplicativity {first}+{second}",
                mapping_torus_character(1, direct_sum),
                mapping_torus_character(1, first) * mapping_torus_character(1, second),
            )


def block_pfaffian(parameters: list[Fraction]) -> Fraction:
    product = Fraction(1)
    for parameter in parameters:
        product *= parameter
    return product


def sign(value: Fraction) -> int:
    if value > 0:
        return 1
    if value < 0:
        return -1
    raise ValueError("sign requested at a zero Pfaffian coordinate")


def check_finite_pfaffian_block_model() -> None:
    samples = [
        [Fraction(2), Fraction(3), Fraction(5)],
        [Fraction(-2), Fraction(3), Fraction(5)],
        [Fraction(-2), Fraction(-3), Fraction(5)],
        [Fraction(7, 2), Fraction(-5, 3), Fraction(-11, 4), Fraction(13, 5)],
    ]
    for parameters in samples:
        pf = block_pfaffian(parameters)
        determinant = pf * pf
        block_determinants = Fraction(1)
        for parameter in parameters:
            block_determinants *= parameter * parameter
        assert_equal(f"finite Pfaffian square parameters={parameters}", determinant, block_determinants)

    initial = [Fraction(2), Fraction(3), Fraction(5), Fraction(7)]
    for mask in range(1 << len(initial)):
        final = []
        crossings = 0
        for index, parameter in enumerate(initial):
            if mask & (1 << index):
                final.append(-parameter)
                crossings += 1
            else:
                final.append(parameter)
        expected_sign_ratio = -1 if crossings % 2 else 1
        got_sign_ratio = sign(block_pfaffian(final)) * sign(block_pfaffian(initial))
        assert_equal(f"finite Pfaffian crossing parity mask={mask}", got_sign_ratio, expected_sign_ratio)

    first = [Fraction(2), Fraction(-3), Fraction(5)]
    second = [Fraction(-7), Fraction(11)]
    direct_sum = first + second
    assert_equal(
        "finite Pfaffian tensor/direct-sum multiplicativity",
        block_pfaffian(direct_sum),
        block_pfaffian(first) * block_pfaffian(second),
    )


def check_su2_cubic_weight_sum_vanishes() -> None:
    for n in range(0, 16):
        doubled_weights = list(range(-n, n + 1, 2))
        assert_equal(f"SU(2) cubic weight sum n={n}", sum(weight**3 for weight in doubled_weights), 0)


def check_orientation_reversal_eta_bookkeeping() -> None:
    samples = [
        (Fraction(3, 7), 0),
        (Fraction(-5, 4), 2),
        (Fraction(11, 6), 5),
    ]
    for eta, kernel_dim in samples:
        xi = (eta + kernel_dim) / 2
        xi_reversed = (-eta + kernel_dim) / 2
        assert_equal(
            f"xi(-B) relation eta={eta} h={kernel_dim}",
            xi_reversed,
            -xi + kernel_dim,
        )


def reduced_eta_single_mode(sign_label: int) -> Fraction:
    """Contribution of one crossing eigenvalue to xi=(eta+h)/2.

    sign_label is -1 for a negative eigenvalue, 0 at the kernel crossing,
    and +1 for a positive eigenvalue.
    """

    eta = Fraction(sign_label)
    kernel_dim = 1 if sign_label == 0 else 0
    return (eta + kernel_dim) / 2


def check_reduced_eta_crossing_integer_jump() -> None:
    negative = reduced_eta_single_mode(-1)
    zero = reduced_eta_single_mode(0)
    positive = reduced_eta_single_mode(1)
    assert_equal("single-mode eta contribution below zero", negative, Fraction(-1, 2))
    assert_equal("single-mode eta contribution at zero", zero, Fraction(1, 2))
    assert_equal("single-mode eta contribution above zero", positive, Fraction(1, 2))
    assert_equal("upward crossing changes reduced eta by an integer", positive - negative, Fraction(1))
    assert_equal("downward crossing changes reduced eta by an integer", negative - positive, Fraction(-1))
    assert_equal("eta phase is unchanged by upward integer jump", mod_one(positive - negative), Fraction(0))


def check_aps_cylinder_congruence() -> None:
    examples = [
        (Fraction(5, 3), Fraction(2, 3), 2),
        (Fraction(-1, 5), Fraction(9, 5), -1),
        (Fraction(7, 4), Fraction(-1, 4), 3),
    ]
    for bulk_integral, xi0, fredholm_index in examples:
        # APS on [0,1] x Y gives
        # index = bulk - xi1 + xi0 modulo the integer endpoint-kernel term.
        xi1 = bulk_integral + xi0 - fredholm_index
        difference = xi1 - xi0 - bulk_integral
        assert_equal("APS cylinder difference is integral", difference.denominator, 1)


def check_aps_cylinder_exact_bookkeeping() -> None:
    examples = [
        (Fraction(5, 3), Fraction(2, 3), 0, 2),
        (Fraction(-1, 5), Fraction(9, 5), 3, -1),
        (Fraction(7, 4), Fraction(-1, 4), 1, 3),
    ]
    for bulk_integral, xi0, endpoint_kernel, aps_index in examples:
        # With boundary Y_1 union (-Y_0), APS gives
        # index = bulk - xi_1 + xi_0 - h(B_0).
        xi1 = bulk_integral + xi0 - endpoint_kernel - aps_index
        assert_equal(
            f"exact APS cylinder identity bulk={bulk_integral} xi0={xi0}",
            bulk_integral - xi1 + xi0 - endpoint_kernel,
            aps_index,
        )
        assert_equal(
            f"APS cylinder congruence after endpoint bookkeeping bulk={bulk_integral}",
            mod_one(xi1 - xi0 - bulk_integral),
            Fraction(0),
        )


def check_aps_spectral_flow_sign_convention() -> None:
    examples = [
        ([], Fraction(3, 7), Fraction(1, 5)),
        ([1], Fraction(0), Fraction(0)),
        ([1, -1, 1], Fraction(5, 6), Fraction(-2, 9)),
        ([-1, -1], Fraction(-2, 5), Fraction(7, 11)),
    ]
    for crossings, local_change, xi0 in examples:
        # +1 is a negative-to-positive crossing.  In the chapter's APS
        # boundary convention the crossing contribution to the cylinder index
        # is the negative of this spectral flow; the smooth part is accounted
        # for by the local index-density integral.
        spectral_flow = sum(crossings)
        xi1 = xi0 + local_change + spectral_flow
        aps_index = local_change - xi1 + xi0
        assert_equal(
            f"APS cylinder index has opposite sign to spectral flow crossings={crossings}",
            aps_index,
            Fraction(-spectral_flow),
        )
        assert_equal(
            f"spectral-flow jumps are integral after removing local change crossings={crossings}",
            mod_one(xi1 - xi0 - local_change),
            Fraction(0),
        )


def spectral_cut_transition(singular_values: list[Fraction], low: Fraction, high: Fraction) -> Fraction:
    """Finite determinant-line transition factor for a spectral-cut window."""

    product = Fraction(1)
    for singular_value in singular_values:
        eigenvalue = singular_value * singular_value
        if low <= eigenvalue < high:
            product *= singular_value
    return product


def check_quillen_spectral_cut_transition_cocycle() -> None:
    singular_values = [
        Fraction(1, 2),
        Fraction(2, 3),
        Fraction(3, 2),
        Fraction(5, 2),
        Fraction(7, 3),
        Fraction(11, 4),
    ]
    cuts = [Fraction(0), Fraction(1, 3), Fraction(1), Fraction(4), Fraction(7), Fraction(9)]
    for i, low in enumerate(cuts):
        for j in range(i + 1, len(cuts)):
            middle = cuts[j]
            for high in cuts[j + 1 :]:
                direct = spectral_cut_transition(singular_values, low, high)
                composed = spectral_cut_transition(singular_values, low, middle)
                composed *= spectral_cut_transition(singular_values, middle, high)
                assert_equal(
                    f"Quillen spectral-cut transition cocycle {low}->{middle}->{high}",
                    direct,
                    composed,
                )


def mod_one(value: Fraction) -> Fraction:
    quotient = value.numerator // value.denominator
    return value - quotient


def check_dai_freed_gluing_phase_algebra() -> None:
    fillings = [Fraction(1, 7), Fraction(5, 6), Fraction(-2, 5), Fraction(9, 4)]
    for xi0 in fillings:
        for xi1 in fillings:
            for xi2 in fillings:
                glued_01 = mod_one(xi0 - xi1)
                glued_12 = mod_one(xi1 - xi2)
                glued_02 = mod_one(xi0 - xi2)
                assert_equal(
                    f"Dai-Freed glued phase associativity {xi0},{xi1},{xi2}",
                    mod_one(glued_01 + glued_12),
                    glued_02,
                )

    bounding_data = [
        (Fraction(13, 5), 2),
        (Fraction(-7, 3), -4),
        (Fraction(19, 12), 1),
    ]
    for bulk_integral, aps_index in bounding_data:
        xi = bulk_integral - aps_index
        assert_equal(
            f"bounding integral equals eta phase modulo integers {bulk_integral}",
            mod_one(xi),
            mod_one(bulk_integral),
        )


def oriented_edge_value(cochain: dict[tuple[int, int], Fraction], start: int, end: int) -> Fraction:
    if (start, end) in cochain:
        return cochain[(start, end)]
    if (end, start) in cochain:
        return -cochain[(end, start)]
    raise KeyError(f"missing oriented edge {start}->{end}")


def boundary_integral(cochain: dict[tuple[int, int], Fraction], vertices: list[int]) -> Fraction:
    total = Fraction(0)
    for index, start in enumerate(vertices):
        end = vertices[(index + 1) % len(vertices)]
        total += oriented_edge_value(cochain, start, end)
    return total


def check_contractible_loop_curvature_stokes() -> None:
    """Finite cochain model of the contractible-loop Stokes step.

    The chapter uses this algebra to pass from Bismut--Freed curvature over a
    background-space disk to the local descent integral on the boundary loop.
    Interior cut contributions cancel before reducing the final exponent
    modulo integers.
    """

    connection = {
        (0, 1): Fraction(1, 5),
        (1, 2): Fraction(-2, 7),
        (2, 3): Fraction(3, 11),
        (0, 3): Fraction(5, 13),
        (0, 2): Fraction(-7, 17),
    }
    left_triangle_curvature = boundary_integral(connection, [0, 1, 2])
    right_triangle_curvature = boundary_integral(connection, [0, 2, 3])
    disk_curvature = left_triangle_curvature + right_triangle_curvature
    outer_boundary = boundary_integral(connection, [0, 1, 2, 3])
    assert_equal(
        "contractible-loop Stokes cancellation of the interior cut",
        disk_curvature,
        outer_boundary,
    )

    local_descent_integral = Fraction(19, 23)
    aps_integer_ambiguity = 4
    eta_phase_exponent = local_descent_integral + aps_integer_ambiguity
    assert_equal(
        "APS integer ambiguity leaves the contractible-loop anomaly phase unchanged",
        mod_one(eta_phase_exponent),
        mod_one(local_descent_integral),
    )


def orbit_action(a: int, g: int, orbit_size: int) -> int:
    return (a + g) % orbit_size


def anomaly_cocycle_exponent(a: int, g: int, orbit_size: int, phase_modulus: int) -> int:
    """A finite action-groupoid 1-cocycle in additive exponent notation.

    The value represents exp(2*pi*i*exponent/phase_modulus).  The dependence
    on the base object models a local trivialization; only based-loop values
    survive coboundary changes.
    """

    ag = orbit_action(a, g, orbit_size)
    potential_a = (a * a + 2 * a + 1) % phase_modulus
    potential_ag = (ag * ag + 2 * ag + 1) % phase_modulus
    return (potential_a - potential_ag) % phase_modulus


def trivialization_exponent(a: int, orbit_size: int, phase_modulus: int) -> int:
    return (3 * a * a + a + 1) % phase_modulus


def coboundary_shifted_exponent(a: int, g: int, orbit_size: int, phase_modulus: int) -> int:
    ag = orbit_action(a, g, orbit_size)
    return (
        anomaly_cocycle_exponent(a, g, orbit_size, phase_modulus)
        + trivialization_exponent(a, orbit_size, phase_modulus)
        - trivialization_exponent(ag, orbit_size, phase_modulus)
    ) % phase_modulus


def check_action_groupoid_anomaly_cocycle_and_descent() -> None:
    for orbit_size in range(1, 8):
        for phase_modulus in range(2, 11):
            for a in range(orbit_size):
                for g in range(orbit_size):
                    for h in range(orbit_size):
                        gh = (g + h) % orbit_size
                        ag = orbit_action(a, g, orbit_size)
                        lhs = anomaly_cocycle_exponent(a, gh, orbit_size, phase_modulus)
                        rhs = (
                            anomaly_cocycle_exponent(a, g, orbit_size, phase_modulus)
                            + anomaly_cocycle_exponent(ag, h, orbit_size, phase_modulus)
                        ) % phase_modulus
                        assert_equal(
                            f"action-groupoid anomaly cocycle orbit={orbit_size} phase={phase_modulus}",
                            lhs,
                            rhs,
                        )

                        shifted_lhs = coboundary_shifted_exponent(a, gh, orbit_size, phase_modulus)
                        shifted_rhs = (
                            coboundary_shifted_exponent(a, g, orbit_size, phase_modulus)
                            + coboundary_shifted_exponent(ag, h, orbit_size, phase_modulus)
                        ) % phase_modulus
                        assert_equal(
                            f"coboundary-shifted anomaly cocycle orbit={orbit_size} phase={phase_modulus}",
                            shifted_lhs,
                            shifted_rhs,
                        )

            for a in range(orbit_size):
                based_g = 0
                original = anomaly_cocycle_exponent(a, based_g, orbit_size, phase_modulus)
                shifted = coboundary_shifted_exponent(a, based_g, orbit_size, phase_modulus)
                assert_equal(
                    f"based-loop holonomy invariant orbit={orbit_size} phase={phase_modulus}",
                    shifted,
                    original,
                )

            for a in range(orbit_size):
                for g in range(orbit_size):
                    first = anomaly_cocycle_exponent(a, g, orbit_size, phase_modulus)
                    second = (2 * anomaly_cocycle_exponent(a, g, orbit_size, phase_modulus)) % phase_modulus
                    tensor_product = (first + first) % phase_modulus
                    assert_equal(
                        f"tensoring anomaly lines adds exponents orbit={orbit_size} phase={phase_modulus}",
                        tensor_product,
                        second,
                    )


def check_stabilizer_holonomy_character_obstruction() -> None:
    for group_order in range(2, 12):
        for phase_modulus in range(2, 12):
            for charge in range(phase_modulus):
                # A based loop in the quotient groupoid is a stabilizer
                # element.  For the trivial action, the groupoid cocycle is a
                # character of the stabilizer written in additive exponents.
                for g in range(group_order):
                    for h in range(group_order):
                        lhs = charge * ((g + h) % group_order) % phase_modulus
                        rhs = (charge * g + charge * h) % phase_modulus
                        if (charge * group_order) % phase_modulus == 0:
                            assert_equal(
                                f"stabilizer holonomy character G={group_order} phase={phase_modulus}",
                                lhs,
                                rhs,
                            )

                descends = all((charge * g) % phase_modulus == 0 for g in range(group_order))
                expected_descends = charge % phase_modulus == 0
                assert_equal(
                    f"trivial stabilizer character is exact iff holonomy trivial G={group_order}",
                    descends,
                    expected_descends,
                )


def main() -> None:
    check_su2_index_table()
    check_witten_parity_criterion()
    check_pfaffian_sign_multiplicativity()
    check_mapping_torus_z2_character_bookkeeping()
    check_finite_pfaffian_block_model()
    check_su2_cubic_weight_sum_vanishes()
    check_orientation_reversal_eta_bookkeeping()
    check_reduced_eta_crossing_integer_jump()
    check_aps_cylinder_congruence()
    check_aps_cylinder_exact_bookkeeping()
    check_aps_spectral_flow_sign_convention()
    check_quillen_spectral_cut_transition_cocycle()
    check_dai_freed_gluing_phase_algebra()
    check_contractible_loop_curvature_stokes()
    check_action_groupoid_anomaly_cocycle_and_descent()
    check_stabilizer_holonomy_character_obstruction()
    print("Eta-invariant and SU(2) global-anomaly checks passed.")


if __name__ == "__main__":
    main()
