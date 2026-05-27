#!/usr/bin/env python3
"""Finite checks for tree-level lattice gauge-action improvement.

These checks support Volume XI, Chapter 5.  They verify the arithmetic behind
the plaquette-plus-rectangle Symanzik coefficients and the rectangle flux
moments used in the tree-level derivation.
"""

from __future__ import annotations

from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def leading_area_square(r: int, s: int) -> int:
    """Coefficient multiplying F^2 from an r by s rectangular flux."""

    return r * r * s * s


def derivative_artifact_pair(r: int, s: int) -> tuple[int, int]:
    """Return coefficients for (partial_mu F)^2 and (partial_nu F)^2.

    The common factor -a^6/24 is omitted.  For a rectangle of side lengths
    r a and s a, the coefficients are r^2 s^2 r^2 and r^2 s^2 s^2.
    """

    common = r * r * s * s
    return common * r * r, common * s * s


def solve_two_by_two_for_symanzik() -> tuple[Fraction, Fraction]:
    """Solve c0 + 8 c1 = 1 and c0 + 20 c1 = 0."""

    c1 = Fraction(-1, 12)
    c0 = Fraction(5, 3)
    require(c0 + 8 * c1 == 1, "continuum normalization failed")
    require(c0 + 20 * c1 == 0, "derivative-artifact cancellation failed")
    return c0, c1


def check_rectangle_moments() -> None:
    plaquette_area = leading_area_square(1, 1)
    rectangle_area_sum = leading_area_square(1, 2) + leading_area_square(2, 1)
    require(plaquette_area == 1, "plaquette leading area-square coefficient should be 1")
    require(rectangle_area_sum == 8, "two 1x2 rectangles should contribute 8 at leading order")

    plaquette_mu, plaquette_nu = derivative_artifact_pair(1, 1)
    rect_a_mu, rect_a_nu = derivative_artifact_pair(1, 2)
    rect_b_mu, rect_b_nu = derivative_artifact_pair(2, 1)
    require((plaquette_mu, plaquette_nu) == (1, 1), "plaquette derivative coefficients failed")
    require(
        rect_a_mu + rect_b_mu == 20 and rect_a_nu + rect_b_nu == 20,
        "two 1x2 rectangles should contribute 20 to each derivative artifact",
    )


def check_iwasaki_normalization_convention() -> None:
    # The decimal -0.331 is a convention for the one-parameter rectangle
    # family.  This check only verifies the same normalization equation used
    # for the tree-level improved action.
    c1 = Fraction(-331, 1000)
    c0 = 1 - 8 * c1
    require(c0 == Fraction(3648, 1000), "Iwasaki c0 convention should be 1 - 8 c1")
    require(c0 + 8 * c1 == 1, "Iwasaki normalization convention failed")


def main() -> None:
    check_rectangle_moments()
    solve_two_by_two_for_symanzik()
    check_iwasaki_normalization_convention()
    print("All gauge-action improvement checks passed.")


if __name__ == "__main__":
    main()
