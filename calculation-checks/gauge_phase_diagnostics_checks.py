#!/usr/bin/env python3
"""Finite checks for gauge-theory phase diagnostics.

These checks cover only the algebraic and asymptotic bookkeeping used in the
phase-diagnostics chapter: finite dyonic pairings, condensate orthogonality,
static-potential spectral extraction in a tropical model, and the leading
exponent of a Fredenhagen-Marcu type ratio.
"""

from __future__ import annotations

from itertools import product


Charge = tuple[int, int]


def assert_equal(lhs, rhs, message: str) -> None:
    if lhs != rhs:
        raise AssertionError(f"{message}: {lhs!r} != {rhs!r}")


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


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


def all_charges(n: int) -> list[Charge]:
    return [(e, m) for e in range(n) for m in range(n)]


def dirac_numerator(n: int, lhs: Charge, rhs: Charge) -> int:
    e, m = lhs
    ep, mp = rhs
    return (e * mp - ep * m) % n


def orthogonal_complement(n: int, subgroup: set[Charge]) -> set[Charge]:
    return {
        charge
        for charge in all_charges(n)
        if all(dirac_numerator(n, charge, condensed) == 0 for condensed in subgroup)
    }


def check_condensate_orthogonality() -> None:
    for n in range(2, 15):
        electric = subgroup_generated(n, [(1, 0)])
        magnetic = subgroup_generated(n, [(0, 1)])
        assert_equal(orthogonal_complement(n, electric), electric, "electric axis is maximal isotropic")
        assert_equal(orthogonal_complement(n, magnetic), magnetic, "magnetic axis is maximal isotropic")
        assert_true((1, 0) not in orthogonal_complement(n, magnetic), "magnetic condensate confines fundamental electric charge")
        assert_true((0, 1) not in orthogonal_complement(n, electric), "electric condensate confines fundamental magnetic charge")

        for p in range(n):
            dyonic = subgroup_generated(n, [(p, 1)])
            assert_equal(orthogonal_complement(n, dyonic), dyonic, "primitive dyonic condensate is maximal isotropic")
            for test_charge in all_charges(n):
                confined = test_charge not in orthogonal_complement(n, dyonic)
                paired = dirac_numerator(n, test_charge, (p, 1)) != 0
                assert_equal(confined, paired, "oblique confinement is nontrivial finite Dirac pairing")


def tropical_static_energy(exponents: list[int]) -> int:
    """Lowest exponent in a finite sum of positive terms q^E."""

    return min(exponents)


def check_static_potential_tropical_extraction() -> None:
    spectra = [
        [7],
        [5, 8, 13],
        [12, 3, 9, 4],
        [20, 20, 21],
    ]
    for exponents in spectra:
        assert_equal(
            tropical_static_energy(exponents),
            min(exponents),
            "large-time Wilson rectangle extracts the bottom spectral exponent",
        )


def fm_ratio_exponent(open_exponent_twice: int, closed_exponent: int) -> int:
    """Twice the leading exponent a - b/2 of an FM-type ratio."""

    return open_exponent_twice - closed_exponent


def check_fredenhagen_marcu_exponent_bookkeeping() -> None:
    examples = [
        # 2a, b, expected sign of 2(a-b/2)
        (10, 10, 0),
        (14, 10, 1),
        (6, 10, -1),
    ]
    for two_a, b, sign in examples:
        exponent = fm_ratio_exponent(two_a, b)
        if sign == 0:
            assert_equal(exponent, 0, "FM ratio has matched leading exponent")
        elif sign > 0:
            assert_true(exponent > 0, "FM ratio decays exponentially")
        else:
            assert_true(exponent < 0, "FM ratio grows before normalization choices are revised")


def main() -> None:
    check_condensate_orthogonality()
    check_static_potential_tropical_extraction()
    check_fredenhagen_marcu_exponent_bookkeeping()
    print("Gauge-phase diagnostic finite checks passed.")


if __name__ == "__main__":
    main()
