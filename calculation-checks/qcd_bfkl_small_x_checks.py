#!/usr/bin/env python3
"""Finite checks for the small-x/BFKL convention block in Volume II.

The manuscript writes the leading dipole/BFKL kernel in the trace-delta
Yang-Mills convention

    tr_fund(t^a t^b)=delta^{ab},       C_A=2 N_c,
    S_YM=-1/(4 g^2) int tr F^2.

These checks verify convention-invariant coefficient products, the transverse
inversion covariance of the dipole kernel measure, the elementary
Mellin-eigenvalue constants of the leading BFKL characteristic function, and
the finite Wilson-line/Fokker-Planck algebra used as the JIMWLK theorem
boundary.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_zero(name: str, expr: sp.Expr) -> None:
    reduced = sp.simplify(expr)
    if reduced != 0:
        raise AssertionError(f"{name}: got {reduced!r}, expected 0")


def dist2(p: tuple[Fraction, Fraction], q: tuple[Fraction, Fraction]) -> Fraction:
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def invert(p: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    radius2 = p[0] ** 2 + p[1] ** 2
    return (p[0] / radius2, p[1] / radius2)


def check_trace_delta_kernel_coefficient() -> None:
    g_delta_sq = Fraction(5, 11)
    n_c = Fraction(7, 1)
    c_a_delta = 2 * n_c

    g_half_sq = 2 * g_delta_sq
    c_a_half = n_c

    assert_equal(
        "BFKL color-coupling product",
        g_delta_sq * c_a_delta,
        g_half_sq * c_a_half,
    )


def check_transverse_inversion_covariance() -> None:
    x = (Fraction(1, 1), Fraction(2, 1))
    y = (Fraction(4, 1), Fraction(1, 1))
    z = (Fraction(3, 1), Fraction(5, 1))

    kernel = dist2(x, y) / (dist2(x, z) * dist2(z, y))

    xi, yi, zi = invert(x), invert(y), invert(z)
    transformed_kernel = dist2(xi, yi) / (dist2(xi, zi) * dist2(zi, yi))
    jacobian = Fraction(1, 1) / (z[0] ** 2 + z[1] ** 2) ** 2

    assert_equal("dipole kernel inversion covariance", transformed_kernel * jacobian, kernel)


def check_bfkl_characteristic_values() -> None:
    gamma = sp.symbols("gamma")
    chi = 2 * sp.polygamma(0, 1) - sp.polygamma(0, gamma) - sp.polygamma(0, 1 - gamma)

    assert_zero("BFKL saddle value", chi.subs(gamma, sp.Rational(1, 2)) - 4 * sp.log(2))
    assert_zero("BFKL saddle first derivative", sp.diff(chi, gamma).subs(gamma, sp.Rational(1, 2)))
    assert_zero(
        "BFKL saddle second derivative",
        sp.diff(chi, gamma, 2).subs(gamma, sp.Rational(1, 2)) - 28 * sp.zeta(3),
    )

    nu = sp.symbols("nu")
    quadratic_coefficient = -sp.diff(chi, gamma, 2).subs(gamma, sp.Rational(1, 2)) / 2
    assert_zero("BFKL diffusion coefficient", quadratic_coefficient + 14 * sp.zeta(3))

    gamma_line = sp.Rational(1, 2) + sp.I * nu
    series = 4 * sp.log(2) - 14 * sp.zeta(3) * nu**2
    assert_zero(
        "BFKL nu-expansion through quadratic order",
        sp.series(chi.subs(gamma, gamma_line) - series, nu, 0, 3).removeO(),
    )


def apply_constant_diffusion_generator(
    modes: dict[tuple[int, int], Fraction],
    matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
) -> dict[tuple[int, int], Fraction]:
    """Apply H=1/2 A_ij d_i d_j on the two-torus Fourier basis.

    The mode exp(i k.theta) has eigenvalue -1/2 k_i A_ij k_j.
    This is the constant-coefficient finite compact-manifold model of the
    divergence-form Wilson-line generator in the text.
    """
    output: dict[tuple[int, int], Fraction] = {}
    for (k1, k2), coeff in modes.items():
        quadratic = (
            matrix[0][0] * k1 * k1
            + (matrix[0][1] + matrix[1][0]) * k1 * k2
            + matrix[1][1] * k2 * k2
        )
        output[(k1, k2)] = -Fraction(1, 2) * quadratic * coeff
    return output


def torus_inner(
    left: dict[tuple[int, int], Fraction],
    right: dict[tuple[int, int], Fraction],
) -> Fraction:
    """Normalized torus pairing: integral left(theta) right(theta) dtheta."""
    total = Fraction(0)
    for mode, coeff in left.items():
        total += coeff * right.get((-mode[0], -mode[1]), Fraction(0))
    return total


def check_finite_wilson_line_diffusion_algebra() -> None:
    matrix = (
        (Fraction(2), Fraction(1)),
        (Fraction(1), Fraction(3)),
    )

    constant = {(0, 0): Fraction(1)}
    assert_equal(
        "finite diffusion preserves constants",
        apply_constant_diffusion_generator(constant, matrix),
        {(0, 0): Fraction(0)},
    )

    test_modes = {
        (1, 0): Fraction(2),
        (-1, 0): Fraction(2),
        (0, 1): Fraction(3),
        (0, -1): Fraction(3),
        (1, -1): Fraction(5),
        (-1, 1): Fraction(5),
    }
    h_test = apply_constant_diffusion_generator(test_modes, matrix)

    # The integral is the zero Fourier coefficient.  A divergence-form
    # generator has zero integral on compact configuration space.
    assert_equal("finite diffusion mass conservation", h_test.get((0, 0), Fraction(0)), Fraction(0))

    for mode in [(1, 0), (0, 1), (1, -1), (2, 1)]:
        singleton = {mode: Fraction(1)}
        eigenvalue = apply_constant_diffusion_generator(singleton, matrix)[mode]
        if eigenvalue >= 0:
            raise AssertionError(f"mode {mode} has nondissipative eigenvalue {eigenvalue}")

    other_modes = {
        (1, 0): Fraction(7),
        (-1, 0): Fraction(7),
        (0, 1): Fraction(-2),
        (0, -1): Fraction(-2),
        (1, -1): Fraction(4),
        (-1, 1): Fraction(4),
    }
    lhs = torus_inner(test_modes, apply_constant_diffusion_generator(other_modes, matrix))
    rhs = torus_inner(apply_constant_diffusion_generator(test_modes, matrix), other_modes)
    assert_equal("finite diffusion weak-strong duality", lhs, rhs)


def main() -> None:
    check_trace_delta_kernel_coefficient()
    check_transverse_inversion_covariance()
    check_bfkl_characteristic_values()
    check_finite_wilson_line_diffusion_algebra()
    print("All QCD small-x/BFKL and finite Wilson-line evolution checks passed.")


if __name__ == "__main__":
    main()
