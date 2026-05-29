#!/usr/bin/env python3
"""Finite checks for the Gribov-Zwanziger horizon subsection.

The script checks only algebraic identities used in the manuscript: the
spectral form of the horizon functional, the sign of the Gaussian localization
with an imaginary source, and the tree-level transverse propagator denominator.
It does not test the existence of the Yang-Mills continuum limit.
"""

from __future__ import annotations

from fractions import Fraction


def assert_equal(name: str, lhs: Fraction | complex, rhs: Fraction | complex) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: got {lhs!r}, expected {rhs!r}")


def assert_close(name: str, lhs: complex, rhs: complex, tol: float = 1e-12) -> None:
    if abs(lhs - rhs) > tol:
        raise AssertionError(f"{name}: got {lhs!r}, expected {rhs!r}")


def horizon_spectral(eigenvalues: list[Fraction], projections: list[Fraction]) -> Fraction:
    if len(eigenvalues) != len(projections):
        raise ValueError("eigenvalue and projection lists must have equal length")
    if any(lam <= 0 for lam in eigenvalues):
        raise ValueError("the Gribov-region interior requires positive eigenvalues")
    return sum((proj * proj) / lam for lam, proj in zip(eigenvalues, projections))


def gaussian_shift_constant(operator_eigenvalue: Fraction, gamma_squared: Fraction, source: Fraction) -> Fraction:
    """Constant added to the action after completing the square.

    For one bosonic localization mode,

        m phibar phi + i gamma^2 b (phi + phibar)
        = m (phibar + i gamma^2 b/m)(phi + i gamma^2 b/m)
          + gamma^4 b^2/m.

    Hence the Euclidean weight contributes exp(-gamma^4 b^2/m), the sign
    needed to localize a positive horizon action.
    """

    if operator_eigenvalue <= 0:
        raise ValueError("positive Faddeev-Popov eigenvalue required")
    return gamma_squared * gamma_squared * source * source / operator_eigenvalue


def real_source_shift_constant(operator_eigenvalue: Fraction, gamma_squared: Fraction, source: Fraction) -> Fraction:
    """The same completion with a real source has the opposite sign."""

    if operator_eigenvalue <= 0:
        raise ValueError("positive Faddeev-Popov eigenvalue required")
    return -gamma_squared * gamma_squared * source * source / operator_eigenvalue


def gz_tree_propagator(p_squared: Fraction, g_squared: Fraction, lambda_fourth: Fraction) -> Fraction:
    if p_squared <= 0 or g_squared <= 0 or lambda_fourth <= 0:
        raise ValueError("positive Euclidean momentum, coupling, and horizon scale required")
    return g_squared * p_squared / (p_squared * p_squared + lambda_fourth)


def gz_inverse_kernel(p_squared: Fraction, g_squared: Fraction, lambda_fourth: Fraction) -> Fraction:
    if p_squared <= 0 or g_squared <= 0 or lambda_fourth <= 0:
        raise ValueError("positive Euclidean momentum, coupling, and horizon scale required")
    return p_squared / g_squared + lambda_fourth / (g_squared * p_squared)


def check_horizon_spectral_growth() -> None:
    projections = [Fraction(2), Fraction(1), Fraction(0)]
    far_from_horizon = horizon_spectral(
        [Fraction(1), Fraction(3), Fraction(5)],
        projections,
    )
    near_horizon = horizon_spectral(
        [Fraction(1, 10), Fraction(3), Fraction(5)],
        projections,
    )

    assert_equal("horizon spectral sum away from boundary", far_from_horizon, Fraction(13, 3))
    assert_equal("horizon spectral sum near boundary", near_horizon, Fraction(121, 3))
    if near_horizon <= far_from_horizon:
        raise AssertionError("horizon functional should increase when a charged eigenmode softens")


def check_gaussian_localization_sign() -> None:
    m = Fraction(7, 3)
    gamma_squared = Fraction(5, 2)
    source = Fraction(4, 1)
    expected = Fraction(300, 7)

    assert_equal(
        "imaginary-source horizon action sign",
        gaussian_shift_constant(m, gamma_squared, source),
        expected,
    )
    assert_equal(
        "real-source sign is opposite",
        real_source_shift_constant(m, gamma_squared, source),
        -expected,
    )


def check_tree_propagator_inverse() -> None:
    p_squared = Fraction(3, 2)
    g_squared = Fraction(5, 3)
    lambda_fourth = Fraction(7, 4)

    propagator = gz_tree_propagator(p_squared, g_squared, lambda_fourth)
    inverse = gz_inverse_kernel(p_squared, g_squared, lambda_fourth)
    assert_equal("GZ propagator inverts transverse kernel", propagator * inverse, Fraction(1))

    free_propagator = g_squared / p_squared
    uv_ratio = propagator / free_propagator
    assert_equal(
        "GZ propagator free-field ratio",
        uv_ratio,
        p_squared * p_squared / (p_squared * p_squared + lambda_fourth),
    )


def check_complex_p_squared_poles() -> None:
    lambda_squared = 3
    lambda_fourth = lambda_squared * lambda_squared
    for sign in (1, -1):
        q = sign * 1j * lambda_squared
        assert_close("GZ p^2-plane pole", q * q + lambda_fourth, 0j)


def main() -> None:
    check_horizon_spectral_growth()
    check_gaussian_localization_sign()
    check_tree_propagator_inverse()
    check_complex_p_squared_poles()
    print("All Gribov-Zwanziger horizon checks passed.")


if __name__ == "__main__":
    main()
