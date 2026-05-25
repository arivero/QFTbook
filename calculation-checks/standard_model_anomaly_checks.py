#!/usr/bin/env python3
"""Finite representation checks for one Standard Model generation.

The chapter uses left-handed Weyl fields:

    Q_L : (3,2)_{1/6}
    u^c : (bar 3,1)_{-2/3}
    d^c : (bar 3,1)_{1/3}
    L_L : (1,2)_{-1/2}
    e^c : (1,1)_1

The script checks the hypercharge anomaly sums and the even number of weak
doublets needed to avoid the finite SU(2) anomaly.
"""

from __future__ import annotations

from fractions import Fraction


FIELDS = [
    ("Q_L", 3, 2, Fraction(1, 6), True),
    ("u^c", 3, 1, Fraction(-2, 3), False),
    ("d^c", 3, 1, Fraction(1, 3), False),
    ("L_L", 1, 2, Fraction(-1, 2), True),
    ("e^c", 1, 1, Fraction(1, 1), False),
]


def assert_zero(name: str, value: Fraction) -> None:
    if value != 0:
        raise AssertionError(f"{name} = {value}, expected 0")


def check_su3_su3_u1() -> None:
    # The common quadratic index T(3)=T(bar 3) factors out.
    value = sum(su2_dim * hypercharge for _, su3_dim, su2_dim, hypercharge, _ in FIELDS if su3_dim == 3)
    assert_zero("SU(3)^2 U(1)_Y anomaly coefficient without common T(3)", value)


def check_su2_su2_u1() -> None:
    # The common quadratic index T(2) factors out.
    value = sum(su3_dim * hypercharge for _, su3_dim, su2_dim, hypercharge, _ in FIELDS if su2_dim == 2)
    assert_zero("SU(2)^2 U(1)_Y anomaly coefficient without common T(2)", value)


def check_u1_cubic() -> None:
    value = sum(su3_dim * su2_dim * hypercharge**3 for _, su3_dim, su2_dim, hypercharge, _ in FIELDS)
    assert_zero("U(1)_Y^3 anomaly coefficient", value)


def check_mixed_gravitational_u1() -> None:
    value = sum(su3_dim * su2_dim * hypercharge for _, su3_dim, su2_dim, hypercharge, _ in FIELDS)
    assert_zero("mixed gravitational-U(1)_Y anomaly coefficient", value)


def check_witten_su2_anomaly() -> None:
    doublets = sum(su3_dim for _, su3_dim, su2_dim, _, is_weak_doublet in FIELDS if is_weak_doublet and su2_dim == 2)
    if doublets % 2 != 0:
        raise AssertionError(f"weak SU(2) doublets per generation = {doublets}, expected even")
    if 3 * doublets % 2 != 0:
        raise AssertionError("three-generation weak-doublet count should remain even")


def check_electric_charges() -> None:
    q_up = Fraction(1, 2) + Fraction(1, 6)
    q_down = Fraction(-1, 2) + Fraction(1, 6)
    q_nu = Fraction(1, 2) + Fraction(-1, 2)
    q_e = Fraction(-1, 2) + Fraction(-1, 2)
    expected = (Fraction(2, 3), Fraction(-1, 3), Fraction(0), Fraction(-1))
    actual = (q_up, q_down, q_nu, q_e)
    if actual != expected:
        raise AssertionError(f"electric charges {actual} != {expected}")


def main() -> None:
    check_su3_su3_u1()
    check_su2_su2_u1()
    check_u1_cubic()
    check_mixed_gravitational_u1()
    check_witten_su2_anomaly()
    check_electric_charges()
    print("All Standard Model hypercharge and weak-doublet checks passed.")


if __name__ == "__main__":
    main()
