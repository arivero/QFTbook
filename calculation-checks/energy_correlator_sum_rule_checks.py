#!/usr/bin/env python3
"""Exact finite-event checks for energy-correlator detector algebra.

The script verifies the eventwise algebra behind the nonperturbative
energy-energy-correlator sum rules and the asymptotic multiplication-operator
model in the QCD chapter.  It does not model a cross section; averaging
positive event weights preserves these identities.  It also checks the
finite distinction between detector contact strata and ensemble-connected
cumulants.  The Legendre-multipole check verifies that contact-inclusive
EEC moments are positive quadratic forms of the calorimetric measure, while
separated-angle data alone need not preserve those positivity constraints.
"""

from __future__ import annotations

from collections.abc import Iterable
from fractions import Fraction
from math import factorial

Vector = tuple[Fraction, Fraction, Fraction]
Particle = tuple[Fraction, Vector]
WeightedEvent = tuple[Fraction, list[Particle]]


def assert_equal(name: str, got: object, expected: object) -> None:
    if got != expected:
        raise AssertionError(f"{name}: got {got!r}, expected {expected!r}")


def assert_true(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)


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


def legendre_value(ell: int, zeta: Fraction) -> Fraction:
    if ell == 0:
        return Fraction(1)
    if ell == 1:
        return zeta
    if ell == 2:
        return (3 * zeta * zeta - 1) / 2
    raise ValueError("only ell=0,1,2 are used in this finite check")


def eec_legendre_moment(event: list[Particle], ell: int, include_contact: bool = True) -> Fraction:
    total = Fraction(0)
    for r, (z_r, n_r) in enumerate(event):
        for s, (z_s, n_s) in enumerate(event):
            if not include_contact and r == s:
                continue
            total += z_r * z_s * legendre_value(ell, dot(n_r, n_s))
    return total


def quadrupole_tensor(event: list[Particle]) -> tuple[tuple[Fraction, Fraction, Fraction], ...]:
    rows: list[tuple[Fraction, Fraction, Fraction]] = []
    for i in range(3):
        row = []
        for j in range(3):
            entry = sum(
                z * (n[i] * n[j] - (Fraction(1, 3) if i == j else Fraction(0)))
                for z, n in event
            )
            row.append(entry)
        rows.append(tuple(row))  # type: ignore[arg-type]
    return tuple(rows)


def tensor_square_norm(tensor: tuple[tuple[Fraction, Fraction, Fraction], ...]) -> Fraction:
    return sum(tensor[i][j] * tensor[i][j] for i in range(3) for j in range(3))


def three_detector_zeroth_moment(event: list[Particle]) -> Fraction:
    return sum(
        z_i * z_j * z_k
        for z_i, _ in event
        for z_j, _ in event
        for z_k, _ in event
    )


def three_detector_pair_moment(
    event: list[Particle],
    first_slot: int,
    second_slot: int,
) -> Fraction:
    total = Fraction(0)
    for first_particle in event:
        for second_particle in event:
            for third_particle in event:
                particles = (first_particle, second_particle, third_particle)
                weight = particles[0][0] * particles[1][0] * particles[2][0]
                total += weight * dot(particles[first_slot][1], particles[second_slot][1])
    return total


def three_detector_contact_weights(event: list[Particle]) -> dict[str, Fraction]:
    all_distinct = Fraction(0)
    pair_12 = Fraction(0)
    pair_13 = Fraction(0)
    pair_23 = Fraction(0)
    all_same = Fraction(0)
    for r, (z_r, _) in enumerate(event):
        for s, (z_s, _) in enumerate(event):
            for t, (z_t, _) in enumerate(event):
                weight = z_r * z_s * z_t
                if r == s == t:
                    all_same += weight
                elif r == s:
                    pair_12 += weight
                elif r == t:
                    pair_13 += weight
                elif s == t:
                    pair_23 += weight
                else:
                    all_distinct += weight
    return {
        "all_distinct": all_distinct,
        "pair_12": pair_12,
        "pair_13": pair_13,
        "pair_23": pair_23,
        "all_same": all_same,
    }


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


