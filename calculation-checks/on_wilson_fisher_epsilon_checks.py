#!/usr/bin/env python3
"""Exact algebra checks for the O(N) Wilson-Fisher epsilon expansion.

The script verifies the rational algebra displayed in the monograph for the
singlet O(N) Wilson-Fisher family.  It starts from the two-loop pole-map
coefficients, solves for the fixed point through order epsilon^2, and checks
the exponents eta, nu, and omega.  It does not recompute the Feynman integrals
that produce the pole coefficients.
"""

from fractions import Fraction


def assert_eq(name: str, value: Fraction, expected: Fraction) -> None:
    if value != expected:
        raise AssertionError(f"{name}: got {value}, expected {expected}")


def check_n(n_value: int) -> None:
    n = Fraction(n_value, 1)

    beta2 = Fraction(n_value + 8, 3)
    beta3 = -Fraction(3 * n_value + 14, 3)

    # beta = -eps x + beta2 x^2 + beta3 x^3.
    x1 = Fraction(1, 1) / beta2
    x2 = -beta3 / beta2**3
    assert_eq(f"N={n_value} fixed point x eps", x1, Fraction(3, n_value + 8))
    assert_eq(
        f"N={n_value} fixed point x eps^2",
        x2,
        Fraction(9 * (3 * n_value + 14), (n_value + 8) ** 3),
    )

    gamma_s_1 = Fraction(n_value + 2, 3)
    gamma_s_2 = -Fraction(5 * (n_value + 2), 18)
    gamma_s_star_1 = gamma_s_1 * x1
    gamma_s_star_2 = gamma_s_1 * x2 + gamma_s_2 * x1**2
    assert_eq(
        f"N={n_value} gamma_S eps",
        gamma_s_star_1,
        Fraction(n_value + 2, n_value + 8),
    )
    assert_eq(
        f"N={n_value} gamma_S eps^2",
        gamma_s_star_2,
        Fraction((n_value + 2) * (13 * n_value + 44), 2 * (n_value + 8) ** 3),
    )

    eta_eps2 = 2 * Fraction(n_value + 2, 36) * x1**2
    assert_eq(
        f"N={n_value} eta eps^2",
        eta_eps2,
        Fraction(n_value + 2, 2 * (n_value + 8) ** 2),
    )

    # y_t = 2 - gamma_S(x*), so nu is the reciprocal of
    # 2 + y1 eps + y2 eps^2.
    y1 = -gamma_s_star_1
    y2 = -gamma_s_star_2
    nu1 = -y1 / 4
    nu2 = y1**2 / 8 - y2 / 4
    assert_eq(
        f"N={n_value} nu eps",
        nu1,
        Fraction(n_value + 2, 4 * (n_value + 8)),
    )
    assert_eq(
        f"N={n_value} nu eps^2",
        nu2,
        Fraction(
            (n_value + 2) * (n_value**2 + 23 * n_value + 60),
            8 * (n_value + 8) ** 3,
        ),
    )

    omega1 = -1 + 2 * beta2 * x1
    omega2 = 2 * beta2 * x2 + 3 * beta3 * x1**2
    assert_eq(f"N={n_value} omega eps", omega1, Fraction(1, 1))
    assert_eq(
        f"N={n_value} omega eps^2",
        omega2,
        -Fraction(3 * (3 * n_value + 14), (n_value + 8) ** 2),
    )

    if n_value == 1:
        assert_eq("N=1 eta agrees with Ising check", eta_eps2, Fraction(1, 54))
        assert_eq("N=1 nu eps", nu1, Fraction(1, 12))
        assert_eq("N=1 nu eps^2", nu2, Fraction(7, 162))
        assert_eq("N=1 omega eps^2", omega2, -Fraction(17, 27))


def main() -> None:
    for n_value in [1, 2, 3, 4, 10, 100]:
        check_n(n_value)

    # Large-N consistency at the level of leading coefficients:
    # u = N x has u_* = 3 eps + O(1/N), eta = O(1/N), and
    # nu -> 1/(2-eps) = 1/2 + eps/4 + eps^2/8 + ...
    n = 10**6
    u1 = Fraction(n, 1) * Fraction(3, n + 8)
    if not u1 < Fraction(3, 1):
        raise AssertionError("large-N u_* coefficient should approach 3 from below")
    if Fraction(3, 1) - u1 > Fraction(1, 1000):
        raise AssertionError("large-N u_* coefficient convergence check failed")

    print("All O(N) Wilson-Fisher epsilon-expansion algebra checks passed.")


if __name__ == "__main__":
    main()
