#!/usr/bin/env python3
"""Finite checks for discrete-theta and Pontryagin-square arithmetic."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Charge = tuple[int, int]


def assert_equal(lhs, rhs, message: str) -> None:
    if lhs != rhs:
        raise AssertionError(f"{message}: {lhs!r} != {rhs!r}")


def divisors(n: int) -> list[int]:
    return [candidate for candidate in range(1, n + 1) if n % candidate == 0]


def target_modulus(n: int) -> int:
    return n if n % 2 else 2 * n


def inv_mod(value: int, modulus: int) -> int:
    for candidate in range(modulus):
        if (value * candidate) % modulus == 1:
            return candidate
    raise ValueError(f"{value} is not invertible modulo {modulus}")


def q_num(n: int, p: int, b: int) -> int:
    """Numerator in the natural counterterm group.

    For even N the Pontryagin-square representative has denominator 2N.
    For odd N, 2 is invertible and the same quadratic refinement is represented
    by (p/2) b^2 modulo N.
    """

    modulus = target_modulus(n)
    if n % 2:
        return (inv_mod(2, n) * p * b * b) % modulus
    return (p * b * b) % modulus


def add_charge(n: int, lhs: Charge, rhs: Charge) -> Charge:
    return ((lhs[0] + rhs[0]) % n, (lhs[1] + rhs[1]) % n)


def scale_charge(n: int, coefficient: int, charge: Charge) -> Charge:
    return ((coefficient * charge[0]) % n, (coefficient * charge[1]) % n)


def subgroup_generated(n: int, generators: list[Charge]) -> set[Charge]:
    subgroup: set[Charge] = set()
    for coefficients in product(range(n), repeat=len(generators)):
        total = (0, 0)
        for coefficient, generator in zip(coefficients, generators, strict=True):
            total = add_charge(n, total, scale_charge(n, coefficient, generator))
        subgroup.add(total)
    return subgroup


def dirac_numerator(n: int, lhs: Charge, rhs: Charge) -> int:
    e, m = lhs
    ep, mp = rhs
    return (e * mp - ep * m) % n


def line_lattice(n: int, k: int, p: int) -> set[Charge]:
    return subgroup_generated(n, [(k, 0), (p, n // k)])


def check_quadratic_refinement_identity() -> None:
    for n in range(2, 15):
        modulus = target_modulus(n)
        for p in range(modulus):
            for b in range(n):
                for c in range(n):
                    lhs = (q_num(n, p, b + c) - q_num(n, p, b) - q_num(n, p, c)) % modulus
                    if n % 2:
                        rhs = (p * b * c) % modulus
                    else:
                        rhs = (2 * p * b * c) % modulus
                    assert_equal(lhs, rhs, "Pontryagin-square quadratic identity")


def check_counterterm_classification_periodicity() -> None:
    for n in range(2, 15):
        modulus = target_modulus(n)
        for p in range(modulus):
            for b in range(n):
                assert_equal(
                    q_num(n, p + modulus, b),
                    q_num(n, p, b),
                    "oriented Pontryagin-square classification periodicity",
                )


def check_discrete_theta_line_lattice_periodicity() -> None:
    for n in range(2, 15):
        for k in divisors(n):
            for p in range(k):
                assert_equal(
                    line_lattice(n, k, p + k),
                    line_lattice(n, k, p),
                    "p and p+k define the same SU(N)/Z_k line lattice",
                )


def check_discrete_theta_line_lattice_isotropic() -> None:
    for n in range(2, 13):
        for k in divisors(n):
            for p in range(k):
                lattice = line_lattice(n, k, p)
                assert_equal(len(lattice), n, "line lattice has order N")
                for lhs, rhs in product(lattice, repeat=2):
                    assert_equal(
                        dirac_numerator(n, lhs, rhs),
                        0,
                        "line lattice is mutually local",
                    )


def check_named_su2_so3_cases() -> None:
    su2 = line_lattice(2, 1, 0)
    so3_plus = line_lattice(2, 2, 0)
    so3_minus = line_lattice(2, 2, 1)
    assert_equal(su2, {(0, 0), (1, 0)}, "SU(2) line axis")
    assert_equal(so3_plus, {(0, 0), (0, 1)}, "SO(3)+ line axis")
    assert_equal(so3_minus, {(0, 0), (1, 1)}, "SO(3)- dyonic axis")


def check_theta_shift_tilts_minimal_magnetic_line() -> None:
    for n in range(2, 15):
        for k in divisors(n):
            for p in range(k):
                old_generator = (p % n, n // k)
                new_generator = ((p + 1) % n, n // k)
                electric_shift = (new_generator[0] - old_generator[0]) % n
                assert_equal(electric_shift, 1 % n, "theta shift electric tilt")


def fractional_part(value: Fraction) -> Fraction:
    numerator = value.numerator % value.denominator
    return Fraction(numerator, value.denominator)


def check_projective_c2_tensor_invariance() -> None:
    for n in range(2, 12):
        for c1 in range(-5, 6):
            for c2 in range(-3, 4):
                nu = Fraction(c2, 1) - Fraction(n - 1, 2 * n) * c1 * c1
                expected_fraction = Fraction((-(n - 1) * c1 * c1) % (2 * n), 2 * n)
                assert_equal(
                    fractional_part(nu),
                    expected_fraction,
                    "fractional PSU(N) instanton number",
                )
                for ell in range(-3, 4):
                    c1_shifted = c1 + n * ell
                    c2_shifted = c2 + (n - 1) * c1 * ell + n * (n - 1) * ell * ell // 2
                    shifted_nu = Fraction(c2_shifted, 1) - Fraction(n - 1, 2 * n) * c1_shifted * c1_shifted
                    assert_equal(
                        shifted_nu,
                        nu,
                        "projective second Chern coordinate is tensor invariant",
                    )


def main() -> None:
    check_quadratic_refinement_identity()
    check_counterterm_classification_periodicity()
    check_discrete_theta_line_lattice_periodicity()
    check_discrete_theta_line_lattice_isotropic()
    check_named_su2_so3_cases()
    check_theta_shift_tilts_minimal_magnetic_line()
    check_projective_c2_tensor_invariance()
    print("Discrete-theta and Pontryagin-square arithmetic checks passed.")


if __name__ == "__main__":
    main()
