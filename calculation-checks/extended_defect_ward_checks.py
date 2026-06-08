#!/usr/bin/env python3
"""Finite checks for extended-defect Ward and fusion formulas.

Evidence contract.
Target claims: the finite higher-form Ward algebra in Volume IX, Chapter 2,
including the local integer linking chart, the topology restrictions on global
integer linking, the degree distinction between finite-background
characteristic classes and operator holonomy data, the separation between
background gauge cochains and closed symmetry parameters, torsion linking, and
junction-charge conservation.
Independent construction: exact arithmetic in finite cyclic groups, a homology
model of nonbounding loops on T^3, an intersection-pairing model of
bounding-chain ambiguity, local signed-crossing recovery of the integer
meridian rule, finite degree-checked cochain evaluation, transgression of a
defect class to a degree-p complement datum, a finite cochain Stokes model for
background gauge covariance versus flat symmetry action, and the lens-space
torsion pairing a*b/n in Q/Z.
Imported assumptions: oriented closed manifolds for the global torsion-pairing
model, the standard degree condition
Tor H_{D-p-1}(M) x Tor H_p(M) -> Q/Z, and the use of finite homology models
as topology negative controls rather than continuum QFT constructions.
Negative controls: two noncontractible loops on T^3 do not start the
bounding-chain integer-linking construction; two bounding chains whose
difference has nonzero intersection with the charged cycle give different
integers; a torsion pairing returns Q/Z data rather than canonical integers.
Evaluating an H^{p+1} characteristic class directly on an H_p charged cycle is
rejected as a degree error.  A closed degree-p symmetry cocycle is rejected as a
source of a nonzero background coboundary shift.
Scope boundary: these checks do not prove Alexander duality, construct
topological defect operators in a continuum QFT, or classify all possible
global higher-form backgrounds.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(lhs, rhs, message: str) -> None:
    if lhs != rhs:
        raise AssertionError(f"{message}: {lhs!r} != {rhs!r}")


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def zn_phase_exponent(n: int, symmetry_label: int, charge_label: int, linking: int) -> int:
    """Return the numerator exponent modulo n for exp(2 pi i exponent/n)."""

    return (symmetry_label * charge_label * linking) % n


def mod_one(value: Fraction) -> Fraction:
    return value - (value.numerator // value.denominator)


def check_group_like_fusion() -> None:
    for n in range(2, 13):
        for a in range(n):
            for b in range(n):
                fused = (a + b) % n
                assert_equal((fused - b) % n, a, "left inverse in Z_n fusion")
                assert_equal((fused - a) % n, b, "right inverse in Z_n fusion")
                for c in range(n):
                    lhs = ((a + b) % n + c) % n
                    rhs = (a + (b + c) % n) % n
                    assert_equal(lhs, rhs, "associativity of Z_n fusion")


def check_ward_phase_multiplicativity() -> None:
    for n in range(2, 13):
        for a in range(n):
            for b in range(n):
                for q in range(n):
                    for linking in range(-3, 4):
                        fused = (a + b) % n
                        lhs = zn_phase_exponent(n, fused, q, linking)
                        rhs = (
                            zn_phase_exponent(n, a, q, linking)
                            + zn_phase_exponent(n, b, q, linking)
                        ) % n
                        assert_equal(lhs, rhs, "Ward phase under defect fusion")


def check_orientation_and_charge_reversal() -> None:
    for n in range(2, 13):
        for a in range(n):
            for q in range(n):
                for linking in range(-3, 4):
                    original = zn_phase_exponent(n, a, q, linking)
                    reverse_linking = zn_phase_exponent(n, a, q, -linking)
                    reverse_symmetry = zn_phase_exponent(n, (-a) % n, q, linking)
                    reverse_charge = zn_phase_exponent(n, a, (-q) % n, linking)
                    assert_equal(
                        (original + reverse_linking) % n,
                        0,
                        "orientation reversal in linking",
                    )
                    assert_equal(
                        (original + reverse_symmetry) % n,
                        0,
                        "inverse symmetry defect",
                    )
                    assert_equal(
                        (original + reverse_charge) % n,
                        0,
                        "opposite charged operator",
                    )


def check_linking_dimension_bookkeeping() -> None:
    for dimension in range(2, 12):
        for p in range(dimension):
            symmetry_defect_dim = dimension - p - 1
            charged_operator_dim = p
            assert_equal(
                symmetry_defect_dim + charged_operator_dim,
                dimension - 1,
                "linking dimensions sum to D-1",
            )
            bounding_chain_dim = symmetry_defect_dim + 1
            assert_equal(
                bounding_chain_dim + charged_operator_dim,
                dimension,
                "intersection dimensions sum to D",
            )


def check_local_meridian_integer_linking_chart() -> None:
    for n in range(2, 13):
        for symmetry_label in range(n):
            for charge_label in range(n):
                positive_crossing = [1]
                negative_crossing = [-1]
                canceling_isotopy = [1, -1, 1, -1]

                assert_equal(
                    zn_phase_exponent(
                        n,
                        symmetry_label,
                        charge_label,
                        sum(positive_crossing),
                    ),
                    (symmetry_label * charge_label) % n,
                    "local positive meridian crossing recovers the Ward phase",
                )
                assert_equal(
                    (
                        zn_phase_exponent(
                            n,
                            symmetry_label,
                            charge_label,
                            sum(positive_crossing),
                        )
                        + zn_phase_exponent(
                            n,
                            symmetry_label,
                            charge_label,
                            sum(negative_crossing),
                        )
                    )
                    % n,
                    0,
                    "opposite local crossings cancel",
                )
                assert_equal(
                    zn_phase_exponent(
                        n,
                        symmetry_label,
                        charge_label,
                        sum(canceling_isotopy),
                    ),
                    0,
                    "local isotopy away from charge has zero net crossing",
                )


def check_t3_noncontractible_loops_have_no_canonical_integer_linking() -> None:
    """A T^3 homology class must vanish before the bounding-chain formula starts."""

    def bounds_in_t3_h1(homology_class: tuple[int, int, int]) -> bool:
        return homology_class == (0, 0, 0)

    x_loop = (1, 0, 0)
    y_loop = (0, 1, 0)
    small_contractible_loop = (0, 0, 0)

    assert_true(
        not bounds_in_t3_h1(x_loop),
        "noncontractible T^3 loop does not bound an integral two-chain",
    )
    assert_true(
        not bounds_in_t3_h1(y_loop),
        "a second noncontractible T^3 loop also lacks a bounding chain",
    )
    assert_true(
        bounds_in_t3_h1(small_contractible_loop),
        "a local small loop is the homology-zero case where local linking can start",
    )


def check_bounding_chain_ambiguity_requires_homology_condition() -> None:
    """Model B-B' as the S^2 generator in S^2 x S^1."""

    def intersection_with_charged_cycle(closed_two_cycle_coeff: int, one_cycle_coeff: int) -> int:
        return closed_two_cycle_coeff * one_cycle_coeff

    ambiguity = intersection_with_charged_cycle(1, 1)
    assert_equal(
        ambiguity,
        1,
        "bounding chains differing by a closed cycle can change B dot Sigma",
    )
    assert_equal(
        intersection_with_charged_cycle(1, 0),
        0,
        "ambiguity vanishes when Sigma pairs trivially with ambient homology",
    )
    assert_equal(
        intersection_with_charged_cycle(0, 1),
        0,
        "identical bounding-chain homology class gives no ambiguity",
    )


