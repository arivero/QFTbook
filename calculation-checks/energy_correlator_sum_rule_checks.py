#!/usr/bin/env python3
r"""Exact finite-event checks for energy-correlator detector algebra.

The script verifies the eventwise algebra behind the nonperturbative
energy-energy-correlator sum rules and the asymptotic multiplication-operator
model in the QCD chapter.  It does not model a cross section; averaging
positive event weights preserves these identities.  It also checks the
finite distinction between detector contact strata and ensemble-connected
cumulants.  The Legendre-multipole check verifies that contact-inclusive
EEC moments are positive quadratic forms of the calorimetric measure, while
separated-angle data alone need not preserve those positivity constraints.
The bin-resolved contact check verifies that a one-variable EEC contact atom
at \(\zeta=1\) fixes only the projected total diagonal mass: same-bin
detector products require the pre-pushforward diagonal measure.
Finally, it tests a finite-resolution detector map and residual ledger: a
Lipschitz smeared correlator changes by at most the declared bin diameter
times the total energy power, and an observable-level budget must include that
detector binning term rather than relying on signed residual cancellation.

Evidence contract.

Target claims:
  Volume II, Chapter 19 and the jet-observable continuation formulate the EEC
  as a positive calorimetric product measure, keep the coincident-detector
  contact coordinate in the zeroth and first moment ledger, distinguish
  projected one-variable EEC endpoint atoms from bin-resolved detector
  contacts, and separate ensemble-connected cumulants from same-event
  diagonal strata.

Independent construction:
  The checks build finite final states from rational energy fractions and
  rational unit vectors, expand detector products directly as finite sums over
  hadron labels, compute Legendre multipoles from the calorimetric measure,
  solve endpoint-atom moment equations, and compare bin-resolved diagonal
  contact pairings with their one-variable projected masses.  They do not use
  displayed manuscript formulas as assumed expected answers.

Imported assumptions:
  The existence of energy-flow detectors on scattering states, positivity of
  physical event weights, the passage from finite detector sums to continuum
  calorimetric distributions, perturbative factorization/OPE inputs for
  endpoint charts, and detector-response modelling are imported QFT inputs.

Negative controls:
  The suite rejects separated-angle EEC data as a contact-inclusive moment
  ledger, treating total diagonal contact mass as bin-resolved detector
  contact data, deleting same-event contacts by taking ensemble cumulants,
  omitting endpoint atoms in global moment closure, and dropping the
  finite-resolution binning term from a measured-observable residual budget.

Scope boundary:
  These are exact finite-event algebra, moment, contact, endpoint, and
  detector-resolution checks.  They are not a proof of perturbative QCD
  factorization, a construction of the energy-flow operator, a continuum
  calorimeter limit, a cross-section calculation, or an experimental detector
  simulation.

Primary derivation route:
  The manuscript route starts with the calorimetric measure of a hadronic
  final state, forms product measures and their diagonal contact strata,
  projects to the one-variable EEC, closes the zeroth and first moment ledger
  by endpoint/contact atoms, and then transports the resulting coordinates
  through finite detector bins and response covariances.

Independent verification route:
  The executable route uses rational two- and three-body events.  It checks
  total energy, center-of-mass momentum, EEC moments, Legendre positivity,
  three-detector contact partitions, endpoint-atom solving, finite-resolution
  Lipschitz budgets, ensemble cumulant partition formulae, and a negative
  control where the projected \(\zeta=1\) contact atom is held fixed while a
  same-bin detector product changes.

Convention dependencies:
  Energy fractions are normalized to total event or selected energy, angular
  coordinates use \(\zeta=\cos\chi=\mathbf n_i\cdot\mathbf n_j\), ordered
  detector products use the product measure \(\mu_X^{\otimes k}\), diagonal
  contacts include all same-hadron label coincidences, and endpoint atoms sit
  at \(\zeta=1\) and \(\zeta=-1\) in the normalized EEC ledger.

Domain and remainder assumptions:
  The finite identities apply to finite positive final states before continuum
  limits.  Physical predictions still require event-weight averaging,
  perturbative and nonperturbative remainder estimates, endpoint subtraction
  conventions, detector-bin diameters, and response/noise budgets.

Remaining unproved or conditional:
  The checks leave open the QCD factorization theorem for the chosen measured
  EEC, the light-ray OPE convergence domain, the continuum detector-response
  limit, and the size of omitted perturbative, power, endpoint, and
  hadronization corrections in any phenomenological application.
"""

from __future__ import annotations

from collections.abc import Iterable
from fractions import Fraction
from math import factorial

from check_utils import assert_leq as _assert_leq

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


def contact_weight_pairing(
    contact_weights: list[Fraction],
    left_values: list[Fraction],
    right_values: list[Fraction],
) -> Fraction:
    if len(contact_weights) != len(left_values) or len(contact_weights) != len(right_values):
        raise ValueError("one detector-test value is required for each contact weight")
    return sum(weight * f * g for weight, f, g in zip(contact_weights, left_values, right_values))


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


def finite_resolution_kernel(x: Fraction, y: Fraction) -> Fraction:
    return Fraction(3) + x / 2 - y / 7 + x * y / 5


def smeared_pair_coordinate(
    energies: list[Fraction],
    coordinates: list[Fraction],
) -> Fraction:
    if len(energies) != len(coordinates):
        raise ValueError("one detector coordinate is required for each energy")
    return sum(
        z_i * z_j * finite_resolution_kernel(coordinates[i], coordinates[j])
        for i, z_i in enumerate(energies)
        for j, z_j in enumerate(energies)
    )


