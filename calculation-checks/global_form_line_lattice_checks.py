#!/usr/bin/env python3
"""Exact finite checks for global forms and Wilson-'t Hooft line lattices.

The script checks only the finite center-sensitive arithmetic used in Volume IX,
Chapter 1.  It does not define continuum line operators or prove existence of
the corresponding gauge theories.  The mathematical object checked here is the
finite symplectic abelian group

    Z_N^e direct-sum Z_N^m

with pairing ((e,m),(e',m')) -> (e m' - e' m) / N mod 1.

It also checks the finite phase bookkeeping behind the higher-form linking
definition: for A=Z_N, a defect label a, charge q, and oriented intersection
number L, the character phase is recorded by the exponent a q L modulo N.
"""

from __future__ import annotations

from itertools import product


Charge = tuple[int, int]


def assert_equal(name: str, lhs: object, rhs: object) -> None:
    if lhs != rhs:
        raise AssertionError(f"{name}: got {lhs!r}, expected {rhs!r}")


def add_charge(n: int, lhs: Charge, rhs: Charge) -> Charge:
    return ((lhs[0] + rhs[0]) % n, (lhs[1] + rhs[1]) % n)


def scale_charge(n: int, coefficient: int, charge: Charge) -> Charge:
    return ((coefficient * charge[0]) % n, (coefficient * charge[1]) % n)


def dirac_numerator(n: int, lhs: Charge, rhs: Charge) -> int:
    """Return N times the finite Dirac pairing, reduced modulo N."""

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
        candidate
        for candidate in all_charges(n)
        if all(dirac_numerator(n, candidate, line) == 0 for line in subgroup)
    }


def check_pairing_axioms(n: int) -> None:
    zero = (0, 0)
    charges = all_charges(n)
    for charge in charges:
        assert_equal(f"alternating self-pairing N={n} charge={charge}", dirac_numerator(n, charge, charge), 0)
        assert_equal(f"zero left pairing N={n} charge={charge}", dirac_numerator(n, zero, charge), 0)
        assert_equal(f"zero right pairing N={n} charge={charge}", dirac_numerator(n, charge, zero), 0)

    for lhs, rhs in product(charges, repeat=2):
        antisymmetric = (dirac_numerator(n, lhs, rhs) + dirac_numerator(n, rhs, lhs)) % n
        assert_equal(f"antisymmetry N={n} lhs={lhs} rhs={rhs}", antisymmetric, 0)

    for lhs, rhs, third in product(charges, repeat=3):
        left_sum = dirac_numerator(n, add_charge(n, lhs, rhs), third)
        right_sum = (dirac_numerator(n, lhs, third) + dirac_numerator(n, rhs, third)) % n
        assert_equal(f"left bilinearity N={n} lhs={lhs} rhs={rhs} third={third}", left_sum, right_sum)

        right_arg_sum = dirac_numerator(n, lhs, add_charge(n, rhs, third))
        split_sum = (dirac_numerator(n, lhs, rhs) + dirac_numerator(n, lhs, third)) % n
        assert_equal(f"right bilinearity N={n} lhs={lhs} rhs={rhs} third={third}", right_arg_sum, split_sum)

    for charge in charges:
        if charge == zero:
            continue
        witnesses = [other for other in charges if dirac_numerator(n, charge, other) != 0]
        if not witnesses:
            raise AssertionError(f"nondegeneracy failed for N={n}, charge={charge}")


def divisors(n: int) -> list[int]:
    return [candidate for candidate in range(1, n + 1) if n % candidate == 0]