def detector_product_values(event: list[Particle], test_values: list[list[Fraction]]) -> Fraction:
    result = Fraction(1)
    for values in test_values:
        result *= energy_detector_value(event, values)
    return result


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


def triple_contact_partition(
    event: list[Particle],
    f_values: list[Fraction],
    g_values: list[Fraction],
    h_values: list[Fraction],
) -> dict[str, Fraction]:
    if len(event) != len(f_values) or len(event) != len(g_values) or len(event) != len(h_values):
        raise ValueError("one detector-test value is required for each particle")

    all_distinct = Fraction(0)
    fg_contact = Fraction(0)
    fh_contact = Fraction(0)
    gh_contact = Fraction(0)
    all_contact = Fraction(0)
    for r, ((z_r, _), f_r, g_r, h_r) in enumerate(zip(event, f_values, g_values, h_values)):
        all_contact += z_r**3 * f_r * g_r * h_r
        for s, ((z_s, _), f_s, g_s, h_s) in enumerate(zip(event, f_values, g_values, h_values)):
            for t, ((z_t, _), f_t, g_t, h_t) in enumerate(zip(event, f_values, g_values, h_values)):
                term = z_r * z_s * z_t * f_r * g_s * h_t
                if r == s == t:
                    continue
                if r == s:
                    fg_contact += term
                elif r == t:
                    fh_contact += term
                elif s == t:
                    gh_contact += term
                else:
                    all_distinct += term
    return {
        "all_distinct": all_distinct,
        "fg_contact": fg_contact,
        "fh_contact": fh_contact,
        "gh_contact": gh_contact,
        "all_contact": all_contact,
    }


def set_partitions(items: tuple[int, ...]) -> Iterable[tuple[tuple[int, ...], ...]]:
    if not items:
        yield ()
        return
    first, *rest = items
    for partition in set_partitions(tuple(rest)):
        yield ((first,),) + partition
        for block_index, block in enumerate(partition):
            new_block = tuple(sorted((first,) + block))
            yield partition[:block_index] + (new_block,) + partition[block_index + 1 :]


def raw_ensemble_moment(
    ensemble: list[WeightedEvent],
    test_values_by_event: list[list[list[Fraction]]],
    indices: tuple[int, ...],
) -> Fraction:
    total = Fraction(0)
    for event_index, (weight, event) in enumerate(ensemble):
        selected_tests = [test_values_by_event[event_index][i] for i in indices]
        total += weight * detector_product_values(event, selected_tests)
    return total


def ensemble_cumulant(
    ensemble: list[WeightedEvent],
    test_values_by_event: list[list[list[Fraction]]],
    indices: tuple[int, ...],
) -> Fraction:
    total = Fraction(0)
    for partition in set_partitions(indices):
        coefficient = Fraction((-1) ** (len(partition) - 1) * factorial(len(partition) - 1))
        block_product = Fraction(1)
        for block in partition:
            block_product *= raw_ensemble_moment(ensemble, test_values_by_event, block)
        total += coefficient * block_product
    return total


def endpoint_delta_solution(open_zeroth: Fraction, open_first: Fraction) -> tuple[Fraction, Fraction]:
    contact_at_plus = (Fraction(1) - open_zeroth - open_first) / 2
    back_to_back_atom = (Fraction(1) - open_zeroth + open_first) / 2
    return contact_at_plus, back_to_back_atom


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


