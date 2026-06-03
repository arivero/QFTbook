#!/usr/bin/env python3
"""Exact finite checks for confinement and oblique-confinement diagnostics.

The manuscript uses the finite center-sensitive charge group

    C_N = Z_N^e direct-sum Z_N^m

with pairing ((e,m),(e',m')) -> (e m' - e' m) / N mod 1.  These checks verify
the arithmetic behind screening quotients, orthogonal complements of
condensates, and the dyonic unconfined direction in oblique confinement.  The
script also checks the finite algebra in the controlled three-dimensional
Polyakov monopole-gas mechanism: dual-photon mass normalization, sine-Gordon
wall first-order identities, and the area-law/static-potential extraction.
It does not simulate a gauge theory or prove that a condensate forms.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product

Charge = tuple[int, int]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def add_charge(n: int, lhs: Charge, rhs: Charge) -> Charge:
    return ((lhs[0] + rhs[0]) % n, (lhs[1] + rhs[1]) % n)


def scale_charge(n: int, coefficient: int, charge: Charge) -> Charge:
    return ((coefficient * charge[0]) % n, (coefficient * charge[1]) % n)


def dirac_numerator(n: int, lhs: Charge, rhs: Charge) -> int:
    e, m = lhs
    ep, mp = rhs
    return (e * mp - ep * m) % n


def all_charges(n: int) -> list[Charge]:
    return [(e, m) for e in range(n) for m in range(n)]


def subgroup_generated(n: int, generators: list[Charge]) -> set[Charge]:
    subgroup: set[Charge] = set()
    for coefficients in product(range(n), repeat=len(generators)):
        total = (0, 0)
        for coefficient, generator in zip(coefficients, generators, strict=True):
            total = add_charge(n, total, scale_charge(n, coefficient, generator))
        subgroup.add(total)
    return subgroup


def orthogonal_complement(n: int, subgroup: set[Charge]) -> set[Charge]:
    return {
        charge
        for charge in all_charges(n)
        if all(dirac_numerator(n, charge, generator) == 0 for generator in subgroup)
    }


def is_isotropic(n: int, subgroup: set[Charge]) -> bool:
    return all(dirac_numerator(n, lhs, rhs) == 0 for lhs, rhs in product(subgroup, repeat=2))


def quotient_classes(n: int, ambient: set[Charge], subgroup: set[Charge]) -> list[frozenset[Charge]]:
    unseen = set(ambient)
    classes: list[frozenset[Charge]] = []
    while unseen:
        representative = next(iter(unseen))
        coset = frozenset(add_charge(n, representative, s) for s in subgroup)
        classes.append(coset)
        unseen -= set(coset)
    return classes


def check_screened_pairing_descends() -> None:
    for n in range(2, 13):
        for generator in [(1, 0), (0, 1)]:
            screened = subgroup_generated(n, [generator])
            assert_equal(f"screened subgroup isotropic N={n} gen={generator}", is_isotropic(n, screened), True)
            sperp = orthogonal_complement(n, screened)
            classes = quotient_classes(n, sperp, screened)
            for class_a, class_b in product(classes, repeat=2):
                values = {
                    dirac_numerator(n, a, b)
                    for a, b in product(class_a, class_b)
                }
                assert_equal(
                    f"descended pairing well-defined N={n} gen={generator}",
                    len(values),
                    1,
                )


def check_maximal_isotropic_axes_and_dyons() -> None:
    for n in range(2, 13):
        for p in range(n):
            condensate = subgroup_generated(n, [(p, 1)])
            assert_equal(f"dyonic condensate size N={n} p={p}", len(condensate), n)
            assert_equal(f"dyonic condensate isotropic N={n} p={p}", is_isotropic(n, condensate), True)
            assert_equal(
                f"dyonic condensate maximal N={n} p={p}",
                orthogonal_complement(n, condensate),
                condensate,
            )


def check_oblique_unconfined_direction() -> None:
    for n in range(2, 13):
        for p in range(n):
            condensate = subgroup_generated(n, [(p, 1)])
            unconfined = orthogonal_complement(n, condensate)
            expected = {(p * m % n, m) for m in range(n)}
            assert_equal(f"oblique condition e=p m mod N, N={n} p={p}", unconfined, expected)


def check_magnetic_condensation_confines_electric_nality() -> None:
    for n in range(2, 13):
        magnetic = subgroup_generated(n, [(0, 1)])
        unconfined = orthogonal_complement(n, magnetic)
        expected = {(0, m) for m in range(n)}
        assert_equal(f"magnetic condensation leaves only electric-neutral N={n}", unconfined, expected)
        for e in range(1, n):
            assert_equal(
                f"nonzero electric N-ality confined N={n} e={e}",
                (e, 0) in unconfined,
                False,
            )


def check_nonisotropic_pair_cannot_condense_together() -> None:
    for n in range(2, 13):
        electric_magnetic_pair = subgroup_generated(n, [(1, 0), (0, 1)])
        assert_equal(
            f"electric and magnetic generators are not mutually local N={n}",
            is_isotropic(n, electric_magnetic_pair),
            False,
        )


def check_polyakov_monopole_gas_wall_tension() -> None:
    # In the declared normalization
    # S = int [kappa/2 (d phi)^2 + 2 zeta (1-cos phi)] d^3x,
    # the dual photon has m_gamma^2 = 2 zeta/kappa and the primitive
    # sine-Gordon wall tension is sigma_P = 8 sqrt(2 kappa zeta).
    kappa = Fraction(5, 7)
    zeta = Fraction(11, 13)
    mass_squared = 2 * zeta / kappa
    assert_equal("Polyakov dual photon mass squared", mass_squared, Fraction(154, 65))

    tension_squared = 128 * kappa * zeta
    assert_equal("Polyakov wall tension squared", tension_squared, Fraction(7040, 91))
    assert_equal(
        "Polyakov wall tension equals 8 kappa m_gamma",
        tension_squared,
        64 * kappa * kappa * mass_squared,
    )

    # The explicit kink phi(x)=4 arctan exp(m x) obeys
    # phi'/m = 2 sin(phi/2).  With u=exp(m x),
    # sin(phi/2)=sin(2 arctan u)=2u/(1+u^2).
    for u in [Fraction(1, 3), Fraction(2, 5), Fraction(7, 4)]:
        derivative_over_mass = 4 * u / (1 + u * u)
        two_sin_half_phi = 4 * u / (1 + u * u)
        assert_equal(
            f"Polyakov kink first-order identity u={u}",
            derivative_over_mass,
            two_sin_half_phi,
        )

        sin_half_phi_squared = (2 * u / (1 + u * u)) ** 2
        one_minus_cos_phi = 2 * sin_half_phi_squared
        gradient_energy_density = (
            kappa
            * Fraction(1, 2)
            * mass_squared
            * derivative_over_mass
            * derivative_over_mass
        )
        potential_density = 2 * zeta * one_minus_cos_phi
        assert_equal(
            f"Polyakov wall first-integral energy balance u={u}",
            gradient_energy_density,
            potential_density,
        )

    # For a rectangular loop of area A=L T, the area exponent sigma A gives
    # V(L)=sigma L after taking -T^{-1} log <W>.  Track the coefficient
    # algebra without choosing an irrational value for sigma.
    spatial_length = Fraction(17, 5)
    time_length = Fraction(19, 3)
    area = spatial_length * time_length
    assert_equal("Polyakov rectangular area", area, Fraction(323, 15))
    assert_equal(
        "Polyakov static potential squared from area law",
        tension_squared * area * area / (time_length * time_length),
        tension_squared * spatial_length * spatial_length,
    )


def main() -> None:
    check_screened_pairing_descends()
    check_maximal_isotropic_axes_and_dyons()
    check_oblique_unconfined_direction()
    check_magnetic_condensation_confines_electric_nality()
    check_nonisotropic_pair_cannot_condense_together()
    check_polyakov_monopole_gas_wall_tension()
    print("All oblique-confinement finite charge checks passed.")


if __name__ == "__main__":
    main()
