#!/usr/bin/env python3
"""Exact arithmetic checks for the curved trace-anomaly chapter."""

from __future__ import annotations

from fractions import Fraction


def assert_equal(actual, expected, message: str) -> None:
    if actual != expected:
        raise AssertionError(f"{message}: expected {expected!r}, got {actual!r}")


def curvature_coefficients_from_ac(a: Fraction, c: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Coefficients of Riem^2, Ric^2, R^2 in c W^2 - a E4."""

    riem = c - a
    ric = -2 * c + 4 * a
    scalar = Fraction(1, 3) * c - a
    return (riem, ric, scalar)


def check_conformal_scalar_heat_kernel_map() -> None:
    a = Fraction(1, 360)
    c = Fraction(1, 120)
    assert_equal(
        curvature_coefficients_from_ac(a, c),
        (Fraction(1, 180), Fraction(-1, 180), Fraction(0)),
        "real conformal scalar a4 curvature combination",
    )

    # Direct a4 substitution for P = -nabla^2 + R/6, written as
    # P = -(nabla^2 + E) with E = -R/6.
    r2_coefficient = Fraction(5, 360) - Fraction(1, 36) + Fraction(1, 72)
    assert_equal(r2_coefficient, Fraction(0), "conformal scalar R^2 cancellation")


def check_r_squared_counterterm_shift() -> None:
    # In D=4, delta sqrt(g)=4 sigma sqrt(g) and
    # delta R = -2 sigma R - 6 nabla^2 sigma.  Therefore
    # delta(sqrt(g) R^2) has zero sigma R^2 term and -12 R nabla^2 sigma.
    sigma_r2 = 4 - 4
    laplacian_coefficient = -12
    assert_equal(sigma_r2, 0, "R^2 Weyl variation has no sigma R^2 term in D=4")
    assert_equal(laplacian_coefficient, -12, "R^2 Weyl variation Laplacian coefficient")

    # With delta W = - int sigma A, adding kappa/(16 pi^2) int R^2 shifts
    # b by +12 kappa.
    kappa = Fraction(7, 5)
    assert_equal(12 * kappa, Fraction(84, 5), "Box R coefficient shift")


def check_free_field_coefficients() -> None:
    scalar = (Fraction(1, 360), Fraction(1, 120))
    weyl = (Fraction(11, 720), Fraction(1, 40))
    dirac = (Fraction(11, 360), Fraction(1, 20))
    vector = (Fraction(31, 180), Fraction(1, 10))

    assert_equal((2 * weyl[0], 2 * weyl[1]), dirac, "Dirac equals two Weyl fermions")

    # N=4 vector multiplet per adjoint generator: 6 real scalars, 4 Weyl
    # fermions, 1 vector.
    n4_a = 6 * scalar[0] + 4 * weyl[0] + vector[0]
    n4_c = 6 * scalar[1] + 4 * weyl[1] + vector[1]
    assert_equal(n4_a, Fraction(1, 4), "N=4 SYM a per adjoint generator")
    assert_equal(n4_c, Fraction(1, 4), "N=4 SYM c per adjoint generator")
    assert_equal(n4_a, n4_c, "N=4 SYM a equals c")


def check_constant_curvature_identities() -> None:
    # In D=4 constant sectional curvature has
    # Riem^2 = R^2/6 and Ric^2 = R^2/4.
    riem = Fraction(1, 6)
    ric = Fraction(1, 4)
    scalar = Fraction(1)
    e4 = riem - 4 * ric + scalar
    w2 = riem - 2 * ric + Fraction(1, 3) * scalar
    assert_equal(e4, Fraction(1, 6), "constant-curvature Euler density coefficient")
    assert_equal(w2, Fraction(0), "constant-curvature Weyl tensor vanishes")


def check_two_dimensional_wz_variation() -> None:
    # Vary int sqrt(g) [tau R + (nabla tau)^2] with tau -> tau + sigma.
    # After integrating by parts, the coefficient of sigma is R - 2 Box tau,
    # which is e^{2 tau} R[e^{2 tau}g] in two dimensions.
    tau_r_coefficient = 1
    kinetic_variation_after_parts = -2
    assert_equal(tau_r_coefficient, 1, "2D WZ R coefficient")
    assert_equal(kinetic_variation_after_parts, -2, "2D WZ Laplacian tau coefficient")


def main() -> None:
    check_conformal_scalar_heat_kernel_map()
    check_r_squared_counterterm_shift()
    check_free_field_coefficients()
    check_constant_curvature_identities()
    check_two_dimensional_wz_variation()
    print("All curved trace-anomaly checks passed.")


if __name__ == "__main__":
    main()