def check_eec_legendre_multipole_positivity() -> None:
    event: list[Particle] = [
        (Fraction(1, 4), (Fraction(1), Fraction(0), Fraction(0))),
        (Fraction(1, 3), (Fraction(0), Fraction(1), Fraction(0))),
        (Fraction(5, 12), (Fraction(-3, 5), Fraction(-4, 5), Fraction(0))),
    ]
    momentum = event_momentum_fraction(event)
    momentum_norm_squared = dot(momentum, momentum)
    quadrupole = quadrupole_tensor(event)
    quadrupole_norm_squared = tensor_square_norm(quadrupole)

    assert_equal("EEC Legendre M0", eec_legendre_moment(event, 0), Fraction(1))
    assert_equal("EEC Legendre M1 as momentum square", eec_legendre_moment(event, 1), momentum_norm_squared)
    assert_equal("EEC Legendre M1 center-of-mass", eec_legendre_moment(event, 1), Fraction(0))
    assert_equal("EEC quadrupole norm", quadrupole_norm_squared, Fraction(4, 15))
    assert_equal(
        "EEC Legendre M2 as quadrupole square",
        eec_legendre_moment(event, 2),
        Fraction(3, 2) * quadrupole_norm_squared,
    )
    assert_equal("EEC Legendre M2 value", eec_legendre_moment(event, 2), Fraction(2, 5))
    for ell in range(3):
        assert_true(
            f"contact-inclusive Legendre moment ell={ell} is nonnegative",
            eec_legendre_moment(event, ell) >= 0,
        )

    separated_first_moment = eec_legendre_moment(event, 1, include_contact=False)
    assert_equal("separated first Legendre moment misses contact", separated_first_moment, -eec_contact_weight(event))
    assert_true(
        "separated-angle EEC alone can violate Legendre positivity",
        separated_first_moment < 0,
    )


def check_three_detector_moment_and_contact_ledger() -> None:
    event: list[Particle] = [
        (Fraction(1, 4), (Fraction(1), Fraction(0), Fraction(0))),
        (Fraction(1, 3), (Fraction(0), Fraction(1), Fraction(0))),
        (Fraction(5, 12), (Fraction(-3, 5), Fraction(-4, 5), Fraction(0))),
    ]
    assert_equal("three-detector total energy", event_total_energy_fraction(event), Fraction(1))
    assert_equal("three-detector total momentum", event_momentum_fraction(event), (Fraction(0), Fraction(0), Fraction(0)))
    assert_equal("three-detector zeroth moment", three_detector_zeroth_moment(event), Fraction(1))
    assert_equal("three-detector zeta12 moment", three_detector_pair_moment(event, 0, 1), Fraction(0))
    assert_equal("three-detector zeta13 moment", three_detector_pair_moment(event, 0, 2), Fraction(0))
    assert_equal("three-detector zeta23 moment", three_detector_pair_moment(event, 1, 2), Fraction(0))

    contact_weights = three_detector_contact_weights(event)
    assert_equal("three-detector all-same contact weight", contact_weights["all_same"], Fraction(1, 8))
    assert_equal("three-detector 12 pair-contact weight", contact_weights["pair_12"], Fraction(2, 9))
    assert_equal("three-detector 13 pair-contact weight", contact_weights["pair_13"], Fraction(2, 9))
    assert_equal("three-detector 23 pair-contact weight", contact_weights["pair_23"], Fraction(2, 9))
    assert_equal("three-detector all-distinct separated weight", contact_weights["all_distinct"], Fraction(5, 24))
    assert_equal(
        "three-detector contact partition exhausts unit moment",
        sum(contact_weights.values(), Fraction(0)),
        three_detector_zeroth_moment(event),
    )
    if contact_weights["all_distinct"] == three_detector_zeroth_moment(event):
        raise AssertionError("separated three-detector weight should not include contact strata")


def check_endpoint_matching_delta_ledger() -> None:
    # A truncated open-interval matched distribution has finite moments I0,I1.
    # If both endpoint delta coordinates are retained, the two exact EEC moment
    # sum rules solve for their coefficients.
    open_zeroth = Fraction(7, 10)
    open_first = Fraction(-1, 5)
    contact_at_plus, back_to_back_atom = endpoint_delta_solution(open_zeroth, open_first)
    assert_equal("matched endpoint contact coordinate", contact_at_plus, Fraction(1, 4))
    assert_equal("matched endpoint back-to-back coordinate", back_to_back_atom, Fraction(1, 20))
    assert_equal(
        "matched zeroth moment",
        open_zeroth + contact_at_plus + back_to_back_atom,
        Fraction(1),
    )
    assert_equal(
        "matched first moment",
        open_first + contact_at_plus - back_to_back_atom,
        Fraction(0),
    )

    # If the coincident-detector contact coordinate is fixed independently,
    # the same equations become a consistency check for the remaining endpoint
    # atom and the open-interval approximation.
    fixed_contact = Fraction(1, 4)
    inferred_back_to_back = Fraction(1) - open_zeroth - fixed_contact
    assert_equal("fixed-contact inferred endpoint atom", inferred_back_to_back, Fraction(1, 20))
    assert_equal(
        "fixed-contact first-moment consistency",
        open_first + fixed_contact - inferred_back_to_back,
        Fraction(0),
    )


