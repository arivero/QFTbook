#!/usr/bin/env python3
"""Exact finite checks for confinement and oblique-confinement diagnostics.

The manuscript uses the finite center-sensitive charge group

    C_N = Z_N^e direct-sum Z_N^m

with pairing ((e,m),(e',m')) -> (e m' - e' m) / N mod 1.  These checks verify
the arithmetic behind screening quotients, orthogonal complements of
condensates, and the dyonic unconfined direction in oblique confinement.  The
script does not simulate a gauge theory or prove that a condensate forms.
"""

from __future__ import annotations

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


def main() -> None:
    check_screened_pairing_descends()
    check_maximal_isotropic_axes_and_dyons()
    check_oblique_unconfined_direction()
    check_magnetic_condensation_confines_electric_nality()
    check_nonisotropic_pair_cannot_condense_together()
    print("All oblique-confinement finite charge checks passed.")


if __name__ == "__main__":
    main()