def torsion_linking_lens_space(n: int, lhs: int, rhs: int) -> Fraction:
    """Linking form on the Z_n torsion H_1 of L(n,1), represented in Q/Z."""

    return mod_one(Fraction(lhs * rhs, n))


def check_torsion_linking_pairing_is_q_mod_z() -> None:
    for n in range(2, 13):
        for a in range(n):
            for b in range(n):
                value = torsion_linking_lens_space(n, a, b)
                assert_true(0 <= value < 1, "torsion linking is represented modulo one")
                assert_equal(
                    mod_one(n * value),
                    Fraction(0, 1),
                    "Z_n torsion linking has denominator dividing n",
                )
                for c in range(n):
                    lhs = torsion_linking_lens_space(n, (a + b) % n, c)
                    rhs = mod_one(
                        torsion_linking_lens_space(n, a, c)
                        + torsion_linking_lens_space(n, b, c)
                    )
                    assert_equal(lhs, rhs, "torsion linking is bilinear in the first slot")


def degree_checked_cochain_evaluation(
    n: int,
    cochain_degree: int,
    cycle_dimension: int,
    cochain: tuple[int, ...],
    cycle: tuple[int, ...],
) -> int:
    if cochain_degree != cycle_dimension:
        raise ValueError(
            f"degree-{cochain_degree} cochain cannot evaluate on a "
            f"{cycle_dimension}-cycle"
        )
    return sum(bg * cyc for bg, cyc in zip(cochain, cycle, strict=True)) % n


