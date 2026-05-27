#!/usr/bin/env python3
"""Finite convention checks for nonabelian lattice observables.

These checks support Volume XI, Chapter 5.  They verify the normalization of
the leading SU(N) fundamental plaquette term, the spectral ratio used to
extract a static energy, and the algebraic cancellation built into Creutz
ratios.
"""

from __future__ import annotations

from fractions import Fraction


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def leading_fundamental_plaquette_slope(n: int, *, self_conjugate: bool = False) -> Fraction:
    """Return d/d beta <(1/N) Re Tr U_p>|_{beta=0}.

    The Wilson weight is exp[(beta/N) Re Tr U].  For SU(N), N >= 3, the
    fundamental and antifundamental characters are distinct, so the
    orthogonality integral of (chi_F + chi_Fbar)^2 gives two cross terms.
    For SU(2), the fundamental character is real and self-conjugate.
    """

    if self_conjugate:
        return Fraction(1, n * n)
    return Fraction(1, 2 * n * n)


def check_sun_fundamental_plaquette_slope() -> None:
    require(
        leading_fundamental_plaquette_slope(3) == Fraction(1, 18),
        "SU(3) fundamental plaquette slope should be 1/18",
    )
    require(
        leading_fundamental_plaquette_slope(4) == Fraction(1, 32),
        "SU(4) fundamental plaquette slope should be 1/32",
    )
    require(
        leading_fundamental_plaquette_slope(2, self_conjugate=True) == Fraction(1, 4),
        "SU(2) self-conjugate fundamental plaquette slope should be 1/4",
    )


def check_static_effective_mass_single_state_ratio() -> None:
    amplitude = Fraction(7, 5)
    transfer_eigenvalue = Fraction(3, 8)
    for m in range(1, 6):
        w_m = amplitude * transfer_eigenvalue**m
        w_next = amplitude * transfer_eigenvalue ** (m + 1)
        require(
            w_next / w_m == transfer_eigenvalue,
            "single-state Wilson-loop ratio should recover transfer eigenvalue",
        )


def area_perimeter_exponent(n: int, m: int, sigma: Fraction, mu: Fraction, constant: Fraction) -> Fraction:
    """Exponent E in W(n,m)=exp(-E)."""

    return sigma * n * m + mu * (n + m) + constant


def check_creutz_ratio_cancels_perimeter() -> None:
    sigma = Fraction(5, 7)
    mu = Fraction(11, 13)
    constant = Fraction(17, 19)
    n = 6
    m = 5
    exponent_combination = (
        area_perimeter_exponent(n, m, sigma, mu, constant)
        + area_perimeter_exponent(n - 1, m - 1, sigma, mu, constant)
        - area_perimeter_exponent(n, m - 1, sigma, mu, constant)
        - area_perimeter_exponent(n - 1, m, sigma, mu, constant)
    )
    require(
        exponent_combination == sigma,
        "Creutz exponent combination should cancel perimeter and constant terms",
    )


def main() -> None:
    check_sun_fundamental_plaquette_slope()
    check_static_effective_mass_single_state_ratio()
    check_creutz_ratio_cancels_perimeter()
    print("All nonabelian lattice-observable checks passed.")


if __name__ == "__main__":
    main()
