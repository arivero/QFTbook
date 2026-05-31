#!/usr/bin/env python3
"""Exact finite-event checks for energy-correlator detector algebra.

The script verifies the eventwise algebra behind the nonperturbative
energy-energy-correlator sum rules and the asymptotic multiplication-operator
model in the QCD chapter.  It does not model a cross section; averaging
positive event weights preserves these identities.
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


def energy_detector_value(event: list[Particle], values: list[Fraction]) -> Fraction:
    if len(event) != len(values):
        raise ValueError("one detector-test value is required for each particle")
    return sum(z * f for (z, _), f in zip(event, values))


def detector_product_value(
    event: list[Particle],
    left_values: list[Fraction],
    right_values: list[Fraction],
) -> Fraction:
    return energy_detector_value(event, left_values) * energy_detector_value(event, right_values)


def product_measure_pairing(
    event: list[Particle],
    left_values: list[Fraction],
    right_values: list[Fraction],
) -> Fraction:
    if len(event) != len(left_values) or len(event) != len(right_values):
        raise ValueError("one detector-test value is required for each particle")
    return sum(
        z_i * z_j * f_i * g_j
        for (z_i, _), f_i in zip(event, left_values)
        for (z_j, _), g_j in zip(event, right_values)
    )


def diagonal_pairing(
    event: list[Particle],
    left_values: list[Fraction],
    right_values: list[Fraction],
) -> Fraction:
    if len(event) != len(left_values) or len(event) != len(right_values):
        raise ValueError("one detector-test value is required for each particle")
    return sum(z * z * f * g for (z, _), f, g in zip(event, left_values, right_values))


def sup_norm(values: list[Fraction]) -> Fraction:
    return max(abs(value) for value in values)


def assert_detector_bound(event: list[Particle], values: list[Fraction], name: str) -> None:
    total_energy = event_total_energy_fraction(event)
    value = energy_detector_value(event, values)
    if abs(value) > sup_norm(values) * total_energy:
        raise AssertionError(f"{name}: detector bound failed")


def check_multiplication_model_for_event(
    event: list[Particle],
    left_values: list[Fraction],
    right_values: list[Fraction],
    name: str,
) -> None:
    assert_equal(
        f"{name} constant detector",
        energy_detector_value(event, [Fraction(1)] * len(event)),
        event_total_energy_fraction(event),
    )
    assert_detector_bound(event, left_values, f"{name} left bound")
    assert_detector_bound(event, right_values, f"{name} right bound")
    assert_equal(
        f"{name} product measure",
        detector_product_value(event, left_values, right_values),
        product_measure_pairing(event, left_values, right_values),
    )
    assert_equal(
        f"{name} diagonal contact",
        diagonal_pairing(event, [Fraction(1)] * len(event), [Fraction(1)] * len(event)),
        eec_contact_weight(event),
    )


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
    check_multiplication_model_for_event(
        event,
        [Fraction(2, 3), Fraction(-5, 7)],
        [Fraction(11, 13), Fraction(3, 5)],
        "two-body multiplication model",
    )


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
    check_multiplication_model_for_event(
        event,
        [Fraction(2, 5), Fraction(-1, 7), Fraction(3, 11)],
        [Fraction(-5, 13), Fraction(4, 9), Fraction(7, 15)],
        "three-body multiplication model",
    )


def main() -> None:
    check_two_body_back_to_back_event()
    check_three_body_orthogonal_rational_event()
    print("All finite-event energy-correlator detector-algebra checks passed.")


if __name__ == "__main__":
    main()