def delta_one_to_two(n: int, cochain: tuple[int, int, int]) -> tuple[int]:
    # A finite CW model with two boundary 1-cells for one 2-cell and one
    # independent loop 1-cell.  The loop component is invisible to delta.
    return ((cochain[0] + cochain[1]) % n,)


def check_background_characteristic_class_degree_not_operator_holonomy() -> None:
    p = 1
    n = 7
    characteristic_class = (1, 2, 3)
    charged_cycle = (0, 1, 0)
    try:
        degree_checked_cochain_evaluation(
            n,
            cochain_degree=p + 1,
            cycle_dimension=p,
            cochain=characteristic_class,
            cycle=charged_cycle,
        )
    except ValueError:
        pass
    else:
        raise AssertionError("H^{p+1} characteristic class evaluated directly on H_p cycle")

    two_cycle = (1, 0, 1)
    assert_equal(
        degree_checked_cochain_evaluation(
            n,
            cochain_degree=p + 1,
            cycle_dimension=p + 1,
            cochain=characteristic_class,
            cycle=two_cycle,
        ),
        4 % n,
        "degree p+1 characteristic class evaluates on p+1 cycles",
    )


def check_background_gauge_cochain_separate_from_closed_symmetry_parameter() -> None:
    n = 5
    charge = 2

    # A background gauge redundancy uses an arbitrary p-cochain.  This sample is
    # not closed, so it shifts the cocycle representative by delta xi.
    gauge_cochain = (1, 2, 0)
    gauge_shift = delta_one_to_two(n, gauge_cochain)
    assert_equal(gauge_shift, (3,), "nonclosed gauge cochain has nonzero coboundary")

    background = (4,)
    shifted_background = ((background[0] + gauge_shift[0]) % n,)
    assert_equal(shifted_background, (2,), "background representative shifts by delta xi")

    two_chain = (1,)
    boundary_cycle = (1, 1, 0)
    bulk_shift_exponent = charge * degree_checked_cochain_evaluation(
        n,
        cochain_degree=2,
        cycle_dimension=2,
        cochain=gauge_shift,
        cycle=two_chain,
    )
    boundary_compensator_exponent = -charge * degree_checked_cochain_evaluation(
        n,
        cochain_degree=1,
        cycle_dimension=1,
        cochain=gauge_cochain,
        cycle=boundary_cycle,
    )
    assert_equal(
        (bulk_shift_exponent + boundary_compensator_exponent) % n,
        0,
        "charged insertion compensates background gauge cochain by Stokes",
    )

    before = charge * degree_checked_cochain_evaluation(
        n,
        cochain_degree=2,
        cycle_dimension=2,
        cochain=background,
        cycle=two_chain,
    )
    after = (
        charge
        * degree_checked_cochain_evaluation(
            n,
            cochain_degree=2,
            cycle_dimension=2,
            cochain=shifted_background,
            cycle=two_chain,
        )
        + boundary_compensator_exponent
    )
    assert_equal(
        after % n,
        before % n,
        "background coupling plus charged operator is gauge covariant",
    )

    # A global higher-form symmetry at fixed background is closed.  It may act
    # nontrivially on a nonbounding p-cycle, but its coboundary is zero.
    symmetry_cocycle = (0, 0, 2)
    symmetry_shift = delta_one_to_two(n, symmetry_cocycle)
    loop_cycle = (0, 0, 1)
    symmetry_phase = charge * degree_checked_cochain_evaluation(
        n,
        cochain_degree=1,
        cycle_dimension=1,
        cochain=symmetry_cocycle,
        cycle=loop_cycle,
    )
    assert_equal(symmetry_shift, (0,), "closed symmetry cocycle leaves background fixed")
    assert_equal(symmetry_phase % n, 4, "closed symmetry cocycle acts on charged p-cycle")
    assert_true(
        symmetry_shift != gauge_shift,
        "closed symmetry cocycle must not masquerade as nonzero background gauge shift",
    )


