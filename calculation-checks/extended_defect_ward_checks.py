#!/usr/bin/env python3
"""Finite checks for extended-defect Ward and fusion formulas."""

from __future__ import annotations


def assert_equal(lhs, rhs, message: str) -> None:
    if lhs != rhs:
        raise AssertionError(f"{message}: {lhs!r} != {rhs!r}")


def zn_phase_exponent(n: int, symmetry_label: int, charge_label: int, linking: int) -> int:
    """Return the numerator exponent modulo n for exp(2 pi i exponent/n)."""

    return (symmetry_label * charge_label * linking) % n


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
    check_junction_charge_conservation()
    print("Extended-defect Ward and fusion checks passed.")


if __name__ == "__main__":
    main()