def check_connected_cumulants_do_not_remove_detector_contacts() -> None:
    event_a: list[Particle] = [
        (Fraction(1, 2), (Fraction(1), Fraction(0), Fraction(0))),
        (Fraction(1, 2), (Fraction(-1), Fraction(0), Fraction(0))),
    ]
    event_b: list[Particle] = [
        (Fraction(1, 4), (Fraction(1), Fraction(0), Fraction(0))),
        (Fraction(1, 3), (Fraction(0), Fraction(1), Fraction(0))),
        (Fraction(5, 12), (Fraction(-3, 5), Fraction(-4, 5), Fraction(0))),
    ]
    ensemble: list[WeightedEvent] = [(Fraction(2, 5), event_a), (Fraction(3, 5), event_b)]
    tests_by_event = [
        [
            [Fraction(2, 3), Fraction(-5, 7)],
            [Fraction(11, 13), Fraction(3, 5)],
            [Fraction(-7, 17), Fraction(19, 23)],
        ],
        [
            [Fraction(2, 5), Fraction(-1, 7), Fraction(3, 11)],
            [Fraction(-5, 13), Fraction(4, 9), Fraction(7, 15)],
            [Fraction(6, 17), Fraction(-2, 19), Fraction(5, 23)],
        ],
    ]

    moment_01 = raw_ensemble_moment(ensemble, tests_by_event, (0, 1))
    product_0_1 = raw_ensemble_moment(ensemble, tests_by_event, (0,)) * raw_ensemble_moment(
        ensemble, tests_by_event, (1,)
    )
    assert_equal(
        "second cumulant subtracts ensemble factorization",
        ensemble_cumulant(ensemble, tests_by_event, (0, 1)),
        moment_01 - product_0_1,
    )

    m0 = raw_ensemble_moment(ensemble, tests_by_event, (0,))
    m1 = raw_ensemble_moment(ensemble, tests_by_event, (1,))
    m2 = raw_ensemble_moment(ensemble, tests_by_event, (2,))
    m01 = raw_ensemble_moment(ensemble, tests_by_event, (0, 1))
    m02 = raw_ensemble_moment(ensemble, tests_by_event, (0, 2))
    m12 = raw_ensemble_moment(ensemble, tests_by_event, (1, 2))
    m012 = raw_ensemble_moment(ensemble, tests_by_event, (0, 1, 2))
    assert_equal(
        "third cumulant partition formula",
        ensemble_cumulant(ensemble, tests_by_event, (0, 1, 2)),
        m012 - m01 * m2 - m02 * m1 - m12 * m0 + 2 * m0 * m1 * m2,
    )

    deterministic_ensemble: list[WeightedEvent] = [(Fraction(1), event_b)]
    deterministic_tests = [tests_by_event[1]]
    assert_equal(
        "deterministic second ensemble cumulant vanishes",
        ensemble_cumulant(deterministic_ensemble, deterministic_tests, (0, 1)),
        Fraction(0),
    )
    assert_equal(
        "deterministic third ensemble cumulant vanishes",
        ensemble_cumulant(deterministic_ensemble, deterministic_tests, (0, 1, 2)),
        Fraction(0),
    )

    triple_parts = triple_contact_partition(event_b, *tests_by_event[1])
    reconstructed = sum(triple_parts.values(), Fraction(0))
    assert_equal(
        "triple detector contact-stratum partition",
        reconstructed,
        detector_product_values(event_b, tests_by_event[1]),
    )
    assert_true("same-hadron triple contact remains in a deterministic event", triple_parts["all_contact"] != 0)


def main() -> None:
    check_two_body_back_to_back_event()
    check_three_body_orthogonal_rational_event()
    check_eec_legendre_multipole_positivity()
    check_three_detector_moment_and_contact_ledger()
    check_endpoint_matching_delta_ledger()
    check_connected_cumulants_do_not_remove_detector_contacts()
    print("All finite-event energy-correlator detector-algebra checks passed.")


if __name__ == "__main__":
    main()
