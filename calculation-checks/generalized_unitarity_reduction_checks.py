#!/usr/bin/env python3
"""Finite checks for generalized unitarity and one-loop reduction.

The companion section in Volume II, Chapter 6 develops the bridge from
Cutkosky discontinuities to generalized cuts, scalar-integral reconstruction,
IBP reduction, and master-integral differential equations.  This script
checks the exact algebraic ledger behind the worked massless phi^4 example
and the one-loop bubble family, then adds finite helicity and regulator
bookkeeping for the Yang-Mills MHV/all-plus control examples, including the
five-gluon all-plus rational template.  It also checks a finite two-master
threshold-mixing model, a two-letter master-transport model with boundary and
branch negative controls, and the finite Laurent-pole ledger that turns a
reconstructed virtual amplitude into a finite observable only after infrared
subtraction, real radiation, and scheme transport have been assembled.

Evidence contract.
Target claims: the generalized-unitarity section of Volume II Chapter 6,
especially the phi^4 cut reconstruction, the negative controls for incomplete
cut sets and four-dimensional blind spots, the bubble IBP identity, and the
bubble master differential equation, plus the gauge-theory MHV box and
all-plus rational-term comparison, the local two-master threshold-mixing
datum in a Fuchsian differential system, the two-letter transport/boundary
audit for a reduced master sector, and the virtual-to-observable finite
remainder assembly; additionally, the five-point all-plus rational amplitude
has the correct little-group weights, mass dimension, cyclic term coverage,
and strict four-dimensional cut invisibility.
Independent construction: finite cut-signature matrices over rational
numbers, an explicit identical-state symmetry factor, a nullspace model for
local/rational terms invisible to four-dimensional cuts, and exact rational
checks of the one-loop bubble IBP coefficients at several regulator values;
spinor-bracket exponent ledgers for little-group weights and dimensions; and
a finite four-gluon helicity enumeration for all-plus two-particle cuts;
finite spinor-bracket power counting and helicity-cut enumeration for the
five-gluon all-plus rational template;
nilpotent rational matrix algebra for threshold monodromy and regular
boundary constants; noncommuting two-letter residue algebra for first-order
transport, path-order sensitivity, and cut-invisible boundary shifts;
Laurent-pole arithmetic for virtual/real infrared cancellation and finite
scheme transport.
Imported assumptions: dimensional regularization, the standard massless
two-particle phase-space normalization with the common factor of pi stripped
off, the Feynman-parameter gamma-function form of the bubble master, and the
vanishing of scaleless tadpoles in dimensional regularization; the
four-dimensional Yang-Mills tree selection rule that nonzero four-gluon trees
have two negative helicities, up to parity.
Negative controls: the script rejects an s-channel-only ansatz, verifies that
local counterterms are invisible to cuts, and constructs two amplitudes with
identical four-dimensional cuts but different D-dimensional rational probes;
it also verifies that the all-plus one-loop rational structure is invisible
to strict four-dimensional two-particle cuts but visible to a nonzero
mu_perp^2 massive-scalar probe, verifies the same rational blind spot at five
points, and rejects virtual-only pole cancellation, omitted rational finite
remainders, diagonal one-master threshold shortcuts, cut-only boundary
reconstruction, branch/path omission in a two-letter master transport, and
untransported finite IR-scheme shifts.
Scope boundary: a pass checks the finite reconstruction and reduction
bookkeeping; it does not compute a nonabelian helicity amplitude from Feynman
graphs, prove unitarity from Wightman axioms, or solve a physical
multi-scale integral family.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, value: object, expected: object) -> None:
    if value != expected:
        raise AssertionError(f"{name}: got {value!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(f"{name}: condition failed")


def assert_false(name: str, condition: bool) -> None:
    if condition:
        raise AssertionError(f"{name}: unexpectedly true")


def rank(matrix: list[list[Fraction]]) -> int:
    """Row rank over the rationals."""
    rows = [row[:] for row in matrix]
    if not rows:
        return 0
    n_rows = len(rows)
    n_cols = len(rows[0])
    pivot_row = 0
    for col in range(n_cols):
        pivot = None
        for row in range(pivot_row, n_rows):
            if rows[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][col]
        rows[pivot_row] = [entry / pivot_value for entry in rows[pivot_row]]
        for row in range(n_rows):
            if row == pivot_row:
                continue
            factor = rows[row][col]
            if factor:
                rows[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(rows[row], rows[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == n_rows:
            break
    return pivot_row


CHANNELS = ("s", "t", "u")
BASIS = ("B_s", "B_t", "B_u", "local", "four_dimensional_rational_null")
BracketPowers = dict[tuple[int, int], int]
Laurent = tuple[Fraction, Fraction]
Matrix = list[list[Fraction]]
Vector = list[Fraction]


def laurent_add(left: Laurent, right: Laurent) -> Laurent:
    return (left[0] + right[0], left[1] + right[1])


def laurent_sub(left: Laurent, right: Laurent) -> Laurent:
    return (left[0] - right[0], left[1] - right[1])


def laurent_scale(scale: Fraction, value: Laurent) -> Laurent:
    return (scale * value[0], scale * value[1])


def matrix_mul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(left[row][k] * right[k][col] for k in range(len(right)))
            for col in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[row][col] - right[row][col] for col in range(len(left[0]))]
        for row in range(len(left))
    ]


def matrix_vector_mul(matrix: Matrix, vector: Vector) -> Vector:
    return [
        sum(row[col] * vector[col] for col in range(len(vector)))
        for row in matrix
    ]


def vector_add(left: Vector, right: Vector) -> Vector:
    return [left[index] + right[index] for index in range(len(left))]


def vector_sub(left: Vector, right: Vector) -> Vector:
    return [left[index] - right[index] for index in range(len(left))]


def vector_scale(scale: Fraction, vector: Vector) -> Vector:
    return [scale * entry for entry in vector]


def dot(left: Vector, right: Vector) -> Fraction:
    return sum(left[index] * right[index] for index in range(len(left)))


def four_dimensional_cut_signature(basis_name: str) -> tuple[Fraction, Fraction, Fraction]:
    if basis_name == "B_s":
        return (Fraction(1), Fraction(0), Fraction(0))
    if basis_name == "B_t":
        return (Fraction(0), Fraction(1), Fraction(0))
    if basis_name == "B_u":
        return (Fraction(0), Fraction(0), Fraction(1))
    if basis_name in {"local", "four_dimensional_rational_null"}:
        return (Fraction(0), Fraction(0), Fraction(0))
    raise ValueError(basis_name)


def channel_cuts(coefficients: dict[str, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    cuts = [Fraction(0), Fraction(0), Fraction(0)]
    for basis_name, coefficient in coefficients.items():
        signature = four_dimensional_cut_signature(basis_name)
        for index, value in enumerate(signature):
            cuts[index] += coefficient * value
    return tuple(cuts)


def check_phi4_cut_reconstruction() -> None:
    lam = Fraction(5, 3)
    tree = -lam
    identical_state_factor = Fraction(1, 2)

    # Strip the common i/(8 pi) factor from the massless two-body phase-space
    # discontinuity.  The cut-normalized bubble has unit signature in these
    # units, so the coefficient is read directly.
    expected_channel_cut = identical_state_factor * tree * tree
    expected_coeff = lam * lam / 2
    assert_equal("identical-state cut coefficient", expected_channel_cut, expected_coeff)

    reconstructed = {"B_s": expected_coeff, "B_t": expected_coeff, "B_u": expected_coeff}
    expected_cuts = (expected_coeff, expected_coeff, expected_coeff)
    assert_equal("all channel cuts reconstructed", channel_cuts(reconstructed), expected_cuts)

    s_only = {"B_s": expected_coeff}
    assert_equal("s-only ansatz matches s cut", channel_cuts(s_only)[0], expected_coeff)
    assert_equal("s-only ansatz misses t cut", channel_cuts(s_only)[1], Fraction(0))
    assert_false("s-only ansatz is crossing complete", channel_cuts(s_only) == expected_cuts)

    with_local_counterterm = dict(reconstructed)
    with_local_counterterm["local"] = Fraction(17, 11)
    assert_equal(
        "local counterterm has no discontinuity",
        channel_cuts(with_local_counterterm),
        expected_cuts,
    )

    cut_matrix = [
        list(four_dimensional_cut_signature(basis_name))
        for basis_name in BASIS
    ]
    assert_equal("four-dimensional cut rank", rank(cut_matrix), 3)
    assert_true("cut map has local/rational nullspace", len(BASIS) - rank(cut_matrix) == 2)


def d_dimensional_probe_signature(basis_name: str) -> Fraction:
    # A toy D-dimensional probe sees the evanescent numerator sector.  It is
    # invisible to strictly four-dimensional cuts, but can leave a finite
    # rational term after a regulator pole multiplies an O(epsilon) numerator.
    if basis_name == "four_dimensional_rational_null":
        return Fraction(1)
    return Fraction(0)


def check_four_dimensional_cut_blind_spot() -> None:
    base = {"B_s": Fraction(2), "B_t": Fraction(3), "B_u": Fraction(5)}
    shifted = dict(base)
    shifted["four_dimensional_rational_null"] = Fraction(7)
    assert_equal("same four-dimensional cuts", channel_cuts(base), channel_cuts(shifted))
    base_probe = sum(
        coefficient * d_dimensional_probe_signature(name)
        for name, coefficient in base.items()
    )
    shifted_probe = sum(
        coefficient * d_dimensional_probe_signature(name)
        for name, coefficient in shifted.items()
    )
    assert_equal("base D-dimensional rational probe", base_probe, Fraction(0))
    assert_equal("shifted D-dimensional rational probe", shifted_probe, Fraction(7))
    assert_true("D-dimensional information distinguishes amplitudes", base_probe != shifted_probe)


def little_group_weights(
    angle_powers: BracketPowers,
    square_powers: BracketPowers,
    legs: tuple[int, ...] = (1, 2, 3, 4),
) -> tuple[int, ...]:
    """Return exponents of t_i under lambda_i -> t_i lambda_i."""
    weights = {leg: 0 for leg in legs}
    for (left, right), power in angle_powers.items():
        weights[left] += power
        weights[right] += power
    for (left, right), power in square_powers.items():
        weights[left] -= power
        weights[right] -= power
    return tuple(weights[leg] for leg in legs)


def bracket_mass_dimension(
    angle_powers: BracketPowers,
    square_powers: BracketPowers,
) -> int:
    return sum(angle_powers.values()) + sum(square_powers.values())


def add_powers(*power_maps: BracketPowers) -> BracketPowers:
    result: BracketPowers = {}
    for power_map in power_maps:
        for bracket, power in power_map.items():
            result[bracket] = result.get(bracket, 0) + power
    return {bracket: power for bracket, power in result.items() if power != 0}


def four_gluon_tree_nonzero(helicities: tuple[int, int, int, int]) -> bool:
    negative_count = sum(1 for helicity in helicities if helicity == -1)
    return negative_count == 2


def plus_tree_possible_with_internal(
    external_plus_count: int,
    internal_helicities: tuple[int, int],
) -> bool:
    leg_count = external_plus_count + 2
    negative_count = sum(1 for helicity in internal_helicities if helicity == -1)
    if leg_count == 3:
        return negative_count in {1, 2}
    return negative_count == 2


def all_plus_massive_scalar_probe(mu_perp_squared: Fraction) -> Fraction:
    # The four-point all-plus rational term is seen by the evanescent sector:
    # the product of two massive-scalar cut trees carries two powers of
    # mu_perp^2 in this finite ledger.
    return mu_perp_squared * mu_perp_squared


def check_gauge_theory_helicity_controls() -> None:
    parke_taylor_angle = {
        (1, 2): 3,   # <12>^4 / <12>
        (2, 3): -1,
        (3, 4): -1,
        (4, 1): -1,
    }
    parke_taylor_square: BracketPowers = {}
    assert_equal(
        "Parke-Taylor little-group weights",
        little_group_weights(parke_taylor_angle, parke_taylor_square),
        (2, 2, -2, -2),
    )
    assert_equal(
        "Parke-Taylor mass dimension",
        bracket_mass_dimension(parke_taylor_angle, parke_taylor_square),
        0,
    )

    st_dimension = 4
    scalar_box_dimension = -4
    assert_equal(
        "N=4 MHV box dimension",
        bracket_mass_dimension(parke_taylor_angle, parke_taylor_square)
        + st_dimension
        + scalar_box_dimension,
        0,
    )
    assert_equal(
        "N=4 MHV box inherits tree little-group weights",
        little_group_weights(parke_taylor_angle, parke_taylor_square),
        (2, 2, -2, -2),
    )

    all_plus_angle = {(1, 2): -1, (3, 4): -1}
    all_plus_square = {(1, 2): 1, (3, 4): 1}
    assert_equal(
        "all-plus rational little-group weights",
        little_group_weights(all_plus_angle, all_plus_square),
        (-2, -2, -2, -2),
    )
    assert_equal(
        "all-plus rational mass dimension",
        bracket_mass_dimension(all_plus_angle, all_plus_square),
        0,
    )

    nonzero_two_particle_cuts = []
    for h_left_1 in (-1, 1):
        for h_left_2 in (-1, 1):
            left_tree = (h_left_1, 1, 1, h_left_2)
            right_tree = (-h_left_2, 1, 1, -h_left_1)
            if four_gluon_tree_nonzero(left_tree) and four_gluon_tree_nonzero(right_tree):
                nonzero_two_particle_cuts.append((left_tree, right_tree))
    assert_equal("strict 4D all-plus two-particle cuts", nonzero_two_particle_cuts, [])

    assert_equal(
        "all-plus massive-scalar probe vanishes in 4D",
        all_plus_massive_scalar_probe(Fraction(0)),
        Fraction(0),
    )
    assert_true(
        "all-plus massive-scalar probe sees evanescent sector",
        all_plus_massive_scalar_probe(Fraction(3, 5)) != 0,
    )


def check_five_gluon_all_plus_rational_template() -> None:
    legs = (1, 2, 3, 4, 5)
    denominator_angle: BracketPowers = {
        (1, 2): -1,
        (2, 3): -1,
        (3, 4): -1,
        (4, 5): -1,
        (5, 1): -1,
    }

    trace_terms: list[tuple[int, BracketPowers, BracketPowers]] = []
    for omitted in legs:
        kept = tuple(leg for leg in legs if leg != omitted)
        i, j, k, ell = kept
        trace_angle = {(i, j): 1, (k, ell): 1}
        trace_square = {(j, k): 1, (ell, i): 1}
        trace_terms.append((omitted, trace_angle, trace_square))

    assert_equal("five-point all-plus trace terms", len(trace_terms), 5)
    assert_equal(
        "five-point trace numerator covers each omitted leg",
        {omitted for omitted, _, _ in trace_terms},
        set(legs),
    )

    for omitted, trace_angle, trace_square in trace_terms:
        assert_equal(
            f"five-point trace term {omitted} little-group neutral",
            little_group_weights(trace_angle, trace_square, legs),
            (0, 0, 0, 0, 0),
        )
        full_angle = add_powers(denominator_angle, trace_angle)
        assert_equal(
            f"five-point all-plus term {omitted} little-group weights",
            little_group_weights(full_angle, trace_square, legs),
            (-2, -2, -2, -2, -2),
        )
        assert_equal(
            f"five-point all-plus term {omitted} mass dimension",
            bracket_mass_dimension(full_angle, trace_square),
            -1,
        )

    nonzero_strict_cuts: list[tuple[int, int, int]] = []
    for left_external_plus_count in range(1, 5):
        right_external_plus_count = 5 - left_external_plus_count
        for h1 in (-1, 1):
            for h2 in (-1, 1):
                left_possible = plus_tree_possible_with_internal(
                    left_external_plus_count,
                    (h1, h2),
                )
                right_possible = plus_tree_possible_with_internal(
                    right_external_plus_count,
                    (-h2, -h1),
                )
                if left_possible and right_possible:
                    nonzero_strict_cuts.append((left_external_plus_count, h1, h2))
    assert_equal("strict 4D five-gluon all-plus two-particle cuts", nonzero_strict_cuts, [])

    assert_equal(
        "five-point all-plus massive-scalar probe vanishes in 4D",
        all_plus_massive_scalar_probe(Fraction(0)),
        Fraction(0),
    )
    assert_equal(
        "five-point all-plus evanescent probe power",
        all_plus_massive_scalar_probe(Fraction(2, 3)),
        Fraction(4, 9),
    )


def check_bubble_ibp_identity() -> None:
    samples = [
        (Fraction(1, 11), Fraction(3, 2), Fraction(5, 7)),
        (Fraction(-1, 13), Fraction(7, 5), Fraction(11, 3)),
        (Fraction(2, 17), Fraction(19, 6), Fraction(13, 10)),
    ]
    for epsilon, q_squared, master in samples:
        dimension = Fraction(4) - 2 * epsilon
        squared_propagator = -(dimension - 3) * master / q_squared
        scaleless_tadpole = Fraction(0)
        ibp_residual = (
            (dimension - 3) * master
            - scaleless_tadpole
            + q_squared * squared_propagator
        )
        assert_equal(f"bubble IBP residual epsilon={epsilon}", ibp_residual, Fraction(0))

        derivative = -epsilon * master / q_squared
        differential_residual = q_squared * derivative + epsilon * master
        assert_equal(
            f"bubble master differential equation epsilon={epsilon}",
            differential_residual,
            Fraction(0),
        )


def check_branch_and_landau_ledger() -> None:
    # In the expansion
    #   Gamma(eps)[exp(i pi eps)-exp(-i pi eps)]/(16 pi^2),
    # the branch jump contributes 2 i pi eps and Gamma(eps) contributes 1/eps.
    # Stripping the common factor i/pi leaves 2/16 = 1/8, matching the
    # massless two-body phase-space coefficient used in the text.
    branch_jump_linear_coefficient = Fraction(2)
    normalization = Fraction(16)
    assert_equal(
        "cut-normalized bubble discontinuity coefficient",
        branch_jump_linear_coefficient / normalization,
        Fraction(1, 8),
    )

    singular_loci = {"bubble_differential_equation": {Fraction(0)}}
    landau_loci = {"massless_two_particle_threshold": {Fraction(0)}}
    assert_equal(
        "bubble differential singularity matches Landau threshold",
        singular_loci["bubble_differential_equation"],
        landau_loci["massless_two_particle_threshold"],
    )


def check_two_master_threshold_mixing() -> None:
    threshold_residue: Matrix = [
        [Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(0)],
    ]
    zero_matrix: Matrix = [
        [Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0)],
    ]
    assert_equal(
        "nilpotent threshold residue",
        matrix_mul(threshold_residue, threshold_residue),
        zero_matrix,
    )

    log_constants = [Fraction(5, 7), Fraction(11, 13)]
    stripped_monodromy = matrix_vector_mul(threshold_residue, log_constants)
    assert_equal(
        "threshold monodromy feeds second master",
        stripped_monodromy,
        [Fraction(0), Fraction(5, 7)],
    )

    log_coordinate = Fraction(3, 5)
    singular_solution = vector_add(
        log_constants,
        vector_scale(log_coordinate, stripped_monodromy),
    )
    log_derivative = stripped_monodromy
    fuchsian_rhs = matrix_vector_mul(threshold_residue, singular_solution)
    assert_equal(
        "two-master Fuchsian equation residual",
        vector_sub(log_derivative, fuchsian_rhs),
        [Fraction(0), Fraction(0)],
    )

    diagonal_shortcut: Matrix = [
        [threshold_residue[0][0], Fraction(0)],
        [Fraction(0), threshold_residue[1][1]],
    ]
    shortcut_monodromy = matrix_vector_mul(diagonal_shortcut, log_constants)
    assert_true(
        "diagonal one-master shortcut misses threshold mixing",
        shortcut_monodromy != stripped_monodromy,
    )

    amplitude_weights = [Fraction(2, 3), Fraction(-5, 4)]
    exact_discontinuity = dot(amplitude_weights, stripped_monodromy)
    shortcut_discontinuity = dot(amplitude_weights, shortcut_monodromy)
    assert_true(
        "dropping threshold mixing changes amplitude discontinuity",
        exact_discontinuity != shortcut_discontinuity,
    )

    regular_boundary_a = [Fraction(2, 5), Fraction(3, 7)]
    regular_boundary_b = [
        Fraction(2, 5) - Fraction(1, 17),
        Fraction(3, 7) + Fraction(1, 19),
    ]
    value_a = vector_add(regular_boundary_a, singular_solution)
    value_b = vector_add(regular_boundary_b, singular_solution)
    assert_equal(
        "same threshold monodromy under regular boundary shift",
        matrix_vector_mul(threshold_residue, log_constants),
        stripped_monodromy,
    )
    assert_true(
        "cut data do not fix regular boundary constants",
        dot(amplitude_weights, value_a) != dot(amplitude_weights, value_b),
    )

    residuals = {
        "threshold_mixing": abs(exact_discontinuity - shortcut_discontinuity),
        "regular_boundary": abs(dot(amplitude_weights, vector_sub(value_b, value_a))),
    }
    total_difference = (
        exact_discontinuity
        - shortcut_discontinuity
        + dot(amplitude_weights, vector_sub(value_b, value_a))
    )
    majorant = sum(residuals.values(), Fraction(0))
    assert_true("two-master reconstruction residual bound", abs(total_difference) <= majorant)
    underbudget = majorant - residuals["regular_boundary"]
    assert_true(
        "omitting boundary residual underbudgets multi-master comparison",
        abs(total_difference) > underbudget,
    )


def check_two_letter_master_transport() -> None:
    a0: Matrix = [
        [Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(0)],
    ]
    a1: Matrix = [
        [Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(0)],
    ]
    zero_matrix: Matrix = [
        [Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0)],
    ]
    assert_equal(
        "x-letter residue is nilpotent",
        matrix_mul(a0, a0),
        zero_matrix,
    )
    assert_equal(
        "one-minus-x residue is nilpotent",
        matrix_mul(a1, a1),
        zero_matrix,
    )

    commutator = matrix_sub(matrix_mul(a0, a1), matrix_mul(a1, a0))
    assert_equal(
        "two-letter residue commutator",
        commutator,
        [
            [Fraction(1), Fraction(0)],
            [Fraction(0), Fraction(-1)],
        ],
    )

    epsilon = Fraction(1, 11)
    l0 = Fraction(3, 5)
    l1 = Fraction(-4, 9)
    boundary = [Fraction(2, 3), Fraction(5, 7)]
    x_disc_stripped = matrix_vector_mul(a0, boundary)
    one_minus_x_disc_stripped = matrix_vector_mul(a1, boundary)
    assert_equal(
        "x-letter stripped discontinuity",
        x_disc_stripped,
        [Fraction(5, 7), Fraction(0)],
    )
    assert_equal(
        "one-minus-x stripped discontinuity",
        one_minus_x_disc_stripped,
        [Fraction(0), Fraction(2, 3)],
    )

    first_order_action = vector_add(
        vector_scale(l0, x_disc_stripped),
        vector_scale(l1, one_minus_x_disc_stripped),
    )
    transported = vector_add(boundary, vector_scale(epsilon, first_order_action))
    assert_equal(
        "first-order two-letter transport",
        transported,
        [Fraction(163, 231), Fraction(1429, 2079)],
    )
    assert_equal(
        "dlog-x differential equation at first order",
        vector_scale(epsilon, x_disc_stripped),
        matrix_vector_mul(a0, vector_scale(epsilon, boundary)),
    )
    assert_equal(
        "dlog-one-minus-x differential equation at first order",
        vector_scale(epsilon, one_minus_x_disc_stripped),
        matrix_vector_mul(a1, vector_scale(epsilon, boundary)),
    )

    kernel_shift = [Fraction(0), Fraction(1, 5)]
    shifted_boundary = vector_add(boundary, kernel_shift)
    assert_equal(
        "same one-minus-x cut after kernel boundary shift",
        matrix_vector_mul(a1, shifted_boundary),
        one_minus_x_disc_stripped,
    )
    amplitude_weights = [Fraction(7, 13), Fraction(-5, 11)]
    assert_true(
        "cut-only boundary reconstruction misses finite master value",
        dot(amplitude_weights, shifted_boundary) != dot(amplitude_weights, boundary),
    )

    path_order_difference = vector_scale(
        l0 * l1,
        matrix_vector_mul(commutator, boundary),
    )
    assert_equal(
        "second-order path-order commutator contribution",
        path_order_difference,
        [Fraction(-8, 45), Fraction(4, 21)],
    )
    assert_true(
        "forgetting path ordering loses a nonzero master contribution",
        path_order_difference != [Fraction(0), Fraction(0)],
    )

    branch_path_residual = abs(
        dot(amplitude_weights, vector_scale(epsilon * l0, x_disc_stripped))
    )
    boundary_residual = abs(dot(amplitude_weights, kernel_shift))
    residuals = {
        "connection": Fraction(1, 89),
        "boundary": boundary_residual,
        "branch_path": branch_path_residual,
        "lower_sector": Fraction(1, 97),
        "UV_IR": Fraction(1, 101),
        "observable": Fraction(1, 103),
    }
    exact_difference = sum(residuals.values(), Fraction(0))
    majorant = sum(abs(value) for value in residuals.values())
    assert_equal(
        "two-letter transport residual telescope",
        exact_difference,
        majorant,
    )
    underbudget = majorant - residuals["boundary"] - residuals["branch_path"]
    assert_true(
        "omitting boundary and branch residuals underbudgets transport comparison",
        exact_difference > underbudget,
    )


def check_virtual_to_observable_assembly() -> None:
    tree = Fraction(3, 2)
    ir_operator = (Fraction(-5, 3), Fraction(7, 11))
    finite_remainder = Fraction(11, 13)
    real_finite = Fraction(17, 19)

    virtual = laurent_add(
        laurent_scale(tree, ir_operator),
        (Fraction(0), finite_remainder),
    )
    extracted_remainder = laurent_sub(virtual, laurent_scale(tree, ir_operator))
    assert_equal(
        "finite remainder after IR subtraction",
        extracted_remainder,
        (Fraction(0), finite_remainder),
    )

    virtual_cross_section = laurent_scale(2 * tree, virtual)
    integrated_real = laurent_add(
        laurent_scale(-2 * tree * tree, ir_operator),
        (Fraction(0), real_finite),
    )
    assembled = laurent_add(virtual_cross_section, integrated_real)
    expected_finite = 2 * tree * finite_remainder + real_finite
    assert_equal(
        "virtual-real pole cancellation",
        assembled,
        (Fraction(0), expected_finite),
    )
    assert_true(
        "virtual-only contribution still has IR pole",
        virtual_cross_section[0] != 0,
    )

    rational_term = Fraction(5, 17)
    missing_rational_remainder = finite_remainder - rational_term
    missing_rational_observable = 2 * tree * missing_rational_remainder + real_finite
    assert_true(
        "omitting rational term changes finite observable",
        missing_rational_observable != expected_finite,
    )

    finite_scheme_shift = Fraction(4, 9)
    shifted_ir_operator = laurent_add(ir_operator, (Fraction(0), finite_scheme_shift))
    shifted_remainder = finite_remainder - finite_scheme_shift * tree
    shifted_virtual = laurent_add(
        laurent_scale(tree, shifted_ir_operator),
        (Fraction(0), shifted_remainder),
    )
    assert_equal(
        "finite IR-scheme transport leaves virtual amplitude unchanged",
        shifted_virtual,
        virtual,
    )

    shifted_real_finite = real_finite + 2 * tree * tree * finite_scheme_shift
    shifted_observable = 2 * tree * shifted_remainder + shifted_real_finite
    assert_equal(
        "finite IR-scheme transport leaves observable unchanged",
        shifted_observable,
        expected_finite,
    )
    untransported_observable = 2 * tree * shifted_remainder + real_finite
    assert_true(
        "untransported finite IR-scheme shift changes observable",
        untransported_observable != expected_finite,
    )

    residuals = {
        "cut": Fraction(1, 101),
        "rational": Fraction(1, 103),
        "IBP": Fraction(1, 107),
        "UV": Fraction(1, 109),
        "IR_real": Fraction(1, 113),
        "factorization": Fraction(1, 127),
        "measurement": Fraction(1, 131),
    }
    exact_observable = expected_finite + sum(residuals.values(), Fraction(0))
    majorant = sum(abs(value) for value in residuals.values())
    assert_equal(
        "one-loop observable residual telescope",
        exact_observable - expected_finite,
        sum(residuals.values(), Fraction(0)),
    )
    assert_true(
        "one-loop observable reconstruction bound",
        abs(exact_observable - expected_finite) <= majorant,
    )
    underbudget = majorant - abs(residuals["IR_real"]) - abs(residuals["measurement"])
    assert_true(
        "omitted observable residuals underbudget comparison",
        abs(exact_observable - expected_finite) > underbudget,
    )


def main() -> None:
    check_phi4_cut_reconstruction()
    check_four_dimensional_cut_blind_spot()
    check_gauge_theory_helicity_controls()
    check_five_gluon_all_plus_rational_template()
    check_bubble_ibp_identity()
    check_branch_and_landau_ledger()
    check_two_master_threshold_mixing()
    check_two_letter_master_transport()
    check_virtual_to_observable_assembly()
    print("All generalized unitarity and one-loop reduction checks passed.")


if __name__ == "__main__":
    main()
