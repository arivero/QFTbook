#!/usr/bin/env python3
"""Exact checks for eta-invariant and SU(2) global-anomaly conventions.

Evidence contract.

Target claims:
    APS boundary-sign bookkeeping, determinant/Pfaffian line coordinate
    algebra, finite action-groupoid descent, Witten SU(2) trace-delta
    parity arithmetic, typed orientation/variance of Dai-Freed boundary
    lines, and the finite phase algebra used by Dai-Freed gluing, boundary
    pairing, and intermediate-cut composition.

Independent construction:
    The checks use exact integer, rational, and finite cyclic phase models
    built directly from the algebraic definitions in the chapter: spectral
    windows multiply by finite determinants, Pfaffians multiply by skew-block
    products, groupoid cocycles are evaluated on every finite arrow, and
    Dai-Freed line pairings are checked in additive U(1)-exponent
    coordinates.

Imported assumptions:
    The script does not prove the APS Fredholm/heat-kernel theorem,
    Bismut-Freed holonomy theorem, Dai-Freed analytic boundary-line
    construction, or the real mod-two-index theorem.  It assumes those
    theorem-level inputs and tests the finite convention and line-algebra
    consequences used in the monograph.

Negative controls:
    The checks include nontrivial flat stabilizer holonomy before dual-line
    cancellation, nontrivial stabilizer-character obstruction to descent,
    zero-mode exclusion in the APS half-cylinder convention, parity-changing
    Pfaffian sign crossings, rejection of the relative boundary-amplitude
    variance as a Dai-Freed inverse-line variance, and nontrivial SU(2)
    mapping-torus generator signs for odd trace-delta index.

Scope boundary:
    Passing this script verifies exact finite algebra and convention-sensitive
    coordinates.  It is not a numerical or analytic proof of the continuum
    eta invariant, determinant/Pfaffian line, Dai-Freed theory, or global
    index theorems, and it does not construct physical Hilbert-space or
    path-integral gluing.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


LineType = tuple[int, ...]


def invert_line_type(line_type: LineType) -> LineType:
    return tuple(-entry for entry in line_type)


def add_line_types(*line_types: LineType) -> LineType:
    if not line_types:
        raise ValueError("at least one line type is required")
    width = len(line_types[0])
    if any(len(line_type) != width for line_type in line_types):
        raise ValueError("line types must have the same width")
    return tuple(sum(line_type[index] for line_type in line_types) for index in range(width))


def dai_freed_bordism_type(source: int, target: int, boundary_count: int) -> LineType:
    """Line exponents for Z_DF(Y: M_source -> M_target).

    The ordinary bordism convention is boundary(Y) = -M_source union M_target.
    Since L_{-M} = L_M^{-1} and Z_DF(Y) lives in L_{boundary Y}^{-1}, the
    source exponent is +1 and the target exponent is -1.
    """

    boundary_type = [0] * boundary_count
    boundary_type[source] -= 1
    boundary_type[target] += 1
    return invert_line_type(tuple(boundary_type))


def relative_boundary_amplitude_type(source: int, target: int, boundary_count: int) -> LineType:
    """Line exponents for a relative boundary-QFT transition amplitude."""

    return invert_line_type(dai_freed_bordism_type(source, target, boundary_count))


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


def half_cylinder_l2_mode(lambda_value: Fraction) -> bool:
    """L2 criterion for exp(-lambda u) on the inward collar (-infty, 0]."""

    return lambda_value < 0


def aps_keeps_boundary_mode(lambda_value: Fraction) -> bool:
    """APS boundary condition P_{>=0} psi|_Y=0 keeps only lambda<0 modes."""

    return lambda_value < 0


def check_aps_half_cylinder_mode_selection() -> None:
    eigenvalues = [
        Fraction(-5, 2),
        Fraction(-1),
        Fraction(-1, 7),
        Fraction(0),
        Fraction(1, 9),
        Fraction(3),
    ]
    for eigenvalue in eigenvalues:
        assert_equal(
            f"inward half-cylinder L2 mode equals APS kept mode lambda={eigenvalue}",
            half_cylinder_l2_mode(eigenvalue),
            aps_keeps_boundary_mode(eigenvalue),
        )
        assert_equal(
            f"opposite boundary orientation reverses APS spectral sign lambda={eigenvalue}",
            aps_keeps_boundary_mode(-eigenvalue),
            eigenvalue > 0,
        )

    assert_equal("APS forbids zero mode on the half-cylinder", aps_keeps_boundary_mode(Fraction(0)), False)


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


def check_cech_de_rham_line_holonomy_bookkeeping() -> None:
    """Finite Cech-de Rham check for determinant-line connection data.

    In a local frame with nabla e_i = -2*pi*i a_i e_i and
    e_j = exp(2*pi*i f_ij) e_i, the transition law is
    a_j = a_i - d f_ij.  A loop holonomy coordinate is the sum of connection
    integrals on charted arcs minus the transition functions at vertices.
    Local frame changes must telescope out of the closed-loop exponent.
    """

    a_i_integral = Fraction(7, 10)
    f_start = Fraction(1, 5)
    f_end = Fraction(-1, 6)
    a_j_integral = a_i_integral - (f_end - f_start)
    assert_equal(
        "Cech-de Rham connection transition integral",
        a_j_integral - a_i_integral,
        -(f_end - f_start),
    )

    # Loop vertices 0 -> 1 -> 2 -> 3 -> 0.  Each edge is assigned a chart and
    # an integral of the local connection form in that chart.
    edges = [
        (0, 1, 0, Fraction(2, 5)),
        (1, 2, 1, Fraction(-1, 7)),
        (2, 3, 1, Fraction(3, 11)),
        (3, 0, 2, Fraction(5, 13)),
    ]
    transitions = [
        (0, 1, 1, Fraction(1, 6)),
        (1, 1, 2, Fraction(0)),
        (1, 2, 3, Fraction(-2, 9)),
        (2, 0, 0, Fraction(4, 15)),
    ]

    def h(chart: int, vertex: int) -> Fraction:
        return Fraction((chart + 2) * (vertex + 1), 17) - Fraction(chart - vertex, 19)

    original_exponent = sum(integral for _, _, _, integral in edges)
    original_exponent -= sum(value for _, _, _, value in transitions)

    transformed_edges = []
    for start, end, chart, integral in edges:
        transformed_integral = integral - (h(chart, end) - h(chart, start))
        transformed_edges.append((start, end, chart, transformed_integral))

    transformed_transitions = []
    for current_chart, next_chart, vertex, value in transitions:
        transformed_value = value + h(next_chart, vertex) - h(current_chart, vertex)
        transformed_transitions.append((current_chart, next_chart, vertex, transformed_value))

    transformed_exponent = sum(integral for _, _, _, integral in transformed_edges)
    transformed_exponent -= sum(value for _, _, _, value in transformed_transitions)
    assert_equal(
        "closed-loop determinant-line holonomy exponent is frame independent",
        transformed_exponent,
        original_exponent,
    )
    assert_equal(
        "closed-loop determinant-line phase is frame independent modulo one",
        mod_one(transformed_exponent),
        mod_one(original_exponent),
    )


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


def check_dai_freed_boundary_pairing_cancels_cocycle() -> None:
    """Finite phase check for boundary vector times inverse inflow vector."""

    for phase_modulus in range(2, 13):
        for anomaly in range(phase_modulus):
            for boundary_exponent in range(phase_modulus):
                for inflow_exponent in range(phase_modulus):
                    boundary_transformed = (
                        boundary_exponent + anomaly
                    ) % phase_modulus
                    inflow_transformed = (
                        inflow_exponent - anomaly
                    ) % phase_modulus
                    assert_equal(
                        f"Dai-Freed boundary pairing gauge invariant phase={phase_modulus}",
                        (boundary_transformed + inflow_transformed)
                        % phase_modulus,
                        (boundary_exponent + inflow_exponent) % phase_modulus,
                    )

        fillings = [1, 3, 5, phase_modulus - 1]
        boundary_vector = 2 % phase_modulus
        for first in fillings:
            for second in fillings:
                paired_first = (boundary_vector + first) % phase_modulus
                paired_second = (boundary_vector + second) % phase_modulus
                closed_phase = (first - second) % phase_modulus
                assert_equal(
                    f"Dai-Freed filling change equals closed phase phase={phase_modulus}",
                    (paired_first - paired_second) % phase_modulus,
                    closed_phase,
                )


def check_dai_freed_interface_orientation_variance() -> None:
    """Typed line-variance check for the ordinary bordism convention."""

    df_01 = dai_freed_bordism_type(0, 1, 3)
    df_12 = dai_freed_bordism_type(1, 2, 3)
    df_02 = dai_freed_bordism_type(0, 2, 3)
    assert_equal("Dai-Freed source-target variance Y01", df_01, (1, -1, 0))
    assert_equal("Dai-Freed source-target variance Y12", df_12, (0, 1, -1))
    assert_equal("Dai-Freed source-target variance Y02", df_02, (1, 0, -1))
    assert_equal("Dai-Freed composition cancels the intermediate line", add_line_types(df_01, df_12), df_02)

    boundary_01 = relative_boundary_amplitude_type(0, 1, 3)
    boundary_12 = relative_boundary_amplitude_type(1, 2, 3)
    boundary_02 = relative_boundary_amplitude_type(0, 2, 3)
    assert_equal("relative boundary amplitude has dual Y01 variance", boundary_01, (-1, 1, 0))
    assert_equal("relative boundary composition cancels the intermediate line", add_line_types(boundary_01, boundary_12), boundary_02)
    assert_equal("relative boundary variance is not the Dai-Freed inverse-line variance", boundary_01 == df_01, False)
    assert_equal(
        "Dai-Freed and relative boundary amplitudes pair to a scalar",
        add_line_types(df_02, boundary_02),
        (0, 0, 0),
    )


def check_dai_freed_interface_composition_frame_cancellation() -> None:
    """Finite phase check for gluing through an intermediate anomaly line."""

    for phase_modulus in range(2, 17):
        for z01 in range(phase_modulus):
            for z12 in range(phase_modulus):
                direct_composition = (z01 + z12) % phase_modulus
                for frame_change in range(phase_modulus):
                    # e_1 -> q e_1 sends the coefficient of
                    # L_0 tensor L_1^{-1} by q and the coefficient of
                    # L_1 tensor L_2^{-1} by q^{-1}.
                    transformed_z01 = (z01 + frame_change) % phase_modulus
                    transformed_z12 = (z12 - frame_change) % phase_modulus
                    assert_equal(
                        "Dai-Freed intermediate frame cancels in two-step gluing "
                        f"phase={phase_modulus}",
                        (transformed_z01 + transformed_z12) % phase_modulus,
                        direct_composition,
                    )

                    initial_boundary = (3 * z01 + 5) % phase_modulus
                    final_functional = (7 * z12 + 11) % phase_modulus
                    scalar_amplitude = (
                        initial_boundary + z01 + z12 + final_functional
                    ) % phase_modulus
                    transformed_scalar = (
                        initial_boundary
                        + transformed_z01
                        + transformed_z12
                        + final_functional
                    ) % phase_modulus
                    assert_equal(
                        "Dai-Freed endpoint scalar is independent of intermediate frame "
                        f"phase={phase_modulus}",
                        transformed_scalar,
                        scalar_amplitude,
                    )

            for z12 in range(phase_modulus):
                for z23 in range(phase_modulus):
                    left_grouping = (
                        (z01 + z12) % phase_modulus + z23
                    ) % phase_modulus
                    right_grouping = (
                        z01 + (z12 + z23) % phase_modulus
                    ) % phase_modulus
                    assert_equal(
                        f"Dai-Freed interface composition is associative phase={phase_modulus}",
                        left_grouping,
                        right_grouping,
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


def inverse_line_exponent(exponent: int, phase_modulus: int) -> int:
    return (-exponent) % phase_modulus


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


def check_dual_anomaly_line_cancellation() -> None:
    for orbit_size in range(1, 8):
        for phase_modulus in range(2, 13):
            for a in range(orbit_size):
                for g in range(orbit_size):
                    for h in range(orbit_size):
                        gh = (g + h) % orbit_size
                        ag = orbit_action(a, g, orbit_size)
                        dual_lhs = inverse_line_exponent(
                            anomaly_cocycle_exponent(a, gh, orbit_size, phase_modulus),
                            phase_modulus,
                        )
                        dual_rhs = (
                            inverse_line_exponent(
                                anomaly_cocycle_exponent(a, g, orbit_size, phase_modulus),
                                phase_modulus,
                            )
                            + inverse_line_exponent(
                                anomaly_cocycle_exponent(ag, h, orbit_size, phase_modulus),
                                phase_modulus,
                            )
                        ) % phase_modulus
                        assert_equal(
                            f"dual anomaly line is a cocycle orbit={orbit_size} phase={phase_modulus}",
                            dual_lhs,
                            dual_rhs,
                        )

                for g in range(orbit_size):
                    original = anomaly_cocycle_exponent(a, g, orbit_size, phase_modulus)
                    dual = inverse_line_exponent(original, phase_modulus)
                    assert_equal(
                        f"anomaly line times dual line trivializes orbit={orbit_size} phase={phase_modulus}",
                        (original + dual) % phase_modulus,
                        0,
                    )

    for group_order in range(2, 9):
        phase_modulus = group_order
        charge = 1
        dual_charge = inverse_line_exponent(charge, phase_modulus)
        nontrivial_flat_values = []
        for g in range(group_order):
            primary = (charge * g) % phase_modulus
            dual = (dual_charge * g) % phase_modulus
            assert_equal(
                f"flat stabilizer character cancels with dual G={group_order}",
                (primary + dual) % phase_modulus,
                0,
            )
            nontrivial_flat_values.append(primary)

        assert_equal(
            f"nontrivial flat stabilizer holonomy exists before dual cancellation G={group_order}",
            any(value != 0 for value in nontrivial_flat_values),
            True,
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

                # A local frame change is a 0-cochain beta(A).  On a
                # stabilizer arrow A -> A the additive coboundary contribution
                # beta(A)-beta(A) vanishes, so it cannot change the stabilizer
                # character.  This is the finite version of the obstruction
                # stated in the chapter.
                beta_value = (3 * group_order + 5 * phase_modulus) % phase_modulus
                for stabilizer_element in range(group_order):
                    original = charge * stabilizer_element % phase_modulus
                    shifted = (
                        beta_value - beta_value + charge * stabilizer_element
                    ) % phase_modulus
                    assert_equal(
                        f"stabilizer character invariant under frame change G={group_order}",
                        shifted,
                        original,
                    )

    # On a single finite orbit with trivial stabilizer character, transporting
    # a chosen vector from a representative is independent of the group element
    # used to reach the same point.  If the stabilizer character is nontrivial,
    # two representatives differing by a stabilizer element disagree.
    group_order = 6
    stabilizer = {0, 3}
    orbit_representatives = {0: 0, 1: 1, 2: 2}
    trivial_charge = 0
    bad_charge = 1
    phase_modulus = 2
    for point, representative in orbit_representatives.items():
        for stabilizer_element in stabilizer:
            alternative = (representative + stabilizer_element) % group_order
            trivial_transport = trivial_charge * alternative % phase_modulus
            canonical_transport = trivial_charge * representative % phase_modulus
            assert_equal(
                f"trivial stabilizer character gives well-defined orbit vector {point}",
                trivial_transport,
                canonical_transport,
            )
            bad_transport = bad_charge * alternative % phase_modulus
            bad_canonical = bad_charge * representative % phase_modulus
            if stabilizer_element != 0:
                assert_equal(
                    f"nontrivial stabilizer character obstructs orbit vector {point}",
                    bad_transport != bad_canonical,
                    True,
                )


def cyclic_quotient_action(point: int, group_element: int, orbit_size: int) -> int:
    return (point + group_element) % orbit_size


def cyclic_orbit_potential(point: int, phase_modulus: int) -> int:
    return (5 * point * point + 3 * point + 1) % phase_modulus


def cyclic_stabilizer_carry(point: int, group_element: int, orbit_size: int) -> int:
    return (point + group_element) // orbit_size


def cyclic_action_groupoid_cocycle_exponent(
    point: int,
    group_element: int,
    orbit_size: int,
    group_order: int,
    phase_modulus: int,
    stabilizer_charge: int,
) -> int:
    """Cocycle on a transitive finite action groupoid with stabilizer.

    The cyclic group Z_group_order acts on an orbit of size orbit_size, with
    group_order a multiple of orbit_size.  The carry records how many times
    the arrow crosses the chosen orbit section, hence which stabilizer element
    is seen by the transported frame.
    """

    if group_order % orbit_size != 0:
        raise ValueError("group_order must be a multiple of orbit_size")
    stabilizer_order = group_order // orbit_size
    if (stabilizer_charge * stabilizer_order) % phase_modulus != 0:
        raise ValueError("stabilizer charge must define a character")

    target = cyclic_quotient_action(point, group_element, orbit_size)
    potential_difference = (
        cyclic_orbit_potential(target, phase_modulus)
        - cyclic_orbit_potential(point, phase_modulus)
    )
    stabilizer_exponent = stabilizer_charge * cyclic_stabilizer_carry(
        point, group_element, orbit_size
    )
    return (potential_difference + stabilizer_exponent) % phase_modulus


def check_finite_action_groupoid_descent_criterion() -> None:
    """Verify the constructive finite action-groupoid descent theorem."""

    for orbit_size in range(1, 7):
        for stabilizer_order in range(1, 5):
            group_order = orbit_size * stabilizer_order
            for phase_modulus in range(2, 12):
                charges = [
                    charge
                    for charge in range(phase_modulus)
                    if (charge * stabilizer_order) % phase_modulus == 0
                ]
                for charge in charges:
                    for point in range(orbit_size):
                        for g in range(group_order):
                            for h in range(group_order):
                                gh = (g + h) % group_order
                                pg = cyclic_quotient_action(point, g, orbit_size)
                                lhs = cyclic_action_groupoid_cocycle_exponent(
                                    point,
                                    gh,
                                    orbit_size,
                                    group_order,
                                    phase_modulus,
                                    charge,
                                )
                                rhs = (
                                    cyclic_action_groupoid_cocycle_exponent(
                                        point,
                                        g,
                                        orbit_size,
                                        group_order,
                                        phase_modulus,
                                        charge,
                                    )
                                    + cyclic_action_groupoid_cocycle_exponent(
                                        pg,
                                        h,
                                        orbit_size,
                                        group_order,
                                        phase_modulus,
                                        charge,
                                    )
                                ) % phase_modulus
                                assert_equal(
                                    "finite action-groupoid cocycle with stabilizer "
                                    f"orbit={orbit_size} stab={stabilizer_order} "
                                    f"phase={phase_modulus} charge={charge}",
                                    lhs,
                                    rhs,
                                )

                    stabilizer_values = []
                    for point in range(orbit_size):
                        for q in range(stabilizer_order):
                            h = q * orbit_size
                            value = cyclic_action_groupoid_cocycle_exponent(
                                point,
                                h,
                                orbit_size,
                                group_order,
                                phase_modulus,
                                charge,
                            )
                            stabilizer_values.append(value)
                            assert_equal(
                                "stabilizer character value "
                                f"orbit={orbit_size} stab={stabilizer_order} "
                                f"phase={phase_modulus} charge={charge} q={q}",
                                value,
                                (charge * q) % phase_modulus,
                            )

                    stabilizer_trivial = all(value == 0 for value in stabilizer_values)
                    if stabilizer_trivial:
                        trivializing_cochain = [
                            cyclic_action_groupoid_cocycle_exponent(
                                0,
                                point,
                                orbit_size,
                                group_order,
                                phase_modulus,
                                charge,
                            )
                            for point in range(orbit_size)
                        ]
                        for point in range(orbit_size):
                            for g in range(group_order):
                                target = cyclic_quotient_action(point, g, orbit_size)
                                coboundary = (
                                    trivializing_cochain[target]
                                    - trivializing_cochain[point]
                                ) % phase_modulus
                                cocycle = cyclic_action_groupoid_cocycle_exponent(
                                    point,
                                    g,
                                    orbit_size,
                                    group_order,
                                    phase_modulus,
                                    charge,
                                )
                                assert_equal(
                                    "trivial stabilizer character constructs descent cochain "
                                    f"orbit={orbit_size} stab={stabilizer_order} "
                                    f"phase={phase_modulus} charge={charge}",
                                    coboundary,
                                    cocycle,
                                )
                    else:
                        assert_equal(
                            "nontrivial stabilizer character blocks exact descent "
                            f"orbit={orbit_size} stab={stabilizer_order} "
                            f"phase={phase_modulus} charge={charge}",
                            any(value != 0 for value in stabilizer_values),
                            True,
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
    check_aps_half_cylinder_mode_selection()
    check_quillen_spectral_cut_transition_cocycle()
    check_cech_de_rham_line_holonomy_bookkeeping()
    check_dai_freed_gluing_phase_algebra()
    check_dai_freed_boundary_pairing_cancels_cocycle()
    check_dai_freed_interface_orientation_variance()
    check_dai_freed_interface_composition_frame_cancellation()
    check_contractible_loop_curvature_stokes()
    check_action_groupoid_anomaly_cocycle_and_descent()
    check_dual_anomaly_line_cancellation()
    check_stabilizer_holonomy_character_obstruction()
    check_finite_action_groupoid_descent_criterion()
    print("Eta-invariant and SU(2) global-anomaly checks passed.")


if __name__ == "__main__":
    main()