def check_degree_p_holonomy_data_replaces_integer_linking() -> None:
    for n in range(2, 13):
        holonomy_data = (1 % n, 2 % n, 3 % n)
        x_cycle = (1, 0, 0)
        y_cycle = (0, 1, 0)
        sum_cycle = (1, 1, 0)

        assert_equal(
            degree_checked_cochain_evaluation(n, 1, 1, holonomy_data, y_cycle),
            2 % n,
            "degree-p holonomy data evaluate on a noncontractible T^3 cycle",
        )
        assert_equal(
            degree_checked_cochain_evaluation(n, 1, 1, holonomy_data, sum_cycle),
            (
                degree_checked_cochain_evaluation(n, 1, 1, holonomy_data, x_cycle)
                + degree_checked_cochain_evaluation(n, 1, 1, holonomy_data, y_cycle)
            )
            % n,
            "holonomy evaluation is additive on charged cycles",
        )


def check_defect_transgression_yields_degree_p_action() -> None:
    for n in range(2, 13):
        for p in range(0, 4):
            relative_or_thom_degree = p + 1
            transgressed_degree = relative_or_thom_degree - 1
            assert_equal(
                transgressed_degree,
                p,
                "codimension-(p+1) defect transgresses to degree-p action datum",
            )
            for defect_label in range(n):
                for charge_label in range(n):
                    for local_linking in range(-2, 3):
                        transgressed_parameter = (defect_label * local_linking) % n
                        charged_cycle = (1,)
                        evaluated_parameter = degree_checked_cochain_evaluation(
                            n,
                            cochain_degree=p,
                            cycle_dimension=p,
                            cochain=(transgressed_parameter,),
                            cycle=charged_cycle,
                        )
                        lhs = (charge_label * evaluated_parameter) % n
                        rhs = zn_phase_exponent(
                            n,
                            defect_label,
                            charge_label,
                            local_linking,
                        )
                        assert_equal(lhs, rhs, "local linking is a transgressed degree-p action")


def check_junction_charge_conservation() -> None:
    # At a junction of p-dimensional charged defects in a Z_N p-form
    # symmetry, a small linking symmetry defect sees the product of character
    # phases.  Charge conservation means the total charge vanishes modulo N.
    examples = [
        (5, [1, 1, 3]),
        (7, [2, 4, 1]),
        (8, [1, 3, 4]),
        (11, [2, 5, 7, 8]),
    ]
    for n, charges in examples:
        total_charge = sum(charges) % n
        assert_equal(total_charge, 0, "junction charge conservation example")
        for symmetry_label in range(n):
            total_exponent = sum(
                zn_phase_exponent(n, symmetry_label, q, 1) for q in charges
            ) % n
            assert_equal(total_exponent, 0, "junction Ward phase cancellation")


def main() -> None:
    check_group_like_fusion()
    check_ward_phase_multiplicativity()
    check_orientation_and_charge_reversal()
    check_linking_dimension_bookkeeping()
    check_local_meridian_integer_linking_chart()
    check_t3_noncontractible_loops_have_no_canonical_integer_linking()
    check_bounding_chain_ambiguity_requires_homology_condition()
    check_torsion_linking_pairing_is_q_mod_z()
    check_background_characteristic_class_degree_not_operator_holonomy()
    check_background_gauge_cochain_separate_from_closed_symmetry_parameter()
    check_degree_p_holonomy_data_replaces_integer_linking()
    check_defect_transgression_yields_degree_p_action()
    check_junction_charge_conservation()
    print("Extended-defect Ward and fusion checks passed.")


if __name__ == "__main__":
    main()
