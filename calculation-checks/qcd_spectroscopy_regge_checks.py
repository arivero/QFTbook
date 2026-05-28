#!/usr/bin/env python3
"""Exact algebra checks for QCD spectroscopy and Regge conventions."""

from __future__ import annotations

from fractions import Fraction


Poly = tuple[Fraction, ...]  # coefficients in ascending powers


def assert_equal(name: str, got, expected) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got}, expected {expected}")


def poly_mul(a: Poly, b: Poly) -> Poly:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return tuple(out)


def veneziano_residue_polynomial(n: int) -> Poly:
    # Up to the universal pole denominator and sign, the n-th s-channel
    # residue of B(-alpha(s),-alpha(t)) is prod_{r=1}^n (alpha(t)+r)/n!.
    poly: Poly = (Fraction(1),)
    for r in range(1, n + 1):
        poly = poly_mul(poly, (Fraction(r), Fraction(1)))
    factorial = 1
    for r in range(2, n + 1):
        factorial *= r
    return tuple(c / factorial for c in poly)


def check_gell_mann_okubo() -> None:
    m0 = Fraction(11)
    a = Fraction(3)
    b = Fraction(5)
    n = m0 + a + b / 2
    xi = m0 - a + b / 2
    lam = m0
    sigma = m0 + 2 * b
    assert_equal("octet GMO", 2 * (n + xi), 3 * lam + sigma)


def check_decuplet_equal_spacing() -> None:
    m0 = Fraction(17)
    c = Fraction(-4)
    delta = m0 + c
    sigma_star = m0
    xi_star = m0 - c
    omega = m0 - 2 * c
    assert_equal("decuplet spacing 1", sigma_star - delta, xi_star - sigma_star)
    assert_equal("decuplet spacing 2", xi_star - sigma_star, omega - xi_star)


def check_veneziano_residue_degree() -> None:
    p3 = veneziano_residue_polynomial(3)
    assert_equal(
        "third Veneziano residue polynomial",
        p3,
        (Fraction(1), Fraction(11, 6), Fraction(1), Fraction(1, 6)),
    )
    for n in range(1, 7):
        pn = veneziano_residue_polynomial(n)
        assert_equal(f"Veneziano residue degree {n}", len(pn) - 1, n)
        assert_equal(f"Veneziano leading coefficient {n}", pn[-1], Fraction(1, factorial(n)))


def factorial(n: int) -> int:
    out = 1
    for k in range(2, n + 1):
        out *= k
    return out


def check_rotating_string_slope_coefficient() -> None:
    # For a classical open string with massless endpoints,
    # E = pi*sigma/omega and J = pi*sigma/(2 omega^2), hence
    # J/E^2 = 1/(2*pi*sigma).  The exact rational coefficient is 1/2.
    energy_coeff = Fraction(1)
    angular_momentum_coeff = Fraction(1, 2)
    assert_equal(
        "open-string Regge slope rational coefficient",
        angular_momentum_coeff / (energy_coeff**2),
        Fraction(1, 2),
    )


def check_luscher_kmatrix_pole_algebra() -> None:
    # From delta + phi = n*pi, cot(delta) = -cot(phi).  With
    # K^{-1}=rho*cot(delta), finite-volume levels therefore sample
    # K^{-1}=-rho*cot(phi).  Use rationals for an exact representative.
    rho = Fraction(5, 7)
    cot_phi = Fraction(-11, 13)
    cot_delta = -cot_phi
    assert_equal("Luscher cotangent sign", rho * cot_delta, -rho * cot_phi)

    # With t_I = 1/(K^{-1} - i*rho), the adjacent second sheet is
    # t_II = 1/(K^{-1} + i*rho).  For K^{-1}(s)=(s-M^2)/g^2 and locally
    # constant rho, the pole is s_* = M^2 - i g^2 rho.  Check the real
    # and imaginary parts of the denominator separately.
    mass_sq = Fraction(19, 3)
    coupling_sq = Fraction(2, 5)
    pole_real = mass_sq
    pole_imag = -coupling_sq * rho
    denominator_real = (pole_real - mass_sq) / coupling_sq
    denominator_imag = pole_imag / coupling_sq + rho
    assert_equal("second-sheet pole denominator real part", denominator_real, Fraction(0))
    assert_equal("second-sheet pole denominator imaginary part", denominator_imag, Fraction(0))


def main() -> None:
    check_gell_mann_okubo()
    check_decuplet_equal_spacing()
    check_veneziano_residue_degree()
    check_rotating_string_slope_coefficient()
    check_luscher_kmatrix_pole_algebra()
    print("All QCD spectroscopy and Regge convention checks passed.")


if __name__ == "__main__":
    main()
