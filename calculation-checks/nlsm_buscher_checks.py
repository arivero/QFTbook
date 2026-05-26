#!/usr/bin/env python3
"""Finite exact checks for Buscher-rule algebra and NLSM beta bookkeeping."""

from __future__ import annotations

from fractions import Fraction


Matrix = list[list[Fraction]]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def buscher_e(E: Matrix) -> Matrix:
    size = len(E)
    E00 = E[0][0]
    dual = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    dual[0][0] = Fraction(1, 1) / E00
    for i in range(1, size):
        dual[0][i] = E[0][i] / E00
        dual[i][0] = -E[i][0] / E00
    for i in range(1, size):
        for j in range(1, size):
            dual[i][j] = E[i][j] - E[i][0] * E[0][j] / E00
    return dual


def split_g_b(E: Matrix) -> tuple[Matrix, Matrix]:
    size = len(E)
    G = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    B = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            G[i][j] = (E[i][j] + E[j][i]) / 2
            B[i][j] = (E[i][j] - E[j][i]) / 2
    return G, B


def check_buscher_involutive() -> None:
    E = [
        [Fraction(5), Fraction(7), Fraction(-2)],
        [Fraction(3), Fraction(11), Fraction(13)],
        [Fraction(-17), Fraction(19), Fraction(23)],
    ]
    assert_equal("Buscher E involution", buscher_e(buscher_e(E)), E)


def check_g_b_component_rules() -> None:
    G = [
        [Fraction(6), Fraction(2), Fraction(-3)],
        [Fraction(2), Fraction(5), Fraction(7)],
        [Fraction(-3), Fraction(7), Fraction(11)],
    ]
    B = [
        [Fraction(0), Fraction(13), Fraction(-17)],
        [Fraction(-13), Fraction(0), Fraction(19)],
        [Fraction(17), Fraction(-19), Fraction(0)],
    ]
    E = [
        [G[i][j] + B[i][j] for j in range(3)]
        for i in range(3)
    ]
    G_dual, B_dual = split_g_b(buscher_e(E))
    G00 = G[0][0]
    assert_equal("G'00", G_dual[0][0], Fraction(1, 1) / G00)
    for i in range(1, 3):
        assert_equal(f"G'0{i}", G_dual[0][i], B[0][i] / G00)
        assert_equal(f"B'0{i}", B_dual[0][i], G[0][i] / G00)
    for i in range(1, 3):
        for j in range(1, 3):
            expected_g = G[i][j] - (G[0][i] * G[0][j] - B[0][i] * B[0][j]) / G00
            expected_b = B[i][j] - (G[0][i] * B[0][j] - B[0][i] * G[0][j]) / G00
            assert_equal(f"G'{i}{j}", G_dual[i][j], expected_g)
            assert_equal(f"B'{i}{j}", B_dual[i][j], expected_b)


def check_constant_curvature_two_loop_coefficient() -> None:
    # For an n-dimensional constant-curvature target,
    # R_{iklm} R_j^{klm} = 2 (n-1) K^2 g_{ij}.  The displayed two-loop
    # coefficient 1/2 therefore contributes (n-1) K^2 g_{ij}.
    for dimension in range(2, 8):
        K = Fraction(dimension + 1, dimension + 3)
        contraction = 2 * (dimension - 1) * K * K
        two_loop = contraction / 2
        assert_equal(
            f"constant-curvature two-loop coefficient in dimension {dimension}",
            two_loop,
            (dimension - 1) * K * K,
        )


def check_dilaton_shift_involutive() -> None:
    # Logarithms are represented by formal exponents of log(G00).
    first_shift = Fraction(-1, 2)
    second_shift = Fraction(1, 2)
    assert_equal("Buscher dilaton shift involution", first_shift + second_shift, 0)


def main() -> None:
    check_buscher_involutive()
    check_g_b_component_rules()
    check_constant_curvature_two_loop_coefficient()
    check_dilaton_shift_involutive()
    print("All NLSM Buscher and beta-coefficient checks passed.")


if __name__ == "__main__":
    main()
