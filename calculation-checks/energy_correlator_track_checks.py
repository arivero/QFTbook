#!/usr/bin/env python3
"""Exact checks for track-energy correlator bookkeeping.

The script verifies finite algebra used in the QCD energy-correlator
discussion: selected calorimetric measures, track-EEC moment identities, and
the binomial moment ledger for a collinear track-function split.  It also
checks the selected endpoint-atom gluing equations, the global moment-closure
correction for a proposed measured EEC endpoint assembly, and the finite
residual budget for a measured EEC prediction.
"""

from fractions import Fraction
from math import comb

from check_utils import assert_leq as _assert_leq


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: got {actual!r}, expected {expected!r}")


def assert_true(name, condition):
    if not condition:
        raise AssertionError(name)


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def check_selected_measure_moments():
    # Three massless particles in a center-of-mass event.
    z = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    directions = [
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(-1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
    ]
    tau = [Fraction(1), Fraction(0), Fraction(1)]  # selected charged tracks

    selected_energy = sum(t * e for t, e in zip(tau, z))
    selected_momentum = tuple(
        sum(tau[r] * z[r] * directions[r][mu] for r in range(3))
        for mu in range(3)
    )

    zeroth = sum(tau[r] * tau[s] * z[r] * z[s] for r in range(3) for s in range(3))
    first = sum(
        tau[r] * tau[s] * z[r] * z[s] * dot(directions[r], directions[s])
        for r in range(3)
        for s in range(3)
    )
    contact = sum(t * t * e * e for t, e in zip(tau, z))

    assert_equal("track EEC zeroth moment", zeroth, selected_energy**2)
    assert_equal("track EEC first moment", first, dot(selected_momentum, selected_momentum))
    assert_equal("track contact weight", contact, Fraction(5, 18))


def split_moment(z, moments_j, moments_k, n):
    return sum(
        Fraction(comb(n, a))
        * z**a
        * (1 - z) ** (n - a)
        * moments_j[a]
        * moments_k[n - a]
        for a in range(n + 1)
    )


def check_track_function_split_moments():
    z = Fraction(2, 5)
    moments_j = {
        0: Fraction(1),
        1: Fraction(3, 7),
        2: Fraction(2, 9),
        3: Fraction(5, 33),
    }
    moments_k = {
        0: Fraction(1),
        1: Fraction(1, 4),
        2: Fraction(1, 10),
        3: Fraction(1, 20),
    }

    assert_equal("split zeroth moment", split_moment(z, moments_j, moments_k, 0), Fraction(1))

    expected_first = z * moments_j[1] + (1 - z) * moments_k[1]
    assert_equal("split first moment", split_moment(z, moments_j, moments_k, 1), expected_first)

    contact = z**2 * moments_j[2] + (1 - z) ** 2 * moments_k[2]
    separated = 2 * z * (1 - z) * moments_j[1] * moments_k[1]
    expected_second = contact + separated
    assert_equal("split second moment", split_moment(z, moments_j, moments_k, 2), expected_second)

    # For a full calorimeter all moments equal one, and the separated track
    # weight becomes the ordinary EEC weight 2 z (1-z).
    full = {0: Fraction(1), 1: Fraction(1), 2: Fraction(1)}
    full_separated = 2 * z * (1 - z) * full[1] * full[1]
    assert_equal("full calorimeter separated weight", full_separated, 2 * z * (1 - z))
    assert_equal("full calorimeter second moment", split_moment(z, full, full, 2), Fraction(1))


def check_selected_endpoint_atom_gluing():
    # For a selected-energy EEC, the endpoint atoms are fixed by the selected
    # zeroth and first moments, not by the full calorimetric values unless the
    # selector is tau=1.
    selected_energy_square = Fraction(17, 19)
    selected_momentum_square = Fraction(5, 23)
    open_zeroth = Fraction(2, 7)
    open_first = Fraction(-1, 11)

    contact_atom = (
        selected_energy_square
        + selected_momentum_square
        - open_zeroth
        - open_first
    ) / 2
    back_to_back_atom = (
        selected_energy_square
        - selected_momentum_square
        - open_zeroth
        + open_first
    ) / 2

    assert_equal(
        "selected EEC zeroth endpoint gluing",
        open_zeroth + contact_atom + back_to_back_atom,
        selected_energy_square,
    )
    assert_equal(
        "selected EEC first endpoint gluing",
        open_first + contact_atom - back_to_back_atom,
        selected_momentum_square,
    )

    full_contact_atom = (1 - open_zeroth - open_first) / 2
    full_back_to_back_atom = (1 - open_zeroth + open_first) / 2
    assert_equal(
        "full calorimeter atom solution is recovered",
        (
            full_contact_atom,
            full_back_to_back_atom,
        ),
        (
            Fraction(1, 2) * (1 - open_zeroth - open_first),
            Fraction(1, 2) * (1 - open_zeroth + open_first),
        ),
    )


def check_measured_eec_global_moment_closure_residual():
    selected_energy_square = Fraction(17, 19)
    selected_momentum_square = Fraction(5, 23)
    open_zeroth = Fraction(2, 7)
    open_first = Fraction(-1, 11)

    proposed_contact_atom = Fraction(3, 13)
    proposed_back_to_back_atom = Fraction(5, 17)
    zeroth_defect = selected_energy_square - (
        open_zeroth + proposed_contact_atom + proposed_back_to_back_atom
    )
    first_defect = selected_momentum_square - (
        open_first + proposed_contact_atom - proposed_back_to_back_atom
    )

    contact_correction = (zeroth_defect + first_defect) / 2
    back_to_back_correction = (zeroth_defect - first_defect) / 2
    corrected_contact_atom = proposed_contact_atom + contact_correction
    corrected_back_to_back_atom = proposed_back_to_back_atom + back_to_back_correction

    assert_equal(
        "global moment closure corrected zeroth moment",
        open_zeroth + corrected_contact_atom + corrected_back_to_back_atom,
        selected_energy_square,
    )
    assert_equal(
        "global moment closure corrected first moment",
        open_first + corrected_contact_atom - corrected_back_to_back_atom,
        selected_momentum_square,
    )

    phi_plus = Fraction(2, 5)
    phi_minus = Fraction(-3, 7)
    endpoint_correction = (
        contact_correction * phi_plus
        + back_to_back_correction * phi_minus
    )
    endpoint_bound = (
        abs(zeroth_defect + first_defect) * abs(phi_plus) / 2
        + abs(zeroth_defect - first_defect) * abs(phi_minus) / 2
    )
    _assert_leq(
        "global moment closure endpoint-test bound",
        abs(endpoint_correction),
        endpoint_bound,
    )

    zero_only_contact = proposed_contact_atom + zeroth_defect / 2
    zero_only_back_to_back = proposed_back_to_back_atom + zeroth_defect / 2
    assert_equal(
        "zeroth-only correction repairs only the zeroth moment",
        open_zeroth + zero_only_contact + zero_only_back_to_back,
        selected_energy_square,
    )
    assert_equal(
        "zeroth-only correction leaves first-moment defect",
        selected_momentum_square - (
            open_first + zero_only_contact - zero_only_back_to_back
        ),
        first_defect,
    )
    assert_true(
        "zeroth-only correction is insufficient for selected EEC closure",
        first_defect != 0,
    )

    full_contact_atom = (1 - open_zeroth - open_first) / 2
    full_back_to_back_atom = (1 - open_zeroth + open_first) / 2
    assert_true(
        "full-calorimeter atoms fail selected zeroth moment",
        open_zeroth + full_contact_atom + full_back_to_back_atom
        != selected_energy_square,
    )
    assert_true(
        "full-calorimeter atoms fail selected first moment",
        open_first + full_contact_atom - full_back_to_back_atom
        != selected_momentum_square,
    )


def check_measured_eec_residual_bound():
    # A finite detector-test residual is bounded by the sum of chart, endpoint,
    # and power/hadronization error budgets.  The signs can cancel in the
    # observable, but the stated accuracy claim uses absolute budgets.
    chart_defects = [Fraction(1, 37), Fraction(-2, 41), Fraction(3, 43)]
    endpoint_defects = {
        "plus": Fraction(-5, 47),
        "minus": Fraction(7, 53),
    }
    phi_plus = Fraction(2, 5)
    phi_minus = Fraction(-3, 7)
    power_defect = Fraction(-11, 59)

    actual_residual = (
        sum(chart_defects)
        + phi_plus * endpoint_defects["plus"]
        + phi_minus * endpoint_defects["minus"]
        + power_defect
    )
    bound = (
        sum(abs(entry) for entry in chart_defects)
        + abs(phi_plus) * abs(endpoint_defects["plus"])
        + abs(phi_minus) * abs(endpoint_defects["minus"])
        + abs(power_defect)
    )
    _assert_leq("measured EEC residual budget", abs(actual_residual), bound)


def main():
    check_selected_measure_moments()
    check_track_function_split_moments()
    check_selected_endpoint_atom_gluing()
    check_measured_eec_global_moment_closure_residual()
    check_measured_eec_residual_bound()
    print("All track energy-correlator checks passed.")


if __name__ == "__main__":
    main()
