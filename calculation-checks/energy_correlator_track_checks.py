#!/usr/bin/env python3
"""Exact checks for track-energy correlator bookkeeping.

Evidence contract:
- Target claims: selected calorimetric measures, track-EEC moment identities,
  collinear track-function split moments, measured endpoint-atom gluing,
  measured EEC moment closure, and the response/covariance contract in
  ``ca:measured-eec-response-covariance-contract``.
- Independent construction: all moments, endpoint corrections, ensemble
  covariances, and response covariances are recomputed from finite event
  samples using exact rational arithmetic rather than by substituting the
  displayed manuscript equations as black boxes.
- Imported assumptions: finite event ensembles, finite detector-test vectors,
  linear detector response, zero-mean detector noise with a declared
  conditional covariance, and the monograph's endpoint convention
  ``zeta=+1`` for coincident detectors and ``zeta=-1`` for back-to-back
  atoms.
- Negative controls: full-calorimeter endpoint atoms fail selected-energy
  moments, zeroth-only repair fails first-moment closure, mean-only endpoint
  repair misses covariance, and omitting detector noise underbudgets a
  response covariance.
- Scope boundary: these checks do not prove continuum light-ray OPE
  convergence, perturbative factorization, detector calibration, or
  nonperturbative QCD estimates; they verify the finite algebra that such
  claims must satisfy.
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


def vector_add(u, v):
    return [a + b for a, b in zip(u, v)]


def vector_sub(u, v):
    return [a - b for a, b in zip(u, v)]


def matrix_add(a, b):
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def matrix_sub(a, b):
    return [[x - y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    b_t = transpose(b)
    return [[dot(row_a, col_b) for col_b in b_t] for row_a in a]


def matvec(a, v):
    return [dot(row, v) for row in a]


def outer(u, v):
    return [[a * b for b in v] for a in u]


def zero_matrix(rows, cols):
    return [[Fraction(0) for _ in range(cols)] for _ in range(rows)]


def weighted_mean(samples, weights):
    dim = len(samples[0])
    return [
        sum(weight * sample[i] for sample, weight in zip(samples, weights))
        for i in range(dim)
    ]


def weighted_cross_covariance(samples_a, samples_b, weights):
    mean_a = weighted_mean(samples_a, weights)
    mean_b = weighted_mean(samples_b, weights)
    rows = len(mean_a)
    cols = len(mean_b)
    cov = zero_matrix(rows, cols)
    for sample_a, sample_b, weight in zip(samples_a, samples_b, weights):
        da = vector_sub(sample_a, mean_a)
        db = vector_sub(sample_b, mean_b)
        cov = matrix_add(cov, [[weight * entry for entry in row] for row in outer(da, db)])
    return cov


def weighted_covariance(samples, weights):
    return weighted_cross_covariance(samples, samples, weights)


def quadratic_form(matrix, vector):
    return dot(vector, matvec(matrix, vector))


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


def check_measured_eec_response_covariance_contract():
    # Three finite events with fluctuating selected-energy moments and
    # endpoint defects.  The first two detector tests are 1 and zeta; the third
    # is a generic smooth test with nontrivial endpoint values.
    weights = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    phi_plus = [Fraction(1), Fraction(1), Fraction(2, 5)]
    phi_minus = [Fraction(1), Fraction(-1), Fraction(-1, 3)]
    events = [
        {
            "selected_energy_square": Fraction(17, 19),
            "selected_momentum_square": Fraction(5, 23),
            "open_zeroth": Fraction(2, 7),
            "open_first": Fraction(-1, 11),
            "open_generic": Fraction(4, 29),
            "contact_atom": Fraction(3, 13),
            "back_to_back_atom": Fraction(5, 17),
        },
        {
            "selected_energy_square": Fraction(11, 13),
            "selected_momentum_square": Fraction(7, 31),
            "open_zeroth": Fraction(3, 10),
            "open_first": Fraction(1, 17),
            "open_generic": Fraction(-2, 37),
            "contact_atom": Fraction(2, 11),
            "back_to_back_atom": Fraction(1, 5),
        },
        {
            "selected_energy_square": Fraction(19, 29),
            "selected_momentum_square": Fraction(2, 19),
            "open_zeroth": Fraction(1, 4),
            "open_first": Fraction(-3, 23),
            "open_generic": Fraction(5, 41),
            "contact_atom": Fraction(1, 7),
            "back_to_back_atom": Fraction(4, 27),
        },
    ]

    proposed_vectors = []
    correction_vectors = []
    corrected_vectors = []
    for event in events:
        proposed = [
            event["open_zeroth"] + event["contact_atom"] + event["back_to_back_atom"],
            event["open_first"] + event["contact_atom"] - event["back_to_back_atom"],
            event["open_generic"]
            + event["contact_atom"] * phi_plus[2]
            + event["back_to_back_atom"] * phi_minus[2],
        ]
        zeroth_defect = event["selected_energy_square"] - proposed[0]
        first_defect = event["selected_momentum_square"] - proposed[1]
        contact_correction = (zeroth_defect + first_defect) / 2
        back_to_back_correction = (zeroth_defect - first_defect) / 2
        correction = [
            contact_correction * plus + back_to_back_correction * minus
            for plus, minus in zip(phi_plus, phi_minus)
        ]
        corrected = vector_add(proposed, correction)

        assert_equal(
            "eventwise endpoint repair fixes selected-energy moment",
            corrected[0],
            event["selected_energy_square"],
        )
        assert_equal(
            "eventwise endpoint repair fixes selected-momentum moment",
            corrected[1],
            event["selected_momentum_square"],
        )

        proposed_vectors.append(proposed)
        correction_vectors.append(correction)
        corrected_vectors.append(corrected)

    cov_proposed = weighted_covariance(proposed_vectors, weights)
    cov_correction = weighted_covariance(correction_vectors, weights)
    cov_cross_pc = weighted_cross_covariance(proposed_vectors, correction_vectors, weights)
    cov_cross_cp = weighted_cross_covariance(correction_vectors, proposed_vectors, weights)
    cov_repaired = weighted_covariance(corrected_vectors, weights)
    repaired_from_identity = matrix_add(
        matrix_add(cov_proposed, cov_cross_pc),
        matrix_add(cov_cross_cp, cov_correction),
    )
    assert_equal(
        "eventwise endpoint covariance repair identity",
        cov_repaired,
        repaired_from_identity,
    )
    assert_true(
        "mean-only endpoint repair misses covariance terms",
        cov_repaired != cov_proposed,
    )

    mean_proposed = weighted_mean(proposed_vectors, weights)
    mean_correction = weighted_mean(correction_vectors, weights)
    mean_corrected = weighted_mean(corrected_vectors, weights)
    assert_equal(
        "mean endpoint correction repairs mean vector",
        vector_add(mean_proposed, mean_correction),
        mean_corrected,
    )

    response = [
        [Fraction(3, 5), Fraction(1, 10), Fraction(1, 4)],
        [Fraction(1, 5), Fraction(2, 3), Fraction(-1, 6)],
    ]
    observed_core_vectors = [matvec(response, sample) for sample in corrected_vectors]
    mean_observed_core = weighted_mean(observed_core_vectors, weights)
    assert_equal(
        "linear detector response mean",
        mean_observed_core,
        matvec(response, mean_corrected),
    )

    cov_observed_core = weighted_covariance(observed_core_vectors, weights)
    response_covariance = matmul(matmul(response, cov_repaired), transpose(response))
    assert_equal(
        "linear detector response covariance",
        cov_observed_core,
        response_covariance,
    )

    noise_covariances = [
        [[Fraction(1, 50), Fraction(1, 200)], [Fraction(1, 200), Fraction(1, 70)]],
        [[Fraction(1, 60), Fraction(-1, 240)], [Fraction(-1, 240), Fraction(1, 80)]],
        [[Fraction(1, 90), Fraction(1, 300)], [Fraction(1, 300), Fraction(1, 100)]],
    ]
    mean_noise = zero_matrix(2, 2)
    for weight, noise in zip(weights, noise_covariances):
        mean_noise = matrix_add(
            mean_noise,
            [[weight * entry for entry in row] for row in noise],
        )
    full_detector_covariance = matrix_add(response_covariance, mean_noise)
    detector_test = [Fraction(5, 7), Fraction(-2, 3)]
    omitted_noise_residual = quadratic_form(
        matrix_sub(full_detector_covariance, response_covariance),
        detector_test,
    )
    _assert_leq(
        "detector response covariance noise budget",
        abs(omitted_noise_residual),
        quadratic_form(mean_noise, detector_test),
    )
    assert_true(
        "omitting detector noise underbudgets response covariance",
        omitted_noise_residual != 0,
    )

    mean_only_observed = matvec(response, mean_proposed)
    assert_true(
        "using unrepaired endpoint means changes detector response mean",
        mean_only_observed != mean_observed_core,
    )


def main():
    check_selected_measure_moments()
    check_track_function_split_moments()
    check_selected_endpoint_atom_gluing()
    check_measured_eec_global_moment_closure_residual()
    check_measured_eec_residual_bound()
    check_measured_eec_response_covariance_contract()
    print("All track energy-correlator checks passed.")


if __name__ == "__main__":
    main()