def check_su_n_mod_z_k_descent(n: int, k: int) -> None:
    electric_allowed = {e for e in range(n) if e % k == 0}
    expected_electric = {(k * a) % n for a in range(n)}
    assert_equal(f"SU({n})/Z_{k} electric descent", electric_allowed, expected_electric)
    assert_equal(f"SU({n})/Z_{k} electric quotient size", len(electric_allowed), n // k)

    magnetic_allowed = {((n // k) * b) % n for b in range(n)}
    assert_equal(f"SU({n})/Z_{k} magnetic quotient size", len(magnetic_allowed), k)

    for e, m in product(electric_allowed, magnetic_allowed):
        assert_equal(
            f"SU({n})/Z_{k} electric-magnetic integrality e={e} m={m}",
            (e * m) % n,
            0,
        )


def check_line_lattice(n: int, k: int, p: int) -> None:
    subgroup = subgroup_generated(n, [(k, 0), (p, n // k)])
    assert_equal(f"L_{{{n},{k},{p}}} size", len(subgroup), n)

    for lhs, rhs in product(subgroup, repeat=2):
        assert_equal(
            f"L_{{{n},{k},{p}}} isotropy lhs={lhs} rhs={rhs}",
            dirac_numerator(n, lhs, rhs),
            0,
        )

    assert_equal(
        f"L_{{{n},{k},{p}}} maximality",
        orthogonal_complement(n, subgroup),
        subgroup,
    )


def check_named_axes(n: int) -> None:
    su_n = subgroup_generated(n, [(1, 0)])
    psu_n = subgroup_generated(n, [(0, 1)])
    assert_equal(f"SU({n}) axis size", len(su_n), n)
    assert_equal(f"PSU({n}) axis size", len(psu_n), n)
    assert_equal(f"SU({n}) axis maximal isotropic", orthogonal_complement(n, su_n), su_n)
    assert_equal(f"PSU({n}) axis maximal isotropic", orthogonal_complement(n, psu_n), psu_n)
    assert_equal(f"fundamental Wilson/minimal 't Hooft nonlocality N={n}", dirac_numerator(n, (1, 0), (0, 1)), 1 % n)


def linking_phase_exponent(n: int, defect: int, charge: int, intersections: list[int]) -> int:
    """Return the Z_N exponent of a finite higher-form linking phase."""

    oriented_linking = sum(intersections)
    return (defect * charge * oriented_linking) % n


def check_higher_form_linking_phase(n: int) -> None:
    for defect, charge in product(range(n), repeat=2):
        base = [1, 1, -1]
        base_phase = linking_phase_exponent(n, defect, charge, base)

        deformation_away_from_charge = base + [1, -1]
        assert_equal(
            f"Z_{n} linking deformation invariance a={defect} q={charge}",
            linking_phase_exponent(n, defect, charge, deformation_away_from_charge),
            base_phase,
        )

        crossing_once = base + [1]
        assert_equal(
            f"Z_{n} linking crossing phase a={defect} q={charge}",
            (linking_phase_exponent(n, defect, charge, crossing_once) - base_phase) % n,
            (defect * charge) % n,
        )

        reversed_orientation = [-entry for entry in base]
        assert_equal(
            f"Z_{n} linking orientation reversal a={defect} q={charge}",
            linking_phase_exponent(n, defect, charge, reversed_orientation),
            (-base_phase) % n,
        )

    for defect_a, defect_b, charge in product(range(n), repeat=3):
        intersections = [1, -1, 1, 1]
        fused_defect = linking_phase_exponent(n, (defect_a + defect_b) % n, charge, intersections)
        product_defects = (
            linking_phase_exponent(n, defect_a, charge, intersections)
            + linking_phase_exponent(n, defect_b, charge, intersections)
        ) % n
        assert_equal(
            f"Z_{n} linking defect group law a={defect_a} b={defect_b} q={charge}",
            fused_defect,
            product_defects,
        )

    for defect, charge_q, charge_r in product(range(n), repeat=3):
        intersections = [1, 1, -1, 1]
        fused_charge = linking_phase_exponent(n, defect, (charge_q + charge_r) % n, intersections)
        product_charges = (
            linking_phase_exponent(n, defect, charge_q, intersections)
            + linking_phase_exponent(n, defect, charge_r, intersections)
        ) % n
        assert_equal(
            f"Z_{n} linking charge fusion a={defect} q={charge_q} r={charge_r}",
            fused_charge,
            product_charges,
        )


def main() -> None:
    for n in range(2, 10):
        check_pairing_axioms(n)
        check_named_axes(n)
        check_higher_form_linking_phase(n)
        for k in divisors(n):
            check_su_n_mod_z_k_descent(n, k)
            for p in range(k):
                check_line_lattice(n, k, p)

    print("All global-form, finite line-lattice, and linking-phase checks passed.")


if __name__ == "__main__":
    main()
