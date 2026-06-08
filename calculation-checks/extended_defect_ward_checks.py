#!/usr/bin/env python3
"""Finite checks for extended-defect Ward and fusion formulas.

Evidence contract.
Target claims: the finite higher-form Ward algebra in Volume IX, Chapter 2,
including the local integer linking chart, the topology restrictions on global
integer linking, finite-background evaluation, torsion linking, and
junction-charge conservation.
Independent construction: exact arithmetic in finite cyclic groups, a homology
model of nonbounding loops on T^3, an intersection-pairing model of
bounding-chain ambiguity, local signed-crossing recovery of the integer
meridian rule, and the lens-space torsion pairing a*b/n in Q/Z.
Imported assumptions: oriented closed manifolds for the global torsion-pairing
model, the standard degree condition
Tor H_{D-p-1}(M) x Tor H_p(M) -> Q/Z, and the use of finite homology models
as topology negative controls rather than continuum QFT constructions.
Negative controls: two noncontractible loops on T^3 do not start the
bounding-chain integer-linking construction; two bounding chains whose
difference has nonzero intersection with the charged cycle give different
integers; a torsion pairing returns Q/Z data rather than canonical integers.
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


def finite_background_evaluation(n: int, background: tuple[int, ...], cycle: tuple[int, ...]) -> int:
    return sum(bg * cyc for bg, cyc in zip(background, cycle, strict=True)) % n


def check_global_background_evaluation_replaces_integer_linking() -> None:
    for n in range(2, 13):
        background = (1 % n, 2 % n, 3 % n)
        x_cycle = (1, 0, 0)
        y_cycle = (0, 1, 0)
        sum_cycle = (1, 1, 0)

        assert_equal(
            finite_background_evaluation(n, background, y_cycle),
            2 % n,
            "finite background evaluates on a noncontractible T^3 cycle",
        )
        assert_equal(
            finite_background_evaluation(n, background, sum_cycle),
            (
                finite_background_evaluation(n, background, x_cycle)
                + finite_background_evaluation(n, background, y_cycle)
            )
            % n,
            "background evaluation is additive on charged cycles",
        )


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
    check_global_background_evaluation_replaces_integer_linking()
    check_junction_charge_conservation()
    print("Extended-defect Ward and fusion checks passed.")


if __name__ == "__main__":
    main()
