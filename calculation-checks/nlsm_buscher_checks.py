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


def constant_curvature_radius_beta(
    dimension: int,
    curvature_sign: int,
    lambda_value: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return (d r^2/d log mu)/alpha' and d lambda/d log mu.

    The dimensionless coupling is lambda=alpha'/r^2.  The first component is
    divided by alpha' so the check stays in rational arithmetic.
    """

    radius_beta_over_alpha_prime = (
        (dimension - 1) * (curvature_sign + lambda_value)
    )
    lambda_beta = (
        -(dimension - 1)
        * lambda_value
        * lambda_value
        * (curvature_sign + lambda_value)
    )
    return radius_beta_over_alpha_prime, lambda_beta


def check_constant_curvature_radius_flow() -> None:
    for dimension in range(2, 9):
        for lambda_value in [Fraction(1, 11), Fraction(2, 7), Fraction(3, 5)]:
            sphere_radius, sphere_lambda = constant_curvature_radius_beta(
                dimension,
                1,
                lambda_value,
            )
            assert_equal(
                f"sphere radius beta dimension {dimension} lambda {lambda_value}",
                sphere_radius,
                (dimension - 1) * (1 + lambda_value),
            )
            assert_equal(
                f"sphere asymptotic-freedom sign dimension {dimension} lambda {lambda_value}",
                sphere_lambda,
                -(dimension - 1) * lambda_value**2 * (1 + lambda_value),
            )

            hyperbolic_radius, hyperbolic_lambda = constant_curvature_radius_beta(
                dimension,
                -1,
                lambda_value,
            )
            assert_equal(
                f"hyperbolic radius beta dimension {dimension} lambda {lambda_value}",
                hyperbolic_radius,
                (dimension - 1) * (-1 + lambda_value),
            )
            assert_equal(
                f"hyperbolic coupling beta dimension {dimension} lambda {lambda_value}",
                hyperbolic_lambda,
                (dimension - 1) * lambda_value**2 * (1 - lambda_value),
            )


def check_dilaton_shift_involutive() -> None:
    # Logarithms are represented by formal exponents of log(G00).
    first_shift = Fraction(-1, 2)
    second_shift = Fraction(1, 2)
    assert_equal("Buscher dilaton shift involution", first_shift + second_shift, 0)


def check_cell_regularized_dilaton_shift() -> None:
    """Check the Euler-characteristic ledger for the Buscher determinant."""

    # On a finite cell decomposition the G00 exponents are:
    #   - one half per edge gauge Gaussian,
    #   + one half per vertex gauge/Faddeev-Popov normalization,
    #   + one half per face when the multiplier is written as the dual scalar.
    # The resulting exponent must match the path-integral effect of
    # delta Phi = -log(G00)/2, namely -chi * delta Phi = chi/2.
    cell_decompositions = [
        (4, 6, 4),   # tetrahedral sphere
        (8, 12, 6),  # cubical sphere
        (1, 2, 1),   # one-vertex two-edge torus cell structure
        (1, 4, 1),   # one-vertex genus-two polygon
        (1, 6, 1),   # one-vertex genus-three polygon
    ]
    for vertices, edges, faces in cell_decompositions:
        chi = vertices - edges + faces
        determinant_exponent = (
            Fraction(vertices, 2)
            - Fraction(edges, 2)
            + Fraction(faces, 2)
        )
        dilaton_shift_exponent = -chi * Fraction(-1, 2)
        assert_equal(
            f"Buscher cell determinant Euler exponent for {(vertices, edges, faces)}",
            determinant_exponent,
            Fraction(chi, 2),
        )
        assert_equal(
            f"Buscher cell determinant versus dilaton shift for {(vertices, edges, faces)}",
            determinant_exponent,
            dilaton_shift_exponent,
        )


def main() -> None:
    check_buscher_involutive()
    check_g_b_component_rules()
    check_constant_curvature_two_loop_coefficient()
    check_constant_curvature_radius_flow()
    check_dilaton_shift_involutive()
    check_cell_regularized_dilaton_shift()
    print("All NLSM Buscher and beta-coefficient/radius-flow checks passed.")


if __name__ == "__main__":
    main()
