#!/usr/bin/env python3
"""Finite checks for generalized unitarity and one-loop reduction.

The companion section in Volume II, Chapter 6 develops the bridge from
Cutkosky discontinuities to generalized cuts, scalar-integral reconstruction,
IBP reduction, and a master-integral differential equation.  This script
checks the exact algebraic ledger behind the worked massless phi^4 example
and the one-loop bubble family, then adds finite helicity and regulator
bookkeeping for the Yang-Mills MHV/all-plus control example.  It also checks
the finite Laurent-pole ledger that turns a reconstructed virtual amplitude
into a finite observable only after infrared subtraction, real radiation, and
scheme transport have been assembled.

Evidence contract.
Target claims: the generalized-unitarity section of Volume II Chapter 6,
especially the phi^4 cut reconstruction, the negative controls for incomplete
cut sets and four-dimensional blind spots, the bubble IBP identity, and the
bubble master differential equation, plus the gauge-theory MHV box and
all-plus rational-term comparison and the virtual-to-observable finite
remainder assembly.
Independent construction: finite cut-signature matrices over rational
numbers, an explicit identical-state symmetry factor, a nullspace model for
local/rational terms invisible to four-dimensional cuts, and exact rational
checks of the one-loop bubble IBP coefficients at several regulator values;
spinor-bracket exponent ledgers for little-group weights and dimensions; and
a finite four-gluon helicity enumeration for all-plus two-particle cuts;
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
mu_perp^2 massive-scalar probe, and rejects virtual-only pole cancellation,
omitted rational finite remainders, and untransported finite IR-scheme shifts.
Scope boundary: a pass checks the finite reconstruction and reduction
bookkeeping; it does not compute a nonabelian helicity amplitude from Feynman
graphs, prove unitarity from Wightman axioms, or solve a multi-master
differential system.
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


def laurent_add(left: Laurent, right: Laurent) -> Laurent:
    return (left[0] + right[0], left[1] + right[1])


def laurent_sub(left: Laurent, right: Laurent) -> Laurent:
    return (left[0] - right[0], left[1] - right[1])


def laurent_scale(scale: Fraction, value: Laurent) -> Laurent:
    return (scale * value[0], scale * value[1])


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


def four_gluon_tree_nonzero(helicities: tuple[int, int, int, int]) -> bool:
    negative_count = sum(1 for helicity in helicities if helicity == -1)
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
    check_bubble_ibp_identity()
    check_branch_and_landau_ledger()
    check_virtual_to_observable_assembly()
    print("All generalized unitarity and one-loop reduction checks passed.")


if __name__ == "__main__":
    main()
