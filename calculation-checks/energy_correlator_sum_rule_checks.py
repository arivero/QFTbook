#!/usr/bin/env python3
"""Exact finite-event checks for the EEC sum rules.

The script verifies the eventwise algebra behind the nonperturbative
energy-energy-correlator sum rules in the QCD chapter.  It does not model a
cross section; averaging positive event weights preserves these identities.
"""

from __future__ import annotations

from fractions import Fraction

Vector = tuple[Fraction, Fraction, Fraction]
Particle = tuple[Fraction, Vector]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def dot(a: Vector, b: Vector) -> Fraction:
    return sum(a[i] * b[i] for i in range(3))


def add(a: Vector, b: Vector) -> Vector:
    return tuple(a[i] + b[i] for i in range(3))  # type: ignore[return-value]


def scale(c: Fraction, a: Vector) -> Vector:
    return tuple(c * a[i] for i in range(3))  # type: ignore[return-value]


def event_total_energy_fraction(event: list[Particle]) -> Fraction:
    return sum(z for z, _ in event)


def event_momentum_fraction(event: list[Particle]) -> Vector:
    total: Vector = (Fraction(0), Fraction(0), Fraction(0))
    for z, n in event:
        total = add(total, scale(z, n))
    return total


def eec_zeroth_moment(event: list[Particle]) -> Fraction:
    return sum(z_i * z_j for z_i, _ in event for z_j, _ in event)


def eec_first_moment(event: list[Particle]) -> Fraction:
    return sum(z_i * z_j * dot(n_i, n_j) for z_i, n_i in event for z_j, n_j in event)


def eec_contact_weight(event: list[Particle]) -> Fraction:
    return sum(z * z for z, _ in event)


def check_two_body_back_to_back_event() -> None:
    event: list[Particle] = [
        (Fraction(1, 2), (Fraction(1), Fraction(0), Fraction(0))),
        (Fraction(1, 2), (Fraction(-1), Fraction(0), Fraction(0))),
    ]
    assert_equal("two-body total energy", event_total_energy_fraction(event), Fraction(1))
    assert_equal("two-body momentum", event_momentum_fraction(event), (Fraction(0), Fraction(0), Fraction(0)))
    assert_equal("two-body EEC zeroth moment", eec_zeroth_moment(event), Fraction(1))
    assert_equal("two-body EEC first moment", eec_first_moment(event), Fraction(0))
    assert_equal("two-body contact weight", eec_contact_weight(event), Fraction(1, 2))


def check_three_body_orthogonal_rational_event() -> None:
    # Three unit directions with rational dot products and zero weighted sum:
    # n1=(1,0,0), n2=(0,1,0), n3=(-3/5,-4/5,0), with weights 3/8, 1/2, 5/8
    # normalized by total weight 3/2.
    event: list[Particle] = [
        (Fraction(1, 4), (Fraction(1), Fraction(0), Fraction(0))),
        (Fraction(1, 3), (Fraction(0), Fraction(1), Fraction(0))),
        (Fraction(5, 12), (Fraction(-3, 5), Fraction(-4, 5), Fraction(0))),
    ]
    assert_equal("three-body total energy", event_total_energy_fraction(event), Fraction(1))
    assert_equal("three-body momentum", event_momentum_fraction(event), (Fraction(0), Fraction(0), Fraction(0)))
    assert_equal("three-body EEC zeroth moment", eec_zeroth_moment(event), Fraction(1))
    assert_equal("three-body EEC first moment", eec_first_moment(event), Fraction(0))
    assert_equal("three-body contact weight", eec_contact_weight(event), Fraction(25, 72))


def main() -> None:
    check_two_body_back_to_back_event()
    check_three_body_orthogonal_rational_event()
    print("All finite-event EEC sum-rule checks passed.")


if __name__ == "__main__":
    main()