def sup_norm(values: list[Fraction]) -> Fraction:
    return max(abs(value) for value in values)


def assert_detector_bound(event: list[Particle], values: list[Fraction], name: str) -> None:
    total_energy = event_total_energy_fraction(event)
    value = energy_detector_value(event, values)
    _assert_leq(name, abs(value), sup_norm(values) * total_energy)


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


def check_projected_contact_mass_does_not_fix_detector_bins() -> None:
    event: list[Particle] = [
        (Fraction(1, 2), (Fraction(1), Fraction(0), Fraction(0))),
        (Fraction(1, 3), (Fraction(0), Fraction(1), Fraction(0))),
        (Fraction(1, 6), (Fraction(0), Fraction(0), Fraction(1))),
    ]
    actual_contact_weights = [z * z for z, _ in event]
    shifted_contact_weights = [
        Fraction(0),
        actual_contact_weights[0] + actual_contact_weights[1],
        actual_contact_weights[2],
    ]
    assert_equal(
        "same projected contact mass",
        sum(actual_contact_weights, Fraction(0)),
        sum(shifted_contact_weights, Fraction(0)),
    )
    for ell in range(3):
        assert_equal(
            f"projected contact Legendre atom ell={ell}",
            sum(actual_contact_weights, Fraction(0)) * legendre_value(ell, Fraction(1)),
            sum(shifted_contact_weights, Fraction(0)) * legendre_value(ell, Fraction(1)),
        )

    constant_cell = [Fraction(1), Fraction(1), Fraction(1)]
    assert_equal(
        "constant detector sees only total contact mass",
        contact_weight_pairing(actual_contact_weights, constant_cell, constant_cell),
        contact_weight_pairing(shifted_contact_weights, constant_cell, constant_cell),
    )

    first_cell = [Fraction(1), Fraction(0), Fraction(0)]
    second_cell = [Fraction(0), Fraction(1), Fraction(0)]
    assert_equal(
        "actual first-cell diagonal contact",
        contact_weight_pairing(actual_contact_weights, first_cell, first_cell),
        Fraction(1, 4),
    )
    assert_equal(
        "shifted first-cell diagonal contact",
        contact_weight_pairing(shifted_contact_weights, first_cell, first_cell),
        Fraction(0),
    )
    assert_equal(
        "actual second-cell diagonal contact",
        contact_weight_pairing(actual_contact_weights, second_cell, second_cell),
        Fraction(1, 9),
    )
    assert_equal(
        "shifted second-cell diagonal contact",
        contact_weight_pairing(shifted_contact_weights, second_cell, second_cell),
        Fraction(13, 36),
    )
    assert_true(
        "projected contact atom cannot be used as bin-resolved contact data",
        contact_weight_pairing(actual_contact_weights, first_cell, first_cell)
        != contact_weight_pairing(shifted_contact_weights, first_cell, first_cell),
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


def check_finite_resolution_detector_assembly_budget() -> None:
    energies = [Fraction(1, 4), Fraction(1, 3), Fraction(5, 12)]
    true_coordinates = [Fraction(1, 10), Fraction(9, 20), Fraction(4, 5)]
    binned_representatives = [Fraction(0), Fraction(1, 2), Fraction(3, 4)]

    total_energy = sum(energies, Fraction(0))
    assert_equal("finite-resolution total energy", total_energy, Fraction(1))

    full_coordinate = smeared_pair_coordinate(energies, true_coordinates)
    binned_coordinate = smeared_pair_coordinate(energies, binned_representatives)
    binning_error = abs(full_coordinate - binned_coordinate)

    # On 0 <= x,y <= 1, this kernel has slotwise Lipschitz constant at most
    # 7/10 for the l1 product metric.  Moving each detector atom by at most
    # delta in each slot gives the k L E^k delta estimate with k=2.
    kernel_lipschitz = Fraction(7, 10)
    detector_diameter = Fraction(1, 10)
    binning_bound = 2 * kernel_lipschitz * total_energy**2 * detector_diameter
    assert_equal("finite-resolution exact binned difference", binning_error, Fraction(1553, 96000))
    _assert_leq("finite-resolution Lipschitz detector bound", binning_error, binning_bound)

    perturbative_defect = Fraction(1, 120)
    contact_defect = -Fraction(1, 140)
    hadronization_defect = Fraction(1, 150)
    actual_residual = (
        full_coordinate
        - binned_coordinate
        + perturbative_defect
        + contact_defect
        + hadronization_defect
    )
    declared_budget = (
        binning_bound
        + abs(perturbative_defect)
        + abs(contact_defect)
        + abs(hadronization_defect)
    )
    _assert_leq("finite-resolution observable assembly residual", abs(actual_residual), declared_budget)

    omitted_binning_budget = (
        abs(perturbative_defect)
        + abs(contact_defect)
        + abs(hadronization_defect)
    )
    assert_true(
        "omitting the detector-binning budget undercounts the measured residual",
        abs(actual_residual) > omitted_binning_budget,
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
    check_projected_contact_mass_does_not_fix_detector_bins()
    check_three_detector_moment_and_contact_ledger()
    check_endpoint_matching_delta_ledger()
    check_finite_resolution_detector_assembly_budget()
    check_connected_cumulants_do_not_remove_detector_contacts()
    print("All finite-event energy-correlator detector-algebra checks passed.")


if __name__ == "__main__":
    main()
