#!/usr/bin/env python3
"""Finite algebra checks for the N=1 Wilson-Fisher epsilon expansion.

The script verifies the algebra that turns the two-loop minimal-subtraction
pole data in the monograph into the fixed-point coordinate and the exponents
eta, nu, and omega.  It deliberately does not attempt to recompute the
two-loop Feynman integrals; those pole coefficients are derived in the text.
"""

from fractions import Fraction


def assert_eq(name: str, value: Fraction, expected: Fraction) -> None:
    if value != expected:
        raise AssertionError(f"{name}: got {value}, expected {expected}")


def main() -> None:
    # beta_x = -eps x + b1 x^2 + b2 x^3, from
    # x0 = mu^eps [x + A x^2/eps + x^3(A^2/eps^2 + C/eps)].
    A = Fraction(3, 1)
    C = Fraction(-17, 6)
    b1 = A
    b2 = 2 * C
    assert_eq("two-loop beta x^2 coefficient", b1, Fraction(3, 1))
    assert_eq("two-loop beta x^3 coefficient", b2, Fraction(-17, 3))

    # Solve beta_x(x*) = 0 with x* = a eps + b eps^2.
    a = Fraction(1, b1)
    b = -(b2 * a**3) / (-1 + 2 * b1 * a)
    assert_eq("fixed point epsilon coefficient", a, Fraction(1, 3))
    assert_eq("fixed point epsilon^2 coefficient", b, Fraction(17, 81))

    # gamma_phi = x^2/12 + O(x^3); eta = 2 gamma_phi(x*).
    eta_eps2 = 2 * Fraction(1, 12) * a**2
    assert_eq("eta epsilon^2 coefficient", eta_eps2, Fraction(1, 54))

    # gamma_2 = x - 5 x^2 / 6 + O(x^3).
    gamma2_eps1 = a
    gamma2_eps2 = b - Fraction(5, 6) * a**2
    assert_eq("gamma_2 epsilon coefficient", gamma2_eps1, Fraction(1, 3))
    assert_eq("gamma_2 epsilon^2 coefficient", gamma2_eps2, Fraction(19, 162))

    # Delta_phi2 = 2 - eps + gamma_2*, so y_t = D - Delta_phi2.
    yt_eps1 = Fraction(-1, 3)
    yt_eps2 = -gamma2_eps2
    assert_eq("y_t epsilon coefficient", yt_eps1, Fraction(-1, 3))
    assert_eq("y_t epsilon^2 coefficient", yt_eps2, Fraction(-19, 162))

    # nu = 1 / (2 + a1 eps + a2 eps^2).
    a1 = yt_eps1
    a2 = yt_eps2
    nu_eps0 = Fraction(1, 2)
    nu_eps1 = -a1 / 4
    nu_eps2 = a1**2 / 8 - a2 / 4
    assert_eq("nu epsilon^0 coefficient", nu_eps0, Fraction(1, 2))
    assert_eq("nu epsilon coefficient", nu_eps1, Fraction(1, 12))
    assert_eq("nu epsilon^2 coefficient", nu_eps2, Fraction(7, 162))

    # omega = beta_x'(x*) = -eps + 2 b1 x* + 3 b2 x*^2.
    omega_eps1 = -1 + 2 * b1 * a
    omega_eps2 = 2 * b1 * b + 3 * b2 * a**2
    assert_eq("omega epsilon coefficient", omega_eps1, Fraction(1, 1))
    assert_eq("omega epsilon^2 coefficient", omega_eps2, Fraction(-17, 27))

    print("All Wilson-Fisher epsilon-expansion algebra checks passed.")


if __name__ == "__main__":
    main()
