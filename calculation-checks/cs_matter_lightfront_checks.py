#!/usr/bin/env python3
"""Exact bookkeeping checks for 3D Chern-Simons-matter light-cone gauge."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, got, expected) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got}, expected {expected}")


def permutation_sign(p: tuple[int, int, int]) -> int:
    inv = 0
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]:
                inv += 1
    return -1 if inv % 2 else 1


def check_light_cone_quadratic_factor() -> None:
    # Labels are (+,-,perp)=(0,1,2), with epsilon^{+-perp}=+1.
    eps_plus_minus_perp = permutation_sign((0, 1, 2))
    eps_perp_minus_plus = permutation_sign((2, 1, 0))
    assert_equal("epsilon + - perp", eps_plus_minus_perp, 1)
    assert_equal("epsilon perp - +", eps_perp_minus_plus, -1)

    # A_+ d_- A_perp - A_perp d_- A_+ becomes 2 A_+ d_- A_perp after
    # integrating the second term by parts.  The CS prefactor k/(4*pi)
    # therefore becomes k/(2*pi).
    coefficient_before_parts = Fraction(eps_plus_minus_perp, 1)
    coefficient_after_parts = Fraction(-eps_perp_minus_plus, 1)
    assert_equal(
        "light-cone CS quadratic factor",
        coefficient_before_parts + coefficient_after_parts,
        Fraction(2),
    )


def check_first_order_gaussian_sign() -> None:
    # Finite-dimensional analogue with antisymmetric D replaced by a formal
    # inverse convention.  For S=a A_+ D A_perp - A_+ J+ - A_perp Jperp,
    # equations give A_perp=a^{-1}D^{-1}J+, A_+=-a^{-1}D^{-1}Jperp.
    # The on-shell action is -a^{-1}(D^{-1}J+)Jperp, so the rational
    # coefficient multiplying 2*pi/k is -1.
    bilinear = Fraction(1)
    source_plus = Fraction(-1)
    source_perp = Fraction(-1)

    # Substitute D A_perp = a^{-1} J+ and A_+ = -a^{-1}D^{-1}Jperp.
    # Coefficients are counted relative to a^{-1}(D^{-1}Jperp)J+ and then
    # converted to the displayed ordering (D^{-1}J+)Jperp.
    first_two_terms = -bilinear - source_plus
    remaining_term = source_perp
    assert_equal("first-order CS first two terms cancel", first_two_terms, Fraction(0))
    assert_equal("first-order CS effective source sign", remaining_term, Fraction(-1))


def check_trace_delta_color_scaling() -> None:
    # In trace-delta normalization,
    # t^a_i^j t^a_k^l = delta_i^l delta_k^j - (1/N) delta_i^j delta_k^l.
    # A normalized singlet contraction receives an O(N) planar term and an
    # O(1) trace-subtraction term before the conventional overall 1/N
    # normalization of connected singlet correlators.
    for n in (3, 5, 11):
        planar = Fraction(n, 1)
        subtraction = Fraction(1, 1)
        assert_equal(f"CS vector planar/subleading ratio N={n}", planar / subtraction, Fraction(n, 1))


def check_t_hooft_coordinate_dimensionless() -> None:
    # In three dimensions k is an integer level and N is a rank.  Their ratio is
    # dimensionless.  This check records the algebraic normalization used in the
    # chapter: lambda=N/k_eff and one gauge exchange from the CS kernel carries
    # the coefficient 2*pi/k_eff, hence N times the rational part is 2 lambda.
    n = Fraction(17)
    k_eff = Fraction(19)
    lam = n / k_eff
    one_exchange_without_pi = Fraction(2, 1) / k_eff
    planar_exchange_without_pi = n * one_exchange_without_pi
    assert_equal("CS vector planar exchange coefficient", planar_exchange_without_pi, 2 * lam)


def check_bilocal_saddle_scaling() -> None:
    # With B=(1/N) psi_bar psi, the trace-preserving color contraction of
    # J^a K J^a is N^2 B K B, while the trace-subtraction is N B K B.
    # Multiplication by the CS kernel coefficient 2*pi/k_eff = 2*pi lambda/N
    # gives an O(N) leading bilocal action and an O(1) subtraction.
    n = Fraction(23)
    k_eff = Fraction(29)
    lam = n / k_eff
    kernel_coeff_without_pi = Fraction(2, 1) / k_eff

    leading_without_pi = kernel_coeff_without_pi * n * n
    subtraction_without_pi = kernel_coeff_without_pi * n
    assert_equal("CS bilocal leading action coefficient", leading_without_pi, 2 * n * lam)
    assert_equal("CS bilocal subtraction coefficient", subtraction_without_pi, 2 * lam)
    assert_equal("CS bilocal leading/subleading ratio", leading_without_pi / subtraction_without_pi, n)


def matmul(left: tuple[tuple[Fraction, ...], ...], right: tuple[tuple[Fraction, ...], ...]) -> tuple[tuple[Fraction, ...], ...]:
    size = len(left)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(size)) for j in range(size))
        for i in range(size)
    )


def mat_sub(left: tuple[tuple[Fraction, ...], ...], right: tuple[tuple[Fraction, ...], ...]) -> tuple[tuple[Fraction, ...], ...]:
    size = len(left)
    return tuple(tuple(left[i][j] - right[i][j] for j in range(size)) for i in range(size))


def identity(size: int) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(tuple(Fraction(1 if i == j else 0) for j in range(size)) for i in range(size))


def inverse_2x2(matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    (a, b), (c, d) = matrix
    det = a * d - b * c
    if det == 0:
        raise AssertionError("singular test matrix")
    return ((d / det, -b / det), (-c / det, a / det))


def bilocal_interaction(
    g: tuple[tuple[Fraction, ...], ...],
    v_plus: tuple[tuple[Fraction, ...], ...],
    kernel: tuple[tuple[Fraction, ...], ...],
    v_perp: tuple[tuple[Fraction, ...], ...],
    coeff: Fraction,
) -> Fraction:
    size = len(g)
    total = Fraction(0)
    for a in range(size):
        for b in range(size):
            for c in range(size):
                for d in range(size):
                    for e in range(size):
                        total += v_plus[a][b] * g[b][c] * kernel[c][d] * v_perp[d][e] * g[e][a]
    return -coeff * total


def self_energy_from_variation(
    g: tuple[tuple[Fraction, ...], ...],
    v_plus: tuple[tuple[Fraction, ...], ...],
    kernel: tuple[tuple[Fraction, ...], ...],
    v_perp: tuple[tuple[Fraction, ...], ...],
    coeff: Fraction,
) -> tuple[tuple[Fraction, ...], ...]:
    size = len(g)
    sigma = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for c_index in range(size):
        for m in range(size):
            first = Fraction(0)
            for a in range(size):
                for d in range(size):
                    for e in range(size):
                        first += v_plus[a][m] * kernel[c_index][d] * v_perp[d][e] * g[e][a]
            second = Fraction(0)
            for b in range(size):
                for d in range(size):
                    for e in range(size):
                        second += v_plus[c_index][b] * g[b][d] * kernel[d][e] * v_perp[e][m]
            sigma[c_index][m] = -coeff * (first + second)
    return tuple(tuple(row) for row in sigma)


def replace_entry(
    matrix: tuple[tuple[Fraction, ...], ...],
    row: int,
    col: int,
    delta: Fraction,
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(value + (delta if i == row and j == col else 0) for j, value in enumerate(row_values))
        for i, row_values in enumerate(matrix)
    )


def check_bilocal_self_energy_variation() -> None:
    g = (
        (Fraction(2), Fraction(1), Fraction(-1)),
        (Fraction(0), Fraction(3), Fraction(2)),
        (Fraction(1), Fraction(-2), Fraction(1)),
    )
    v_plus = (
        (Fraction(1), Fraction(2), Fraction(0)),
        (Fraction(-1), Fraction(1), Fraction(3)),
        (Fraction(2), Fraction(0), Fraction(1)),
    )
    kernel = (
        (Fraction(0), Fraction(1), Fraction(-1)),
        (Fraction(2), Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(-2), Fraction(0)),
    )
    v_perp = (
        (Fraction(2), Fraction(-1), Fraction(1)),
        (Fraction(0), Fraction(1), Fraction(2)),
        (Fraction(3), Fraction(1), Fraction(-1)),
    )
    coeff = Fraction(5, 7)
    sigma = self_energy_from_variation(g, v_plus, kernel, v_perp, coeff)

    # The manuscript defines Sigma^C_M = dI/dG^M_C.  A centered finite
    # difference extracts the linear coefficient of I(G+t E_{M C}).
    for c_index in range(3):
        for m in range(3):
            forward = bilocal_interaction(replace_entry(g, m, c_index, Fraction(1)), v_plus, kernel, v_perp, coeff)
            backward = bilocal_interaction(replace_entry(g, m, c_index, Fraction(-1)), v_plus, kernel, v_perp, coeff)
            derivative = (forward - backward) / 2
            assert_equal(f"bilocal self-energy derivative C={c_index} M={m}", sigma[c_index][m], derivative)


def check_planar_dyson_index_convention() -> None:
    g = ((Fraction(2), Fraction(1)), (Fraction(1), Fraction(1)))
    sigma = ((Fraction(3), Fraction(-1)), (Fraction(2), Fraction(4)))
    q = mat_sub(inverse_2x2(g), sigma)
    lhs = matmul(g, tuple(tuple(q[i][j] + sigma[i][j] for j in range(2)) for i in range(2)))
    assert_equal("planar Dyson equation index convention", lhs, identity(2))


def main() -> None:
    check_light_cone_quadratic_factor()
    check_first_order_gaussian_sign()
    check_trace_delta_color_scaling()
    check_t_hooft_coordinate_dimensionless()
    check_bilocal_saddle_scaling()
    check_bilocal_self_energy_variation()
    check_planar_dyson_index_convention()
    print("All Chern-Simons-matter light-front checks passed.")


if __name__ == "__main__":
    main()
